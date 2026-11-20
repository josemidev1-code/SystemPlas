"""
Generador de la web de SYSTEM PLAST.
Edita los datos de este archivo o data/productos.json y ejecuta:  python3 build.py

Diseño: sistema de la skill taste-skill (assets/system.css, motion, layout) con los colores
del logo (verde #037c75, azul marino #012c3d). La portada lleva un vídeo de licencia libre
(Pexels) detrás del titular: assets/video/maquina-*.mp4.
"""
import os, html, json
from urllib.parse import quote

OUT = os.path.dirname(os.path.abspath(__file__))
E = html.escape
FICHAS = json.load(open(os.path.join(OUT, "data", "productos.json"), encoding="utf-8"))

TEL = "+34627967729"
TEL_TXT = "(+34) 627 96 77 29"
MAIL = "info@systemplas.com"
DIR1, DIR2 = "Pol. Ind. Riodil, 1", "03110 Mutxamel, Alicante"
LINKEDIN = "https://www.linkedin.com/company/system-plas/"
MAIN_ACTION = "Pedir presupuesto"
YEAR = 2026

ICON = {
 "wa": '<svg viewBox="0 0 32 32" aria-hidden="true" width="18" height="18"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7a.6.6 0 0 0 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zm7 0h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.6c0-1.34-.02-3.06-1.86-3.06-1.87 0-2.15 1.46-2.15 2.96V21h-4z"/></svg>',
}
ARROW = '<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg>'

# ---------------------------------------------------------------------------
# Catálogo: (nombre en tarjeta, imagen de tarjeta, slug de ficha o None, descripción breve)
# ---------------------------------------------------------------------------
CATS = [
 {"slug": "hrs-controladores", "name": "HRS Controladores", "img": "hrs-1.png",
  "short": "Controladores de temperatura para canal caliente: monozona, multizona y sistemas inteligentes con algoritmo PID.",
  "hero": ("Catálogo de controladores HRS", "Control de temperatura de canal caliente con precisión PID"),
  "band": ("Especialistas en control de canal caliente", "Seleccione el controlador de temperatura de canal caliente según sus necesidades y requisitos de uso. Le asesoramos para elegir la serie adecuada y le enviamos recambios en 12-24 horas."),
  "items": [("Serie MTC-B", "hrs-1.png", "serie-mtc-b", "Pantalla IPS a todo color"),
            ("Serie MTC-G", "hrs-2.png", "serie-mtc-g", "Gráfico de temperatura en tiempo real"),
            ("Serie MTC-H", "hrs-3.png", "serie-mtc-h", "Hasta 128 zonas y pantalla plegable"),
            ("Serie MTC-I", "hrs-4.png", "serie-mtc-i", "Compacto: un módulo, dos temperaturas"),
            ("Serie TG", "hrs-5.png", "serie-tg", "Módulos con perilla, hasta 128 zonas"),
            ("Pantalla táctil serie TG", "hrs-6.png", "pantalla-tactil-serie-tg", "Doble pantalla, 15 zonas por página"),
            ("Tarjeta tipo MTC-B", "hrs-7.png", "tarjeta-tipo-mtc-b", "Interfaz universal compatible"),
            ("Controlador de secuencia SVGE-8", "hrs-8.png", "svge-8", "8 zonas para valve gates")]},
 {"slug": "resistencias-electricas", "name": "Resistencias eléctricas", "img": "res-2.png",
  "short": "Resistencias de mica, aluminio, cobre, cerámicas y de infrarrojos para husillos, boquillas y moldes.",
  "hero": ("Catálogo de resistencias eléctricas", "Calefacción eficiente y a medida para máquinas de inyección"),
  "band": ("Resistencias fabricadas a su medida", "Indíquenos dimensiones, voltaje, potencia, perforaciones y tipo de conexión, y fabricamos la resistencia exacta que necesita su máquina."),
  "items": [("Resistencia de mica en acero inoxidable", "res-1.png", "resistencia-en-acero-inoxidable-de-mica", "Calentamiento estable"),
            ("Resistencias de aluminio", "res-2.png", "resistencias-de-aluminio", "Rápidas y de bajo consumo"),
            ("Resistencia en cobre puro", "res-3.png", "resistencia-en-cobre-puro", "Hasta 500 °C en superficie"),
            ("Resistencia tipo resorte", "res-4.png", "resistencias-de-calentamiento-tipo-resorte", "Hasta 750 °C, termopar J/K"),
            ("Nano-infrarrojo de bajo consumo", "res-5.png", "nano-infrarrojo-calentador-de-bajo-consumo", "Ahorro de energía del 30 % al 83 %"),
            ("Placa calefactora de mica e inox", "res-6.png", "placa-calefactora-de-mica-y-acero-inoxidable", "Soporta hasta 600 °C"),
            ("Funda de aislamiento térmico", "res-7.png", "funda-de-aislamiento-para-el-ahorro-de-energia", "Menos pérdida de calor"),
            ("Anillo calefactor cerámico", "res-8.png", "anillo-calefactor-ceramico", "Alta temperatura y seguridad")]},
 {"slug": "eoat-accesorio-robotica", "name": "EOAT accesorio robótica", "img": "home-junto.png",
  "short": "Garras, pinzas, ventosas y perfilería para robots de extracción en inyección.",
  "hero": ("Catálogo EOAT · accesorios de robótica", "Garras y herramientas de final de brazo para robots de extracción"),
  "band": ("Especialistas en garras para robot", "Disponemos de una gran variedad de componentes, medidas y tamaños para combinar y construir la garra que mejor se adapte a cada pieza y a cada robot."),
  "items": [("Cambiadores rápidos (Quick Changers)", "eoat-1.png", "cambiadores-rapidos-de-herramientas-quick-changers", "Carga máxima 15 kg"),
            ("Pinzas de bebedero (Sprue Grippers)", "eoat-2.png", "pinzas-de-bebedero-sprue-grippers", "Extracción de coladas"),
            ("Accesorios perfil EOAT", "eoat-3.png", None, "Perfilería y uniones"),
            ("Pinzas de aguja y de expansión", "eoat-4.png", "pinzas-de-aguja-y-de-expansion", "Piezas blandas e interiores"),
            ("Pinzas neumáticas angulares de dedo", "eoat-5.png", "pinzas-neumaticas-paralelas-y-angulares", "De dos o tres dedos"),
            ("Ventosas de vacío", "eoat-6.png", "ventosas-de-vacio", "Silicona, NBR y poliuretano"),
            ("Recuperadores", "eoat-7.png", None, None),
            ("Pistones paralelos", "eoat-8.png", None, None),
            ("Corte neumático", "eoat-9.png", None, None),
            ("Sistema tubular", "eoat-10.png", None, None)]},
 {"slug": "estanterias-moldes", "name": "Estanterías moldes", "img": None,
  "short": "Racks, cajones extraíbles, carros y accesorios para almacenar y mover moldes con seguridad.",
  "hero": ("Catálogo de estanterías para moldes", "Almacenaje seguro y ordenado de sus moldes de inyección"),
  "band": ("Orden y seguridad en su almacén de moldes", "Diseñamos soluciones de almacenaje adaptadas al peso y tamaño de sus moldes, para ganar espacio y trabajar con total seguridad."),
  "items": [("Estanterías de cajones extraíbles (Pull-Out Racks)", None, None, "Sistemas dinámicos donde cada nivel funciona como un cajón deslizante sobre rodamientos, facilitando la extracción superior de los moldes mediante grúa."),
            ("Estanterías de carga estática heavy-duty", None, None, "Estructuras fijas de perfiles de acero estructural de alto calibre, diseñadas para el almacenamiento permanente de matrices de gran tonelaje."),
            ("Racks compactos para moldes pequeños", None, None, "Almacenamiento de alta densidad para moldes de bajo peso y accesorios periféricos, maximizando el espacio vertical en planta."),
            ("Estanterías con polipasto superior integrado", None, None, "Racks autónomos con monorraíl y polipasto de cadena, sin necesidad de puentes grúa externos para la carga y descarga."),
            ("Bases rodantes y carros de transporte", None, None, "Plataformas de acero con ruedas de poliuretano de alta carga para trasladar matrices con seguridad hasta la inyectora."),
            ("Estanterías abiertas de carga frontal/lateral", None, None, "Sin travesaños frontales, permiten el acceso directo de carretillas; ideales para moldes paletizados de dimensiones irregulares."),
            ("Mesas de mantenimiento y apertura de moldes", None, None, "Estaciones reforzadas y escuadras magnéticas para la separación, limpieza y reparación segura de las mitades del molde."),
            ("Sistemas anticaídas y topes de seguridad", None, None, "Bloqueos, pasadores de retención y topes traseros que evitan el deslizamiento accidental de las matrices."),
            ("Fundas y cortinas de protección para moldes", None, None, "Cerramientos de PVC antiestático y fundas textiles contra polvo, humedad y oxidación de moldes con acabado espejo."),
            ("Estantes modulares expansibles", None, None, "Racks atornillables que permiten añadir módulos a medida que crece su inventario de moldes.")]},
]
NAV = [("index.html", "Inicio"), ("productos.html", "Productos"), ("quienes-somos.html", "Quiénes somos"), ("noticias.html", "Noticias"), ("contacto.html", "Contacto")]

