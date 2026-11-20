// SYSTEM PLAST: animaciones de entrada de las páginas (revela los bloques marcados con data-enter)
// y trazo de la línea sobre los titulares. La portada (.hero) la lleva motion.js: aquí se ignora.

const html = document.documentElement;
const reduced = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
const shot = () => /HeadlessChrome/.test(navigator.userAgent) && html.dataset.motion !== 'live';
const EASE = 'cubic-bezier(.22, 1, .36, 1)';
const LINE_HEADINGS = '.section-head h2, .grid-h, .pdp-body-h, .band-row h2, .split-6 h2, main > .section h2';

// Cada palabra del h1 en su máscara (.m-w / .m-w__in); devuelve las palabras por línea y cómo deshacerlo.
function maskWords(h1) {
  const own = document.createDocumentFragment();
  own.append(...h1.childNodes);
  const copy = own.cloneNode(true);
  const words = [];
  const walk = node => [...node.childNodes].forEach(n => {
    if (n.nodeType === 1) return walk(n);
    if (n.nodeType !== 3) return;
    const frag = document.createDocumentFragment();
    n.textContent.split(/(\s+)/).forEach(part => {
      if (!part) return;
      if (/^\s+$/.test(part)) { frag.append(part); return; }
      const w = document.createElement('span'), i = document.createElement('span');
      w.className = 'm-w'; i.className = 'm-w__in'; i.textContent = part;
      w.append(i); frag.append(w); words.push(w);
    });
    n.replaceWith(frag);
  });
  walk(copy);
  const hadLabel = h1.hasAttribute('aria-label');
  if (!hadLabel) h1.setAttribute('aria-label', own.textContent.replace(/\s+/g, ' ').trim());
  h1.append(copy);
  h1.querySelectorAll('.m-w').forEach(w => w.setAttribute('aria-hidden', 'true'));
  // palabras agrupadas en las líneas en que el navegador las colocó
  const lines = [];
  let top = null;
  words.forEach(w => {
    const t = w.getBoundingClientRect().top;
    if (top === null || Math.abs(t - top) > 3) { lines.push([]); top = t; }
    lines[lines.length - 1].push(w.firstChild);
  });
  return { lines, restore() { h1.replaceChildren(own); if (!hadLabel) h1.removeAttribute('aria-label'); } };
}

