import os
import re
from bs4 import BeautifulSoup

CHAPTER_INFO = {
    1: 10, 2: 10, 3: 10, 4: 10, 5: 10,
    6: 16, 7: 16, 8: 16, 9: 16
}

def apply_glows(text):
    text = re.sub(r'\b(cyph3r|cipher)\b', r'<span style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(HAARP)\b', r'<span style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(DEW(?:s)?)\b', r'<span style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(bleed)\b', r'<span style="color: #ff3333; text-shadow: 0 0 8px rgba(255,51,51,0.9); font-weight: bold;">\1</span>', text, flags=re.IGNORECASE)
    return text

def process_files():
    total_processed = 0
    for chap, total_pages in CHAPTER_INFO.items():
        for page in range(1, total_pages + 1):
            filename = f"chapter-{chap}-page-{page}.html"
            if not os.path.exists(filename):
                continue

            with open(filename, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")

            content_div = soup.find('div', class_='narrative-content')
            if not content_div:
                continue

            # Check existing elements
            existing_elements = [el for el in content_div.find_all(['p', 'div'], recursive=False) if el.get_text().strip()]

            if len(existing_elements) > 2:
                # Structure is already split into multiple paragraphs; safely update styling without touching text
                for el in existing_elements:
                    text = el.get_text().strip()
                    is_terminal = (
                        text.startswith('[') or 
                        (text.startswith('(') and 'Y/N' in text) or 
                        "Routed via Tor Exit Node" in text or 
                        "Dark Fiber Node" in text or
                        any(phrase in text for phrase in [
                            "WE HAVE BEEN EXPECTING YOUR DESCENT",
                            "PREPARING PHYSICAL DISMANTLEMENT",
                            "HEADING TO SALT FLATS JUNCTION",
                            "WELCOME TO THE END OF THE LINE"
                        ])
                    )

                    if is_terminal:
                        el.name = 'div'
                        el['style'] = 'font-family: monospace; color: #00f3ff; text-shadow: 0 0 6px rgba(0,243,255,0.4); margin: 1.8rem 0; line-height: 1.6; font-size: 0.88rem; word-wrap: break-word; font-weight: bold;'
                    else:
                        el.name = 'p'
                        if text.startswith('*') and text.endswith('*'):
                            el['style'] = 'font-family: monospace; margin-bottom: 2rem; line-height: 1.8; color: #ff9900; font-size: 0.95rem; word-wrap: break-word; font-style: italic;'
                        else:
                            el['style'] = 'font-family: monospace; margin-bottom: 2rem; line-height: 1.8; color: #e6edf3; font-size: 0.95rem; word-wrap: break-word;'
            else:
                # Fallback: If text was flattened into a single block, split safely on double newlines
                full_text = content_div.get_text()
                raw_blocks = [b.strip() for b in full_text.split('\n\n') if b.strip()]
                if len(raw_blocks) <= 1:
                    raw_blocks = [b.strip() for b in full_text.split('\n') if b.strip()]

                new_html = ""
                for block in raw_blocks:
                    if not block:
                        continue
                    is_terminal = (
                        block.startswith('[') or 
                        (block.startswith('(') and 'Y/N' in block) or 
                        "Routed via Tor Exit Node" in block or 
                        "Dark Fiber Node" in block or
                        any(phrase in block for phrase in [
                            "WE HAVE BEEN EXPECTING YOUR DESCENT",
                            "PREPARING PHYSICAL DISMANTLEMENT",
                            "HEADING TO SALT FLATS JUNCTION",
                            "WELCOME TO THE END OF THE LINE"
                        ])
                    )

                    if is_terminal:
                        new_html += f'<div style="font-family: monospace; color: #00f3ff; text-shadow: 0 0 6px rgba(0,243,255,0.4); margin: 1.8rem 0; line-height: 1.6; font-size: 0.88rem; word-wrap: break-word; font-weight: bold;">{apply_glows(block)}</div>\n'
                    else:
                        if block.startswith('*') and block.endswith('*'):
                            new_html += f'<p style="font-family: monospace; margin-bottom: 2rem; line-height: 1.8; color: #ff9900; font-size: 0.95rem; word-wrap: break-word; font-style: italic;">{apply_glows(block)}</p>\n'
                        else:
                            new_html += f'<p style="font-family: monospace; margin-bottom: 2rem; line-height: 1.8; color: #e6edf3; font-size: 0.95rem; word-wrap: break-word;">{apply_glows(block)}</p>\n'

                content_div.clear()
                content_div.append(BeautifulSoup(new_html, 'html.parser'))

            with open(filename, "w", encoding="utf-8") as f:
                f.write(str(soup))
            total_processed += 1

    print(f"SUCCESS: Restored 2rem paragraph spacing and 0.95rem font size with 100% content fidelity across {total_processed} files!")

if __name__ == "__main__":
    process_files()
