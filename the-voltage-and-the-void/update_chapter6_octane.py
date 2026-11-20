import os

pages = {}

site_header = """  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="../investigations.html">Investigations</a></li>
        <li><a href="../video-drops.html">Video Drops</a></li>
      </ul>
    </nav>
  </header>"""

def get_ch6_nav_block(current_page, total_pages=12):
    prev_link = f"chapter-6-page-{current_page - 1}.html" if current_page > 1 else "chapter-5-page-10.html"
    next_link = f"chapter-6-page-{current_page + 1}.html" if current_page < total_pages else "chapter-7-page-1.html"
    
    prev_text = "← Prev" if current_page > 1 else "← Ch. 5"
    next_text = "Next Page →" if current_page < total_pages else "Ch. 7 Page 1 →"

    buttons = []
    for i in range(1, total_pages + 1):
        if i == current_page:
            buttons.append(f'<span style="background: var(--terminal-green); color: #000; padding: 6px 10px; border-radius: 4px; font-family: monospace; font-weight: bold; font-size: 0.85rem;">P.{i}</span>')
        else:
            buttons.append(f'<a href="chapter-6-page-{i}.html" style="background: #21262d; color: var(--terminal-green); padding: 6px 10px; border: 1px solid var(--border-color); border-radius: 4px; text-decoration: none; font-family: monospace; font-size: 0.85rem; font-weight: bold;">P.{i}</a>')

    return f"""
    <div style="margin: 1.5rem 0; display: flex; flex-direction: column; gap: 10px;">
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; padding: 8px 14px; border-radius: 4px;">⚡ Phantom Index</a>
        <a href="../index.html" class="nav-btn" style="background: #21262d; color: #c9d1d9; text-decoration: none; padding: 8px 14px; border: 1px solid var(--border-color); border-radius: 4px;">🏠 Portal Home</a>
        <a href="{prev_link}" class="nav-btn" style="background: #21262d; color: #c9d1d9; text-decoration: none; padding: 8px 14px; border: 1px solid var(--border-color); border-radius: 4px;">{prev_text}</a>
      </div>
      
      <div style="margin-top: 5px;">
        <a href="{next_link}" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 18px; border-radius: 4px; font-family: monospace; font-size: 1rem;">{next_text}</a>
      </div>

      <div style="margin-top: 15px; padding: 12px; background: #161b22; border: 1px solid var(--border-color); border-radius: 6px;">
        <p style="color: #8b949e; font-size: 0.8rem; font-family: monospace; margin-bottom: 8px;">CHAPTER 6 NAVIGATION (P.1 - P.12):</p>
        <div style="display: flex; gap: 6px; flex-wrap: wrap;">
          {''.join(buttons)}
        </div>
      </div>
    </div>
    """

