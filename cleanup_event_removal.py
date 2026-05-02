from pathlib import Path
import re
root = Path('.')
# Remove event navigation items from all HTML pages.
nav_pattern = re.compile(r"<li>\s*<a href=\"event\.html\"[^>]*>.*?</li>\s*", re.DOTALL)
for name in ['index.html', 'about.html', 'admissions.html', 'blog.html', 'blog-single.html', 'contact.html', 'faculty.html', 'event.html']:
    p = root / name
    if not p.exists():
        continue
    text = p.read_text(encoding='utf-8')
    new_text = nav_pattern.sub('', text)
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')

# Remove selected home sections from index.html.
index = root / 'index.html'
if index.exists():
    text = index.read_text(encoding='utf-8')
    # Remove the feature section.
    text = re.sub(r'<!--Begin feature-->[\s\S]*?<!-- End feature -->', '', text)
    # Remove the faculty block (from its heading through its closing comment).
    text = re.sub(r'<h2 class="center">Our Faculty:</h2>[\s\S]*?<!--End our faculty-->', '', text)
    # Remove the current news block.
    text = re.sub(r'<!--Begin current news -->[\s\S]*?<!--End current news -->', '', text)
    # Clean up extra blank lines.
    text = re.sub(r'\n{3,}', '\n\n', text)
    index.write_text(text, encoding='utf-8')

# Delete the event page.
event_file = root / 'event.html'
if event_file.exists():
    event_file.unlink()
