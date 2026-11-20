import os

with open("chapter-6-page-16.html", "r") as f:
    content = f.read()

# Cleaned up Page 16 body with removed redundant text and fixed "heavy" repetition
new_body = """      <div class="story-body">
        <p>From the darkness inside, a pair of thick, heavily scarred hands reached out through the dark, snagging Elena by her vest and yanking her inside an instant before a second missile obliterated the outer apron.</p>
        <p>Marcus dove headfirst through the narrow gap as the blast wave slammed the steel door shut behind him with the force of a naval cannon, rattling his teeth in his skull. He hit the cold steel catwalk, gasping for thick, stale air.</p>
        <p>Above them, a massive, bearded figure threw his full weight onto a pneumatic locking lever. Four massive steel pins slammed home into the frame with resonant, earth-shaking thuds, sealing the bunker off from the radioactive hell outside.</p>
        <p>'You're late, Vance,' Phoenix rasped from the gloom, holding a manual lever in one hand and a blood-stained surgical clamp in the other.</p>
        <p>Phoenix dropped instantly to one knee beside Elena, slicing her tactical vest open with surgical shears as relentless burrowing munitions hammered the structural cap above. There was no turning back.</p>
        
        <div style="margin-top: 2rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;">
          <a href="chapter-7-page-1.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;">CHAPTER 7: The Phoenix Protocol (Page 1) →</a>
        </div>
      </div>"""

import re
content = re.sub(r'<div class="story-body">.*?</div>', new_body, content, flags=re.DOTALL)

with open("chapter-6-page-16.html", "w") as f:
    f.write(content)

print("Chapter 6 Page 16 successfully updated!")
