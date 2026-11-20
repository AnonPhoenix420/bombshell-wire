import os

with open("chapter-6-page-2.html", "r") as f:
    content = f.read()

# Dense, purely visual, heavyweight prose for Page 2
new_body = """      <div class="story-body">
        <p>Fifty yards deep into the winding concrete-lined service trench, the escape vector abruptly narrowed into a choked bottleneck of twisted rebar and fallen masonry. That was where the roar of the mountain resolved into something human: the frantic, rhythmic clanging of a wrench hammering against a jammed steel casing.</p>
        
        <p>Kyle was locked beneath a nightmarish tangle of iron. Three seconds before Marcus and Elena rounded the corner, a multi-ton slab of basalt had sheared off the vault ceiling, dropping directly onto the front-left suspension of his heavy electric utility sled. The impact had crushed the steering housing flat, driving the iron steering column six inches deep into the heavy rubber floor mat and pinning Kyle’s shins immovably against the deformed footwell.</p>

        <p>The sled's lead-acid battery housing had cracked cleanly down the center under the tectonic pressure. A steady geyser of boiling, caustic electrolyte was hissing violently onto the hot chassis, venting an acrid, choking wall of white vapor that burned the back of the throat and made the eyes water instantly as the entire concrete trench groaned under the shifting weight of the dying mountain.</p>
      </div>"""

import re
content = re.sub(r'<div class="story-body">.*?</div>', new_body, content, flags=re.DOTALL)

with open("chapter-6-page-2.html", "w") as f:
    f.write(content)

print("Chapter 6 Page 2 successfully rewritten with pure visual and mechanical depth!")
