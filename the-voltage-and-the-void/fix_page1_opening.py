import os

with open("chapter-6-page-1.html", "r") as f:
    content = f.read()

# The improved, high-tension opening for Page 1
new_body = """      <div class="story-body">
        <p>The shockwave hit like a physical wall of solid lead, knocking Marcus off his feet and burying his face in a drift of scorching, toxic gray ash. The entire upper ridge of Black Ridge didn't just collapse—it atomized. Twelve thousand tons of granite vaporized into a roaring, blinding tsunami of white-hot slag. Marcus scrambled blindly through the choking dark, clawing Elena up by her tactical vest and dragging her stumbling toward the lower drainage trench.</p>

        <p>That's where they collided with Kyle. The local network runner wasn't waiting—he was pinned flat behind the rusted chassis of a heavy electric utility sled, frantically crossing exposed ignition wires beneath the dash with shaking, bloodied fingers as the steering column sparked blue. 'The primary bypass is sealed! The whole ridge is sliding!' Kyle roared over the deafening mechanical shriek of grinding rock.</p>

        <p>Marcus shoved Elena into the bed of the cart just as the sky overhead fractured. An orbital directed-energy pulse lanced down with blinding, soundless speed, turning the air into liquid fire. Kyle threw his weight onto the throttle, but a secondary thermal back-blast swept across the trench mid-stride. There was no explosion—just a blinding white flash and the sickening odor of scorched ozone. Kyle vanished into a wall of white heat, leaving behind a smoking, carbonized silhouette pressed against the basalt.</p>
      </div>"""

# Replace old story body in Page 1
import re
content = re.sub(r'<div class="story-body">.*?</div>', new_body, content, flags=re.DOTALL)

with open("chapter-6-page-1.html", "w") as f:
    f.write(content)

print("Chapter 6 Page 1 successfully rewritten with high-stakes tension!")
