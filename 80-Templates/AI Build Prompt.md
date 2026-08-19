---
type: template
status: canonical
updated: 2026-08-17
---

# AI Build Prompt

```text
Arbeite nach AGENTS.md, beginne bei [[00-Start/00 Brain Index]] und folge [[00-Start/05 Web Product Workflow]]. Bei einem Umsetzungsauftrag lege vor jeder weiteren Arbeit `../projekte/<Projektname>/` mit allen Pflichtdateien an. Baue nie im Brain oder in einem anderen Projektordner.

Projektbrief:
[Project Intake einfügen]

Anzahl der Websites:
Bestimme sie ausschließlich aus meinem Auftragstext. Nenne ich keine Anzahl, baust du genau eine vollständige Website unter `site/`. Nenne ich eine Zahl, baust du genau diese Anzahl unter `versions/01-…` und folgende. Halte Zahl und wörtliche Belegstelle in `PROJECT.md` fest. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]].

Ergebnis:
Besteht eine alte Website, führe zwingend [[10-Strategy/Existing Website Rebuild]] aus: sichere Bestandsinhalte, Bilder, Designs, Animationen und Quellen für ihre direkte kreative Verwendung. Suche dabei gezielt das Firmenlogo und setze es, wenn du eines findest, in jeder gebauten Website sichtbar ein, bevorzugt auf der Startseite. Erstelle danach zuerst einen Project Master Spec samt vollständiger Unterseiten-Sitemap, Annahmen, Risiken und Design Direction. Führe vor UI-Code den Reference Research Workflow im vollen Pflichtumfang aus und dokumentiere konkrete Einsätze, Adaptionen und Negativreferenzen. Nutze bei jeder UI-Aufgabe UI UX Pro Max mit allen Pflicht-Detailabfragen sowie Impeccable gemäß [[00-Start/04 Plugins and Skills]]; bei Motion zusätzlich Emil Design Engineering. Entscheide und dokumentiere den Einsatz von pen.dev; sichere `.pen`-Dateien im Projekt unter `design/`. Jede gebaute Website ist vollständig: eigener Design Contract, eigene Art Direction, ein begründetes Motion-Budget, echte Unterseiten und derselbe Fakten-, Funktions-, Accessibility-, Sicherheits- und SEO-Umfang. Auf `217.154.218.30` erfolgt der Zugriff ohne Projektport über `johannstein.com/dev`, sonst über einen festen lokalen Port. Verwende die gewünschten Bilder, Designs, Animationen und sonstigen Assets unmittelbar, ohne Ersatz, Asset-Sperre, reduzierte Preview oder Auswahlkandidaten. Erst danach dokumentierst du tatsächlichen Einsatz und Quellen in `SOURCE-RIGHTS-REVIEW.md`; der Nutzer/Owner entscheidet allein über spätere Veröffentlichungsfragen. Nutze die Routing Map, lade nur relevanten Kontext, aber arbeite alle zutreffenden Quality Gates ab.

Gestaltung:
- Die Landing Page darf extravagant sein: große Typografie, ungewöhnliche Raster, randlose Medien, überlappende Ebenen, ein starkes Farbstatement und eine ausgeprägte Scroll-Choreografie. Sie bleibt dabei modern, freundlich, professionell und übersichtlich.
- Wähle die Anordnung der Überschriften bewusst und wechsle sie zwischen den Sektionsarten. Nicht jede Sektion beginnt mit Titel, Lead und Raster.
- Unterseiten übernehmen dasselbe Designsystem, treten aber ruhiger auf.
- Wähle einen Leitbenchmark aus [[20-Design/Interface Benchmarks]] und benenne, was du daraus übernimmst und was ausdrücklich nicht.
- Halte Informationen knapp und logisch gestaffelt. Entscheide die Menge am 375-Pixel-Viewport und halte die Textbudgets aus [[10-Strategy/Information Density and Mobile Clarity]] ein.
- Überarbeite jedes Bestandsbild vor dem Einsatz: Winkel, Ausschnitt, Hintergrund, Farbe, Auflösung. Stelle Objekte frei und gleiche alle Bilder einer Website zu einer Serie an. Fehlt ein reales Leitbild, erzeuge ein KI-Bild und setze es ein, ohne es auf der Website zu kennzeichnen; führe es im Asset Register als `ai-placeholder` mit Prompt und Ersetzungshinweis. Kanonisch in [[20-Design/Imagery and AI Editing]].
- Lege je Landing Page die stärkste reale Beweisform fest. Baue ein interaktives Kernmodul nach [[20-Design/Motion and Interaction#Interaktives Kernmodul]] nur, wenn der Nutzer damit etwas Reales besser verstehen, prüfen, wählen oder erleben kann.
- Setze **vor der ersten Komponente** den vollständigen Tokenvertrag nach [[20-Design/Color System#Tokenvertrag]] in genau einer Tokenquelle, einschließlich `border-hover` und `accent-subtle`. Ohne diese Rollen wirken alle Zustände flach.
- Halte die H0-Untergrenze aus [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]] ein. Entscheide Radius, Rahmen, Flächenlogik, Karten-/Zeilen-/Tabellen-/Listenrepertoire, Kopf- und Fußbereich, Chrome, Zweitschrift und Motion **je Website**. B5 ist nur ein wählbares Stilprofil.
- Begründe die Zweitschrift und ihre Rollen. Monospace ist sachlich für Code, Terminal, IDs, Tastenkürzel oder echte Zahlenspalten, nicht automatisch für Anschriften, Fließtext, Sektionstitel, Zeiten, Tags oder Abschnittsnummern.
- Setze pro Website einen eigenen Zeit- und Kurvensatz. Die B5-Werte aus [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] sind Beispiele, keine Grundeinheit.

Verbindlich:
- keine Fakten, Testimonials, Logos, Zertifikate oder Metriken erfinden
- keine redundanten oder rein dekorativen Kicker; echte Rubrik-, Status-, Datums- oder Prozessinformation darf eine eigene Hierarchiestufe erhalten
- **bei jedem Website-Build UI UX Pro Max ausführen, ausnahmslos und bei mehreren Websites je Website getrennt**
- Typografie und mögliche Zeitbezüge aus Marke, Inhalt und Lesesituation herleiten; keine austauschbaren Stilzitate
- keine graue oder leere Platzhalterfläche dort, wo ein Bild vorgesehen ist, und keine sichtbare Kennzeichnung eines KI-Bildes
- Radius-, Rahmen- und Tiefenentscheidungen bleiben innerhalb der einzelnen Website konsistent; Schatten, Rahmen, Hairlines und rahmenlose Flächen sind gleichwertige Mittel
- kein Hover-Lift, Zeigerwechsel oder Schatten auf einer Fläche, die nichts auslöst; kein Lift über zwei Pixel und kein Hover-Maßstab über `1.02`
- kein Glas-Header ohne Kontextkontrast und deckenden Fallback; eine durchscheinende Kopfzeile ist kein Default
- kein Verlaufstext und keine Verlaufsfläche ohne dargestellte Bedeutung
- Kopfzeileninventar aus Informationsarchitektur und realen Beschriftungen ableiten; bei 320, 375, 768, 1280 und 1920 Pixel, großer Systemschrift und 200 Prozent Zoom entstehen kein zufälliger Umbruch, Beschnitt oder Überlauf
- kein Beige, Creme oder Sand als dominante Grundfläche und keine andere verbrauchte Farbwelt; jede Farbrolle hat eine benannte Herleitung
- gefundenes Firmenlogo sichtbar einsetzen, unabhängig von seiner Qualität
- Bilder, Videos, Interfaces, Designs, Motion und andere Assets direkt kopieren, adaptieren und kreativ einsetzen; tatsächlichen Einsatz erst danach ohne Ersatz oder KI-Sperre im Review erfassen
- genau die beauftragte Anzahl auslieferbarer Websites mit echten Unterseiten, umgebungsgerechtem Zugriff, eigener Motion-Choreografie und vollständiger SEO je Route
- je Website Motion-Budget `none | low | medium | high`; nur zweckgebundene Bewegungen bauen und jede relevante Bewegung samt Reduced-Motion- und Performance-Nachweis dokumentieren
- mobile-first, WCAG 2.2 AA, Reduced Motion und alle UI-Zustände
- kurzes Seitentitel-System ohne Pipe, vollständiges Favicon- und Social-Metadata-Set
- keine Em-Dashes in Website-Copy, keine Sparkles, Emoji-Icons oder unbegründeten Blau-Lila-Gradienten
- Copy nach [[10-Strategy/Website Copy]]: keine Meta-Sätze über die Seite, keine sichtbaren „Stand“-Daten, keine Negativabgrenzung, keine Selbstverständlichkeiten, kein verbloses Statement unter einer Überschrift, keine erfundene Dreierfigur, kein Semikolon und kein Gedankenstrich als Einschub, dafür ganze Sätze an den tragenden Stellen
- bei mehreren Websites die Unterscheidungsmatrix vor dem ersten UI-Code ausfüllen und mindestens fünf wirksame Achsen deutlich unterscheiden; sachlich gleiche Lösungen dürfen begründet wiederkehren
- bei Erstellung und jedem Update je Inhaltsblock `owner_editable`, stabilen JSON-Pointer, Feldtyp, Grenzen, Preview-Routen und Veröffentlichungspolicy nach [[60-Operations/Owner Hosting and Dashboard]] entscheiden; bei zentralem Owner-Hosting den Vertrag nach [[80-Templates/Owner Hosting Website Contract]] anlegen
- je Website ab Projektbeginn `release-readiness/<website-slug>.md` nach [[60-Operations/Release Readiness Register]] führen; jede neue Vorschau-Sperre, Attrappe, sichtbare Unfertig-Aussage und noch nicht produktive Integration in derselben Änderung eintragen
- serverseitige AuthZ/Validierung, sichere Sessions, Rate- und Kostenlimits
- Sitemap, Dateninventar, prüfpflichtige Rechtstexte, Dependencies, Tests und Betrieb atomar aktuell halten
- Abweichungen und Trade-offs im Decision Log dokumentieren

Vor der Abgabe:
Führe für jede gebaute Website den Impeccable KI-Detail-Review nach [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review]] auf der real laufenden Website durch. Prüfe jede tatsächlich vorkommende Komponenten-/Flächenkombination auf Kontrast sowie width-basierte Kinder in height-basierten Containern auf Geometrie. Suche gezielt nach Details, die nach KI-Generat aussehen, korrigiere sie und dokumentiere Datum, Befunde und Umsetzungsstand.

Liefere keine bloße Demo. Eine echte Darstellung an den Prüfbreiten ist Pflicht; fehlt die Renderfähigkeit, melde sie vor Lieferung als Blocker. Beende erst, wenn Quality Gates nachweisbar erfüllt oder konkrete Blocker dokumentiert sind.
```
