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
# Dirección pública de la web. Cuando systemplas.com apunte a GitHub Pages, cámbiala aquí (y crea el archivo CNAME).
BASE_URL = "https://josemidev1-code.github.io/SystemPlas/"
# Envío del formulario de contacto (FormSubmit, sin cuenta). El primer envío manda a MAIL un correo de activación.
FORM_ENDPOINT = f"https://formsubmit.co/ajax/{MAIL}"
FORM_ACTION = f"https://formsubmit.co/{MAIL}"
WA_TEXT = "Hola, quiero información sobre sus productos (System Plast)."

ICON = {
 "wa": '<svg viewBox="0 0 32 32" aria-hidden="true" width="18" height="18"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7a.6.6 0 0 0 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" aria-hidden="true" width="18" height="18"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M5 3.5h3.2l1.6 4-2 1.3a11 11 0 0 0 5.4 5.4l1.3-2 4 1.6V17a2.5 2.5 0 0 1-2.7 2.5A16 16 0 0 1 2.5 6.2 2.5 2.5 0 0 1 5 3.5z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zm7 0h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.6c0-1.34-.02-3.06-1.86-3.06-1.87 0-2.15 1.46-2.15 2.96V21h-4z"/></svg>',
}
# Emblemas de servicio: marco octogonal grueso en dos tonos de verde petróleo, interior blanco y
# pictograma bicolor (idea tomada de los emblemas de la web de referencia, con forma y dibujo propios)
import math as _m
def _octa(r, c=60):
    pts = [(c + r * _m.cos(_m.radians(22.5 + 45 * k)), c + r * _m.sin(_m.radians(22.5 + 45 * k))) for k in range(8)]
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
SVC_PICTO = {
 "asesoria": '<path class="s" d="M38 62v-4a22 22 0 0 1 44 0v4"/><rect class="f" x="32" y="60" width="12" height="18" rx="4"/><rect class="f" x="76" y="60" width="12" height="18" rx="4"/><path class="s" d="M82 78v2a8 8 0 0 1-8 8h-8"/><circle class="d" cx="62" cy="88" r="3.5"/>',
 "recambios": '<rect class="f" x="30" y="46" width="34" height="26" rx="2"/><path class="s" d="M64 54h12l10 10v8H64z"/><circle class="d" cx="42" cy="78" r="6"/><circle class="d" cx="76" cy="78" r="6"/><path class="s" d="M36 56h14M36 63h20"/>',
 "medida": '<circle cx="60" cy="60" r="21" fill="none" stroke="#037c75" stroke-width="9" stroke-dasharray="6.6 9.9"/><circle class="f" cx="60" cy="60" r="17"/><circle cx="60" cy="60" r="6.5" fill="#fff" stroke="#012c3d" stroke-width="3.2"/>',
 "mundo": '<circle class="f" cx="60" cy="60" r="24"/><path class="s" d="M36 60h48M60 36c7 7 10.5 15 10.5 24S67 77 60 84c-7-7-10.5-15-10.5-24S53 43 60 36z"/><path class="s" d="M40 48h40M40 72h40"/>',
}
REELS = [("eoat-3", "Pinza neumática recogiendo una pieza"), ("eoat-2", "Garra con ventosas de vacío"),
         ("eoat-5", "Utillaje con muelles y ventosas"), ("eoat-4", "Utillaje con cableado neumático"),
         ("eoat-1", "Robot de extracción en movimiento")]
def reels_html():
    # Vídeos del cliente (WhatsApp, 2026-11-21), 8 s cada uno sin audio; se reproducen solo en pantalla (assets/js/reels.js)
    return '<div class="reels" data-reels>' + "".join(
        f'<figure class="reel"><video muted loop playsinline preload="none" poster="assets/video/{v}-poster.jpg" aria-label="{E(t)}">'
        f'<source src="assets/video/{v}.mp4" type="video/mp4"></video>'
        f'<button class="reel__btn reel-pause" type="button" aria-label="Reproducir: {E(t)}" aria-pressed="true" data-reel-btn data-pause></button></figure>'
        for v, t in REELS) + '</div>'
