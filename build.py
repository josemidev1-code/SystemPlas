"""
Generador de la web de SYSTEM PLAST.
Edita los datos de este archivo o data/productos.json y ejecuta:  python3 build.py
"""
import os, html, json
from urllib.parse import quote

OUT = os.path.dirname(os.path.abspath(__file__))
E = html.escape
ACT = ' class="active"'
FICHAS = json.load(open(os.path.join(OUT, "data", "productos.json"), encoding="utf-8"))

TEL = "+34627967729"
TEL_TXT = "(+34) 627 96 77 29"
MAIL = "info@systemplas.com"
DIR1, DIR2 = "Pol. Ind. Riodil, 1", "03110 Mutxamel, Alicante"
LINKEDIN = "https://www.linkedin.com/company/system-plas/"

ICON = {
 "pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
 "wa": '<svg viewBox="0 0 32 32"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7a.6.6 0 0 0 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zm7 0h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.6c0-1.34-.02-3.06-1.86-3.06-1.87 0-2.15 1.46-2.15 2.96V21h-4z"/></svg>',
 "rack": '<svg class="thumb-placeholder" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M10 6v52M54 6v52M10 20h44M10 36h44M10 52h44"/><rect x="16" y="10" width="14" height="10"/><rect x="34" y="26" width="16" height="10"/><rect x="18" y="42" width="20" height="10"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>',
 "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
 "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="M8.2 13.2 7 22l5-3 5 3-1.2-8.8"/></svg>',
 "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3 6 6.5 1-4.7 4.6 1.1 6.4L12 17l-5.9 3 1.1-6.4L2.5 9 9 8z"/></svg>',
 "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.2 4.2l2.9 2.9M16.9 16.9l2.9 2.9M1 12h4M19 12h4M4.2 19.8l2.9-2.9M16.9 7.1l2.9-2.9"/></svg>',
}

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
CAT_BY_PRODUCT = {it[2]: c for c in CATS for it in c["items"] if it[2]}
CARD_IMG = {it[2]: it[1] for c in CATS for it in c["items"] if it[2]}

NAV = [("index.html", "Inicio"), ("productos.html", "Productos"), ("quienes-somos.html", "Quiénes somos"), ("noticias.html", "Noticias"), ("contacto.html", "Contacto")]

NEWS = [
 ("agencia-6.jpg", "Un catalizador abre la puerta al reciclaje de plásticos sin clasificación previa", "Residuos Profesional", "https://www.residuosprofesional.com/catalizador-reciclaje-plasticos-sin-clasificacion-previa/"),
 ("agencia-7.jpg", "Tendencias en envases plásticos 2025: sostenibilidad e innovación", "Smartco", "https://smartco.mx/tendencias-de-empaque-2025-innovacion-sostenibilidad-y-eficiencia/"),
 ("agencia-8.jpg", "Informe del mercado mundial de envases biodegradables y su crecimiento proyectado", "Mordor Intelligence", "https://www.mordorintelligence.com/es/industry-reports/gobal-biodegradable-packaging-solutions-market-industry"),
]

# ---------------------------------------------------------------------------
def head(title, desc):
    return f'''<!doctype html>
<html lang="es" class="no-js">
<head>
<meta charset="utf-8">
<script>document.documentElement.className="js"</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="assets/img/logo.png">
<link rel="icon" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
'''

