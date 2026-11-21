"""Tests de la decoración y la entrada.  Ejecutar: python3 -m unittest tests/test_decor.py -v"""
import glob
import os
import unittest

from test_build import ROOT, Base, page, setUpModule  # noqa: F401


class Enlaces(Base):
    def test_todas_las_paginas_enlazan_decor_y_entrada(self):
        for f in glob.glob(os.path.join(ROOT, "*.html")):
            with open(f, encoding="utf-8") as fh:
                html = fh.read()
            self.has('href="assets/css/decor.css"', html)
            self.has('src="assets/js/entrance.js"', html)


class Cabeceras(Base):
    def test_cabecera_interior_lleva_cuadricula_y_regla(self):
        html = page("contacto.html")
        self.has('<div class="decor-grid" aria-hidden="true"></div>', html)
        self.has('<div class="decor-ruler" aria-hidden="true"></div>', html)

    def test_cabecera_con_video_tambien(self):
        self.has('class="decor-grid"', page("hrs-controladores.html"))

    def test_ficha_marcada_para_entrar(self):
        self.has('<section class="pdp" data-enter>', page("serie-mtc-b.html"))

    def test_portada_no_cambia_su_entrada(self):
        self.lacks('class="decor-grid"', page("index.html"))


class Momentos(Base):
    def test_robot_se_revela(self):
        self.has('eoat-photo" data-moment="picture-develops"', page("index.html"))

    def test_empresa_se_revela(self):
        self.has('about-photo" data-moment="picture-develops"', page("quienes-somos.html"))

    def test_portada_dos_momentos_como_maximo(self):
        self.assertEqual(page("index.html").count("data-moment="), 2)

    def test_fondo_ruled_en_hrs(self):
        html = page("index.html")
        self.has('class="section bg-ruled" id="hrs"', html)
        self.has('href="assets/backgrounds/backgrounds.css"', html)
        self.has('<script src="assets/backgrounds/backgrounds.js"></script>', html)


if __name__ == "__main__":
    unittest.main()
