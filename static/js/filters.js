// Debounce helper for search/filter inputs that should query as-you-type
// rather than firing a request per keystroke (spec section 30).
function debounce(fn, wait = 350) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), wait);
    };
}

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('input[name="q"]');
    if (!searchInput || !searchInput.form) return;

    // Auto-submit the containing filter form after the user pauses typing,
    // rather than requiring an explicit click on desktop.
    searchInput.addEventListener('input', debounce(() => {
        searchInput.form.requestSubmit ? searchInput.form.requestSubmit() : searchInput.form.submit();
    }, 500));
});