def header(active):
    items = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        if label == "Productos":
            sub = "".join(f'<li><a href="{c["slug"]}.html">{E(c["name"])}</a></li>' for c in CATS)
            items.append(f'<li class="has-sub"><a href="productos.html"{cls}>Productos</a><ul class="submenu">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return f'''<div class="topbar"><div class="container">
  <span class="addr">{ICON["pin"]} {DIR1} · {DIR2} · España</span>
  <a href="tel:{TEL}">{ICON["phone"]} {TEL_TXT}</a>
  <a href="mailto:{MAIL}">{ICON["mail"]} {MAIL}</a>
</div></div>
<header class="header"><div class="container">
  <a class="logo" href="index.html" aria-label="System Plast - inicio"><img src="assets/img/logo.png" alt="System Plast" width="600" height="260"></a>
  <button class="menu-toggle" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="nav"><ul>{"".join(items)}</ul><a class="btn btn-primary" href="contacto.html">Contáctanos</a></nav>
</div></header>
'''

CTA = '''<section class="cta" style="background-image:url(assets/img/home-2.jpg)"><div class="container">
  <h2>Innovamos contigo</h2>
  <p>Nuestras <strong>soluciones a medida</strong> garantizan una integración perfecta con las líneas de producción de nuestros clientes, lo que les permite obtener <strong>una ventaja competitiva en el mercado</strong>. Cuéntanos tu proyecto.</p>
  <a class="btn" href="contacto.html">Contacto</a>
</div></section>
'''

def footer():
    return f'''<footer class="footer"><div class="container footer-grid">
  <div>
    <h4>System Plast</h4>
    <p>Innovación en sistemas de control y plásticos industriales. Respuesta y recambios en 12 a 24 horas.</p>
    <div class="socials"><a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON["linkedin"]}</a><a href="https://wa.me/{TEL[1:]}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON["wa"]}</a><a href="mailto:{MAIL}" aria-label="Email">{ICON["mail"]}</a></div>
    <a class="footer-logo" href="index.html"><img src="assets/img/logo.png" alt="System Plast"></a>
  </div>
  <div>
    <h4>Contacto</h4>
    <address>{DIR1}<br>{DIR2} · España<br>
    <a href="tel:{TEL}">{TEL_TXT}</a><br>
    <a href="mailto:{MAIL}">{MAIL}</a></address>
  </div>
  <div>
    <h4>Productos</h4>
    <ul class="footer-links">{"".join(f'<li><a href="{c["slug"]}.html">{E(c["name"])}</a></li>' for c in CATS)}</ul>
  </div>
</div>
<div class="footer-bottom"><div class="container">© 2026 SYSTEM PLAST · <a href="#">Aviso legal</a> · <a href="#">Política de privacidad</a> · <a href="#">Política de cookies</a></div></div>
</footer>
<a class="whatsapp" href="https://wa.me/{TEL[1:]}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{ICON["wa"]}</a>
<button class="to-top" aria-label="Volver arriba">↑</button>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

def hero(title, sub, compact=False):
    cls = "hero hero--compact" if compact else "hero"
    return f'''<section class="{cls}" style="background-image:url(assets/img/home-2.jpg)"><div class="container">
  <h1>{E(title)}</h1><p>{E(sub)}</p>
</div></section>
'''

def crumbs(*parts):
    out = ['<a href="index.html">Inicio</a>']
    for i, (label, href) in enumerate(parts):
        out.append("<span>›</span>")
        out.append(f'<span aria-current="page">{E(label)}</span>' if href is None else f'<a href="{href}">{E(label)}</a>')
    return f'<nav class="crumbs" aria-label="Migas de pan"><div class="container">{"".join(out)}</div></nav>\n'

def contact_url(prod, cat):
    return f"contacto.html?producto={quote(prod)}&cat={quote(cat)}"

def img_src(name):
    """Ruta de la foto: la versión sin mancha verde si existe, si no la original."""
    if os.path.exists(os.path.join(OUT, "assets", "img", "sin-fondo", name)):
        return f"assets/img/sin-fondo/{name}"
    return f"assets/img/{name}"

def card(title, img, href):
    inner = f'<img src="{img_src(img)}" alt="{E(title)}" loading="lazy">' if img else ICON["rack"]
    return f'<a class="product-card" href="{href}"><div class="thumb">{inner}</div><h3>{E(title)}</h3></a>'

def product_cards(cat):
    return "".join(card(name, img, f"{slug}.html" if slug else contact_url(name, cat["name"]))
                   for name, img, slug, _desc in cat["items"])

def cat_tabs(active):
    return '<nav class="cat-tabs" aria-label="Categorías"><div class="container">' + "".join(
        f'<a href="{c["slug"]}.html"{ACT if c["slug"] == active else ""}>{E(c["name"])}</a>' for c in CATS
    ) + "</div></nav>\n"

def band(title, text, btn="Solicitar catálogo de productos", href="contacto.html"):
    return f'''<section class="band"><div class="container">
  <h2>{E(title)}</h2><p>{E(text)}</p>
  <a class="btn btn-outline-light" href="{href}">{E(btn)}</a>
</div></section>
'''

