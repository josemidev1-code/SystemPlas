# Rediseño de System Plast con el estilo de Botbox

Fecha: 2026-11-16 · Estado: pendiente de aprobación

Decisiones mías (revisables): mantener el verde de System Plast en vez del
azul de Botbox; tarjetas y galería con fondo blanco puro; quitar la animación
de aparición de las tarjetas.

## Intención

El cliente (System Plast) quiere que su web "quede como Botbox"
(referencia: https://botboxiberica.es/productos-crg-componentes). La versión
actual (https://josemidev1-code.github.io/SystemPlas/) ya copia la
**estructura** de Botbox, pero no transmite la misma **sensación**: la de un
catálogo industrial limpio donde el producto es el protagonista. El éxito es
que el cliente ponga las dos webs lado a lado y diga "esto es lo que quería".

## Objetivos

1. Que las páginas de categoría (p. ej. `eoat-accesorio-robotica.html`) se
   vean como la página de productos de Botbox: portada fotográfica con título
   blanco, cuadrícula de 4 columnas de tarjetas solo con foto + nombre, franja
   "Especialistas en…" con botón "Solicitar catálogo", franja de cierre con
   foto y "Contacto".
2. Llevar ese mismo lenguaje visual al resto de páginas (inicio, productos,
   fichas, quiénes somos, noticias, contacto) para que la web sea coherente.
3. Que las fotos se vean desde el primer momento: nada de tarjetas grises
   vacías mientras se carga una animación.
4. Mantenerlo responsive (móvil y tablet), como ya está ahora.

## No objetivos

- Cambiar los textos o los datos de productos (`data/productos.json`, `CATS`
  en `build.py`) más allá de recortar lo que el nuevo diseño no muestra.
- Cambiar de tecnología o de alojamiento: sigue siendo HTML estático generado
  con `python3 build.py` y publicado en GitHub Pages.
- Añadir funciones nuevas (buscador, filtros, tienda, multidioma).

## Anti-objetivos (fracaso aunque "funcione")

- Copiar la identidad de Botbox: logo, textos, fotos, nombre CRG, o su código
  HTML/CSS. Se toma el estilo, no los materiales.
- Que siga pareciendo "una web de plantilla con tarjetas": descripciones
  largas en las tarjetas, sombras y redondeos marcados, demasiados elementos
  pequeños (etiquetas, contadores, enlaces "Ver producto").
- Que las fotos de producto queden pequeñas o recortadas.

## Restricciones

- Todo sale de `build.py` + `assets/css/styles.css` + `assets/js/main.js`.
  Las páginas `.html` se regeneran, nunca se editan a mano.
- Fotos disponibles: las 41 de `assets/img/` (productos en PNG con fondo,
  más `home-2.jpg`, `agencia-*.jpg`, `industria-*.png` para portadas).
- Marca del cliente: logo actual, verde `#037c75` y azul marino `#012c3d`.

## Fotos de producto: el punto crítico

Todas las fotos de producto de `assets/img/` (hrs-*, res-*, eoat-*) llevan
**una mancha verde oscura dibujada detrás del producto** (heredada de la web
original). Botbox enseña el producto limpio sobre blanco o gris claro. Con la
mancha, por mucho que se cambie el CSS, la cuadrícula seguirá sin parecerse.
Solución (decidida por el usuario): **recortar las fotos actuales** para
quitar la mancha y dejar el producto sobre fondo blanco. Las originales se
conservan; las recortadas se guardan aparte. Si el cliente envía fotos
originales más adelante, se sustituyen.

**Hecho:** 42 fotos recortadas (27 de catálogo + 15 de galería de fichas) en
`assets/img/sin-fondo/` y `assets/img/sin-fondo/p/`, con los mismos nombres
que las originales. Script reproducible en `tools/quitar_mancha.py`
(rembg `isnet-general-use`, solo CPU). Revisadas una a una: todas usables.
Avisos para quien construye:
- `res-6` y `placa-calefactora…-1` conservan un resto blanco de la mancha:
  invisible sobre blanco, visible sobre gris. **Las tarjetas y la galería
  deben tener fondo blanco puro.**
- `eoat-3`: los perfiles azul claro pierden algo de color. Aceptado.
- Las fotos sin mancha (`home-*`, `industria-*`, `agencia-*`, `home-2.jpg`,
  `logo.png`) no se tocan.
- `build.py` debe usar la versión de `sin-fondo/` cuando exista y la
  original si no.

## Lo que se ha medido en Botbox

- Tipografía: Source Sans Pro (la misma familia que ya usamos). Texto 16px.
- Portada: ~460px de alto, foto a todo el ancho, título en mayúsculas,
  blanco, negrita, ~45px, con subtítulo blanco debajo.
- Tarjetas: foto grande y centrada (~270px de ancho), nombre en semibold
  centrado debajo, sin descripción ni enlaces. Cuadrícula de 4 columnas.
- Franja "Especialistas": fondo de color de marca, título blanco ~24px,
  párrafo blanco y botón contorno en mayúsculas.
- Franja final: foto con capa de color, título grande blanco, botón.

## Enfoques considerados

1. **Rediseñar sobre el generador actual (elegido).** Cambiar `styles.css` y
   las plantillas de `build.py`. Mismo resultado visual, poco riesgo, los
   datos y el flujo de trabajo se mantienen.
2. Rehacer desde cero imitando el código de Botbox: más fiel, pero tira lo
   hecho y copiar su plantilla tiene riesgo legal.
3. WordPress con una plantilla parecida: obliga a cambiar hosting y
   mantenimiento; desproporcionado.

El usuario eligió el 1.

## Diseño

### Global
- **Color:** se mantiene el verde de System Plast en lugar del azul de
  Botbox (*decisión mía; cambiar si el cliente quiere el azul*). El verde
  ocupa el papel del azul: botón "Contáctanos", franjas, enlaces activos.
- **Tipografía:** Source Sans 3, títulos en negrita 700, más contraste
  (texto casi negro `#0f0f0f` como Botbox en vez del gris actual).
- **Formas:** esquinas rectas o casi (0–4px), sombras mínimas.
- **Animaciones:** se elimina el efecto de aparición `.reveal` en tarjetas
  e imágenes (o se garantiza que el contenido sea visible sin JS y sin
  esperar al scroll). Se pueden conservar transiciones de hover suaves.

### Barra superior y cabecera
Se mantienen (ya coinciden con Botbox). Ajuste fino de tamaños y color del
menú para que se lea como el de Botbox.

### Portada de página (`hero`)
- Foto a todo el ancho con capa oscura/verde, **texto blanco**, título en
  mayúsculas ~45px negrita, subtítulo debajo. Alto ~420–460px en escritorio,
  menor en móvil.
- Se quita la ceja ("System Plast" pequeño encima del título) y el borde
  verde inferior si estorban al parecido.

### Páginas de categoría (la referencia directa)
- Fondo blanco. Cuadrícula de 4 columnas (2 en tablet, 2 en móvil).
- Tarjeta = foto grande centrada + nombre en negrita debajo. Sin
  descripción, sin "Ver producto", sin contadores. Toda la tarjeta enlaza a
  la ficha.
- Hover: ligera elevación o zoom de la foto.
- Las pestañas de categorías (`cat-tabs`) se mantienen pero más discretas,
  o pasan a ser solo el submenú (*decisión del constructor tras ver el
  resultado; el criterio es que no compitan con la cuadrícula*).
- Debajo: franja verde "Especialistas en…" con el texto de `band` de cada
  categoría y botón contorno "SOLICITAR CATÁLOGO DE PRODUCTOS".
- Cierre: franja con foto y "Creamos la diferencia contigo"-equivalente
  propio de System Plast (texto existente de `CTA`) + botón "Contacto".

### Página de productos (`productos.html`)
Mismo estilo de tarjeta, mostrando las 4 categorías (foto + nombre).

### Inicio
Portada con el nuevo estilo de hero; el resto de secciones existentes se
reestiliza con el mismo lenguaje (cuadrícula foto + nombre, franjas de
color). No se cambia el contenido.

### Fichas de producto
Se mantiene la estructura (galería, datos, botones de presupuesto y
WhatsApp), con la nueva tipografía, colores y esquinas rectas. Bloque de
"Otros productos de la categoría" con las tarjetas nuevas.

### Pie
Se mantiene el contenido; se ajusta al nuevo estilo.

## Cómo se comprueba

- Captura a 1440px y 375px de una página de categoría junto a la de Botbox.
- Revisión rápida de todas las páginas generadas en el navegador: sin
  tarjetas vacías, sin errores en consola, sin scroll horizontal en móvil.

## Queda en manos del constructor

- Valores exactos de espaciados, tamaños de foto y capas de color de la
  portada, siempre buscando el parecido con las medidas de arriba.
- Qué foto de `assets/img/` usar en cada portada.
- Cómo limpiar en `build.py` los parámetros de `card()` que dejan de usarse.
