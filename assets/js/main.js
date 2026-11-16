// SYSTEM PLAST — interacciones
(function () {
  const header = document.querySelector('.header');
  const toTop = document.querySelector('.to-top');
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle('scrolled', y > 40);
    toTop && toTop.classList.toggle('show', y > 500);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  toTop && toTop.addEventListener('click', () => window.scrollTo({ top: 0 }));

  // Menú móvil
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open);
    });
  }

  // Galería de la ficha de producto
  const main = document.querySelector('.gallery-main img');
  document.querySelectorAll('.thumbs button').forEach((b) => {
    b.addEventListener('click', () => {
      main.src = b.dataset.src;
      document.querySelectorAll('.thumbs button').forEach((x) => x.classList.toggle('active', x === b));
    });
  });

  // Formulario de contacto (abre el cliente de correo hasta conectar un backend)
  const form = document.querySelector('#contact-form');
  if (form) {
    // Rellena producto y categoría si se llega desde una ficha (?producto=...&cat=...)
    const q = new URLSearchParams(location.search);
    const prod = q.get('producto');
    const cat = q.get('cat');
    if (cat) {
      const sel = form.querySelector('#producto');
      [...sel.options].forEach((o) => { if (o.text === cat) sel.value = o.value; });
    }
    if (prod) {
      form.querySelector('#mensaje').value = `Hola, me interesa recibir información y presupuesto de: ${prod}.\n\n`;
    }
    form.addEventListener('submit', (ev) => {
      ev.preventDefault();
      const d = new FormData(form);
      const body = `Nombre: ${d.get('nombre')}\nEmpresa: ${d.get('empresa') || '-'}\nTeléfono: ${d.get('telefono') || '-'}\nEmail: ${d.get('email')}\nProducto: ${d.get('producto')}\n\n${d.get('mensaje')}`;
      window.location.href = `mailto:info@systemplas.com?subject=${encodeURIComponent('Consulta web - ' + d.get('producto'))}&body=${encodeURIComponent(body)}`;
      const msg = form.querySelector('.form-msg');
      if (msg) msg.style.display = 'block';
    });
  }
})();