// Entrada de una cabecera (.pg-head) o ficha (.pdp): titular, resto del bloque y primeras tarjetas, en 1,1 s.
export function enterPage(root) {
  // .is-in: la cuadrícula y la regla se dibujan (decor.css) en paralelo con las palabras
  const show = () => { root.classList.add('is-in'); html.classList.add('page-entered'); };
  if (!html.classList.contains('m-enter') || html.dataset.motion === 'off' || shot() || reduced() || root.getBoundingClientRect().bottom < 0) return show();
  // la marca de seguridad ya pasó: el CSS funde el texto; se da por terminada tras el fundido
  const late = () => setTimeout(() => { root.classList.add('is-in'); html.classList.add('page-entered'); }, 450);
  if (html.classList.contains('m-enter-done')) return void late();
  const h1 = root.querySelector('h1');
  if (!h1) return show();

  const anims = [];
  let masks = null, over = false;
  const finish = () => {
    if (over) return;
    over = true;
    anims.forEach(a => { try { a.cancel(); } catch { /* ya no está */ } });
    masks?.restore();
    root.classList.remove('is-entering');
    show();
  };

  // las fuentes primero (una línea en la tipografía de reserva se parte distinto), 100 ms como mucho
  const t0 = performance.now();
  Promise.race([document.fonts?.ready ?? Promise.resolve(), new Promise(r => setTimeout(r, 100))])
    // un fotograma más: el pagereveal de la cabecera ya habrá nombrado la foto de la transición de vista
    .then(() => new Promise(r => { requestAnimationFrame(r); setTimeout(r, 60); })).then(() => {
    if (over) return;
    if (html.classList.contains('m-enter-done') && !root.classList.contains('is-entering')) { over = true; late(); return; }
    masks = maskWords(h1);
    // .is-entering suelta la espera del CSS (las animaciones retienen el estado inicial); page-entering,
    // la de las tarjetas, que están en otra sección. Las que no caben en pantalla quedan visibles ya.
    root.classList.add('is-entering', 'is-in');
    html.classList.add('page-entering');
    // presupuesto: la última animación acaba a 1100 ms de empezar la entrada (≥ 1000 ms tras la espera de fuentes)
    const B = Math.max(900, 1100 - (performance.now() - t0));
    const lines = masks ? masks.lines : [[h1]];
    const lineStep = Math.max(0, Math.min(80, 240 / Math.max(1, lines.length - 1), (B - 780) / Math.max(1, lines.length - 1)));
    lines.forEach((ws, k) => ws.forEach(w => anims.push(w.animate(masks
      ? [{ transform: 'translateY(calc(100% + .2em))' }, { transform: 'none' }]
      : [{ transform: 'translateY(.35em)', opacity: 0 }, { transform: 'none', opacity: 1 }],
      { duration: 700, delay: 80 + k * lineStep, easing: EASE, fill: 'both' }))));

    // la etiqueta sobre el titular entra con su primera línea
    const label = root.querySelector('.pdp-info > .t-label');
    if (label) {
      const t = { duration: 500, delay: 80, easing: EASE, fill: 'both' };
      anims.push(label.animate([{ opacity: 0 }, { opacity: 1 }], t),
        label.animate([{ transform: 'translateY(12px)' }, { transform: 'none' }], { ...t, composite: 'add' }));
    }
    // migas, entradilla, hijos de la ficha y miniaturas: uno tras otro, 220 ms después del titular
    const steps = [...new Set(root.querySelectorAll('.crumbs, .t-lead, .pdp-sub, .pdp-info > :not(h1, .t-label), .thumbs'))];
    const after = Math.min(80 + (lines.length - 1) * lineStep + 220, B - 500);
    const gap = Math.max(0, Math.min(60, (B - 500 - after) / Math.max(1, steps.length - 1)));
    steps.forEach((el, k) => {
      const t = { duration: 500, delay: after + k * gap, easing: EASE, fill: 'both' };
      anims.push(el.animate([{ opacity: 0 }, { opacity: 1 }], t),
        el.animate([{ transform: 'translateY(12px)' }, { transform: 'none' }], { ...t, composite: 'add' }));
    });

    // el vídeo de la cabecera se asienta (scale compone con el desplazamiento por scroll de site.css)
    const bg = root.querySelector('.pg-head__bg');
    if (bg) anims.push(bg.animate([{ scale: 1.04 }, { scale: 1 }], { duration: B, easing: EASE, fill: 'both' }));

    // la foto de la galería se asienta, salvo que ya la lleve la transición de vista entre documentos
    const vtName = el => el && (el.style.viewTransitionName || html.dataset.vtArrive === '1');
    const photo = root.querySelector('.gallery-main img[data-gallery-main]');
    if (photo && !vtName(photo)) anims.push(photo.animate([{ scale: 1.04, clipPath: 'inset(2%)' }, { scale: 1, clipPath: 'inset(0)' }],
      { duration: B, easing: EASE, fill: 'both' }));

    // primeras tarjetas del catálogo que caben en el primer viewport, en cascada desde los 300 ms
    const cards = [...document.querySelectorAll('.prod-grid > .card:nth-child(-n+8)')].filter(c => c.getBoundingClientRect().top < innerHeight && !c.querySelector('img')?.style.viewTransitionName);
    const cardGap = Math.max(0, Math.min(60, (B - 500 - 300) / Math.max(1, cards.length - 1)));
    cards.forEach((c, i) => {
        const t = { duration: 500, delay: 300 + i * cardGap, easing: EASE, fill: 'both' };
        anims.push(c.animate([{ opacity: 0 }, { opacity: 1 }], t),
          c.animate([{ transform: 'translateY(12px)' }, { transform: 'none' }], { ...t, composite: 'add' }));
      });

    // todo termina antes de 1,1 s; sin animaciones (pestaña oculta) el límite lo pone el temporizador
    Promise.all(anims.map(a => a.finished)).then(finish, finish);
    setTimeout(finish, B + 50);   // tope real de la entrada
  }).catch(finish);
  setTimeout(finish, 2400);   // pase lo que pase, la cabecera queda en pie a los 2,4 s
}

// Trazo de la línea sobre los titulares: la primera vez que se ven (decor.css las esconde bajo .js-decor).
function drawHeadingLines() {
  const all = () => document.querySelectorAll(LINE_HEADINGS).forEach(h => h.classList.add('decor-line--in'));
  html.classList.add('js-decor');
  if (reduced() || !('IntersectionObserver' in window)) return all();
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('decor-line--in');
    io.unobserve(e.target);
  }), { threshold: 0.6 });
  document.querySelectorAll(LINE_HEADINGS).forEach(h => io.observe(h));
}

function start() {
  drawHeadingLines();
  const roots = [...document.querySelectorAll('.pg-head[data-enter], .pdp[data-enter]')].filter(r => !r.closest('.hero'));
  // la entrada completa es para el primero; si hubiera más (cabecera y ficha), basta con darlos por llegados
  roots.forEach((r, i) => {
    if (i === 0) {
      try { enterPage(r); } catch (e) { console.warn('entrance.js: enterPage', e); r.classList.add('is-in'); html.classList.add('page-entered'); }
    } else r.classList.add('is-in');
  });
}
start();

// Vuelta desde el historial (bfcache): todo en su sitio, sin animar
addEventListener('pageshow', e => {
  if (!e.persisted) return;
  html.classList.add('page-entered');
  document.querySelectorAll('.pg-head[data-enter], .pdp[data-enter]').forEach(r => r.classList.remove('is-entering') || r.classList.add('is-in'));
  document.querySelectorAll(LINE_HEADINGS).forEach(h => h.classList.add('decor-line--in'));
});