REELS_JS = '<script type="module" src="assets/js/reels.js"></script>\n'

CAT_PICTO = {
 "hrs": '<rect class="f" x="33" y="45" width="54" height="32" rx="3"/><path class="s" d="M50 45v-5h20v5M38 79v3M82 79v3"/>'
        + "".join(f'<rect x="{x}" y="49" width="10" height="24" rx="1.5" fill="#fff" stroke="#012c3d" stroke-width="2.4"/><rect x="{x+2}" y="52" width="6" height="5" fill="#037c75"/><circle cx="{x+5}" cy="66" r="2.2" fill="#012c3d"/>' for x in (37, 49, 61, 73))
        + '<path class="s" d="M87 69c7 0 7 9 1 11"/>',
 "res": '<path class="f" d="M36 55v15a21 7.5 0 0 0 42 0V55"/><ellipse cx="57" cy="55" rx="21" ry="7.5" fill="#fff" stroke="#037c75" stroke-width="3.2"/><ellipse cx="57" cy="55" rx="13.5" ry="4.2" fill="#012c3d"/><rect x="74" y="58" width="8" height="15" rx="1.5" fill="#fff" stroke="#012c3d" stroke-width="2.4"/><circle cx="78" cy="62" r="1.6" fill="#012c3d"/><circle cx="78" cy="69" r="1.6" fill="#012c3d"/><path class="s" d="M82 65c6 0 6-12 2-18"/><rect class="f" x="78" y="38" width="11" height="9" rx="1.5"/>',
 "eoat": '<rect x="53" y="33" width="14" height="9" rx="2" fill="#012c3d"/><rect class="f" x="49" y="42" width="22" height="6" rx="2"/><rect class="f" x="57" y="48" width="6" height="27"/><rect class="f" x="33" y="56" width="54" height="6"/><path class="s" d="M37 62v6M83 62v6M60 75v5"/><path class="d" d="M31 68h12l-2 5h-8z"/><path class="d" d="M77 68h12l-2 5h-8z"/><path class="d" d="M54 80h12l-2 5h-8z"/>',
 "est": '<rect x="33" y="34" width="4.5" height="52" rx="1" fill="#012c3d"/><rect x="82.5" y="34" width="4.5" height="52" rx="1" fill="#012c3d"/><rect class="f" x="36" y="50" width="48" height="3.5"/><rect class="f" x="36" y="67" width="48" height="3.5"/><rect class="f" x="36" y="82" width="48" height="3.5"/>'
        + "".join(f'<rect x="{x}" y="{y}" width="17" height="11" rx="1.5" fill="#fff" stroke="#012c3d" stroke-width="2.4"/><rect x="{x}" y="{y}" width="17" height="3.6" fill="#037c75"/>' for x in (41, 62) for y in (38.5, 55.5))
        + '<rect x="41" y="71.5" width="17" height="10" rx="1.5" fill="#fff" stroke="#012c3d" stroke-width="2.4"/><rect x="41" y="71.5" width="17" height="3.4" fill="#037c75"/>',
}
CAT_KEY = {"hrs-controladores": "hrs", "resistencias-electricas": "res", "eoat-accesorio-robotica": "eoat", "estanterias-moldes": "est"}

def badge(key):
    return (f'<svg class="emb" viewBox="0 0 120 120" aria-hidden="true">'
            f'<defs><linearGradient id="bg-{key}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#037c75"/><stop offset=".56" stop-color="#037c75"/>'
            f'<stop offset=".56" stop-color="#5fb0a9"/><stop offset="1" stop-color="#5fb0a9"/></linearGradient></defs>'
            f'<path class="emb__frame" fill="url(#bg-{key})" fill-rule="evenodd" d="{_octa(58)} {_octa(44)}"/>'
            f'<path class="emb__in" d="{_octa(44)}"/><g class="emb__picto" transform="translate(60 60) scale(1.14) translate(-60 -60)">{SVC_PICTO.get(key) or CAT_PICTO[key]}</g></svg>')
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

