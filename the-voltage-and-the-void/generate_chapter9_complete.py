import os

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

def get_ch9_nav_block(current_page, total_pages=16):
    prev_link = f"chapter-9-page-{current_page - 1}.html" if current_page > 1 else "chapter-8-page-16.html"
    next_link = f"chapter-9-page-{current_page + 1}.html" if current_page < total_pages else "chapter-10-page-1.html"
    
    prev_text = "← Prev" if current_page > 1 else "← Ch. 8"
    next_text = "Next Page →" if current_page < total_pages else "Ch. 10 Page 1 →"

    buttons = []
    for i in range(1, total_pages + 1):
        if i == current_page:
            buttons.append(f'<span style="background: var(--terminal-green); color: #000; padding: 5px 8px; border-radius: 4px; font-family: monospace; font-weight: bold; font-size: 0.8rem;">P.{i}</span>')
        else:
            buttons.append(f'<a href="chapter-9-page-{i}.html" style="background: #21262d; color: var(--terminal-green); padding: 5px 8px; border: 1px solid var(--border-color); border-radius: 4px; text-decoration: none; font-family: monospace; font-size: 0.8rem; font-weight: bold;">P.{i}</a>')

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
        <p style="color: #8b949e; font-size: 0.8rem; font-family: monospace; margin-bottom: 8px;">CHAPTER 9 NAVIGATION (P.1 - P.16):</p>
        <div style="display: flex; gap: 5px; flex-wrap: wrap;">
          {''.join(buttons)}
        </div>
      </div>
    </div>
    """

ch9_contents = {
    1: ("The Ion Storm Breaks", """
    <p>The desert sky didn't transition into night; it tore open like a bruised seam. A violent, high-altitude ion-storm sweeping down from the Great Basin slammed into the salt flats with zero warning, turning the horizon into a churning wall of violet haze and static electricity. The air tasted of ozone and burning copper, every loose grain of alkaline dust lifting off the crust to form a stinging, abrasive ground blizzard that scoured exposed skin raw in seconds.</p>
    <p>Marcus hauled Elena out of the drainage pipe exit, his shoulders burning as he dropped her weight against the wind-scoured base of a weathered rock outcrop. Her breathing was shallow, a wet, rattling hiss that signaled the internal strain of the forced crawl.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[ATMOSPHERIC ALERT: ION_STORM_ACTIVE]
WINDSPEED: 68 MPH // GUSTS: 92 MPH
VISIBILITY: < 15 METERS
ELECTROMAGNETIC INTERFERENCE: SEVERE</code></pre>
    <p>'The storm's masking our thermal signature,' Marcus shouted over the shrieking gale, wrapping a thick wool scarf across Elena's mouth and nose. 'If the drones are still painting the sector, the static will blind their optics.'</p>
    """),

    2: ("The Glowing Flats", """
    <p>They pushed out into the open basin, the salt crust crunching beneath their boots like shattered glass. The ion-storm overhead created an eerie, ambient luminescence—a pale, ghost-white glow that bounced off the endless white salt pans, making it impossible to tell where the ground ended and the sky began. The Glass Horizon.</p>
    <p>Every step Elena took sent a white-hot spike of agony up her right thigh. The coarse nylon stitches were biting deep into inflamed muscle tissue, but she didn't utter a single sound, her eyes locked on the dark, jagged silhouette of the distant highway arroyo.</p>
    <p>Marcus kept his arm locked firmly around her waist, half-carrying her forward while his free hand clutched the encrypted payload case tightly against his ribs.</p>
    """),

    3: ("The Thermal Sweep", """
    <p>A sudden, high-pitched acoustic whine cut sharply through the howling wind—not the steady drone of atmospheric turbulence, but the distinct, rhythmic beating of rotor blades and infrared scanning arrays.</p>
    <p>'Get down!' Marcus roared, tackling Elena behind a low, wind-carved ridge of gypsum crust just as a low-slung, autonomous reconnaissance drone swept across the salt flat fifty feet above their heads.</p>
    <p>Its central optical turret was ringed by a pulsing circle of crimson laser diodes, painting the swirling dust storm in a grid of blood-red geometry as it hunted for warm-blooded targets.</p>
    """),

    4: ("The Ion Blindness", """
    <p>The drone hovered in place for three agonizing seconds, its directional thrusters fighting the sixty-mile-an-hour crosswinds with a harsh mechanical roar. The sensor head swiveled directly toward their depression.</p>
    <p>Marcus held his breath, pressing his face flat against the cold salt crust. A stray arc of atmospheric static from the ion-storm snapped across the drone's belly housing with a sharp, blinding electrical pop.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[SENSOR EXCEPTION: OPTICAL_FLARE]
