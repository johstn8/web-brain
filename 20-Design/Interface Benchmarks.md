---
type: canonical
status: canonical
updated: 2026-08-17
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

Fünf Benchmarks, fünf Rollen. Jede gebaute Website wählt mindestens einen davon als Leitbenchmark und benennt ihn in ihrem eigenen Design Contract.

## H0 Handwerksuntergrenze

H0 ist kein Look und kein sechster Benchmark. Die Untergrenze gilt für jede Website, ohne ihr eine gemeinsame Art Direction aufzuzwingen:

- anwendbare Komponenten besitzen vollständige Zustände einschließlich `focus-visible`, Laden, Fehler, Leerzustand und deaktiviert;
- Text, Icons, Controls und Fokus erreichen ihren erforderlichen Kontrast in der tatsächlich gerenderten Kombination aus Variante und Untergrund;
- ruhende Inhaltsflächen tragen keinen dekorativen Schatten; Abgrenzung entsteht zuerst durch Weißraum, Typografie und bei Bedarf eine Hairline;
- Tokens, Typografie, Spacing, Radius-, Rahmen-, Flächen-, Tiefen- und Motionentscheidungen bilden **innerhalb einer Website** ein konsistentes System;
- Interaktion bleibt per Tastatur, Touch und Zeigegerät verständlich, Reduced Motion erhält die Information und kein visueller Effekt blockiert Inhalt oder primäre Aktion;
- eine echte Darstellung an den Prüfbreiten ist Teil der Abnahme. Nicht renderbare UI ist ein Blocker nach [[70-QA/Quality Gates]], kein ersatzweise bestandener Textscan.

Die frühere B5-Regel vermischte diese Handwerksuntergrenze mit einem fertigen Stil. Künftig gilt folgende Zuordnung:

| Aussage aus dem früheren B5 | Ebene ab jetzt |
|---|---|
| Zustandsvollständigkeit, sichtbarer Fokus, Kontrast im Kontext, kein Schatten auf ruhenden Inhaltsflächen, Hairline als mögliches Abgrenzungsmittel, interne Systemkonsistenz | **H0, immer verbindlich** |
| Anzahl und Abstand der Flächenstufen, Radiusanzahl und -werte, genaue Rahmenbehandlung, Hover-Lift, Kartenaufbau, Kopfzeilenaufbau, Mono-Familie und ihre Rollen, Metazeilentrenner, genaue Reveal- und Bewegungswerte | **Stilebene, je Website zu entscheiden** |

Ein Build ist nicht deshalb handwerklich schwächer, weil er kantig statt weich, zeilen- statt kartenbasiert, deckend statt durchscheinend oder ohne Monospace gestaltet ist. Schwach ist er, wenn seine gewählte Grammatik inkonsistent oder in realen Zuständen unlesbar und unbedienbar wird.

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

**Rolle:** Wählbares Stilprofil für Marketing-Landings, Portfolios, Verzeichnisse und inhaltsgetriebene Seiten. B5 ist nicht die allgemeine Handwerksuntergrenze. Nur eine Website, die B5 als Leit- oder Zusatzbenchmark wählt, übernimmt seine konkrete Formsprache.