# Foto de tarjeta de categoría. Estanterías: foto del cliente (2026-11-21), estantería sobre blanco (web/sin-fondo/est-1.jpg)
CAT_IMG = {"hrs-controladores": "hrs-1.png", "resistencias-electricas": "res-2.png",
           "eoat-accesorio-robotica": "eoat-3.png", "estanterias-moldes": "est-1.png"}
STOCK_CAT = set()
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


PAGES = []


def page_url(name):
    return BASE_URL if name == "index.html" else BASE_URL + name


def write(name, body):
    if name != "404.html":
        PAGES.append(name)
    url = page_url(name)
    tags = "" if name == "404.html" else f'<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">'
    body = body.replace("<!--URL-->", tags, 1)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)


# ---------------------------------------------------------------------------
# Cabecera, navegación y pie comunes
# ---------------------------------------------------------------------------
# Paso entre páginas: en la página que llega, la foto del producto recibe el nombre compartido antes del
# primer pintado (por eso va en línea en el <head>; site.js nombra la de la página que se va).
VT_HEAD = """<script>(()=>{const n=window.navigation;if(!n||!('onpagereveal' in window))return;const l=document.createElement('link');l.rel='expect';l.href='#vt-parsed';l.setAttribute('blocking','render');document.head.append(l);const P=s=>s.replace(/\\/index\\.html$/,'/');const same=(a,b)=>{try{const x=new URL(a,location.href),y=new URL(b,location.href);return x.origin===y.origin&&P(x.pathname)===P(y.pathname)}catch(e){return false}};addEventListener('pagereveal',e=>{const vt=e.viewTransition,f=n.activation&&n.activation.from;if(!vt||!f||matchMedia('(prefers-reduced-motion: reduce)').matches)return;let el=null;for(const a of document.querySelectorAll('a.card[href]'))if(same(a.href,f.url)){el=a.querySelector('.frame__img,img');break}el=el||document.querySelector('[data-gallery-main]');if(!el)return;const r=el.getBoundingClientRect();if(!r.height||r.bottom<0||r.top>innerHeight)return;el.style.viewTransitionName='product-photo';document.documentElement.dataset.vtArrive='1';const c=()=>{el.style.viewTransitionName='';delete document.documentElement.dataset.vtArrive};vt.finished.then(c,c)})})()</script>"""

LOCAL_BUSINESS = {
    "@context": "https://schema.org", "@type": "LocalBusiness", "@id": BASE_URL + "#empresa",
    "name": "System Plast", "url": BASE_URL, "logo": BASE_URL + "assets/img/logo-320.png", "image": BASE_URL + "share.jpg",
    "description": "Controladores de canal caliente, resistencias eléctricas a medida, EOAT y estanterías para moldes de inyección de plástico.",
    "telephone": TEL, "email": MAIL,
    "address": {"@type": "PostalAddress", "streetAddress": DIR1, "postalCode": "03110", "addressLocality": "Mutxamel",
                "addressRegion": "Alicante", "addressCountry": "ES"},
    "sameAs": [LINKEDIN],
}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"


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
<meta property="og:image" content="{BASE_URL}share.jpg">
<meta property="og:site_name" content="System Plast">
<meta property="og:locale" content="es_ES">
<!--URL-->
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#f4f6f6">
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
<link rel="stylesheet" href="assets/css/decor.css">
<script type="module" src="assets/js/entrance.js"></script>
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
  <a class="skip-link" href="#top">Saltar al contenido</a>
  <div class="nav__top"><div class="wrap nav__top-in">
    <span>{DIR1} · {DIR2}</span>
    <a href="tel:{TEL}">{TEL_TXT}</a>
    <a href="mailto:{MAIL}">{MAIL}</a>
    <a class="nav__top-in-social" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON["linkedin"]}</a>
  </div></div>
  <div class="wrap nav__bar">
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
    return f'''<footer class="footer closing" id="contact" aria-labelledby="close-h">
  <div class="wrap">
    <div class="closing__cta close--word close--band">
      <img class="close__bg" src="assets/img/photo-f74695444.jpg" width="1280" height="853" alt="" loading="lazy" decoding="async" data-source="stand-in" data-subject="injection moulding hall">
      <div class="close__in">
        <h2 id="close-h">Presupuesto para su línea de inyección</h2><p class="t-lead">{E(close_line)}</p>
        <div class="btn-row"><a class="btn btn--primary" href="contacto.html">{MAIN_ACTION}{ARROW}</a><a class="btn btn--secondary" href="tel:{TEL}">Llamar al {TEL_TXT}</a></div>
      </div>
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
<a class="wa-float" href="https://wa.me/{TEL[1:]}?text={quote(WA_TEXT)}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{ICON["wa"]}<span>WhatsApp</span></a>
<nav class="actionbar" aria-label="Acciones rápidas">
  <a class="btn btn--secondary actionbar__call" href="tel:{TEL}" aria-label="Llamar">{ICON["phone"]}<span>Llamar</span></a>
  <a class="btn btn--secondary" href="https://wa.me/{TEL[1:]}?text={quote(WA_TEXT)}" target="_blank" rel="noopener">{ICON["wa"]}<span>WhatsApp</span></a>
  <a class="btn btn--primary" href="contacto.html">Presupuesto</a>
</nav>
<script type="module" src="assets/system.js"></script>
<script type="module" src="assets/motion/motion.js"></script>
<script type="module" src="assets/layout/layout.js"></script>
{scripts}</body>
</html>
'''


