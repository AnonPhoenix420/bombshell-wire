import os
import re

def fix_files():
    count = 0
    for page in range(1, 21):
        filename = f"chapter-8-page-{page}.html"
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Fix background and add CRT green side borders/framing matching Chapter 1 style
        # Replace body style
        old_body_style = """        body {
            background-color: #05080c;
            color: #e6edf3;
            font-family: monospace;
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }"""
        
        new_body_style = """        body {
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
        }"""
        
        content = content.replace(old_body_style, new_body_style)
        
        # 2. Update keyword colors in paragraphs:
        # HAARP -> Neon Pink (#ff007f)
        # cyph3r/cipher -> Neon Green (#00ff66)
        # DEW/DEWs -> Neon Orange (#ff9900)
        
        # We replace the span generator helper logic or directly replace rendered spans/text
        content = content.replace('style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;"', 'style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;"')
        
        # Regex or direct string replacements for keyword formatting inside the HTML
        # Let's ensure HAARP is neon pink, cyph3r/cipher is neon green, DEW/DEWs is neon orange
        
        def replace_keywords(match):
            word = match.group(0)
            lower = word.lower()
            if 'haarp' in lower:
                return f'<span style="color: #ff007f; text-shadow: 0 0 8px rgba(255,0,127,0.9); font-weight: bold;">{word}</span>'
            elif 'cyph3r' in lower or 'cipher' in lower:
                return f'<span style="color: #00ff66; text-shadow: 0 0 8px rgba(0,255,102,0.9); font-weight: bold;">{word}</span>'
            elif 'dew' in lower:
                return f'<span style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;">{word}</span>'
            return word

        # Clean up any existing colored spans for these keywords first to avoid nesting duplication
        content = re.sub(r'<span[^>]*>(HAARP|cyph3r|cipher|DEW|DEWs)</span>', r'\1', content, flags=re.IGNORECASE)
        
        # Apply new precise coloring rules
        content = re.sub(r'\b(HAARP)\b', r'<span style="color: #ff007f; text-shadow: 0 0 8px rgba(255,0,127,0.9); font-weight: bold;">\1</span>', content)
        content = re.sub(r'\b(cyph3r|cipher)\b', r'<span style="color: #00ff66; text-shadow: 0 0 8px rgba(0,255,102,0.9); font-weight: bold;">\1</span>', content, flags=re.IGNORECASE)
        content = re.sub(r'\b(DEWs?)\b', r'<span style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;">\1</span>', content, flags=re.IGNORECASE)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

    print(f"SUCCESS: Updated CRT green side borders and exact keyword colors (HAARP = Neon Pink, CYPH3R = Neon Green, DEW = Neon Orange) across {count} Chapter 8 pages without touching story text.")

if __name__ == '__main__':
    fix_files()
