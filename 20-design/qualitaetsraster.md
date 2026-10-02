---
type: canonical
status: canonical
updated: 2026-10-02
sources_checked: 2026-10-02
review_by: 2027-04-01
depends_on:
  - "[[20-design/landing-page-craft.md]]"
  - "[[20-design/anti-ai-slop.md]]"
  - "[[90-references/reference-research-workflow.md]]"
impacts:
  - "[[90-references/website-reference-pool.md]]"
  - "[[90-references/inspiration-catalog.md]]"
  - "[[20-design/visual-iteration-loop.md]]"
  - "[[70-qa/quality-gates.md]]"
---

# Qualitätsraster

> [!important] Rang
> Diese Notiz ist der kanonische Besitzer für die Frage, **woran man am Bild erkennt, dass bei einer Website jemand nachgedacht hat** — unabhängig vom Code. Sie liefert das Raster, mit dem fremde Websites für den Gattungsvergleich bewertet werden, und den Benchmarkvergleich, mit dem die eigene Website vor der Lieferung gegen die besten Seiten ihrer Gattung gehalten wird.
> Angrenzende Besitzer: [[20-design/anti-ai-slop.md]] für die harten Sperren und den Befundkatalog, [[20-design/landing-page-craft.md]] für Aufbau und Auftakt, [[90-references/reference-research-workflow.md]] für Suche, Aufnahme und Ablage.

## Warum es dieses Raster gibt

Bis Oktober 2026 hat das Brain Qualität fast nur über Regeln und Messungen gesichert: Kontrast, Rhythmus, Zustände, Typostufen. Vier Fassungen für die Trattoria Alberto haben alle diese Messungen bestanden und wurden vom Nutzer trotzdem als generiert erkannt. Der Vergleich mit realen Restaurantseiten, die er als gut empfand, zeigte den Grund: Die guten Seiten unterscheiden sich nicht in messbaren Werten, sondern darin, dass erkennbar **Entscheidungen** getroffen wurden — was weggelassen wird, was das Bild trägt, welcher eine Satz stehen bleibt.

Solche Entscheidungen lassen sich nicht aus Regeln ableiten, aber am Bild erkennen. Das Raster macht dieses Erkennen wiederholbar.

## Die zehn Kriterien

Jedes Kriterium wird am Screenshot bei 1440 und bei 390 Pixel beurteilt, mit **0, 1 oder 2** Punkten. Keine Codeansicht, keine Werkzeugmessung: Das Raster beschreibt, was ein Gast sieht.

