from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class PostExample:
    text: str
    reactions: int
    comments: int
    reposts: int
    analysis: str
    
    @property
    def engagement_score(self) -> int:
        """Calculate engagement score: reactions + (comments * 2) + (reposts * 3)"""
        return self.reactions + (self.comments * 2) + (self.reposts * 3)


def build_post_examples() -> Dict[str, List[PostExample]]:
    """Return curated post examples grouped by performance buckets based on engagement score."""

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
            comments=1,
            reposts=35,
            analysis="Kontroverse + emotionaler Aufhänger + lokaler Bezug + Überraschung + hohe Viral-Rate",
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
            comments=13,
            reposts=16,
            analysis="Nostalgie + Schweizer Identität + Emojis + Kult-Faktor + Storytelling + hohe Interaktion",
        ),
        PostExample(
            text=(
                "Natur und Kreativität vereint: Das Gartencenter Meier zeigt, wie Werbung und"
                " Umgebung eine Einheit bilden. Absichtlich überwucherte Plakatstellen dienen"
                " als kreative Bühne für den Herbstschnitt-Service. Ein einzigartiger Out of"
                " Home Einsatz, der Aufmerksamkeit weckt, Botschaften verankert und begeistert!"
            ),
            reactions=206,
            comments=3,
            reposts=5,
            analysis="Kreative Überraschung + Natur-Bezug + unerwartete Wendung",
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
            comments=4,
            reposts=14,
            analysis="Wichtige Neuigkeit + konkrete Zahlen + lokaler Bezug Zürich + hohe Share-Rate",
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
            comments=5,
            reposts=14,
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
            comments=2,
            reposts=16,
            analysis="Bewegung + geografische Expansion + prominente Sichtbarkeit + Neugier + hohe Reichweite",
        ),
        PostExample(
            text=(
                "Open-Air-Ausstellung am Zürcher Utoquai eröffnet: Bis zum 13. Juli 2025 zeigen"
                " 150 sorgfältig ausgewählte historische Plakate die visuelle Geschichte rund um"
                " Stadt und See – ein gemeinsames Projekt des Museum für Gestaltung Zürich und der"
                " APG|SGA."
            ),
            reactions=136,
            comments=4,
            reposts=12,
            analysis="Kultur + Geschichte + Zürich-Bezug + zeitlich begrenzt",
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
            comments=4,
            reposts=15,
            analysis="Starker Hook + geografische Überraschung + Unternehmen + Innovation",
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
            comments=0,
            reposts=13,
            analysis="Gemeinschaftsgefühl + gesellschaftlicher Auftrag + Schweiz-Bezug + CTA",
        ),
        PostExample(
            text=(
                "Die Königsklasse der Aussenwerbung: Mit bis zu 471 m² inszenieren MegaPoster am"
                " Flughafen Zürich AG Marken gross – für maximale Sichtbarkeit bei einem"
                " anspruchsvollen, internationalen Publikum.\n\nJetzt Eindruck machen:"
                " https://lnkd.in/dDq_NpWu"
            ),
            reactions=112,
            comments=6,
            reposts=11,
            analysis="Superlativ + konkrete Zahlen + Prestige-Location + Zielgruppen-Fokus",
        ),
        PostExample(
            text=(
                "Premiere am Flughafen Zürich AG: Mit einer Werbebotschaft auf zwei"
                " nebeneinanderliegenden MegaPoster sorgt MINI in Zusammenarbeit mit dentsu für"
                " Aufsehen.\n\nInspiriert? Werben Sie gross – oder sogar doppelt:"
                " https://lnkd.in/dXVqdUbQ"
            ),
            reactions=125,
            comments=0,
            reposts=7,
            analysis="Premiere + Superlativ + direkter CTA + Wortwitz",
        ),
        PostExample(
            text=(
                "Ein traditioneller Anlass mit festlicher Stimmung: Köstliche Wiediker-Würste,"
                " süsse Berliner und heisser Glühwein machten den Abend im Hinterhof der APG|SGA zu"
                " einem unvergesslichen Auftakt der Out of Home-Saison 2025. Herzlichen Dank an"
                " alle, die dabei waren – bis zum nächsten Hoffäscht!"
            ),
            reactions=129,
            comments=3,
            reposts=2,
            analysis="Tradition + sinnliche Details + Gemeinschaftsgefühl + Atmosphäre",
        ),
    ]

    medium_performers: List[PostExample] = [
        PostExample(
            text=(
                "Out of Home trifft Kunst: MINI (BMW Group) und die WAND AG realisieren gemeinsam"
                " das grösste Werbemural der Schweiz. Seit letzter Woche schmückt das"
                " beeindruckende Wandgemälde eine Fassade in der Nähe der Zürcher Hardbrücke.\n\n"
                "Mehr Einblicke: https://lnkd.in/dH8MwAVm\n\ndentsu"
            ),
            reactions=97,
            comments=2,
            reposts=10,
            analysis="Kunst-Bezug + Superlativ + Zürich-Bezug, aber schwacher Hook",
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
            comments=1,
            reposts=8,
            analysis="Vielfalt + konkrete Zahlen + Slogan, aber wenig Emotion",
        ),
        PostExample(
            text=(
                "Hinter jeder Plakatkampagne steckt Präzision, Erfahrung und Leidenschaft: Rolf"
                " nimmt uns mit in seinen Alltag als Afficheur und zeigt, wie Aussenwerbung jeden"
                " Tag sichtbar wird – Schritt für Schritt, Plakat für Plakat."
            ),
            reactions=74,
            comments=1,
            reposts=12,
            analysis="Persönliche Geschichte + Behind-the-Scenes, aber zu beruflich",
        ),
        PostExample(
            text=(
                "Plakatwerbung macht den Unterschied: Der Hof Neufallenbach hatte mit 1000 Gästen"
                " für sein Kräuterfestival gerechnet – am Ende waren es 6000! Der Grund für diesen"
                " überwältigenden Erfolg? Eine gezielte Out of Home-Werbekampagne.\n\nEntdecken Sie"
                " diese und weitere lokale Erfolgsgeschichten: https://lnkd.in/dWbWG-JH"
            ),
            reactions=72,
            comments=5,
            reposts=10,
            analysis="Erfolgsgeschichte + konkrete Zahlen + Überraschung, aber werblich",
        ),
        PostExample(
            text=(
                "Hochkarätig besetztes Podium am WOOHW!-Event: Nach den inspirierenden Keynotes"
                " von Ana Campos, Vorstandsmitglied Meta EMEA, und Marius Smytzek, CEO Ströer SE &"
                " Co. KGaA, diskutierten sie gemeinsam mit weiteren Expert:innen über die Zukunft"
                " digitaler Out of Home-Werbung und deren Potenzial, Marken emotional zu verbinden"
                " und nachhaltig sichtbar zu machen."
            ),
            reactions=87,
            comments=0,
            reposts=7,
            analysis="Expertenwissen + Event-Atmosphäre, aber zu formal",
        ),
        PostExample(
            text=(
                "Animation, die Massstäbe setzt: ABB bespielt die AdWalks am Flughafen Zürich AG"
                " mit einer eindrucksvollen animierten Kampagne über mehrere Screens hinweg. Eine"
                " aufmerksamkeitsstarke Kampagne in einem hochwertigen Werbeumfeld.\n\nDigitales"
                " Werbeangebot am Flughafen Zürich entdecken: https://lnkd.in/dt9k3AXG"
            ),
            reactions=75,
            comments=4,
            reposts=8,
            analysis="Technologie + Superlativ + Flughafen-Prestige, aber wenig persönlich",
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
            comments=1,
            reposts=3,
            analysis="Innovation + Technologie + internationale Reichweite, aber technisch",
        ),
        PostExample(
            text=(
                "Lancôme beeindruckt auf eBoards mit spektakulärer 3D-Umsetzung: Maximale"
                " Sichtbarkeit, beeindruckende Grösse und ein Wow-Effekt, der ins Auge sticht.\n\n"
                "Entdecken Sie die beeindruckenden Grossformate, die alle Blicke auf sich ziehen:"
                " https://lnkd.in/gkyC6EJH"
            ),
            reactions=74,
            comments=1,
            reposts=8,
            analysis="Luxus-Marke + Technologie + Wow-Faktor, aber generische Sprache",
        ),
        PostExample(
            text=(
                "Am Puls der Stadt zur besten Zeit: Zalando zeigt, wie clevere Platzierung die"
                " perfekte Zielgruppe erreicht – genau dann, wenn sie am aufmerksamsten ist."
                " Digital City Lights schaffen maximale Sichtbarkeit und Flexibilität für urbane"
                " Kampagnen.\n\nJetzt entdecken: https://lnkd.in/dHYNiNAC"
            ),
            reactions=71,
            comments=4,
            reposts=7,
            analysis="Timing + Zielgruppen-Fokus + urbaner Kontext, aber zu werblich",
        ),
    ]

    low_performers: List[PostExample] = [
        PostExample(
            text=(
                "Glückwunsch zum fantastischen 3. Platz! 🥉🎉\n\nDie APG|SGA AG ist stolz auf das"
                " erfolgreiche Abschneiden des Landschaftsprojekts «eBoards – Bildschirme erobern"
                " Schweizer Bahnhöfe» beim SBB Green Class Award.\n\nUnser Ziel: Ein"
                " verantwortungsvoller Umgang mit Energie und Ressourcen durch nachhaltige,"
                " umweltfreundliche Massnahmen in der Aussenwerbung."
            ),
            reactions=33,
            comments=0,
            reposts=0,
            analysis="Erfolg erwähnt, aber zu corporate und wenig emotional",
        ),
        PostExample(
            text=(
                "Natur, Nahrung und Nachhaltigkeit: Die in Zusammenarbeit mit Planted Foods AG"
                " entstande Kampagne von WIRZ Group setzt Geschmack und Umweltbewusstsein gekonnt"
                " in Szene. Sichtbar auf digitalen Screens in urbanen Zentren."
            ),
            reactions=28,
            comments=0,
            reposts=1,
            analysis="Nachhaltigkeitsthema, aber zu allgemein und ohne Hook",
        ),
        PostExample(
            text=(
                "Call for Entries: Reichen Sie Ihre (D)OOH-Kampagne bis zum 31. März 2025 beim"
                " renommierten ADC Switzerland ein und sichern Sie sich die Chance auf eine"
                " Auszeichnung in der Kategorie Out of Home.\n\nJetzt einreichen:"
                " https://lnkd.in/dDRZqx3p"
            ),
            reactions=22,
            comments=0,
            reposts=3,
            analysis="CTA vorhanden, aber rein administrativ ohne emotionale Ansprache",
        ),
        PostExample(
            text=(
                "StarLounge-Plätze im Hallenstadion Zürich zu gewinnen: Auch in diesem Jahr bietet"
                " die APG|SGA exklusive Werbemöglichkeiten am Hallenstadion Zürich. Nutzen Sie die"
                " Chance, Ihre Marke in einem hochkarätigen Umfeld zu präsentieren – und nehmen Sie"
                " an unserem Wettbewerb teil!\n\nMehr erfahren: https://lnkd.in/efiHixVg"
            ),
            reactions=24,
            comments=0,
            reposts=2,
            analysis="Gewinnspiel erwähnt, aber verkaufsorientiert und wenig ansprechend",
        ),
        PostExample(
            text=(
                "✨ ePoster Gallery feiert die Jubiläumsausgabe \n\n🔸 125 Jahre APG|SGA finden"
                " Raum auf den digitalen Screens der ePoster Gallery. \n🔸 Entdecken Sie die"
                " Highlights an den Standorten Basel SBB, Bern und Zürich HB. \n🔸 Zu sehen vom 1."
                " bis 28. Februar 2025.\n\nErfahren Sie mehr: https://lnkd.in/dtDRb5pq"
            ),
            reactions=20,
            comments=0,
            reposts=1,
            analysis="Jubiläum erwähnt, aber zu listenorientiert und wenig fesselnd",
        ),
        PostExample(
            text=(
                "Starke Kampagnen brauchen starke Präsenz. Wir freuen uns, dass MANOR unsere"
                " Werbeflächen nutzt, um ihre neue «Looks That Last»-Kampagne ins Rampenlicht zu"
                " rücken. Sichtbar an verschiedenen Standorten in der ganzen Schweiz.\n\nMehr zu"
                " unseren Angeboten: https://lnkd.in/dkUeNdGa"
            ),
            reactions=19,
            comments=0,
            reposts=1,
            analysis="Kampagnenerwähnung, aber zu werblich und ohne Storytelling",
        ),
        PostExample(
            text=(
                "ADC Switzerland Young Creatives Award 2025 – Kreativer Nachwuchs gesucht!\n\n"
                "Junge Talente bis 30 Jahre haben die Chance, ihre innovativen Ideen einzureichen"
                " und in der Kreativbranche Fuss zu fassen. Einsendeschluss: 31. März 2025.\n\n"
                "Jetzt teilnehmen: https://lnkd.in/dPdDCb5d\n\nADC Switzerland"
            ),
            reactions=17,
            comments=0,
            reposts=1,
            analysis="Award-Ausschreibung, aber rein informativ ohne emotionalen Bezug",
        ),
        PostExample(
            text=(
                "Herzlichen Glückwunsch an die APG|SGA AG zum Erhalt des Fair-ON-Pay-Zertifikats!"
                " Die Auszeichnung würdigt das Engagement für faire und transparente"
                " Lohnstrukturen – ein wichtiger Schritt zu mehr Gleichstellung und sozialer"
                " Gerechtigkeit.\n\nMehr dazu: https://lnkd.in/dYpT9qgn"
            ),
            reactions=6,
            comments=0,
            reposts=2,
            analysis="Wichtiges Thema, aber zu formal und ohne persönlichen Touch",
        ),
    ]

    return {
        "high_performers": high_performers,
        "medium_performers": medium_performers,
        "low_performers": low_performers,
    }


POST_EXAMPLES = build_post_examples()