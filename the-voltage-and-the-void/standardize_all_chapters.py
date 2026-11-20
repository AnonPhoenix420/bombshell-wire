import os
import re
from bs4 import BeautifulSoup

MASTER_CSS = """
body {
    background-color: #05080c;
    color: #e6edf3;
    font-family: monospace;
    padding: 2.5rem;
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.8;
    border-left: 3px solid #00ff66;
    border-right: 3px solid #00ff66;
    box-shadow: inset 0 0 20px rgba(0,255,102,0.1);
}
.header {
    border-bottom: 1px dashed #00f3ff;
    padding-bottom: 1rem;
    margin-bottom: 2rem;
    color: #00f3ff;
    text-shadow: 0 0 8px rgba(0,243,255,0.6);
}
.page-tabs-top {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px dashed #00f3ff;
}
.page-tab {
    border: 1px solid #00f3ff !important;
    padding: 0.3rem 0.6rem !important;
    color: #00f3ff !important;
    text-decoration: none !important;
    background: rgba(0,243,255,0.05) !important;
    font-family: monospace !important;
    font-size: 0.85rem !important;
    font-weight: bold !important;
    display: inline-block !important;
}
.page-tab.active {
    background: #00f3ff !important;
    color: #05080c !important;
    box-shadow: 0 0 8px rgba(0,243,255,0.8) !important;
}
.page-tab:hover {
    background: rgba(0,243,255,0.2) !important;
    box-shadow: 0 0 10px rgba(0,243,255,0.6) !important;
}
.terminal-nav {
    margin: 2rem 0;
    padding: 1rem 0;
    border-top: 1px dashed #00f3ff;
    border-bottom: 1px dashed #00f3ff;
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: space-between;
    align-items: center;
    font-family: monospace;
}
.terminal-btn {
    border: 1px solid #00f3ff !important;
    padding: 0.5rem 1rem !important;
    color: #00f3ff !important;
    text-decoration: none !important;
    background: rgba(0,243,255,0.05) !important;
    text-shadow: 0 0 6px rgba(0,243,255,0.4) !important;
    font-family: monospace !important;
    font-weight: bold !important;
    display: inline-block !important;
}
.terminal-btn:hover {
    background: rgba(0,243,255,0.2) !important;
    box-shadow: 0 0 10px rgba(0,243,255,0.6) !important;
}
.narrative-content p {
    font-family: monospace;
    font-size: 0.95rem;
    color: #e6edf3;
    margin-bottom: 2rem;
    line-height: 1.8;
    word-wrap: break-word;
}
.terminal-log {
    font-family: monospace;
    color: #00f3ff;
    text-shadow: 0 0 6px rgba(0,243,255,0.4);
    margin: 1.8rem 0;
    line-height: 1.6;
    font-size: 0.88rem;
    word-wrap: break-word;
    font-weight: bold;
}
"""

def process_book():
    # 1. Discover chapters and max pages dynamically from existing files
    chapters = {}
    for filename in os.listdir('.'):
        if filename.startswith('chapter-') and filename.endswith('.html'):
            parts = filename.replace('.html', '').split('-')
            if len(parts) >= 4:
                try:
                    chap = int(parts[1])
                    page = int(parts[3])
                    chapters[chap] = max(chapters.get(chap, 0), page)
                except:
                    pass

    if not chapters:
        chapters = {i: (20 if i == 8 else (16 if i >= 6 else 10)) for i in range(1, 10)}

    max_chapter_num = max(chapters.keys())

    updated_files = 0
    for chap, max_pages in chapters.items():
        for page in range(1, max_pages + 1):
            filename = f"chapter-{chap}-page-{page}.html"
            if not os.path.exists(filename):
                continue

            with open(filename, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            # Extract narrative paragraphs & logs so story text is never lost or altered
            content_container = soup.find('div', class_='narrative-content')
            if not content_container:
                # Fallback: gather all paragraphs and logs from body if class isn't explicit
                body = soup.find('body')
                if body:
                    # Remove navs, headers, tabs, tables first
                    for el in body.find_all(['div', 'nav'], class_=['terminal-nav', 'page-tabs-top', 'header', 'phantom-index-table', 'nav-links', 'chapter-nav-box']):
                        el.decompose()
                    narrative_html = "".join([str(child) for child in body.contents if child.name in ['p', 'div']])
                else:
                    narrative_html = "<p>[Content extraction error]</p>"
            else:
                narrative_html = "".join([str(child) for child in content_container.contents])

            # Build top page number tabs (P.1 to P.N)
            tabs_html = []
            for p in range(1, max_pages + 1):
                active_class = " active" if p == page else ""
                tabs_html.append(f'<a href="chapter-{chap}-page-{p}.html" class="page-tab{active_class}">P.{p}</a>')
            top_tabs_str = "\n".join(tabs_html)

            # Build Navigation links (Top & Bottom identical)
            # Left side: Previous page or Previous chapter / Prologue
            left_links = []
            if page > 1:
                left_links.append(f'<a href="chapter-{chap}-page-{page-1}.html" class="terminal-btn">◄ Previous Page</a>')
            elif chap > 1:
                prev_max = chapters.get(chap - 1, 10)
                left_links.append(f'<a href="chapter-{chap-1}-page-{prev_max}.html" class="terminal-btn">◄ End of Ch {chap-1}</a>')
            else:
                left_links.append(f'<a href="index.html" class="terminal-btn">◄ Prologue</a>')

            left_links.append(f'<a href="index.html" class="terminal-btn">▲ Phoenix Index</a>')

            # Right side: Next page or Next chapter
            right_links = []
            if page < max_pages:
                right_links.append(f'<a href="chapter-{chap}-page-{page+1}.html" class="terminal-btn">Next Page ►</a>')
            elif chap < max_chapter_num:
                right_links.append(f'<a href="chapter-{chap+1}-page-1.html" class="terminal-btn">► Next Chapter (Ch {chap+1})</a>')
            else:
                right_links.append(f'<a href="index.html" class="terminal-btn">▲ Phoenix Index</a>')

            nav_left_str = " ".join(left_links)
            nav_right_str = " ".join(right_links)

            nav_block = f"""
    <div class="terminal-nav">
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
            {nav_left_str}
        </div>
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
            {nav_right_str}
        </div>
    </div>
            """

            # Construct clean, standardized HTML page
            new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chapter {chap} - Page {page} // The Voltage and the Void</title>
    <style>{MASTER_CSS}</style>
</head>
<body>
    <div class="header">
        <h2>CHAPTER {chap}: SECURE DATA NODE</h2>
        <p>Page {page} of {max_pages} // Subterranean Sector</p>
    </div>

    <div class="page-tabs-top">
        {top_tabs_str}
    </div>

    {nav_block}

    <div class="narrative-content">
        {narrative_html}
    </div>

    {nav_block}
</body>
</html>
"""

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_html)
            updated_files += 1

    print(f"SUCCESS: Standardized background, green side borders, top page number tabs, and neon blue top/bottom navigation across {updated_files} chapter files. Story text and placeholders untouched.")

if __name__ == '__main__':
    process_book()
