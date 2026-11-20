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

def get_ch6_nav_block(current_page, total_pages=16):
    prev_link = f"chapter-6-page-{current_page - 1}.html" if current_page > 1 else "chapter-5-page-10.html"
    next_link = f"chapter-6-page-{current_page + 1}.html" if current_page < total_pages else "chapter-7-page-1.html"
    
    prev_text = "← Prev" if current_page > 1 else "← Ch. 5"
    next_text = "Next Page →" if current_page < total_pages else "Ch. 7 Page 1 →"

    buttons = []
    for i in range(1, total_pages + 1):
        if i == current_page:
            buttons.append(f'<span style="background: var(--terminal-green); color: #000; padding: 5px 8px; border-radius: 4px; font-family: monospace; font-weight: bold; font-size: 0.8rem;">P.{i}</span>')
        else:
            buttons.append(f'<a href="chapter-6-page-{i}.html" style="background: #21262d; color: var(--terminal-green); padding: 5px 8px; border: 1px solid var(--border-color); border-radius: 4px; text-decoration: none; font-family: monospace; font-size: 0.8rem; font-weight: bold;">P.{i}</a>')

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
        <p style="color: #8b949e; font-size: 0.8rem; font-family: monospace; margin-bottom: 8px;">CHAPTER 6 NAVIGATION (P.1 - P.16):</p>
        <div style="display: flex; gap: 5px; flex-wrap: wrap;">
          {''.join(buttons)}
        </div>
      </div>
    </div>
    """

ch6_contents = {
    1: ("The Mountain Collapse", """
    <p>The shockwave didn't just register as sound; it tore through the bedrock like an industrial explosive detonating straight inside the cranium. Marcus buried his face deep into the coarse, sulfurous gravel of the creek bed as twelve thousand tons of reinforced basalt at Black Ridge turned into an incandescent, roaring torrent of liquid orange slag. The orbital directed-energy beam didn't dissipate—it punched straight through the lower structural foundations, vaporizing the quantum annealing cores in a blinding, silent flash of electromagnetic fury that scorched the night sky.</p>
    <p>Marcus scrambled blindly through the choking black fallout, coughing up lungfuls of toxic gray grit. He hauled Elena up by her tactical harness, her boots dragging uselessly as he dragged her toward the lower drainage trench where the escape vector lay buried.</p>
    """),

    2: ("The Wrecked Utility Sled", """
    <p>Fifty yards into the ravine, they slammed head-first into Kyle. The local network runner wasn't staging a clean extraction; he was pinned under a nightmarish tangle of iron. A falling basalt boulder had crushed the front axle of his electric utility sled, fusing the steering column into a twisted knot of smoking steel.</p>
    <p>Blood was arterial and bright, pumping from a deep gash across Kyle's forehead into his eyes. He was half-buried beneath the wreckage, frantically ripping housing panels off the dashboard with bare, bleeding fingers, desperately trying to cross-wire the high-output traction motor by hand while raw electrical sparks showered over his knuckles.</p>
    """),

    3: ("Desperate Hotwire", """
    <p>'The primary bypass is glowing white! The whole valley floor is cooking!' Kyle screamed over the deafening, mechanical shriek of grinding rock and boiling stone. He wasn't waiting for a hero's welcome; he was fighting a frantic, losing battle against a machine that had already locked onto his telemetry.</p>
    <p>Marcus didn't hesitate. He grabbed Elena by the collar and hurled her straight into the metal bed of the utility sled, throwing his own weight against the chassis as Kyle jammed two live, smoking copper leads together.</p>
    <p>The sled's electric motor shrieked in protest, its wheels spinning furiously against the bloody gravel as it fought to wrench itself free from the debris.</p>
    """),

    4: ("Kyle's Horrific End", """
    <p>Before the tires could grip the shelf, the upper atmosphere ruptured entirely. A secondary thermal beam refraction whipped across the trench with zero warning—no sound, no air-raid sirens, just an instantaneous, blinding wall of white-hot glare.</p>
    <p>Kyle was caught mid-stride as he lunged for the rear rail to haul himself aboard. There was no clean death here. The thermal pulse stripped the moisture from his flesh in a millisecond, searing his uniform directly into his skin and carbonizing his frame against the basalt wall.</p>
    <p>His silhouette vanished instantly into a smoking, charred impression seared permanently into the stone, leaving behind only the reek of scorched fat and melted copper.</p>
    """),

    5: ("Arterial Iron", """
    <p>The concussive back-blast threw Marcus violently into the truck bed right on top of Elena. As the sled's motor finally caught, tearing itself out of the trench, a massive slab of falling concrete clipped the side rail with a sickening metallic shriek, pinning Elena's leg against the iron frame.</p>
    <p>Marcus braced his boots against the dashboard, his vision tunneling to black at the edges as he heaved upward with every ounce of muscle fiber he possessed, rolling the concrete block away in a wet, grinding slide.</p>
    <p>When he hauled her upright, his palms plunged straight into warm, dark crimson. A five-inch shard of jagged aluminum fuselage had driven clean through her left flank, wedged deep between her lower ribs and pelvis.</p>
    """),

    6: ("The Plug", """
    <p>'Don't... don't touch it,' she hissed through teeth coated in pink froth, her fingers locking onto Marcus's wrist with a desperate, white-knuckled grip that threatened to break bone. 'It's acting as a plug... if you pull it, the iliac goes in thirty seconds.'</p>
    <p>Above them, the low-frequency thrumming of orbital reconnaissance micro-scanners vibrated through their teeth. Their transport was a half-mile back, melted into an unrecognizable puddle of slag. No wheels. No armor. Just forty miles of open, salt-crusted badlands stretching toward the horizon.</p>
    <p>Two miles out, the sled's battery coughed a final puff of gray smoke and locked up permanently. They were entirely on foot.</p>
    """),

    7: ("The Hunter-Killer", """
    <p>A high-pitched hydraulic whine cut sharply through the howling wind. Marcus whipped around, unholstering his deck as a low-slung, four-legged automated hunter-killer dropped over the rim of the ravine.</p>
    <p>Its articulated titanium legs struck the scree with sharp, rhythmic clacks, its central optical turret whirring as an infrared laser grid swept across the rocks, painting Kyle's carbonized remains before locking straight onto Marcus's chest.</p>
    <p>'Up! Now!' Marcus roared, hooking his arm under Elena's shoulder and heaving her upright. A sharp, agonized cry broke from her lips as her weight hit her shattered leg.</p>
    """),

    8: ("The Flare Blind", """
    <p>The walker's 7.62mm twin-barrel turret spun up with a dry, mechanical screech, pre-calculating their trajectory. Marcus didn't hesitate; he ripped a high-intensity thermal decoy flare from his web gear, cracked the primer against his thigh, and slammed it straight into the machine's primary optical array.</p>
    <p>A blinding cascade of white-hot magnesium sparks erupted across the chassis. The machine stumbled blindly, its turret firing a deafening, erratic burst of heavy rounds into the canyon walls that showered them with razor-sharp rock splinters.</p>
    <p>Marcus dragged Elena into the blinding, featureless expanse of the dry alkaline wash just as the automated killer lost their thermal trail in the glare.</p>
    """),

    9: ("Carrying the Weight", """
    <p>The midday heat radiating off the salt pan hit like an open furnace door, instantly sucking the moisture from their cracked lips. Marcus was carrying ninety percent of Elena’s dead weight now, her combat boots dragging a deep, bloody furrow through the abrasive white crust.</p>
    <p>'Marcus... drop the payload drives,' she breathed, her voice a fragile, rasping whisper against his collarbone. 'The auxiliary batteries... they're weighing you down to the grave. Leave them.'</p>
    <p>'Shut your mouth and keep your feet moving,' Marcus snarled through bleeding lips. 'If we drop the drives, everything Kyle died for is wiped out. We carry the load.'</p>
    """),

    10: ("The Copper Shunt", """
    <p>A piercing digital shriek trilled from Marcus's chest pouch. He froze, his boots sinking an inch into the crust. On the small OLED screen of his deck, a red tactical grid overlay had locked onto their coordinates, shrinking rapidly down to a forty-meter kill box.</p>
    <p>The overhead satellite mesh had picked up Elena's medical harness telemetry. 'They've got our bio-signature,' Marcus hissed, his heart hammering against his ribs like a sledgehammer. 'The suit's emergency transponder is broadcasting live.'</p>
    <p>Without a second wasted, Marcus unzipped his side pocket, yanked out a heavy copper grounding shunt, and jammed it straight across the deck's primary capacitor bank.</p>
    """),
    
    11: ("Going Ghost", """
    <p>A violent arc of blue static snapped across Marcus's knuckles, filling the air with the sharp, stinging reek of fried silicon. The screen shuddered, fractured into vertical white static lines, and went permanently dead. Comms, tracking, and network access vanished in a millisecond.</p>
    <p>'No signal. No footprint,' Marcus panted, shoving the smoking electronics back into his pouch. 'We're ghosts now. Walk west.'</p>
    <p>The next three hours dissolved into an unyielding gauntlet of pure physical torment as the sun plummeted toward the western range, casting bruised shades of violet and toxic yellow across the salt pan.</p>
    """),

    12: ("The Silo Silhouette", """
    <p>Marcus’s shoulders burned white-hot where the heavy straps of the payload case dug deep into his flesh. Elena had stopped moving entirely; her limbs hung dead and uncooperative against his chest, her breathing shallow and irregular.</p>
    <p>He talked constantly—barking tactical code fragments, reciting memory addresses, screaming at the empty desert just to keep his own consciousness from slipping into the salt.</p>
    <p>As twilight bled across the flats, a dark, jagged silhouette broke the flat horizon: a sunken, half-buried concrete dome ringed by rusted concertina wire. The abandoned Titan II missile silo.</p>
    """),

    13: ("The Kinetic Fall", """
    <p>They dragged themselves across the perimeter fence through a gap torn by ancient storms. But as they crossed the cracked concrete apron, the ground beneath their boots began to shudder with a deep, violent mechanical thrum.</p>
    <p>High above the gathering storm clouds, the screaming turbine whine of tactical strike drones ripped through the atmosphere, painting the concrete apron in searing crimson gridlines.</p>
    <p>'Down!' Marcus bellowed, throwing himself and Elena into a shallow erosion trench just as a kinetic penetrator slammed into the concrete with the force of an earthquake, turning tons of stone into a roaring geyser of white-hot shrapnel.</p>
    """),

    14: ("Manual Override", """
    <p>Marcus dragged Elena up from the dirt, his vision swimming in a haze of red and black. He half-carried, half-dragged her across the smoking crater field as a second high-pitched acoustic whine screamed down from the drone swarm.</p>
    <p>'Grab the wheel!' Marcus yelled, shoving Elena's hand onto the rusted manual override dial of the blast door while he threw his entire body weight against the massive three-ton steel plate.</p>
    <p>Metal screeched against metal as the heavy door groaned open just wide enough for a body, revealing the pitch-black void inside.</p>
    """),

    15: ("Sealing the Vault", """<p>From the darkness inside, a pair of thick, heavily scarred hands reached out through the dark, snagging Elena by her vest and yanking her inside an instant before a second missile obliterated the outer apron.</p><p>Marcus dove headfirst through the narrow gap as the blast wave slammed the steel door shut behind him with the force of a naval cannon, rattling his teeth in his skull. He hit the cold steel catwalk, gasping for thick, stale air.</p><p>Above them, a massive, bearded figure threw his full weight onto a heavy pneumatic locking lever. Four massive steel pins slammed home into the frame with resonant, earth-shaking thuds, sealing the bunker off from the radioactive hell outside.</p><p>'You're late, Vance,' Phoenix rasped from the gloom, holding a heavy manual lever in one hand and a blood-stained surgical clamp in the other.</p>"""),

    16: ("The Deep Cellar", """<p>Phoenix dropped instantly to one knee beside Elena, his thick fingers moving with terrifying, practiced speed as he sliced her tactical vest open with heavy shears. 'She’s hemorrhaging fast. The shrapnel is pinned directly against her iliac artery. If I pull it without an immediate clamp, she's gone in sixty seconds.'</p><p>Marcus collapsed onto his back on the diamond-plate floor, wheezing for air as he stared up into the massive three-hundred-foot dark cavern of the launch tube. Ancient vacuum-tube racks hummed along the walls, casting a steady, amber glow across the gloom.</p><p>As Phoenix’s surgical clamp locked onto the wound with a sharp metallic click, a low, ominous groaning vibration shuddered through the silo's deep concrete foundations as heavy burrowing munitions hammered the surface cap above. There was no turning back.</p><div style='margin-top: 2rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;'><h3 style='color: var(--terminal-green); margin-bottom: 0.5rem; font-family: monospace;'>NEXT OPERATIONAL ARC</h3><p style='color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem;'>Chapter 6 complete. Proceed to Chapter 7.</p><a href='chapter-7-page-1.html' class='nav-btn' style='background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;'>CHAPTER 7: The Phoenix Protocol (Page 1) →</a></div>""")
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
        <span class="chapter-tag">CHAPTER 6 • PAGE {p_num} OF 16</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">{subtitle}</p>
      </div>

      {get_ch6_nav_block(p_num, 16)}

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
    print(f"Generated heavy 16-page build for {filename}")

print("\nChapter 6 successfully re-engineered into 16 heavy, cinematic, high-impact pages!")
