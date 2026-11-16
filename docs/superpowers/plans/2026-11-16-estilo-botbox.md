# Rediseño estilo Botbox — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que la web de System Plast se vea como el catálogo de Botbox: fotos limpias sobre blanco, tarjetas solo foto + nombre, portadas fotográficas con título blanco y sin animaciones que dejen huecos.

**Architecture:** Sitio estático generado por `build.py` (Python, sin dependencias) a partir de `CATS` y `data/productos.json`, con un único `assets/css/styles.css` y `assets/js/main.js`. Se cambian las plantillas de `build.py` y el CSS; los `.html` se regeneran con `python3 build.py`, nunca a mano.

**Tech Stack:** Python 3 (stdlib), HTML, CSS, JS sin librerías. Tests con `unittest` de la stdlib sobre el HTML generado.

**Spec:** `docs/superpowers/specs/2026-11-16-estilo-botbox-design.md`

## Global Constraints

- Las páginas `.html` solo cambian ejecutando `python3 build.py`.
- No se tocan textos ni datos de productos (`CATS`, `data/productos.json`) salvo quitar lo que el diseño deja de mostrar.
- Color de marca: verde `#037c75` (`--brand`), azul marino `#012c3d`. No se usa el azul de Botbox.
- Tipografía Source Sans 3 (ya cargada). Texto `#0f0f0f`, títulos 700.
- Esquinas 0–4px, sombras mínimas o ninguna.
- Tarjetas y galería de fichas con fondo **blanco puro** (`#fff`): las fotos recortadas tienen restos blancos que solo son invisibles sobre blanco.
- No se copia nada de Botbox (logo, textos, fotos, código).
- Responsive: 4 columnas escritorio, 2 en tablet y móvil; sin scroll horizontal a 375px.

## Review Focus

- Producto sin foto (`img` es `None`, p. ej. estanterías): la tarjeta debe mostrar el icono `rack`, no una `<img>` rota. → test en Task 2.
- Foto que no tiene versión recortada (p. ej. `home-1.png`, `logo.png`): debe usar la original de `assets/img/`. → test en Task 1.
- Producto sin ficha (`slug` es `None`): la tarjeta debe seguir enlazando a `contacto.html?producto=…&cat=…` para que el formulario se rellene. → test en Task 2.
- Navegador sin JavaScript: todo el contenido visible desde el principio. → test en Task 4.
- Nombres de producto largos en móvil (2 columnas a 375px): deben partir línea sin desbordar. → verificación visual en Task 5.

---

### Task 0: Rama y material ya preparado

**Files:**
- Add (ya existen, sin commit): `assets/img/sin-fondo/` (28 png), `assets/img/sin-fondo/p/` (15 png), `tools/quitar_mancha.py`, `docs/superpowers/specs/2026-11-16-estilo-botbox-design.md`, este plan.

- [ ] **Step 1: Crear rama**

Run: `git switch -c rediseno-botbox`
Expected: `Switched to a new branch 'rediseno-botbox'`

- [ ] **Step 2: Commit del material**

```bash
git add assets/img/sin-fondo tools/quitar_mancha.py docs/superpowers
git commit -m "Fotos de producto sin mancha verde, script y diseño del rediseño estilo Botbox"
```

### Task 1: Usar las fotos recortadas

**Files:**
- Modify: `build.py` (función `card`, galería de fichas ~líneas 264-299)
- Create: `tests/test_build.py`

**Interfaces:**
- Produces: `img_src(name: str) -> str` en `build.py`: devuelve `"assets/img/sin-fondo/" + name` si ese archivo existe en disco, si no `"assets/img/" + name`. `name` puede llevar subcarpeta (`"p/serie-mtc-b-1.png"`).
- Produces: `tests/test_build.py` con helper `page(name: str) -> str` que lee un `.html` generado. `setUpModule()` ejecuta `python3 build.py` una vez (vía `subprocess.run(..., check=True)`).

- [ ] **Step 1: Escribir tests que fallan**

```python
class FotosRecortadas(unittest.TestCase):
    def test_tarjeta_usa_foto_sin_fondo(self):
        self.assertIn('src="assets/img/sin-fondo/eoat-3.png"', page("eoat-accesorio-robotica.html"))
    def test_galeria_ficha_usa_foto_sin_fondo(self):
        self.assertIn('assets/img/sin-fondo/p/serie-mtc-b-1.png', page("serie-mtc-b.html"))
    def test_sin_recorte_usa_original(self):
        html = page("index.html")
        self.assertIn('src="assets/img/logo.png"', html)
        self.assertNotIn('sin-fondo/logo.png', html)
```

- [ ] **Step 2: Ejecutar y ver que fallan**

