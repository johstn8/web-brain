---
type: canonical
status: canonical
updated: 2026-08-08
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

## Kartenrezept

Kanonisch für jede abgegrenzte Inhaltsfläche. Werte belegt in [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]]. Tokens nach [[20-Design/Color System#Tokenvertrag]], Radien nach [[20-Design/Typography Layout and Spacing#Radiusskala]].

**Wann eine Karte entsteht**

Eine Karte ist berechtigt, wenn ihr Inhalt eine eigenständig lesbare oder anklickbare Einheit ist: ein Projekt, ein Beitrag, ein Angebot, eine Kennzahl, ein Listeneintrag. Ein Absatz, eine Leistungsaufzählung oder ein Zitat wird nicht eingerahmt, sondern typografisch gesetzt. Das Verbot des gleichförmigen Kartenrasters aus [[20-Design/Anti AI Slop]] bleibt bindend: Das Rezept beschreibt, wie eine Karte aussieht, nicht wie viele es geben darf.

**Ruhezustand**

- Fläche `surface`, ein Pixel Rahmen in `border`, Radius `radius-card`, kein Schatten.
- Innenabstand projektweit identisch, Richtwert `1.25rem` bis `1.5rem`. Bildflächen sitzen randlos an der Oberkante, nur oben gerundet, mit festem Seitenverhältnis.
- Inhaltsreihenfolge: Medium oder Icon, Titel in `text`, genau eine Erklärzeile in `text-secondary`, Metazeile in `text-tertiary` im Muster `Wert · Wert`, höchstens eine Aktion.
- Tags als Pillen in `accent-subtle` oder im Kategorieton bei niedriger Deckung, Schrift im selben Ton, Mono, Stufe Label.

**Zustände**

| Zustand | Verhalten |
|---|---|
| `hover` bei `hover: hover` und `pointer: fine` | Rahmen wechselt auf `border-hover`, Verschiebung `translateY(-1px)` bis `-2px`, optional die einzige Schattenstufe. Übergang `transition: border-color, box-shadow, transform 150ms cubic-bezier(0,0,.2,1)`. Nur auf klickbaren Karten. |
| `focus-visible` | sichtbarer Fokusring in `focus` mit Offset. Der Ring ist unabhängig vom Hover und wird nie durch ihn ersetzt. |
| `active` | `scale(0.98)` oder Rücknahme der Verschiebung auf null, unter 160 Millisekunden. |
| `selected` oder `aria-current` | Rahmen `border-hover` oder `accent`, Fläche `accent-subtle`, zusätzlich ein Merkmal ohne Farbe, etwa Gewicht oder Häkchen. |
| `loading` | Platzhalterflächen in `surface-alt` in der realen Textgeometrie, optional eine wandernde Aufhellung. Kein Spinner in der Kartenmitte. |
| `empty` | benennt was fehlt, warum, und die eine Aktion, die es behebt. |
| nicht klickbar | kein Hover-Lift, kein Schatten, kein Zeigerwechsel. |

**Verboten**

Mehr als eine Schattenstufe, Maßstabssprünge über `1.02`, Rotation, Cursor-Glow, farbiger Rand als Dauerzustand, Verlauf als Kartenfüllung ohne Bedeutung, sowie ein Hover-Lift auf einer Fläche, die nichts auslöst.

## Statuspille, Tag und Chip

- Statuspille: Radius `radius-pill`, Fläche in der semantischen `-subtle`-Tönung, sechs bis acht Pixel Punkt in der Vollfarbe, danach das Wort. Farbe ist nie das einzige Signal; das Wort steht immer da.
- Ein **echter** Live-Zustand darf einen atmenden Ring tragen: `box-shadow` wächst von drei auf sechs Pixel bei sehr niedriger Deckung und zurück, Dauer zwei Sekunden, unendlich. Ein statischer Zustand bekommt diesen Ring nicht. Werte in [[20-Design/Motion and Interaction#Standardrezepte mit Werten]].
- Tags und Kategorien tragen eine feste Ton-Zuordnung über alle Ansichten hinweg, in Mono, Stufe Label, mit Beschriftung. Der Ton färbt nie eine Sektionsfläche.
- Zähler und Werte in tabellarischen Ziffern. Ein Zähler ohne Bezugsgröße ist nach [[20-Design/Interface Benchmarks#B4 Data Product Depth]] keine Aussage.

## Kopfzeile und Hauptnavigation

Kanonische Regel für die Kopfzeile jeder Website. Sie gilt für alle Breakpoints, in denen die Navigation ausgeschrieben sichtbar ist.

- **Höchstens sechs Navigationselemente** in der sichtbaren Hauptnavigation. Logo, Handlungsknopf, Telefonnummer, Sprach- oder Themenumschalter zählen nicht zu diesen sechs, dürfen aber die Zeile nicht sprengen.
- **Nichts in der Kopfzeile ist zweizeilig.** Kein Navigationslink, kein Knopf, kein Label bricht um. Einzige Ausnahme ist eine Wortmarke oder ein Logo, das gestalterisch bewusst zweizeilig gesetzt ist.
- Die Kopfzeile wird bei **1280, 1440 und 1920 Pixel** sowie mit der längsten realen Beschriftung geprüft. Wer das nicht ohne Umbruch schafft, kürzt die Beschriftungen oder reduziert die Zahl der Punkte, statt Abstände immer weiter zu verkleinern.
- Reichen sechs Punkte nicht aus, wird die Informationsarchitektur nach [[10-Strategy/Information Architecture and Sitemap]] verdichtet: verwandte Seiten unter einem Oberbegriff bündeln, seltene Ziele in den Fußbereich, Rechtsseiten immer in den Fußbereich.
- Kurzformen sind erlaubt, wenn sie eindeutig bleiben und der vollständige Seitenname in Schublade, Fußbereich und Brotkrumen erscheint.
- Auf schmalen Flächen ersetzt eine Schublade die Zeile. Sie hält den Fokus, schließt mit Escape, gibt den Fokus an den Auslöser zurück und sperrt den Hintergrundscroll.
- Der aktive Punkt ist ohne Farbe allein erkennbar, etwa über Unterstrich, Gewicht oder Position, und trägt `aria-current="page"`.
- Die Kopfzeile hat einen definierten Zustand über jedem Untergrund. Eine durchscheinende Leiste über wechselndem Medium braucht eine geprüfte Kontrastlösung, sonst wird sie deckend.

### Rezept der durchscheinenden Kopfzeile

Alle sieben Referenzen aus [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]] setzen die Kopfzeile so um. Sie ist damit der Standard, nicht die Ausnahme.

- `position: sticky` am oberen Rand, Fläche `surface` bei 70 bis 80 Prozent Deckung, `backdrop-filter: blur(8px)` bis `blur(24px)`, unten ein Pixel `border`.
- **Der Kontrast wird gegen den ungünstigsten tatsächlich darunterliegenden Inhalt gemessen**, nicht gegen die Fläche allein. Jeder Text und jedes Icon in der Leiste erreicht mindestens 4,5:1, Controls mindestens 3:1.
- Ohne Unterstützung für `backdrop-filter` wird die Leiste deckend. Das ist der Pflicht-Fallback über `@supports`, keine Kür.
- Über einem großen Leitmedium wird die Leiste entweder deckend oder erhält eine geprüfte Abdunkelung. Eine transparente Navigation über wechselndem Medium ohne solche Lösung ist ein Befund nach [[20-Design/Anti AI Slop]].
- Der Wechsel von transparent nach deckend beim Scrollen ist erlaubt, dauert 150 bis 200 Millisekunden und ändert dabei die Höhe der Leiste nicht.
- Auf schmalen Flächen sperrt die Schublade den Hintergrundscroll, hält den Fokus und schließt mit Escape. Sie ist deckend, nicht durchscheinend.

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