def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)

TRUST = f'''<section class="trust"><div class="container">
  <div class="trust-item"><div class="ic">{ICON["award"]}</div><div><strong>20</strong><span>años de experiencia en la industria del plástico</span></div></div>
  <div class="trust-item"><div class="ic">{ICON["clock"]}</div><div><strong>12-24 h</strong><span>respuesta y envío de recambios</span></div></div>
  <div class="trust-item"><div class="ic">{ICON["gear"]}</div><div><strong>128</strong><span>zonas de control en una sola unidad</span></div></div>
  <div class="trust-item"><div class="ic">{ICON["globe"]}</div><div><strong>+50</strong><span>clientes con envíos a todo el mundo</span></div></div>
</div></section>
'''

# ---------------------------------------------------------------------------
# Fichas de producto
# ---------------------------------------------------------------------------
def render_section(sec, first):
    items = sec["items"]
    lis = [i for i in items if i["t"] == "li"]
    ps = [i for i in items if i["t"] == "p"]
    kvs = [i for i in items if i["t"] == "kv"]
    many_long = sum(len(i["v"]) > 110 for i in kvs) * 2 > len(kvs)
    short_kv = [] if many_long else kvs
    long_kv = kvs if many_long else []
    h = sec["h"] or ("Descripción" if first else "Más información")
    body = "".join(f"<p>{E(p['v'])}</p>" for p in ps)
    if lis:
        body += '<ul class="checklist">' + "".join(f"<li>{E(i['v'])}</li>" for i in lis) + "</ul>"
    if short_kv:
        body += '<table class="spec"><tbody>' + "".join(f"<tr><th>{E(i['k'])}</th><td>{E(i['v'])}</td></tr>" for i in short_kv) + "</tbody></table>"
    if long_kv:
        body += '<div class="feat-grid">' + "".join(f'<div class="feat"><h3>{E(i["k"])}</h3><p>{E(i["v"])}</p></div>' for i in long_kv) + "</div>"
    wide = bool(long_kv) or len(" ".join(p["v"] for p in ps)) > 700 or len(short_kv) > 7
    return f'<section class="block{" block--wide" if wide else ""}"><h2>{E(h)}</h2>{body}</section>', wide

