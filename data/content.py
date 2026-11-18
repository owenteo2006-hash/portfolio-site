"""
All site content lives here. Edit this file to update the portfolio.
The templates only loop over these lists, so you never need to touch HTML for a content change.
"""

PROFILE = {
    "name": "Owen Teo",
    "title": "Marine Engineering student, Singapore Polytechnic",
    "tagline": "Robotics · Embedded systems · Electrical",
    "intro": "I build things that sense, move and think, and I'm heading toward a degree in electrical, computer or robotics engineering.",
    # Used for search results and link previews (LinkedIn, WhatsApp). Keep it under about 160 characters.
    "description": "Owen Teo, Marine Engineering student at Singapore Polytechnic, building robots, embedded systems and electrical projects in Singapore.",
    "site_url": "https://portfolio-site-sxr1.onrender.com",
    "location": "Singapore",
    "email": "owenteo2006@gmail.com",
    "linkedin": "https://www.linkedin.com/in/owen-teo-411006371/",
    "github": "#",  # set to "https://github.com/owenteo2006-hash" once your GitHub profile has proper write-ups
    "about": [
        "I'm a final-year Marine Engineering student at Singapore Polytechnic who likes building things that sense, move and think. Most of my free time goes into robots, microcontrollers and Linux, and I'm heading toward a degree in electrical, computer or robotics engineering.",
        "I spent six months as a mechanical intern at Sea Forest, assembling battery charger and UPS cabinets for a naval shipbuilding client. I built two of the cabinets on my own and worked through the fixes from factory acceptance testing.",
        "In 2025 I led our team to Silver in the Future Innovators (Senior) category at the World Robot Olympiad Singapore Nationals, as team leader and lead 3D modeller.",
        "Right now I lead my final-year project team and I'm back for a second try at the GNSS Innovation Quest. My 2025 robot's satellite navigation didn't work in time, so I spent the year getting better at embedded systems.",
        "Tools I use: ESP32 and Arduino (C++), Python, Fusion 360, SolidWorks, AutoCAD, Linux and 3D printing, plus workshop basics from shipyard work.",
    ],
}

# The three cards on the home page.
HIGHLIGHTS = [
    {
        "icon": "⚙",
        "title": "Robotics & embedded",
        "text": "ESP32 builds, GNSS positioning and sensor projects. Silver at WRO Singapore 2025 as team leader and lead 3D modeller.",
    },
    {
        "icon": "🔌",
        "title": "Electrical systems",
        "text": "Six months assembling battery charger and UPS cabinets at Sea Forest, through to factory acceptance testing.",
    },
    {
        "icon": "🛠",
        "title": "Design & fabrication",
        "text": "Fusion 360, SolidWorks, AutoCAD and FreeCAD, FDM 3D printing, and workshop basics from shipyard work.",
    },
]

