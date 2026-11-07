# Befund: 180-Grad-Produktbetrachter

Quelle: https://tutor-timer-28553736.figma.site/ · gemessen 2026-11-07 vom Nutzer in seinem Chrome über die Chrome-Erweiterung · Werte in `messung.json`.
Kennzeichnung: **[M]** gemessen, **[A]** abgeleitet oder geschätzt.

## Gemessen

- [M] Figma Make, React, Tailwind v4, shadcn/ui. Root-Schriftgröße 14 px, Systemschrift, Titel nicht größer als Fließtext.
- [M] Ziehen dreht stufenlos, 0,8° je Pixel (250 px → 200°, 50 px → 40°), modulo 360.
- [M] Acht benannte 45°-Stufen, Grenze ±22,5°. Drei Bilder: Front 315/0/45, Seite 90/135/270, Rücken 180/225. Wechsel hart per `src`.
- [M] Automatisch drehen ≈ 31,5°/s, eine Umdrehung ≈ 11,5 s; Knopf wird zu „Stop“ und gefüllt.
- [M] Zoom 50–200 % in 25er-Stufen, `scale()` mit 300 ms `cubic-bezier(0,0,.2,1)`.
- [M] Hover: Kachel nur Randfarbe, Knopf nur Grund, Segment weiß 50 %, je 150 ms `cubic-bezier(.4,0,.2,1)`. Kein Lift, kein Scale, keine Scrollanimation.
- [M] Layout: Steuerkarten 1/3 links, Bühne 2/3 rechts; unter 896 px Bühne zuerst.
- [M] Defekt: −45°, +45° und die Segmente wirken bei echten Klicks nicht. Die Farbwahl ändert das Bild nicht.

## Geschätzt

- [A] Taktung des automatischen Drehens intern unbekannt, nur die Geschwindigkeit ist gemessen.
- [A] Doppelklick setzt den Zoom zurück: nur laut Hinweistext.

## Übertragen in `web-kit/blocks/Produktansicht.astro`

Drehen per Ziehen, Stufen, harter Bildwechsel, Overlay mit Name und Grad, Segmentleiste, −45°/+45°, Drehen mit Anhalten, Zoom als Option, Farb- und Größenkacheln, Hover und Zeiten wie gemessen. Am 2026-11-07 im Nachbau nachgemessen: alle Werte stimmen.

## Bewusst anders

- Knöpfe und Segmente funktionieren.
- Schmal ist die Bühne quadratisch statt fest 600 px hoch; das Original lässt bei 390 px große Leerflächen.
- Tastatur (Pfeile, Pos1, Ende) und Wischen kommen dazu. Drehen entfällt bei reduzierter Bewegung.
- Hinweis auf der Bühne nur auf Wunsch; dauerhaft wirkt er unruhig.
- Nicht übernommen: Produktfotos und Marke, Entwicklerhinweis, Tailwind-Blau (dafür der Akzent des Presets).

## Screenshots

Das ZIP `figma-messung-screenshots-2026-11-07.zip` lag beim Ablegen nicht auf dem Server. Wenn es nachgeliefert wird, gehören die Bilder als WebP in `screenshots/`.
