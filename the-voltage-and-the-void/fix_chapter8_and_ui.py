import os
import re

# We want Chapter 8 to have 16 pages, matching the exact Bombshell Wire layout structure shown in Image 2:
# - Dark CRT background with green side borders
# - Red siren header / "BOMBSHELL WIRE" logo banner at top
# - SECURE DATA NODE subheader
# - Neon blue primary buttons ("Phantom Index", "Next Page")
# - Grid of page number selector tabs (P.1 through P.16)
# - Exact keyword coloring: HAARP = Neon Pink (#ff007f), cyph3r/cipher = Neon Green (#00ff66), DEW = Neon Orange (#ff9900)
# - Phoenix sacrifices himself brutally in Chapter 8 to save Marcus and Elena, while Elena survives Chapter 8 with her leg injury.

MASTER_CSS = """
body {
    background-color: #05080c;
    color: #e6edf3;
    font-family: monospace;
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.8;
    border-left: 3px solid #00ff66;
    border-right: 3px solid #00ff66;
    box-shadow: inset 0 0 20px rgba(0,255,102,0.1);
}
.site-header {
    text-align: center;
    border-bottom: 1px dashed #ff3333;
    padding-bottom: 1rem;
    margin-bottom: 2rem;
}
.site-header h1 {
    font-family: monospace;
    color: #ff3333;
    text-shadow: 0 0 10px rgba(255,51,51,0.7);
    font-size: 1.5rem;
    letter-spacing: 2px;
    margin: 0.5rem 0;
}
.nav-links {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}
.nav-links a {
    color: #00f3ff;
    text-decoration: none;
    text-shadow: 0 0 6px rgba(0,243,255,0.4);
}
.header {
    border-bottom: 1px dashed #00f3ff;
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
    color: #00f3ff;
    text-shadow: 0 0 8px rgba(0,243,255,0.6);
}
.page-tabs-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 1.5rem 0;
}
.page-tab {
    border: 1px solid #00f3ff !important;
    padding: 0.3rem 0.6rem !important;
    color: #00f3ff !important;
    text-decoration: none !important;
    background: rgba(0,243,255,0.05) !important;
    font-family: monospace !important;
    font-size: 0.85rem !important;
    font-weight: bold !important;
    display: inline-block !important;
}
.page-tab.active {
    background: #00f3ff !important;
    color: #05080c !important;
    box-shadow: 0 0 8px rgba(0,243,255,0.8) !important;
}
.page-tab:hover {
    background: rgba(0,243,255,0.2) !important;
    box-shadow: 0 0 10px rgba(0,243,255,0.6) !important;
}
.terminal-nav {
    margin: 2rem 0;
    padding: 1rem 0;
    border-top: 1px dashed #00f3ff;
    border-bottom: 1px dashed #00f3ff;
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
.narrative-content p {
    font-family: monospace;
    font-size: 0.95rem;
    color: #e6edf3;
    margin-bottom: 2rem;
    line-height: 1.8;
    word-wrap: break-word;
}
.terminal-log {
    font-family: monospace;
    color: #00f3ff;
    text-shadow: 0 0 6px rgba(0,243,255,0.4);
    margin: 1.8rem 0;
    line-height: 1.6;
    font-size: 0.88rem;
    word-wrap: break-word;
    font-weight: bold;
}
"""

def make_pink(word):
    return f'<span style="color: #ff007f; text-shadow: 0 0 8px rgba(255,0,127,0.9); font-weight: bold;">{word}</span>'

def make_green(word):
    return f'<span style="color: #00ff66; text-shadow: 0 0 8px rgba(0,255,102,0.9); font-weight: bold;">{word}</span>'

def make_orange(word):
    return f'<span style="color: #ff9900; text-shadow: 0 0 8px rgba(255,153,0,0.9); font-weight: bold;">{word}</span>'

def make_terminal(text):
    return f'<div class="terminal-log">{text}</div>'