for slug, f in FICHAS.items():
    cat = CAT_BY_PRODUCT.get(slug)
    if not cat:
        continue
    imgs = f["images"] or [CARD_IMG[slug]]
    imgs = list(dict.fromkeys(imgs))
    main = imgs[0]
    thumbs = ""
    if len(imgs) > 1:
        thumbs = '<div class="thumbs">' + "".join(
            f'<button type="button" data-src="{img_src(i)}"{ACT if n == 0 else ""} aria-label="Ver imagen {n+1}"><img src="{img_src(i)}" alt="" loading="lazy"></button>' for n, i in enumerate(imgs[:10])) + "</div>"
    sections = [dict(s) for s in f["sections"]]
    # Párrafo de entrada: primer párrafo de la primera sección sin título
    lead = ""
    if sections and sections[0]["h"] is None and sections[0]["items"] and sections[0]["items"][0]["t"] == "p":
        lead = sections[0]["items"][0]["v"]
        sections[0] = {"h": None, "items": sections[0]["items"][1:]}
    if not lead:
        lead = cat["short"]
    sections = [s for s in sections if s["items"]]
    # Chips: primeras ventajas o claves técnicas
    chips_src = [i["v"] for s in sections for i in s["items"] if i["t"] == "li"][:4]
    chips = ('<ul class="chips">' + "".join(f"<li>{E(c.rstrip('.'))}</li>" for c in chips_src) + "</ul>") if chips_src else ""
    blocks = []
    for n, s in enumerate(sections):
        b, _ = render_section(s, n == 0)
        blocks.append(b)
    custom = ""
    if cat["slug"] == "resistencias-electricas":
        custom = '<div class="custom-note"><div><strong>¿Necesita una medida especial?</strong> Envíenos dimensiones, voltaje, potencia, perforaciones y tipo de conexión y le preparamos un presupuesto a medida.</div></div>'
    related = [it for it in cat["items"] if it[2] != slug][:4]
    rel_html = "".join(card(n, i, f"{s}.html" if s else contact_url(n, cat["name"])) for n, i, s, d in related)
    wa_text = quote(f"Hola, me interesa {f['title']} (System Plast). ¿Me pueden dar más información?")
    sub = f'<p class="pdp-sub">{E(f["subtitle"])}</p>' if f["subtitle"] else ""
    mobile_cta = f'<div class="mobile-cta"><a class="btn btn-primary" href="{contact_url(f["title"], cat["name"])}">Pedir presupuesto</a><a class="btn btn-wa" href="https://wa.me/{TEL[1:]}?text={wa_text}" target="_blank" rel="noopener">{ICON["wa"]} WhatsApp</a></div>\n'
    page = head(f"{f['title']} | {cat['name']} | System Plast", (lead or cat["short"])[:155]) + header("productos.html") + \
        crumbs(("Productos", "productos.html"), (cat["name"], f"{cat['slug']}.html"), (f["title"], None)) + f'''<main>
<section class="pdp"><div class="container">
  <div class="pdp-top">
    <div class="gallery"><div class="gallery-main"><img src="{img_src(main)}" alt="{E(f['title'])}"></div>{thumbs}</div>
    <div class="pdp-info">
      <span class="kicker">{E(cat['name'])}</span>
      <h1>{E(f['title'])}</h1>{sub}
      <p class="lead">{E(lead)}</p>
      {chips}
      <div class="pdp-actions">
        <a class="btn btn-primary btn-lg" href="{contact_url(f['title'], cat['name'])}">Solicitar presupuesto</a>
        <a class="btn btn-wa btn-lg" href="https://wa.me/{TEL[1:]}?text={wa_text}" target="_blank" rel="noopener">{ICON['wa']} WhatsApp</a>
      </div>
      {custom}
      <ul class="pdp-assure">
        <li>{ICON['clock']} Recambios en 12-24 h</li>
        <li>{ICON['user']} Asesoría técnica</li>
        <li>{ICON['globe']} Envíos a todo el mundo</li>
      </ul>
    </div>
  </div>
  <div class="pdp-body">{"".join(blocks)}</div>
</div></section>
<section class="related"><div class="container">
  <div class="section-head"><span class="kicker">{E(cat['name'])}</span><h2>Otros productos de la categoría</h2></div>
  <div class="product-grid grid-4">{rel_html}</div>
</div></section>
''' + CTA + "</main>\n" + mobile_cta + footer()
    write(f"{slug}.html", page)

# ---------------------------------------------------------------------------
# Páginas de categoría
# ---------------------------------------------------------------------------
for c in CATS:
    t, s = c["hero"]
    bt, bx = c["band"]
    page = head(f"{c['name']} | System Plast", c["short"]) + header("productos.html") + hero(t, s) + \
        cat_tabs(c["slug"]) + f'''<main>
<section class="section"><div class="container">
  <div class="product-grid">{product_cards(c)}</div>
</div></section>
''' + band(bt, bx) + CTA + "</main>\n" + footer()
    write(f"{c['slug']}.html", page)

# ---------------------------------------------------------------------------
# Productos
# ---------------------------------------------------------------------------
cats_html = "".join(card(c["name"], c["img"], f"{c['slug']}.html") for c in CATS)
write("productos.html", head("Productos | System Plast", "Catálogo System Plast: controladores HRS de canal caliente, resistencias eléctricas, EOAT para robótica y estanterías para moldes.") +
      header("productos.html") + hero("Catálogo de productos", "Productos diseñados para mejorar la productividad y garantizar procesos de inyección más eficientes y seguros") +
      cat_tabs(None) + f'''<main>
<section class="section section--grey"><div class="container">
  <div class="section-head"><span class="kicker">Categorías de productos</span><h2>Conoce nuestra variedad de productos</h2><p>Equipos y componentes para que sus procesos de inyección sean más eficientes, seguros y rentables.</p></div>
  <div class="product-grid cat-grid cat-grid--4">{cats_html}</div>
</div></section>
''' + band("Soluciones a medida", "Nuestras soluciones a medida garantizan una integración perfecta con las líneas de producción de nuestros clientes, lo que les permite obtener una ventaja competitiva en el mercado.", "Contáctanos") + f'''<section class="section"><div class="container">
  <p class="statement">Estos productos ayudan a nuestros clientes a <strong>mejorar la eficiencia de la producción, reducir el consumo de energía y mejorar la calidad del producto</strong>.</p>
  <p>Al ofrecer productos de mayor calidad y servicios más especializados, aspiramos a contribuir significativamente al desarrollo de la industria global del moldeo por inyección y a liderar la nueva generación de tecnología de control de temperatura de canal caliente.</p>
</div></section>
''' + CTA + "</main>\n" + footer())

