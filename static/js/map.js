// Districts overview interactivity (spec section 14).
// Pins are positioned server-side via map_x/map_y; this just wires up
// hover tooltips (already CSS-driven) and click-through, which happens
// natively via the <a> tag. Kept deliberately simple and framework-free.
document.addEventListener('DOMContentLoaded', () => {
    const pins = document.querySelectorAll('.districts-map__pin');
    pins.forEach((pin) => {
        pin.addEventListener('focus', () => pin.classList.add('is-active'));
        pin.addEventListener('blur', () => pin.classList.remove('is-active'));
    });
});
