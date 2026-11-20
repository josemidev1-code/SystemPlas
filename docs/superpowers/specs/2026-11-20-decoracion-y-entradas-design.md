# Decoración y animaciones de entrada (System Plast)

Fecha: 2026-11-20 · Tamaño: cambio mediano (diseño corto)

## Por qué
La web se ve "cutre": fondos planos (gris claro, blanco y algún bloque azul marino), ningún adorno y
nada que se mueva al entrar. El cliente quiere un diseño agradable, con decoración y movimiento
basados en los colores de la marca: verde petróleo `#037c75` y azul marino `#012c3d`.

## Objetivos
- Todas las páginas tienen una entrada al cargar: la cabecera se revela y la foto se asienta.
- Decoración propia con los colores de la marca, inspirada en planos técnicos (moldes, inyección).
- Uno o dos momentos memorables por página larga, del catálogo del kit.
- Mismo contenido, textos y estructura: solo cambia el aspecto.

## Fuera de alcance
Cambiar textos, añadir secciones, rehacer maquetación o añadir librerías.

## Lo que no puede pasar
- Bloques en blanco que esperan a que hagas scroll. Fue el motivo por el que se quitaron las
  apariciones el 16 de noviembre: todo el texto se ve siempre.
- Efectos chillones o el típico brillo "hecho por IA" (halos, degradados de color en el texto, cristal).
- Tirones en el móvil, o movimiento para quien tiene activado "reducir movimiento".

## Restricciones
- Web estática generada por `build.py`; publicada en GitHub Pages.
- Kit taste-skill (`site-kind: tech`): como mucho dos fondos del kit por página, entradas de 1,1 s
  como máximo, solo transform/opacity/clip/filter, sin librerías.

## Caminos considerados
- A. Solo el kit (sus fondos y momentos): rápido y seguro, pero genérico.
- B. Mundo propio de plano técnico, todo a medida: lo más distintivo, pero mucho código nuevo.
- **C. Mezcla (elegida por el cliente):** los fondos del kit para dar color a las secciones, más tres
  detalles propios de plano técnico, más entradas en todas las páginas.

## Diseño

### 1. Decoración (colores de la marca)
- **Cabeceras de página:** cuadrícula técnica de líneas finas en verde petróleo, que se desvanece
  hacia el texto, con una regla de marcas de medida en el borde inferior. En la cabecera azul marino
  de Contacto, la misma cuadrícula en verde claro.
- **Secciones de la portada:** el fondo del kit `ruled` (cuadrícula en los márgenes, limpia detrás
  del titular) en una sección clara, y la banda azul marino de resistencias con líneas tenues.
  Máximo dos fondos del kit por página.
- **Fotos de producto:** cuatro marcas de esquina en verde petróleo, como en un plano. Se ven
  suaves en reposo y se cierran hacia la foto al pasar el ratón.
- **Titulares de sección:** una línea corta en verde petróleo que se dibuja junto al titular.
- **Pie:** la cuadrícula muy tenue de fondo.

```
┌────────────────────────────────────────────┐
│ ┼  ┼  ┼  ┼  ┼  ┼  (cuadrícula verde tenue) │
│ Inicio / Productos                         │
│ Catálogo de controladores HRS   [vídeo]    │
│ Control de temperatura...                  │
│ |    |    |    |    |    |    (regla)      │
└────────────────────────────────────────────┘
  ⌜      ⌝   ⌜      ⌝   ⌜      ⌝
    foto       foto       foto      ← marcas de esquina
  ⌞      ⌟   ⌞      ⌟   ⌞      ⌟
```

### 2. Entradas (al cargar, una vez, 1,1 s como máximo)
- **Cabeceras de las páginas interiores:** la entrada del kit que ya tiene la portada. El titular
  sube palabra a palabra, luego aparecen la ruta y la entradilla, y el vídeo se asienta.
- **Fichas de producto:** el título entra igual y la foto de la galería se asienta (escala y recorte).
- **Rejillas de productos:** solo las tarjetas visibles al cargar entran en cascada, con 60 ms entre
  ellas. Las de más abajo ya están puestas: el scroll no esconde nada (es una regla del kit y
  nuestro "lo que no puede pasar").
- **Decoración:** la cuadrícula y la regla se dibujan dentro de esa misma entrada.

### 3. Momentos (del catálogo del kit)
- Portada: `picture-develops` en la foto de la planta (se revela una vez al llegar), además del
  `line-carries-colour` que ya existe.
- Quiénes somos: `picture-develops` en la foto principal.
- Si hay una fila de cifras (12-24 h, 128 zonas), `counter-rolls`. Si no la hay, no se fuerza.

### 4. Reducir movimiento y sin JavaScript
La decoración se queda; las entradas y los momentos muestran su estado final al instante.

## Herramientas
- taste-skill: fondos, momentos, su comprobador y su revisión final.
- impeccable: animate y polish, la revisión de movimiento y el detector.

## Decisiones que quedan al constructor
Opacidades exactas de la decoración, tiempos dentro de los valores del kit, y qué sección clara
lleva `ruled`.
