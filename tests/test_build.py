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


if __name__ == "__main__":
    unittest.main()