ch6_contents = {
    1: ("The Ash-Flat Breakout", """<p>As the superheated shockwave and incandescent wall of ash blasted over the creek bed, Marcus slammed his terminal shut, his face caked in toxic gray grit. 'Black Ridge is a smoking crater. Move!' He hauled Elena to her feet, shoving her stumbling toward the drainage trench where Kyle—a local network runner who knew every subterranean service pipe by heart—was revving a rigged electric utility cart.</p>
    <p>'Get in! The entire mountain cap is liquefying!' Kyle screamed over the deafening roar of collapsing stone. But before the cart's tires could catch the gravel, the sky above didn't just break—it melted. An orbital directed-energy pulse lanced down with the blinding speed of light, turning twelve thousand tons of reinforced basalt into a surging wave of glowing orange magma.</p>
    <p>Ten feet away, Kyle never even dropped into gear. A secondary thermal back-blast swept across the trench, catching him mid-stride. There was no explosion, just an instantaneous, blinding white flash and the sickening odor of scorched ozone and cooked flesh. Kyle’s silhouette vanished, leaving only a smoking heap of carbon collapsed against the basalt wall.</p>"""),
    
    2: ("Blood on the Salt", """<p>Marcus didn't have a second to process the smell. He dropped hard onto his knees, grabbing Elena by the tactical webbing as a jagged concrete slab crashed down right where she had been standing. He threw his shoulder against the debris, muscles tearing and vision blackening at the edges until the heavy block rolled aside with a wet, grinding shriek.</p>
    <p>When he hauled her up, his hands plunged straight into warm, arterial blood. A five-inch shard of razor-sharp aluminum fuselage had punched clean through her left flank, buried deep between her ribs and hip.</p>
    <p>'Don't... don't pull it,' she gasped, her teeth coated in pink froth, her hand locking onto his wrist with desperate strength. 'It's blocking... the line.' Above them, the low, pulsing thrum of orbital targeting scanners vibrated through their skulls. Their transport was a melted puddle of slag half a mile back. No wheels. No armor. Just an open expanse of lethal badlands ahead.</p>"""),

    3: ("The Quad-Walker", """<p>A high-pitched metallic shriek tore through the smoke behind them. Marcus whirled around, unslinging his cracked terminal deck. Dropping out of the ash cloud thirty yards back came a low-slung, four-legged military hunter-killer. Its hydraulic legs hammered the scree with terrifying speed, its optical sensor locking an infrared targeting laser straight onto Marcus's chest.</p>
    <p>'Move!' Marcus roared, yanking Elena into a brutal sprint that tore a gut-wrenching scream from her throat as her injured leg took weight. She unholstered her sidearm with a shaking hand, blinking back crimson sweat to track the advancing machine.</p>
    <p>The quad-walker’s top-mounted turret spun up with a dry, mechanical scream. Marcus didn't hesitate—he ripped a high-intensity thermal decoy flare from his web gear, cracked the base against his thigh, and hurled it directly into the machine's central optical lens. Sparks exploded in a blinding cascade as the blind walker fired a wild, deafening burst into the canyon walls.</p>"""),

    4: ("Trauma in the Wash", """<p>They burst out of the ravine and plunged straight into an unforgiving, blinding white expanse of dry alkaline wash. The midday heat radiating off the salt pan hit like a physical blow. Marcus was carrying ninety percent of Elena’s dead weight now, her combat boots dragging a bloody, jagged furrow through the abrasive white crust.</p>
    <p>'Marcus... drop the pack,' she breathed, her voice a fragile, fluttering whisper against his chest. 'The heavy payload batteries... you're carrying a death sentence. Leave them.'</p>
    <p>'Shut up!' Marcus snarled through cracked, bleeding lips. 'If we drop the drives, everything Kyle died for goes into the void. We keep moving!'</p>
    <p>He glanced down at his chest rig. The HUD on his wrecked deck flickered an amber warning pulse: <em>HYPOVOLEMIC SHOCK // BP 80/45 // CRITICAL FLUID DEPLETION</em>. She was fading fast, her body temperature dropping into the danger zone.</p>"""),

    5: ("The EMP Sacrifice", """<p>A piercing digital shriek cut through the wind. Marcus froze. On his chest deck, a red tactical grid had suddenly materialized, locking down a forty-meter kill radius directly on their coordinates. The low-earth satellite mesh had picked up Elena's suit telemetry.</p>
    <p>'They've got our bio-signature,' Marcus hissed, his heart hammering against his ribs like a sledgehammer. 'The medical harness is broadcasting a live beacon.'</p>
    <p>With violent precision, Marcus yanked a thick copper grounding shunt from his pocket and jammed it straight across the deck's primary capacitor board. A blinding arc of blue static snapped across his knuckles, filling the air with the stinging reek of fried silicon. The screen shuddered, fractured into vertical white static, and went permanently dark. Comms, maps, and tracking—all dead in a millisecond.</p>
    <p>'We're ghosts,' Marcus panted, shoving the smoking wreck away. 'No digital footprint. Just run.'</p>"""),

    6: ("The Salt-Flat Crawl", """<p>The next three hours blurred into an unyielding gauntlet of pure physical torment. The sun plummeted toward the western horizon, painting the badlands in violent shades of bruised purple and toxic yellow. Marcus’s shoulders burned white-hot where the heavy payload straps dug deep into his flesh. Elena had stopped moving entirely; her limbs hung slack, her weight heavy and lifeless against his torso.</p>
    <p>He talked constantly—barking orders, reciting code fragments, screaming at the empty desert just to keep himself from collapsing into the salt. The sound of his own voice was the only thing standing between them and the abyss.</p>
    <p>As twilight bled across the flats, a jagged silhouette broke the flat horizon: a sunken, half-buried concrete dome ringed by rusted concertina wire. The abandoned Titan II missile silo. Salvation—if they could reach it before the sky opened up.</p>"""),

    7: ("The Basin Approach", """<p>They dragged themselves across the perimeter fence through a gap torn by ancient storms. The silo dome rose like an industrial tombstone out of the dirt. But as they crossed the cracked concrete apron, the ground beneath their boots began to shudder with a deep, violent mechanical thrum.</p>
    <p>Marcus stopped dead, his breath catching. It wasn't an earthquake. It was the high-frequency hydraulic whine of orbital targeting locks shifting into position overhead. The machine had calculated their destination and was priming the impact zone.</p>
    <p>'Almost there, Elena,' Marcus strained, lifting her higher against his chest. 'The emergency hatch is right by the vent stack.'</p>
    <p>Elena’s eyes flickered open once, her pale lips moving silently before her head dropped back against his shoulder.</p>"""),

    8: ("The Silo Strike", """<p>High above the gathering storm clouds, the screaming turbine whine of tactical strike drones ripped through the atmosphere. Three automated aircraft dropped out of the haze, their ventral lasers painting the concrete apron in searing crimson gridlines.</p>
    <p>'Down!' Marcus bellowed, throwing himself and Elena into a shallow erosion trench just as a blinding white flash incinerated the ground fifty feet behind them. A kinetic penetrator slammed into the concrete with the force of an earthquake, turning tons of stone into a roaring geyser of white-hot shrapnel.</p>
    <p>The shockwave slammed over them like a tidal wave. Through the swirling cloud of dust and pulverized concrete, Marcus spotted it: the heavy steel emergency personnel hatch at the base of the dome, cracked open four inches with a frantic yellow strobe flashing in the gap.</p>"""),

    9: ("Clawing Through Slag", """<p>Marcus dragged Elena up from the dirt, his vision swimming in a haze of red and black. He half-carried, half-dragged her across the smoking crater field as a second high-pitched acoustic whine screamed down from the drone swarm.</p>
    <p>'Grab the wheel!' Marcus yelled, shoving Elena's hand onto the rusted manual override dial of the blast door while he threw his entire body weight against the massive three-ton steel plate.</p>
    <p>Metal screeched against metal as the heavy door groaned open just wide enough for a body. From the pitch-black void inside, a pair of thick, heavily scarred hands reached out through the dark, snagging Elena by her vest and yanking her inside an instant before a second missile obliterated the outer apron.</p>"""),

    10: ("Sealing the Vault", """<p>Marcus dove headfirst through the narrow gap as the blast wave slammed the steel door shut behind him with the force of a naval cannon, rattling his teeth in his skull. He hit the cold steel catwalk, gasping for thick, stale air heavy with machine oil and hydraulic fluid.</p>
    <p>Above them, a massive, bearded figure in a grease-stained canvas apron threw his full weight onto a heavy pneumatic locking lever. Four massive steel pins slammed home into the frame with resonant, earth-shaking thuds, sealing the bunker off from the radioactive hell outside.</p>
    <p>'You're late, Vance,' a deep, gravelly voice echoed from the shadows. Phoenix stood over them, a heavy manual lever in one hand and a blood-stained surgical clamp in the other.</p>"""),

    11: ("The Silo Sanctuary", """<p>Phoenix dropped instantly to one knee beside Elena, his thick, calloused fingers moving with terrifying, practiced speed as he sliced her tactical vest open with heavy shears. 'She’s hemorrhaging fast. The shrapnel is pinned directly against her iliac artery. If I pull it without an immediate clamp, she's gone in sixty seconds.'</p>
    <p>Marcus collapsed onto his back on the diamond-plate floor, wheezing for air as he stared up into the massive three-hundred-foot dark cavern of the launch tube. Ancient vacuum-tube racks hummed along the walls, casting a steady, amber glow across the gloom.</p>
    <p>'Can you fix her?' Marcus choked out, his hands slick with ash and blood.</p>
    <p>'I can stitch the flesh,' Phoenix grunted, reaching for his tray. 'But outside these walls, the core just locked down its final regional sweep. We're trapped in the deep cellar, and the burners are already lit.'</p>"""),

    12: ("The Final Cellar", """<p>As Phoenix’s surgical clamp locked onto the wound with a sharp metallic click, a low, ominous groaning vibration shuddered through the silo's deep concrete foundations. The orbital bombardment above was shifting to heavy burrowing munitions, pounding directly toward the silo's structural cap.</p>
    <p>Marcus pushed himself back up to his feet, wiping the grit from his eyes. The payloads were safe, Elena was in the hands of a legend, and the surface world had burned to cinders. There was no turning back.</p>
    
    <div style="margin-top: 2rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;">
      <h3 style="color: var(--terminal-green); margin-bottom: 0.5rem; font-family: monospace;">NEXT OPERATIONAL ARC</h3>
      <p style="color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem;">Chapter 6 complete. Proceed to Chapter 7.</p>
      <a href="chapter-7-page-1.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;">CHAPTER 7: The Phoenix Protocol (Page 1) →</a>
    </div>""")
}

for p_num, (subtitle, body_content) in ch6_contents.items():
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page {p_num} | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
{site_header}
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE {p_num} OF 12</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">{subtitle}</p>
      </div>

      {get_ch6_nav_block(p_num, 12)}

      <div class="story-body">
        {body_content}
      </div>

      <div class="story-nav" style="margin-top: 2rem;">
        <a href="chapter-6-page-{p_num-1}.html" class="nav-btn">← Prev</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-{p_num+1}.html" class="nav-btn next-btn">Next Page →</a>
      </div>
    </article>
  </main>
</body>
</html>"""
    
    filename = f"chapter-6-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(page_html)
    print(f"Written high-octane action to {filename}")

print("\nChapter 6 successfully rewritten with high-octane pacing!")
