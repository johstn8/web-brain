---
type: canonical
status: canonical
updated: 2026-08-08
depends_on:
  - "[[90-References/Inspiration Catalog]]"
impacts:
  - "[[20-Design/Design Direction]]"
  - "[[20-Design/Color System]]"
  - "[[20-Design/Typography Layout and Spacing]]"
  - "[[20-Design/Motion and Interaction]]"
  - "[[30-Frontend/Components and UI States]]"
  - "[[90-References/Derived Design Patterns]]"
---

# Interface Benchmarks

> [!important] Rang
> Diese Notiz ist die kanonische Beschreibung der vom Nutzer ausdrücklich als gut bewerteten Oberflächen. Sie steht bei visuellen Entscheidungen **über** allgemeinen Referenzmustern aus [[90-References/Derived Design Patterns]] und unter dem jeweiligen `PROJECT.md`. Die Belege dazu stehen in [[90-References/Inspiration Catalog#Vom Nutzer bewertete Benchmarks]].

Fünf Benchmarks, fünf Rollen. Jedes Web-Produkt wählt mindestens einen davon als Leitbenchmark und benennt ihn im Design Contract.

**B5 ist die Detailebene über allen anderen.** B1 bis B4 legen Haltung, Struktur und Rolle fest. B5 legt die handwerklichen Werte fest, mit denen diese Haltung tatsächlich gebaut wird: Tokens, Radien, Rahmen, Hoverrezepte, Bewegungswerte. Ein Build, der B1 bis B4 folgt, aber B5 ignoriert, sieht richtig konzipiert und trotzdem unfertig aus. Genau das war der Befund vom 8. August 2026.

## B1 Soft Neutral Product Console

**Rolle:** Grundhaltung für Oberflächen mit Daten, Listen, Status und Verwaltung. Höchste Priorität. Wenn nichts anderes im Auftrag steht, ist das die Standardanmutung für Anwendungs-UI.

Bezug: das vom Nutzer gelieferte Dashboard-Bild sowie das ATS-Dashboard, beide in [[90-References/Inspiration Catalog#Vom Nutzer bewertete Benchmarks]].

**Fläche und Farbe**

- Weiße bis fast weiße Grundfläche, ein einziger neutraler Grauton als Sekundärfläche. Kein Beige, keine Fläche mit Farbstich.
- Farbe erscheint fast ausschließlich semantisch: Grün für positive Veränderung und `Online`, Rot für Fehler, Gelb für Warnung.
- Zusätzliche Farbtöne nur als Kategoriemarker in Icon-Tints, etwa Blau, Grün, Violett, Orange bei je einem Kennzahlenfeld. Sie färben nie eine Fläche ein.
- Genau eine dunkle Signalfarbe für den aktiven Zustand, im Benchmark ein fast schwarzes Element.

**Struktur**

- Seitenleiste mit Produktmarke oben, darunter eine flache Navigationsliste aus Linienicon und Beschriftung. Der aktive Punkt ist eine gefüllte, dunkle, abgerundete Fläche mit heller Schrift; inaktive Punkte tragen keine Fläche.
- Inhaltsbereich beginnt mit Seitentitel und einer einzigen erklärenden Zeile in Grau. Kein Kicker darüber, siehe [[20-Design/Anti AI Slop#Kicker und Überschriften]].
- Kennzahlenreihe aus vier gleich breiten Feldern: Beschriftung und Icon in einer Zeile, darunter die große Zahl, darunter die Veränderung.
- Darunter zwei ungleich breite Blöcke nebeneinander, danach ein breiter Block über die volle Breite. Kein durchgehend gleichförmiges Kartenraster.

**Detailsprache**

- Ein Rahmen von einem Pixel in sehr niedrigem Kontrast trägt die Abgrenzung. Kein Schlagschatten, kein Verlauf, kein Glas.
- Eine einzige Radiusstufe für Container, ungefähr `12px` bis `14px`. Pillen nur für Statusanzeigen.
- Linienicons in einer Strichstärke. Icons sind klein und stehen nie größer als der Text, den sie begleiten.
- Fortschrittsbalken sind flach, wenige Pixel hoch, mit hellgrauer Spur und einer einzigen kräftigen Füllung. Beschriftung links, Wert rechts, beide über dem Balken.
- Listeneinträge bestehen aus rundem, sehr hell getöntem Icon-Träger, kräftiger Titelzeile und einer grauen Metazeile im Muster `Name · Zeitangabe`.
- Großzügiger Innenabstand in den Containern und deutlich sichtbare Abstände zwischen den Blöcken. Dichte entsteht durch Inhalt, nicht durch Zusammenrücken.

**Typografie:** eine neutrale, geometrisch geprägte Grotesk. Titel halbfett, Kennzahlen fett, Fließtext und Metazeilen normal in Grau. Keine Serifen, keine Versalzeilen als Dekoration.

**Motion:** klein und bestätigend. Zahlen dürfen beim ersten Sichtbarwerden einmal zählen, Balken einmal auf ihren Wert wachsen, Listen mit kurzem Versatz eintreten. Danach ist die Oberfläche ruhig.

## B2 Rounded Selection Configurator

**Rolle:** Leitbild für Produkt-, Varianten- und Größenauswahl sowie für jede Seite, deren Kern ein einzelnes Objekt ist.

Bezug: der 180-Grad-Produktbetrachter in [[90-References/Inspiration Catalog#Vom Nutzer bewertete Benchmarks]].

- Das Objekt steht freigestellt und groß auf einer hellen, neutralen Studiofläche, mit weichem Bodenschatten und ohne Rahmen. Es ist das Leitmedium der Seite, nicht eine Abbildung neben Text.
- Der Betrachter wechselt über benannte Ansichten. Die Bezeichnungen bleiben konkret, etwa `Vorderansicht links`, `Seitenansicht`, `Rückansicht`. Ein Zähler oder Punktindikator zeigt die Position in der Reihe.
- Bedienung über Ziehen, Wischen und Pfeiltasten. Jede Ansicht ist auch ohne Zeigegerät direkt anwählbar; der Betrachter ist nie die einzige Möglichkeit, alle Ansichten zu sehen.
- Auswahlelemente sind weich abgerundet: Größen als gleich große Felder mit deutlicher Radiusstufe, Farben als runde Felder mit sichtbarem Auswahlring. Der ausgewählte Zustand ist an Fläche und Kontrast erkennbar, nie nur an Farbe.
- Nicht verfügbare Optionen bleiben sichtbar, sind aber eindeutig als nicht wählbar markiert und benennen den Grund.
- Sekundäre Informationen wie Materialangabe, Pflegehinweis oder Größenhilfe liegen in einer kurzen, klar getrennten Detailliste, nicht in Fließtext.
- Übertragung auf Nicht-Produkte: Dieselbe Grammatik trägt Leistungspakete, Raumtypen, Termine, Modelle oder Ausstattungsvarianten. Gibt es nichts sinnvoll Wählbares, wird die Mechanik nicht erfunden. Dann bleibt vom Benchmark nur die weiche, abgerundete Formsprache auf heller Neutralfläche.

**Motion:** Die Ansichtsdrehung folgt der Eingabe unmittelbar und ist unterbrechbar. Auswahlwechsel bestätigen in unter 200 ms. Kein automatisches Dauerdrehen ohne Stoppmöglichkeit.

## B3 Full-Bleed Leitbild-Landing

**Rolle:** Auftakt für Dienstleister, Betriebe und Anlagen, deren Gegenstand fotografierbar ist.

Bezug: die Solarseite in [[90-References/Inspiration Catalog#Vom Nutzer bewertete Benchmarks]].

**Übernehmen**

- Ein einziges großes, randloses Leitbild trägt den Auftakt. Der Gegenstand des Betriebs ist darauf tatsächlich zu sehen: die Anlage, der Laden, das Fahrzeug, die Werkstatt, das Team bei der Arbeit.
- Genau eine kräftige Signalfarbe aus dem Gegenstand selbst gegen eine dunkle, entsättigte Grundfläche. Die Signalfarbe erscheint in Marke, primärer Aktion und wenigen Akzenten, nie flächig.
- Leistungen als kleine, klar benannte Gruppe statt als lange Liste. Vier bis sechs Einträge mit je einer Zeile Erklärung reichen.
- Eine kurze Nutzenüberschrift, ein erklärender Satz, eine primäre Aktion. Danach folgt Beweis.

**Nicht übernehmen**

- Die gesperrten Versalzeilen über den Sektionsüberschriften. Das sind Kicker und damit verboten.
- Erfundene Kennzahlen wie erzeugte Energie, abgeschlossene Projekte, Zufriedenheitsquote oder Jahre Erfahrung ohne Beleg, und ebenso erfundene Kundenstimmen mit Namen. Beides fällt unter [[10-Strategy/Content and Conversion#Beweis-Hierarchie]].
- Austauschbare Abschnittstexte, die zu jedem beliebigen Anbieter derselben Branche passen.

## B4 Data Product Depth

**Rolle:** Aufbau für Anwendungen, die Daten auswerten.

Bezug: das ATS-Dashboard in [[90-References/Inspiration Catalog#Vom Nutzer bewertete Benchmarks]].

- Jede Kennzahl wird eingeordnet: eigener Wert, Vergleichswert und benannter Zeitraum. Eine Zahl ohne Bezugsgröße ist keine Aussage.
- Kategorien erhalten je eine feste Farbe, die über alle Ansichten hinweg dieselbe bleibt. Farbe ist nie das einzige Unterscheidungsmerkmal; Beschriftung steht immer dabei.
- Leerzustände sind vollwertig gestaltet: Was fehlt, warum, und die eine Aktion, die es behebt.
- Einstellungen, Datenaufbewahrung, Export und Löschung sind sichtbare, echte Funktionen, keine Attrappen. Serverseitige Durchsetzung nach [[40-Backend-Security/Security Baseline]].
- Diagramme folgen den Regeln aus [[30-Frontend/Components and UI States]] und behalten eine textliche oder tabellarische Alternative.

## B5 Modern Neutral Craft Web

**Rolle:** Verbindliche Detail- und Handwerksebene für **jede** gebaute Website, unabhängig vom gewählten Leitbenchmark. Zusätzlich Leitbenchmark für Marketing-Landings, Portfolios, Verzeichnisse und inhaltsgetriebene Seiten.

Bezug: das Sieben-Seiten-Set in [[90-References/Inspiration Catalog#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]]. Vom Nutzer am 8. August 2026 ausdrücklich für Oberfläche, Bedienung, Animation und Kastengestaltung als Messlatte benannt und ausdrücklich **nicht** für Rechtstexte, Belege oder Inhaltswahrheit.

### Drei-Flächen-Regel

Alle sieben Referenzen arbeiten mit genau drei Helligkeitsstufen, nie mit mehr:

- **Seitengrund**, minimal abgesetzt gegen Weiß, im Beleg `#fafafa`.
- **Fläche** für Karten, Panels und Kopfzeile, im Beleg `#ffffff`.
- **Sekundärfläche** für eingebettete Bereiche, Codeblöcke und Leerzustände, im Beleg `#f5f5f5`.

Der Kontrast zwischen Grund und Fläche ist absichtlich sehr klein. Die Karte wird nicht durch ihre Füllung sichtbar, sondern durch ihren Hairline-Rahmen. Wer den Grund weiß und die Karte weiß setzt, verliert die gesamte Struktur; wer den Grund kräftig grau setzt, erzeugt das Kastenraster aus [[20-Design/Anti AI Slop]]. Kanonische Tokenwerte in [[20-Design/Color System#Tokenvertrag]].

### Rahmen als Hauptmittel, Tiefe als Ausnahme

- Jede abgegrenzte Fläche trägt genau **einen Pixel Rahmen** in sehr niedrigem Kontrast. Das ist projektweit die einzige Rahmenstärke.
- Es gibt **zwei** Rahmenstufen: die ruhende und eine deutlich sichtbarere für Hover, Fokus und ausgewählten Zustand. Im Beleg `#e5e5e5` gegen `#d4d4d4`, bei ClaudeFolio bis auf die Vordergrundfarbe hoch.
- **Im Ruhezustand trägt keine Fläche einen Schatten.** Tiefe ist ein Zustandssignal, kein Dekor.
- Ein weicher Hover-Schatten ist erlaubt, aber nur auf tatsächlich klickbaren Flächen, in genau einer Stufe, sehr flach und sehr transparent. Belegter Richtwert `0 8px 30px rgba(0,0,0,.06)`. Mehr als eine Schattenstufe pro Projekt ist ein Befund.
- Verläufe bleiben Flächen ohne Bedeutung verboten. Ein Verlauf darf ein reales Objekt, eine Lichtsituation oder einen Datenzustand darstellen, nie „Hochwertigkeit".

### Kastengestaltung

Das Kartenrezept mit allen Werten und Zuständen steht kanonisch in [[30-Frontend/Components and UI States#Kartenrezept]]. Als Haltung gilt hier:

- Eine Karte existiert, weil ihr Inhalt eine eigene, anklickbare oder eigenständig lesbare Einheit ist. Sie existiert nie, weil ein Absatz eine Umrandung braucht.
- Innerhalb einer Karte gibt es eine klare Reihenfolge: Medium oder Icon, Titel, eine Zeile Erklärung, darunter eine Metazeile in gedeckter Farbe, darunter höchstens eine Aktion.
- Die Metazeile trennt mit `·` und bleibt einzeilig. Werte, Tags und Zahlen stehen in der Mono-Schrift nach [[20-Design/Typography Layout and Spacing#Schriftwahl]].
- Bildflächen in Karten sitzen randlos an der Oberkante mit nur oben gerundeten Ecken und einem festen Seitenverhältnis, im Beleg `16/9`. Kein Rahmen zwischen Bild und Kartenrand.
- Innenabstand ist großzügig und projektweit identisch. Dichte entsteht über Inhalt, nicht über engere Polster.

### Bedienung und Zustand

- Die Kopfzeile ist durchscheinend mit Blur, hat aber einen geprüften Kontrast und einen deckenden Fallback. Rezept in [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]].
- Klickbare Karten heben beim Hover um ein bis zwei Pixel und hellen gleichzeitig ihren Rahmen auf. Werte in [[20-Design/Motion and Interaction#Standardrezepte mit Werten]].
- Status wird als Pille mit Punkt gezeigt, nicht als Farbfläche. Ein echter Live-Zustand darf einen atmenden Ring tragen; ein statischer Zustand nie.
- Tags und Kategorien sind Pillen aus dem Kategorieton bei sehr niedriger Deckung mit demselben Ton als Schriftfarbe. Der Ton färbt nie eine Sektionsfläche.
- Linienicons in einer einzigen Strichstärke und nie größer als der Text, den sie begleiten.

### Motion

- Bewegung ist kurz, gerichtet und in der Fläche verankert. Der Standard-Reveal ist ein Aufstieg über zwölf Pixel mit Opazität in etwa 500 Millisekunden, `ease-out`, mit gehaltenem Endzustand.
- Der Auftakt einer Seite darf einen zeichen- oder wortweisen Aufbau mit Unschärfe tragen. Er blockiert die primäre Aktion nicht.
- Dekorative Hintergründe werden weich ausmaskiert, nicht hart beschnitten.
- Alle Werte kanonisch in [[20-Design/Motion and Interaction#Standardrezepte mit Werten]].

### Was aus diesem Set nicht übernommen wird

Verlaufstext aus Indigo, Violett und Pink; Emojis als Sektionszeichen; Verlaufsflächen als Bildersatz; jede Sektion als gleichförmiges Kartenraster; alles Rechtliche und alle Kennzahlen. Begründung und Belege in [[90-References/Inspiration Catalog#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]].

## Gemeinsamer Nenner

Was alle fünf Benchmarks teilen und was deshalb bei jedem Build gilt:

1. Helle, entsättigte Neutralbasis oder eine bewusst dunkle, entsättigte Fläche. Nie eine Grundfläche mit Beige-, Creme- oder Verlaufscharakter.
2. Eine Radiusfamilie mit den vier Stufen aus [[20-Design/Typography Layout and Spacing#Radiusskala]], eine Rahmenstärke, eine Iconstrichstärke im gesamten Produkt.
3. Abgrenzung über Hairline und Weißraum. Im Ruhezustand kein Schatten und kein bedeutungsloser Verlauf. Ein einziger flacher Hover-Schatten auf klickbaren Flächen ist nach B5 erlaubt; in B1 bleibt die Oberfläche vollständig schattenfrei.
4. Farbe trägt Bedeutung. Wo sie keine trägt, ist sie grau.
5. Ein Objekt, ein Bild oder eine echte Oberfläche steht im Mittelpunkt, nicht eine Anordnung von Karten.
6. Kurze, konkrete Beschriftungen. Erklärung genau eine Zeile lang.
7. Der ausgewählte, aktive oder aktuelle Zustand ist immer eindeutig und ohne Farbunterscheidung erkennbar.

## Anwendung

Im Design Contract wird festgehalten:

- gewählter Leitbenchmark und Begründung,
- konkret übernommene Elemente je Benchmark,
- ausdrücklich nicht übernommene Elemente, insbesondere die Kicker und die erfundenen Belege aus B3 und die nicht übernommenen Muster aus B5,
- Abweichungen mit inhaltlicher Begründung.

B5 wird nicht gewählt, sondern gilt immer. Der Design Contract belegt für B5 die tatsächlich gesetzten Tokenwerte, die vier Radiusstufen, die zwei Rahmenstufen, die eine Schattenstufe und die Bewegungswerte. Ein Contract ohne diese Zahlen ist unvollständig.
