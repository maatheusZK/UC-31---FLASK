
/* ════════════════════════════════════════
   NAVBAR — efeito de scroll
════════════════════════════════════════ */
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.navbar');
    if (!nav) return;
    nav.style.background = window.scrollY > 60
        ? 'rgba(0,0,0,0.90)'
        : 'rgba(0,0,0,0.4)';
});

/* ════════════════════════════════════════
   MENU — troca de categorias
════════════════════════════════════════ */
function switchTab(e, categoryId) {
    document.querySelectorAll('.menu-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.menu-category').forEach(c => c.classList.remove('active'));
    e.target.classList.add('active');
    const category = document.getElementById(categoryId);
    if (category) category.classList.add('active');
}

/* ════════════════════════════════════════
   CONTATO — feedback no envio
════════════════════════════════════════ */
function handleSubmit(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.textContent = '✓ Mensagem enviada!';
    btn.style.background = '#4caf83';
    setTimeout(() => {
        btn.textContent = 'Enviar Mensagem';
        btn.style.background = '';
        e.target.reset();
    }, 3000);
}