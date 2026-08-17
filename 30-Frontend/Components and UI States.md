---
type: canonical
status: canonical
updated: 2026-08-17
impacts:
  - accessibility-tests
  - visual-regression
  - analytics
  - header-navigation
  - "[[10-Strategy/Information Architecture and Sitemap]]"
---

# Components and UI States

## Komponentenvertrag

Jede Komponente dokumentiert:

- Zweck und Nicht-Zweck
- Props/Input mit erlaubten Grenzen
- semantisches Element und Tastaturverhalten
- visuelle Tokens und Varianten
- Daten-, Fehler- und Ladeverhalten
- responsive Verhalten
- Accessibility Name, Role, Value
- Events und Seiteneffekte
- Beispiele und Tests

## Zustände

Prüfe, soweit relevant: default, hover, focus-visible, active, selected, disabled, read-only, loading, optimistic, success, warning, error, empty, partial data, offline, permission denied, expired session.

## Kartenentscheidung

Vor UI-Code wird je Website entschieden, welches Komponentenrepertoire ihre Inhalte trägt. Eine Karte ist eine Möglichkeit, kein Standardcontainer.

| Inhalt oder Aufgabe | mögliche Grundform |
|---|---|
| eigenständig verlinktes Projekt oder Angebot | Karte, Zeile, Cover, Eintrag im Index |
| vergleichbare Werte | Tabelle, ausgerichtete Liste, Diagramm mit Textalternative |
| kurze Leistungsgruppe | typografische Liste, Definition List, Prozessstrecke |
| Status oder Ereignisfolge | Zeile, Timeline, Log, gruppierte Liste |
| ein dominantes Objekt | Bühne, Viewer oder randlose Medienfläche statt Kartenraster |

