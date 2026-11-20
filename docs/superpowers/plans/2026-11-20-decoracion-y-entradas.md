# Decoración y entradas: plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dar a la web de System Plast decoración propia con los colores de la marca (estilo plano técnico) y una entrada animada en todas las páginas, sin cambiar textos ni estructura.

**Architecture:** Dos archivos nuevos y focalizados: `assets/css/decor.css` (toda la decoración y los estados de entrada) y `assets/js/entrance.js` (la entrada de las páginas interiores y el trazo de los titulares). `build.py` los enlaza en el `<head>` de todas las páginas, marca las cabeceras y fichas con `data-enter` y reparte los dos momentos `picture-develops` y el fondo `bg-ruled` del kit. La portada conserva su entrada (`motion.js`, `.hero[data-enter]`), que no se toca.

**Tech Stack:** HTML estático generado con Python (`build.py`), CSS y JS (módulos ES) sin librerías; kit taste-skill (`assets/motion`, `assets/moments`, `assets/backgrounds`); pruebas con `unittest` de Python sobre el HTML generado.

**Spec:** `docs/superpowers/specs/2026-11-20-decoracion-y-entradas-design.md`

## Global Constraints

- Colores: verde petróleo `#037c75` (`var(--action)`) y azul marino `#012c3d` (`var(--ink)`); ningún color nuevo fuera de mezclas de estos con el fondo.
- Entrada al cargar: una vez, **1,1 s como máximo** en total; solo `transform`, `opacity`, `clip-path` y `filter`.
- Ningún texto queda oculto esperando al scroll. Solo se oculta lo que la entrada va a mostrar, únicamente bajo `html.m-enter:not(.m-enter-done)` (la marca de seguridad de 700 ms ya presente en todas las páginas).
- `prefers-reduced-motion: reduce` y sin JavaScript: la decoración se ve, y las entradas y los momentos muestran su estado final al instante.
- Máximo dos fondos del kit por página y como mucho dos momentos por página (la portada ya tiene `line-carries-colour`).
- Sin halos de color, sin degradados en el texto, sin cristal ni `backdrop-filter`.
- Mismos textos, secciones y orden: solo cambian clases, atributos y estilos.

## Review Focus

1. **Volver atrás desde el historial (bfcache):** la página restaurada no debe volver a esconder ni repetir la entrada. Se cubre en la tarea 3 (comprobación de `pageshow` con `persisted`).
2. **Móvil de 375 px:** la cuadrícula, la regla y las marcas de esquina no desbordan en horizontal (`scrollWidth === innerWidth`). Se cubre en la tarea 5.
3. **Reducir movimiento:** sin animación de entrada, titulares completos al instante y momentos en su estado final. Se cubre en las tareas 3 y 5.
4. **Entrada a la vez que la transición entre páginas:** al llegar desde otra página, la entrada se ve una vez y sin parpadeo, porque `pagereveal` y la entrada conviven. Se cubre en la tarea 5.
5. **Cabecera fuera de pantalla al cargar** (un enlace con `#ancla` o el scroll restaurado): la entrada se salta y todo queda visible. Se cubre en la tarea 3.

---

### Task 1: Pruebas del HTML y enlaces de los archivos nuevos

**Files:**
- Create: `tests/test_decor.py`
- Create: `assets/css/decor.css` (vacío, con su comentario de cabecera)
- Create: `assets/js/entrance.js` (vacío, con su comentario de cabecera)
- Modify: `build.py`: `head()`, `page_head()` y la plantilla de la ficha (línea ~546, `<section class="pdp">`)

**Interfaces:**
- Produces: todas las páginas enlazan `<link rel="stylesheet" href="assets/css/decor.css">` (después de `site.css`) y `<script type="module" src="assets/js/entrance.js"></script>`; la ficha abre con `<section class="pdp" data-enter>`; `page_head()` añade a su `<header>` un hijo decorativo `<div class="decor-grid" aria-hidden="true"></div>` y una regla `<div class="decor-ruler" aria-hidden="true"></div>` como últimos hijos.

- [ ] **Step 1: Escribir `tests/test_decor.py`** (mismo patrón que `tests/test_build.py`: `setUpModule` ejecuta `build.py`, helpers `has`/`lacks`)

```python
class Enlaces(Base):
    def test_todas_las_paginas_enlazan_decor_y_entrada(self):
        for f in glob.glob(os.path.join(ROOT, "*.html")):
            html = open(f, encoding="utf-8").read()
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
```

- [ ] **Step 2: Ejecutar y ver que falla**