NEWS = [
 ("agencia-6.jpg", "Un catalizador abre la puerta al reciclaje de plásticos sin clasificación previa", "Residuos Profesional", "https://www.residuosprofesional.com/catalizador-reciclaje-plasticos-sin-clasificacion-previa/"),
 ("agencia-7.jpg", "Tendencias en envases plásticos 2025: sostenibilidad e innovación", "Smartco", "https://smartco.mx/tendencias-de-empaque-2025-innovacion-sostenibilidad-y-eficiencia/"),
 ("agencia-8.jpg", "Informe del mercado mundial de envases biodegradables y su crecimiento proyectado", "Mordor Intelligence", "https://www.mordorintelligence.com/es/industry-reports/gobal-biodegradable-packaging-solutions-market-industry"),
]

# Foto de tarjeta de categoría (la de estanterías es una foto de molde: el cliente no tiene foto de racks)
CAT_IMG = {"hrs-controladores": "hrs-1.png", "resistencias-electricas": "res-2.png",
           "eoat-accesorio-robotica": "eoat-3.png", "estanterias-moldes": "photo-f7026183-500.jpg"}
CAT_LINE = {"hrs-controladores": "Monozona, multizona y secuencia para valve gate.",
            "resistencias-electricas": "Mica, aluminio, cobre, cerámica e infrarrojos.",
            "eoat-accesorio-robotica": "Pinzas, ventosas, cambiadores y perfilería.",
            "estanterias-moldes": "Racks, cajones extraíbles y carros para moldes."}
CAT_BY_PRODUCT = {it[2]: c for c in CATS for it in c["items"] if it[2]}
CARD_IMG = {it[2]: it[1] for c in CATS for it in c["items"] if it[2]}
NAVW = [("productos.html", "Productos"), ("quienes-somos.html", "Empresa"), ("noticias.html", "Noticias"), ("contacto.html", "Contacto")]


def img_src(name):
    """La foto ligera: el JPEG sobre blanco de la versión sin mancha verde si existe, si no la original."""
    base = name[:-4] if name.endswith(".png") else None
    for cand in ([f"web/sin-fondo/{base}.jpg", f"sin-fondo/{name}", f"web/{base}.jpg"] if base else []) + [name]:
        if os.path.exists(os.path.join(OUT, "assets", "img", cand)):
            return f"assets/img/{cand}"
    return f"assets/img/{name}"


