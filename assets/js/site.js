(() => {
  const btn = document.querySelector('[data-menu]');
  const nav = document.querySelector('[data-nav]');
  if (btn && nav) {
    btn.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
      btn.textContent = open ? '×' : '☰';
      document.body.classList.toggle('nav-open', open);
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded','false');
      btn.textContent = '☰';
      document.body.classList.remove('nav-open');
    }));
  }

  const io = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, {threshold: .12}) : null;
  document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('is-visible'));

  const form = document.querySelector('[data-enquiry-form]');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const data = new FormData(form);
      const name = data.get('name') || '';
      const phone = data.get('phone') || '';
      const email = data.get('email') || '';
      const matter = data.get('matter') || 'General legal enquiry';
      const message = data.get('message') || '';
      const subject = encodeURIComponent(`Website enquiry: ${matter}`);
      const body = encodeURIComponent(`Name: ${name}\nPhone: ${phone}\nEmail: ${email}\nMatter: ${matter}\n\nMessage:\n${message}`);
      window.location.href = `mailto:murithikiraguadvocate@gmail.com?subject=${subject}&body=${body}`;
    });
  }

  const y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
