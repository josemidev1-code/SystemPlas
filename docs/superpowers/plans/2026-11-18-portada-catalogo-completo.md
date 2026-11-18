# Portada con el catálogo completo — plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Steps use `- [ ]`.

**Goal:** La portada (`index.html`) muestra los 36 productos de `CATS`, con EOAT como sección estrella.

**Architecture:** `build.py` gana funciones de tarjeta por variante (`eoat_card`, `hrs_row`, `res_tile`,
`shelf_item`) y una función `home_catalog()`; todo sale de `CATS` + `FICHAS`. CSS nuevo en
`assets/css/site.css` (bloque "home catalogue"); JS mínimo en `assets/js/site.js` (índice activo).

**Tech Stack:** Python 3 (stdlib), HTML/CSS/JS estático, GitHub Pages. Tests `unittest`.

**Spec:** `docs/superpowers/specs/2026-11-18-portada-catalogo-completo-design.md`

## Global Constraints

- Colores `#012c3d` / `#037c75`, IBM Plex Sans, `data-radius="sharp"`; sin dependencias nuevas.
- URLs y fichas existentes intactas; formulario y su preselección `?producto=&cat=` intactos.
- Nada de productos, cifras ni certificaciones inventadas: sólo textos ya presentes en `CATS`/`FICHAS`/build.py.
- No editar archivos del kit (`assets/system.css`, `assets/layout/*`, `assets/motion/*`, `assets/moments/*`).

## Review Focus

- Producto sin ficha (`slug=None`): debe enlazar a `contacto.html?producto=…&cat=…`, no a `None.html`.
- Producto sin imagen (estanterías): no debe generar `<img src="assets/img/None">`.
- Nombres con paréntesis/acentos en la query: deben ir codificados (`quote`).
- Anclas del índice: cada `href="#…"` debe existir como `id` en la página.
- 320px: ninguna tarjeta ni el índice pegajoso provoca scroll horizontal.

---

### Task 1: Tests que fijan el catálogo completo en portada

**Files:** Modify `tests/test_build.py` (reescribir las clases obsoletas que buscan `product-card`).

- [ ] Test `test_portada_muestra_todos_los_productos`: cada nombre de `CATS[*]["items"]` aparece
      dentro de un elemento `data-product` en `index.html`; `len(re.findall('data-product=', html)) == 36`.
- [ ] Test `test_enlaces_de_portada_resuelven`: cada `href` de un `data-product` es un `.html` existente
      o empieza por `contacto.html?producto=`.
- [ ] Test `test_eoat_primera_linea`: la sección `id="eoat"` aparece antes que `id="hrs"`.
- [ ] Test `test_anclas_del_indice_existen`, `test_sin_imagen_none`.
- [ ] Ejecutar: FAIL. Actualizar tests obsoletos a la marca actual (`card--prod`).

### Task 2: Generador de la portada

**Files:** Modify `build.py` (bloque "Inicio"), `footer()` acepta `closing=` opcional.

- [ ] `prod_href(item, cat) -> str`; `pic(img, alt, sizes) -> str` (srcset 360/700, lazy, width/height).
- [ ] Secciones: `#catalogo` (índice), `#eoat`, `#hrs`, `#resistencias`, `#estanterias`, `#servicio`; cierre de contacto.
- [ ] `python3 build.py && python3 -m unittest tests/test_build.py` → PASS.

### Task 3: Estilos y comportamiento

**Files:** Modify `assets/css/site.css`, `assets/js/site.js`.

- [ ] CSS de las cuatro composiciones, índice pegajoso, pausa del vídeo en móvil, secciones de catálogo con altura según contenido.
- [ ] JS: marcar `aria-current` en el índice según la sección visible (IntersectionObserver).

### Task 4: Auditoría visual y QA

- [ ] Capturas 1440/1024/768/390/320; crítica (impeccable); corregir.
- [ ] taste-skill: copy-lint, perf, gate; waivers justificados.
- [ ] Navegador: consola, red, enlaces, formulario con `?producto=`, vídeo y pausa.
- [ ] Commit en la rama; sin push ni merge.