Bezug: das Sieben-Seiten-Set in [[90-References/Inspiration Catalog#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]]. Vom Nutzer am 8. August 2026 ausdrücklich für Oberfläche, Bedienung, Animation und Kastengestaltung als Messlatte benannt und ausdrücklich **nicht** für Rechtstexte, Belege oder Inhaltswahrheit.

### Flächenlogik des Stilprofils

Die sieben Referenzen arbeiten mit drei nahen Helligkeitsstufen:

- **Seitengrund**, minimal abgesetzt gegen Weiß, im Beleg `#fafafa`.
- **Fläche** für Karten, Panels und Kopfzeile, im Beleg `#ffffff`.
- **Sekundärfläche** für eingebettete Bereiche, Codeblöcke und Leerzustände, im Beleg `#f5f5f5`.

Der Kontrast zwischen Grund und Fläche ist absichtlich sehr klein. Die Karte wird nicht durch ihre Füllung sichtbar, sondern durch ihren Hairline-Rahmen. Das ist ein B5-Merkmal, keine Pflicht für eine andere Art Direction. Kanonische Rollen, nicht diese konkrete Helligkeitslogik, stehen in [[20-Design/Color System#Tokenvertrag]].

### Rahmen als Hauptmittel, Tiefe als Ausnahme

- Jede abgegrenzte Fläche trägt genau **einen Pixel Rahmen** in sehr niedrigem Kontrast. Innerhalb einer B5-Website ist dies die einzige Rahmenstärke.
- Es gibt **zwei** Rahmenstufen: die ruhende und eine deutlich sichtbarere für Hover, Fokus und ausgewählten Zustand. Im Beleg `#e5e5e5` gegen `#d4d4d4`, bei ClaudeFolio bis auf die Vordergrundfarbe hoch.
- **Im Ruhezustand trägt keine Fläche einen Schatten.** Tiefe ist ein Zustandssignal, kein Dekor.
- Ein weicher Hover-Schatten ist erlaubt, aber nur auf tatsächlich klickbaren Flächen, in genau einer Stufe, sehr flach und sehr transparent. Belegter Richtwert `0 8px 30px rgba(0,0,0,.06)`. Mehr als eine Schattenstufe pro Projekt ist ein Befund.
- Verläufe bleiben Flächen ohne Bedeutung verboten. Ein Verlauf darf ein reales Objekt, eine Lichtsituation oder einen Datenzustand darstellen, nie „Hochwertigkeit".

### Kartenstil

Die B5-Kartenvariante mit allen Werten und Zuständen steht in [[30-Frontend/Components and UI States#Kartenentscheidung]]. Als Stil gilt hier:

- Eine Karte existiert, weil ihr Inhalt eine eigene, anklickbare oder eigenständig lesbare Einheit ist. Sie existiert nie, weil ein Absatz eine Umrandung braucht.
- Innerhalb einer Karte gibt es eine klare Reihenfolge: Medium oder Icon, Titel, eine Zeile Erklärung, darunter eine Metazeile in gedeckter Farbe, darunter höchstens eine Aktion.
- Die Metazeile trennt mit `·` und bleibt einzeilig. Eine Mono-Schrift für technische Werte und Tags ist Teil dieses Stilprofils und wird nicht auf andere Websites übertragen.
- Bildflächen in Karten sitzen randlos an der Oberkante mit nur oben gerundeten Ecken und einem festen Seitenverhältnis, im Beleg `16/9`. Kein Rahmen zwischen Bild und Kartenrand.
- Innenabstand ist großzügig und projektweit identisch. Dichte entsteht über Inhalt, nicht über engere Polster.

### Bedienung und Zustand

- Die Kopfzeile ist durchscheinend mit Blur, hat aber einen geprüften Kontrast und einen deckenden Fallback. Diese Ausprägung ist eine Option in [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]], kein allgemeines Kopfzeilenrezept.
- Klickbare Karten heben beim Hover um ein bis zwei Pixel und hellen gleichzeitig ihren Rahmen auf. Werte in [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]].
- Status wird als Pille mit Punkt gezeigt, nicht als Farbfläche. Ein echter Live-Zustand darf einen atmenden Ring tragen; ein statischer Zustand nie.
- Tags und Kategorien sind Pillen aus dem Kategorieton bei sehr niedriger Deckung mit demselben Ton als Schriftfarbe. Der Ton färbt nie eine Sektionsfläche.
- Linienicons in einer einzigen Strichstärke und nie größer als der Text, den sie begleiten.

### Motion

- Bewegung ist kurz, gerichtet und in der Fläche verankert. Der Standard-Reveal ist ein Aufstieg über zwölf Pixel mit Opazität in etwa 500 Millisekunden, `ease-out`, mit gehaltenem Endzustand.
- Der Auftakt einer Seite darf einen zeichen- oder wortweisen Aufbau mit Unschärfe tragen. Er blockiert die primäre Aktion nicht.
- Dekorative Hintergründe werden weich ausmaskiert, nicht hart beschnitten.
- Die Werte sind als B5-Kalibrierung in [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] dokumentiert. Jede Website setzt ihren eigenen Zeit- und Kurvensatz.

### Was aus diesem Set nicht übernommen wird

Verlaufstext aus Indigo, Violett und Pink; Emojis als Sektionszeichen; Verlaufsflächen als Bildersatz; jede Sektion als gleichförmiges Kartenraster; alles Rechtliche und alle Kennzahlen. Begründung und Belege in [[90-References/Inspiration Catalog#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]].

## Gemeinsamer Handwerksnenner

Der gemeinsame Nenner der Benchmarks ist H0, nicht ein gemeinsames Aussehen: eindeutige Zustände, Kontextkontrast, ruhende Flächen ohne dekorativen Schatten, Abgrenzung zuerst durch Hierarchie und bei Bedarf Hairlines sowie ein konsistentes System innerhalb der jeweiligen Website. Farbwelt, Radius, Rahmenrhythmus, Flächenlogik, Kartenanteil, Kopfzeile, Zweitschrift und Bewegungscharakter bleiben Art-Direction-Entscheidungen.

## Anwendung

Im Design Contract **jeder gebauten Website** wird festgehalten:

- gewählter Leitbenchmark und Begründung,
- konkret übernommene Elemente je Benchmark,
- ausdrücklich nicht übernommene Elemente, insbesondere die Kicker und die erfundenen Belege aus B3 und die nicht übernommenen Muster aus B5,
- Abweichungen mit inhaltlicher Begründung,
- die H0-Nachweise und die frei gewählten Stilparameter für Radius, Rahmen, Flächen, Tiefe, Karten, Kopfzeile, Zweitschrift und Motion.

B5 wird wie B1 bis B4 bewusst gewählt. Wird B5 nicht gewählt, dürfen seine drei Flächenstufen, vier Radien, B5-Karte, durchscheinende Kopfzeile, Mono-Rollen und Bewegungswerte nicht still als Default einwandern.