def page_head(title, lead, crumbs=(), video=False, photo=None):
    trail = ""
    if crumbs:
        parts = ['<a href="index.html">Inicio</a>']
        for label, href in crumbs:
            parts.append(f'<a href="{href}">{E(label)}</a>' if href else f'<span aria-current="page">{E(label)}</span>')
        trail = '<nav class="crumbs" aria-label="Migas de pan">' + '<span aria-hidden="true">/</span>'.join(parts) + '</nav>'
    if photo:
        # Cabecera con foto de fondo bajo el velo verde (catálogo: el robot de extracción, accesorios EOAT)
        src, alt = photo
        return f'''<header class="pg-head pg-head--video pg-head--photo" data-enter>
  <img class="pg-head__bg" src="{src}" srcset="{src[:-4]}-700.jpg 700w, {src} 1112w" sizes="100vw" width="1112" height="1200" alt="{E(alt)}" fetchpriority="high">
  <div class="wrap">{trail}<h1>{E(title)}</h1><p class="t-lead">{E(lead)}</p></div>
  <div class="decor-grid" aria-hidden="true"></div>
  <div class="decor-ruler" aria-hidden="true"></div>
</header>
'''
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
  <div class="decor-grid" aria-hidden="true"></div>
  <div class="decor-ruler" aria-hidden="true"></div>