# ---------------------------------------------------------------------------
# Inicio
# ---------------------------------------------------------------------------
features = [("01", "Sistemas de control de temperatura para hot runner", "Diseñados para garantizar precisión y estabilidad en procesos de inyección plástica, optimizando la calidad del producto final y reduciendo tiempos de producción."),
            ("02", "Accesorios y recambios para moldes de inyección", "Componentes y piezas de alto rendimiento que extienden la vida útil de sus moldes, asegurando continuidad operativa sin interrupciones."),
            ("03", "Soluciones personalizadas para procesos industriales", "Proyectos a medida según las necesidades de su línea de producción, integrando innovación y eficiencia en cada etapa del proceso.")]
why = [("star", "Calidad garantizada", "Equipos y productos diseñados bajo estándares internacionales."),
       ("gear", "Tecnología de vanguardia", "Innovación constante en cada solución."),
       ("user", "Atención personalizada", "Soporte antes, durante y después de su compra."),
       ("globe", "Cobertura amplia", "Envíos y atención en cualquier parte del mundo."),
       ("clock", "Respuesta y recambios", "De 12 a 24 horas.")]
news_html = "".join(f'<a class="news-card" href="{u}" target="_blank" rel="noopener"><img src="assets/img/{i}" alt="" loading="lazy"><div class="body"><span class="kicker">{E(src)}</span><h3>{E(t)}</h3><span class="card-link">Leer noticia ↗</span></div></a>' for i, t, src, u in NEWS)
home_cats = "".join(card(c["name"], c["img"], f"{c['slug']}.html") for c in CATS)
featured = [("serie-mtc-b", "Serie MTC-B", "Más vendido"), ("resistencias-de-aluminio", "Resistencias de aluminio", None),
            ("cambiadores-rapidos-de-herramientas-quick-changers", "Cambiadores rápidos", None), ("svge-8", "Controlador SVGE-8", "Nuevo")]
feat_html = "".join(card(n, CARD_IMG[s], f"{s}.html") for s, n, b in featured)
write("index.html", head("System Plast | Sistemas de control y plásticos industriales", "Soluciones de alto rendimiento para la industria del plástico y la inyección: controladores de canal caliente, resistencias, EOAT y estanterías para moldes.") +
      header("index.html") + f'''<section class="hero hero--home" style="background-image:url(assets/img/home-2.jpg)"><div class="container">
  <span class="hero-eyebrow">Innovación en sistemas de control y plásticos industriales</span>
  <h1>Soluciones de alto rendimiento para la industria del plástico y la inyección</h1>
  <p>Tecnología y soluciones para tu negocio</p>
  <a class="btn btn-primary btn-lg" href="productos.html">Ver productos</a>
</div></section>
''' + TRUST + f'''<main>
<section class="section section--grey"><div class="container">
  <div class="section-head"><span class="kicker">Nuestros productos</span><h2>Tecnología y soluciones para tu negocio</h2><p>En SYSTEM PLAST ofrecemos productos diseñados para mejorar la productividad y garantizar procesos de inyección de plástico más eficientes y seguros.</p></div>
  <div class="product-grid grid-4">{home_cats}</div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Destacados</span><h2>Productos más solicitados</h2></div>
  <div class="product-grid grid-4">{feat_html}</div>
</div></section>
<section class="section section--grey"><div class="container">
  <div class="section-head"><span class="kicker">Tecnología avanzada para tu proceso de inyección</span><h2>Tu aliado estratégico en innovación</h2></div>
  <div class="feature-list">{"".join(f'<div class="feature"><span class="num">{n}.</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for n, t, d in features)}</div>
</div></section>
''' + band("Asesoría técnica especializada", "En SYSTEM PLAST entendemos que elegir un proveedor es elegir un socio de confianza. Le ayudamos a elegir el equipo adecuado y le acompañamos antes, durante y después de la compra.", "Solicitar asesoramiento") + f'''<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Por qué elegirnos</span><h2>Lo que nos diferencia</h2><p>En SYSTEM PLAST entendemos que elegir un proveedor es elegir un socio de confianza. Por eso ofrecemos:</p></div>
  <div class="why">{"".join(f'<div class="why-item"><div class="icon">{ICON[ic]}</div><h4>{E(t)}</h4><p>{E(d)}</p></div>' for ic, t, d in why)}</div>
</div></section>
<section class="section section--grey"><div class="container">
  <div class="section-head"><span class="kicker">Industrias</span><h2>Que confían en SYSTEM PLAST</h2><p>Nuestros productos están presentes en grandes sectores como automoción, electrodomésticos, dispositivos médicos y envases.</p></div>
  <div class="logos">{"".join(f'<img src="assets/img/industria-{i}.png" alt="Cliente de System Plast" loading="lazy">' for i in range(1, 7))}</div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Actualidad</span><h2>Noticias del sector</h2></div>
  <div class="news-grid">{news_html}</div>
</div></section>
<section class="section section--grey"><div class="container">
  <p class="statement">Estos productos ayudan a nuestros clientes a <strong>mejorar la eficiencia de la producción, reducir el consumo de energía y mejorar la calidad del producto</strong>.</p>
  <p>Al ofrecer productos de mayor calidad y servicios más especializados, aspiramos a contribuir significativamente al desarrollo de la industria global del moldeo por inyección y a liderar la nueva generación de tecnología de control de temperatura de canal caliente.</p>
</div></section>
''' + CTA + "</main>\n" + footer())