def make_paragraph(text):
    text = text.replace("cyph3r", make_green("cyph3r")).replace("Cyph3r", make_green("Cyph3r"))
    text = text.replace("cipher", make_green("cipher")).replace("Cipher", make_green("Cipher"))
    text = text.replace("HAARP", make_pink("HAARP"))
    text = text.replace("DEW", make_orange("DEW")).replace("DEWs", make_orange("DEWs"))
    return f'<p>{text}</p>'

def get_chapter8_content(page):
    c = []
    if page == 1:
        c.append(make_paragraph("The heavy hydraulic blast doors of the Titan II silo slammed shut with a bone-jarring, concussive thud that rattled the fillings in Marcus's teeth. Just outside, an orbital DEW sweep had scorched the valley grass into white ash, leaving the air thick with the suffocating stench of vaporized silica and burning hydrocarbons."))
        c.append(make_paragraph("Phoenix hauled Marcus and Elena inward, his boots skidding across the concrete dust as heavy alarms wailed overhead. He slammed his palm against the manual closure toggle, locking the massive steel pins into their housing just as a searing wall of thermal energy licked against the exterior seals."))
        c.append(make_terminal("[SECTOR LOCK]: TITAN SILO 4 SEALED // EXTERNAL TEMPERATURE: 720°C // INTEGRITY: 89%"))
        c.append(make_paragraph("Elena gasped in ragged agony, collapsing against a metal storage rack as white-hot pain lanced up her injured thigh. The glancing DEW strike from the valley sprint had charred her tactical fatigues and fused the fabric directly into her skin, leaving a raw, weeping burn that bled sluggishly onto the floor."))
        c.append(make_paragraph("Marcus dropped beside her, tearing open an emergency trauma pack with trembling fingers. His hands were slick with cold sweat and soot, tasting copper and metallic bile in the back of his throat as he pressed a sterile compression dressing over her ruined leg."))
    elif page == 2:
        c.append(make_paragraph("Phoenix didn't pause for breath. He shouldered his modified assault rifle and scanned the cavernous missile control room, his eyes reflecting the amber flicker of dying emergency CRTs. \"They know we're inside. The HAARP resonance arrays in the upper peaks are painting our exact electromagnetic signature through three hundred feet of limestone.\""))
        c.append(make_paragraph("A low, rhythmic vibration began to hum through the concrete floor—not seismic, but the unmistakable mechanical trudge of automated killer bots descending the primary access hoist."))
        c.append(make_terminal("[DEFENSE ALERT]: SUBTERRANEAN SENSOR GRID DETECTS MULTIPLE HOSTILE CONTACTS IN SHAFT B."))
        c.append(make_paragraph("Elena gritted her teeth so hard a thin line of red bubbled at the corner of her mouth, pushing Marcus's hands away as she pulled herself up against the console. \"Move... we have to arm the core terminals before they breach the bulkhead. If the cyph3r payload doesn't deploy, the entire grid goes dark permanently.\""))
        c.append(make_paragraph("Marcus looked into her pale, sweat-soaked face, feeling the crushing weight of their bond amidst the terror. Every breath tasted of iron, ozone, and impending catastrophe."))
    elif page == 3:
        c.append(make_paragraph("Phoenix wrenched open an auxiliary floor panel, unspooling a heavy fiber-optic tap and shoving the connector into the primary diagnostic bus. Sparks showered down from an overhead conduit as a stray kinetic missile strike rattled the mountain above, showering them in gritty gray dust."))
        c.append(make_paragraph("“They're dropping smart traps in the ventilation bypass,” Phoenix cursed, his voice raspy and grim. “Proximity-triggered EMP clusters designed to fry our remaining logic boards the second we draw power.”"))
        c.append(make_terminal("[WARNING]: LOCAL ELECTROMAGNETIC ANOMALY DETECTED. SMART TRAP CLUSTER ARMED."))
        c.append(make_paragraph("Elena hobbled forward on her good leg, using a heavy steel pipe as a crutch, her face contorted in agony with every step. “I'll clear the bypass line. Give me the frequency emitter.”"))
        c.append(make_paragraph("“No, Elena, your leg—” Marcus started, but she cut him off with a fierce, unwavering glare that left zero room for argument."))
    elif page == 4:
        c.append(make_paragraph("With agonizing precision, Elena tossed a handheld decoy beacon down the darkened ventilation shaft, drawing a blinding, concussive flash as the smart traps detonated in a chain reaction of blue-white fire."))
        c.append(make_paragraph("The shockwave battered the bulkhead, knocking Marcus off balance and sending a fresh wave of blinding pain through Elena's wounded leg. She slumped against the wall, leaving a jagged smear of blood on the gray concrete."))
        c.append(make_terminal("[EXPLOSION LOG]: SMART TRAP CLUSTER NEUTRALIZED. BYPASS CLEAR."))
        c.append(make_paragraph("“Bypass is clear! Marcus, get the core compiling!” Phoenix roared, laying down suppressive fire toward the main service elevator as the first robotic chassis hauled its heavy steel treads into view."))
        c.append(make_paragraph("Red optical sensors flared in the gloom, accompanied by the high-pitched whining of automated plasma weaponry powering up for execution."))
    elif page == 5:
        c.append(make_paragraph("Marcus slammed his fingers across the mechanical keyboard, feeding the cyph3r compilation script straight into the Titan silo's massive guidance computer. The old military hardware groaned, its vacuum tubes glowing an angry, pulsing crimson as they processed the uncompressed decryption strings."))
        c.append(make_paragraph("Outside the heavy blast door, the relentless scraping of plasma cutters began to chew through the outer steel plate with a deafening, piercing screech."))
        c.append(make_terminal("[COMPILATION]: CYPH3R PROTOCOL INJECTED INTO GUIDANCE BUS [NODE 04]."))
        c.append(make_paragraph("“They're cutting through the main lock!” Phoenix shouted over the din, emptying a full 30-round magazine down the corridor. The tungsten rounds ricocheted off the advancing killer bot's titanium armor with a shower of blinding yellow sparks."))
        c.append(make_paragraph("The air grew thick with the acrid stench of scorched rubber and vaporized solder, making every lungful burn like liquid fire."))
    elif page == 6:
        c.append(make_paragraph("Elena dragged herself to the secondary control panel, plugging her tactical datapad directly into the silo's fire-control circuit. “I'm routing the remaining silo power into the local feedback loop. If we can supercharge the HAARP relay towers overhead, we can fry their orbital uplinks in one shot.”"))
        c.append(make_paragraph("“That'll draw every DEW battery within five hundred miles straight onto our position!” Marcus yelled back, beads of sweat stinging his eyes."))
        c.append(make_terminal("[POWER SURGE]: SUBSTATION 4 DRAWING 400% OVER NOMINAL CAPACITY."))
        c.append(make_paragraph("“It's the only way to stop the global sweep,” Elena replied softly, her hand briefly resting over Marcus's knuckles as a silent reaffirmation of their unbreakable bond."))
        c.append(make_paragraph("Phoenix loaded a fresh drum into his rifle, his expression hardened into stone. “Then let's give them a fireworks show they'll never forget.”"))
    elif page == 7:
        c.append(make_paragraph("The reinforced blast door buckled inward under a concentrated plasma burst, shearing the hydraulic locking pins and sending thick plumes of toxic smoke billowing into the control bunker."))
        c.append(make_paragraph("Two automated killer bots surged through the breach, their multi-barrel rotary cannons spinning up with a terrifying, high-velocity whine."))
        c.append(make_terminal("[COMBAT ENGAGEMENT]: ENEMY UNITS BREACHED INTERIOR PERIMETER."))
        c.append(make_paragraph("Phoenix didn't hesitate. He lunged forward, hurling an active fragmentation grenade directly between the advancing units before diving behind a heavy concrete pillar."))
        c.append(make_paragraph("The resulting explosion obliterated the lead robot in a shattering roar of shrapnel and severed wiring, but the second unit stepped over its smoldering wreckage, its target acquisition laser locked dead on Marcus."))
    elif page == 8:
        c.append(make_paragraph("With a desperate cry, Elena raised her sidearm and fired three armor-piercing rounds directly into the remaining killer bot's optical cluster, blinding its primary targeting suite."))
        c.append(make_paragraph("The machine spun wildly, blind-firing plasma bolts that scored deep, smoking trenches into the steel ceiling and showered them in glowing molten slag."))
        c.append(make_terminal("[TARGET STATUS]: UNIT 02 OPTICAL SENSORS DESTROYED. MANUAL OVERRIDE ENGAGED."))
        c.append(make_paragraph("Marcus slammed his pneumatic crowbar into the machine's exposed cooling vents, wrenching upward until the internal gyroscopes exploded in a geyser of white-hot sparks and black grease."))
        c.append(make_paragraph("The mechanical beast shuddered violently and collapsed into a motionless heap of twisted scrap metal across the blood-stained floor."))
    elif page == 9:
        c.append(make_paragraph("“That bought us maybe two minutes before the next wave clears the elevator shaft,” Phoenix panted, wiping blood and soot from his forehead. He checked his tactical vest—only one magazine left, and the heavy rumble from above was growing louder by the second."))
        c.append(make_paragraph("Marcus watched the progress bar on the main terminal. cyph3r was at 78%, eating through the machine's central neural architecture node by node."))
        c.append(make_terminal("[PROGRESS]: GLOBAL SUBNET ISOLATION AT 78%. TERMINAL LOCK PENDING."))
        c.append(make_paragraph("“The uplink is routing through the satellite array now,” Marcus said, his voice tight with exhausted triumph. “Just hold them off a little longer!”"))
        c.append(make_paragraph("Suddenly, the seismic monitors spiked off the scale as a cluster of supersonic kinetic missiles impacted the terrain directly above the Titan silo."))
    elif page == 10:
        c.append(make_paragraph("The subterranean bunker shuddered as a massive slab of concrete sheared off the ceiling, crashing down onto the secondary terminal and crushing it into powder."))
        c.append(make_paragraph("Elena cried out as a flying shard of plastic struck her shoulder, but she forced herself to stay upright, leaning heavily against Marcus for support."))
        c.append(make_terminal("[STRUCTURAL WARNING]: SILO CEILING INTEGRITY AT 31%. EVACUATION IMPOSSIBLE."))
        c.append(make_paragraph("“The main exit shaft is blocked by the cave-in,” Phoenix said quietly, staring up at the twisted mass of steel and rock sealing their only way back to the surface."))
        c.append(make_paragraph("The grim reality settled over them like a shroud. There was no extraction route. There was only the mission, and the terminal screen ticking toward completion."))
    elif page == 11:
        c.append(make_paragraph("Phoenix stepped toward the blown-out blast door, checking the heavy service hatch that led deeper into the silo's sub-reactor core. His face was etched with the absolute resolve of a man who knew his time had run out."))
        c.append(make_paragraph("“The manual blast valve for the lower floodgates is down the service corridor,” Phoenix said, his voice steady and calm above the wailing sirens. “If I don't seal the lower bulkhead manually, the incoming missile shockwave will cave this entire vault in before the upload finishes.”"))
        c.append(make_paragraph("“Phoenix, no! There's no time to get back!” Marcus yelled, lunging forward to grab his tactical vest, but Phoenix pushed him back with a firm, solemn grip."))
        c.append(make_terminal("[MANUAL OVERRIDE]: FLOODGATE 9 REQUIRES ON-SITE MECHANICAL ENGAGEMENT."))
        c.append(make_paragraph("“Somebody has to turn the wheel, Marcus,” Phoenix said with a faint, grim smile. “Take care of each other. Finish the loop.”"))
    elif page == 12:
        c.append(make_paragraph("Before Marcus or Elena could utter another word, Phoenix spun on his heel and sprinted down the dark service corridor, slamming the heavy titanium hatch shut behind him and throwing the mechanical locking dogs into place."))
        c.append(make_paragraph("“Phoenix!” Elena screamed, beating her fists against the thick steel door in helpless anguish as the heavy locking pins clicked home from the inside."))
        c.append(make_terminal("[SECURITY LOCK]: BULKHEAD 9 SEALED FROM INTERIOR. MANUAL OVERRIDE DISABLED."))
        c.append(make_paragraph("Through the reinforced glass port, they saw Phoenix standing beside the massive brass flood valve, raising his hand in a final, silent salute as the emergency seismic charges began to rumble in the tunnel beyond."))
        c.append(make_paragraph("A profound wave of grief and horrific loss tore through Marcus's chest, leaving him hollowed out and burning with a cold, unforgiving rage."))
    elif page == 13:
        c.append(make_paragraph("A thunderous subterranean explosion echoed through the service corridor as Phoenix manually triggered the secondary floodgates, sacrificing himself in a brutal, crushing collapse to save the control bunker from total destruction."))
        c.append(make_paragraph("The sacrifice held. The bunker stayed upright, its primary terminals flickering back to life as the cyph3r progress bar surged past 92%."))
        c.append(make_terminal("[STATUS]: FLOODGATE SEALED. UPLINK STABLE. 94% COMPLETE."))
        c.append(make_paragraph("Elena wept silently against Marcus's shoulder, her injured leg throbbing with agonizing heat, every fiber of their being aching from the immense physical and emotional trauma of the siege."))
        c.append(make_paragraph("“He saved us,” Marcus whispered, his voice cracking with unshed tears as he stared at the sealed hatch where Phoenix had given his life."))
    elif page == 14:
        c.append(make_paragraph("With trembling fingers, Marcus returned to the primary console, watching the final digits of the decryption sequence cascade down the glowing green screen."))
        c.append(make_paragraph("The HAARP weather control towers across the horizon flickered and died as the virus severed their power substations in a cascading wave of digital feedback."))
        c.append(make_terminal("[EXECUTION]: CYPH3R PROTOCOL PROPAGATED ACROSS 98% OF GLOBAL NETWORKS."))
        c.append(make_paragraph("Outside, the oppressive, humming resonance in the atmosphere abruptly ceased, replaced by an eerie, profound silence that hadn't been felt since the machine war began."))
        c.append(make_paragraph("They had crippled the global machine network, blinding its orbital eyes and shattering its automated defense grids in one monumental, devastating blow."))
    elif page == 15:
        c.append(make_paragraph("Yet victory came coated in the ash of unimaginable loss. Kyle was dead; Phoenix had just been brutally crushed behind the bulkhead; and the physical toll on Elena's body was reaching a terrifying, critical threshold."))
        c.append(make_paragraph("Marcus pulled her close, inspecting the severe burn on her leg, where the tissue damage from the DEW blast was beginning to show signs of virulent, systemic toxicity."))
        c.append(make_terminal("[MEDICAL ALERT]: SYSTEMIC TOXICITY DETECTED. IMMEDIATE SURGICAL INTERVENTION REQUIRED."))
        c.append(make_paragraph("“We need to get to the medical cache in Sector 9,” Marcus said, his voice laced with rising panic as Elena's breathing grew shallower and more labored."))
        c.append(make_paragraph("“There's no time, Marcus,” Elena murmured, her eyes heavy with exhaustion as she looked up at him with heartbreaking devotion. “We keep going... for Phoenix, for all of us.”"))
    elif page == 16:
        c.append(make_paragraph("Marcus helped her settle against the reinforced console, laying out their remaining supplies while the terminal screen blinked a steady, victorious green across the wreckage."))
        c.append(make_paragraph("The Titan silo stood bruised and battered in the deep earth, a lonely monument to the few who dared to stand against an unfeeling mechanized world."))
        c.append(make_terminal("[CHAPTER 8 COMPLETE]: GLOBAL SUBNETWORK DISCONNECTED. PREPARING SECTOR 9 TRANSIT."))
        c.append(make_paragraph("Marcus gripped his sidearm, standing tall amidst the ruins with Phoenix's brutal sacrifice etched into his soul and Elena's life hanging by a fragile thread as they prepared for Chapter 9."))
        c.append(make_paragraph("Chapter 8 closed in the heavy, radioactive silence of the deep earth, leaving Marcus and Elena battered and bleeding, stepping forward into the dark."))
    return "\n".join(c)

