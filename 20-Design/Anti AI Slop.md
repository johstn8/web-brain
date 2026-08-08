---
type: canonical
status: canonical
updated: 2026-08-08
source: "[[90-References/Inspiration Catalog]]"
impacts:
  - design-direction
  - components
  - copy
  - qa
---

# Anti AI Slop

## Verbot ohne konkrete Begründung

- **Kicker über Überschriften.** Keine Eyebrow-Zeile, kein Label, keine Kategoriezeile oberhalb einer Überschrift. Weder als Pille, noch als Versalzeile, noch als kleiner farbiger Text, noch als Marker mit vorangestellter Linie oder Ziffer. Details im nächsten Abschnitt.
- Blau-Lila-Gradient, Neon-Glow, Sparkles oder generische Aurora-Fläche
- Retro-Anmutung: kantige Epochen-Displayschrift, alte Buchserife als Markenschrift einschließlich `Iowan Old Style`, dieselbe Serife kombiniert mit Dunkelgrün oder anderen gedeckten Erdtönen, Vintage-Badges, Ornamente, Papier- und Filmkorn. Kanonisch in [[20-Design/Typography Layout and Spacing#Retro-Verbot]]
- unbearbeitete Bestandsbilder mit falschem Winkel, störendem Hintergrund, fremder Farbstimmung oder zu geringer Auflösung; kanonisch in [[20-Design/Imagery and AI Editing]]
- sichtbare Kennzeichnung, Wasserzeichen oder Overlay auf einem KI-generierten Bild
- graue Platzhalterflächen, Bildsymbole oder `lorem`-Bilder an Stellen, an denen ein Bild vorgesehen ist
- Textwände, doppelt beantwortete Nutzerfragen und Abschnitte über dem Budget aus [[10-Strategy/Information Density and Mobile Clarity]]
- Beige, Creme oder Sand als dominante Grundfläche einer Website, siehe [[20-Design/Color System#Verbrauchte Farbwelten]]
- Em-Dash in Website-Copy
- Emojis als Icons oder Aufzählungszeichen
- Glas-Header ohne gemessenen Kontrast gegen den tatsächlich darunterliegenden Inhalt oder ohne deckenden Fallback. Die durchscheinende Kopfzeile selbst ist erlaubt und Standard; Rezept in [[30-Frontend/Components and UI States#Rezept der durchscheinenden Kopfzeile]]
- Schatten im Ruhezustand, mehr als eine Schattenstufe im Projekt, Verlauf als Flächenfüllung ohne Bedeutung. Kanonisch in [[20-Design/Typography Layout and Spacing#Tiefe und Rahmen]]
- Kopfzeile mit mehr als sechs Navigationspunkten oder mit umbrechendem Text, siehe [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]]
- jede Sektion als gleichförmiges abgerundetes Card-Grid
- riesige Icons mit winzigem Text
- Radien außerhalb der vier Stufen aus [[20-Design/Typography Layout and Spacing#Radiusskala]], mehrere Rahmenstärken, uneinheitliche Container- und Buttonhöhen
- aggressive Card-Lifts, also Verschiebung über zwei Pixel, Maßstab über `1.02`, Rotation oder Schattensprung. Der kleine Ein- bis Zwei-Pixel-Lift auf tatsächlich klickbaren Karten ist ausdrücklich erlaubt und erwünscht; Rezept in [[30-Frontend/Components and UI States#Kartenrezept]]
- Hover-Lift, Zeigerwechsel oder Schatten auf einer Fläche, die nichts auslöst
- Cursor-Glows, Bounce oder Scroll-Jacking
- generische KI-/SaaS-Copy, Fake-Testimonials, erfundene Logos und Metriken
- Pricing, FAQ, Logo-Marquee oder Bento-Grid nur weil Landingpages sie oft besitzen
- Hero nach dem Schema Badge, Überschrift, Unterzeile, zwei Buttons
- jede Sektion in derselben Anordnung aus Titel, Lead und Raster

## Kicker und Überschriften

Der Kicker über der Überschrift ist das deutlichste Erkennungszeichen generierter Seiten. Er wiederholt meist, was die Überschrift ohnehin sagt, und verbraucht eine Hierarchiestufe ohne Gegenwert.

**Verboten sind unter anderem:**

- eine Eyebrow-Zeile `PREISE` über der Überschrift „Preise und Gebühren“
- eine gesperrte Versalzeile mit Ziffer wie `01 AUSGANGSLAGE` über der Sektionsüberschrift
- kleine Pillen mit `Neu`, `KI-gestützt`, `Beta` oder einem Kategoriewort über dem Titel
- ein farbiger Kurztext mit vorangestelltem Strich als reine Dekoration

**Stattdessen:**

- Die Einordnung gehört in die Überschrift selbst. Aus „Preise“ plus „Preise und Gebühren“ wird eine Überschrift, die tatsächlich etwas aussagt.
- Eine Nummerierung, die wirklich Orientierung stiftet, steht in derselben Zeile wie die Überschrift, in einer Randspalte oder in einer sichtbaren Kapitelnavigation, nicht als eigene Zeile darüber.
- Kontext, der über die Überschrift hinausgeht, gehört in den Lead darunter, in eine Bildunterschrift oder in die Navigation.
- Eine reale Metazeile in einem redaktionellen Beitrag, etwa Datum, Rubrik oder Autor, ist kein Kicker in diesem Sinn, solange sie eine echte, nicht redundante Information trägt.

## Erkennungsfragen

- Könnte der Text unverändert zu zehn anderen Produkten passen?
- Steht über einer Überschrift eine Zeile, die nur wiederholt, was die Überschrift sagt?
- Ist eine Sektion vorhanden, weil Nutzer sie brauchen oder weil ein Generator sie erwartet?
- Gibt es mehr visuelle Effekte als belastbare Beweise?
- Wiederholt sich dieselbe Kartenform ohne Informationsgrund?
- Beginnt jede Sektion mit derselben Anordnung?
- Sind Mobile, Loading, Error und Focus sichtbar weniger ausgereift als der Hero?
- Soll die Seite älter wirken, als sie ist?
- Sieht die Bildersammlung aus wie eine Sammlung statt wie eine Serie?
- Bleibt auf einem 375 Pixel breiten Display eine Bildschirmhöhe übrig, die nichts Neues sagt?
- Funktioniert jedes sichtbare Control real?
- Gibt es für jede Rolle aus [[20-Design/Color System#Tokenvertrag]] einen gesetzten Wert, insbesondere für `border-hover` und `accent-subtle`?
- Verändert sich beim Überfahren einer klickbaren Karte tatsächlich etwas, und zwar Rahmen und Position statt nur Farbe?
- Stehen alle Radien auf einer der vier Stufen, und trägt im Ruhezustand wirklich keine Fläche einen Schatten?
- Ist negatives Tracking auf den großen Stufen gesetzt und im Fließtext nicht?
- Würde diese Startseite mit ausgetauschtem Logo für jede beliebige Branche funktionieren?

## Impeccable KI-Detail-Review

Verbindlich für **jede** gebaute Website, unabhängig davon, wie viele Websites der Auftrag verlangt. Der Review findet nach der Implementierung und vor der Abnahme statt, zusätzlich zu jedem Einsatz von Impeccable während der Gestaltung.

1. Website vollständig bauen und lokal starten.
2. Impeccable nach [[00-Start/04 Plugins and Skills]] im Review-Modus auf die reale, laufende Website anwenden, nicht auf Entwürfe oder Beschreibungen.
3. Gezielt nach Details suchen, die nach KI-Generat aussehen: Kicker über Überschriften, immer gleiche Sektionsanordnung, austauschbare Copy, dekorative Karten, Standardfarben ohne Markenbezug, Verläufe ohne Grund, gleichförmige Hover-Effekte, erfundene Belege, Füllsätze, Symmetrie ohne Absicht, generische Icons.
4. Jeden Befund entweder korrigieren oder mit inhaltlicher Begründung im Decision Log festhalten. „Gefällt mir so“ ist keine Begründung.
5. Ergebnis mit Datum, geprüfter Website, Befundliste und Umsetzungsstand im Projekt dokumentieren. Ohne diesen Nachweis ist Gate `G1` in [[70-QA/Quality Gates]] nicht erfüllt.

Bei mehreren Websites wird der Review je Website getrennt geführt. Ein gemeinsamer Sammelbefund genügt nicht, weil die Websites unterschiedliche Art Directions haben.

## Reparatur

1. Eine klare Nutzenbotschaft und ein Markenkonzept festlegen.
2. Alle Kicker entfernen und ihre Information in Überschrift, Lead oder Navigation überführen.
3. Unbelegte und redundante Sektionen löschen.
4. Tokens vereinheitlichen.
5. Produkt, Prozess oder echte Arbeit zeigen.
6. Die Motion-Dichte nicht reduzieren, sondern jeden Moment mit Kapitel, Prozess, räumlicher Beziehung oder Handlung verknüpfen und nach [[20-Design/Motion and Interaction]] als eigenständige Route-Choreografie ausarbeiten.
7. Copy konkretisieren und alle Links testen.
8. Mobile, Zustände, Accessibility und Performance vor zusätzlichem Polish fertigstellen.

Der zugrunde liegende Bericht beschreibt diese Muster nach einer nicht unabhängig verifizierten Stichprobe von mehr als 500 Seiten. Seine Liste ist Heuristik, kein Qualitätsstandard.[^report]

[^report]: [Aftermark AI: Vibe Coded Website Report](https://docs.google.com/document/d/e/2PACX-1vTnLEdwSF1HPkuwOkuNneXGCaQAw5N2nnRf7cX_B4zuBLf2VTMi4Yh59gqS-eeVqYpa11iFQYmRjVBW/pub)