def jpeg_size(path):
    """Ancho y alto de un JPEG o PNG, para width/height (sin librerías)."""
    import struct
    with open(os.path.join(OUT, path), "rb") as fh:
        d = fh.read()
    if d[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", d[16:24])
    i = 2
    while i < len(d):
        marker, size = d[i + 1], struct.unpack(">H", d[i + 2:i + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", d[i + 5:i + 9])
            return w, h
        i += 2 + size
    return 700, 534


def wh(src):
    w, h = jpeg_size(src)
    out = f'width="{w}" height="{h}"'
    small = src[:-4] + "-360.jpg"
    if src.endswith(".jpg") and os.path.exists(os.path.join(OUT, small)):
        out += f' srcset="{small} 360w, {src} {w}w" sizes="(max-width: 639px) 50vw, 40vw"'
    return out


def is_cutout(name):
    return bool(name) and name.endswith(".png")


def contact_url(prod, cat):
    return f"contacto.html?producto={quote(prod)}&cat={quote(cat)}"


def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)


# ---------------------------------------------------------------------------
# Cabecera, navegación y pie comunes
# ---------------------------------------------------------------------------
# Paso entre páginas: en la página que llega, la foto del producto recibe el nombre compartido antes del
# primer pintado (por eso va en línea en el <head>; site.js nombra la de la página que se va).
VT_HEAD = """<script>(()=>{const n=window.navigation;if(!n||!('onpagereveal' in window))return;const l=document.createElement('link');l.rel='expect';l.href='#vt-parsed';l.setAttribute('blocking','render');document.head.append(l);const P=s=>s.replace(/\\/index\\.html$/,'/');const same=(a,b)=>{try{const x=new URL(a,location.href),y=new URL(b,location.href);return x.origin===y.origin&&P(x.pathname)===P(y.pathname)}catch(e){return false}};addEventListener('pagereveal',e=>{const vt=e.viewTransition,f=n.activation&&n.activation.from;if(!vt||!f||matchMedia('(prefers-reduced-motion: reduce)').matches)return;let el=null;for(const a of document.querySelectorAll('a.card[href]'))if(same(a.href,f.url)){el=a.querySelector('.frame__img,img');break}el=el||document.querySelector('[data-gallery-main]');if(!el)return;const r=el.getBoundingClientRect();if(!r.height||r.bottom<0||r.top>innerHeight)return;el.style.viewTransitionName='product-photo';const c=()=>{el.style.viewTransitionName=''};vt.finished.then(c,c)})})()</script>"""

def head(title, desc, extra=""):
    return f'''<!doctype html>
<html lang="es" data-type="product" data-radius="sharp" data-buttons="solid" data-motion>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="share.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/logo.png" type="image/png">
<meta name="theme-color" content="#f4f6f6">
<!-- <link rel="canonical" href="https://systemplas.com/"> cuando el dominio esté publicado -->
<meta name="site-kind" content="tech">
<meta name="page-type" content="product">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wdth,wght@85..100,400..700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/system.css">
<link rel="stylesheet" href="assets/ui/cards.css">
<link rel="stylesheet" href="assets/motion/motion.css">
<link rel="stylesheet" href="assets/layout/layout.css">
<style>
:root {{
  --p-bg: #f4f6f6; --p-surface: #e8eeee; --p-ink: #012c3d; --p-muted: #546d79;
  --p-accent: #037c75; --p-accent-ink: #f4f6f6; --p-action: #037c75; --p-action-ink: #f4f6f6;
  --p-inv-bg: #012c3d; --p-inv-surface: #143849; --p-inv-ink: #f4f6f6; --p-inv-muted: #93a3ab;
  --p-inv-accent: #f4f6f6; --p-inv-accent-ink: #012c3d; --p-inv-action: #f4f6f6; --p-inv-action-ink: #012c3d;
  --font-display: "IBM Plex Sans", system-ui, sans-serif;
  --font-text: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  --display-weight: 500;
  --display-tracking: -0.025em;
  --display-tracking-xl: -0.035em;
  --ly-scale: 0.98;
}}
</style>
<link rel="stylesheet" href="assets/css/site.css">
<script>document.documentElement.classList.add('m-enter');setTimeout(()=>document.documentElement.classList.add('m-enter-done'),700)</script>
{VT_HEAD}
{extra}</head>
'''


def nav(active=None):
    cards = "".join(
        f'''<a class="menu-card span-3" href="{c["slug"]}.html">
              <div class="panel{" panel--white" if is_cutout(CAT_IMG[c["slug"]]) else ""}"><img class="frame__img" src="{img_src(CAT_IMG[c["slug"]])}" {wh(img_src(CAT_IMG[c["slug"]]))} alt="" loading="lazy"></div>
              <span class="t-card">{E(c["name"])}</span>
              <span class="t-small muted">{E(CAT_LINE[c["slug"]])}</span>
            </a>''' for n, c in enumerate(CATS))
    items = []
    for href, label in NAVW:
        cur = ' aria-current="page"' if href == active else ""
        if label == "Productos":
            items.append(f'''<div class="nav__item">
        <a class="nav__link" href="{href}"{cur}>{label} <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <div class="nav__menu"><div class="wrap grid">{cards}</div></div>
      </div>''')
        else:
            items.append(f'<div class="nav__item"><a class="nav__link" href="{href}"{cur}>{label}</a></div>')
    return f'''<body>
<header class="nav">
  <div class="wrap nav__bar">
    <a class="skip-link" href="#top">Saltar al contenido</a>
    <a class="nav__logo" href="index.html"><img src="assets/img/logo-320.png" alt="System Plast" width="320" height="139"></a>
    <nav class="nav__links" aria-label="Principal">
      {"".join(items)}
    </nav>
    <div class="nav__actions">
      <a class="btn btn--primary" href="contacto.html">{MAIN_ACTION}</a>
    </div>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-label="Menú">
      <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>
'''


CREDITS_LINE = '<a class="credits" href="creditos.html">Vídeo y fotos de contexto vía Pexels y Wikimedia Commons</a>'


def footer(close_line="Respuesta y envío de recambios en 12 a 24 horas.", scripts=""):
    cats = "".join(f'<li><a href="{c["slug"]}.html">{E(c["name"])}</a></li>' for c in CATS)
    return f'''<footer class="footer closing g2m" id="contact" aria-labelledby="close-h">
  <div class="wrap">
    <div class="closing__cta close--word">
      <div class="section-head--split">
        <div><h2 id="close-h">Presupuesto para su línea de inyección</h2><p class="t-lead">{E(close_line)}</p></div>
        <a class="btn btn--primary" href="contacto.html">{MAIN_ACTION}{ARROW}</a>
      </div>
      <p class="close__word" aria-hidden="true">System Plast</p>
    </div>
    <div class="closing__links">
      <div class="grid">
        <div class="span-4 stack-4">
          <a class="nav__logo" href="index.html"><img src="assets/img/logo-320.png" alt="System Plast" width="320" height="139" loading="lazy"></a>
          <p class="footer__lede">Componentes y recambios para la inyección de plástico.</p>
        </div>
        <div class="span-3 footer__col"><h3>Productos</h3><ul>{cats}</ul></div>
        <div class="span-2 footer__col"><h3>Empresa</h3><ul><li><a href="quienes-somos.html">Quiénes somos</a></li><li><a href="noticias.html">Noticias</a></li><li><a href="contacto.html">Contacto</a></li></ul></div>
        <div class="span-3 footer__col"><h3>Contacto</h3><ul><li>{DIR1}, {DIR2}</li><li><a href="tel:{TEL}">{TEL_TXT}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
      </div>
      <div class="footer__legal">
        <span>&copy; {YEAR} System Plast</span>
        <div class="socials"><a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON["linkedin"]}</a></div>
        {CREDITS_LINE}
      </div>
    </div>
  </div>
</footer>
<script type="module" src="assets/system.js"></script>
<script type="module" src="assets/motion/motion.js"></script>
<script type="module" src="assets/layout/layout.js"></script>
{scripts}</body>
</html>
'''


def page_head(title, lead, crumbs=(), video=False):
    trail = ""
    if crumbs:
        parts = ['<a href="index.html">Inicio</a>']
        for label, href in crumbs:
            parts.append(f'<a href="{href}">{E(label)}</a>' if href else f'<span aria-current="page">{E(label)}</span>')
        trail = '<nav class="crumbs" aria-label="Migas de pan">' + '<span aria-hidden="true">/</span>'.join(parts) + '</nav>'
    if video:
        # La portada de catálogo lleva el mismo vídeo de máquinas que la portada (como Botbox)
        return f'''<header class="pg-head pg-head--video" data-enter>
  <video class="pg-head__bg" autoplay muted loop playsinline preload="metadata" poster="assets/video/maquina-poster.jpg" aria-hidden="true" data-bg-video>
    <source src="assets/video/maquina-640.mp4" type="video/mp4" media="(max-width: 639px)">
    <source src="assets/video/maquina-720.mp4" type="video/mp4">
  </video>
  <div class="wrap">{trail}<h1>{E(title)}</h1><p class="t-lead">{E(lead)}</p>
    <button class="loop-pause pg-head__pause" type="button" aria-label="Pausar el vídeo" aria-pressed="false" data-video-pause></button>
  </div>
</header>
'''
    return f'''<header class="pg-head ground-inverse" data-enter>
  <div class="wrap">{trail}<h1>{E(title)}</h1><p class="t-lead">{E(lead)}</p></div>
</header>
'''


def card(title, img, href, line=None):
    panel = ""
    if img:
        cls = "panel panel--white" if is_cutout(img) else "panel"
        panel = f'<div class="{cls}"><img class="frame__img" src="{img_src(img)}" {wh(img_src(img))} alt="{E(title)}" loading="lazy"></div>'
    sub = f'<p>{E(line)}</p>' if line else ""
    return f'<a class="card card--open card--prod" href="{href}">{panel}<h3>{E(title)}</h3>{sub}</a>'

# ---------------------------------------------------------------------------
# Inicio
# ---------------------------------------------------------------------------
HOME_EXTRA = '''<script>document.documentElement.classList.add('mo-js');setTimeout(()=>document.documentElement.classList.add('mo-safe'),2500)</script>
<link rel="modulepreload" href="assets/moments/moments.js">
<link rel="modulepreload" href="assets/moments/lib.js">
<link rel="modulepreload" href="assets/moments/line-carries-colour/moment.js">
'''

def row_link(name, value, href):
    return f'<li><a class="rows__link" href="{href}"><span class="rows__name">{E(name)}</span><span class="rows__value">{E(value)}</span></a></li>'

home_cards = "".join(f'''<a class="card card--open card--prod {"cat-big span-6" if n == 0 else "cat-small span-6 start-7"}" href="{c["slug"]}.html">
          <div class="panel{" panel--white" if is_cutout(CAT_IMG[c["slug"]]) else ""}"><img class="frame__img" src="{img_src(CAT_IMG[c["slug"]])}" {wh(img_src(CAT_IMG[c["slug"]]))} alt="{E(c["name"])}" loading="lazy" data-source="{"client" if is_cutout(CAT_IMG[c["slug"]]) else "stand-in"}" data-subject="{"product" if is_cutout(CAT_IMG[c["slug"]]) else "injection mould"}"></div>
          <h3>{E(c["name"])}</h3><p>{E(CAT_LINE[c["slug"]])}</p>
        </a>''' for n, c in enumerate(CATS))

hrs_rows = "".join(row_link(n, v, f"{s}.html") for n, v, s in [
    ("Serie MTC-B", "Pantalla IPS a color", "serie-mtc-b"),
    ("Serie MTC-H", "Hasta 128 zonas", "serie-mtc-h"),
    ("Serie TG", "Módulos con perilla", "serie-tg"),
    ("Controlador SVGE-8", "8 zonas, valve gate", "svge-8")])

res_rows = "".join(f'<li><span class="rows__name">{k}</span><span class="rows__value">{v}</span></li>' for k, v in [
    ("Dimensiones", "Diámetro, ancho, alto"), ("Tensión", "Voltios de su máquina"), ("Potencia", "En vatios"),
    ("Perforaciones", "Posición y diámetro"), ("Conexión", "Cable, borna o terminal")])
res_tiles = "".join(f'<a href="{s}.html"><img src="{img_src(i)}" width="700" height="534" alt="{E(n)}" loading="lazy" data-source="client" data-subject="product"></a>' for n, i, s in [
    ("Resistencia de mica en acero inoxidable", "res-1.png", "resistencia-en-acero-inoxidable-de-mica"),
    ("Resistencia en cobre puro", "res-3.png", "resistencia-en-cobre-puro"),
    ("Nano-infrarrojo de bajo consumo", "res-5.png", "nano-infrarrojo-calentador-de-bajo-consumo"),
    ("Anillo calefactor cerámico", "res-8.png", "anillo-calefactor-ceramico")])

eoat_rows = "".join(row_link(n, v, f"{s}.html") for n, v, s in [
    ("Cambiadores rápidos", "Carga máxima 15 kg", "cambiadores-rapidos-de-herramientas-quick-changers"),
    ("Pinzas de bebedero", "Extracción de coladas", "pinzas-de-bebedero-sprue-grippers"),
    ("Ventosas de vacío", "Silicona, NBR, poliuretano", "ventosas-de-vacio"),
    ("Pinzas neumáticas", "Dos o tres dedos", "pinzas-neumaticas-paralelas-y-angulares")])

write("index.html", head("System Plast: componentes para inyectoras de plástico",
                         "Controladores de canal caliente, resistencias a medida y garras EOAT para moldeo por inyección, con recambios en 12 a 24 horas desde Mutxamel.",
                         HOME_EXTRA) + nav() + f'''<!-- type: product (hardware, site-kind tech)
     deal: hero photo con vídeo de fondo (el cliente pide un vídeo de máquinas detrás, como Botbox; sustituye al hero product repartido),
     nav nav-cards, close close-word, footer footer-columns, rhythm dark-band, buttons solid, mark: logo del cliente
     palette: colores del logo (start.mjs brand), type plex, radius sharp
     moments: line-carries-colour en #resistencias (la franja oscura) -->
<main id="top">
  <section class="hero hero--photo" data-enter data-calm="left" data-box="none" data-tone="light" aria-labelledby="hero-h">
    <!-- VÍDEO: Pexels 32386599 (licencia Pexels, uso libre). Se cambia aquí por el vídeo propio del cliente. -->
    <video class="hero__bg" autoplay muted loop playsinline preload="metadata" poster="assets/video/maquina-poster.jpg" aria-hidden="true" style="--ly-pos: 70% 50%; --ly-pos-phone: 70% 50%" data-source="stand-in" data-subject="vacuum gripper on an automated line">
      <source src="assets/video/maquina-640.mp4" type="video/mp4" media="(max-width: 639px)">
      <source src="assets/video/maquina-720.mp4" type="video/mp4">
    </video>
    <div class="wrap"><div class="hero-text">
      <div class="hero__text">
        <h1 id="hero-h">Componentes para inyectoras</h1>
        <p class="hero__lead">Controladores de canal caliente de hasta 128 zonas, resistencias fabricadas a medida y garras EOAT para robots de extracción, con recambios en 12 a 24 horas.</p>
        <div class="btn-row"><a class="btn btn--primary" href="contacto.html">{MAIN_ACTION}{ARROW}</a><a class="btn btn--secondary" href="productos.html">Ver el catálogo</a></div>
      </div>
      <button class="loop-pause hero-pause" type="button" aria-label="Pausar el vídeo" aria-pressed="false" data-video-pause></button>
    </div></div>
  </section>

  <section class="section" id="catalogo" aria-labelledby="catalogo-h">
    <div class="wrap">
      <div class="section-head section-head--row">
        <h2 id="catalogo-h">Catálogo por línea de producto</h2>
        <a class="link" href="productos.html">Ver el catálogo</a>
      </div>
      <div class="grid fill cat-row">
        {home_cards}
      </div>
    </div>
  </section>

  <section class="section" id="hrs" style="--hm: 2" aria-labelledby="hrs-h">
    <div class="wrap grid grid--top">
      <div class="span-5 stack-6">
        <div class="section-head">
          <h2 id="hrs-h">Controladores de canal caliente</h2>
          <p>Control PID de cada boquilla del molde, de una zona a 128 en la misma unidad.</p>
        </div>
        <ul class="rows rows--links">{hrs_rows}</ul>
        <a class="link" href="hrs-controladores.html">Ver controladores</a>
      </div>
      <a class="frame frame--white span-6 start-7 big-product" href="serie-mtc-g.html" aria-label="Serie MTC-G">
        <img class="frame__img" src="{img_src("hrs-2.png")}" width="700" height="534" alt="Controlador de canal caliente Serie MTC-G de seis zonas" loading="lazy" data-source="client" data-subject="product">
      </a>
    </div>
  </section>

  <section class="section ground-inverse" id="resistencias" style="--hm: 2" aria-labelledby="res-h" data-moment="line-carries-colour" data-moment-opts='{{"from": "base"}}'>
    <div class="wrap grid grid--top">
      <div class="span-5 stack-6">
        <div class="section-head">
          <h2 id="res-h">Resistencias fabricadas a su medida</h2>
          <p>Envíe estos cinco datos y fabricamos la resistencia exacta para su husillo, boquilla o molde.</p>
        </div>
        <ul class="rows rows--spec">{res_rows}</ul>
        <a class="link" href="resistencias-electricas.html">Ver resistencias</a>
      </div>
      <div class="span-6 start-7 res-wall">{res_tiles}</div>
    </div>
  </section>

  <section class="section" id="eoat" style="--hm: 2" aria-labelledby="eoat-h">
    <div class="wrap grid grid--top">
      <div class="span-5 stack-6">
        <div class="section-head">
          <h2 id="eoat-h">Garras EOAT para robots de extracción</h2>
          <p>Combinamos pinzas, ventosas y perfilería para montar la garra de cada pieza y de cada robot.</p>
        </div>
        <ul class="rows rows--links">{eoat_rows}</ul>
        <a class="link" href="eoat-accesorio-robotica.html">Ver la gama EOAT</a>
      </div>
      <a class="frame frame--photo span-6 start-7 eoat-photo" href="eoat-accesorio-robotica.html" aria-label="Componentes EOAT">
        <img class="frame__img" src="assets/img/home-2.jpg" width="1000" height="1000" alt="Robot de extracción junto a una inyectora, con garra montada" loading="lazy" data-source="client" data-subject="robot at injection machine">
      </a>
    </div>
  </section>

  <section class="section ground-surface" id="servicio" aria-labelledby="servicio-h">
    <div class="wrap">
      <div class="section-head section-head--row">
        <h2 id="servicio-h">Recambios en 12 a 24 horas</h2>
        <a class="link" href="quienes-somos.html">Conocer la empresa</a>
      </div>
      <div class="grid service-cols">
        <div class="span-4"><h3>Asesoría para elegir controlador</h3><p>Le ayudamos a elegir la serie y la resistencia antes de la compra, y le atendemos después.</p></div>
        <div class="span-4"><h3>Envío de recambios al extranjero</h3><p>Más de 50 clientes en automoción, electrodomésticos, dispositivos médicos y envases.</p></div>
        <div class="span-4"><h3>Cajas de control para su molde</h3><p>Fabricamos cajas de control de temperatura ajustadas a su molde y a su producción.</p></div>
      </div>
      <div class="frame frame--photo fill plant-photo">
        <img class="frame__img" src="assets/img/photo-f74695444.jpg" srcset="assets/img/photo-f74695444-500.jpg 500w, assets/img/photo-f74695444-960.jpg 960w, assets/img/photo-f74695444.jpg 1280w" sizes="(max-width: 1279px) 100vw, 1280px" width="1280" height="853" alt="Nave con una fila de inyectoras de plástico" loading="lazy" decoding="async" data-source="stand-in" data-subject="injection moulding hall">
      </div>
    </div>
  </section>
</main>
''' + footer(scripts='<script type="module" src="assets/js/site.js"></script>\n'))

SITE_JS = '<script type="module" src="assets/js/site.js"></script>\n'


def inner(title, desc, active, body, close_line=None):
    kw = {"scripts": SITE_JS}
    if close_line:
        kw["close_line"] = close_line
    write_html = head(title, desc) + nav(active) + '<main id="top">\n<div class="page">\n' + body + '</div>\n</main>\n' + footer(**kw)
    return write_html


CUR = ' aria-current="page"'


def cat_tabs(active):
    return '<nav class="cat-tabs" aria-label="Categorías"><div class="wrap">' + "".join(
        f'<a href="{c["slug"]}.html"{CUR if c["slug"] == active else ""}>{E(c["name"])}</a>' for c in CATS
    ) + "</div></nav>\n"


def band(title, text, btn, href):
    return f'''<section class="pg-band ground-surface"><div class="wrap band-row">
  <div><h2>{E(title)}</h2><p>{E(text)}</p></div>
  <a class="btn btn--secondary" href="{href}">{E(btn)}</a>
</div></section>
'''

# ---------------------------------------------------------------------------
# Fichas de producto
# ---------------------------------------------------------------------------
def de(title):
    """«de la Serie», «del Anillo», «de las Pinzas», «de los Cambiadores»: concuerda con la primera palabra."""
    w = title.split()[0].lower()
    if w in ("cambiadores",):
        return f"de los {title}"
    if w.endswith("as"):
        return f"de las {title}"
    if w.endswith("a") or w in ("serie",):
        return f"de la {title}"
    return f"del {title}"


def render_section(sec, first, title=""):
    items = sec["items"]
    lis = [i for i in items if i["t"] == "li"]
    ps = [i for i in items if i["t"] == "p"]
    kvs = [i for i in items if i["t"] == "kv"]
    many_long = sum(len(i["v"]) > 110 for i in kvs) * 2 > len(kvs)
    short_kv = [] if many_long else kvs
    long_kv = kvs if many_long else []
    h = sec["h"] or ("Descripción" if first else "Más información")
    if title and len(h.split()) <= 2:
        h = f"{h} {de(title)}"
    body = "".join(f"<p>{E(p['v'])}</p>" for p in ps)
    if lis:
        body += '<ul class="rows rows--plain">' + "".join(f"<li><span>{E(i['v'])}</span></li>" for i in lis) + "</ul>"
    if short_kv:
        body += '<ul class="rows rows--spec">' + "".join(f'<li><span class="rows__name">{E(i["k"])}</span><span class="rows__value">{E(i["v"])}</span></li>' for i in short_kv) + "</ul>"
    if long_kv:
        body += '<div class="feat-grid">' + "".join(f'<div class="feat"><h4>{E(i["k"])}</h4><p>{E(i["v"])}</p></div>' for i in long_kv) + "</div>"
    return f'<section class="pdp-block"><h3>{E(h)}</h3>{body}</section>'


for slug, f in FICHAS.items():
    cat = CAT_BY_PRODUCT.get(slug)
    if not cat:
        continue
    imgs = list(dict.fromkeys(f["images"] or [CARD_IMG[slug]]))
    main_img = imgs[0]
    thumbs = ""
    if len(imgs) > 1:
        thumbs = '<div class="thumbs">' + "".join(
            f'<button type="button" data-gallery-thumb data-src="{img_src(i)}" aria-pressed="{"true" if n == 0 else "false"}" aria-label="Ver imagen {n+1}"><img src="{img_src(i)}" {wh(img_src(i))} alt="" loading="lazy"></button>'
            for n, i in enumerate(imgs[:10])) + "</div>"
    sections = [dict(s) for s in f["sections"]]
    lead = ""
    if sections and sections[0]["h"] is None and sections[0]["items"] and sections[0]["items"][0]["t"] == "p":
        lead = sections[0]["items"][0]["v"]
        sections[0] = {"h": None, "items": sections[0]["items"][1:]}
    if not lead:
        lead = cat["short"]
    sections = [s for s in sections if s["items"]]
    blocks = "".join(render_section(s, n == 0, f["title"]) for n, s in enumerate(sections))
    custom = ""
    if cat["slug"] == "resistencias-electricas":
        custom = '<p class="pdp-note">¿Necesita otra medida? Envíenos dimensiones, tensión, potencia, perforaciones y tipo de conexión.</p>'
    related = [it for it in cat["items"] if it[2] != slug][:4]
    rel_html = "".join(card(n, i, f"{s}.html" if s else contact_url(n, cat["name"])) for n, i, s, d in related)
    wa_text = quote(f"Hola, me interesa {f['title']} (System Plast). ¿Me pueden dar más información?")
    sub = f'<p class="pdp-sub">{E(f["subtitle"])}</p>' if f["subtitle"] else ""
    body = f'''<section class="pdp"><div class="wrap">
  <nav class="crumbs crumbs--light" aria-label="Migas de pan"><a href="index.html">Inicio</a><span aria-hidden="true">/</span><a href="productos.html">Productos</a><span aria-hidden="true">/</span><a href="{cat['slug']}.html">{E(cat['name'])}</a></nav>
  <div class="pdp-top">
    <div class="pdp-info" data-enter>
      <p class="t-label muted">{E(cat['name'])}</p>
      <h1>{E(f['title'])}</h1>{sub}
      <p class="pdp-lead">{E(lead)}</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{contact_url(f['title'], cat['name'])}">{MAIN_ACTION}{ARROW}</a>
        <a class="btn btn--secondary" href="https://wa.me/{TEL[1:]}?text={wa_text}" target="_blank" rel="noopener">{ICON['wa']} Escribir por WhatsApp</a>
      </div>
      {custom}
      <ul class="rows rows--spec pdp-assure">
        <li><span class="rows__name">Recambios</span><span class="rows__value">12 a 24 horas</span></li>
        <li><span class="rows__name">Asesoría técnica</span><span class="rows__value">Antes y después</span></li>
        <li><span class="rows__name">Envíos</span><span class="rows__value">A todo el mundo</span></li>
      </ul>
    </div>
    <div class="gallery"><div class="gallery-main"><img data-gallery-main src="{img_src(main_img)}" width="700" height="700" alt="{E(f['title'])}"></div>{thumbs}</div>
  </div>
  <h2 class="pdp-body-h">Características {E(de(f['title']))}</h2>
  <div class="pdp-body">{blocks}</div>
</div></section>
<section class="pg-section"><div class="wrap">
  <div class="section-head section-head--row"><h2>Más de {E(cat['name'].lower() if cat['slug'] != 'hrs-controladores' else 'HRS controladores')}</h2><a class="link" href="{cat['slug']}.html">Ver la categoría</a></div>
  <div class="prod-grid">{rel_html}</div>
</div></section>
'''
    write(f"{slug}.html", inner(f"{f['title']} | {cat['name']} | System Plast", (lead or cat["short"])[:155], "productos.html", body))

# ---------------------------------------------------------------------------
# Páginas de categoría
# ---------------------------------------------------------------------------
for c in CATS:
    t, s = c["hero"]
    bt, bx = c["band"]
    if any(it[1] for it in c["items"]):
        grid = '<div class="prod-grid">' + "".join(
            card(n, i, f"{sl}.html" if sl else contact_url(n, c["name"]), d) for n, i, sl, d in c["items"]) + "</div>"
    else:
        grid = '<div class="text-grid">' + "".join(
            f'<a class="text-card" href="{contact_url(n, c["name"])}"><h3>{E(n)}</h3><p>{E(d)}</p><span class="link">Pedir información</span></a>' for n, i, sl, d in c["items"]) + "</div>"
    body = page_head(t, s, [("Productos", "productos.html"), (c["name"], None)], video=True) + cat_tabs(c["slug"]) + \
        f'<section class="pg-section"><div class="wrap"><h2 class="grid-h">{len(c["items"])} productos de {E(c["name"])}</h2>{grid}</div></section>\n' + band(bt, bx, "Pedir el catálogo completo", "contacto.html")
    write(f"{c['slug']}.html", inner(f"{c['name']} | System Plast", c["short"], "productos.html", body))

# ---------------------------------------------------------------------------
# Productos
# ---------------------------------------------------------------------------
cats_html = "".join(card(c["name"], CAT_IMG[c["slug"]], f"{c['slug']}.html", CAT_LINE[c["slug"]]) for c in CATS)
body = page_head("Catálogo de componentes para inyectoras", "Controladores, resistencias, EOAT y estanterías para que sus procesos de inyección sean más eficientes y seguros.", [("Productos", None)], video=True) + \
    f'<section class="pg-section"><div class="wrap"><h2 class="grid-h">Cuatro líneas de producto</h2><div class="prod-grid">{cats_html}</div></div></section>\n' + \
    band("Soluciones a medida", "Diseñamos cajas de control y resistencias que se integran en su línea de producción tal como está.", "Contar su proyecto", "contacto.html")
write("productos.html", inner("Productos | System Plast", "Catálogo System Plast: controladores HRS de canal caliente, resistencias eléctricas, EOAT para robótica y estanterías para moldes.", "productos.html", body))

# ---------------------------------------------------------------------------
# Quiénes somos
# ---------------------------------------------------------------------------
logos = "".join(f'<img src="assets/img/industria-{i}.png" alt="{n}" loading="lazy">' for i, n in
                [(1, "Samsung"), (2, "Midea"), (3, "Valeo"), (4, "Gree"), (5, "Hasco"), (6, "Sharp")])
body = page_head("Quiénes somos", "20 años desarrollando y distribuyendo soluciones tecnológicas para la industria del plástico.", [("Quiénes somos", None)]) + f'''<section class="pg-section"><div class="wrap split-6">
  <div class="stack-5">
    <h2>Especialistas en control de temperatura para la inyección</h2>
    <p>En System Plast desarrollamos y distribuimos equipos para la industria del plástico: controladores de canal caliente, resistencias, garras EOAT y almacenaje de moldes.</p>
    <p>Con 20 años de experiencia y más de 50 clientes, acompañamos a cada fábrica antes, durante y después de la compra.</p>
  </div>
  <div class="frame frame--photo about-photo"><img class="frame__img" src="assets/img/home-2.jpg" width="1000" height="1000" alt="Célula de inyección con robot de extracción" loading="lazy"></div>
</div></section>
<section class="pg-section ground-surface"><div class="wrap split-6">
  <div class="stack-4"><h2>Liderazgo tecnológico</h2><p>Del equipo monozona al multizona y a los sistemas inteligentes: nuestros controladores de canal caliente usan algoritmos PID para un control estable, exacto y rápido de cada zona.</p></div>
  <div class="stack-4"><h2>Servicios personalizados</h2><p>Fabricamos cajas de control de temperatura a medida, ajustadas a cada molde y a la producción de cada cliente, para que encajen en su línea sin cambios.</p></div>
</div></section>
<section class="pg-section"><div class="wrap">
  <div class="section-head"><h2>Sectores que trabajan con nosotros</h2><p>Automoción, electrodomésticos, dispositivos médicos y envases.</p></div>
  <div class="logo-row">{logos}</div>
</div></section>
'''
write("quienes-somos.html", inner("Quiénes somos | System Plast", "20 años desarrollando y distribuyendo soluciones tecnológicas para la industria del plástico.", "quienes-somos.html", body))

# ---------------------------------------------------------------------------
# Noticias
# ---------------------------------------------------------------------------
news_html = "".join(f'<a class="card card--open card--prod news-card" href="{u}" target="_blank" rel="noopener"><div class="panel"><img class="frame__img" src="assets/img/{i}" alt="" loading="lazy"></div><p class="t-label muted">{E(src)}</p><h3>{E(t)}</h3></a>' for i, t, src, u in NEWS)
body = page_head("Noticias del sector", "Actualidad y tendencias de la industria del plástico.", [("Noticias", None)]) + \
    f'<section class="pg-section"><div class="wrap"><div class="news-grid">{news_html}</div></div></section>\n'
write("noticias.html", inner("Noticias | System Plast", "Noticias y tendencias de la industria del plástico.", "noticias.html", body))

# ---------------------------------------------------------------------------
# Contacto
# ---------------------------------------------------------------------------
opts = "".join(f"<option>{E(c['name'])}</option>" for c in CATS) + "<option>Otro / proyecto a medida</option>"
body = page_head("Presupuesto de controladores, resistencias y EOAT", "Cuéntenos qué necesita y le respondemos en 12 a 24 horas.", [("Contacto", None)]) + f'''<section class="pg-section"><div class="wrap split-6 contact">
  <div class="stack-5">
    <h2>Hablemos de su proyecto</h2>
    <p>Controladores de canal caliente, controladores de válvula secuencial, resistencias o EOAT: complete el formulario y un técnico le responderá.</p>
    <ul class="rows rows--spec">
      <li><span class="rows__name">Dirección</span><span class="rows__value">{DIR1}<br>{DIR2}</span></li>
      <li><span class="rows__name">Teléfono</span><span class="rows__value"><a class="link" href="tel:{TEL}">{TEL_TXT}</a></span></li>
      <li><span class="rows__name">Email</span><span class="rows__value"><a class="link" href="mailto:{MAIL}">{MAIL}</a></span></li>
      <li><span class="rows__name">WhatsApp</span><span class="rows__value"><a class="link" href="https://wa.me/{TEL[1:]}" target="_blank" rel="noopener">Escribir por WhatsApp</a></span></li>
    </ul>
  </div>
  <form class="form form-card" id="contact-form" action="mailto:{MAIL}" method="post" enctype="text/plain" data-endpoint="" novalidate>
    <div class="field"><label for="f-name">Nombre</label><input id="f-name" name="nombre" type="text" autocomplete="name" required aria-describedby="f-name-err"><p class="field__error" id="f-name-err" hidden>Escriba su nombre.</p></div>
    <div class="field"><label for="f-company">Empresa</label><input id="f-company" name="empresa" type="text" autocomplete="organization"></div>
    <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" inputmode="email" required aria-describedby="f-email-err"><p class="field__error" id="f-email-err" hidden>Escriba un email con @, por ejemplo nombre@empresa.com.</p></div>
    <div class="field"><label for="f-cat">Producto de interés</label><select id="f-cat" name="producto">{opts}</select></div>
    <div class="field"><label for="f-msg">Mensaje</label><textarea id="f-msg" name="mensaje" rows="5" required aria-describedby="f-msg-err"></textarea><p class="field__error" id="f-msg-err" hidden>Escriba qué producto o medida necesita.</p></div>
    <div class="btn-row"><button class="btn btn--primary" type="submit">{MAIN_ACTION}</button></div>
    <p class="form__status" role="status" data-form-status></p>
    <p class="t-small">Al enviar acepta que usemos sus datos solo para responder a esta consulta.</p>
  </form>
</div></section>
'''
write("contacto.html", inner("Contacto | System Plast", f"Contacte con System Plast en Mutxamel (Alicante): presupuestos de controladores, resistencias y EOAT.", "contacto.html", body))

# ---------------------------------------------------------------------------
# Créditos
# ---------------------------------------------------------------------------
body = page_head("Créditos", "Material de terceros usado en esta web.", [("Créditos", None)]) + '''<section class="pg-section"><div class="wrap measure stack-4">
  <ul class="rows rows--plain">
    <li><span>Vídeo de la portada: «Automated Manufacturing Equipment in Action», Pexels, vídeo 32386599, <a class="link" href="https://www.pexels.com/license/">licencia Pexels</a>.</span></li>
    <li><span>Nave de inyectoras: «Inside the factory», Orionpenindia, Wikimedia Commons, <a class="link" href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</span></li>
    <li><span>Molde de inyección: «HTS main frame polymer injection mold», MobiusDaXter, Wikimedia Commons, <a class="link" href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>.</span></li>
    <li><span>Las marcas y logotipos de clientes pertenecen a sus propietarios.</span></li>
  </ul>
</div></section>
'''
write("creditos.html", inner("Créditos | System Plast", "Licencias del vídeo y de las fotografías de terceros usadas en la web de System Plast.", None, body))

print("Páginas generadas:", len([f for f in os.listdir(OUT) if f.endswith(".html")]))