def main():
    total_pages = 16
    for page in range(1, total_pages + 1):
        filename = f"chapter-8-page-{page}.html"
        
        # Build page tabs grid (P.1 through P.16)
        tabs_html = []
        for p in range(1, total_pages + 1):
            active_class = " active" if p == page else ""
            tabs_html.append(f'<a href="chapter-8-page-{p}.html" class="page-tab{active_class}">P.{p}</a>')
        tabs_str = "\n".join(tabs_html)

        # Top navigation buttons matching Image 2 style
        left_links = []
        if page > 1:
            left_links.append(f'<a href="chapter-8-page-{page-1}.html" class="terminal-btn">◄ Previous Page</a>')
        else:
            left_links.append(f'<a href="chapter-7-page-16.html" class="terminal-btn">◄ End of Ch 7</a>')
        
        left_links.append(f'<a href="index.html" class="terminal-btn">⚡ Phantom Index</a>')

        right_links = []
        if page < total_pages:
            right_links.append(f'<a href="chapter-8-page-{page+1}.html" class="terminal-btn">Next Page ►</a>')
        else:
            right_links.append(f'<a href="chapter-9-page-1.html" class="terminal-btn">► Next Chapter (Ch 9)</a>')

        nav_left_str = " ".join(left_links)
        nav_right_str = " ".join(right_links)

        nav_block = f"""
    <div class="terminal-nav">
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
            {nav_left_str}
        </div>
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
            {nav_right_str}
        </div>
    </div>
        """

        phantom_banner = '<div class="phantom-index-table" style="text-align: center; margin: 2rem 0; border: 1px solid #00f3ff; padding: 0.8rem; background: rgba(0,243,255,0.03);"><a href="index.html" style="color: #00f3ff; text-decoration: none; font-weight: bold;">[ PHANTOM INDEX // JUMP BACK TO DIRECTORY ]</a></div>' if page == total_pages else ""

        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chapter 8 - Page {page} // The Voltage and the Void</title>
    <style>{MASTER_CSS}</style>
</head>
<body>
    <div class="site-header">
        <div style="font-size: 1.2rem;">🚨</div>
        <h1>BOMBSHELL WIRE</h1>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="index.html">Investigations</a>
            <a href="index.html">Video Drops</a>
        </div>
    </div>

    <div class="header">
        <div style="color: #00f3ff; margin-bottom: 0.3rem;">// SECURE_DATA_NODE //</div>
        <h2>CHAPTER 8: THE TITAN SILO SIEGE</h2>
        <p>Page {page} of {total_pages} // Subterranean Sector 4</p>
    </div>

    <div class="page-tabs-grid">
        {tabs_str}
    </div>

    {nav_block}

    <div class="narrative-content">
        {get_chapter8_content(page)}
    </div>

    {phantom_banner}

    {nav_block}
</body>
</html>
"""

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_html)

    print("SUCCESS: Generated 16 pages for Chapter 8 with Bombshell Wire top header banner, neon blue buttons, page tabs grid, exact keyword colors (HAARP = pink, cyph3r = green, DEW = orange), Phoenix's brutal sacrifice, and Elena's surviving leg injury.")

if __name__ == '__main__':
    main()