SRC: ATMOSPHERIC_DISCHARGE [EMP SPIKE]
TARGET_LOCK: LOST // RETRYING ALGORITHM...
WARNING: SYSTEM REBOOT REQUIRED</code></pre>
    <p>Sparks showered from the machine's undercarriage as the EMP spike scrambled its targeting processor. With a shrill mechanical squeal, the drone banked hard into the wind and vanished back into the purple murk.</p>
    """),

    5: ("Pushing Through the White", """
    <p>'It's loop-hunting,' Marcus panted, hauling Elena back to her feet as her knees buckled under her. 'When it reboots, it'll run a wider sweep. We have less than ten minutes before it covers this grid square again.'</p>
    <p>They staggered forward into the blinding white expanse. The ground became treacherous—patches of hard, knife-edged salt crust giving way unexpectedly into deep, brine-filled sinkholes that sucked at their boots like quicksand.</p>
    <p>Elena's left boot tore clean off in a patch of suction mud, leaving her sock soaked in freezing, hypersaline sludge. She didn't pause; she kept moving, her teeth bared against the pain.</p>
    """),

    6: ("The Abandoned Rig", """
    <p>Out of the swirling wall of salt and static, a rusted, skeletal structure loomed—an abandoned oil-drilling rig left to rot in the middle of the desert decades ago, its steel derrick standing like an executioner's gallows against the violet storm clouds.</p>
    <p>At the base of the rig sat a battered, mud-caked utility truck, its chassis half-buried in a drift of white gypsum sand. Marcus dragged Elena toward the vehicle, throwing his weight against the driver's side door.</p>
    <p>'Check the ignition!' Elena gasped, collapsing against the rusted fender as Marcus pried the broken steering column open with his combat knife.</p>
    """),

    7: ("Hotwiring the Rust", """
    <p>Marcus ripped the plastic housing away from the dash, exposing a nest of greasy, faded copper wires. The battery was stone dead, drained by months of desert heat and neglect, but the alternator housing still held residual charge.</p>
    <p>He stripped two heavy-gauge leads with his teeth, twisting them together with raw, bleeding fingers as he jammed a flathead screwdriver into the starter slot.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[DIAGNOSTIC: AUXILIARY_IGNITION]
BATTERY_VOLT: 4.2V [CRITICAL LOW]
ALTERNATOR_BYPASS: ENGAGED
CRANK_ATTEMPT: INITIATING...</code></pre>
    <p>The rusted starter motor coughed twice with a hollow, metallic death rattle, then caught with a deafening roar that shook the entire truck bed.</p>
    """),

    8: ("The Pursuit Begins", """
    <p>Marcus shoved the floor shifter into four-wheel drive, dumping the clutch as the rear tires spun furiously in the brine-slicked salt, spraying a roostertail of white slush against the derrick legs.</p>
    <p>As the truck surged forward onto an old, cracked asphalt maintenance road, a high-pitched acoustic shriek ripped through the air behind them. Two automated reconnaissance drones dropped out of the ion-cloud, their searchlights painting the truck's rear bumper in blinding white illumination.</p>
    <p>'They've got our tread pattern!' Elena shouted over the screaming engine, locking her fingers into the dashboard grip as Marcus slammed the accelerator to the floor.</p>
    """),

    9: ("The Asphalt Gauntlet", """
    <p>The truck bounced violently across cracked potholes and fractured asphalt, its worn-out shock absorbers bottoming out with bone-jarring crunches against the frame. Above them, the drones closed the distance, their twin-barrel turrets spinning up with a dry, mechanical whir.</p>
    <p>A burst of heavy kinetic rounds chewed up the asphalt ten feet behind the tailgate, sending a shower of razor-sharp black shards flying into the truck bed.</p>
    <p>'Hold on!' Marcus yelled, wrenching the steering wheel hard to the left as they careened off the maintenance road and plunged directly down a steep, rocky arroyo wash.</p>
    """),

    10: ("The Arroyo Run", """
    <p>The truck slammed into the dry creek bed with an earth-shattering crash, bottoming out its suspension as water and mud splashed across the windshield. Marcus kept his foot planted firmly on the gas, fishtailing wildly between towering canyon walls of crumbling red sandstone.</p>
    <p>The narrow ravine acted as a natural waveguide, amplifying the howling roar of the ion-storm and the screaming turbine whine of the pursuing drones overhead.</p>
    <p>Elena reached into her tactical vest, pulled out a heavy signal booster module, and wired it directly into the dashboard's radio harness. 'If we can bounce an RF burst off the canyon walls, we can blind their tracking optics in the static!'</p>
    """),

    11: ("The EMP Burst", """
    <p>'Do it!' Marcus roared, spinning the wheel to dodge a jagged protrusion of fallen boulder.</p>
    <p>Elena slammed her palm down onto the signal booster's manual trigger switch. A massive, unfiltered surge of high-frequency microwave energy discharged from the truck's modified antenna, echoing violently off the canyon walls.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[TRANSMISSION: BROADBAND_RF_JAMMER]