Run: `python3 -m unittest tests/test_build.py -v`
Expected: FAIL en los dos primeros (siguen apuntando a `assets/img/eoat-3.png`).

- [ ] **Step 3: Implementar `img_src` y usarlo** en `card()`, en la imagen principal de la galería y en `data-src`/`src` de las miniaturas. El logo, portadas, noticias e industrias siguen con su ruta actual.

- [ ] **Step 4: Regenerar y pasar tests**

Run: `python3 build.py && python3 -m unittest tests/test_build.py -v`
Expected: OK

- [ ] **Step 5: Commit**

```bash
git add build.py tests/test_build.py *.html
git commit -m "Las tarjetas y galerías usan las fotos sin mancha"
```

### Task 2: Tarjetas solo foto + nombre

**Files:**
- Modify: `build.py` (`card`, `product_cards`, `rel_html`, `cats_html`, `feat_html`, plantilla de categoría ~línea 332, `cat_tabs`)
- Modify: `assets/css/styles.css` (bloque "Rejilla de productos", `.cat-tabs`, `.tag`, `.badge`)
- Test: `tests/test_build.py`

**Interfaces:**
- Consumes: `img_src` (Task 1).
- Produces: `card(title: str, img: str | None, href: str) -> str` → `<a class="product-card" href="…"><div class="thumb"><img …> o icono rack</div><h3>título</h3></a>`. Se eliminan los parámetros `desc`, `tag`, `tag_muted`, `badge` y todas las llamadas se adaptan.

- [ ] **Step 1: Tests que fallan**

```python
class Tarjetas(unittest.TestCase):
    def cards(self, name):
        return re.findall(r'<a class="product-card[^"]*"[^>]*>.*?</a>', page(name), re.S)
    def test_tarjeta_solo_foto_y_nombre(self):
        for c in self.cards("eoat-accesorio-robotica.html"):
            self.assertNotIn("<p>", c); self.assertNotIn('class="tag', c); self.assertNotIn('class="badge', c)
    def test_producto_sin_foto_muestra_icono(self):
        self.assertTrue(any("thumb-placeholder" in c for c in self.cards("estanterias-moldes.html")))
    def test_producto_sin_ficha_enlaza_a_contacto(self):
        self.assertTrue(any('href="contacto.html?producto=' in c for c in self.cards("estanterias-moldes.html")))
    def test_categoria_sin_contadores_en_pestanas(self):
        self.assertNotIn('class="count"', page("eoat-accesorio-robotica.html"))
```

(Comprobado: los 9 productos de `estanterias-moldes` tienen `img = None` y `slug = None`.)

- [ ] **Step 2: Ejecutar y ver que fallan**

Run: `python3 -m unittest tests/test_build.py -v` → FAIL en `Tarjetas`.

- [ ] **Step 3: Implementar.** Nueva firma de `card`. En la plantilla de categoría se quita el `section-head` ("¿Qué producto necesitas?") y la sección pasa de `section section--grey` a `section` (fondo blanco). `cat_tabs` sin `<span class="count">`. CSS de tarjeta:
  - `.product-grid`: 4 columnas, `gap: 40px 30px`.
  - `.thumb`: fondo `#fff`, sin sombra ni borde redondeado, `aspect-ratio: 4/3`, foto `object-fit: contain` ocupando ~90%.
  - `h3`: 18px, peso 600, color `#0f0f0f`, centrado, `margin-top: 14px`, `overflow-wrap: anywhere`.
  - Hover: `img` `scale(1.04)` y `h3` en `var(--brand)`; nada más.
  - `.cat-tabs`: fondo blanco, texto 15px, solo subrayado verde en la activa; borrar reglas de `.tag`, `.badge`, `.count`.

- [ ] **Step 4: Regenerar y pasar tests**

Run: `python3 build.py && python3 -m unittest tests/test_build.py -v` → OK

- [ ] **Step 5: Commit**

```bash
git add build.py assets/css/styles.css tests/test_build.py *.html
git commit -m "Tarjetas de producto estilo catálogo: solo foto y nombre"
```

### Task 3: Portada fotográfica con título blanco

**Files:**
- Modify: `build.py` (`hero` y sus 6 llamadas)
- Modify: `assets/css/styles.css` (bloque "Hero" y media queries de `.hero`)
- Test: `tests/test_build.py`

**Interfaces:**
- Produces: `hero(title: str, sub: str, compact: bool = False) -> str` (se elimina `eyebrow`). Marcado: `<section class="hero"> <div class="container"><h1>…</h1><p>…</p></div></section>`.

- [ ] **Step 1: Test que falla**