</header>
'''
    return f'''<header class="pg-head ground-inverse" data-enter>
  <div class="wrap">{trail}<h1>{E(title)}</h1><p class="t-lead">{E(lead)}</p></div>
  <div class="decor-grid" aria-hidden="true"></div>
  <div class="decor-ruler" aria-hidden="true"></div>
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
<link rel="modulepreload" href="assets/moments/picture-develops/moment.js">
'''

def row_link(name, value, href):
    return f'<li><a class="rows__link" href="{href}"><span class="rows__name">{E(name)}</span><span class="rows__value">{E(value)}</span></a></li>'

home_cards = "".join(f'''<a class="card card--open card--prod cat-card span-3" href="{c["slug"]}.html">
          <span class="cat-card__emb">{badge(CAT_KEY[c["slug"]])}</span>
          <div class="cat-card__body"><h3>{E(c["name"])}</h3><p>{E(CAT_LINE[c["slug"]])}</p><span class="more">Ver productos{ARROW}</span></div>
        </a>''' for n, c in enumerate(CATS))

HOME_LOGOS = "".join(f'<img src="assets/img/industria-{i}.png" alt="{n}" width="300" height="300" loading="lazy">' for i, n in
                     [(1, "Samsung"), (2, "Midea"), (3, "Valeo"), (4, "Gree"), (5, "Hasco"), (6, "Sharp")])
HOME_NEWS = "".join(f'''<a class="news-card2" href="{u}" target="_blank" rel="noopener">
          <span class="news-card2__img"><img src="assets/img/{i[:-4]}-820.jpg" srcset="assets/img/{i[:-4]}-480.jpg 480w, assets/img/{i[:-4]}-820.jpg 820w" sizes="(max-width: 639px) 100vw, (max-width: 1023px) 50vw, 410px" width="820" height="820" alt="" loading="lazy" decoding="async"></span>
          <span class="news-card2__body"><span class="t-label">{E(src)}</span><h3>{E(t)}</h3><span class="more">Leer la noticia{ARROW}</span></span>
        </a>''' for i, t, src, u in NEWS)

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
                         HOME_EXTRA + ld(LOCAL_BUSINESS)) + nav() + f'''<!-- type: product (hardware, site-kind tech)
     deal: hero photo con vídeo de fondo (el cliente pide un vídeo de máquinas detrás, como Botbox; sustituye al hero product repartido),
     nav nav-cards, close close-word, footer footer-columns, rhythm dark-band, buttons solid, mark: logo del cliente
     palette: colores del logo (start.mjs brand), type plex, radius sharp
     moments: line-carries-colour en #resistencias (la franja oscura) -->