Run: `python3 -m unittest tests/test_decor.py -v`
Expected: FAIL en las 4 primeras (falta `decor.css`, `decor-grid` y `data-enter` en la ficha); la última pasa.

- [ ] **Step 3: Enlazar los archivos en `head()`, añadir los dos `div` decorativos en las dos ramas de `page_head()` y `data-enter` en la `<section class="pdp">`**

- [ ] **Step 4: Ejecutar y ver que pasa**

Run: `python3 -m unittest tests/test_decor.py -v`
Expected: 5 OK. Luego `python3 -m unittest discover -s tests`: siguen los mismos 6 fallos y 1 error que ya existían antes (`FAILED (failures=6, errors=1)`), ninguno nuevo.

- [ ] **Step 5: Commit**

```bash
git add tests/test_decor.py assets/css/decor.css assets/js/entrance.js build.py *.html
git commit -m "Enlazar decoración y entrada en todas las páginas"
```

### Task 2: Decoración de plano técnico (`decor.css`)

**Files:**
- Modify: `assets/css/decor.css`

**Interfaces:**
- Consumes: `.decor-grid` y `.decor-ruler` (tarea 1); `.panel--white`, `.gallery-main` y `footer.closing` (ya existen).
- Produces: las clases de estado `.is-in` (en `.pg-head` y `.pdp`) y `.decor-line--in` (en titulares), que usa la tarea 3; la variable `--decor-c: var(--action)` en `:root`.

- [ ] **Step 1: Cuadrícula de cabecera.** `.decor-grid` va en posición absoluta, cubre la cabecera, `pointer-events: none` y `z-index: 0` (el `.wrap` ya tiene `z-index: 1`). Líneas de 1 px con `repeating-linear-gradient` cada 48 px en ambos ejes, color `color-mix(in oklab, var(--decor-c) 14%, transparent)`. Una `mask-image` en degradado lineal la hace visible a la derecha y la funde hacia el texto (`to left, #000 30%, transparent 75%`). En `.ground-inverse` usa `color-mix(in oklab, #fff 10%, transparent)`. En `.pg-head--video` se queda en el 55 % izquierdo con el 8 % de opacidad del color. Se dibuja al entrar: en reposo `clip-path: inset(0)`; bajo `html.m-enter:not(.m-enter-done) .pg-head[data-enter]:not(.is-in)` vale `clip-path: inset(0 0 0 100%)`, con una transición de `clip-path` de 900 ms y `cubic-bezier(.22,1,.36,1)`.
- [ ] **Step 2: Regla de medida.** `.decor-ruler` va abajo del todo de la cabecera, 10 px de alto, con marcas de 1 px cada 12 px y una marca larga (10 px) cada 60 px (dos `repeating-linear-gradient` superpuestos), en el color de la cuadrícula. Entra con `scale: 0 1` y `transform-origin: left`, 700 ms con 150 ms de retraso, bajo la misma condición que la cuadrícula.
- [ ] **Step 3: Marcas de esquina en las fotos.** En `.card--prod > .panel--white` y `.gallery-main`, un `::after` con `inset: 10px` y cuatro esquinas en L de 14×14 px y 1,5 px de grosor, dibujadas con 8 `linear-gradient` como `background` y `background-repeat: no-repeat`. Color al 35 % de `--decor-c`. Con `(hover: hover) and (pointer: fine)`, en `:hover` de la tarjeta, `inset: 6px` y color al 70 %, con una transición de 200 ms. Reactivar `display: block` solo para este `::after` (en `site.css` los pseudoelementos de `.panel--white` están ocultos).
- [ ] **Step 4: Línea de los titulares.** En `:is(.section-head h2, .grid-h, .pdp-body-h, .band-row h2, .split-6 h2, main > .section h2)`, un `::before` de bloque de 32×2 px en `--decor-c` (blanco al 70 % en `.ground-inverse`) con `margin-bottom: var(--s-4)`. En reposo `scale: 1`; con `html.js-decor` y sin `.decor-line--in`, `scale: 0 1` y `transform-origin: left`; con `.decor-line--in`, transición de 600 ms. El texto nunca cambia.
- [ ] **Step 5: Bandas y pie.** `#resistencias.ground-inverse` y `footer.closing` llevan un `::before` absoluto con la cuadrícula del paso 1 al 6 % y `mask-image: radial-gradient(...)`, que deja limpio el centro. Es una máscara y no un color, así que no cuenta como halo. `isolation: isolate` va en el contenedor.
- [ ] **Step 6: Reducir movimiento.** Bajo `@media (prefers-reduced-motion: reduce)` se anulan todas las transiciones de este archivo y los estados ocultos (`clip-path: inset(0)`, `scale: 1`).
- [ ] **Step 7: Comprobar en el navegador** (servidor de la copia de vista previa, viewport de 1440×900): la cuadrícula y la regla se ven en Contacto y en HRS, las esquinas en las tarjetas, y la línea sobre «Catálogo por línea de producto». `document.documentElement.scrollWidth === innerWidth` a 375 px.
- [ ] **Step 8: Commit**

