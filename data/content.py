"""
All site content lives here. Edit this file to update the portfolio.
"""

PROFILE = {
    "name": "Owen Teo",
    "title": "Marine Engineering Student",
    "tagline": "Robotics · Embedded Systems · Automation",
    "location": "Singapore",
    "email": "owenteo2006@gmail.com",
    "linkedin": "https://www.linkedin.com/in/owenteo",
    "github": "#",  # add when repos are public
    "about": [
        "Marine Engineering student at Singapore Polytechnic, building at the intersection of mechanical systems and electronics.",
        "My Final Year Project is a Smart Vessel Health Monitoring System — ESP32-S3 sensor nodes feeding a Flask dashboard on a LattePanda, targeting predictive maintenance and stability monitoring.",
        "I've led teams in competitive robotics (GNSS GIQ) and engineering challenges (Future Innovators Silver 2025), handling full design pipelines from CAD to fabrication to system integration.",
        "Currently developing skills in embedded systems, Python, Linux, and condition monitoring — oriented toward robotics/mechatronics and a future in marine or mechanical engineering.",
    ],
}

PROJECTS = [
    {
        "title": "Smart Vessel Health Monitoring System",
        "subtitle": "Final Year Project — In Progress",
        "description": "Predictive maintenance and stability monitoring for marine vessels. ESP32-S3 sensor nodes collect vibration, temperature, and inclination data. Flask dashboard on LattePanda Iota displays real-time readings with alert thresholds.",
        "tags": ["ESP32-S3", "Flask", "Python", "Sensors", "Embedded Systems"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "GNSS GIQ Robotics Competition",
        "subtitle": "Team Leader, Main 3D Designer — In Progress",
        "description": "Autonomous park-connector cleaning robot. GNSS positioning, ultrasonic obstacle avoidance, ESP32 control. 3D printed chassis designed for LEGO Technic compatibility. Responsible for mechanical design, fabrication, and system integration.",
        "tags": ["ESP32", "GNSS", "3D Printing", "Robotics", "Fusion 360"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "Robot Arm + Vision System",
        "subtitle": "Personal Project — In Progress",
        "description": "Multi-axis robot arm with camera-based vision for object detection and pick-and-place. Integrating servo control, kinematics, and computer vision as a foundation for mechatronics work.",
        "tags": ["Servo Control", "Computer Vision", "Kinematics", "Arduino"],
        "status": "in-progress",
        "link": None,
    },
    {
        "title": "RC Car — FS90R Drive",
        "subtitle": "Weekend Build",
        "description": "IR-controlled RC car using FS90R continuous rotation servos as drive wheels (no H-bridge needed). Arduino Uno + HX1838 IR receiver. 3D printed chassis and wheel hubs.",
        "tags": ["Arduino", "Servo PWM", "IR Remote", "3D Printing"],
        "status": "planned",
        "link": None,
    },
]

EXPERIENCE = [
    {
        "role": "Shipyard Operations Intern",
        "org": "Prosper Marine Pte Ltd (sub to Seatrium / Shell Crux)",
        "period": "Mar – Apr 2024",
        "points": [
            "Observed gas-cutting, arc welding, fabrication, crane ops, and pipe assembly on the Shell Crux offshore topside project.",
            "Participated in safety inductions and weekly inspections with Shell QA/Safety officers.",
            "Exposure to offshore deck support fabrication, helideck layout, and engine module assembly.",
        ],
    },
    {
        "role": "Data Centre Server Relocation — Team Leader",
        "org": "Contract (Digital Realty → STTelemedia)",
        "period": "Sep – Oct 2024",
        "points": [
            "Led crew to remove, label, package, and transport server racks under time-critical conditions.",
            "Zero-loss tracking accuracy across all hardware assets throughout the relocation.",
            "Selected for the reinstallation phase at the receiving site based on demonstrated reliability.",
        ],
    },
    {
        "role": "Warehouse & Logistics Assistant",
        "org": "Far East Flora",
        "period": "Dec 2023 – Jan 2024",
        "points": [
            "Managed inventory and material flow for seasonal hamper production.",
            "Prepared daily fulfilment selections; organised storage and assembled shelving to handle peak volume.",
        ],
    },
]

SKILLS = {
    "Engineering & Workshop": [
        "Arc Welding (basic)",
        "Gas Cutting",
        "Pipe Welding (learning)",
        "Milling & Lathe (beginner)",
        "Workshop Safety",
    ],
    "Software & CAD": [
        "AutoCAD (Proficient)",
        "Fusion 360 (Beginner)",
        "Linux (Beginner)",
        "Microsoft Office (Proficient)",
    ],
    "Programming & Electronics": [
        "Python (Beginner)",
        "Arduino / C++ (Beginner)",
        "ESP32 (In Progress)",
        "Flask (In Progress)",
        "Basic Automation",
    ],
}

AWARDS = [
    {
        "title": "Certificate of Achievement (Silver)",
        "org": "Future Innovators — Senior World Olympiad Singapore Nationals",
        "year": "2025",
        "detail": "Team Leader and Lead 3D Modeller/Printer. Designed functional 3D-printed components and led team coordination.",
    },
    {
        "title": "Certificate of Recognition — 2nd Runner-Up",
        "org": "Energy Harvester Challenge",
        "year": "2020",
        "detail": "Designed and built a DIY solar power system to power LED lighting.",
    },
    {
        "title": "Edusave Good Progress Award",
        "org": "Ministry of Education Singapore",
        "year": "2021",
        "detail": "Recognised for significant academic improvement and good conduct.",
    },
]

CERTIFICATIONS = [
    "Apply Workplace Safety and Health in Shipyard (General Trade) — DV Training / Guardian IC (2025)",
    "Basic First Aid — Singapore Polytechnic",
    "AutoCAD Proficiency — SP Module",
]
