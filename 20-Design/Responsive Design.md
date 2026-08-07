---
type: canonical
status: canonical
updated: 2026-08-05
---

# Responsive Design

## Prinzip

Responsive bedeutet gleichwertige Aufgabe auf kleinem, großem, gezoomtem und ungewöhnlichem Viewport. Kein Desktop-Layout nur stapeln.

## Regeln

- Mit schmalstem sinnvollen Viewport beginnen; dann erweitern.
- Reflow bei 320 CSS-Pixeln ohne Informations- oder Funktionsverlust anstreben.[^wcag]
- Fluid Type, Gaps und Container mit sinnvollen Min-/Max-Werten.
- Keine Interaktion ausschließlich über Hover. Touch-Ziele und Abstände einplanen.
- Tabellen: echte Tabelle erhalten, horizontaler Scrollbereich mit Hinweis oder passende alternative Ansicht.
- Navigation: Fokusreihenfolge, Escape, Scroll-Lock und Rückfokus testen.
- Medien mit `width`/`height` oder `aspect-ratio`; `srcset`/`sizes`; art direction nur bei inhaltlichem Bedarf.
- 3D, große Videos und Partikel: vereinfachter Mobile- und Low-Power-Fallback.
- Landscape, Zoom 200/400 Prozent, große Schrift, lange Übersetzungen und Soft Keyboard testen.

## Viewport-Matrix

Mindestens 320, 375, 768, 1024, 1440 CSS-Pixel sowie eine reale Touch-Prüfung. Breakpoints werden dort gesetzt, wo Inhalt bricht.

Für die hohe Motion-Dichte jede Scrollsequenz pro Breakpoint separat choreografieren und testen. Desktop-Pinning, Parallax oder horizontale Strecken werden auf schmalen Displays in eine ebenso inhaltsreiche vertikale oder statische Reihenfolge übersetzt; die Desktopsequenz wird nicht blind verkleinert.

[^wcag]: [W3C WCAG 2.2, Reflow und vollständige Seitenvarianten](https://www.w3.org/TR/WCAG22/)