FREQ: 5.8 GHz // POWER: 50 WATTS [PEAK]
TARGET: DRONE_SWARM_OPTICS
STATUS: MULTI-PATH REFLECTION ACTIVE</code></pre>
    <p>Behind them, a blinding flash of white plasma illuminated the arroyo as the reflected microwave energy fried the drones' primary optical processing units.</p>
    """),

    12: ("Silence in the Air", """
    <p>Both pursuing drones lost their tracking lock simultaneously, their rotors stuttering mid-air before veering wildly off course. One smashed directly into the sandstone canyon wall in a fiery explosion of shrapnel and burning lithium batteries; the second spun out of control into the salt flats above.</p>
    <p>The sudden absence of the high-pitched turbine whine left an eerie, ringing silence in the arroyo, broken only by the steady roar of the wind and the rattling cough of the truck's overheating engine.</p>
    <p>Marcus let out a long, shuddering breath, easing off the accelerator as the truck coasted across the gravel wash.</p>
    """),

    13: ("The Overheated Engine", """
    <p>A thick plume of white steam hissed out from beneath the truck's dented hood, smelling of burnt oil and boiling radiator fluid. Marcus killed the ignition, the engine dying with a final, protesting shudder.</p>
    <p>'We're out of wheels,' Marcus said quietly, grabbing the payload case from the floorboard. 'The block's cracked. We walk the last four miles across the ridge.'</p>
    <p>Elena looked down at her leg. The makeshift bandage was soaked through, dark crimson pooling around the top of her tactical boot. She nodded slowly, her face etched with exhaustion.</p>
    """),

    14: ("Climbing the Ridge", """
    <p>The ascent up the shale-covered ridge was a vertical nightmare. Every handhold of loose, unstable slate threatened to give way, sliding down into the dark canyon below. Marcus pulled Elena upward step by agonizing step, his fingers raw and bleeding against the sharp rock faces.</p>
    <p>The ion-storm was beginning to break overhead, parting to reveal a cold, unblinking expanse of desert stars stretching across the dark infinity of space.</p>
    <p>Below them, the glowing white expanse of the salt flats stretched out like an open wound, silent and untracked once more.</p>
    """),

    15: ("The Overlook", """
    <p>They reached the summit of the ridge just as the first cold rays of dawn began to paint the eastern horizon in bruised shades of indigo and slate gray. Far below them, nestled in the valley floor, sat their final destination: the abandoned communications switching hub known as Terminal Zero.</p>
    <p>It was a massive, brutalist concrete ziggurat ringed by towering microwave arrays and dead fiber-optic trunk lines—the root certificate authority core of the entire regional network.</p>
    <p>'There it is,' Marcus whispered, pointing down toward the concrete monolith. 'The root. Where this whole nightmare started.'</p>
    """),

    16: ("The Final Approach", """
    <p>Elena leaned against a boulder, adjusting the straps of her tactical rig as she stared down at the sprawling concrete fortress below. Her jaw was set, her eyes hard and unyielding despite the blood loss and exhaustion.</p>
    <p>'Then let's go finish it,' she rasped, taking the lead down the western slope.</p>
    <p>Chapter 9 complete. The glass horizon had been crossed. Terminal Zero awaited.</p>
    <div style='margin-top: 2rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;'><h3 style='color: var(--terminal-green); margin-bottom: 0.5rem; font-family: monospace;'>OPERATIONAL ARC COMPLETE</h3><p style='color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem;'>Chapter 9 complete. Proceed to Chapter 10.</p><a href='chapter-10-page-1.html' class='nav-btn' style='background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;'>CHAPTER 10: Terminal Zero (Page 1) →</a></div>
    """)
}

for p_num, (subtitle, body_content) in ch9_contents.items():
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 9: The Glass Horizon - Page {p_num} | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
{site_header}
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 9 • PAGE {p_num} OF 16</span>
        <h1>The Glass Horizon</h1>
        <p class="story-subtitle">{subtitle}</p>
      </div>

      {get_ch9_nav_block(p_num, 16)}

      <div class="story-body">
        {body_content}
      </div>

      <div class="story-nav" style="margin-top: 2rem;">
        <a href="chapter-9-page-{p_num-1}.html" class="nav-btn">← Prev</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-9-page-{p_num+1}.html" class="nav-btn next-btn">Next Page →</a>
      </div>
    </article>
  </main>
</body>
</html>"""
    
    filename = f"chapter-9-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(page_html)
    print(f"Generated heavyweight 16-page build for {filename}")

print("\nAll 16 pages of Chapter 9 successfully generated with uncompromising literary prose and ion-storm drone combat!")
