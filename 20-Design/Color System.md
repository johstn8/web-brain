---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - design-tokens
  - components
  - charts
  - accessibility-tests
---

# Color System

## Ablauf

1. Markenattribute in Farbrollen übersetzen.
2. Neutrale Skala für Flächen, Text und Grenzen festlegen.
3. Eine dominante Markenfarbe, optionale sekundäre Farbe und semantische Farben definieren.
4. Rollen statt Hex-Werte benennen: `surface`, `text`, `muted`, `border`, `accent`, `focus`, `success`, `warning`, `danger`.
5. Für jede Rolle Default, Hover, Active, Disabled und kontrastierende Inhaltsfarbe definieren.
6. Light und Dark Mode getrennt kuratieren, nicht invertieren.

## Harmonie

- Monochromatisch: ruhig, kohärent; braucht klare Helligkeitsstufen.
- Analog: weich und organisch; Akzentkontrast absichern.
- Komplementär: hohe Energie; eine Farbe dominant, die andere sparsam.
- Split-komplementär: lebendig mit geringerem Konflikt.
- Triadisch: nur bei ausdrucksstarker Marke und strenger Gewichtung.

60/30/10 ist ein Startpunkt, kein Gesetz. UI-Flächen brauchen meist deutlich mehr Neutralanteil.

## Kontrast und Bedeutung

- Normaltext mindestens 4,5:1; großer Text mindestens 3:1; UI-Komponenten und relevante Grafiken mindestens 3:1 für WCAG AA.[^wcag]
- Farbe nie als einziges Statussignal. Text, Icon, Muster oder Form ergänzen.
- Focus-Farbe auf allen angrenzenden Flächen testen.
- Kontrast mit realen Font-Schnitten, Transparenzen, Bildern und Zuständen testen.

## Verbrauchte Farbwelten

Diese Paletten sind durch generierte Websites so stark belegt, dass sie unabhängig von ihrer handwerklichen Qualität nach KI aussehen. Sie werden nicht als dominante Grundfläche verwendet:

| Verbrauchte Farbwelt | Warum sie auffällt | Besserer Weg |
|---|---|---|
| Beige, Creme, Sand, warmes Off-White als Hauptfläche | Standardausgabe vieler Generatoren für „hochwertig“ und „handgemacht“ | Neutralskala aus einem realen Material, Ort oder Produkt ableiten und leicht kühl oder klar setzen |
| Blau-Lila-Verlauf | Standard für „Technologie“ und „KI“ | eine dominante Markenfarbe mit belegter Herkunft, Verlauf nur wenn er etwas darstellt |
| Dunkelviolett mit Neon-Akzent | Standard für „Zukunft“ | dunkle Fläche mit genau einem Signalton aus dem Produkt |
| durchgehend saturiertes Pastell | Standard für „freundlich“ | klare Neutralbasis plus ein oder zwei kräftige Marken- und Signalfarben |
| gedecktes Dunkelgrün, Oliv, Senf, Ziegel oder Terracotta zusammen mit einer alten Buchserife | erzeugt eine Retro-Anmutung, die der Nutzer ausdrücklich ablehnt; siehe [[20-Design/Typography Layout and Spacing#Retro-Verbot]] | dieselbe Farbfamilie klar und kühl setzen und mit einer zeitgenössischen Grotesk kombinieren, oder eine Signalfarbe aus dem realen Gegenstand ableiten |

Wenn Marke, Material, Ort oder Produkt einen dieser Töne tatsächlich vorgeben, ist er erlaubt. Die Herleitung wird dann im Design Contract benannt. Ein Ton ohne solche Herleitung wird ersetzt.

## Farbverteilung in Produkt-UI

Für Oberflächen mit Daten, Listen, Status und Verwaltung gilt die Verteilung aus [[20-Design/Interface Benchmarks#B1 Soft Neutral Product Console]]: neutrale Fläche, Abgrenzung über Hairline, Farbe fast ausschließlich semantisch, eine einzige dunkle Signalfarbe für den aktiven Zustand, Kategorietöne nur als kleine Icon-Tints. Wo Farbe keine Bedeutung trägt, ist sie grau.

Grundhaltung: **modern, klar, übersichtlich.** Eine ruhige Neutralskala, eine dominante Markenfarbe mit belegter Herkunft, höchstens eine sekundäre Farbe und eindeutige semantische Farben. Farbe wird gezielt gesetzt, nicht flächendeckend gestreut.

## Anti-Slop

- Kein Blau-Lila-Verlauf, außer Marke und Inhalt begründen ihn.
- Keine Neon-Glows oder zufällige Gradient-Meshes als Ersatz für Art Direction.
- Farbfläche und Akzent gezielt einsetzen; nicht jede Sektion neu einfärben.
- Keine Farbe, die nur gewählt wurde, weil sie „hochwertig“ oder „modern“ wirkt. Jede Rolle hat eine benennbare Herleitung.

Tools wie Coolors können Varianten erzeugen, entscheiden aber nicht über Marke, Rollen oder Kontrast.[^coolors]

[^wcag]: [W3C: Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
[^coolors]: [Coolors](https://coolors.co/)

