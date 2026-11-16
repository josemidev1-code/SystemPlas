"""1) pinta de blanco la mancha verde  2) recorta el producto con IA.
Uso: python hibrido.py MODELO SALIDA_DIR ENTRADA..."""
import sys, os
import numpy as np
from PIL import Image
from rembg import remove, new_session

model, outdir, files = sys.argv[1], sys.argv[2], sys.argv[3:]
os.makedirs(outdir, exist_ok=True)
sess = new_session(model, providers=["CPUExecutionProvider"])
GREEN = np.array([14, 81, 81.0])
HALO = float(os.environ.get("HALO", 26))


def blanquear(im):
    a = np.asarray(im.convert("RGBA")).astype(np.float32)
    rgb, al = a[..., :3], a[..., 3:] / 255.0
    rgb = rgb * al + 255 * (1 - al)  # aplanar sobre blanco
    d = np.sqrt(((rgb - GREEN) ** 2).sum(-1))
    w = np.clip((70 - d) / 40, 0, 1)[..., None]  # 1 = mancha
    # el halo es blanco mezclado con verde: estimar cuánto verde lleva y quitarlo
    rgb = rgb * (1 - w) + 255 * w
    # halo: colores sobre la recta verde->blanco (mezcla de brillo blanco y mancha)
    W = np.array([255, 255, 255.0]); u = (W - GREEN) / np.linalg.norm(W - GREEN)
    v = rgb - GREEN; t = (v @ u)[..., None]
    dist = np.linalg.norm(v - t * u, axis=-1)
    tint = (rgb[..., 1] - rgb[..., 0])  # el halo tiene más verde que rojo
    h = (np.clip((HALO - dist) / 8, 0, 1) * np.clip((tint - 4) / 10, 0, 1))[..., None]
    rgb = rgb * (1 - h) + 255 * h
    return Image.fromarray(rgb.astype(np.uint8))


for f in files:
    flat = blanquear(Image.open(f))
    mask = remove(flat, session=sess, only_mask=True, post_process_mask=True)
    orig = Image.open(f).convert("RGBA")
    base = Image.new("RGBA", orig.size, (255, 255, 255, 255))
    base.alpha_composite(orig)
    out = flat.convert("RGBA")
    out.putalpha(mask)
    bb = out.getbbox()
    if bb:
        out = out.crop(bb)
    dst = os.path.join(outdir, os.path.basename(f))
    out.save(dst, optimize=True)
    flat.save(os.path.join(outdir, "flat-" + os.path.basename(f)))
    print(dst, out.size)