```bash
git add assets/css/decor.css
git commit -m "Decoración de plano técnico: cuadrícula, regla, esquinas y línea de titulares"
```

### Task 3: Entrada de páginas interiores y trazo de titulares (`entrance.js`)

**Files:**
- Modify: `assets/js/entrance.js`
- Modify: `assets/css/decor.css` (estados de espera de la entrada)
- Test: comprobación en el navegador (no hay banco de pruebas de JS en el repo)

**Interfaces:**
- Consumes: `.pg-head[data-enter]` y `.pdp[data-enter]` (tarea 1); `.is-in` y `.decor-line--in` (tarea 2); `html.m-enter` y `html.m-enter-done` (línea del `<head>` ya existente).
- Produces: `.is-in` en la cabecera o la ficha cuando acaba la entrada; `html.js-decor` al cargar el módulo.

- [ ] **Step 1: Estados de espera en `decor.css`.** Bajo `@media screen and (prefers-reduced-motion: no-preference)` y `html.m-enter:not(.m-enter-done) :is(.pg-head, .pdp)[data-enter]:not(.is-entering, .is-in)`, `opacity: 0` en `h1`, `.crumbs`, `.t-lead`, `.pdp-sub`, `.pdp-info > :not(h1)` y en las primeras tarjetas, `.prod-grid > .card:nth-child(-n+8)`. La foto de la galería espera con `scale: 1.04` y `clip-path: inset(2%)`. Si la marca de 700 ms llega antes que el script, todo aparece con una transición de opacidad de 400 ms.
- [ ] **Step 2: Implementar `enterPage(root: HTMLElement): void` en `entrance.js`**, con la misma coreografía que `motion.js` `enter()` (no se toca `motion.js`):
  1. Las palabras del `h1` suben desde una máscara (`.m-w` / `.m-w__in`, las clases que ya estila `motion.css`), 700 ms cada una, empezando a los 80 ms, con un escalón por línea de `min(80, 240/(líneas-1))` ms y `cubic-bezier(.22,1,.36,1)`.
  2. A los 220 ms del final del titular, `.crumbs`, `.t-lead` y `.pdp-sub`, y luego los hijos de `.pdp-info` y la galería, aparecen uno tras otro cada 60 ms (opacidad de 0 a 1 y `translateY(12px)` a `none`, 500 ms).
  3. La foto de `.gallery-main` va de `scale: 1.04` y `clip-path: inset(2%)` a `1` e `inset(0)` en 1100 ms.
  4. Las tarjetas de `.prod-grid` que caben en el primer viewport (`getBoundingClientRect().top < innerHeight`, 8 como máximo) aparecen en cascada cada 60 ms, a partir de los 300 ms.
  5. Todo termina antes de 1100 ms. Se añade `.is-entering` al empezar y `.is-in` al terminar, y luego se restaura el `h1` (fuera las máscaras, `aria-label` limpio).
  La entrada se salta (se añade `.is-in` directamente) si no hay `html.m-enter`, si está activo reducir movimiento, si `root.getBoundingClientRect().bottom < 0` o si ya pasó `m-enter-done`.
- [ ] **Step 3: Trazo de titulares.** Se añade `html.js-decor`. Un `IntersectionObserver` con `threshold: 0.6` añade `.decor-line--in` a cada titular de la lista de la tarea 2 la primera vez que entra en pantalla, y deja de observarlo. Sin `IntersectionObserver`, todos lo reciben al instante.
- [ ] **Step 4: Historial (bfcache).** En `pageshow` con `e.persisted`, se añade `.is-in` a la cabecera o ficha y `.decor-line--in` a todos los titulares, sin animar.
- [ ] **Step 5: Comprobar en el navegador:**
  - Contacto, HRS y Serie MTC-B: la entrada se ve y acaba con `.is-in`; `getAnimations()` está vacío a los 1200 ms.
  - Con `resize_window` y emulación de reducir movimiento: sin animaciones y con `.is-in` al instante.
  - Abriendo `contacto.html#contact`: la cabecera fuera de pantalla queda visible.
  - Consola sin errores.
