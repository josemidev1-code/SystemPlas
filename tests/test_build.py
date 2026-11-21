"""Tests del HTML generado por build.py.  Ejecutar: python3 -m unittest tests/test_build.py -v"""
import glob
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def setUpModule():
    subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], check=True, cwd=ROOT)


def page(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return f.read()


class Base(unittest.TestCase):
    def has(self, needle, html):
        self.assertTrue(needle in html, f"falta: {needle}")

    def lacks(self, needle, html):
        self.assertFalse(needle in html, f"sobra: {needle}")


class FotosRecortadas(Base):
    def test_tarjeta_usa_foto_sin_fondo(self):
        self.has('src="assets/img/web/sin-fondo/eoat-3.jpg"', page("eoat-accesorio-robotica.html"))

    def test_galeria_ficha_usa_foto_sin_fondo(self):
        self.has('src="assets/img/web/sin-fondo/p/serie-mtc-b-1.jpg"', page("serie-mtc-b.html"))

    def test_sin_recorte_usa_original(self):
        html = page("index.html")
        self.has('src="assets/img/logo-320.png"', html)
        self.lacks("sin-fondo/logo", html)


class Tarjetas(Base):
    def cards(self, name):
        return re.findall(r'<a class="card card--open card--prod"[^>]*>.*?</a>', page(name), re.S)

    def text_cards(self, name):
        return re.findall(r'<a class="text-card"[^>]*>.*?</a>', page(name), re.S)

    def test_tarjeta_foto_nombre_y_una_linea(self):
        # Desde el rediseño (9243c31) la tarjeta es foto, nombre y como mucho una línea debajo
        cards = self.cards("eoat-accesorio-robotica.html")
        self.assertEqual(len(cards), 10)
        for c in cards:
            self.has('<img class="frame__img"', c)
            self.has("<h3>", c)
            self.assertLessEqual(c.count("<p>"), 1)
            self.lacks('class="tag', c)
            self.lacks('class="badge', c)

    def test_producto_sin_foto_es_tarjeta_de_texto(self):
        # Estanterías no tiene fotos: cada producto es una tarjeta de texto, sin marco de foto vacío
        html = page("estanterias-moldes.html")
        self.assertEqual(len(self.text_cards("estanterias-moldes.html")), 10)
        self.lacks('class="card card--open card--prod"', html)

    def test_producto_sin_ficha_enlaza_a_contacto(self):
        eoat = self.cards("eoat-accesorio-robotica.html")
        self.assertTrue(any('href="contacto.html?producto=' in c for c in eoat))
        self.assertTrue(all('href="contacto.html?producto=' in c for c in self.text_cards("estanterias-moldes.html")))

    def test_categoria_sin_contadores_en_pestanas(self):
        self.lacks('class="count"', page("eoat-accesorio-robotica.html"))


class Portada(Base):
    def test_portada_sin_ceja(self):
        for n in ["productos.html", "eoat-accesorio-robotica.html", "quienes-somos.html"]:
            self.lacks("hero-eyebrow", page(n))


class SinAnimacion(Base):
    def test_ninguna_pagina_usa_reveal(self):
        for f in glob.glob(os.path.join(ROOT, "*.html")):
            with open(f, encoding="utf-8") as fh:
                self.assertNotRegex(fh.read(), r'class="[^"]*\breveal\b', os.path.basename(f))

    def test_js_no_revela_contenido_al_hacer_scroll(self):
        # main.js ya no existe. Los únicos IntersectionObserver de la web propia son el de entrance.js
        # (la línea decorativa de los titulares) y el de home-motion.js (emblemas y cifras); ninguno oculta texto.
        for f in glob.glob(os.path.join(ROOT, "assets/js/*.js")):
            with open(f, encoding="utf-8") as fh:
                src = fh.read()
            if os.path.basename(f) == "reels.js":
                # vídeos EOAT: solo los pone en marcha o los pausa según estén en pantalla; no oculta texto
                self.assertNotRegex(src, r"\breveal\b")
                self.lacks("visibility", src)
            elif os.path.basename(f) == "home-motion.js":
                # portada: traza los emblemas (decorativos) y cuenta las cifras (siempre con número); no oculta texto
                self.assertNotRegex(src, r"\breveal\b")
                self.lacks("visibility", src)
            elif os.path.basename(f) == "entrance.js":
                self.has("decor-line--in", src)
                self.assertNotRegex(src, r"\breveal\b")  # la clase de aparición antigua (pagereveal no cuenta)
            else:
                self.lacks("IntersectionObserver", src)


if __name__ == "__main__":
    unittest.main()
