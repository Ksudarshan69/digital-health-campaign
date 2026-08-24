// Shared form helpers: lightweight required-field check before submit,
// so users get instant feedback instead of a full round-trip for
// obviously-empty fields. Server-side validation (Django forms) remains
// the source of truth.
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('form').forEach((form) => {
        form.addEventListener('submit', (e) => {
            const required = form.querySelectorAll('[required]');
            let firstInvalid = null;
            required.forEach((field) => {
                if (!field.value.trim() && !firstInvalid) firstInvalid = field;
            });
            if (firstInvalid) {
                e.preventDefault();
                firstInvalid.focus();
            }
        });
    });
});