- [ ] **Step 6: Commit**

```bash
git add assets/js/entrance.js assets/css/decor.css
git commit -m "Entrada animada en cabeceras, fichas y primeras tarjetas; trazo de titulares"
```

### Task 4: Fondo del kit y momentos (portada y Quiénes somos)

**Files:**
- Create: `assets/moments/picture-develops/moment.js` y `moment.css` (copiados de `~/.claude/skills/taste-skill/assets/moments/picture-develops/`)
- Create: `assets/backgrounds/` ya existe; solo se enlaza
- Modify: `build.py`: `HOME_EXTRA`, sección `#hrs` (línea ~391), `.plant-photo` (línea ~448) y `.about-photo` (línea ~612)
- Modify: `tests/test_decor.py`

**Interfaces:**
- Consumes: el cargador `assets/moments/moments.js`, que `system.js` ya carga cuando hay `[data-moment]`.
- Produces: `data-moment="picture-develops"` con `data-moment-opts='{"look": "film"}'` en `.plant-photo` y `.about-photo`; clase `bg-ruled` en `#hrs`; en la portada, `backgrounds.css` enlazado después de `layout.css` y `backgrounds.js` sin `module` al final del `<head>`.

- [ ] **Step 1: Añadir las pruebas**

```python
class Momentos(Base):
    def test_planta_se_revela(self):
        self.has('plant-photo" data-moment="picture-develops"', page("index.html"))
    def test_empresa_se_revela(self):
        self.has('about-photo" data-moment="picture-develops"', page("quienes-somos.html"))
    def test_portada_dos_momentos_como_maximo(self):
        self.assertEqual(page("index.html").count("data-moment="), 2)
    def test_fondo_ruled_en_hrs(self):
        html = page("index.html")
        self.has('class="section bg-ruled" id="hrs"', html)
        self.has('href="assets/backgrounds/backgrounds.css"', html)
```

- [ ] **Step 2: Ejecutar y ver que falla:** `python3 -m unittest tests/test_decor.py -v`. Fallan las 4 nuevas.
- [ ] **Step 3: Copiar el momento, añadir los atributos y el fondo, y regenerar con `python3 build.py`.** La foto de la portada lleva `loading="lazy"`: se deja, porque el momento espera a que la imagen esté cargada.
- [ ] **Step 4: Ejecutar y ver que pasa:** las 9 pruebas de `test_decor.py` dan OK.
- [ ] **Step 5: Comprobar en el navegador** que la foto de la planta se revela una vez al llegar (en unos 1,6 s), que con reducir movimiento se ve quieta, y que `#hrs` muestra la cuadrícula en los márgenes con el titular limpio.
- [ ] **Step 6: Commit**

```bash
git add assets/moments/picture-develops build.py *.html tests/test_decor.py
git commit -m "Momentos picture-develops y fondo ruled en la portada"
```

### Task 5: Verificación, revisión y publicación

**Files:** ninguno nuevo (solo correcciones que salgan de la revisión)

- [ ] **Step 1: Repasar escritorio (1440×900) y móvil (375×812)** en portada, catálogo, ficha, Quiénes somos y Contacto: sin desborde horizontal y sin texto tapado por la decoración. El contraste del texto sobre la cuadrícula no baja de 4.5:1, porque la cuadrícula está al 14 % como mucho y enmascarada detrás del texto.
- [ ] **Step 2: Entrada junto con la transición entre páginas:** de HRS a Serie MTC-G por la tarjeta; la entrada se ve una sola vez. Con el panel oculto no se puede ver: se apunta como no comprobado.
- [ ] **Step 3: Detector de impeccable:** `~/.claude/skills/impeccable/scripts/impeccable detect --json --changed` sin hallazgos nuevos atribuibles a `decor.css` o `entrance.js`.
- [ ] **Step 4: Captura de movimiento de la entrada de Contacto** (normal y reducida) con `impeccable motion-capture` y revisión con el agente `impeccable-motion-reviewer`; aplicar sus correcciones (2 rondas como máximo).
- [ ] **Step 5: Pruebas:** `python3 -m unittest discover -s tests`. `test_decor.py` pasa entero y los fallos previos siguen siendo los mismos 6 y 1.
- [ ] **Step 6: Commit de las correcciones y push** a `origin/main`. Esperar a que GitHub Pages diga `built` con el commit nuevo.
