---
type: canonical
status: canonical
updated: 2026-08-06
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
