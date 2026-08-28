---
type: canonical
status: canonical
updated: 2026-08-27
impacts:
  - design-tokens
  - components
  - responsive-tests
---

# Typography Layout and Spacing

## Grundhaltung

Typografie übersetzt Marke, Inhalt, Lesesituation und Bedienaufgabe. Neutral, expressiv, sachlich, humanistisch, technisch, historisch oder bewusst zeitgenössisch sind gleichwertige Richtungen. Verbindlich sind Lesbarkeit, passende Zeichenabdeckung, stabile Rollen, belastbare Webfonts und eine nachvollziehbare Herleitung.

## Stilzitat und Zeitbezug

Ein Zeitbezug ist eine Art-Direction-Entscheidung, kein globaler Fehler. Historische Serifen, kantige Displayschriften, Schreibmaschine, Terminal, Ornamente, Papier, Filmkorn oder gedeckte Erdtöne sind erlaubt, wenn sie aus Marke, Produkt, Ort, Publikum oder einer bewusst gewählten kulturellen Referenz entstehen.

Ein starkes Epochenzitat entsteht nicht erst durch eine einzelne Schrift. Sobald mehrere tragende Ebenen wie Displaytypografie, Grundfläche, Linien- oder Rahmenstil, Textur, Bildbehandlung und Seiten-Chrome gemeinsam eine vergangene Epoche simulieren, prägt es die gesamte Website. Diese Intensität ist eine Ausnahme: Sie braucht einen ausdrücklichen Nutzerwunsch oder einen Markenbezug, der ohne das Zitat verloren ginge. Ohne diesen Nachweis bleibt der Grundcharakter gegenwärtig und historische Typografie übernimmt eine klar begrenzte Rolle, etwa eine einzelne Auszeichnungsstufe. Stilabstand zwischen mehreren Fassungen ist kein ausreichender Grund.

Ein Befund entsteht, wenn das Stilzitat austauschbar ist, Lesbarkeit oder Vertrauen beschädigt, den Betrieb hinter der Epoche verschwinden lässt, nur dekorative Versatzstücke verwendet oder gegen die reale Marke arbeitet. Prüffragen: Welche konkrete Quelle trägt den Zeitbezug? Welche Rollen übernimmt er? Wie viele tragende Ebenen zitieren dieselbe Epoche? Würde die Website ohne Logo noch zu diesem Betrieb gehören? Ist das Zitat auch auf Mobilgerät, in Formularen und in langen Texten funktionsfähig? Wäre dieselbe Informationsstruktur in einer gegenwärtigen Ausprägung überzeugender?

## Schriftwahl

- **Primärschrift nach Aufgabe wählen.** Grotesk, Serif, Slab, Humanist, Mono, Displayfamilie oder Systemstack sind möglich. Für dichte Produkt-UI braucht die primäre Familie robuste Schnitte, Ziffern und kleine Größen; eine Marketingseite darf stärker über eine charaktervolle Displayrolle geführt werden.
- **Die Zweitschrift ist eine begründete Entscheidung je Website**, kein globaler Reflex. Ihr Contract benennt Familie, Rollen, Ausschlüsse und den Grund, warum die Primärschrift diese Aufgabe nicht übernimmt. Auch `keine Zweitschrift` ist eine gültige, zu dokumentierende Entscheidung.
- Eine Monospace ist besonders sinnvoll, wenn Zeichenbreite oder technischer Kontext Bedeutung tragen. Sie darf auch markenprägend eingesetzt werden, wenn längere Texte lesbar bleiben und die Rolle begründet ist; für tabellarische Zahlen genügen oft die OpenType-Ziffern der Primärschrift.
- Displayschriften mit starkem Eigencharakter erhalten die Rollen, in denen ihr Rhythmus und ihre Lesbarkeit funktionieren. Sie sind nicht pauschal auf eine einzige Stufe begrenzt.
- Die gewählte Familie muss mindestens Regular, Medium und Semibold sowie Ziffern in Tabellenform anbieten. Fehlt das, ist sie für Produkt-UI ungeeignet.
- Herkunft, Version, Lizenz und Downloaddatum jeder Schrift gehören in das [[80-Templates/Asset Register]].

## Typografie

- So wenige Familien wie nötig. Eine oder zwei reichen häufig; weitere sind zulässig, wenn jede eine stabile, wiederkehrende Rolle besitzt und Ladebudget sowie visuelle Kohärenz gewahrt bleiben.
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

- Tracking folgt Schrift, Größe, Sprache und gewünschtem Charakter. Große Grotesks profitieren oft von engerer Laufweite; andere Familien nicht. Fließtext wird auf Lesbarkeit statt auf eine globale Nullregel geprüft.
- Große Überschriften erhalten `text-wrap: balance`, Lead und Fließtext `text-wrap: pretty`, damit keine Einzelwortzeile entsteht.
- Der semantische Seitentitel bleibt vollständig sichtbar. `overflow: hidden`, Masken, Layer und klebende Kopfzeilen dürfen nur dekorative Duplikate beschneiden, nie die einzige lesbare H1. Für 320 und 375 Pixel, Desktop-Prüfbreiten, 200 Prozent Zoom und große Systemschrift wird die reale Zeilenanzahl dokumentiert; ein beabsichtigter Größensprung wird verkleinert, sobald Wörter kollidieren, verdeckt oder unlesbar werden.
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

- Tiefe kann durch Schatten, Überlagerung, Farbe, Maßstab, Unschärfe, Rahmen oder Weißraum entstehen. Das gewählte Mittel muss zur materiellen Logik der Website passen und darf Hierarchie nicht vortäuschen.
- Jede Website entscheidet Rahmenstärke, Ton, Vollständigkeit und Rhythmus als eigenes System. Ein Vollrahmen, nur horizontale Hairlines, geteilte Tabellenlinien oder bewusst rahmenlose Flächen sind unterschiedliche gültige Grammatiken.
- Schatten werden konsistent und mit klarer Rolle eingesetzt. Interaktive, überlagernde und bewusst objektartige ruhende Elemente dürfen unterschiedliche dokumentierte Tiefenstufen besitzen.
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