# Newest and most important first.
# status: "in-progress" | "planned" | "complete"
# link: None, or a URL (for example a GitHub repo or demo video)
PROJECTS = [
    {
        "title": "Engine Room Scout",
        "subtitle": "Final-year project · Group leader, FYP09",
        "period": "Oct 2026 – present",
        "description": "Our main design is a drone that checks whether an engine room is safe to re-enter after a CO2-smothered fire, and runs visual and thermal patrols the rest of the time. I lead the six-person team and I'm modelling the frame in FreeCAD. Design stage.",
        "tags": ["Drone", "Sensor fusion", "Thermal sensing", "FreeCAD", "CDIO"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "GNSS Innovation Quest 2026",
        "subtitle": "Team Ping Me Maybe · Advanced category",
        "period": "Oct 2026 – present",
        "description": "My second entry in the competition run by the Singapore Land Authority and Space Faculty. We're designing a device around SLA's SiReNT RTK network, which gives centimetre-level positioning. System diagram due Nov 2026, final submission Feb 2027.",
        "tags": ["GNSS", "RTK", "SiReNT", "u-blox ZED-F9K"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "ESP32-S3 Signal Explorer",
        "subtitle": "Personal project",
        "period": "Oct 2026 – present",
        "description": "A handheld 2.4 GHz scanner on an ESP32-S3. It lists Wi-Fi and Bluetooth LE devices and draws an energy heatmap of the band with nRF24L01 radios on an OLED display. Receive-only by design. Next: a CC1101 module for sub-GHz bands.",
        "tags": ["ESP32-S3", "C++", "nRF24L01", "Wi-Fi / BLE", "OLED"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "Self-hosted home server",
        "subtitle": "Personal project",
        "period": "Oct 2026 – present",
        "description": "I turned an old laptop into a headless Debian 13 server. It runs Immich in Docker to back up my phone's photos, and I reach it remotely over a VPN. It's how I'm teaching myself Linux administration.",
        "tags": ["Debian", "Docker", "Immich", "Linux"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "Maritime Hackathon 2026: Smart Fleet Selection",
        "subtitle": "Team TRYwin · Category B",
        "period": "Feb 2026",
        "description": "Run by the NUS Centre for Maritime Studies with the Singapore Maritime Foundation and RightShip. Our team of three built a Python and Databricks model that picks the lowest-cost ship fleet to carry Singapore's monthly bunker fuel demand to Australia's west coast, while keeping the average safety score at 3.0 or above.",
        "tags": ["Python", "Databricks", "Optimisation", "Data analysis"],
        "status": "complete",
        "link": None,
    },
    {
        "title": "GNSS Innovation Quest 2025: park-connector cleaning robot",
        "subtitle": "Team leader · Advanced category",
        "period": "2025",
        "description": "Team leader of a four-person team. I did most of the mechanical design, fabrication and system integration: a 3D-printed frame that works with LEGO Technic, an ESP32 controller, GNSS positioning and ultrasonic obstacle detection. GNSS navigation didn't work reliably by the deadline, which pushed me to build my embedded skills for 2026.",
        "tags": ["ESP32", "GNSS", "3D printing", "Fusion 360"],
        "status": "complete",
        "link": None,
    },
]

# Newest first.
EXPERIENCE = [
    {
        "role": "Mechanical Intern",
        "org": "Sea Forest Engineering · posted to the Creation Lab of Sea Forest Power Solutions",
        "period": "Mar – Sep 2026",
        "points": [
            "Assembled battery charger and UPS cabinets for a naval shipbuilding client, and built two of the cabinets on my own (a rectifier cabinet and a battery and UPS cabinet).",
            "Contributed to the second-version charger design after the first version ran into component placement, breaker clearance and fan orientation issues at factory acceptance testing.",
            "Worked through the punch list after the UPS factory acceptance test in Aug 2026.",
            "Aligned a motor shaft for another marine client using shims.",
            "Guided workers on cable trunking and torque marking, and checked their work.",
            "Learned SolidWorks (3D models to 2D drawings) and how to read electrical schematics on the job.",
        ],
    },
    {
        "role": "Team Leader, Data Centre Server Relocation",
        "org": "Contract",
        "period": "Sep – Oct 2024",
        "points": [
            "Moved a cloud provider's server racks from a Digital Realty data centre to an ST Telemedia data centre in Loyang.",
            "Led a small crew to remove, label, package and transport the racks under time pressure.",
            "Kept zero-loss tracking of every unit, and was selected to stay on for the reinstallation at the receiving site.",
        ],
    },
    {
        "role": "Shipyard Operations Intern (observation-based)",
        "org": "Prosper Marine Pte Ltd · subcontractor to Seatrium on the Shell Crux offshore project",
        "period": "Mar – Apr 2024",
        "points": [
            "Observed and assisted with gas cutting, arc welding, fabrication, crane operations and pipe assembly.",
            "Took part in safety inductions and weekly inspections with Shell QA and safety officers.",
            "Saw offshore topside construction up close: deck support frames, and helideck and engine module layout.",
        ],
    },
    {
        "role": "Warehouse & Logistics Assistant",
        "org": "Far East Flora",
        "period": "Dec 2023 – Jan 2024",
        "points": [
            "Managed inventory and material flow for seasonal hamper production.",
            "Picked items for the assembly teams from daily fulfilment lists, and assembled extra shelving for peak volume.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Singapore Polytechnic",
        "qualification": "Diploma in Marine Engineering",
        "period": "2024 – 2027",
        "points": [
            "Final-year project group leader (FYP09).",
            "Coursework in thermodynamics, marine engineering knowledge, naval architecture, electrical systems, electronics and engineering drawing.",
            "Workshop training in welding, gas cutting, lathe and milling.",
        ],
    },
    {
        "school": "Boon Lay Secondary School",
        "qualification": "GCE O-Level, Express",
        "period": "2019 – 2023",
        "points": [
            "Moved up from Normal (Technical) to Normal (Academic) to the Express stream.",
        ],
    },
]

SKILLS = {
    "Electronics & embedded": [
        "ESP32 and Arduino (C++)",
        "Microcontrollers and sensor integration",
        "GNSS and RTK positioning",
    ],
    "Electrical": [
        "Control panel assembly",
        "Reading electrical schematics",
        "Electrical wiring",
        "Factory acceptance testing",
    ],
    "Software & data": [
        "Python",
        "Linux (Debian, Arch)",
        "Docker",
        "Flask (this site)",
        "Databricks",
    ],
    "Design & fabrication": [
        "Fusion 360",
        "SolidWorks",
        "AutoCAD",
        "FreeCAD",
        "3D printing (FDM)",
    ],
    "Workshop": [
        "Arc welding",
        "Oxy-fuel cutting",
        "Lathe and milling",
        "Shaft alignment",
        "Workplace safety",
    ],
    "People": [
        "Team leadership",
        "Project coordination",
        "Technical documentation",
    ],
}

AWARDS = [
    {
        "title": "Silver, Future Innovators (Senior)",
        "org": "World Robot Olympiad Singapore Nationals 2025 · Space Faculty",
        "year": "Sep 2025",
        "detail": "Team leader and lead 3D modeller for team Teamgpt. I designed and 3D-printed the prototype's functional parts, ran the design pipeline and led the final presentation.",
    },
    {
        "title": "2nd Runner-Up",
        "org": "Energy Harvester Challenge",
        "year": "2020",
        "detail": "Designed and built a DIY solar power system to run LED lighting.",
    },
    {
        "title": "Certificate of Academic Achievement, Design & Technology",
        "org": "Boon Lay Secondary School",
        "year": "2020",
        "detail": "Top performer in D&T (Normal Academic), Secondary 2.",
    },
    {
        "title": "Edusave Good Progress Award",
        "org": "Ministry of Education",
        "year": "2021",
        "detail": "For academic improvement and good conduct, Secondary 3.",
    },
]

CERTIFICATIONS = [
    "Apply Workplace Safety and Health in Shipyard (General Trade), DV Training Services (2025)",
    "AI/BI for Data Analysts, Databricks (Jan 2026)",
    "Basic First Aid, Singapore Polytechnic",
]