<main id="top">
  <section class="hero hero--photo" data-enter data-calm="left" data-box="none" data-tone="dark" aria-labelledby="hero-h">
    <!-- VÍDEO: Pexels 32386599 (licencia Pexels, uso libre). Se cambia aquí por el vídeo propio del cliente. -->
    <video class="hero__bg" autoplay muted loop playsinline preload="metadata" poster="assets/video/maquina-poster.jpg" aria-hidden="true" style="--ly-pos: 70% 50%; --ly-pos-phone: 70% 50%" data-source="stand-in" data-subject="vacuum gripper on an automated line">
      <source src="assets/video/maquina-640.mp4" type="video/mp4" media="(max-width: 639px)">
      <source src="assets/video/maquina-720.mp4" type="video/mp4">
    </video>
    <div class="wrap"><div class="hero-text">
      <div class="hero__text">
        <!-- Texto del cliente (2026-11-21), su opción 1: la portada empuja los accesorios de robot (EOAT) -->
        <h1 id="hero-h">Precisión y velocidad en cada movimiento</h1>
        <p class="hero__lead">Garras, vacío y soluciones EOAT a medida con las mejores marcas del mercado.</p>
        <div class="btn-row"><a class="btn btn--primary" href="contacto.html">Solicita asesoramiento{ARROW}</a><a class="btn btn--secondary" href="productos.html">Ver catálogo</a></div>
      </div>
      <button class="loop-pause hero-pause" type="button" aria-label="Pausar el vídeo" aria-pressed="false" data-video-pause></button>
    </div></div>
  </section>

  <section class="section ground-surface" id="catalogo" aria-labelledby="catalogo-h">
    <div class="wrap">
      <div class="section-head section-head--center">
        <h2 id="catalogo-h">Nuestras líneas de producto</h2>
        <p>Cuatro gamas para la inyectora, el molde y el robot de extracción.</p>
      </div>
      <div class="grid fill cat-row emb-set">
        {home_cards}
      </div>
    </div>
  </section>

  <section class="section intro" id="empresa" aria-labelledby="empresa-h">
    <div class="wrap intro__in">
      <h2 id="empresa-h">20 años al lado de la inyección de plástico</h2>
      <p class="intro__text">Desarrollamos y distribuimos <strong>equipos de control de temperatura</strong> y <strong>componentes para inyectoras</strong>: controladores de canal caliente, resistencias fabricadas a medida, garras EOAT y almacenaje de moldes. Le asesoramos <strong>antes, durante y después de la compra</strong>.</p>
      <ul class="stats">
        <li><strong data-count="20">20</strong><span>años de experiencia</span></li>
        <li><strong data-count="50" data-prefix="+">+50</strong><span>clientes industriales</span></li>
        <li><strong data-count="128">128</strong><span>zonas por controlador</span></li>
        <li><strong data-count="24" data-suffix=" h">24 h</strong><span>para enviar recambios</span></li>
      </ul>
      <div class="logos" aria-label="Algunos clientes">{HOME_LOGOS}</div>
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
      <a class="frame frame--photo span-6 start-7 eoat-photo" data-moment="picture-develops" data-moment-opts='{{"look": "film"}}' href="eoat-accesorio-robotica.html" aria-label="Componentes EOAT">
        <img class="frame__img" src="assets/img/eoat-garra-1.jpg" srcset="assets/img/eoat-garra-1-700.jpg 700w, assets/img/eoat-garra-1.jpg 1112w" sizes="(max-width: 1023px) 100vw, 50vw" width="1112" height="1200" alt="Garra EOAT con pinzas y ventosas montada sobre perfiles de aluminio" loading="lazy" data-source="client" data-subject="EOAT gripper">
      </a>
    </div>
  </section>

  <section class="section reels-sec" id="eoat-video" aria-labelledby="eoatv-h">
    <div class="wrap">
      <div class="section-head section-head--center">
        <h2 id="eoatv-h">Garras EOAT en acción</h2>
        <p>Montajes reales de pinzas, ventosas y utillajes para robots de extracción.</p>
      </div>
      {reels_html()}
    </div>
  </section>

  <section class="section ground-surface" id="servicio" aria-labelledby="servicio-h">
    <div class="wrap">
      <div class="section-head section-head--center">
        <h2 id="servicio-h">Servicios</h2>
        <p>Le acompañamos desde la elección del equipo hasta el recambio urgente.</p>
      </div>
      <div class="svc emb-set">
        <div class="svc__item"><span class="svc__badge">{badge("asesoria")}</span><h3>Asesoría técnica</h3><p>Le ayudamos a elegir la serie de controlador y la resistencia adecuadas antes de la compra.</p><a class="btn btn--secondary btn--sm" href="contacto.html">Consultar a un técnico</a></div>
        <div class="svc__item"><span class="svc__badge">{badge("recambios")}</span><h3>Recambios urgentes</h3><p>Stock en Mutxamel y envío de recambios en 12 a 24 horas para que su línea no pare.</p><a class="btn btn--secondary btn--sm" href="contacto.html">Pedir un recambio</a></div>
        <div class="svc__item"><span class="svc__badge">{badge("medida")}</span><h3>Fabricación a medida</h3><p>Resistencias y cajas de control de temperatura ajustadas a su molde y a su producción.</p><a class="btn btn--secondary btn--sm" href="resistencias-electricas.html">Ver resistencias</a></div>
        <div class="svc__item"><span class="svc__badge">{badge("mundo")}</span><h3>Envío internacional</h3><p>Clientes en automoción, electrodomésticos, dispositivos médicos y envases fuera de España.</p><a class="btn btn--secondary btn--sm" href="quienes-somos.html">Conocer la empresa</a></div>
      </div>
    </div>
  </section>

  <section class="section" id="noticias" aria-labelledby="noticias-h">
    <div class="wrap">
      <div class="section-head section-head--center">
        <h2 id="noticias-h">Noticias del sector</h2>
        <p>Lo que se mueve en la industria del plástico.</p>
      </div>
      <div class="news-row">{HOME_NEWS}</div>
      <p class="news-more"><a class="link" href="noticias.html">Ver todas las noticias</a></p>
    </div>
  </section>
