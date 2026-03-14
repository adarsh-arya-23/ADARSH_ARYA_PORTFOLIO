
f = r"d:\Documents\Z_PORTFOLIO\main.js"
with open(f, "r", encoding="utf-8") as fh:
    js = fh.read()

NEW_JS = """
/* =============================================================
   19. CARD TILT — 3-D perspective tilt on project cards
   ============================================================= */
function initCardTilt() {
    const cards = document.querySelectorAll('.proj-card');
    const MAX_TILT = 5; // degrees

    cards.forEach(card => {
        let rafId;

        card.addEventListener('mousemove', e => {
            cancelAnimationFrame(rafId);
            rafId = requestAnimationFrame(() => {
                const rect = card.getBoundingClientRect();
                const cx = rect.left + rect.width / 2;
                const cy = rect.top  + rect.height / 2;
                const dx = (e.clientX - cx) / (rect.width  / 2);
                const dy = (e.clientY - cy) / (rect.height / 2);
                const rx =  dy * MAX_TILT * -1;
                const ry =  dx * MAX_TILT;
                card.style.transition = 'none';
                card.style.transform  = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-6px)`;
            });
        });

        card.addEventListener('mouseleave', () => {
            cancelAnimationFrame(rafId);
            card.style.transition = 'transform 0.55s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.4s ease, border-color 0.3s ease';
            card.style.transform  = '';
        });
    });
}

/* =============================================================
   20. PROJECT FILTER — Filter & animate by category
   ============================================================= */
function initProjectFilter() {
    const filters = document.querySelectorAll('.proj-filter');
    const cards   = document.querySelectorAll('.proj-card');
    if (!filters.length) return;

    filters.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active state
            filters.forEach(f => f.classList.remove('active'));
            btn.classList.add('active');

            const selected = btn.dataset.pf;

            cards.forEach((card, i) => {
                const cat = card.dataset.pc || 'all';
                const show = selected === 'all' || cat === selected;

                card.style.transition = `opacity 0.35s ease ${i * 0.05}s, transform 0.4s cubic-bezier(0.23,1,0.32,1) ${i * 0.05}s`;

                if (show) {
                    card.style.opacity   = '1';
                    card.style.transform = '';
                    card.style.pointerEvents = 'auto';
                } else {
                    card.style.opacity   = '0.15';
                    card.style.transform = 'scale(0.97)';
                    card.style.pointerEvents = 'none';
                }
            });
        });
    });
}
"""

# Add calls to the DOMContentLoaded block
old_init = "    initTyping();          // Hero subtitle typewriter"
new_init = old_init + "\n    initCardTilt();        // 3-D card tilt on project cards\n    initProjectFilter();   // Project category filter"

js = js.replace(old_init, new_init)
js += NEW_JS

with open(f, "w", encoding="utf-8") as fh:
    fh.write(js)

print("JS updated successfully")
