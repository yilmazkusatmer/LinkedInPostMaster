from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class PostExample:
    text: str
    reactions: int
    analysis: str


def build_post_examples() -> Dict[str, List[PostExample]]:
    """Return curated post examples grouped by performance buckets."""

    high_performers: List[PostExample] = [
        PostExample(
            text=(
                "Zürich soll leuchten: Nach dem Entscheid des Zürcher Gemeinderates für ein Verbot"
                " von Screens und eine drastische Einschränkung der Plakatstellen in der Stadt,"
                " hat Matthias Ackeret eine private Protestaktion mit Unterschriftensammlung"
                " lanciert. Damit warnt er vor dem Verlust der Wirtschaftsfreiheit zugunsten"
                " einer Bevormundungsmentalität. \n\nMehr dazu: https://lnkd.in/dXfbsqnA"
            ),
            reactions=225,
            analysis="Kontroverse + emotionaler Aufhänger + lokaler Bezug + Überraschung",
        ),
        PostExample(
            text=(
                "Natur und Kreativität vereint: Das Gartencenter Meier zeigt, wie Werbung und"
                " Umgebung eine Einheit bilden. Absichtlich überwucherte Plakatstellen dienen"
                " als kreative Bühne für den Herbstschnitt-Service. Ein einzigartiger Out of"
                " Home Einsatz, der Aufmerksamkeit weckt, Botschaften verankert und begeistert!"
            ),
            reactions=206,
            analysis="Kreative Überraschung + Natur-Bezug + unerwartete Wendung",
        ),
        PostExample(
            text=(
                "Das ikonische Lochdesign ist zurück – und rollt ab sofort durch Bern! 🤩 🧀\n\n"
                "Wer sich an die legendären Schweizer Skianzüge der 90er von Vreni Schneider und"
                " ihren Teamkolleg:innen erinnert, weiss: Das Emmentaler-Lochdesign ist Kult."
                " Ein Stück Schweizer Identität, das damals schon auffiel – und jetzt auf den"
                " Tramschienen sein Revival feiert. Seit dem 7. Juli fährt das Emmentaler AOP-Tram"
                " durch die Hauptstadt – mitten in dem Jahr, in dem Bern als «Capital of Cheese»"
                " auch international im Rampenlicht steht: Im November ist die Bundeshauptstadt"
                " Gastgeberin der World Cheese Awards 2025. \n\nDirekt beim Tramdepot in Bern beim"
                " Eigerplatz enthüllten wir das neue Emmentaler AOP-Tram im ikonischen Lochdesign."
                " Urs Schluechter, Direktor von Emmentaler Switzerland, gab Einblick in die Idee"
                " hinter dem Projekt und Martin Spahr, CMO von Switzerland Cheese Marketing, warf"
                " einen Blick voraus auf die World Cheese Awards 2025. Den Soundtrack zur"
                " Tram-Premiere lieferte Musiker und Emmentaler-Ambassador Nickless, der die"
                " Bühne kurzerhand auf die Tramgleise verlegte. Danach blieb uns genügend Zeit zum"
                " Anstossen, Austauschen und Geniessen – mit einem Apéro vom Berner"
                " Käse-Handwerksbetrieb JUMI, der wilden Truppe aus dem Emmental. \n\nHerzlichen"
                " Dank an alle Beteiligten! 💛\nBernhard Huber, BOFF GmbH, Bruno Djoungong,"
                " Chiara Grieder, Daniel Müller, Daniel Pulfer, Désirée Stocker, Jumi Käse & Omoso"
                " Jungrind, Martin S., Nickless, Pixelfarm, Roger Keller, Switzerland Cheese"
                " Marketing AG, Sedrik Nemeth, Suzanne Nievergelt, Urs Schluechter, Cornelia"
                " Brechbühl, Deborah Ackermann, Maria Stalder"
            ),
            reactions=186,
            analysis="Nostalgie + Schweizer Identität + Emojis + Überraschung + Kult-Faktor + Storytelling",
        ),
        PostExample(
            text=(
                "APG|SGA sichert sich Exklusivvertrag mit VBZ TrafficMedia: Ab dem 1. April 2025"
                " übernimmt die APG|SGA für sieben Jahre die alleinige Vermarktung der Werbeflächen"
                " auf den Trams und Bussen der Verkehrsbetriebe Zürich. Werbekunden profitieren"
                " von exklusivem Zugang und maximaler Sichtbarkeit im öffentlichen Verkehr von"
                " Zürich.\n\nMehr erfahren: https://lnkd.in/dmKjypcn"
            ),
            reactions=164,
            analysis="Wichtige Neuigkeit + konkrete Zahlen + lokaler Bezug Zürich",
        ),
        PostExample(
            text=(
                "125 JAHRE APG|SGA – Das Mitarbeitendenfest: Gute Stimmung, kulinarische"
                " Highlights, Livemusik und eine stets gefüllte Tanzfläche. Die APG|SGA blickt auf"
                " einen unvergesslichen Abend zurück. Zahlreiche Mitarbeitende aus der ganzen"
                " Schweiz sind zusammengekommen, um auf 125 Jahre Aussenwerbung anzustossen.\n\n"
                "Auf viele weitere Jahre voller Engagement, Teamgeist und gemeinsamer Erfolge!"
            ),
            reactions=145,
            analysis="Meilenstein + emotionale Momente + Community-Gefühl + Feier-Atmosphäre",
        ),
        PostExample(
            text=(
                "Markenpräsenz, die bewegt: Nach dem Start in Bern folgt nun Basel – Salt Mobile"
                " SA setzt zum zweiten Mal auf eine Tram-Ganzgestaltung und bringt ihre Botschaft"
                " prominent ins Stadtbild. Sichtbarkeit, die täglich tausende Menschen erreicht."
                " Bleibt die Frage: Welche Stadt ist als Nächstes dran?\n\nJetzt mehr über"
                " Werbung im öffentlichen Verkehr erfahren: https://lnkd.in/dfbmnfDH"
            ),
            reactions=144,
            analysis="Bewegung + geografische Expansion + prominente Sichtbarkeit + Neugier",
        ),
        PostExample(
            text=(
                "Open-Air-Ausstellung am Zürcher Utoquai eröffnet: Bis zum 13. Juli 2025 zeigen"
                " 150 sorgfältig ausgewählte historische Plakate die visuelle Geschichte rund um"
                " Stadt und See – ein gemeinsames Projekt des Museum für Gestaltung Zürich und der"
                " APG|SGA."
            ),
            reactions=136,
            analysis="Kultur + Geschichte + Zürich-Bezug + zeitlich begrenzt",
        ),
        PostExample(
            text=(
                "Ein traditioneller Anlass mit festlicher Stimmung: Köstliche Wiediker-Würste,"
                " süsse Berliner und heisser Glühwein machten den Abend im Hinterhof der APG|SGA zu"
                " einem unvergesslichen Auftakt der Out of Home-Saison 2025. Herzlichen Dank an"
                " alle, die dabei waren – bis zum nächsten Hoffäscht!"
            ),
            reactions=129,
            analysis="Tradition + sinnliche Details + Gemeinschaftsgefühl + Atmosphäre",
        ),
        PostExample(
            text=(
                "Gemeinsam für das Schweizer Plakat: Plakate sind ein fester Bestandteil des"
                " öffentlichen Raums und leisten einen wichtigen Beitrag für Gesellschaft,"
                " Wirtschaft und Politik. Die neu lancierte Allianz «Pro Plakat» setzt sich gegen"
                " Werbeverbote in Schweizer Städten ein – und für ein lebendiges Stadtbild.\n\n"
                "Jetzt unterstützen: https://lnkd.in/d89AassB"
            ),
            reactions=126,
            analysis="Gemeinschaftsgefühl + gesellschaftlicher Auftrag + Schweiz-Bezug + CTA",
        ),
        PostExample(
            text=(
                "Premiere am Flughafen Zürich AG: Mit einer Werbebotschaft auf zwei"
                " nebeneinanderliegenden MegaPoster sorgt MINI in Zusammenarbeit mit dentsu für"
                " Aufsehen.\n\nInspiriert? Werben Sie gross – oder sogar doppelt:"
                " https://lnkd.in/dXVqdUbQ"
            ),
            reactions=125,
            analysis="Premiere + Superlativ + direkter CTA + Wortwitz",
        ),
        PostExample(
            text=(
                "Neu steht das Matterhorn mitten in Zürich: UBS inszeniert mit WAND AG und"
                " Kletterfabrik ein eindrucksvolles und bekletterbares Mural. Es begeistert nicht"
                " nur als gemalte Aussenwerbung, sondern auch als Live-Erlebnis: Dank integrierter"
                " Stiegelemente können Passant:innen jeweils am Freitag und Samstag ab 14 Uhr noch"
                " bis Ende August den Gipfel erklimmen. \n\nJetzt grossflächige Werbeflächen"
                " entdecken: https://lnkd.in/dsv_pW5F\n\n\n📸: zvg"
            ),
            reactions=120,
            analysis="Starker Hook + geografische Überraschung + Unternehmen + Innovation",
        ),
        PostExample(
            text=(
                "Die Königsklasse der Aussenwerbung: Mit bis zu 471 m² inszenieren MegaPoster am"
                " Flughafen Zürich AG Marken gross – für maximale Sichtbarkeit bei einem"
                " anspruchsvollen, internationalen Publikum.\n\nJetzt Eindruck machen:"
                " https://lnkd.in/dDq_NpWu"
            ),
            reactions=112,
            analysis="Superlativ + konkrete Zahlen + Prestige-Location + Zielgruppen-Fokus",
        ),
    ]

    medium_performers: List[PostExample] = [
        PostExample(
            text=(
                "APG|SGA stärkt Plakatflächen-Angebot im Kanton Zürich deutlich: Ab 2026"
                " vermarktet die APG|SGA 672 zusätzliche Flächen an zentralen Verkehrslagen im"
                " Kanton Zürich.\n\nZur Medienmitteilung: https://lnkd.in/dZfTz8hP"
            ),
            reactions=98,
            analysis="Fakten + konkrete Zahlen + geografischer Bezug, aber wenig Emotion",
        ),
        PostExample(
            text=(
                "Out of Home trifft Kunst: MINI (BMW Group) und die WAND AG realisieren gemeinsam"
                " das grösste Werbemural der Schweiz. Seit letzter Woche schmückt das"
                " beeindruckende Wandgemälde eine Fassade in der Nähe der Zürcher Hardbrücke.\n\n"
                "Mehr Einblicke: https://lnkd.in/dH8MwAVm\n\ndentsu"
            ),
            reactions=97,
            analysis="Kunst-Bezug + Superlativ + Zürich-Bezug, aber schwacher Hook",
        ),
        PostExample(
            text=(
                "Erste 3D-Umsetzung von einem Autobrand am Flughafen Zürich AG: Mercedes-Benz"
                " Switzerland verwandelt ihren Spot in ein eindrückliches Erlebnis und zieht die"
                " Aufmerksamkeit von einem internationalen Publikum auf sich.\n\nWerben auch Sie"
                " in diesem einzigartigen Umfeld: https://lnkd.in/dQrBcxhm\n\n\nHashtag\n"
                "#airportadvertising \nHashtag\n#mercedesbenzswitzerland \nHashtag\n#apgsga"
            ),
            reactions=91,
            analysis="Innovation + Technologie + internationale Reichweite, aber technisch",
        ),
        PostExample(
            text=(
                "Mit APG|SGA wird kulturelle Vielfalt sichtbar: Mit über 7.4 Millionen Produkten"
                " bietet Digitec Galaxus AG «Fast alles für fast jede*n» und untermauert dieses"
                " Versprechen für einmal sprachlich. Genauer gesagt: mit über 50 Sujets in 42"
                " Sprachen, die hierzulande vertreten sind. Sichtbar an digitalen und analogen"
                " Werbeträgern im ganzen Land.\n\nEntdecken Sie jetzt Ihre Wunschflächen:"
                " https://lnkd.in/d4xBd_zd"
            ),
            reactions=89,
            analysis="Vielfalt + konkrete Zahlen + Slogan, aber wenig Emotion",
        ),
        PostExample(
            text=(
                "Die neue Kampagne «Bin kein Baby» der SWISS RETAIL FEDERATION stellt sich mit"
                " augenzwinkernden Sujets gegen kleinliche Verbote und übergriffige"
                " Einschränkungen. Die Plakate und Spots sind in der ganzen Schweiz zu sehen und"
                " sollen Erwachsene zu mehr gesundem Menschenverstand ermuntern.\n\nMehr erfahren:"
                " www.bin-kein-baby.ch"
            ),
            reactions=78,
            analysis="Kontroverse + Humor + Rebellion, aber zu abstrakt",
        ),
        PostExample(
            text=(
                "Animation, die Massstäbe setzt: ABB bespielt die AdWalks am Flughafen Zürich AG"
                " mit einer eindrucksvollen animierten Kampagne über mehrere Screens hinweg. Eine"
                " aufmerksamkeitsstarke Kampagne in einem hochwertigen Werbeumfeld.\n\nDigitales"
                " Werbeangebot am Flughafen Zürich entdecken: https://lnkd.in/dt9k3AXG"
            ),
            reactions=75,
            analysis="Technologie + Superlativ + Flughafen-Prestige, aber wenig persönlich",
        ),
        PostExample(
            text=(
                "Hinter jeder Plakatkampagne steckt Präzision, Erfahrung und Leidenschaft: Rolf"
                " nimmt uns mit in seinen Alltag als Afficheur und zeigt, wie Aussenwerbung jeden"
                " Tag sichtbar wird – Schritt für Schritt, Plakat für Plakat."
            ),
            reactions=74,
            analysis="Persönliche Geschichte + Behind-the-Scenes, aber zu beruflich",
        ),
        PostExample(
            text=(
                "Lancôme beeindruckt auf eBoards mit spektakulärer 3D-Umsetzung: Maximale"
                " Sichtbarkeit, beeindruckende Grösse und ein Wow-Effekt, der ins Auge sticht.\n\n"
                "Entdecken Sie die beeindruckenden Grossformate, die alle Blicke auf sich ziehen:"
                " https://lnkd.in/gkyC6EJH"
            ),
            reactions=74,
            analysis="Luxus-Marke + Technologie + Wow-Faktor, aber generische Sprache",
        ),
        PostExample(
            text=(
                "Plakatwerbung macht den Unterschied: Der Hof Neufallenbach hatte mit 1000 Gästen"
                " für sein Kräuterfestival gerechnet – am Ende waren es 6000! Der Grund für diesen"
                " überwältigenden Erfolg? Eine gezielte Out of Home-Werbekampagne.\n\nEntdecken Sie"
                " diese und weitere lokale Erfolgsgeschichten: https://lnkd.in/dWbWG-JH"
            ),
            reactions=72,
            analysis="Erfolgsgeschichte + konkrete Zahlen + Überraschung, aber werblich",
        ),
    ]

    low_performers: List[PostExample] = [
        PostExample(
            text=(
                "Airport Premium Network: Ab sofort erreichen Werbetreibende mit nur einer"
                " Buchung jährlich über 24 Millionen Businessreisende an den Flughäfen München,"
                " Wien und Zürich.\n\nJetzt von drei attraktiven Paketen profitieren:"
                " https://lnkd.in/dvsyn789\n\nFlughafen München Flughafen Wien - Vienna"
                " Airport Flughafen Zürich AG"
            ),
            reactions=49,
            analysis="Produktbeschreibung ohne emotionalen Bezug oder Hook",
        ),
        PostExample(
            text=(
                "Insights in eine vielfältige Aussenwerbekampagne: In einem exklusiven Interview"
                " verrät Branko Nastic von Digitec Galaxus AG, wie die Idee zu ihren 50 Sujets in"
                " 42 Sprachen entstanden ist und welche Herausforderungen sie dabei gemeistert"
                " haben.\n\nInspirieren lassen: https://lnkd.in/dUQihk3P"
            ),
            reactions=48,
            analysis="Behind-the-Scenes + Zahlen, aber zu sachlich und wenig fesselnd",
        ),
        PostExample(
            text=(
                "Startschuss für das OOH-Jahr 2026: Neue Standorte, digitale Angebote und"
                " attraktive Specials bringen frischen Schub für starke Kampagnen. Buchungen ab"
                " dem 6. Oktober 2025 möglich – jetzt die Neuigkeiten entdecken:"
                " https://lnkd.in/dMq6-qTT"
            ),
            reactions=44,
            analysis="Administrative Sprache, generische Begriffe, kein emotionaler Hook",
        ),
        PostExample(
            text=(
                "UEFA Women's EURO 2025: Während Europa auf die Schweiz blickt, eröffnen sich"
                " kontaktstarke Möglichkeiten für Werbetreibende: Mit Programmatic DOOH und aymo"
                " Mobile Targeting stechen Sie aus der Masse heraus – punktgenau, relevant und"
                " wirkungsvoll.\n\nMehr erfahren: https://lnkd.in/d-4R-R7M"
            ),
            reactions=44,
            analysis="Großevent + Technologie, aber zu verkaufsorientiert und unpersönlich",
        ),
        PostExample(
            text=(
                "2025 – Das Jahr der Grossanlässe in der Schweiz: Es stehen zahlreiche Events"
                " bevor – perfekt, um Ihre Botschaft mit kreativen und programmatischen"
                " Kampagnen direkt ans lokale, regionale oder nationale Publikum zu bringen. \n\n"
                "Lassen Sie sich inspirieren: https://lnkd.in/dgUVseWb\n\n\nHashtag\n#outofhome"
                " \nHashtag\n#apgsga \nHashtag\n#markenpräsenz"
            ),
            reactions=42,
            analysis="Allgemeine Ankündigung ohne konkrete Details oder emotionalen Bezug",
        ),
        PostExample(
            text=(
                "Pendler:innen ohne Streuverlust erreicht: Mit aymo LiveTarget in Gemeinden und"
                " aymo ReTarget entlang auserwählten Tramlinien spricht Breitband.ch ihre"
                " Zielgruppe punktgenau an.\nZum Case: https://lnkd.in/gV6FejpQ\n\nZudem neu im"
                " Portfolio:\nDas Halfpage Ad sorgt mit Grösse und permanenter Sichtbarkeit für"
                " maximale Aufmerksamkeit.\nJetzt entdecken: https://lnkd.in/g5RmXpyX"
            ),
            reactions=37,
            analysis="Technische Features ohne emotionalen Bezug oder Geschichte",
        ),
        PostExample(
            text=(
                "Werben mitten im Eventgeschehen: Die kühle Jahreszeit steht vor der Tür – und das"
                " Hallenstadion Zürich wird zum Hotspot für Top-Events. Sichern Sie sich jetzt"
                " Ihre Werbepräsenz und erreichen Sie eine vielseitige Zielgruppe in bester"
                " Stimmung! Bei einem Wettbewerb haben Sie die Chance, StarLounge-Tickets für eine"
                " Veranstaltung zu gewinnen.\n\nMehr erfahren: https://lnkd.in/efiHixVg\n\n\n"
                "Hashtag\n#hallenstadionzürich \nHashtag\n#events \nHashtag\n#apgsga"
            ),
            reactions=37,
            analysis="Verkaufsorientiert + generische Sprache + schwacher CTA",
        ),
        PostExample(
            text=(
                "Markenpräsenz auf höchstem Niveau: Mit APG|SGA wird Ihre Kampagne Teil des"
                " alpinen Wintererlebnisses – an Liften, Pisten und Hotspots. Nutzen Sie das"
                " hochwertige Umfeld der Schweizer Alpen für Ihren Markenauftritt.\n\nErreichen Sie"
                " Ihre Zielgruppe in der Saison 2025/26 dort, wo Emotionen entstehen:"
                " https://lnkd.in/dpzy98be"
            ),
            reactions=37,
            analysis="Werbliche Sprache ohne konkrete Geschichte oder emotionalen Hook",
        ),
    ]

    return {
        "high_performers": high_performers,
        "medium_performers": medium_performers,
        "low_performers": low_performers,
    }


POST_EXAMPLES = build_post_examples()

