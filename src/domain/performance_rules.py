from __future__ import annotations

from typing import Dict, List, Union


RuleValue = Dict[str, Union[str, int, List[str], bool]]


PERFORMANCE_RULES: Dict[str, Dict[str, List[RuleValue]]] = {
    "geographic_patterns": {
        "high_performance": [
            {
                "pattern": "Zürich + Aktion",
                "boost": 59,
                "examples": ["Zürich soll leuchten (225)", "Matterhorn mitten in Zürich (120)"],
            },
            {
                "pattern": "Schweizer + Mission",
                "boost": 46,
                "examples": ["Gemeinsam für das Schweizer Plakat (126)"],
            },
            {
                "pattern": "Flughafen Zürich",
                "boost": 35,
                "examples": [
                    "Premiere am Flughafen Zürich (125)",
                    "MegaPoster am Flughafen Zürich (112)",
                    "Animation am Flughafen Zürich (75)",
                ],
            },
            {
                "pattern": "Basel + Expansion",
                "boost": 30,
                "examples": ["Nach dem Start in Bern folgt nun Basel (144)"],
            },
            {
                "pattern": "Zürich + Kultur",
                "boost": 25,
                "examples": ["Open-Air-Ausstellung am Zürcher Utoquai (136)"],
            },
        ],
        "avoid": [
            {
                "pattern": "Generische Locations",
                "impact": -10,
                "examples": ["Olten werben (34)", "Schaffhausen (66)"],
            }
        ],
    },
    "innovation_language": {
        "triggers": [
            {
                "term": "Premiere",
                "boost": 46,
                "examples": ["Premiere am Flughafen (125)"],
            },
            {
                "term": "Neu steht",
                "boost": 40,
                "examples": ["Neu steht das Matterhorn (120)"],
            },
            {
                "term": "Geschichte/125 Jahre",
                "boost": 35,
                "examples": ["125 Jahre APG|SGA (145)"],
            },
            {
                "term": "Erstmals",
                "boost": 25,
                "examples": ["Korreliert mit Performance"],
            },
            {
                "term": "(Königsklasse|größte|maximale Sichtbarkeit|beeindruckende Grösse)",
                "boost": 20,
                "examples": [
                    "Königsklasse der Aussenwerbung (112)",
                    "grösste Werbemural der Schweiz (97)",
                ],
                "regex": True,
            },
            {
                "term": "Exklusivvertrag",
                "boost": 30,
                "examples": ["Exklusivvertrag mit VBZ TrafficMedia (164)"],
            },
            {
                "term": "(interaktiv|bekletterbar|Live-Erlebnis)",
                "boost": 25,
                "examples": [
                    "bekletterbares Mural (120)",
                    "Live-Erlebnis (120)",
                ],
                "regex": True,
            },
        ],
        "avoid": [
            {
                "term": "Phase",
                "impact": -40,
                "examples": ["Entscheidende Phase (17)"],
            },
            {
                "term": "Call for",
                "impact": -40,
                "examples": ["Call for Entries (22)"],
            },
        ],
    },
    "content_structure": {
        "successful_openings": [
            {
                "pattern": "Neu steht + Location",
                "performance": "Sehr stark",
                "examples": ["Neu steht das Matterhorn mitten in Zürich (120)"],
            },
            {
                "pattern": "Company + inszeniert",
                "performance": "Stark",
                "examples": ["UBS inszeniert (120)"],
            },
            {
                "pattern": "Geographic + soll",
                "performance": "Sehr stark",
                "examples": ["Zürich soll leuchten (225)"],
            },
            {
                "pattern": "(Kontroverse|Streit|Diskussion) + (um|wegen|über)",
                "performance": "Sehr stark",
                "examples": ["Zürich soll leuchten: Nach dem Entscheid... (225)"],
                "regex": True,
            },
            {
                "pattern": "(Natur|Kreativität) + vereint",
                "performance": "Top",
                "examples": ["Natur und Kreativität vereint (206)"],
                "regex": True,
            },
            {
                "pattern": "ikonische .* ist zurück",
                "performance": "Stark",
                "examples": ["Das ikonische Lochdesign ist zurück (186)"],
                "regex": True,
            },
            {
                "pattern": "Markenpräsenz + die bewegt",
                "performance": "Stark",
                "examples": ["Markenpräsenz, die bewegt (144)"],
            },
        ],
        "emotional_triggers": [
            {
                "pattern": "Kreativität vereint",
                "performance": "Top",
                "examples": ["Natur und Kreativität vereint (206)"],
            },
            {
                "pattern": "Tradition + Innovation",
                "performance": "Stark",
                "examples": ["ikonische Lochdesign ist zurück (186)"],
            },
            {
                "pattern": "Mitarbeitende + Fest",
                "performance": "Stark",
                "examples": ["Mitarbeitendenfest (145)"],
            },
            {
                "pattern": "(Community-Gefühl|Gemeinschaft|Wir-Gefühl)",
                "performance": "Stark",
                "examples": [
                    "Mitarbeitendenfest (145)",
                    "Gemeinsam für das Schweizer Plakat (126)",
                ],
                "regex": True,
            },
            {
                "pattern": "(sinnliche Details|kulinarisch|Köstliche)",
                "performance": "Stark",
                "examples": ["Köstliche Wiediker-Würste (129)"],
                "regex": True,
            },
            {
                "pattern": "Welche Stadt ist als Nächstes dran",
                "performance": "Stark",
                "examples": ["Markenpräsenz, die bewegt (144)"],
            },
            {
                "pattern": "(gesellschaftlicher Auftrag|wichtigen Beitrag für Gesellschaft)",
                "performance": "Stark",
                "examples": ["Gemeinsam für das Schweizer Plakat (126)"],
                "regex": True,
            },
        ],
        "anti_patterns": [
            {
                "pattern": "Administrative language",
                "impact": -30,
                "examples": ["Einreichungsphase (22)", "Wettbewerb (17)"],
            },
            {
                "pattern": "Generic product announcements",
                "impact": -15,
                "examples": ["City ePanel (34)", "Sommerkampagne (30)"],
            },
        ],
    },
}