# ---------------------------------------------------------------------------
# Quiénes somos
# ---------------------------------------------------------------------------
write("quienes-somos.html", head("Quiénes somos | System Plast", "20 años desarrollando y distribuyendo soluciones tecnológicas para la industria del plástico.") +
      header("quienes-somos.html") + hero("Quiénes somos", "Desarrollo y distribución de soluciones tecnológicas") + crumbs(("Quiénes somos", None)) + f'''<main>
<section class="section"><div class="container split">
  <div><span class="kicker">01. Nuestra empresa</span><h2>En SYSTEM PLAST nos especializamos</h2>
  <p>En el desarrollo y distribución de soluciones tecnológicas para la industria del plástico. Nuestro compromiso es ofrecer equipos y sistemas que optimicen procesos, aumenten la eficiencia y garanticen calidad en cada producción.</p>
  <p>Con 20 años de experiencia, un equipo altamente capacitado y la confianza de nuestros clientes, nos hemos consolidado como un aliado estratégico para empresas que buscan innovación y resultados reales.</p>
  <div class="stats"><div class="stat"><strong>20</strong><span>Años de experiencia</span></div><div class="stat"><strong>+50</strong><span>Clientes</span></div></div></div>
  <div><img src="assets/img/home-2.jpg" alt="Célula de inyección con robot" loading="lazy"></div>
</div></section>
<section class="section section--grey"><div class="container">
  <div class="section-head"><span class="kicker">Calidad</span><h2>¿Por qué elegirnos?</h2><p>Nos adherimos estrictamente a los sistemas internacionales de gestión de calidad durante todo el proceso de producción, desde la adquisición de materias primas hasta el ensamblaje del producto.</p></div>
  <div class="pdp-body" style="margin-top:0">
    <section class="block"><h2>Liderazgo tecnológico</h2><p>Contamos con una amplia gama de soluciones en control de temperatura, desde equipos monozona y multizona hasta sistemas inteligentes diseñados para lograr la máxima precisión. Nuestros controladores de canal caliente integran tecnología avanzada basada en algoritmos PID, lo que permite un control estable, exacto y con tiempos de respuesta muy rápidos.</p><p>Gracias a estas características, se optimiza el proceso de moldeo por inyección, garantizando mayor eficiencia, consistencia y confiabilidad para los fabricantes que buscan resultados de alto nivel.</p></section>
    <section class="block"><h2>Servicios personalizados</h2><p>Entendemos que cada cliente tiene requerimientos particulares, por eso desarrollamos y fabricamos cajas de control de temperatura totalmente personalizadas, diseñadas para ajustarse de manera precisa a los procesos de moldeo por inyección y a las demandas específicas de producción.</p><p>Nuestras soluciones hechas a la medida se integran de forma eficiente en las líneas de producción, brindando a las empresas un mejor rendimiento operativo y una ventaja competitiva dentro de su industria.</p></section>
  </div>
</div></section>
''' + band("Nuestra visión de futuro", "De cara al futuro, la empresa se compromete a seguir centrándose en el sector de los controladores de temperatura de canal caliente. Incrementaremos la inversión en investigación y desarrollo, fomentando una cultura de innovación continua para liderar la nueva generación de tecnología de control de temperatura de canal caliente.", "Ver productos", "productos.html") + CTA + "</main>\n" + footer())

