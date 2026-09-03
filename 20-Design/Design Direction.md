---
type: canonical
status: canonical
updated: 2026-09-03
depends_on:
  - "[[10-Strategy/Discovery and Scope]]"
impacts:
  - "[[20-Design/Landing Page Craft]]"
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
- Referenzmodus nach [[90-References/Reference Research Workflow]]: `Eigenentwurf`, `nutzer-vorgegeben` oder bei mehreren Websites für genau eine Fassung `ausgewählte Leitreferenz`, sofern eine starke Passung gefunden wird; nur im letzten Fall direkte URL, Passung, Übernahmetiefe, tragende Übernahmen und bewusste Abweichungen
- gewählter Leitbenchmark aus [[20-Design/Interface Benchmarks]] samt übernommenen und ausdrücklich nicht übernommenen Elementen
- vollständiger Tokenvertrag nach [[20-Design/Color System#Tokenvertrag]] mit gesetztem Wert je Pflichtrolle für Light und Dark
- gewählte Radiusskala, Rahmenbehandlung, Flächenlogik und Tiefe; innerhalb der Website konsistent, aber nicht aus einer anderen Fassung übernommen
- Bewegungstokens und eine eigene Bewegungsgrammatik; kalibrierte Beispiele in [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] sind Optionen, keine Defaults
- Primär- und gegebenenfalls Zweitschrift samt Rollen, Lesbarkeits-, Lizenz- und Zeitbezugsentscheidung nach [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]]
- Bildplan nach [[20-Design/Imagery and AI Editing]]: Rolle je Bild, Bearbeitungsbedarf, Freistellungen, geplante `ai-placeholder`-Bilder
- Informations- und Textbudget je Route nach [[10-Strategy/Information Density and Mobile Clarity]]
- primäre Beweisform und konkreter Inhaltsanker der Landing Page; ein interaktives Kernmodul nach [[20-Design/Motion and Interaction#Interaktives Kernmodul]] nur wenn es inhaltlich trägt
- bei referenzgeführter Fassung: Leitreferenz mit übertragbaren Prinzipien und konkreter Einsatz-/Adaptionsentscheidung; bei Eigenentwürfen: Herleitung aus Projektwahrheit, Leitbenchmark und Inhaltsanker statt einer verdeckten Ersatzreferenz
- Grad an Dichte, Ausdruck, Motion und Bilddominanz
- Entscheidung für ein reales Kernartefakt, direkt übernommenes oder kreativ adaptiertes Leitmedium samt statischer Alternative
- die im Auftrag verlangte Anzahl vollständig gebauter Websites nach [[00-Start/05 Web Product Workflow#Anzahl der Websites]]; bei mehreren jeweils eigene Leitidee, Komposition, Unterseiten-Dramaturgie und Motion-Choreografie bei identischen Fakten und Funktionsanforderungen, belegt durch die Unterscheidungsmatrix aus dem Abschnitt Stilabstand bei mehreren Websites
- Copy-Entscheidung nach [[10-Strategy/Website Copy]]: Anrede, Tonfall und die Stellen, an denen zusammenhängende ganze Sätze stehen
- Kompositionsentscheidung für den Auftakt und für jede Sektionsart, ausdrücklich abweichend vom Standardmuster; siehe Abschnitt Komposition und Überschriften sowie [[20-Design/Landing Page Craft#Auftakt-Repertoire]]
- Nutzwertnachweis des Auftakts an den realen Prüfbreiten: vollständige Lesbarkeit, Verhältnis von Überschrift zu Inhaltsanker, sichtbare primäre Handlung und Übergang zur nächsten Nutzerfrage innerhalb der ersten zwei Bildschirmhöhen
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
- Genau ein wiedererkennbares Signaturdetail je Website, aus Marke, Material, Ort oder Inhalt hergeleitet und in ruhigerer Form auf den Unterseiten wiederholt. Siehe [[20-Design/Landing Page Craft#Das Signaturdetail]].

## Medien und mehrere Websites

Medien sind kein nachträglicher Schmuck. Wenn Produkt, Ort, Ergebnis oder Prozess visuell belegt werden können, bildet ein bereitgestelltes, gefundenes, direkt übernommenes oder kreativ adaptiertes Bild, Video, Interface oder Artefakt die visuelle Achse. Für bewegte oder schwere Medien werden Poster, Inhaltsalternative, Ladezustand und Mobile-/Low-Power-Variante im Design Contract bestimmt. Quelle und Einsatz werden nach dem Build in [[50-Legal/Assets Copyright and Licenses]] dokumentiert. Diese Dokumentation darf nie den Einsatz, ein Ersatzmedium oder eine getrennte Website-Fassung auslösen.

Verlangt der Auftrag mehrere Websites, müssen sie mehr sein als andere Farben oder Buttonformen. Jede wählt eine eigene Leitmetapher, Auftaktkomposition, Unterseiten-Dramaturgie, Bewegungsrolle und sichtbare Interface-Grammatik. Jede wird als vollständige Website anhand derselben Inhalte, Nutzerflüsse, Accessibility-, Performance- und SEO-Kriterien umgesetzt, nicht gegeneinander zur Auswahl gestellt.

Stilabstand ist kein Selbstzweck. Wenn dieselbe grobe Landing-Page-Anatomie oder Reihenfolge der Nutzerfragen für alle Fassungen sachlich am stärksten ist, darf und soll sie wiederkehren. Eigenständigkeit entsteht dann über Komposition, Medium, Raster, Typografie, Flächenlogik, Komponenten und Motion. Keine Fassung erhält absichtlich einen schwächeren, leereren oder schwerer lesbaren Auftakt, nur damit die Matrix mehr Unterschiede zeigt.

## Abstand zu Vorgängerfassungen

Existieren frühere Projekte oder Durchläufe desselben Betriebs, entsteht vor dem Design ein Übernahmeregister im `PROJECT.md`:

| Bewusst übernehmen | Bewusst neu entscheiden |
|---|---|
| verifizierte Fakten, gemeinsame Inhaltsquelle, freigegebene Assets, funktionierende Build- und Deployment-Infrastruktur | Art Direction, Leitmotiv, Fassungsname, Signalfarbe, Typografie, Kopf- und Fußbereich, Seiten-Chrome, Komponentenrepertoire, primäre Beweisform und Motion-Grammatik |

Leitmotiv, Fassungsname, Signalfarbe und primäre Beweisform dürfen sich wiederholen, wenn der jeweilige Design Contract eine konkrete, sachliche Begründung dokumentiert. Gleicher Betrieb, gleicher Builder oder funktionierende Vorgängerversion sind allein noch keine Begründung. Gemeinsame Klassen, Komponenten oder Tokens werden übernommen, wenn sie Infrastruktur statt Art Direction verkörpern; der Grenzfall wird im Übernahmeregister benannt.

## Stilabstand bei mehreren Websites

Kanonische Regel für den sichtbaren Unterschied zwischen mehreren gebauten Websites desselben Auftrags. Zwei Websites, die sich beim Überfliegen für dasselbe Angebot halten lassen, verfehlen den Auftrag, auch wenn beide für sich gut sind.

Vor der ersten Zeile UI-Code entsteht in `PROJECT.md` eine Unterscheidungsmatrix mit einer Spalte je Website. Die Matrix erzwingt nicht auf jeder Zeile künstlichen Unterschied. Sie belegt, dass jede Website eine eigenständige, in sich zusammenhängende Richtung besitzt. Mindestens fünf für den Auftrag wirksame Achsen unterscheiden sich deutlich; auf anderen Achsen darf dieselbe sachlich beste Lösung wiederkehren. Bloße Synonyme oder dieselbe Struktur mit anderer Farbe bilden noch keine eigene Richtung.

Die Matrix wird nach der gemeinsamen Nutzstruktur ausgefüllt. Zuerst werden die Nutzerfragen, die stärkste Beweisform und die sinnvolle Grobreihenfolge bestimmt. Erst danach werden mindestens fünf wirksame Gestaltungsachsen auseinandergeführt. Referenznähe zählt nicht als eigene Achse. Nach [[90-References/Reference Research Workflow]] ist genau eine Website des Auftrags referenzgeführt, sofern eine starke Passung gefunden wurde; die übrigen Richtungen dürfen ihre Eigenständigkeit nicht durch ein lauteres Stilzitat, eine größere Überschrift oder den Verzicht auf einen benötigten Inhaltsanker simulieren.

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
- Überschriften dürfen typografisch groß, gebrochen, überlappend oder mit einem Medium verschränkt gesetzt werden, solange Lesbarkeit, Fokusreihenfolge und Reflow stimmen. Anschnitt ist nur an einem dekorativen Duplikat zulässig; die einzige semantische H1 bleibt vollständig sichtbar.
- Der Auftakt wird aus Inhalt, Leitmetapher, Beweis und nächster Handlung entwickelt. Auch ein mittiger Titel mit Unterzeile und Aktionen kann richtig sein, wenn genau diese Ruhe und Symmetrie zum Auftrag passt; er darf nicht bloß ungeprüfter Default sein.
- Zwei bis drei verschiedene Überschriftenanordnungen pro Seite. Eine einzige wiederholte Anordnung wirkt generiert, mehr als drei wirken zufällig. Die Auswahl steht im Design Contract, die Anordnungen selbst in [[90-References/Derived Design Patterns#Anordnung von Überschriften]].
- Der Abstand über einer Überschrift ist größer als der Abstand darunter, und benachbarte Typostufen unterscheiden sich um mindestens den Faktor 1,25. Zu nah beieinanderliegende Stufen erzeugen keine Hierarchie.
- Rhythmus entsteht über Maßstabssprünge, Weißraumwechsel und wechselnde Flächenhelligkeit, nicht über immer neue Kartenformen.
- Derselbe Inhalt darf bewusst eine andere Grundform erhalten: Zeile, Tabelle, Liste, Fließtext, Bildunterschrift oder Randspalte statt Karte. Die Form folgt der Informationsart, nicht der Bequemlichkeit.
- Jede Abweichung von der Leserichtung braucht eine klare Ausrichtungsachse. Asymmetrie ohne Achse ist Unordnung.

## Landing Page

Für die Startseite beziehungsweise Landing Page gilt ein höherer Anspruch als für Unterseiten. Höher bedeutet nützlicher, klarer und merkfähiger, nicht automatisch lauter.

Aufbau, Auftaktrollen, Auftakt-Repertoire, Überschriftenanordnung auf dieser Seite, Kopfzeilenrolle, Beweisplatzierung, Handlungsdichte, Signaturdetail und die konkrete Abgrenzung zur generierten Anmutung sind kanonisch in [[20-Design/Landing Page Craft]] geregelt. Der Design Contract dieser Website entscheidet daraus und begründet:

- gewählte Auftaktkomposition aus [[20-Design/Landing Page Craft#Auftakt-Repertoire]] und die Besetzung aller sechs Auftaktrollen, insbesondere des Beweisankers
- **Nutzwert vor Stilintensität.** Angebot, konkreter Inhaltsanker und nächste Handlung bilden eine zusammenhängende, lesbare Antwort. Reine Stimmung, leere Fläche und typografische Übergröße besetzen den Inhaltsanker nicht.
- **Bild optional, Bildrolle verbindlich.** Wird ein Bild eingesetzt, nimmt es mit Ausschnitt, Maßstab und Blickrichtung am Raster und an der Aussage teil. Fehlt ein vorgesehenes Bild real, gilt [[20-Design/Imagery and AI Editing#KI-generierte Bilder]].
- **Lesbarkeit ist eine harte Grenze.** Die vollständige semantische H1 bleibt bei 320 und 375 Pixel, an den Desktop-Prüfbreiten, bei 200 Prozent Zoom, bei großer Systemschrift und mit der realen Kopfzeile unangeschnitten und unverdeckt. Dekorative Duplikate dürfen beschnitten werden, der einzige lesbare Titel nie.
- **Interesse entsteht aus Beziehung.** Maßstab, Raster, Medium, Fakten und Handlung erzeugen Spannung miteinander. Schriftgröße allein, ein vollflächiges Epochenzitat oder eine erzwungene Andersartigkeit sind kein Konzept. Stilzitate bleiben nachgeordnet und folgen [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]].
- **Beweis vor Pflichtinteraktion.** Bild, Team, Case, Arbeitsprobe, Rechner, Produktansicht, Prozess und klare Erklärung sind gleichwertige Beweisformen.
- **Professionell ist zweckpassend.** Hierarchie, präzise Abstände und ein kohärentes Farb- und Flächensystem gelten in warmen, hellen, dunklen, zurückhaltenden und expressiven Richtungen gleichermaßen. Eine ruhige, weitgehend statische Landing Page mit echtem Inhalt ist eine vollwertige Entscheidung und wird als solche dokumentiert.
- gewähltes Signaturdetail nach [[20-Design/Landing Page Craft#Das Signaturdetail]] samt Herleitung und Wiederholungsorten
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

Die Auseinandersetzung mit Benchmarks und Mustern ist bei jedem neuen Web-Produkt Pflicht. Ihre Zahl folgt [[90-References/Reference Research Workflow]]: Einzelwebsite als Eigenentwurf, bei mehreren genau eine referenzgeführte Fassung bei starker Passung und nur bei dokumentiert erfolgloser Suche keine. Die Designentscheidung entsteht aus Projektziel, Projektwahrheit, Benchmarkevidenz und UI UX Pro Max Empfehlungen; bei Konflikten gilt der freigegebene Master Spec.