<span id="vt-parsed" hidden></span>
</main>
''' + footer(scripts='<script type="module" src="assets/js/site.js"></script>\n<script type="module" src="assets/js/home-motion.js"></script>\n' + REELS_JS))

SITE_JS = '<script type="module" src="assets/js/site.js"></script>\n'


def inner(title, desc, active, body, close_line=None, extra="", scripts=""):
    kw = {"scripts": SITE_JS + scripts}
    if close_line:
        kw["close_line"] = close_line
    write_html = head(title, desc, extra) + nav(active) + '<main id="top">\n<div class="page">\n' + body + '</div>\n<span id="vt-parsed" hidden></span>\n</main>\n' + footer(**kw)
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
    body = f'''<section class="pdp" data-enter><div class="wrap">
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
    product_ld = ld({"@context": "https://schema.org", "@type": "Product", "name": f["title"], "description": lead[:300],
                     "image": [BASE_URL + img_src(i) for i in imgs[:5]], "category": cat["name"],
                     "brand": {"@type": "Brand", "name": "System Plast"}, "url": page_url(f"{slug}.html")})
    write(f"{slug}.html", inner(f"{f['title']} | {cat['name']} | System Plast" if len(f"{f['title']} | {cat['name']} | System Plast") <= 60 else f"{f['title']} | System Plast", (lead or cat["short"])[:155], "productos.html", body, extra=product_ld))

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
    photos = ""
    if c["slug"] == "eoat-accesorio-robotica":
        photos = f'''<section class="pg-section est-photos reels-page"><div class="wrap">
  <h2 class="grid-h">Garras EOAT en acción</h2>
  {reels_html()}
</div></section>
'''
    elif c["slug"] == "estanterias-moldes":
        photos = '''<section class="pg-section est-photos"><div class="wrap est-pair">
  <figure class="est-ph"><img src="assets/img/est-planta.jpg" srcset="assets/img/est-planta-640.jpg 640w, assets/img/est-planta.jpg 1280w" sizes="(max-width: 767px) 100vw, 50vw" width="1280" height="853" alt="Estantería de cajones extraíbles con moldes de inyección en una nave" loading="lazy" decoding="async"></figure>
  <figure class="est-ph"><img src="assets/img/est-moldes.jpg" srcset="assets/img/est-moldes-640.jpg 640w, assets/img/est-moldes.jpg 1280w" sizes="(max-width: 767px) 100vw, 50vw" width="1280" height="960" alt="Estantería para moldes cargada con moldes en sus tres niveles" loading="lazy" decoding="async"></figure>
</div></section>
'''
    body = page_head(t, s, [("Productos", "productos.html"), (c["name"], None)], video=True) + cat_tabs(c["slug"]) + photos + \
        f'<section class="pg-section"><div class="wrap"><h2 class="grid-h">{len(c["items"])} productos de {E(c["name"])}</h2>{grid}</div></section>\n' + band(bt, bx, "Pedir el catálogo completo", "contacto.html")
    write(f"{c['slug']}.html", inner(f"{c['name']} | System Plast", c["short"], "productos.html", body, scripts=REELS_JS if c["slug"] == "eoat-accesorio-robotica" else ""))

