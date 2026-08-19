---
type: canonical
status: canonical
updated: 2026-08-19
source: "[[90-References/Inspiration Catalog]]"
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
- unmotiviertes Stilzitat ohne Marken- oder Inhaltsbezug, gleich ob retro, futuristisch, minimalistisch, editorial oder technisch. Kanonisch in [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]]
- unbearbeitete Bestandsbilder mit falschem Winkel, störendem Hintergrund, fremder Farbstimmung oder zu geringer Auflösung; kanonisch in [[20-Design/Imagery and AI Editing]]
- sichtbare Kennzeichnung, Wasserzeichen oder Overlay auf einem KI-generierten Bild
- graue Platzhalterflächen, Bildsymbole oder `lorem`-Bilder an Stellen, an denen ein Bild vorgesehen ist
- Textwände, doppelt beantwortete Nutzerfragen und Abschnitte über dem Budget aus [[10-Strategy/Information Density and Mobile Clarity]]
- häufige Farbpalette ohne projektspezifische Herleitung, siehe [[20-Design/Color System#Häufige Defaults bewusst entscheiden]]
- Em-Dash in Website-Copy
- Emojis als Icons oder Aufzählungszeichen
- Glas-Header ohne gemessenen Kontrast gegen den tatsächlich darunterliegenden Inhalt oder ohne deckenden Fallback. Eine durchscheinende Kopfzeile ist eine optionale Stilentscheidung, kein Standard; Bedingungen in [[30-Frontend/Components and UI States#Option durchscheinende Kopfzeile]]
- inkonsistente Tiefenlogik und Verlauf oder Schatten ohne erkennbare materielle beziehungsweise hierarchische Rolle. Kanonisch in [[20-Design/Typography Layout and Spacing#Tiefe und Rahmen]]
- Kopfzeile, deren Inventar nicht aus der Informationsarchitektur folgt, oder die bei realen Texten, Zoom und schmalen Breiten zufällig überläuft, siehe [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]]
- jede Sektion als gleichförmiges abgerundetes Card-Grid
- riesige Icons mit winzigem Text
- frei driftende Radius-, Rahmen- oder Containerwerte außerhalb des im Website-Contract gewählten Systems; uneinheitliche Buttonhöhen ohne funktionalen Grund
- aggressive oder überraschende Card-Lifts, Rotation oder Schattensprünge ohne Aufgabe. Interaktionsfeedback folgt der dokumentierten Grammatik aus [[30-Frontend/Components and UI States#Kartenentscheidung]] und erscheint nur auf tatsächlich klickbaren Flächen
- Hover-Lift, Zeigerwechsel oder Schatten auf einer Fläche, die nichts auslöst
- Cursor-Glows, Bounce oder Scroll-Jacking
- generische KI-/SaaS-Copy, Fake-Testimonials, erfundene Logos und Metriken
- verbloses Kurzstatement direkt unter einer Überschrift, etwa `Online in wenigen Minuten`, sowie Ketten freistehender Behauptungen ohne Verb. Kanonisch in [[10-Strategy/Website Copy#Die Statementzeile unter der Überschrift]]
- Meta-Sätze über die eigene Seite, Quellenversicherungen wie `Gerechnet mit unseren echten Preisen`, sichtbare Pflegedaten wie `Stand 8. August 2026` und Negativabgrenzungen wie `Keine Bewertungsdurchschnitte, keine Bestehensquoten`. Kanonisch in [[10-Strategy/Website Copy#Was gestrichen wird]]
- die erfundene Dreierfigur, also Aufzählungen und Satzreihen aus genau drei Aspekten ohne sachlichen Grund. Kanonisch in [[10-Strategy/Website Copy#Die Dreierfigur]]
- Semikolon, Gedankenstrich als Einschub und Doppelpunkt als Spannungszeichen in Website-Copy. Kanonisch in [[10-Strategy/Website Copy#Interpunktion]]
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
- Gibt es für jede Rolle aus [[20-Design/Color System#Tokenvertrag]] einen gesetzten Wert, insbesondere für `border-hover` und `accent-subtle`?
- Verändert sich beim Überfahren einer klickbaren Karte tatsächlich etwas, und zwar Rahmen und Position statt nur Farbe?
- Gehören Radien, Rahmen und Schatten zu einer erkennbaren, dokumentierten Grammatik?
- Ist das Tracking für die konkrete Schrift und Textstufe lesbar kalibriert?
- Würde diese Startseite mit ausgetauschtem Logo für jede beliebige Branche funktionieren?

## Impeccable KI-Detail-Review

Verbindlich für **jede** gebaute Website, unabhängig davon, wie viele Websites der Auftrag verlangt. Der Review findet nach der Implementierung und vor der Abnahme statt, zusätzlich zu jedem Einsatz von Impeccable während der Gestaltung.

1. Website vollständig bauen und lokal starten.
2. Impeccable nach [[00-Start/04 Plugins and Skills]] im Review-Modus auf die reale, laufende Website anwenden, nicht auf Entwürfe oder Beschreibungen.
3. Gezielt nach Details suchen, die nach KI-Generat aussehen: redundante Kicker über Überschriften, immer gleiche Sektionsanordnung, austauschbare Copy, dekorative Karten, Standardfarben ohne Markenbezug, Verläufe ohne Grund, gleichförmige Hover-Effekte, erfundene Belege, Füllsätze, Symmetrie ohne Absicht, generische Icons.
4. Die Prüffragen aus [[10-Strategy/Website Copy#Prüffragen vor der Abnahme]] auf jeden sichtbaren Text der Website anwenden, einschließlich Karten, Formularhilfen und Fußzeile.
5. Jeden Befund entweder korrigieren oder mit inhaltlicher Begründung im Decision Log festhalten. „Gefällt mir so“ ist keine Begründung.
6. Ergebnis mit Datum, geprüfter Website, Befundliste und Umsetzungsstand im Projekt dokumentieren. Ohne diesen Nachweis ist Gate `G1` in [[70-QA/Quality Gates]] nicht erfüllt.

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