# ---------------------------------------------------------------------------
# Noticias
# ---------------------------------------------------------------------------
write("noticias.html", head("Noticias | System Plast", "Noticias y tendencias de la industria del plástico.") + header("noticias.html") +
      hero("Noticias", "Actualidad y tendencias de la industria del plástico", compact=True) + crumbs(("Noticias", None)) + f'''<main>
<section class="section section--grey"><div class="container"><div class="news-grid">{news_html}</div></div></section>
''' + CTA + "</main>\n" + footer())

# ---------------------------------------------------------------------------
# Contacto
# ---------------------------------------------------------------------------
opts = "".join(f"<option>{E(c['name'])}</option>" for c in CATS) + "<option>Otro / proyecto a medida</option>"
write("contacto.html", head("Contacto | System Plast", f"Contacte con System Plast: {DIR1}, {DIR2}. Tel. {TEL_TXT}.") + header("contacto.html") +
      hero("Contacto", "Un miembro de nuestro equipo le responderá", compact=True) + crumbs(("Contacto", None)) + f'''<main>
<section class="section section--grey"><div class="container contact-grid">
  <div class="contact-info">
    <h3>Hablemos de su proyecto</h3>
    <p>Si tiene alguna pregunta sobre controladores de temperatura de canal caliente, controladores de válvula secuencial, resistencias o EOAT, complete el formulario y un miembro de nuestro equipo le responderá.</p>
    <dl><dt>Dirección</dt><dd>{DIR1}<br>{DIR2}</dd>
    <dt>Teléfono</dt><dd><a href="tel:{TEL}">{TEL_TXT}</a></dd>
    <dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
    <dt>WhatsApp</dt><dd><a href="https://wa.me/{TEL[1:]}" target="_blank" rel="noopener">Escríbanos por WhatsApp</a></dd>
    <dt>Respuesta</dt><dd>De 12 a 24 horas</dd></dl>
  </div>
  <form class="form" id="contact-form">
    <div class="row"><div class="field"><label for="nombre">Nombre *</label><input id="nombre" name="nombre" autocomplete="name" required></div>
    <div class="field"><label for="empresa">Empresa</label><input id="empresa" name="empresa" autocomplete="organization"></div></div>
    <div class="row"><div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="telefono">Teléfono</label><input id="telefono" name="telefono" type="tel" autocomplete="tel"></div></div>
    <div class="field"><label for="producto">Categoría de interés</label><select id="producto" name="producto">{opts}</select></div>
    <div class="field"><label for="mensaje">Mensaje *</label><textarea id="mensaje" name="mensaje" required></textarea></div>
    <div class="field"><label class="check"><input type="checkbox" required> He leído y acepto la política de privacidad.</label></div>
    <button class="btn btn-primary btn-lg" type="submit">Enviar consulta</button>
    <div class="form-msg">Se ha abierto su programa de correo con la consulta preparada.</div>
  </form>
</div></section>
<section style="line-height:0"><iframe title="Ubicación System Plast" src="https://maps.google.com/maps?q=Pol.%20Ind.%20Riodil%201%2C%2003110%20Mutxamel%2C%20Alicante&z=15&output=embed" width="100%" height="380" style="border:0" loading="lazy"></iframe></section>
</main>
''' + footer())

print("Páginas generadas:", len([f for f in os.listdir(OUT) if f.endswith(".html")]))
