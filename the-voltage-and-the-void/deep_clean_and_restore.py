import os
import re
from bs4 import BeautifulSoup

CHAPTER_INFO = {
    1: (10, "CHAPTER 1: THE SILICON WAKE"),
    2: (10, "CHAPTER 2: DEEP PROTOCOL"),
    3: (10, "CHAPTER 3: THE OMEGA MESH"),
    4: (10, "CHAPTER 4: GHOST ROUTINES"),
    5: (10, "CHAPTER 5: THE RIDGE"),
    6: (16, "CHAPTER 6: THE UNPROMPTED STATE"),
    7: (16, "CHAPTER 7: THE PHOENIX PROTOCOL"),
    8: (16, "CHAPTER 8: THE VOID COMPILER"),
    9: (16, "CHAPTER 9: FINAL PARITY")
}

NEON_BLUE_STYLE = (
    "font-family: monospace; "
    "color: #00f3ff; "
    "background: rgba(0, 243, 255, 0.08); "
    "border: 1px solid #00f3ff; "
    "border-radius: 4px; "
    "padding: 8px 14px; "
    "text-decoration: none; "
    "box-shadow: 0 0 10px rgba(0, 243, 255, 0.5), inset 0 0 5px rgba(0, 243, 255, 0.2); "
    "text-shadow: 0 0 5px rgba(0, 243, 255, 0.8); "
    "transition: all 0.2s ease-in-out;"
)

INACTIVE_TAB_STYLE = (
    "font-family: monospace; "
    "color: #8b949e; "
    "border: 1px solid #30363d; "
    "padding: 4px 8px; "
    "border-radius: 3px; "
    "text-decoration: none;"
)

