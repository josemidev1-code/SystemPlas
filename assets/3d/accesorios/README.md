# Accesorios 3D

GLB de cada accesorio, uno por variante. Las rutas están en `data/accesorios3d.json`.

| Archivo | Nodo de montaje | Caja (X × Y × Z, m) |
|---|---|---|
| `acc-resistencia-cilindro.glb` | `MONTAJE_CILINDRO_Z1…Z4` | 0,14 × 0,23 × 0,23 (anillo, eje X, Ø int 0,18) |
| `acc-resistencia-cilindro-mica.glb` | `MONTAJE_CILINDRO_Z1…Z4` | igual que la anterior |
| `acc-resistencia-boquilla.glb` | `MONTAJE_BOQUILLA` | 0,085 × 0,11 × 0,11 (anillo, eje X, Ø int 0,07) |
| `acc-eoat.glb` | `MONTAJE_EOAT` | 0,26 × 0,40 × 0,50, cara de agarre hacia −X |
| `acc-hrs.glb` | `MONTAJE_HRS` (+0,8 m sobre el carro) | 0,45 × 0,30 × 0,25, frente hacia +Z, origen en la base |

La página monta un GLB que exista y tenga `"validado": true` o `"aproximacion": true` en `data/accesorios3d.json`. En los demás casos dibuja un volumen translúcido: el archivo falta o no se ha validado todavía. La página no escala, no gira y no centra los modelos.

**Validación de cada GLB, antes de marcarlo como validado y sobre el modelo real:**
1. **Eje del agujero.** Se identifica sobre la geometría: el eje común de las caras interiores cilíndricas. No basta con tomar la dimensión menor de la caja, porque una banda con caja de bornes, bridas o cable puede ser más ancha que alta.
2. **Paso interior real.** Se mide la distancia radial mínima de los vértices al eje en todo el ancho de la banda. Tiene que dejar libre el Ø del cilindro (0,18 m) o de la boquilla (0,07 m) con holgura. Escalar por el diámetro exterior no garantiza el interior.
3. **Escala, orientación y origen.** Se aplican en el archivo:
   - Anillos: eje del agujero en +X y origen en su centro.
   - HRS: frente hacia +Z y origen en el centro de la base.
   - EOAT: cara de agarre hacia −X.
4. **Envolvente total dentro de la reserva.** Se mide la distancia radial máxima al eje del cuerpo junto con los bornes, las orejetas y la salida de cable. Ese valor no cambia al girar la pieza sobre su eje. Debe caber en el Ø exterior reservado sin deformar ni cambiar la escala; si no cabe, el modelo no se valida. El diámetro del cuerpo y la envolvente total se documentan por separado.
5. **Colisiones.** Se comprueba a nivel de triángulos contra las mallas de la máquina y contra los demás accesorios montados, en cada nodo. Las cuatro zonas del cilindro se comprueban una a una.
6. **Peso.** Como máximo 1,5 MB, con texturas de 1024 px como máximo y sin extensiones que la página no carga.

Los candidatos se muestran con avisos visibles y nunca se marcan como validados. La geometría definitiva 1:1 requiere planos y revisión de encajes.

| Modelo | Triángulos | Bytes |
|---|---:|---:|
| Cilindro | 18264 | 895028 |
| Boquilla | 18660 | 541680 |
| EOAT | 9120 | 467200 |
| HRS | 18544 | 626880 |

La variante de mica queda pendiente.
