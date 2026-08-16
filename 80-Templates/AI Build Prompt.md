---
type: template
status: canonical
updated: 2026-08-08
---

# AI Build Prompt

```text
Arbeite nach AGENTS.md, beginne bei [[00-Start/00 Brain Index]] und folge [[00-Start/05 Web Product Workflow]]. Bei einem Umsetzungsauftrag lege vor jeder weiteren Arbeit `../projekte/<Projektname>/` mit allen Pflichtdateien an. Baue nie im Brain oder in einem anderen Projektordner.

Projektbrief:
[Project Intake einfügen]

Anzahl der Websites:
Bestimme sie ausschließlich aus meinem Auftragstext. Nenne ich keine Anzahl, baust du genau eine vollständige Website unter `site/`. Nenne ich eine Zahl, baust du genau diese Anzahl unter `versions/01-…` und folgende. Halte Zahl und wörtliche Belegstelle in `PROJECT.md` fest. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]].

Ergebnis:
Besteht eine alte Website, führe zwingend [[10-Strategy/Existing Website Rebuild]] aus: sichere Bestandsinhalte, Bilder, Designs, Animationen und Quellen für ihre direkte kreative Verwendung. Suche dabei gezielt das Firmenlogo und setze es, wenn du eines findest, in jeder gebauten Website sichtbar ein, bevorzugt auf der Startseite. Erstelle danach zuerst einen Project Master Spec samt vollständiger Unterseiten-Sitemap, Annahmen, Risiken und Design Direction. Führe vor UI-Code den Reference Research Workflow im vollen Pflichtumfang aus und dokumentiere konkrete Einsätze, Adaptionen und Negativreferenzen. Nutze bei jeder UI-Aufgabe UI UX Pro Max mit allen Pflicht-Detailabfragen sowie Impeccable gemäß [[00-Start/04 Plugins and Skills]]; bei Motion zusätzlich Emil Design Engineering. Entscheide und dokumentiere den Einsatz von pen.dev; sichere `.pen`-Dateien im Projekt unter `design/`. Jede gebaute Website ist vollständig: eigene Art Direction, hohe Scroll-Choreografie, echte Unterseiten, eigener fester Port und derselbe Fakten-, Funktions-, Accessibility-, Sicherheits- und SEO-Umfang. Verwende die gewünschten Bilder, Designs, Animationen und sonstigen Assets unmittelbar, ohne Ersatz, Asset-Sperre, reduzierte Preview oder Auswahlkandidaten. Erst danach dokumentierst du tatsächlichen Einsatz und Quellen in `SOURCE-RIGHTS-REVIEW.md`; der Nutzer/Owner entscheidet allein über spätere Veröffentlichungsfragen. Nutze die Routing Map, lade nur relevanten Kontext, aber arbeite alle zutreffenden Quality Gates ab.

Gestaltung:
- Die Landing Page darf extravagant sein: große Typografie, ungewöhnliche Raster, randlose Medien, überlappende Ebenen, ein starkes Farbstatement und eine ausgeprägte Scroll-Choreografie. Sie bleibt dabei modern, freundlich, professionell und übersichtlich.
- Wähle die Anordnung der Überschriften bewusst und wechsle sie zwischen den Sektionsarten. Nicht jede Sektion beginnt mit Titel, Lead und Raster.
- Unterseiten übernehmen dasselbe Designsystem, treten aber ruhiger auf.
- Wähle einen Leitbenchmark aus [[20-Design/Interface Benchmarks]] und benenne, was du daraus übernimmst und was ausdrücklich nicht.
- Halte Informationen knapp und logisch gestaffelt. Entscheide die Menge am 375-Pixel-Viewport und halte die Textbudgets aus [[10-Strategy/Information Density and Mobile Clarity]] ein.
- Überarbeite jedes Bestandsbild vor dem Einsatz: Winkel, Ausschnitt, Hintergrund, Farbe, Auflösung. Stelle Objekte frei und gleiche alle Bilder einer Website zu einer Serie an. Fehlt ein reales Leitbild, erzeuge ein KI-Bild und setze es ein, ohne es auf der Website zu kennzeichnen; führe es im Asset Register als `ai-placeholder` mit Prompt und Ersetzungshinweis. Kanonisch in [[20-Design/Imagery and AI Editing]].
- Baue in jede Landing Page mindestens ein interaktives Kernmodul mit realen Daten nach [[20-Design/Motion and Interaction#Interaktives Kernmodul]].
- Setze **vor der ersten Komponente** den vollständigen Tokenvertrag nach [[20-Design/Color System#Tokenvertrag]] in genau einer Tokenquelle, einschließlich `border-hover` und `accent-subtle`. Ohne diese Rollen wirken alle Zustände flach.
- Halte die Detailebene B5 aus [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]] ein. Sie gilt immer, zusätzlich zum gewählten Leitbenchmark: drei nahe Flächenstufen, ein Pixel Hairline in zwei Rahmenstufen, im Ruhezustand kein Schatten, vier Radiusstufen, negatives Tracking nur groß, Mono für Werte und Tags.
- Baue Karten nach [[30-Frontend/Components and UI States#Kartenrezept]] und die Kopfzeile nach [[30-Frontend/Components and UI States#Rezept der durchscheinenden Kopfzeile]].
- Verwende die Bewegungsrezepte mit den Werten aus [[20-Design/Motion and Interaction#Standardrezepte mit Werten]] als Grundeinheit: Reveal über zwölf Pixel in 500 Millisekunden mit gehaltenem Endzustand, Stagger 30 bis 80 Millisekunden, Karten-Hover ein bis zwei Pixel mit Rahmenwechsel, Press 100 bis 160 Millisekunden, genau ein Zeichenauftakt je Website, dekorative Hintergründe weich ausmaskiert. Darauf baust du die geforderte Route-Choreografie auf; die Rezepte allein erfüllen das Motion-Niveau nicht.

Verbindlich:
- keine Fakten, Testimonials, Logos, Zertifikate oder Metriken erfinden
- kein Kicker über einer Überschrift, weder als Pille noch als Versalzeile noch als Marker mit Linie oder Ziffer
- **bei jedem Website-Build UI UX Pro Max ausführen, ausnahmslos und bei mehreren Websites je Website getrennt**
- keine Retro-Anmutung: kein `Iowan Old Style` oder typgleiche alte Buchserife als Markenschrift, keine kantige Epochen-Displayschrift, keine Kombination aus Serife, gedecktem Erdton und Ornament
- keine graue oder leere Platzhalterfläche dort, wo ein Bild vorgesehen ist, und keine sichtbare Kennzeichnung eines KI-Bildes
- kein Schatten im Ruhezustand, keine zweite Schattenstufe, kein Radius außerhalb der vier Stufen, keine zweite Rahmenstärke
- kein Hover-Lift, Zeigerwechsel oder Schatten auf einer Fläche, die nichts auslöst; kein Lift über zwei Pixel und kein Hover-Maßstab über `1.02`
- kein Glas-Header ohne gemessenen Kontrast und ohne deckenden Fallback
- kein Verlaufstext und keine Verlaufsfläche ohne dargestellte Bedeutung
- Kopfzeile mit höchstens sechs Navigationspunkten; kein Text und kein Knopf in der Kopfzeile bricht um, geprüft bei 1280, 1440 und 1920 Pixel mit der längsten realen Beschriftung. Logos dürfen mehrzeilig sein
- kein Beige, Creme oder Sand als dominante Grundfläche und keine andere verbrauchte Farbwelt; jede Farbrolle hat eine benannte Herleitung
- gefundenes Firmenlogo sichtbar einsetzen, unabhängig von seiner Qualität
- Bilder, Videos, Interfaces, Designs, Motion und andere Assets direkt kopieren, adaptieren und kreativ einsetzen; tatsächlichen Einsatz erst danach ohne Ersatz oder KI-Sperre im Review erfassen
- genau die beauftragte Anzahl auslieferbarer Websites mit echten Unterseiten, eigenem Port, eigener Motion-Choreografie und vollständiger SEO je Route
- pro primärer Inhaltsroute eine kontinuierliche Scrollsequenz, zwei weitere Scroll-/In-View-Bewegungen und insgesamt mindestens zwölf dokumentierte Bewegungsentscheidungen je Website
- mobile-first, WCAG 2.2 AA, Reduced Motion und alle UI-Zustände
- kurzes Seitentitel-System ohne Pipe, vollständiges Favicon- und Social-Metadata-Set
- keine Em-Dashes in Website-Copy, keine Sparkles, Emoji-Icons oder unbegründeten Blau-Lila-Gradienten
- Copy nach [[10-Strategy/Website Copy]]: keine Meta-Sätze über die Seite, keine sichtbaren „Stand“-Daten, keine Negativabgrenzung, keine Selbstverständlichkeiten, kein verbloses Statement unter einer Überschrift, keine erfundene Dreierfigur, kein Semikolon und kein Gedankenstrich als Einschub, dafür ganze Sätze an den tragenden Stellen
- bei mehreren Websites die Unterscheidungsmatrix nach [[20-Design/Design Direction#Stilabstand bei mehreren Websites]] vor dem ersten UI-Code ausfüllen und in mindestens vier Merkmalen umsetzen
- serverseitige AuthZ/Validierung, sichere Sessions, Rate- und Kostenlimits
- Sitemap, Dateninventar, prüfpflichtige Rechtstexte, Dependencies, Tests und Betrieb atomar aktuell halten
- Abweichungen und Trade-offs im Decision Log dokumentieren

Vor der Abgabe:
Führe für jede gebaute Website den Impeccable KI-Detail-Review nach [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review]] auf der real laufenden Website durch. Suche gezielt nach Details, die nach KI-Generat aussehen, korrigiere sie und dokumentiere Datum, Befunde und Umsetzungsstand.

Liefere keine bloße Demo. Beende erst, wenn Quality Gates nachweisbar erfüllt oder konkrete Blocker dokumentiert sind.
```