```python
class Portada(unittest.TestCase):
    def test_portada_sin_ceja(self):
        for n in ["productos.html", "eoat-accesorio-robotica.html", "quienes-somos.html"]:
            self.assertNotIn("hero-eyebrow", page(n))
```

(La portada de `index.html` es plantilla propia, `hero--home`; conserva su ceja y botón.)

- [ ] **Step 2: Ejecutar y ver que falla** → FAIL.

- [ ] **Step 3: Implementar.** CSS `.hero`: `min-height: 440px` (300px por debajo de 600px; `.hero--compact` 300px / 220px), capa `linear-gradient(180deg, rgba(1,44,61,.55), rgba(1,44,61,.70))`, sin `border-bottom`. `h1`: blanco, 700, mayúsculas, `clamp(28px, 4vw, 45px)`. `p`: blanco, 600, 18px. Sombra de texto suave para legibilidad.

- [ ] **Step 4: Regenerar y pasar tests** → OK.

- [ ] **Step 5: Commit**

```bash
git add build.py assets/css/styles.css tests/test_build.py *.html
git commit -m "Portadas con foto y título blanco"
```

### Task 4: Quitar la animación de aparición

**Files:**
- Modify: `build.py` (todas las apariciones de la clase `reveal`)
- Modify: `assets/js/main.js` (bloque "Aparición al hacer scroll")
- Modify: `assets/css/styles.css` (reglas `.reveal`, ~líneas 205-207)
- Test: `tests/test_build.py`

- [ ] **Step 1: Tests que fallan**

```python
class SinAnimacion(unittest.TestCase):
    def test_ninguna_pagina_usa_reveal(self):
        for f in glob.glob(os.path.join(ROOT, "*.html")):
            self.assertNotRegex(open(f, encoding="utf-8").read(), r'class="[^"]*\breveal\b', f)
    def test_js_sin_observer(self):
        self.assertNotIn("IntersectionObserver", open(os.path.join(ROOT, "assets/js/main.js")).read())
```

- [ ] **Step 2: Ejecutar y ver que fallan** → FAIL.

- [ ] **Step 3: Implementar.** Quitar ` reveal` de todos los atributos `class` en `build.py` (dejando el resto de clases), borrar el bloque JS y las reglas CSS `.reveal`. Mantener la regla `prefers-reduced-motion` solo para `scroll-behavior`.

- [ ] **Step 4: Regenerar y pasar tests** → OK.

- [ ] **Step 5: Commit**

```bash
git add build.py assets/js/main.js assets/css/styles.css tests/test_build.py *.html
git commit -m "Sin animación de aparición: el contenido se ve desde el principio"
```

### Task 5: Estilo global y resto de páginas

**Files:**
- Modify: `assets/css/styles.css` (`:root`, `body`, `.btn`, `.band`, `.cta`, `.gallery-main`, `.thumbs`, `.footer`, ficha `.pdp*`, inicio)

- [ ] **Step 1: Ajustar tokens.** `--text: #0f0f0f`, `--heading: #0f0f0f`, `--radius: 4px`, `--shadow: none`; `body` 16px. Títulos `h1–h3` peso 700.

- [ ] **Step 2: Franjas.** `.band` (verde): título blanco ~24px 600, párrafo blanco, botón contorno blanco en mayúsculas 13–14px con letra espaciada y padding ancho, como "SOLICITAR CATÁLOGO DE PRODUCTOS". `.cta`: foto + capa verde/marino, título blanco grande, botón.

- [ ] **Step 3: Fichas.** `.gallery-main` y `.thumbs button` con fondo `#fff`, borde fino `#e6e7eb` en vez de sombra, radio 4px. Botones de presupuesto con radio 4px.

- [ ] **Step 4: Inicio y resto.** Reestilar `trust`, `feature`, `why`, `news-card` y pie con los mismos tokens (sin sombras, radios 4px). Sin cambios de contenido.

- [ ] **Step 5: Regenerar y pasar tests**

Run: `python3 build.py && python3 -m unittest tests/test_build.py -v` → OK

- [ ] **Step 6: Verificación visual.** Servir con `python3 -m http.server 8000` (vía `.claude/launch.json`) y en el navegador:
  - `eoat-accesorio-robotica.html` a 1440px junto a https://botboxiberica.es/productos-crg-componentes: mismo esquema (portada → cuadrícula 4 col → franja → cierre).
  - Las 7 páginas principales + 2 fichas a 1440px y 375px: sin tarjetas vacías, sin errores en consola, `document.documentElement.scrollWidth <= innerWidth` a 375px, nombres largos partiendo línea.
  - Capturas de ambas anchuras para el cliente.

- [ ] **Step 7: Commit**

```bash
git add assets/css/styles.css *.html
git commit -m "Estilo global estilo catálogo en todas las páginas"
```
