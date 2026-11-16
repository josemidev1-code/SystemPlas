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
        self.has('src="assets/img/sin-fondo/eoat-3.png"', page("eoat-accesorio-robotica.html"))

    def test_galeria_ficha_usa_foto_sin_fondo(self):
        self.has("assets/img/sin-fondo/p/serie-mtc-b-1.png", page("serie-mtc-b.html"))

    def test_sin_recorte_usa_original(self):
        html = page("index.html")
        self.has('src="assets/img/logo.png"', html)
        self.lacks("sin-fondo/logo.png", html)


class Tarjetas(Base):
    def cards(self, name):
        return re.findall(r'<a class="product-card[^"]*"[^>]*>.*?</a>', page(name), re.S)

    def test_tarjeta_solo_foto_y_nombre(self):
        cards = self.cards("eoat-accesorio-robotica.html")
        self.assertEqual(len(cards), 10)
        for c in cards:
            self.lacks("<p>", c)
            self.lacks('class="tag', c)
            self.lacks('class="badge', c)

    def test_producto_sin_foto_muestra_icono(self):
        self.assertTrue(any("thumb-placeholder" in c for c in self.cards("estanterias-moldes.html")))

    def test_producto_sin_ficha_enlaza_a_contacto(self):
        self.assertTrue(any('href="contacto.html?producto=' in c for c in self.cards("estanterias-moldes.html")))

    def test_categoria_sin_contadores_en_pestanas(self):
        self.lacks('class="count"', page("eoat-accesorio-robotica.html"))


class Portada(Base):
    def test_portada_sin_ceja(self):
        for n in ["productos.html", "eoat-accesorio-robotica.html", "quienes-somos.html"]:
            self.lacks("hero-eyebrow", page(n))


if __name__ == "__main__":
    unittest.main()
