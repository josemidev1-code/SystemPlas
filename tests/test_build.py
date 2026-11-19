"""Tests del HTML generado por build.py.  Ejecutar: python3 -m unittest tests/test_build.py -v"""
import glob
import html as H
import importlib.util
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def setUpModule():
    subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], check=True, cwd=ROOT, capture_output=True)


def page(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return f.read()


def cats():
    """CATS tal como lo define build.py (se lee el módulo sin regenerar la web dos veces)."""
    with open(os.path.join(ROOT, "build.py"), encoding="utf-8") as fh:
        src = fh.read()
    start = src.index("CATS = [")
    end = src.index("\nNAV = ")
    ns = {}
    exec(src[start:end], ns)
    return ns["CATS"]


class Base(unittest.TestCase):
    def has(self, needle, html):
        self.assertTrue(needle in html, f"falta: {needle}")

    def lacks(self, needle, html):
        self.assertFalse(needle in html, f"sobra: {needle}")


class FotosRecortadas(Base):
    def test_tarjeta_usa_foto_ligera(self):
        self.has('assets/img/web/sin-fondo/eoat-3.jpg', page("eoat-accesorio-robotica.html"))

    def test_galeria_ficha_usa_foto_sin_fondo(self):
        self.has("sin-fondo/p/serie-mtc-b-1", page("serie-mtc-b.html"))


class Categorias(Base):
    def test_producto_sin_ficha_enlaza_a_contacto(self):
        self.has('href="contacto.html?producto=', page("estanterias-moldes.html"))

    def test_todas_las_fichas_se_generan(self):
        import json
        with open(os.path.join(ROOT, "data/productos.json"), encoding="utf-8") as fh:
            fichas = json.load(fh)
        for slug in fichas:
            self.assertTrue(os.path.exists(os.path.join(ROOT, f"{slug}.html")), slug)


class PortadaCatalogo(Base):
    """Requisito del cliente: TODOS los productos en la portada, EOAT primero."""

    def setUp(self):
        self.html = page("index.html")
        self.cards = re.findall(r'<(?:article|li)\b[^>]*\bdata-product="([^"]*)"[^>]*>(.*?)</(?:article|li)>', self.html, re.S)

    def test_portada_muestra_todos_los_productos(self):
        expected = [it[0] for c in cats() for it in c["items"]]
        self.assertEqual(len(expected), 36)
        shown = [H.unescape(n) for n, _ in self.cards]
        self.assertEqual(sorted(shown), sorted(expected))

    def test_enlaces_de_portada_resuelven(self):
        for name, body in self.cards:
            hrefs = re.findall(r'href="([^"]+)"', body)
            self.assertTrue(hrefs, f"{name} sin enlace")
            for h in hrefs:
                h = H.unescape(h)
                if h.startswith("contacto.html?producto="):
                    continue
                self.assertTrue(h.endswith(".html") and os.path.exists(os.path.join(ROOT, h)), f"{name}: {h}")
                self.assertNotIn("None", h)

    def test_ficha_enlazada_es_la_del_producto(self):
        for c in cats():
            for name, img, slug, line in c["items"]:
                if slug:
                    body = dict((H.unescape(n), b) for n, b in self.cards)[name]
                    self.has(f'href="{slug}.html"', body)

    def test_presupuesto_preselecciona_producto_y_linea(self):
        """Los enlaces a contacto llevan el nombre exacto del producto y una línea que existe en el formulario."""
        from urllib.parse import urlsplit, parse_qs
        options = set(H.unescape(o) for o in re.findall(r"<option>([^<]+)</option>", page("contacto.html")))
        checked = 0
        for name, body in self.cards:
            for h in re.findall(r'href="(contacto\.html\?[^"]+)"', body):
                q = parse_qs(urlsplit(H.unescape(h)).query)
                self.assertEqual(q["producto"], [H.unescape(name)], h)
                self.assertIn(q["cat"][0], options, h)
                checked += 1
        self.assertGreaterEqual(checked, 20)  # 15 productos sin ficha + «Pedir presupuesto» de las 5 EOAT con ficha

    def test_eoat_es_la_primera_linea(self):
        order = [self.html.index(f'id="{i}"') for i in ("eoat", "hrs", "resistencias", "estanterias", "servicio")]
        self.assertEqual(order, sorted(order))

    def test_anclas_del_indice_existen(self):
        index = re.search(r'<nav class="cat-index".*?</nav>', self.html, re.S).group(0)
        anchors = re.findall(r'href="#([^"]+)"', index)
        self.assertGreaterEqual(len(anchors), 4)
        for a in anchors:
            self.has(f'id="{a}"', self.html)

    def test_sin_imagenes_none(self):
        self.lacks("None", self.html)

    def test_imagenes_de_catalogo_ligeras_y_diferidas(self):
        for _, body in self.cards:
            for tag in re.findall(r"<img\b[^>]*>", body):
                self.has('loading="lazy"', tag)
                self.has("width=", tag)
                self.assertNotRegex(tag, r'src="assets/img/[^"]+\.png"')

    def test_video_y_pausa_se_conservan(self):
        self.has("data-video-pause", self.html)
        self.has("maquina-640.mp4", self.html)


class EntradasAccesibles(Base):
    """Las entradas al hacer scroll nunca esconden contenido sin JS ni con movimiento reducido."""

    def setUp(self):
        with open(os.path.join(ROOT, "assets/css/site.css"), encoding="utf-8") as fh:
            self.css = fh.read()
        with open(os.path.join(ROOT, "assets/js/site.js"), encoding="utf-8") as fh:
            self.js = fh.read()

    @staticmethod
    def top_level(selector):
        """Parte una lista de selectores por sus comas de primer nivel (no las de :is(...))."""
        parts, depth, cur = [], 0, ""
        for ch in selector:
            depth += ch == "("
            depth -= ch == ")"
            if ch == "," and depth == 0:
                parts.append(cur)
                cur = ""
            else:
                cur += ch
        return parts + [cur]

    def test_css_solo_oculta_bajo_rv_on_y_movimiento_permitido(self):
        start = self.css.index("ENTRANCES ON SCROLL")
        block = self.css[start:]
        for sel in re.findall(r"([^{}]*\[data-rv[^{}]*)\{", block):
            for part in self.top_level(sel):
                if "[data-rv" in part:
                    self.assertIn(".rv-on", part, part.strip())
        self.assertNotIn("[data-rv", self.css[:start])
        for media in re.findall(r"@media[^{]*\{", block):
            self.assertIn("prefers-reduced-motion: no-preference", media)

    def test_js_respeta_movimiento_reducido_y_foco(self):
        self.has("prefers-reduced-motion: reduce", self.js)
        self.has("'focusin'", self.js)
        self.has("classList.add('rv-on')", self.js)

    def test_fichas_sin_entradas(self):
        self.lacks("data-rv", page("serie-mtc-b.html"))


class Reproducible(Base):
    def test_dos_ejecuciones_mismo_resultado(self):
        before = {f: page(os.path.basename(f)) for f in glob.glob(os.path.join(ROOT, "*.html"))}
        subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], check=True, cwd=ROOT, capture_output=True)
        for f, html in before.items():
            self.assertEqual(html, page(os.path.basename(f)), os.path.basename(f))


if __name__ == "__main__":
    unittest.main()