# ---------------------------------------------------------------------------
# Productos
# ---------------------------------------------------------------------------
cats_html = "".join(card(c["name"], CAT_IMG[c["slug"]], f"{c['slug']}.html", CAT_LINE[c["slug"]]) for c in CATS)
body = page_head("Accesorios EOAT para su robot de extracción", "Garras, ventosas y cambiadores rápidos para montar la garra de cada pieza, junto a todo lo que necesita su inyectora.", [("Productos", None)], photo=("assets/img/eoat-garra-2.jpg", "Garra EOAT con ventosas de vacío sobre el suelo de la nave")) + \
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
  <div class="frame frame--photo about-photo" data-moment="picture-develops" data-moment-opts='{{"look": "film"}}'><img class="frame__img" src="assets/img/home-2.jpg" width="1000" height="1000" alt="Célula de inyección con robot de extracción" loading="lazy"></div>
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
news_html = "".join(f'''<a class="news-card2" href="{u}" target="_blank" rel="noopener"><span class="news-card2__img"><img src="assets/img/{i[:-4]}-820.jpg" srcset="assets/img/{i[:-4]}-480.jpg 480w, assets/img/{i[:-4]}-820.jpg 820w" sizes="(max-width: 639px) 100vw, (max-width: 1023px) 50vw, 410px" width="820" height="820" alt="" loading="lazy" decoding="async"></span><span class="news-card2__body"><span class="t-label">{E(src)}</span><h2 class="card__title">{E(t)}</h2><span class="more">Leer la noticia{ARROW}</span></span></a>''' for i, t, src, u in NEWS)
body = page_head("Noticias del sector", "Actualidad y tendencias de la industria del plástico.", [("Noticias", None)]) + \
    f'<section class="pg-section"><div class="wrap"><div class="news-row news-row--page">{news_html}</div></div></section>\n'
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
  <form class="form form-card" id="contact-form" action="{FORM_ACTION}" method="post" data-endpoint="{FORM_ENDPOINT}" data-sending="Enviando…" data-sent="Mensaje enviado. Le responderemos en 12 a 24 horas." data-failed="No se ha podido enviar. Su mensaje sigue aquí: inténtelo de nuevo o escríbanos por WhatsApp." data-fix="Revise {{n}} campo(s) marcados." novalidate>
    <input type="hidden" name="_subject" value="Nueva consulta desde la web de System Plast">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_next" value="{BASE_URL}contacto.html?enviado=1">
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
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
write("contacto.html", inner("Contacto | System Plast", f"Contacte con System Plast en Mutxamel (Alicante): presupuestos de controladores, resistencias y EOAT.", "contacto.html", body, extra=ld(LOCAL_BUSINESS)))

# ---------------------------------------------------------------------------
# Créditos
# ---------------------------------------------------------------------------
body = page_head("Créditos", "Material de terceros usado en esta web.", [("Créditos", None)]) + '''<section class="pg-section"><div class="wrap measure stack-4">
  <ul class="rows rows--plain">
    <li><span>Vídeo de la portada: «Automated Manufacturing Equipment in Action», Pexels, vídeo 32386599, <a class="link" href="https://www.pexels.com/license/">licencia Pexels</a>.</span></li>
    <li><span>Nave de inyectoras: «Inside the factory», Orionpenindia, Wikimedia Commons, <a class="link" href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</span></li>
    <li><span>Las marcas y logotipos de clientes pertenecen a sus propietarios.</span></li>
  </ul>
</div></section>
'''
write("creditos.html", inner("Créditos | System Plast", "Licencias del vídeo y de las fotografías de terceros usadas en la web de System Plast.", None, body))

# ---------------------------------------------------------------------------
# 404, sitemap.xml y robots.txt
# ---------------------------------------------------------------------------
body = page_head("Página no encontrada", "La dirección que busca no existe o ha cambiado de sitio.") + f'''<section class="pg-section"><div class="wrap measure stack-5">
  <p>Puede volver al inicio, ver el catálogo completo o escribirnos y le ayudamos a encontrar la pieza.</p>
  <div class="btn-row"><a class="btn btn--primary" href="productos.html">Ver el catálogo{ARROW}</a><a class="btn btn--secondary" href="contacto.html">Contactar</a></div>
</div></section>
'''
# GitHub Pages sirve 404.html en cualquier ruta: <base> hace que sus enlaces relativos funcionen desde ahí
write("404.html", inner("Página no encontrada | System Plast", "La página que busca no existe.", None, body,
                        extra=f'<base href="{BASE_URL}">\n<meta name="robots" content="noindex">\n'))

skip = {"creditos.html"}
urls = "".join(f"  <url><loc>{page_url(n)}</loc></url>\n" for n in sorted(set(PAGES), key=lambda n: (n != "index.html", n)) if n not in skip)
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
    fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
    fh.write(f"User-agent: *\nDisallow: /assets/ui/_lab/\nDisallow: /assets/backgrounds/demo.html\nDisallow: /assets/backgrounds/check.html\n\nSitemap: {BASE_URL}sitemap.xml\n")

print("Páginas generadas:", len([f for f in os.listdir(OUT) if f.endswith(".html")]))
