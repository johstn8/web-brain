---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - design-tokens
  - components
  - responsive-tests
---

# Typography Layout and Spacing

## Grundhaltung

Die Schrift ist modern und zeitgenössisch, nicht historisierend. Zielbild ist die neutrale, präzise Typografie aus [[20-Design/Interface Benchmarks]]: eine gut ausgebaute Grotesk, klare Gewichtsabstufung, ruhige Laufweite, keine Stilzitate.

## Retro-Verbot

Verbindlich für jede gebaute Website. Verboten ist die **Retro-Anmutung**, also Typografie, die eine vergangene Epoche zitiert, statt eine Haltung zu haben:

- kantige, technisch anmutende Displayschriften mit Achtziger- oder Neunziger-Zitat,
- alte Buch- und Systemserifen mit hoher x-Höhe und schwerem Duktus in der Rolle der Markenschrift, ausdrücklich einschließlich `Iowan Old Style` und typgleicher Familien,
- die Kombination aus solcher Serife und gedeckten Erdtönen, insbesondere Dunkelgrün, Oliv, Senf, Ziegel, Terracotta,
- Schreibmaschinen- und Terminaloptik ohne echten Systembezug, siehe [[20-Design/Anti AI Slop]],
- gesperrte Versalzeilen, Zierlinien, Ornamente, Badges im Vintage-Stil, gealterte Texturen, Papier- und Filmkorn als Grundstimmung.

Eine Serife an sich ist nicht verboten. Verboten ist die Kombination aus Serife, Erdton, Ornament und Nostalgiegeste, die zusammen einen Retro-Eindruck erzeugen. Eine zeitgenössische Serife auf klarer Neutralbasis mit moderner Farbwelt ist ausdrücklich erlaubt und oft die stärkere Wahl für redaktionelle Inhalte.

Prüffrage: Sieht die Seite aus, als sollte sie älter wirken, als sie ist? Dann wird die Schriftwahl ersetzt.

Die Ausnahme ist ein tatsächlicher, belegter historischer Bezug des Betriebs, etwa ein Gründungsjahr mit erhaltener Wortmarke oder ein Produkt, das aus der zitierten Zeit stammt. Die Herleitung wird dann im Design Contract benannt.

## Schriftwahl

- **Primär: eine variable Grotesk mit großem Gewichtsumfang.** Bewährt sind Inter, Geist, Satoshi, General Sans, Manrope, Söhne-nahe Familien sowie die Systemstacks. Sie tragen Auftakt, Oberfläche und Fließtext gleichermaßen.
- **Optional eine zweite Familie mit klarem Auftrag**, etwa eine zeitgenössische Serife für redaktionelle Lesestrecken oder eine Mono für Code, Werte und Tabellen. Nie mehr als zwei Familien plus eine Mono.
- Displayschriften mit starkem Eigencharakter sind erlaubt, wenn sie ausschließlich in der größten Stufe erscheinen und die Leseschrift neutral bleibt.
- Die gewählte Familie muss mindestens Regular, Medium und Semibold sowie Ziffern in Tabellenform anbieten. Fehlt das, ist sie für Produkt-UI ungeeignet.
- Herkunft, Version, Lizenz und Downloaddatum jeder Schrift gehören in das [[80-Templates/Asset Register]].

## Typografie

- Maximal eine Display- und eine Leseschrift; eine gute variable Familie reicht oft.
- Type Ramp definieren: Display, H1-H4, Lead, Body, Small, Label, Code.
- Für jede Stufe Größe, Zeilenhöhe, Gewicht, Letter-Spacing und Maximalbreite festlegen.
- Body meist 16px oder größer; Zeilenlänge grob 45 bis 75 Zeichen.
- Display-Schrift nie für lange Texte. All Caps nur kurz und mit ausreichendem Tracking.
- Fallback-Stack metrisch ähnlich wählen, um Layout Shift zu reduzieren.
- Schriften lokal und nur in benötigten Schnitten/Formaten ausliefern; Lizenz im Asset Register.

## Spacing

- 4- oder 8-Punkt-Basis; semantische Tokens wie `space-1` bis `space-12`.
- Optische Korrekturen sind erlaubt, aber als Token oder dokumentierte Ausnahme.
- Vertikaler Rhythmus: enger innerhalb einer Gruppe, deutlich größer zwischen Gruppen.
- Radiusfamilie auf wenige Stufen begrenzen; Pill nur für echte Chips, Tags oder kompakte Controls.
- Standard ist eine weich abgerundete, aber nicht verspielte Formsprache: eine Containerstufe um `12px` bis `14px`, eine kleinere Stufe für Controls, eine Pillstufe für Status. Diese drei Stufen gelten projektweit, siehe [[20-Design/Interface Benchmarks#Gemeinsamer Nenner]].
- Eine kontrollierte Schattenfamilie; Grenzen bevorzugen, wenn Tiefe keine Bedeutung trägt.

## Layout

- Containerbreiten und Seiten-Gutters als fluides Token, etwa mit `clamp()`.
- Grid explizit: Spalten, Gutter, Maximalbreite und Ausnahmen.
- Visuelle Ausrichtung an Textkanten, Baselines und gemeinsamen Achsen.
- Zentrierte Textblöcke nur kurz; lange Inhalte linksbündig.
- Content bestimmt Breakpoints, nicht Geräte-Namen.

Fontshare bietet freie Fonts, doch Lizenzbedingungen je Familie und Downloadzeitpunkt im Asset Register prüfen.[^fontshare]

[^fontshare]: [Fontshare](https://fontshare.com/)

