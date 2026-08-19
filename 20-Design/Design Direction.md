---
type: canonical
status: canonical
updated: 2026-08-19
depends_on:
  - "[[10-Strategy/Discovery and Scope]]"
impacts:
  - "[[20-Design/Color System]]"
  - "[[20-Design/Typography Layout and Spacing]]"
  - "[[20-Design/Motion and Interaction]]"
---

# Design Direction

## Direction Brief

Vor UI-Code **für jede gebaute Website getrennt** festlegen:

- drei Markenattribute und drei Anti-Attribute
- Zielgefühl in einem Satz
- primäre visuelle Metapher
- gewählter Leitbenchmark aus [[20-Design/Interface Benchmarks]] samt übernommenen und ausdrücklich nicht übernommenen Elementen
- vollständiger Tokenvertrag nach [[20-Design/Color System#Tokenvertrag]] mit gesetztem Wert je Pflichtrolle für Light und Dark
- gewählte Radiusskala, Rahmenbehandlung, Flächenlogik und Tiefe; innerhalb der Website konsistent, aber nicht aus einer anderen Fassung übernommen
- Bewegungstokens und eine eigene Bewegungsgrammatik; kalibrierte Beispiele in [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] sind Optionen, keine Defaults
- Primär- und gegebenenfalls Zweitschrift samt Rollen, Lesbarkeits-, Lizenz- und Zeitbezugsentscheidung nach [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]]
- Bildplan nach [[20-Design/Imagery and AI Editing]]: Rolle je Bild, Bearbeitungsbedarf, Freistellungen, geplante `ai-placeholder`-Bilder
- Informations- und Textbudget je Route nach [[10-Strategy/Information Density and Mobile Clarity]]
- primäre Beweisform der Landing Page; ein interaktives Kernmodul nach [[20-Design/Motion and Interaction#Interaktives Kernmodul]] nur wenn es inhaltlich trägt
- Referenzen mit Rolle, übertragbarem Prinzip und konkreter Einsatz-/Adaptionsentscheidung
- Grad an Dichte, Ausdruck, Motion und Bilddominanz
- Entscheidung für ein reales Kernartefakt, direkt übernommenes oder kreativ adaptiertes Leitmedium samt statischer Alternative
- die im Auftrag verlangte Anzahl vollständig gebauter Websites nach [[00-Start/05 Web Product Workflow#Anzahl der Websites]]; bei mehreren jeweils eigene Leitidee, Komposition, Unterseiten-Dramaturgie und Motion-Choreografie bei identischen Fakten und Funktionsanforderungen, belegt durch die Unterscheidungsmatrix aus dem Abschnitt Stilabstand bei mehreren Websites
- Copy-Entscheidung nach [[10-Strategy/Website Copy]]: Anrede, Tonfall und die Stellen, an denen zusammenhängende ganze Sätze stehen
- Kompositionsentscheidung für den Auftakt und für jede Sektionsart, ausdrücklich abweichend vom Standardmuster; siehe Abschnitt Komposition und Überschriften
- Platzierung des Firmenlogos nach dem Abschnitt Logo des Betriebs
- Kopfzeileninventar, Anordnung, Höhe, Navigationsbeschriftung und Mobile-Übergang sowie Fußbereichsstruktur und sonstiges Seiten-Chrome nach [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]]
- notwendige Vertrauenssignale und Route-zu-Route-Erzählung
- Accessibility- und Performancegrenzen
- verlinkte Entscheidungsmatrix aus [[90-References/Reference Research Workflow]]
- UI UX Pro Max Query, Ergebnisdatum, gewählte Regeln und begründete Abweichungen gemäß [[00-Start/04 Plugins and Skills]]
- Einsatz oder begründeter Verzicht auf [[90-References/pen.dev Workflow|pen.dev]] samt Artefaktpfad
- Motion-Budget `none | low | medium | high`; Inventory für die tatsächlich eingesetzten relevanten Bewegungen und Reduced-Motion-Variante

## Stilachsen

Entscheide bewusst je Achse: ruhig oder expressiv, editorial oder produktnah, warm oder technisch, dicht oder großzügig, flach oder räumlich, statisch oder immersiv. Nicht alle Achsen maximal setzen.

## Premium-Heuristik

- Ein starkes Konzept wiederholen und variieren.
- Produkt oder Arbeit zeigen, statt Features nur zu behaupten.
- Asymmetrie nur mit klarer Ausrichtung und Balance.
- Weißraum als Hierarchie, nicht als leerer Luxus.
- Mikrodetails aus Tokens ableiten.
- Novelty Budget: maximal ein bis zwei auffällige Mechaniken pro View; Rest ruhig.

## Medien und mehrere Websites

Medien sind kein nachträglicher Schmuck. Wenn Produkt, Ort, Ergebnis oder Prozess visuell belegt werden können, bildet ein bereitgestelltes, gefundenes, direkt übernommenes oder kreativ adaptiertes Bild, Video, Interface oder Artefakt die visuelle Achse. Für bewegte oder schwere Medien werden Poster, Inhaltsalternative, Ladezustand und Mobile-/Low-Power-Variante im Design Contract bestimmt. Quelle und Einsatz werden nach dem Build in [[50-Legal/Assets Copyright and Licenses]] dokumentiert. Diese Dokumentation darf nie den Einsatz, ein Ersatzmedium oder eine getrennte Website-Fassung auslösen.

Verlangt der Auftrag mehrere Websites, müssen sie mehr sein als andere Farben oder Buttonformen. Jede wählt eine eigene Leitmetapher, Auftaktkomposition, Unterseiten-Dramaturgie, Bewegungsrolle und sichtbare Interface-Grammatik. Jede wird als vollständige Website anhand derselben Inhalte, Nutzerflüsse, Accessibility-, Performance- und SEO-Kriterien umgesetzt, nicht gegeneinander zur Auswahl gestellt.

## Abstand zu Vorgängerfassungen

Existieren frühere Projekte oder Durchläufe desselben Betriebs, entsteht vor dem Design ein Übernahmeregister im `PROJECT.md`:

| Bewusst übernehmen | Bewusst neu entscheiden |
|---|---|
| verifizierte Fakten, gemeinsame Inhaltsquelle, freigegebene Assets, funktionierende Build- und Deployment-Infrastruktur | Art Direction, Leitmotiv, Fassungsname, Signalfarbe, Typografie, Kopf- und Fußbereich, Seiten-Chrome, Komponentenrepertoire, primäre Beweisform und Motion-Grammatik |

Leitmotiv, Fassungsname, Signalfarbe und primäre Beweisform dürfen sich wiederholen, wenn der jeweilige Design Contract eine konkrete, sachliche Begründung dokumentiert. Gleicher Betrieb, gleicher Builder oder funktionierende Vorgängerversion sind allein noch keine Begründung. Gemeinsame Klassen, Komponenten oder Tokens werden übernommen, wenn sie Infrastruktur statt Art Direction verkörpern; der Grenzfall wird im Übernahmeregister benannt.

## Stilabstand bei mehreren Websites

Kanonische Regel für den sichtbaren Unterschied zwischen mehreren gebauten Websites desselben Auftrags. Zwei Websites, die sich beim Überfliegen für dasselbe Angebot halten lassen, verfehlen den Auftrag, auch wenn beide für sich gut sind.

Vor der ersten Zeile UI-Code entsteht in `PROJECT.md` eine Unterscheidungsmatrix mit einer Spalte je Website. Die Matrix erzwingt nicht auf jeder Zeile künstlichen Unterschied. Sie belegt, dass jede Website eine eigenständige, in sich zusammenhängende Richtung besitzt. Mindestens fünf für den Auftrag wirksame Achsen unterscheiden sich deutlich; auf anderen Achsen darf dieselbe sachlich beste Lösung wiederkehren. Bloße Synonyme oder dieselbe Struktur mit anderer Farbe bilden noch keine eigene Richtung.

| Vergleichsachse | Was auf Unterschied oder sachlich gleiche Lösung geprüft wird |
|---|---|
| Grundhelligkeit und Farbwelt | Flächengewicht, Kontrastverteilung und Signalfarbe mit eigener Herleitung |
| Primärschrift | andere Familie oder grundlegend andere typografische Systemlogik, nicht nur anderes Gewicht |
| Zweitschrift und Rollen | andere Familie **und** andere begründete Rollen oder bewusster Verzicht; Anschriften, Fließtext und Sektionstitel sind keine sachlichen Mono-Rollen |
| Auftaktkomposition | Ort, Maßstab und Rolle von Leitmedium, Überschrift und primärer Aktion |
| Raster- und Flächenlogik | Spalten, Ausrichtung, Randbehandlung, Containerprinzip und Flächenwechsel |
| Kopfzeileninventar und -anordnung | welche Elemente vorkommen, ihre Reihenfolge, Positionierung und der Mobile-Übergang |
| Navigationsbeschriftung | unterschiedliche, dennoch eindeutige Begriffe bei identischer Sitemap |
| Fußbereichsstruktur | Informationsgruppen, Reihenfolge, Dichte und Abschlussgeste |
| Seitenmöblierung | Fortschrittsanzeige, Themenumschalter, Sprungmarken, Breadcrumbs, Floating Actions und sonstiges Chrome: andere Auswahl und Platzierung |
| Komponentenrepertoire | derselbe Inhalt erscheint mit anderer Grundform, etwa Karte gegen Zeile gegen Tabelle gegen Liste, nicht nur mit anderer Kartenfarbe |
| Leitbewegung | prägende Bewegungsgrammatik, etwa Scrollsequenz gegen ortsfeste Bühne gegen Maskenwechsel |
| Sektionsreihenfolge und Dramaturgie | andere Reihenfolge der Nutzerfragen aus [[10-Strategy/Information Density and Mobile Clarity#Eine Frage pro Abschnitt]] |
| primäre Beweisform | etwa Leitbild, Case, Demo, Rechner, Prozess, Team, Produktansicht oder redaktionelle Tiefe |
| Tonfall der Copy | Anrede, Satzlänge und Nähe unterscheiden sich, die Fakten nicht |

Zusätzlich wird je Website der Vergleich mit älteren Fassungen nach [[#Abstand zu Vorgängerfassungen]] dokumentiert. `prototype` nach [[00-Start/04 Plugins and Skills#Prototype]] kann unklare Einzelachsen sichtbar machen, wird aber nur auf Bauteile angewandt, nie auf ganze Websites.

Fakten, Preise, Zeiten, Funktionen, Unterseiten, Accessibility, Sicherheit und SEO bleiben identisch nach [[00-Start/05 Web Product Workflow#Was unabhängig von der Anzahl gilt]]. Die H0-Handwerksuntergrenze aus [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]] gilt für alle. B5 oder ein anderes Stilprofil wird dagegen je Website bewusst gewählt und darf die Fassungen nicht wieder auf dieselbe Grammatik ziehen.

## Komposition und Überschriften

Die Anordnung ist eine Gestaltungsentscheidung, keine Voreinstellung. Wer jede Sektion mit Titel, Lead und Raster beginnt, erzeugt genau die Gleichförmigkeit, die generierte Seiten kennzeichnet.

- Redundante Kicker vermeiden. Echte Rubrik-, Status-, Datums- oder Prozessinformation darf nach [[20-Design/Anti AI Slop#Kicker und Überschriften]] als eigene Hierarchiestufe erscheinen.
- Für jede Sektionsart eine eigene Anordnung wählen. Mögliche Achsen: Überschrift links neben dem Inhalt statt darüber, Überschrift über zwei Spalten gebrochen, Überschrift als Bildunterschrift, Überschrift im Raster versetzt, Text in einer schmalen Randspalte, Zahl und Wort in derselben Zeile, Überschrift, die den Inhalt umfließt.
- Überschriften dürfen typografisch groß, gebrochen, überlappend, angeschnitten oder mit einem Medium verschränkt gesetzt werden, solange Lesbarkeit, Fokusreihenfolge und Reflow stimmen.
- Der Auftakt wird aus Inhalt, Leitmetapher, Beweis und nächster Handlung entwickelt. Auch ein mittiger Titel mit Unterzeile und Aktionen kann richtig sein, wenn genau diese Ruhe und Symmetrie zum Auftrag passt; er darf nicht bloß ungeprüfter Default sein.
- Rhythmus entsteht über Maßstabssprünge, Weißraumwechsel und wechselnde Flächenhelligkeit, nicht über immer neue Kartenformen.
- Jede Abweichung von der Leserichtung braucht eine klare Ausrichtungsachse. Asymmetrie ohne Achse ist Unordnung.

## Landing Page

Für die Startseite beziehungsweise Landing Page gilt ein höherer Anspruch als für Unterseiten. Sie darf und soll auffällig sein.

- **Extravagant erlaubt, beliebig nicht.** Große Typografie, ungewöhnliche Raster, randlose Medien, überlappende Ebenen, ausgeprägte Scroll-Choreografie und ein starkes Farbstatement sind ausdrücklich erwünscht, wenn sie aus der Leitmetapher folgen.
- **Professionell ist zweckpassend.** Klare Hierarchie, präzise Abstände und ein kohärentes Farb- und Flächensystem. Auch warme, helle, dunkle, zurückhaltende oder expressive Richtungen sind möglich, wenn sie aus Marke, Inhalt und Zielgruppe folgen; siehe [[20-Design/Color System#Häufige Defaults bewusst entscheiden]].
- **Freundlich statt kühl.** Ansprache, Farbe und Bildauswahl dürfen Wärme und Freude transportieren. Das entsteht über echte Menschen, echte Arbeit, Farbkontrast und Rhythmus, nicht über Emojis, Sparkles oder Ausrufezeichen.
- **Übersichtlich bleiben.** Auch eine expressive Startseite beantwortet in den ersten zwei Bildschirmhöhen: Wer ist das, was bekomme ich, was ist der nächste Schritt. Die Informationsmenge folgt [[10-Strategy/Information Density and Mobile Clarity]] und wird am 375-Pixel-Viewport entschieden.
- **Beweis vor Pflichtinteraktion.** Interaktion wird eingesetzt, wenn sie etwas Reales zeigt oder eine Aufgabe löst. Statisches Leitbild, Team, Case, Arbeitsprobe oder klare Erklärung sind gleichwertige Beweisformen.
- **Ein echtes Leitbild.** Der Auftakt trägt ein großes, bearbeitetes oder erzeugtes Bild des tatsächlichen Gegenstands nach [[20-Design/Imagery and AI Editing]]. Findet sich kein reales Bild, wird ein KI-Bild eingesetzt und im Projekt als `ai-placeholder` geführt, ohne sichtbare Kennzeichnung auf der Website.
- Das Novelty Budget gilt weiterhin: höchstens ein bis zwei auffällige Mechaniken pro Bildschirmausschnitt.
- Unterseiten übernehmen dasselbe Designsystem, treten aber ruhiger auf. Der Ausdruck liegt auf der Landing Page, die Verlässlichkeit auf den Unterseiten.

## Logo des Betriebs

Wird im Auftrag oder in der Bestandsaufnahme nach [[10-Strategy/Existing Website Rebuild]] ein Logo des Betriebs gefunden, **wird es verwendet.** Diese Entscheidung liegt nicht bei der KI.

- Mindestens ein sichtbarer Einsatz je gebauter Website, bevorzugt auf der Startseite beziehungsweise Landing Page.
- Der Kopfbereich ist ein möglicher, aber kein zwingender Ort. Genauso geeignet sind Auftaktbereich, ein eigener Markenabschnitt, der Fußbereich, ein Trennband oder eine Bildunterschrift.
- Auch ein technisch oder gestalterisch schwaches Logo wird eingesetzt, nicht ersetzt und nicht weggelassen. Es darf skaliert, freigestellt, eingefärbt, auf eine Fläche gesetzt oder in ein größeres Motiv eingebunden werden.
- Ist die Vorlage für kleine Größen zu fein, wird sie an ihrem sichtbaren Einsatzort groß genug gezeigt; kleine Größen wie Favicon dürfen zusätzlich eine abgeleitete, vereinfachte Marke nutzen. Die abgeleitete Marke ersetzt den sichtbaren Einsatz des Originals nicht.
- Der tatsächliche Einsatzort wird im Design Contract und im Asset Register festgehalten.
- Wird kein Logo gefunden, wird das ausdrücklich als Befund dokumentiert, statt es unerwähnt zu lassen.

## Referenznutzung

Für jede Referenz notieren: `Rolle`, `Prinzip`, `warum passend`, `konkreter Einsatz oder Adaption`, `tatsächlich verwendete Elemente`, `statischer Nachweis`, `Interaktionsnachweis`. Siehe [[90-References/Inspiration Catalog]] und [[90-References/Reference Research Workflow]].

Inspiration ist bei jedem neuen Web-Produkt Pflicht, die Übernahme eines Musters nicht. Die Designentscheidung entsteht aus Projektziel, Referenzevidenz und UI UX Pro Max Empfehlungen; bei Konflikten gilt der freigegebene Master Spec.