| Nr. | Kriterium | 2 Punkte | 0 Punkte |
|---|---|---|---|
| K1 | **Das Bild trägt** | Professionelle, reale Fotografie oder Video des Betriebs ist das Erste, was man sieht: Menschen im Raum, der Raum in Betrieb, das Essen, die Arbeit | Stockbild, Schnappschuss als Hauptfläche, Bild als Dekoration neben Text, kein Bild |
| K2 | **Ein Satz statt Absätze** | Der Auftakt sagt in höchstens einem kurzen Satz, was dieses Haus ist, und der Satz besteht den [[#Namenstausch-Test]] | Werbefloskel, Begrüßung wie „Herzlich willkommen", Absatz im Auftakt |
| K3 | **Zurückhaltung** | Nichts auf der Fläche, das nur schmückt: keine Dachzeile, keine Nummernmarke, kein Ornament, keine Icon-Karte, keine Plakette ohne realen Beleg | mehrere Zierelemente je Bildschirmhöhe, Vorlagenmöbel, siehe [[20-design/anti-ai-slop.md#Harte Sperren]] |
| K4 | **Eine Hauptaktion** | Reservieren, Anrufen oder Bestellen ist überall erreichbar, sieht überall gleich aus und heißt überall gleich | zwei gleich starke Aktionen, wechselnde Benennung, Aktion nur in der Fußzeile |
| K5 | **Praktisches sofort** | Öffnungszeiten, Adresse und Telefon stehen in der ersten Bildschirmhöhe oder direkt danach, ruhig gesetzt | nur im Impressum, nur in einem Widget, nur als Fließtext versteckt |
| K6 | **Marke mit Haltung** | Logo oder Wortmarke wird selbstbewusst eingesetzt, eine erkennbare typografische Stimme, höchstens zwei Familien | Logo klein und verloren, drei und mehr Schriften, Standardschrift ohne Bezug |
| K7 | **Rhythmus** | Die Sektionen wechseln Maßstab und Anordnung: vollbreites Bild, Text allein, Bild-Text-Paar, Detail; keine zwei Sektionen hintereinander gleich gebaut | jede Sektion gleich aufgebaut, gleiche Fläche, gleiche Breite, siehe [[20-design/landing-page-craft.md#Sektionsrhythmus]] |
| K8 | **Serie** | Alle Bilder teilen Licht, Farbstimmung und Behandlung; sie sehen aus wie von einem Fotografen an einem Tag | gemischte Quellen, wechselnde Farbstimmung, Collage |
| K9 | **Eigenheit** | Mindestens ein Element, das nur dieses Haus haben kann: seine Menschen, sein Raum, seine Handschrift, ein Gericht mit Geschichte | alles austauschbar; die Seite funktioniert mit jedem anderen Namen |
| K10 | **Handwerk** | Saubere Fluchten, ruhige Abstände, mobil ohne Textwand und ohne Überlagerung, keine kaputten Zustände | Text klebt an Kanten, Widgets verdecken Inhalt, mobile Fassung ist eine gestauchte Desktopseite |

**Höchstwert 20.** Schwellen:

| Summe | Einstufung | Verwendung |
|---|---|---|
| 16 bis 20 | **Benchmark** | taugt als Maßstab und als Quelle übertragbarer Prinzipien |
| 13 bis 15 | **gut mit Mängeln** | einzelne Prinzipien übernehmen, die Mängel benennen |
| 9 bis 12 | **Mittelfeld** | nicht als Vorbild verwenden |
| 0 bis 8 | **Negativbeispiel** | zeigt, was zu vermeiden ist |

Ein einzelnes Kriterium mit 0 Punkten in K1, K3 oder K10 schließt die Einstufung als Benchmark aus, unabhängig von der Summe.

## Namenstausch-Test

Der Satz im Auftakt wird mit dem Namen eines beliebigen anderen Betriebs derselben Gattung in derselben Stadt gelesen. **Bleibt er wahr, ist er generisch.**

| Satz | Ergebnis |
|---|---|
| „Genießen Sie die Aromen des authentischen Italiens" | generisch, gilt für jede Pizzeria |
| „Herzlich willkommen" | generisch |
| „Fun Fine Dining in Charlottenburg" | trägt: Haltung und Ort |
| „Jeden Tag ein gedeckter Tisch in Kladow" | knapp bestanden über den Ort; ohne „Kladow" generisch |

Die Prüfung ist schnell und schließt die häufigste Schwäche generierter Startseiten aus: einen Satz, der schön klingt und nichts behauptet.

## Was die Benchmarks gemeinsam haben

Aus der Auswertung von zwanzig Restaurantseiten am 2. Oktober 2026, davon drei vom Nutzer benannt. Die Liste ist der verdichtete Befund, nicht das Raster selbst.

- **Das Foto ist die Gestaltung.** Die stärksten Seiten haben fast keine eigenen Gestaltungsmittel. Raum, Menschen und Essen tragen die Fläche; Typografie und Farbe treten zurück.
- **Der Auftakt ist ein Raum, kein Layout.** Eine einzige, volle Bildschirmhöhe zeigt den Ort in Betrieb, darauf ein Satz, darunter oder daneben die Praxis: Zeiten, Adresse, Reservieren.[^mine]
- **Weniger Sektionen, jede anders.** Wo es mehr als den Auftakt gibt, wechseln vollbreites Bild, Bild-Text-Paar und reiner Text. Keine Seite wiederholt dieselbe Anordnung dreimal.[^carbone]
- **Kein einziger Kicker.** Keine der als Benchmark eingestuften Seiten setzt eine Dachzeile über die Überschrift des Auftakts. Die als schwach eingestufte Seite tut es zweimal.[^impasto]
- **Der Name als Bild.** Die Wortmarke steht groß und ruhig; sie ersetzt jede gestaltete Überschrift.[^standard]

## Gattungsvergleich

Vor dem Design Contract jeder Website, auch einer einzelnen, wird die Gattung angesehen. Wie gesucht, aufgenommen und abgelegt wird, regelt [[90-references/reference-research-workflow.md#Gattungsvergleich]]. Diese Notiz liefert das Urteil:

1. Jede aufgenommene Seite wird nach den zehn Kriterien bewertet; die Punkte stehen mit je einem Satz Begründung im Projekt.
2. **Zwei bis drei Benchmarks** mit mindestens 16 Punkten werden benannt. Findet sich lokal und national keine, wird international gesucht.
3. **Ein bis zwei Negativbeispiele** derselben Gattung werden benannt. Sie sind genauso wichtig: Sie zeigen, wie die eigene Seite nicht aussehen darf.
4. Aus den Benchmarks werden die übertragbaren Prinzipien in Sätzen festgehalten, etwa „Auftakt ist ein Raumfoto über die volle Höhe, Zeiten und Adresse als Band darunter". Übernommen werden Prinzipien, nie Bilder, Texte, Logos oder Identitätsmerkmale.

## Benchmarkvergleich

Vor der Lieferung wird die eigene Website neben ihre Benchmarks und Negativbeispiele gelegt: Auftakt bei 1440 und 390 Pixel, dazu die ganze Startseite, auf gleiche Breite verkleinert, nebeneinander auf einem Bogen.

Drei Fragen, schriftlich beantwortet:

1. **Sieht die eigene Seite eher aus wie die Benchmarks oder wie die Negativbeispiele?** Wer das nicht eindeutig beantworten kann, hat die zweite Antwort.
2. **Wie viele Punkte erreicht die eigene Seite im Raster?** Unter 16 ist sie nicht lieferfertig; die fehlenden Kriterien werden benannt und behoben.
3. **Welche Entscheidung der Benchmarks fehlt hier noch?** Mindestens eine wird benannt, auch bei 16 Punkten und mehr.

Der Vergleich ersetzt keinen Renderdurchgang und keine Messung. Er ist die Prüfung, die Messungen nicht leisten: ob die Seite in derselben Liga spielt wie gute Seiten ihrer Gattung. Nachweis ist der Bogen samt Antworten im Projekt; ohne ihn ist `G1` nicht erfüllt.

**Rasterpunkte der eigenen Seite vergibt nicht nur der Agent.** Seine Bewertung ist ein Vorschlag. Stuft der Nutzer anders ein, gilt seine Einstufung, und der Unterschied wird als Erkenntnis im Brain festgehalten.

## Bildmaterial als Engpass

K1 und K8 lassen sich mit Schnappschüssen nicht erreichen. Liegt kein professionelles Fotomaterial vor, wird die Website trotzdem gebaut, mit dem besten verfügbaren Material, bearbeitet nach [[20-design/imagery-and-ai-editing.md]]. Zusätzlich steht im Release-Readiness-Register ein Eintrag der Priorität `P1`: Fotoshooting für Raum, Menschen und Essen. Bei Gastronomie ist das die wirksamste einzelne Verbesserung, die der Betrieb selbst beitragen kann; keine Gestaltung gleicht fehlende Fotografie aus.

[^mine]: [MINE Restaurant, Berlin](https://minerestaurant.de/): Video der Gäste im Raum über die volle Höhe, ein Satz, darunter Zeiten, letzte Bestellung und Adresse als Band. Geprüft am 2. Oktober 2026.
[^carbone]: [Carbone, New York](https://carbonenewyork.com/): wechselt vollbreites Bild, Bild-Text-Paare in beiden Richtungen und dunkle Textflächen, ohne eine Anordnung zu wiederholen. Geprüft am 2. Oktober 2026.
[^impasto]: [Impasto Rosso, Berlin](https://impastorosso.de/): Dachzeilen „Freut mich, Sie kennenzulernen" und „Melden Sie sich für unseren Newsletter an" über den Überschriften, dazu Ornamentlinien und Icon-Karten. Gemessen mit `web-kit/scripts/check-slop.ts` am 2. Oktober 2026.
[^standard]: [Standard Serious Pizza, Berlin](https://www.standard-berlin.de/): die Wortmarke über die volle Breite ist zugleich die Überschrift. Geprüft am 2. Oktober 2026.
