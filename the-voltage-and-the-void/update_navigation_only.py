import os
from bs4 import BeautifulSoup

CHAPTER_MAX_PAGES = {
    1: 10, 2: 10, 3: 10, 4: 10, 5: 10,
    6: 16, 7: 16, 8: 16, 9: 16
}

NAV_CSS = """
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
    border: 1px solid #00f3ff;
    padding: 0.5rem 1rem;
    color: #00f3ff;
    text-decoration: none;
    background: rgba(0,243,255,0.05);
    text-shadow: 0 0 6px rgba(0,243,255,0.4);
    font-family: monospace;
    font-weight: bold;
    display: inline-block;
}
.terminal-btn:hover {
    background: rgba(0,243,255,0.2);
    box-shadow: 0 0 10px rgba(0,243,255,0.6);
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

def update_navigation():
    updated_count = 0
    for chap, max_pages in CHAPTER_MAX_PAGES.items():
        for page in range(1, max_pages + 1):
            filename = f"chapter-{chap}-page-{page}.html"
            if not os.path.exists(filename):
                continue

            with open(filename, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            # Inject neon blue button CSS into head if not present
            head = soup.find('head')
            if head and not soup.find(id='terminal-nav-styles'):
                style_tag = soup.new_tag('style', id='terminal-nav-styles')
                style_tag.string = NAV_CSS
                head.append(style_tag)

            # Remove old navigation elements to prevent duplicates
            for old_nav in soup.find_all(['div', 'nav'], class_=['nav-links', 'terminal-nav']):
                old_nav.decompose()
            for old_phantom in soup.find_all(class_='phantom-index-table'):
                old_phantom.decompose()

            # Build new neon blue navigation container
            nav_container = soup.new_tag('div')
            nav_container['class'] = 'terminal-nav'

            # Left group (Previous Page / Previous Chapter / Index)
            left_group = soup.new_tag('div')
            left_group['style'] = 'display: flex; gap: 0.8rem; flex-wrap: wrap;'

            if page > 1:
                prev_btn = soup.new_tag('a', href=f'chapter-{chap}-page-{page-1}.html')
                prev_btn['class'] = 'terminal-btn'
                prev_btn.string = '◄ Previous Page'
                left_group.append(prev_btn)
            elif chap > 1:
                prev_chap_max = CHAPTER_MAX_PAGES.get(chap - 1, 10)
                prev_btn = soup.new_tag('a', href=f'chapter-{chap-1}-page-{prev_chap_max}.html')
                prev_btn['class'] = 'terminal-btn'
                prev_btn.string = f'◄ End of Ch {chap-1}'
                left_group.append(prev_btn)

            index_btn = soup.new_tag('a', href='index.html')
            index_btn['class'] = 'terminal-btn'
            index_btn.string = '▲ Index'
            left_group.append(index_btn)
            nav_container.append(left_group)

            # Right group (Next Page / Next Chapter)
            right_group = soup.new_tag('div')
            right_group['style'] = 'display: flex; gap: 0.8rem; flex-wrap: wrap;'

            if page < max_pages:
                next_btn = soup.new_tag('a', href=f'chapter-{chap}-page-{page+1}.html')
                next_btn['class'] = 'terminal-btn'
                next_btn.string = 'Next Page ►'
                right_group.append(next_btn)
            elif chap < 9:
                next_btn = soup.new_tag('a', href=f'chapter-{chap+1}-page-1.html')
                next_btn['class'] = 'terminal-btn'
                next_btn.string = f'► Start Ch {chap+1}'
                right_group.append(next_btn)

            nav_container.append(right_group)

            # If it's the last page of the chapter, append the Phantom Index table banner
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
            updated_count += 1

    print(f"SUCCESS: Updated navigation buttons and Phantom Index table across {updated_count} files with neon blue styling. All narrative text and index.html left untouched.")

if __name__ == '__main__':
    update_navigation()
