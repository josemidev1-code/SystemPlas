"""Tests de la página de accesorios en 3D (catalogo-3d.html) y de sus datos.

Ejecutar: python3 -m unittest tests/test_catalogo3d.py -v
Los GLB de accesorios pueden faltar todavía: entonces se comprueba que la página no los pida.
"""
import json
import os
import re
import struct
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "data", "accesorios3d.json")
MAX_ACC_BYTES = 1_500_000
MAX_MACHINE_BYTES = 1_000_000


def setUpModule():
    subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], check=True, cwd=ROOT, stdout=subprocess.DEVNULL)


def read(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return f.read()


def glb_json(path):
    """Devuelve el bloque JSON de un .glb (cabecera glTF 2.0 + primer chunk JSON)."""
    with open(path, "rb") as f:
        magic, version, _length = struct.unpack("<4sII", f.read(12))
        assert magic == b"glTF" and version == 2, f"{path}: no es GLB 2.0"
        chunk_len, chunk_type = struct.unpack("<II", f.read(8))
        assert chunk_type == 0x4E4F534A, f"{path}: primer chunk no es JSON"
        return json.loads(f.read(chunk_len))


def page_data():
    html = read("catalogo-3d.html")
    m = re.search(r'<script type="application/json" id="cat3d-data">(.*?)</script>', html, re.S)
    return html, json.loads(m.group(1))


class Pagina(unittest.TestCase):
    def test_importmap_antes_de_cualquier_modulo(self):
        html = read("catalogo-3d.html")
        imap = html.index('<script type="importmap">')
        first_module = html.index('<script type="module"')
        self.assertLess(imap, first_module, "el importmap debe ir antes del primer módulo")

    def test_importmap_usa_rutas_relativas_a_la_copia_local(self):
        html = read("catalogo-3d.html")
        imap = json.loads(re.search(r'<script type="importmap">(.*?)</script>', html, re.S).group(1))["imports"]
        for spec, path in imap.items():
            self.assertTrue(path.startswith("./assets/vendor/three-"), f"{spec} -> {path}")
            self.assertNotIn("http", path)
        self.assertTrue(os.path.isfile(os.path.join(ROOT, imap["three"])))
        for addon in ("loaders/GLTFLoader.js", "controls/OrbitControls.js", "environments/RoomEnvironment.js",
                      "libs/meshopt_decoder.module.js", "utils/BufferGeometryUtils.js"):
            self.assertTrue(os.path.isfile(os.path.join(ROOT, imap["three/addons/"], addon)), addon)

    def test_carga_el_modulo_y_tiene_imagen_fija(self):
        html, data = page_data()
        self.assertIn('<script type="module" src="assets/js/catalogo3d.js">', html)
        self.assertTrue(os.path.isfile(os.path.join(ROOT, "assets/js/catalogo3d.js")))
        self.assertTrue(os.path.isfile(os.path.join(ROOT, data["maquina"]["poster"])), "falta el póster")
        self.assertIn(f'src="{data["maquina"]["poster"]}"', html)

    def test_lista_accesible_con_un_boton_por_accesorio(self):
        html, data = page_data()
        ids = re.findall(r'<button class="cat3d__item" type="button" data-cat3d-item="([^"]+)" aria-pressed="false">', html)
        self.assertEqual(ids, [a["id"] for a in data["accesorios"]])
        self.assertIn('role="status"', html)
        self.assertIn("La inyectora y el robot son ilustrativos", html)

    def test_enlazada_desde_productos_y_en_sitemap(self):
        self.assertIn('href="catalogo-3d.html"', read("productos.html"))
        self.assertIn("catalogo-3d.html", read("sitemap.xml"))


class Datos(unittest.TestCase):
    def setUp(self):
        self.html, self.data = page_data()
        self.machine = os.path.join(ROOT, self.data["maquina"]["glb"])

    def test_maquina_existe_y_cabe_en_el_presupuesto(self):
        self.assertTrue(os.path.isfile(self.machine))
        self.assertLessEqual(os.path.getsize(self.machine), MAX_MACHINE_BYTES)

    def test_cada_montaje_existe_en_la_maquina(self):
        names = {n.get("name") for n in glb_json(self.machine)["nodes"]}
        for acc in self.data["accesorios"]:
            for m in acc["montajes"]:
                self.assertIn(m, names, f"{acc['id']}: nodo {m} no está en el GLB")
        self.assertIn("RUTA_CABLE_HRS", names)

    def test_vistas_y_ajustes_completos(self):
        for acc in self.data["accesorios"]:
            self.assertIn(acc["vista"], self.data["vistas"])
            aj = acc["ajuste"]
            self.assertIn(aj["tipo"], ("anillo", "caja"))
            self.assertEqual(len(aj["caja"]), 3)
            self.assertTrue(all(0 < v < 1.2 for v in aj["caja"]), f"{acc['id']}: caja en metros")
            if aj["tipo"] == "anillo":
                self.assertLess(aj["diametro_int"], aj["caja"][1])

    def test_variantes_enlazan_a_paginas_existentes(self):
        for acc in self.data["accesorios"]:
            self.assertTrue(acc["variantes"])
            for v in acc["variantes"]:
                self.assertTrue(os.path.isfile(os.path.join(ROOT, v["url"])), v["url"])
                self.assertTrue(v["presupuesto"].startswith("contacto.html?producto="))
                self.assertTrue(v["texto"] and v["enlace"] and v["nombre"])

    def test_disponible_coincide_con_el_archivo(self):
        """Sin GLB, la página no lo pide (disponible=false); con GLB, lo carga."""
        for acc in self.data["accesorios"]:
            for v in acc["variantes"]:
                self.assertEqual(v["disponible"], os.path.isfile(os.path.join(ROOT, v["glb"])), v["glb"])

    def test_validado_exige_archivo(self):
        """Un accesorio marcado como validado debe tener su GLB; sin validar no se monta aunque exista."""
        for acc in self.data["accesorios"]:
            for v in acc["variantes"]:
                self.assertIsInstance(v["validado"], bool)
                if v["validado"]:
                    self.assertTrue(v["disponible"], f"{v['glb']} marcado como validado pero no existe")

    def test_la_pagina_no_ajusta_modelos_por_heuristica(self):
        with open(os.path.join(ROOT, "assets/js/catalogo3d.js"), encoding="utf-8") as f:
            src = f.read()
        self.assertIn("variant.disponible && variant.validado", src)
        self.assertNotIn("multiplyScalar(s)", src)

    def test_glb_de_accesorios_presentes_son_validos_y_ligeros(self):
        for acc in self.data["accesorios"]:
            for v in acc["variantes"]:
                path = os.path.join(ROOT, v["glb"])
                if not os.path.isfile(path):
                    continue
                self.assertLessEqual(os.path.getsize(path), MAX_ACC_BYTES, f"{v['glb']} pesa demasiado")
                j = glb_json(path)
                self.assertTrue(j.get("meshes"), f"{v['glb']} sin mallas")
                used = set(j.get("extensionsRequired", []))
                self.assertTrue(used <= {"EXT_meshopt_compression", "KHR_mesh_quantization", "KHR_texture_transform"},
                                f"{v['glb']} requiere extensiones no cargadas: {used}")

    def test_manifiesto_y_pagina_coinciden(self):
        with open(MANIFEST, encoding="utf-8") as f:
            man = json.load(f)
        self.assertEqual([a["id"] for a in man["accesorios"]], [a["id"] for a in self.data["accesorios"]])


if __name__ == "__main__":
    unittest.main()
