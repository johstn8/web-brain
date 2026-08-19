---
type: canonical
status: canonical
updated: 2026-08-19
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

Kanonische Funktions- und Geometrieregel für die Kopfzeile jeder Website. Inventar und Anordnung sind Teil der Art Direction und bei mehreren Websites eine Pflichtachse der Unterscheidungsmatrix. Es gibt weder eine globale Sollzahl noch eine vorgeschriebene Kopfzeilenform.

- Vor UI-Code dokumentieren: Nutzeraufgaben, sichtbare Elemente, Priorität, Reihenfolge, Gruppierung, Positionierungsmodell, Verhalten über den vorkommenden Untergründen, Responsive-Übergang und reale Navigationsbeschriftungen.
- Die Zahl sichtbarer Links folgt der Informationsarchitektur. Drei direkte Ziele können richtig sein, ebenso acht klar gruppierte Ziele, ein Mega-Menü, eine zweistöckige Utility-/Hauptnavigation, eine seitliche Navigation oder eine knappe Kopfzeile mit tiefem Footer. Kein Muster wird nur gewählt, um eine Zahl einzuhalten.
- Primäre, häufige Ziele bleiben direkt auffindbar. Seltene, rechtliche oder sekundäre Ziele dürfen in Untermenü, Utility-Bereich oder Fußbereich wechseln, wenn dies ihre Auffindbarkeit nicht verschlechtert.
- Einzeilige Navigation ist bei einer kompakten horizontalen Kopfzeile ein sinnvolles Ziel, aber kein globales Gesetz. Bewusst mehrzeilige, gestapelte oder umschaltende Konzepte brauchen klare Gruppen und dürfen nicht wie zufälliger Textumbruch aussehen.
- Geprüft wird an den projektbezogenen Breakpoints sowie mindestens bei 320, 375, 768, 1280 und 1920 Pixel mit den längsten realen Beschriftungen, 200 Prozent Zoom und großer Systemschrift. Kein Element wird abgeschnitten, überlagert ein anderes oder verliert seine erreichbare Zielgröße.
- Logo, Wortmarke und Controls behalten ihr Seitenverhältnis und eine zum Konzept passende Innenluft. Starre Höhen dürfen Inhalt nicht beschneiden.
- Auf schmalen Flächen darf die Desktopanordnung zu Schublade, Sheet, gestapeltem Index, Accordion, horizontalem Scroller oder einer anderen dokumentierten Lösung werden. Fokusmanagement, Escape, Rückfokus und Scrollsperre gelten, soweit das Muster sie benötigt.
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