Der Design Contract benennt für jede wichtige Inhaltsart die gewählte Grundform. Bei mehreren Websites muss das Komponentenrepertoire eine Pflichtachse der [[20-Design/Design Direction#Stilabstand bei mehreren Websites|Unterscheidungsmatrix]] sein.

### Option B5-Karte

Nur wenn die Website B5 oder diese Kartenvariante bewusst wählt:

- Fläche `surface`, ein Pixel `border`, dokumentierter Kartenradius, kein Schatten im Ruhezustand;
- großzügiger, einheitlicher Innenabstand; Bildflächen dürfen randlos an der Oberkante sitzen;
- klare Inhaltsreihenfolge aus Medium oder Icon, Titel, kurzer Erklärung, optionaler Metazeile und höchstens einer Aktion;
- eine technische Mono-Metazeile oder `·` als Trenner nur, wenn die Schriftentscheidung der Website genau diese Rolle begründet;
- klickbare Karten dürfen bei geeigneter Zeigereingabe Rahmen, Position und optional den einen dokumentierten Hover-Schatten ändern.

### Zustände abgegrenzter Inhaltsflächen

| Zustand | Verhalten |
|---|---|
| `hover` bei `hover: hover` und `pointer: fine` | nur auf klickbaren Flächen; das Feedback folgt der gewählten Website-Grammatik |
| `focus-visible` | sichtbarer Fokusring oder gleichwertige Kontur in `focus` mit Abstand; unabhängig vom Hover |
| `active` | unmittelbare, unterbrechbare Rückmeldung ohne Layoutsprung |
| `selected` oder `aria-current` | zusätzlich zur Farbe durch Gewicht, Kontur, Position oder Symbol erkennbar |
| `loading` | Platzhalter in realer Inhaltsgeometrie; kein Spinner als Ersatz für die gesamte Fläche |
| `empty` | benennt was fehlt, warum und die eine Aktion, die es behebt |
| nicht klickbar | kein Hover-Lift, kein Aktionszeiger und kein interaktiver Schatten |

Verboten sind dekorative Schwebezustände ohne Aktion, Cursor-Glow als generischer Ersatz für Hierarchie, Maßstabssprünge, die Nachbarlayout verschieben, und ein Kartenraster, das nur durch Einrahmen gewöhnlicher Absätze entsteht.

## Status, Tag und Chip

- Status enthält immer ein Wort oder anderes nicht-farbiges Merkmal. Punkt, Pille, Zeile oder Inline-Text sind Stilentscheidungen je Website.
- Ein **echter** Live-Zustand darf eine zurückhaltende, dokumentierte Bewegung tragen; ein statischer Zustand nie.
- Tags und Kategorien besitzen eine feste Ton-Zuordnung über alle Ansichten. Sie werden nicht automatisch als Pille oder in Mono gesetzt.
- Zähler und vergleichbare Werte nutzen tabellarische Ziffern. Eine Zahl ohne Bezugsgröße ist nach [[20-Design/Interface Benchmarks#B4 Data Product Depth]] keine Aussage.

## Kopfzeile und Hauptnavigation

Kanonische Funktions- und Geometrieregel für die Kopfzeile jeder Website. Inventar und Anordnung sind Teil der Art Direction und bei mehreren Websites eine Pflichtachse der Unterscheidungsmatrix.

- Vor UI-Code dokumentieren: sichtbare Elemente, Reihenfolge, Gruppierung, Positionierungsmodell, Höhe, Verhalten über den vorkommenden Untergründen, Mobile-Übergang und Navigationsbeschriftungen.
- **Höchstens sechs Navigationselemente** in der sichtbaren Hauptnavigation. Weitere Bedienelemente dürfen die Zeile nicht sprengen.
- **Nichts in der Kopfzeile ist zweizeilig.** Einzige Ausnahme ist eine bewusst mehrzeilige Wortmarke oder ein Logo.
- Die Kopfzeile wird bei **1280, 1440 und 1920 Pixel** sowie mit der längsten realen Beschriftung geprüft. Bei Platzmangel werden Inventar, Begriffe oder Informationsarchitektur überarbeitet.
- Kein Element darf höher sein als die nutzbare Innenhöhe der Kopfzeile. Oben und unten bleibt je mindestens `4px` echte Luft; eine projektbezogen größere Mindestluft steht im Design Contract.
- Ist ein Kindmaß über die Breite definiert, während die Kopfzeile über die Höhe begrenzt wird, muss das gerenderte Seitenverhältnis an jedem Prüfbreakpoint gemessen werden. Das gilt besonders für Wortmarken, Logos und quadratische Controls.
- Auf schmalen Flächen ersetzt eine zur jeweiligen Website passende Schublade, ein Sheet oder eine andere dokumentierte Lösung die Desktopanordnung. Fokusmanagement, Escape, Rückfokus und Scrollsperre bleiben Pflicht.
- Der aktive Punkt ist ohne Farbe allein erkennbar und trägt `aria-current="page"`.
- Jede Kopfzeile besitzt einen kontrastgeprüften Zustand über jedem Untergrund. Deckend, im Dokumentfluss, seitlich, aufgeteilt oder durchscheinend sind gleichwertige Art-Direction-Optionen.

### Option durchscheinende Kopfzeile

Nur wenn diese Form bewusst gewählt wurde:

- `position: sticky` oder eine begründete Alternative, teiltransparente Fläche, dokumentierter Blur und die in der Website gewählte Rahmenbehandlung;
- Kontrast gegen den ungünstigsten **tatsächlich darunterliegenden** Inhalt messen, nicht gegen eine angenommene Tokenfläche;
- deckender `@supports`-Fallback ohne `backdrop-filter`;
- über wechselndem Leitmedium deckend werden oder eine geprüfte Abdunkelung erhalten;
- Zustandswechsel dürfen die Höhe nicht ändern;
- die Mobile-Navigation ist deckend.

## Interaktionsregeln

- Link navigiert, Button löst Aktion aus.
- Native HTML-Controls bevorzugen; ARIA ergänzt Semantik, ersetzt sie nicht.
- Modal: Fokus hinein, innerhalb halten, Escape, verständlicher Titel, Rückfokus. WAI-ARIA APG als Verhaltensreferenz.[^apg]
- Destruktive Aktion: Folgen konkret benennen; Bestätigung proportional zum Schaden.
- Async-Aktion: Doppelausführung verhindern, Fortschritt anzeigen, Ergebnis melden, Retry anbieten.
- Optimistic UI nur bei sicher rückrollbarer, konfliktarmer Aktion.
- Pressable Controls haben ein sichtbares, schnelles Active-Feedback; Hover-Animationen nur auf geeigneten Zeigegeräten. Fokus bleibt davon unabhängig sichtbar.
- Popover und Tooltip dokumentieren Trigger, Origin, Enter/Exit, Escape und Rückfokus. Häufige Tastaturauslösung bleibt ohne verzögernde Animation.
- Eine Motion-Änderung darf DOM-Reihenfolge, Fokusreihenfolge oder Screenreader-Ansagen nicht verändern. Ihr Fallback gehört zum Komponentenvertrag.
- Jede Route-Komponente mit Scrollbewegung dokumentiert zudem Scroll-Range, Deep-Link-/Reload-Verhalten, Rückwärts-Scroll, Cleanup bei Routewechsel und Reduced-Motion-Komposition. Sie erfüllt den projektweiten Motion Inventory statt einen einzelnen Hero-Effekt zu isolieren.

## Forms

- Sichtbares Label, Zweck, Format und Required-Status.
- Serverseitige Validierung immer; clientseitig nur für schnelleres Feedback.
- Fehler neben Feld plus Summary; Eingaben erhalten; Fokus sinnvoll setzen.
- Keine Passwort- oder Namensregeln erfinden, die reale Nutzer ausschließen.

[^apg]: [W3C WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/)
