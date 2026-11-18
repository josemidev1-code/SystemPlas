# Portada con el catálogo completo y EOAT protagonista — diseño

Fecha: 2026-11-18 · Rama: `portada-catalogo-completo`

## Intención

El cliente quiere que un comprador industrial vea **todo el catálogo desde la portada**, sin entrar
obligatoriamente en las categorías, y que la línea **EOAT** sea la sección estrella. Prioridad sobre
cualquier preferencia estética (incluidas reglas de la taste-skill que lo impidan).

## Datos reales (inventario)

- `data/productos.json`: 21 fichas de producto (texto + fotos).
- La estructura de categorías vive en `CATS` dentro de `build.py`: **36 productos** en 4 líneas.

| Línea | Productos | Con ficha | Sin ficha (enlazan a contacto con el producto preseleccionado) |
|---|---|---|---|
| EOAT accesorio robótica | 10 | 5 | 5 (Accesorios perfil, Recuperadores, Pistones paralelos, Corte neumático, Sistema tubular) |
| HRS Controladores | 8 | 8 | 0 |
| Resistencias eléctricas | 8 | 8 | 0 |
| Estanterías moldes | 10 | 0 | 10 (sin foto: el cliente no tiene fotos de racks) |

21 + 15 = 36. Las 21 fichas están todas en `CATS`; ninguna ficha queda fuera.

## Objetivos / no objetivos

- Objetivos: 36/36 productos en la portada, generados desde `build.py`; EOAT arriba y con la
  composición más rica; navegación rápida entre líneas; móvil cómodo; rendimiento igual o mejor.
- No objetivos: tocar fichas, categorías, URLs o el formulario (salvo reutilizarlo); migrar de
  tecnología; integrar servicios de terceros; la propuesta oscura/cinematográfica.
- Anti-objetivos: un marketplace genérico de tarjetas idénticas; carruseles o paginación; inventar
  cifras, certificaciones o productos.

## Enfoques considerados

1. **Cuadrícula única filtrable** (todas las tarjetas iguales + chips de filtro). Rápido, pero es
   exactamente el marketplace genérico que el cliente no quiere y diluye EOAT.
2. **Secciones por línea con composición propia** (elegido). Cada línea una sección con su
   ancla y su propia composición; EOAT con jerarquía editorial en fondo azul marino; un índice
   de anclas fijo bajo la cabecera para saltar entre líneas.
3. **Mantener la portada actual y añadir un bloque "Todos los productos" al final.** Cumple el
   conteo, pero EOAT no gana protagonismo y la portada se alarga con contenido repetido.

## Diseño (llamadas mías, corregibles)

Orden: Hero vídeo → índice del catálogo → **EOAT** → HRS → Resistencias → Estanterías → Servicio
técnico → Contacto y presupuesto (cierre) → pie.

- **Hero**: se conserva el vídeo, el titular y la pausa. Botones: "Ver los productos" (ancla al
  catálogo) + "Pedir presupuesto". Pausa reubicada en móvil sobre la esquina del vídeo.
- **Índice del catálogo** (`nav` de anclas, pegajoso bajo la cabecera): EOAT 10 · HRS 8 ·
  Resistencias 8 · Estanterías 10 · Servicio. Sin JS obligatorio; JS sólo marca la sección activa.
- **EOAT (estrella, fondo azul marino `#012c3d`)**: cabecera editorial con numeración, texto real
  del cliente y CTA de presupuesto. Composición en bento: foto real del cliente (robot en
  inyectora) grande + 2 productos destacados horizontales; fila de 3 productos con ficha;
  franja de 5 "componentes bajo consulta" que llevan al formulario con el producto ya puesto.
  Cada tarjeta con ficha tiene dos enlaces separados: "Ver ficha" y "Presupuesto".
- **HRS (fondo claro)**: columna de texto fija a la izquierda + lista técnica de 8 controladores
  en 2 columnas (foto pequeña, nombre, rasgo real). Variación clara frente al bento de EOAT.
- **Resistencias (fondo superficie)**: cuadrícula de 4×2 con fotos cuadradas grandes sobre blanco
  (prioridad: imagen clara), y la franja real "5 datos para fabricar a medida".
- **Estanterías**: 10 productos sin foto como lista numerada en 2 columnas con su descripción
  real y enlace "Pedir información" (precarga producto y categoría).
- **Servicio técnico**: los tres servicios ya publicados + foto de nave. Nada nuevo inventado.
- **Contacto**: el cierre del pie se convierte en bloque de presupuesto con accesos por línea
  (`contacto.html?cat=…`), teléfono, email y WhatsApp ya publicados.

## Restricciones técnicas

- `build.py` genera todo desde `CATS` + `FICHAS`; ninguna tarjeta escrita a mano.
- El kit fuerza `main > section` a 1–2 pantallas de alto en escritorio; las secciones de catálogo
  crecen con su contenido (`min-height` conservado) para no recortar productos. Se registra como
  excepción a la regla "una sección por pantalla" de taste-skill.
- Imágenes: JPEG optimizados existentes (`web/sin-fondo/*.jpg` + variante `-360`), con
  `srcset`/`sizes`, `width`/`height` y `loading="lazy"`.
- Se mantienen colores, IBM Plex Sans, esquinas rectas, el momento `line-carries-colour` (pasa a la
  sección oscura de EOAT) y el comportamiento de preselección del formulario.

## Criterios de aceptación

1. Test automático: los 36 productos de `CATS` aparecen como tarjeta en `index.html`, cada
   `href` resuelve a un archivo existente o a `contacto.html?producto=…&cat=…`.
2. Las 21 fichas siguen generándose; URLs existentes intactas.
3. Sin scroll horizontal a 320, 390, 768, 1024, 1440; sin errores de consola; sin recursos rotos.
4. Vídeo con pausa operativa y en reposo con `prefers-reduced-motion`.
5. Transferencia inicial no peor que la actual (3.057 KiB escritorio / 1.585 KiB móvil).
6. `python3 build.py` reproducible (dos ejecuciones → mismo resultado).
