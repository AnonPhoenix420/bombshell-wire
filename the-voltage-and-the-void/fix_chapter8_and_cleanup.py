import os
from bs4 import BeautifulSoup

CLEAN_CSS = """
.terminal-nav {
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px dashed #00f3ff;
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
.phantom-index-table {
    margin: 2.5rem auto 1.5rem auto;
    border: 1px solid #00f3ff;
    background: rgba(0,243,255,0.03);
    padding: 0.8rem 1rem;
    text-align: center;
    box-shadow: inset 0 0 8px rgba(0,243,255,0.2);
}
.phantom-index-table a {
    color: #00f3ff;
    text-decoration: none;
    text-shadow: 0 0 6px rgba(0,243,255,0.4);
    font-family: monospace;
    font-weight: bold;
    font-size: 0.95rem;
}
"""

def fix_all_chapters():
    # Detect chapters and max pages dynamically
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
        chapters = {i: (10 if i <= 5 else 16) for i in range(1, 10)}

    max_chap = max(chapters.keys())

    for chap, max_pages in chapters.items():
        for page in range(1, max_pages + 1):
            filename = f"chapter-{chap}-page-{page}.html"
            if not os.path.exists(filename):
                continue

            with open(filename, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            # 1. Strip ALL extra injected boxes, grid tables, or summary widgets inside content
            for el in soup.find_all(['div', 'section'], class_=['chapter-nav-box', 'operational-arc', 'nav-links']):
                text_content = el.get_text()
                # Remove if it contains chapter navigation widgets, big blocks, or wrong labels
                if 'P.1' in text_content or 'Epilogue' in text_content or 'Master Index' in text_content or 'PROCEED TO' in text_content:
                    el.decompose()

            # Remove any duplicate old terminal-nav bars or phantom tables
            for old_nav in soup.find_all(class_='terminal-nav'):
                old_nav.decompose()
            for old_phantom in soup.find_all(class_='phantom-index-table'):
                old_phantom.decompose()

            # 2. Ensure CSS is clean
            head = soup.find('head')
            if head:
                for st in head.find_all('style', id=['terminal-nav-styles', 'uniform-nav-styles', 'clean-nav-styles']):
                    st.decompose()
                style_tag = soup.new_tag('style', id='clean-nav-styles')
                style_tag.string = CLEAN_CSS
                head.append(style_tag)

            # 3. Build EXACTLY ONE clean, uniform bottom navigation bar per page
            nav_container = soup.new_tag('div')
            nav_container['class'] = 'terminal-nav'

            left_group = soup.new_tag('div')
            left_group['style'] = 'display: flex; gap: 0.8rem; flex-wrap: wrap;'

            # Previous button logic
            if page > 1:
                prev_btn = soup.new_tag('a', href=f'chapter-{chap}-page-{page-1}.html')
                prev_btn['class'] = 'terminal-btn'
                prev_btn.string = '◄ Previous Page'
                left_group.append(prev_btn)
            elif chap > 1:
                prev_chap_max = chapters.get(chap - 1, 10)
                prev_btn = soup.new_tag('a', href=f'chapter-{chap-1}-page-{prev_chap_max}.html')
                prev_btn['class'] = 'terminal-btn'
                prev_btn.string = f'◄ End of Ch {chap-1}'
                left_group.append(prev_btn)

            index_btn = soup.new_tag('a', href='index.html')
            index_btn['class'] = 'terminal-btn'
            index_btn.string = '▲ Index'
            left_group.append(index_btn)
            nav_container.append(left_group)

            right_group = soup.new_tag('div')
            right_group['style'] = 'display: flex; gap: 0.8rem; flex-wrap: wrap;'

            # Next button logic (Last page of chapter points to next chapter, never Epilogue)
            if page < max_pages:
                next_btn = soup.new_tag('a', href=f'chapter-{chap}-page-{page+1}.html')
                next_btn['class'] = 'terminal-btn'
                next_btn.string = 'Next Page ►'
                right_group.append(next_btn)
            elif chap < max_chap:
                next_btn = soup.new_tag('a', href=f'chapter-{chap+1}-page-1.html')
                next_btn['class'] = 'terminal-btn'
                next_btn.string = f'► Start Ch {chap+1}'
                right_group.append(next_btn)

            nav_container.append(right_group)

            # 4. If it's the last page of the chapter, append the clean Phantom Index table banner
            if page == max_pages:
                phantom_table = soup.new_tag('div')
                phantom_table['class'] = 'phantom-index-table'
                phantom_link = soup.new_tag('a', href='index.html')
                phantom_link.string = "[ PHANTOM INDEX // JUMP BACK TO DIRECTORY ]"
                phantom_table.append(phantom_link)
                soup.body.append(phantom_table)

            soup.body.append(nav_container)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup))

    print("SUCCESS: Stripped all big blocks and extra tabs, fixed Chapter 8 links, removed 'Epilogue' labels, and locked in clean neon blue nav across all files.")

if __name__ == '__main__':
    fix_all_chapters()
