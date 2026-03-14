
f = r"d:\Documents\Z_PORTFOLIO\style.css"
with open(f, "r", encoding="utf-8") as fh:
    css = fh.read()

# Find and patch: ensure mobile-overlay and mob-content start hidden properly
# Also ensure old .mobile-menu / .mobile-link CSS is removed
OLD = """.mobile-overlay {
  position: fixed;
  inset: 0;
  z-index: 990;
  display: flex;
  align-items: stretch;
  pointer-events: none;
  visibility: hidden;
  transition: visibility 0s 0.45s;
}"""

NEW = """.mobile-overlay {
  position: fixed;
  inset: 0;
  z-index: 990;
  pointer-events: none;
  visibility: hidden;
  transition: visibility 0s 0.45s;
}"""

if OLD in css:
    css = css.replace(OLD, NEW)
    print("Fixed mobile-overlay display")
else:
    print("WARNING: mobile-overlay not found exactly")

# Remove old .mobile-menu and .mobile-link rules if they exist
import re
# Remove any leftover old mobile styles
old_patterns = [
    r'\n\.mobile-menu \{[^}]+\}',
    r'\n\.mobile-menu\.open \{[^}]+\}',
    r'\n\.mobile-link \{[^}]+\}',
    r'\n\.mobile-link:hover \{[^}]+\}',
]
for p in old_patterns:
    css, n = re.subn(p, '', css)
    if n: print(f"Removed: {p[:40]}")

with open(f, "w", encoding="utf-8") as fh:
    fh.write(css)
print("Done")