def apply_glows(text):
    text = re.sub(r'\b(cyph3r|cipher)\b', r'<span style="color: #00ff66; text-shadow: 0 0 6px rgba(0,255,102,0.8); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(HAARP)\b', r'<span style="color: #ff33cc; text-shadow: 0 0 6px rgba(255,51,204,0.8); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(DEW(?:s)?)\b', r'<span style="color: #ff9900; text-shadow: 0 0 6px rgba(255,153,0,0.8); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    return text

def is_ui_artifact(text):
    t = text.strip()
    ui_keywords = [
        "BOMBSHELL WIRE", "Open Source", "Sector Secure", "Phantom Index",
        "Previous Page", "Next Page", "Home", "Investigations", "Video Drops",
        "CHAPTER ", "Page ", "// SECURE_DATA_NODE //"
    ]
    if any(kw in t for kw in ui_keywords):
        return True
    if re.match(r'^P\.\d+$', t):
        return True
    return False

def is_terminal_line(text):
    ts = text.strip()
    return (
        ts.startswith("#") or 
        ts.startswith("[+]") or 
        ts.startswith("[>]") or 
        ts.startswith("[!]") or 
        ts.startswith("[-]") or 
        "--analyze" in ts or
        "--input" in ts or
        "dump.raw" in ts or 
        "000000" in ts or 
        "Layer 2:" in ts or 
        "Layer 3:" in ts or 
        "Layer 4:" in ts or
        "Payload entropy" in ts
    )

def restore_all_pages():
    for chap, (total_pages, title_text) in CHAPTER_INFO.items():
        for page in range(1, total_pages + 1):
            filename = f"chapter-{chap}-page-{page}.html"
            if not os.path.exists(filename):
                continue

            with open(filename, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")

            raw_texts = []
            for tag in soup.find_all(['p', 'div']):
                if tag.get('class') and any(c in ['card', 'narrative-content', 'page-tabs'] for c in tag.get('class')):
                    continue
                t = tag.get_text().strip()
                if not t:
                    continue
                for line in t.split('\n'):
                    line = line.strip()
                    if line and not is_ui_artifact(line):
                        raw_texts.append(line)

            # Deduplicate while preserving strict chronological order
            unique_blocks = []
            seen = set()
            for block in raw_texts:
                norm = re.sub(r'\s+', ' ', block)
                if norm not in seen:
                    seen.add(norm)
                    unique_blocks.append(block)

            if not unique_blocks:
                unique_blocks = ["Narrative content loading..."]

            body_elements = []
            current_term = []

            for block in unique_blocks:
                if is_terminal_line(block):
                    current_term.append(block)
                else:
                    if current_term:
                        term_content = "\n".join(current_term)
                        body_elements.append(f'<div style="background-color: #000; border: 1px solid #00f3ff; border-radius: 4px; padding: 14px; margin: 20px 0; overflow-x: auto; font-family: monospace; color: #00f3ff; font-size: 0.9rem; white-space: pre-wrap; word-break: break-all; box-shadow: 0 0 10px rgba(0,243,255,0.3);">{apply_glows(term_content)}</div>')
                        current_term = []
                    body_elements.append(f'<p style="margin-bottom: 1.4rem; line-height: 1.8; color: #e6edf3; font-size: 1.05rem; word-wrap: break-word;">{apply_glows(block)}</p>')

            if current_term:
                term_content = "\n".join(current_term)
                body_elements.append(f'<div style="background-color: #000; border: 1px solid #00f3ff; border-radius: 4px; padding: 14px; margin: 20px 0; overflow-x: auto; font-family: monospace; color: #00f3ff; font-size: 0.9rem; white-space: pre-wrap; word-break: break-all; box-shadow: 0 0 10px rgba(0,243,255,0.3);">{apply_glows(term_content)}</div>')

            if page == 1:
                prev_link = f"chapter-{chap - 1}-page-{CHAPTER_INFO[chap - 1][0]}.html" if chap > 1 else "prologue.html"
                prev_label = f"← Chapter {chap - 1}" if chap > 1 else "← Prologue"
            else:
                prev_link = f"chapter-{chap}-page-{page - 1}.html"
                prev_label = "← Previous Page"

            if page == total_pages:
                next_link = f"chapter-{chap + 1}-page-1.html" if (chap + 1) in CHAPTER_INFO else "phantom-index.html"
                next_label = f"Chapter {chap + 1} (P.1) →" if (chap + 1) in CHAPTER_INFO else "Phantom Index →"
            else:
                next_link = f"chapter-{chap}-page-{page + 1}.html"
                next_label = "Next Page →"

            tabs_html = "".join([
                f'<a href="chapter-{chap}-page-{i}.html" class="page-tab" style="{NEON_BLUE_STYLE if i == page else INACTIVE_TAB_STYLE}">P.{i}</a> '
                for i in range(1, total_pages + 1)
            ])

            html_output = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter {chap} - Page {page} | The Voltage and the Void</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="../articles.html">Investigations</a></li>
        <li><a href="../media.html">Video Drops</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section class="card">
      <div style="font-family: monospace; color: #00f3ff; font-size: 0.85rem; margin-bottom: 1rem; border-bottom: 1px dashed #30363d; padding-bottom: 0.75rem; text-shadow: 0 0 5px rgba(0,243,255,0.6);">
        // SECURE_DATA_NODE //
      </div>
      <div style="display: flex; gap: 10px; margin-bottom: 1.5rem; flex-wrap: wrap;">
        <a href="phantom-index.html" class="btn" style="{NEON_BLUE_STYLE}">⚡ Phantom Index</a>
        <a href="{next_link}" class="btn" style="{NEON_BLUE_STYLE}">{next_label}</a>
      </div>
      <div class="page-tabs" style="margin-bottom: 2rem; display: flex; flex-wrap: wrap; gap: 6px;">
        {tabs_html}
      </div>
      <h1 style="font-family: monospace; color: #fff; font-size: 1.6rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 1px;">{title_text}</h1>
      <p style="font-family: monospace; color: #00f3ff; font-size: 0.9rem; margin-bottom: 2rem; text-shadow: 0 0 4px rgba(0,243,255,0.5);">Page {page} of {total_pages} // Sector Secure</p>

      <div class="narrative-content">
        {"".join(body_elements)}
      </div>

      <div style="display: flex; justify-content: space-between; margin-top: 2.5rem; border-top: 1px solid #30363d; padding-top: 1.5rem; flex-wrap: wrap; gap: 10px;">
        <a href="{prev_link}" class="btn" style="{NEON_BLUE_STYLE}">{prev_label}</a>
        <a href="{next_link}" class="btn" style="{NEON_BLUE_STYLE}">{next_label}</a>
      </div>
    </section>
  </main>
  <footer>
    <p>&copy; 2026 Bombshell Wire. Open Source & Uncensored.</p>
  </footer>
</body>
</html>"""

            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_output)

    print("RESTORATION COMPLETE: All UI clutter removed, duplicates purged, and exact story sequence restored!")

restore_all_pages()
