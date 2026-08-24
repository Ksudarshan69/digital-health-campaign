// Lightbox for album detail pages (spec section 22)
document.addEventListener('DOMContentLoaded', () => {
    const backdrop = document.getElementById('lightbox-backdrop');
    const imageEl = document.getElementById('lightbox-image');
    const captionEl = document.getElementById('lightbox-caption');
    const closeBtn = document.getElementById('lightbox-close');
    if (!backdrop) return;

    document.querySelectorAll('.lightbox-trigger').forEach((trigger) => {
        trigger.addEventListener('click', () => {
            imageEl.src = trigger.dataset.full;
            imageEl.alt = trigger.dataset.caption || '';
            captionEl.textContent = trigger.dataset.caption || '';
            backdrop.classList.add('is-open');
        });
    });

    const close = () => backdrop.classList.remove('is-open');
    closeBtn.addEventListener('click', close);
    backdrop.addEventListener('click', (e) => { if (e.target === backdrop) close(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
});
