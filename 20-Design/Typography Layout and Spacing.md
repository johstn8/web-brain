---
type: canonical
status: canonical
updated: 2026-08-17
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
- **Die Zweitschrift ist eine begründete Entscheidung je Website**, kein globaler Reflex. Ihr Contract benennt Familie, Rollen, Ausschlüsse und den Grund, warum die Primärschrift diese Aufgabe nicht übernimmt. Auch `keine Zweitschrift` ist eine gültige, zu dokumentierende Entscheidung.
- Eine Monospace ist nur sachlich, wenn Zeichenbreite oder technischer Kontext Bedeutung tragen, etwa Code, Terminalausgabe, Tastenkürzel, IDs oder spaltenweise vergleichbare Zahlen. Sie ist sachlich falsch für Anschriften, Fließtext, Sektionstitel, Öffnungszeiten in Prosa und dekorative Abschnittsnummern. Reine Zahlen werden mit tabellarischen Ziffern der Primärschrift gesetzt, sofern kein technischer Grund für Mono besteht.
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

### Kalibrierte Type Ramp

Ausgangswerte, belegt in [[90-References/Inspiration Catalog#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]]. Sie werden übernommen, wenn keine Markenentscheidung dagegen steht.

| Stufe | Größe | Zeilenhöhe | Gewicht | Tracking |
|---|---|---|---|---|
| Display | `clamp(2.5rem, 6vw, 4.5rem)` | `1` | 600 bis 700 | `-0.03em` |
| H1 | `clamp(2rem, 4vw, 3rem)` | `1.05` bis `1.1` | 600 | `-0.025em` |
| H2 | `1.875rem` | `1.2` | 600 | `-0.025em` |
| H3 | `1.25rem` | `1.4` | 600 | `-0.015em` |
| Lead | `1.125rem` | `1.6` | 400 | `0` |
| Body | `1rem` | `1.6` bis `1.625` | 400 | `0` |
| Small | `0.875rem` | `1.45` | 400 bis 500 | `0` |
| Label, Metazeile | `0.75rem` | `1.35` | 500 | `0` bis `0.01em` |

- **Negatives Tracking gehört zu großen Stufen und nur dorthin.** Ab etwa `1.25rem` aufwärts wird enger gesetzt, Fließtext und Beschriftung nie. Das ist der Unterschied zwischen einer gesetzten und einer voreingestellten Überschrift.
- Große Überschriften erhalten `text-wrap: balance`, Lead und Fließtext `text-wrap: pretty`, damit keine Einzelwortzeile entsteht.
- Eine gewählte Mono-Familie trägt ausschließlich die im Website-Contract benannten technischen Rollen. `JetBrains Mono` ist ein belegtes Beispiel aus B5, kein Standard. Tags, Adressen, Uhrzeiten, Sektionsnummern und Metazeilen wechseln nicht automatisch in Mono.
- Ziffern in tabellarischer Form für jede Zahl, die sich ändert oder untereinander steht; dafür genügen meist die OpenType-Ziffern der Primärschrift.
- Eine Serifen-Zweitfamilie ist erlaubt und wird dann für genau eine Rolle eingesetzt, etwa den Auftaktsatz oder redaktionelle Lesestrecken. Bei Consile belegt für die Auftaktzeile.

## Spacing

- 4-Punkt-Basis; semantische Tokens wie `space-1` bis `space-12`.
- Optische Korrekturen sind erlaubt, aber als Token oder dokumentierte Ausnahme.
- Vertikaler Rhythmus: enger innerhalb einer Gruppe, deutlich größer zwischen Gruppen.

## Radiusskala und Rahmenbehandlung

Radius und Rahmen gehören zur variablen Stilebene. Vor der ersten Komponente legt jede Website ihr eigenes System fest und verwendet es danach konsistent. Zulässig sind etwa:

| System | Beispiel | Einsatz |
|---|---|---|
| kantig | `0` oder eine minimale Stufe | technische, editoriale oder konstruktive Richtung |
| kompakt | zwei Stufen für Controls und Container | ruhige, zeilenbasierte Oberflächen |
| abgestuft | drei bis vier benannte Stufen | weiche Produkt- oder B5-Richtung |
| objektbezogen | Radien aus Logo, Produkt oder realem Material | markengebundene Formsprache |

- Keine frei driftenden Einzelwerte: Jede verwendete Rundung gehört zu einer benannten Stufe oder ist eine dokumentierte optische Korrektur.
- Verschachtelte Flächen leiten ihre Innenform aus der Außenform und dem Innenabstand ab.
- Pillen sind nur eine Option für Status, Tags oder kompakte Umschalter. Sie sind kein Standard für primäre Aktionen.
- Die B5-Kalibrierung `6–8px / 10–12px / 16–20px / 9999px` darf übernommen werden, wenn B5 für diese Website gewählt wurde. Sie gilt nicht projektübergreifend.

## Tiefe und Rahmen

- Ruhende Inhaltsflächen tragen nach [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]] keinen dekorativen Schatten. Abgrenzung entsteht zuerst durch Hierarchie, Weißraum und bei Bedarf Hairlines.
- Jede Website entscheidet Rahmenstärke, Ton, Vollständigkeit und Rhythmus als eigenes System. Ein Vollrahmen, nur horizontale Hairlines, geteilte Tabellenlinien oder bewusst rahmenlose Flächen sind unterschiedliche gültige Grammatiken.
- Hover-, Fokus- und Ebenenschatten werden sparsam, konsistent und nur an interaktiven oder tatsächlich überlagernden Elementen eingesetzt. Anzahl und Werte stehen im Website-Contract.
- Für B1 bleibt die Oberfläche vollständig schattenfrei. Wer B5 wählt, kann dessen einen flachen Hover-Schatten und Ein-Pixel-Rahmen übernehmen.
- Fokus bleibt unabhängig von der gewählten Rahmenbehandlung eindeutig sichtbar und kontrastiert gegen jede tatsächlich vorkommende Fläche.

## Layout

- Containerbreiten und Seiten-Gutters als fluides Token, etwa mit `clamp()`. Belegte Ausgangswerte: Inhaltsbreite `64rem` bis `80rem`, Lesestrecke `42rem` bis `48rem`, Seitenpolster `clamp(1rem, 5vw, 2rem)`.
- Sektionspolster fluide und großzügig, Richtwert `clamp(4rem, 10vw, 8rem)` oben und unten. Der Abstand zwischen zwei Sektionen ist deutlich größer als jeder Abstand innerhalb einer Sektion. Bei Phillip Ohren und EVE BCN ist dieser Weißraum das einzige Trennmittel zwischen den Abschnitten; er ersetzt Trennlinien und Flächenwechsel.
- Grid explizit: Spalten, Gutter, Maximalbreite und Ausnahmen. Kartenraster halten einen Gutter aus derselben Spacing-Skala, Richtwert `1rem` bis `1.5rem`.
- Visuelle Ausrichtung an Textkanten, Baselines und gemeinsamen Achsen.
- Zentrierte Textblöcke nur kurz; lange Inhalte linksbündig.
- Content bestimmt Breakpoints, nicht Geräte-Namen.

Fontshare bietet freie Fonts, doch Lizenzbedingungen je Familie und Downloadzeitpunkt im Asset Register prüfen.[^fontshare]

[^fontshare]: [Fontshare](https://fontshare.com/)

