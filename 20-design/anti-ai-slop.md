---
type: canonical
status: canonical
updated: 2026-09-19
source: "[[90-references/inspiration-catalog.md]]"
impacts:
  - design-direction
  - components
  - copy
  - qa
---

# Anti AI Slop

## Verbot ohne konkrete Begründung

- **Redundante Kicker über Überschriften.** Eyebrow, Label oder Kategoriezeile ist ein Befund, wenn sie nur die Überschrift wiederholt, überall mechanisch erscheint oder reine Dekoration ist. Echte Rubrik-, Status-, Datums-, Autor- oder Prozessinformation ist erlaubt. Details im nächsten Abschnitt.
- Blau-Lila-Gradient, Neon-Glow, Sparkles oder generische Aurora-Fläche
- unmotiviertes Stilzitat ohne Marken- oder Inhaltsbezug, gleich ob retro, futuristisch, minimalistisch, editorial oder technisch. Kanonisch in [[20-design/typography-layout-and-spacing.md#Stilzitat und Zeitbezug]]
- ein vollflächiges Retro- oder Epochenzitat, das nur der Unterschiedlichkeit einer Fassung dient; mehrere historische Signale über Schrift, Papierfarbe, Linien, Textur und Seiten-Chrome brauchen einen ausdrücklichen Nutzerwunsch oder tragenden Markenbezug
- unbearbeitete Bestandsbilder mit falschem Winkel, störendem Hintergrund, fremder Farbstimmung oder zu geringer Auflösung; kanonisch in [[20-design/imagery-and-ai-editing.md]]
- sichtbare Kennzeichnung, Wasserzeichen oder Overlay auf einem KI-generierten Bild
- graue Platzhalterflächen, Bildsymbole oder `lorem`-Bilder an Stellen, an denen ein Bild vorgesehen ist
- Textwände, doppelt beantwortete Nutzerfragen und Abschnitte über dem Budget aus [[10-strategy/information-density-and-mobile-clarity.md]]
- häufige Farbpalette ohne projektspezifische Herleitung, siehe [[20-design/color-system.md#Häufige Defaults bewusst entscheiden]]
- Em-Dash in Website-Copy
- Emojis als Icons oder Aufzählungszeichen
- Glas-Header ohne gemessenen Kontrast gegen den tatsächlich darunterliegenden Inhalt oder ohne deckenden Fallback. Eine durchscheinende Kopfzeile ist eine optionale Stilentscheidung, kein Standard; Bedingungen in [[30-frontend/components-and-ui-states.md#Option durchscheinende Kopfzeile]]
- inkonsistente Tiefenlogik und Verlauf oder Schatten ohne erkennbare materielle beziehungsweise hierarchische Rolle. Kanonisch in [[20-design/typography-layout-and-spacing.md#Tiefe und Rahmen]]
- Kopfzeile, deren Inventar nicht aus der Informationsarchitektur folgt, oder die bei realen Texten, Zoom und schmalen Breiten zufällig überläuft, siehe [[30-frontend/components-and-ui-states.md#Kopfzeile und Hauptnavigation]]
- jede Sektion als gleichförmiges abgerundetes Card-Grid
- riesige Icons mit winzigem Text
- eine H1, deren einzig lesbare Fassung durch Übergröße, Maske, `overflow`, Überlagerung oder eine klebende Kopfzeile angeschnitten oder verdeckt wird
- ein Auftakt, dessen Interesse ausschließlich aus großer Schrift, historischer Anmutung oder leerem Weißraum kommen soll und der keinen konkreten Inhaltsanker besitzt
- ein Bild, das zwar vorhanden ist, aber als unverbundener Vollbreitenblock oder beliebig schwebendes Freistellobjekt keine Rolle in Aussage, Raster oder Beweisführung übernimmt
- frei driftende Radius-, Rahmen- oder Containerwerte außerhalb des im Website-Contract gewählten Systems; uneinheitliche Buttonhöhen ohne funktionalen Grund
- aggressive oder überraschende Card-Lifts, Rotation oder Schattensprünge ohne Aufgabe. Interaktionsfeedback folgt der dokumentierten Grammatik aus [[30-frontend/components-and-ui-states.md#Kartenentscheidung]] und erscheint nur auf tatsächlich klickbaren Flächen
- Hover-Lift, Zeigerwechsel oder Schatten auf einer Fläche, die nichts auslöst
- Cursor-Glows, Bounce oder Scroll-Jacking
- generische KI-/SaaS-Copy, Fake-Testimonials, erfundene Logos und Metriken
- verbloses Kurzstatement direkt unter einer Überschrift, etwa `Online in wenigen Minuten`, sowie Ketten freistehender Behauptungen ohne Verb. Kanonisch in [[10-strategy/website-copy.md#Die Statementzeile unter der Überschrift]]
- Meta-Sätze über die eigene Seite, Quellenversicherungen wie `Gerechnet mit unseren echten Preisen`, sichtbare Pflegedaten wie `Stand 8. August 2026` und Negativabgrenzungen wie `Keine Bewertungsdurchschnitte, keine Bestehensquoten`. Kanonisch in [[10-strategy/website-copy.md#Was gestrichen wird]]
- die erfundene Dreierfigur, also Aufzählungen und Satzreihen aus genau drei Aspekten ohne sachlichen Grund. Kanonisch in [[10-strategy/website-copy.md#Die Dreierfigur]]
- Semikolon, Gedankenstrich als Einschub und Doppelpunkt als Spannungszeichen in Website-Copy. Kanonisch in [[10-strategy/website-copy.md#Interpunktion]]
- Pricing, FAQ, Logo-Marquee oder Bento-Grid nur weil Landingpages sie oft besitzen
- Hero nach dem Schema Badge, Überschrift, Unterzeile, zwei Buttons
- jede Sektion in derselben Anordnung aus Titel, Lead und Raster

## Kicker und Überschriften

Ein mechanisch wiederholter Kicker über jeder Überschrift ist ein häufiges Erkennungszeichen generierter Seiten. Das Problem ist Redundanz und Scheinhierarchie, nicht die Position an sich.

**Befunde sind unter anderem:**

- eine Eyebrow-Zeile `PREISE` über der Überschrift „Preise und Gebühren“
- eine gesperrte Versalzeile mit Ziffer wie `01 AUSGANGSLAGE` über der Sektionsüberschrift
- kleine Pillen mit `Neu`, `KI-gestützt`, `Beta` oder einem Kategoriewort, wenn dieser Zustand nicht real oder für die Entscheidung unwichtig ist
- ein farbiger Kurztext mit vorangestelltem Strich als reine Dekoration

**Stattdessen:**

- Die Einordnung gehört in die Überschrift selbst. Aus „Preise“ plus „Preise und Gebühren“ wird eine Überschrift, die tatsächlich etwas aussagt.
- Eine Nummerierung, die wirklich Orientierung stiftet, darf in derselben Zeile, einer Randspalte, einer sichtbaren Kapitelnavigation oder einer bewusst eigenen Zeile stehen.
- Kontext, der über die Überschrift hinausgeht, gehört in den Lead darunter, in eine Bildunterschrift oder in die Navigation.
- Eine reale Metazeile, etwa Datum, Rubrik, Autor, Status, Zielgruppe oder Prozessschritt, ist kein Anti-Slop-Befund, solange sie eine echte, nicht redundante Information trägt.

## Slop-Signaturen

Diese Liste ist der Detailkatalog zu den Verboten oben. Sie sammelt die Einzelmerkmale, an denen erfahrene Gestalter eine generierte Oberfläche innerhalb weniger Sekunden erkennen. Sie wird bei jedem Impeccable-Review und bei jeder Landing Page nach [[20-design/landing-page-craft.md]] durchgegangen.

Jede Zeile ist ein **Befund, kein Verbot**: Wer eines dieser Merkmale bewusst und begründet einsetzt, hält den Grund im Design Contract fest. Wer es ungeprüft übernimmt, hat einen Befund.

### Fläche, Rahmen und Tiefe

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| farbiger Balken an einer Kartenkante, meist oben oder links | eines der zuverlässigsten Einzelmerkmale generierter Oberflächen | Abgrenzung über Rahmen, Flächenwechsel oder Abstand |
| Hairline-Rahmen und weit gestreuter Schatten am selben Element | zwei Abgrenzungsmittel gleichzeitig, keine Materiallogik | eine Entscheidung: entweder Kante oder Tiefe |
| Rundung ab etwa 24 Pixel auf allen Containern | alles wird zur gleichen weichen Blase | Radiusskala je Website nach [[20-design/typography-layout-and-spacing.md#Radiusskala und Rahmenbehandlung]] |
| Glasflächen und Blur ohne Überlagerungsproblem | Effekt ohne Aufgabe | deckende Flächen, Blur nur bei echter Schichtung |
| Karte in Karte | doppelte Tiefe ohne zusätzliche Bedeutung | flach halten, mit Abstand, Typografie und Trennlinien gliedern |
| dekoratives Rasternetz, Streifenverlauf oder Punktetextur im Hintergrund | Struktur wird behauptet statt aus dem Inhalt erzeugt | leere Fläche oder eine Struktur, die etwas darstellt |
| radialer Farbschein oder Spotlight hinter dem Auftakt | simuliertes Licht ohne Lichtquelle | reale Bild- oder Materiallogik |
| farbige Glows und Leuchtschatten auf dunklem Grund | der Standardlook generierter dunkler Oberflächen | monochrome, flache Tiefenstufen |

### Typografie

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| eine einzige Standardfamilie in allen Rollen | keine typografische Entscheidung erkennbar | begründete Familie und Rollen nach [[20-design/typography-layout-and-spacing.md#Schriftwahl]] |
| Stufen mit zu geringem Größenabstand | keine Hierarchie, nur Unschärfe | mindestens Faktor 1,25 zwischen benachbarten Stufen |
| übergroße kursive Serifen-Displayzeile als Auftakt | war eine Geschmacksentscheidung und ist inzwischen der Standardauftakt generierter Startseiten | nur bei tragendem Markenbezug; sonst eine andere Auszeichnungslogik |
| Versal-Kicker mit weiter Sperrung über jeder Überschrift | geliehene Autorität, siehe Abschnitt Kicker und Überschriften | Einordnung in die Überschrift legen |
| kleine Rundquadrat-Kachel mit Icon über der Überschrift | Baustein aus jeder Generatorvorlage | Icon neben den Text stellen oder weglassen |
| winzige Ziffernmarken neben jeder Sektionsüberschrift | Redaktionsanmutung ohne Redaktion | Reihenfolge über Rhythmus und Hierarchie zeigen |
| ganze Absätze in Versalien | Wortbilder verschwinden, Lesbarkeit sinkt | Versalien nur für kurze Beschriftungen |
| stark negatives Tracking auf Fließtext, weites Tracking auf langen Zeilen | Buchstabengruppen zerfallen | Tracking je Stufe kalibrieren |
| Zeilenhöhe unter 1,3 im Fließtext, Zeilen über etwa 80 Zeichen | ermüdet beim Lesen | 1,5 bis 1,7 und 45 bis 75 Zeichen |
| Fließtext unter 14 Pixel, Beschriftungen unter 11 Pixel | auf realen Geräten unlesbar | Mindestgrößen einhalten |
| Blocksatz ohne Silbentrennung | weiße Flüsse im Satz | linksbündig oder Silbentrennung aktivieren |

### Farbe

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| Blau-Violett- oder Violett-Cyan-Verlauf im Auftakt | das bekannteste Einzelmerkmal überhaupt | Farbrollen aus Marke, Material, Ort oder Produkt herleiten |
| Verlaufstext auf Überschriften oder Kennzahlen | Dekoration ohne Bedeutung, oft mit Kontrastverlust | eine gesetzte Textfarbe |
| Creme- oder Beigefläche als Signal für Hochwertigkeit | Reflex, keine Herleitung | Neutralskala aus realem Material ableiten |
| graue Schrift auf farbiger Fläche | wirkt ausgewaschen und fällt unter den Kontrastwert | dunklere Abstufung derselben Farbe oder nahezu Weiß |
| dauerhafter Dunkelmodus mit mittelgrauem Fließtext | Standardanmutung und Kontrastproblem zugleich | bewusste Entscheidung für Grundhelligkeit, Kontrast im Kontext prüfen |

### Aufbau und Raum

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| die feste Kette Hero, drei Karten mit Icon, Logo-Wand, Stimmen, Preise, FAQ | Blockfolge statt Argumentation | Reihenfolge aus realen Nutzerfragen, siehe [[20-design/landing-page-craft.md#Es gibt keinen Standardaufbau, sondern eine Standardaufgabe]] |
| exakt drei gleich große Karten mit Icon, Titel und zwei Zeilen Text | die häufigste generierte Sektion | Anzahl aus der Sache, Form aus der Informationsart |
| Kennzahlenband aus großer Zahl und drei Stützwerten | trägt keine Glaubwürdigkeit, weil die Werte selten belegt sind | belegte Zahl mit Bezugsgröße und Zeitraum oder gar keine |
| identischer Abstand zwischen allem | kein Rhythmus, keine Gruppierung | eng innerhalb der Gruppe, weit zwischen Gruppen |
| Überschrift näher am vorherigen Block als an ihrem eigenen Inhalt | zerstört den Lesefluss | Abstand über der Überschrift größer als darunter |
| Text bündig an der Container- oder Bildschirmkante | wirkt unfertig | Innenabstand mindestens 12 bis 16 Pixel, seitlich mindestens 16 |
| horizontaler Scroller, dessen Karten an der Kante kleben | Rand geht verloren | gleiche Einzüge an beiden Seiten |
| Inhalt läuft aus seinem Container oder wird von einer Überlagerung verdeckt | Layoutfehler, der als Stil durchgeht | Umbruch erlauben, Breiten begrenzen, Überlagerung versetzen |

### Chrome und Beschriftung

Diese Merkmale erscheinen unabhaengig vom Thema und sind deshalb besonders verraeterisch: Sie sind die Ausstattung, die ein Modell ueber jeden Gegenstand legt, statt sie aus ihm herzuleiten.[^frontend]

| Signatur | Warum sie auffaellt | Stattdessen |
|---|---|---|
| Metazeile aus Einzelwerten, mit Mittelpunkt verbunden (`A · B · C`) | Gliederungszeichen ohne Gliederungsaufgabe; erscheint in generierten Seiten als Standardausstattung jeder Karte | die Werte in einen Satz setzen oder als benannte Felder auszeichnen |
| Beschriftung im Muster `WORT — Fragment` mit gesperrtem Gedankenstrich | geliehene Redaktionsanmutung | Rubrik und Aussage trennen oder die Rubrik weglassen |
| angehaengter Pfeil an Link- und Buttontext (`Mehr erfahren →`) | Dekoration, die keine zusaetzliche Information traegt; der Link ist bereits als Link erkennbar | den Text die Handlung benennen lassen |
| getoentes Fast-Schwarz (`#0B0B0B`, `#111`) statt Schwarz oder einer hergeleiteten Dunkelstufe | Kompromisswert ohne Entscheidung | echtes Schwarz oder eine aus dem Material hergeleitete Dunkelstufe |
| Monospace fuer kleine Datenbeschriftungen ohne technischen Bezug | Technik-Anmutung als Dekoration | Mono nur in den im Design Contract benannten Rollen, siehe [[20-design/typography-layout-and-spacing.md#Kalibrierte Type Ramp]] |
| Gewichtskontrast 400 gegen 600 als einzige Hierarchiestufe | zu nah beieinander, um Hierarchie zu tragen; zugleich der haeufigste Default | echten Gewichtsraum nutzen, etwa 300 gegen 800 |
| Schriftfamilie Inter, Roboto, Open Sans, Lato oder der System-Stack ohne Begruendung | die zuverlaessigsten Schrifthinweise auf eine generierte Seite | bewusst gewaehlte Familie, siehe [[30-frontend/web-kit.md#Art-Direction-Presets]] |

### Bekannte Ballungen

Nicht einzelne Merkmale, sondern ganze Erscheinungsbilder, zu denen generierte Oberflaechen derzeit zusammenlaufen. Jedes ist fuer manche Auftraege richtig. Zum Befund wird es, wenn es ohne Bezug zum Gegenstand erscheint.[^frontend]

| Ballung | Erkennungszeichen |
|---|---|
| Creme und Terrakotta | warmer Cremegrund nahe `#F4F1EA`, kontrastreiche Display-Serife, Akzent nahe `#D97757`. Der Akzent ist zugleich die Interaktionsfarbe von Claude selbst und liest sich deshalb als besonders deutlicher Hinweis |
| Neon auf Fast-Schwarz | nahezu schwarzer Grund mit genau einem grellen Gruen oder Zinnoberrot |
| Broadsheet | Haarlinien, Radius null, dichte Zeitungsspalten, Serife ueberall |
| SaaS-Kartenkasten | Inhalt in gleich grosse abgerundete Karten zerlegt, ein Radius fuer alles unabhaengig von der Hierarchie, derselbe weiche graue Schatten unter jeder, Verlaufsflaechen als Dekoration |
| Vorlagen-Chrome | die Merkmale aus dem Abschnitt Chrome und Beschriftung in Kombination |

Der Pruefsatz dazu: **Waere ich bei einem anderen Auftrag derselben Gattung an derselben Stelle gelandet?** Wenn ja, ist es kein Entwurf, sondern ein Default. Wo der Auftrag eine Richtung vorgibt, gilt der Auftrag - auch dann, wenn er eine dieser Ballungen verlangt.

### Bewegung

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| pulsierender Statuspunkt an einem statischen Zustand | vorgetäuschte Lebendigkeit | Bewegung nur bei tatsächlicher Datenänderung |
| blinkender Cursor an nicht editierbarem Text | Terminalzitat ohne Terminal | Cursor nur in echten Eingaben |
| dauerlaufendes Logo- oder Textband | fordert Aufmerksamkeit und verbirgt zugleich Inhalt | lesbare, ruhende Darstellung |
| Bounce- oder Elastic-Kurven auf Oberflächenelementen | wirkt veraltet | weiches Ausklingen; Federphysik nur für tatsächlich physische Bewegung |
| Bild skaliert oder dreht beim Überfahren | wiederkehrende Generatorgeste | Bild ruhig lassen oder eine inhaltliche Reaktion zeigen |
| dieselbe Einblendung auf jedem Element beim Scrollen | Bewegung ohne Aufgabe | Bewegung erklärt Zustand, Weg oder Beziehung |
| Inhalt liegt bis zum Ende der Einblendung auf `opacity: 0` | ausgelieferter Inhalt bleibt unsichtbar, bei Fehlern dauerhaft | Inhalt sichtbar ausliefern, Bewegung als Ergänzung |
| Animation auf `width`, `height`, `padding` oder `margin` | erzeugt Layout-Neuberechnung und ruckelt | `transform` und `opacity` |

### Bild

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| Bestandsbild mit Team im hellen Büro, abstraktes 3D-Objekt, schwebende Formen | austauschbar und erkennbar generisch | reales Motiv des Betriebs nach [[20-design/imagery-and-ai-editing.md]] |
| aus Grundformen zusammengesetzte SVG-Illustration | Platzhalteranmutung | echte Illustration, Foto oder nichts |
| Foto unter einer fast deckenden Farbfläche | das ausgelieferte Bild ist unsichtbar | Bild zeigen oder entfernen |
| leere `src`-Attribute und Platzhalterkästen | ausgelieferter Fehler | reales oder erzeugtes Bild einsetzen |

### Copy

| Signatur | Warum sie auffällt | Stattdessen |
|---|---|---|
| Marketingvokabular wie `streamline`, `empowern`, `world-class`, `nahtlos`, `ganzheitlich` | austauschbar und inhaltsleer | konkretes Verb, konkretes Objekt |
| aphoristische Gegensatzformel am Abschnittsende | erkennbarer Generatorrhythmus | ein normaler Schlusssatz oder keiner |
| dieselbe Beschriftung mehrfach in einem Container | Redundanz | jede Beschriftung genau einmal |
| Em-Dash-Häufung in Fließtext | siehe [[10-strategy/website-copy.md#Interpunktion]] | Komma, Punkt, Klammer |

### Handwerkliche Untergrenze

Diese Punkte sind keine Stilfrage, sondern ein Mangel: unbehandelte Skriptfehler, Kontrast unter WCAG AA, übersprungene Überschriftenebenen, fehlender sichtbarer Fokus, Flächen mit Hover-Reaktion ohne Funktion, Popover und Menüs, die von einem `overflow: hidden` abgeschnitten werden. Sie werden vor jeder gestalterischen Beurteilung behoben.

Die Signaturen in diesem Abschnitt sind aus zwei öffentlich dokumentierten Musterkatalogen zusammengeführt und gegen die Regeln dieses Brains abgeglichen.[^impeccable][^sixteen]

## Erkennungsfragen

- Könnte der Text unverändert zu zehn anderen Produkten passen?
- Steht über einer Überschrift eine Zeile, die nur wiederholt, was die Überschrift sagt?
- Ist eine Sektion vorhanden, weil Nutzer sie brauchen oder weil ein Generator sie erwartet?
- Gibt es mehr visuelle Effekte als belastbare Beweise?
- Wiederholt sich dieselbe Kartenform ohne Informationsgrund?
- Beginnt jede Sektion mit derselben Anordnung?
- Steht ein Satz über die Seite selbst statt über den Betrieb, sein Angebot oder den nächsten Schritt?
- Wie oft wiederholt sich auf der Website eine Dreiergliederung, und ist jede davon sachlich begründet?
- Gibt es auf jeder primären Route mindestens eine Stelle mit zusammenhängenden ganzen Sätzen statt nur Fragmenten?
- Sind Mobile, Loading, Error und Focus sichtbar weniger ausgereift als der Hero?
- Soll die Seite älter wirken, als sie ist?
- Sieht die Bildersammlung aus wie eine Sammlung statt wie eine Serie?
- Bleibt auf einem 375 Pixel breiten Display eine Bildschirmhöhe übrig, die nichts Neues sagt?
- Funktioniert jedes sichtbare Control real?
- Gibt es für jede Rolle aus [[20-design/color-system.md#Tokenvertrag]] einen gesetzten Wert, insbesondere für `border-hover` und `accent-subtle`?
- Verändert sich beim Überfahren einer klickbaren Karte tatsächlich etwas, und zwar Rahmen und Position statt nur Farbe?
- Gehören Radien, Rahmen und Schatten zu einer erkennbaren, dokumentierten Grammatik?
- Ist das Tracking für die konkrete Schrift und Textstufe lesbar kalibriert?
- Würde diese Startseite mit ausgetauschtem Logo für jede beliebige Branche funktionieren?
- Ist die vollständige H1 an jeder Prüfbreite, bei Zoom und nach Aktivierung der klebenden Kopfzeile ohne Anschnitt oder Überlagerung lesbar?
- Beginnt innerhalb der ersten zwei Bildschirmhöhen eine neue Nutzerfrage oder ein konkreter Beweis, statt dass Stilgeste und Kontaktmetadaten weiterlaufen?

## Impeccable KI-Detail-Review

Verbindlich für **jede** gebaute Website, unabhängig davon, wie viele Websites der Auftrag verlangt. Der Review findet nach der Implementierung und vor der Abnahme statt, zusätzlich zu jedem Einsatz von Impeccable während der Gestaltung.

Er setzt den abgeschlossenen [[20-design/visual-iteration-loop.md]] voraus und ersetzt ihn nicht: Der Loop bringt die Fassung auf Qualität, dieser Review prüft sie gegen den Befundkatalog. Ein Review auf einer Fassung, die noch keine drei Durchgänge hinter sich hat, findet Befunde, die der Loop selbst beseitigt hätte, und verbraucht dafür die teurere Prüfrunde.

1. Website vollständig bauen und lokal starten.
2. Impeccable nach [[00-start/04-plugins-and-skills.md]] im Review-Modus auf die reale, laufende Website anwenden, nicht auf Entwürfe oder Beschreibungen.
3. Gezielt nach Details suchen, die nach KI-Generat aussehen: redundante Kicker über Überschriften, immer gleiche Sektionsanordnung, austauschbare Copy, dekorative Karten, Standardfarben ohne Markenbezug, Verläufe ohne Grund, gleichförmige Hover-Effekte, erfundene Belege, Füllsätze, Symmetrie ohne Absicht, generische Icons.
4. Die Prüffragen aus [[10-strategy/website-copy.md#Prüffragen vor der Abnahme]] auf jeden sichtbaren Text der Website anwenden, einschließlich Karten, Formularhilfen und Fußzeile.
5. Jeden Befund entweder korrigieren oder mit inhaltlicher Begründung im Decision Log festhalten. „Gefällt mir so“ ist keine Begründung.
6. Ergebnis mit Datum, geprüfter Website, Befundliste und Umsetzungsstand im Projekt dokumentieren. Ohne diesen Nachweis ist Gate `G1` in [[70-qa/quality-gates.md]] nicht erfüllt.

Bei mehreren Websites wird der Review je Website getrennt geführt. Ein gemeinsamer Sammelbefund genügt nicht, weil die Websites unterschiedliche Art Directions haben.

## Reparatur

1. Eine klare Nutzenbotschaft und ein Markenkonzept festlegen.
2. Redundante Kicker entfernen; echte Metainformation behalten und in eine klare Hierarchie bringen.
3. Unbelegte und redundante Sektionen löschen.
4. Tokens vereinheitlichen.
5. Produkt, Prozess oder echte Arbeit zeigen.
6. Das Motion-Budget neu kalibrieren: zwecklose Bewegung entfernen, tragende Bewegung mit Kapitel, Prozess, räumlicher Beziehung oder Handlung verknüpfen.
7. Copy konkretisieren und alle Links testen.
8. Mobile, Zustände, Accessibility und Performance vor zusätzlichem Polish fertigstellen.

Der zugrunde liegende Bericht beschreibt diese Muster nach einer nicht unabhängig verifizierten Stichprobe von mehr als 500 Seiten. Seine Liste ist Heuristik, kein Qualitätsstandard.[^report]

[^report]: [Aftermark AI: Vibe Coded Website Report](https://docs.google.com/document/d/e/2PACX-1vTnLEdwSF1HPkuwOkuNneXGCaQAw5N2nnRf7cX_B4zuBLf2VTMi4Yh59gqS-eeVqYpa11iFQYmRjVBW/pub)

[^impeccable]: [Impeccable: Slop](https://impeccable.style/slop/). Musterkatalog zu generierter Oberflächengestaltung. Geprüft am 3. September 2026.
[^sixteen]: [Developers Digest: AI Design Slop and how to spot it](https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it). Geprüft am 3. September 2026.
[^frontend]: [Anthropic: frontend-design Skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) und [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills). Die dort benannte Ursache ist Verteilungskonvergenz: Ohne Vorgabe waehlt ein Modell die wahrscheinlichste Loesung, und die ist ueber alle Auftraege dieselbe. Geprueft am 19. September 2026.
