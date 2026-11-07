---
type: canonical
status: canonical
updated: 2026-11-07
depends_on:
  - "[[90-references/inspiration-catalog.md]]"
impacts:
  - "[[20-design/design-direction.md]]"
  - "[[20-design/color-system.md]]"
  - "[[20-design/typography-layout-and-spacing.md]]"
  - "[[20-design/motion-and-interaction.md]]"
  - "[[30-frontend/components-and-ui-states.md]]"
  - "[[90-references/derived-design-patterns.md]]"
---

# Interface Benchmarks

> [!important] Rang
> Diese Notiz ist die kanonische Beschreibung der vom Nutzer ausdrücklich als gut bewerteten Oberflächen. Sie steht bei visuellen Entscheidungen **über** allgemeinen Referenzmustern aus [[90-references/derived-design-patterns.md]] und unter dem jeweiligen `PROJECT.md`. Die Belege dazu stehen in [[90-references/inspiration-catalog.md#Vom Nutzer bewertete Benchmarks]].

Sechs Benchmarks, sechs Rollen. Jede gebaute Website wählt mindestens einen davon als Leitbenchmark und benennt ihn in ihrem eigenen Design Contract. Ein Benchmark ist ein Werkzeug für den jeweiligen Use Case, kein Normalstil des Brains.

## H0 Handwerksuntergrenze

H0 ist kein Look und kein nummerierter Benchmark. Die Untergrenze gilt für jede Website, ohne ihr eine gemeinsame Art Direction aufzuzwingen:

- anwendbare Komponenten besitzen vollständige Zustände einschließlich `focus-visible`, Laden, Fehler, Leerzustand und deaktiviert;
- Text, Icons, Controls und Fokus erreichen ihren erforderlichen Kontrast in der tatsächlich gerenderten Kombination aus Variante und Untergrund;
- Hierarchie und Tiefe sind nachvollziehbar; Schatten, Rahmen, Hairlines, Überlagerung, Farbe und Weißraum sind gleichwertige Mittel, wenn sie im gewählten System eine klare Rolle besitzen;
- Tokens, Typografie, Spacing, Radius-, Rahmen-, Flächen-, Tiefen- und Motionentscheidungen bilden **innerhalb einer Website** ein konsistentes System;
- Interaktion bleibt per Tastatur, Touch und Zeigegerät verständlich, Reduced Motion erhält die Information und kein visueller Effekt blockiert Inhalt oder primäre Aktion;
- eine echte Darstellung an den Prüfbreiten ist Teil der Abnahme. Nicht renderbare UI ist ein Blocker nach [[70-qa/quality-gates.md]], kein ersatzweise bestandener Textscan.

Die frühere B5-Regel vermischte diese Handwerksuntergrenze mit einem fertigen Stil. Künftig gilt folgende Zuordnung:

| Aussage aus dem früheren B5 | Ebene ab jetzt |
|---|---|
| Zustandsvollständigkeit, sichtbarer Fokus, Kontrast im Kontext, klare Hierarchie und interne Systemkonsistenz | **H0, immer verbindlich** |
| Anzahl und Abstand der Flächenstufen, Radiusanzahl und -werte, genaue Rahmenbehandlung, Hover-Lift, Kartenaufbau, Kopfzeilenaufbau, Mono-Familie und ihre Rollen, Metazeilentrenner, genaue Reveal- und Bewegungswerte | **Stilebene, je Website zu entscheiden** |

Ein Build ist nicht deshalb handwerklich schwächer, weil er kantig statt weich, zeilen- statt kartenbasiert, deckend statt durchscheinend oder ohne Monospace gestaltet ist. Schwach ist er, wenn seine gewählte Grammatik inkonsistent oder in realen Zuständen unlesbar und unbedienbar wird.

## B1 Soft Neutral Product Console

**Rolle:** Grundhaltung für Oberflächen mit Daten, Listen, Status und Verwaltung. Höchste Priorität. Wenn nichts anderes im Auftrag steht, ist das die Standardanmutung für Anwendungs-UI.

Bezug: das vom Nutzer gelieferte Dashboard-Bild in [[90-references/inspiration-catalog.md#Vom Nutzer bewertete Benchmarks]].

**Fläche und Farbe**

- Weiße bis fast weiße Grundfläche, ein einziger neutraler Grauton als Sekundärfläche. Kein Beige, keine Fläche mit Farbstich.
- Farbe erscheint fast ausschließlich semantisch: Grün für positive Veränderung und `Online`, Rot für Fehler, Gelb für Warnung.
- Zusätzliche Farbtöne nur als Kategoriemarker in Icon-Tints, etwa Blau, Grün, Violett, Orange bei je einem Kennzahlenfeld. Sie färben nie eine Fläche ein.
- Genau eine dunkle Signalfarbe für den aktiven Zustand, im Benchmark ein fast schwarzes Element.

**Struktur**

- Seitenleiste mit Produktmarke oben, darunter eine flache Navigationsliste aus Linienicon und Beschriftung. Der aktive Punkt ist eine gefüllte, dunkle, abgerundete Fläche mit heller Schrift; inaktive Punkte tragen keine Fläche.
- Inhaltsbereich beginnt mit Seitentitel und einer einzigen erklärenden Zeile in Grau. Kein Kicker darüber, siehe [[20-design/anti-ai-slop.md#Kicker und Überschriften]].
- Kennzahlenreihe aus vier gleich breiten Feldern: Beschriftung und Icon in einer Zeile, darunter die große Zahl, darunter die Veränderung.
- Darunter zwei ungleich breite Blöcke nebeneinander, danach ein breiter Block über die volle Breite. Kein durchgehend gleichförmiges Kartenraster.

**Detailsprache**

- Ein Rahmen von einem Pixel in sehr niedrigem Kontrast trägt die Abgrenzung. Kein Schlagschatten, kein Verlauf, kein Glas.
- Eine einzige Radiusstufe für Container, ungefähr `12px` bis `14px`. Pillen nur für Statusanzeigen.
- Linienicons in einer Strichstärke. Icons sind klein und stehen nie größer als der Text, den sie begleiten.
- Fortschrittsbalken sind flach, wenige Pixel hoch, mit hellgrauer Spur und einer einzigen kräftigen Füllung. Beschriftung links, Wert rechts, beide über dem Balken.
- Listeneinträge bestehen aus rundem, sehr hell getöntem Icon-Träger, kräftiger Titelzeile und einer grauen Metazeile im Muster `Name · Zeitangabe`. Der Mittelpunkt trennt hier genau **zwei** sachlich verschiedene Felder und trägt damit Information; als Aneinanderreihung von drei oder mehr Werten auf jeder Karte wäre er ein Befund nach [[20-design/anti-ai-slop.md#Chrome und Beschriftung]].
- Großzügiger Innenabstand in den Containern und deutlich sichtbare Abstände zwischen den Blöcken. Dichte entsteht durch Inhalt, nicht durch Zusammenrücken.

**Typografie:** eine neutrale, geometrisch geprägte Grotesk. Titel halbfett, Kennzahlen fett, Fließtext und Metazeilen normal in Grau. Keine Serifen, keine Versalzeilen als Dekoration.

**Motion:** klein und bestätigend. Zahlen dürfen beim ersten Sichtbarwerden einmal zählen, Balken einmal auf ihren Wert wachsen, Listen mit kurzem Versatz eintreten. Danach ist die Oberfläche ruhig.

## B2 Rounded Selection Configurator

**Rolle:** Leitbild für Produkt-, Varianten- und Größenauswahl sowie für jede Seite, deren Kern ein einzelnes Objekt ist.

Bezug: der 180-Grad-Produktbetrachter in [[90-references/inspiration-catalog.md#Vom Nutzer bewertete Benchmarks]]. Am 2026-11-07 vom Nutzer bestätigt: starker Aufbau der Produktansichten, gute Knöpfe. Als Baustein im Kit: `blocks/Produktansicht.astro`.

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

Bezug: die Solarseite in [[90-references/inspiration-catalog.md#Vom Nutzer bewertete Benchmarks]]. Am 2026-11-07 vom Nutzer bestätigt: stark, aber Ovale über Überschriften und Verläufe machen die KI sichtbar.

**Übernehmen**

- Ein einziges großes, randloses Leitbild trägt den Auftakt. Der Gegenstand des Betriebs ist darauf tatsächlich zu sehen: die Anlage, der Laden, das Fahrzeug, die Werkstatt, das Team bei der Arbeit.
- Genau eine kräftige Signalfarbe aus dem Gegenstand selbst gegen eine dunkle, entsättigte Grundfläche. Die Signalfarbe erscheint in Marke, primärer Aktion und wenigen Akzenten, nie flächig.
- Leistungen als kleine, klar benannte Gruppe statt als lange Liste. Vier bis sechs Einträge mit je einer Zeile Erklärung reichen.
- Eine kurze Nutzenüberschrift, ein erklärender Satz, eine primäre Aktion. Danach folgt Beweis.

**Nicht übernehmen**

- Jede Zeile oder Pille über einer Überschrift, auch echte Rubrikinformation (harte Sperre S1), und Verläufe in Flächen oder Schrift.
- Erfundene Kennzahlen wie erzeugte Energie, abgeschlossene Projekte, Zufriedenheitsquote oder Jahre Erfahrung ohne Beleg, und ebenso erfundene Kundenstimmen mit Namen. Beides fällt unter [[10-strategy/content-and-conversion.md#Beweis-Hierarchie]].
- Austauschbare Abschnittstexte, die zu jedem beliebigen Anbieter derselben Branche passen.

## B4 Data Product Depth

**Rolle:** Aufbau für Anwendungen, die Daten auswerten.

Bezug: ursprünglich das ATS-Dashboard, das der Nutzer am 2026-11-07 verworfen hat. Die Regeln bleiben als allgemeine Regeln für Datenansichten; ein Vorbild hat B4 derzeit nicht.

- Jede Kennzahl wird eingeordnet: eigener Wert, Vergleichswert und benannter Zeitraum. Eine Zahl ohne Bezugsgröße ist keine Aussage.
- Kategorien erhalten je eine feste Farbe, die über alle Ansichten hinweg dieselbe bleibt. Farbe ist nie das einzige Unterscheidungsmerkmal; Beschriftung steht immer dabei.
- Leerzustände sind vollwertig gestaltet: Was fehlt, warum, und die eine Aktion, die es behebt.
- Einstellungen, Datenaufbewahrung, Export und Löschung sind sichtbare, echte Funktionen, keine Attrappen. Serverseitige Durchsetzung nach [[40-backend-security/security-baseline.md]].
- Diagramme folgen den Regeln aus [[30-frontend/components-and-ui-states.md]] und behalten eine textliche oder tabellarische Alternative.

## B5 Modern Neutral Craft Web

**Rolle:** Wählbares Stilprofil für Produktvorstellungen, Portfolios und inhaltsgetriebene Seiten. B5 ist nicht die Handwerksuntergrenze; nur eine Website, die B5 wählt, übernimmt seine Formsprache.

Bezug: [[90-references/inspiration-catalog.md#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]]. Von den sieben Seiten vom August hat der Nutzer am 2026-11-07 vier verworfen. B5 beruht jetzt nur noch auf dem, was er an Consile und Saad Salman gelobt hat, und auf Phillip Ohren.

- **Produktvorstellung nach Consile:** ein Produkt, Schritt für Schritt gezeigt, mit echter Oberfläche statt Illustration. Nicht übernommen wird die eine Markenfarbe auf jeder Fläche und jeder Verlauf: Der Nutzer erkennt genau daran die KI. Eine B5-Seite wechselt Flächen und Töne.
- **Schwebende Elemente nach Saad Salman:** einzelne Karten oder Bilder liegen mit ruhigem Versatz über dem Grund und bewegen sich beim Scrollen leicht gegeneinander. Klickbare Flächen heben beim Hover um ein bis zwei Pixel, der Rahmen nimmt den Akzent an, dazu höchstens ein sehr flacher Schatten, belegt `0 8px 30px rgba(0,0,0,.06)`.
- **Weißraum nach Phillip Ohren:** großer Abstand ist das Trennmittel, kein Linien- oder Flächenwechsel; Text darf direkt auf dem Leitbild einer Leistung stehen.
- **Rahmen statt Schatten im Ruhezustand.** Ein Pixel, eine Rahmenstufe für Ruhe und eine für Hover und Fokus.
- **Nicht übernommen:** Ovale und Pillen über Überschriften, Pillen als Etiketten, die keine Knöpfe sind, Verläufe in Überschriften und Flächen, Statuspunkte mit atmendem Ring, Mono-Schrift als Stilmittel, Emojis als Sektionszeichen.

Die Bausteine dazu stehen im Kit: `blocks/Schwebend.astro` und `blocks/Produktschritte.astro`.

## B6 Purpose-Fit Professional Web

**Rolle:** Leitbenchmark für Unternehmens-, Praxis-, Beratungs-, Agentur-, Event- und Conversion-Websites, bei denen professionelle Qualität aus Passung statt aus einer wiederholten Designergrammatik entsteht.

Bezug: die vom Nutzer am 19. August 2026 benannte Rocket-Sites-Referenzgruppe in [[90-references/inspiration-catalog.md#Rocket-Sites-Referenzgruppe — strukturell analysiert am 19. August 2026]].

**Übernehmen**

- Angebot, Zielgruppe und nächste Handlung werden früh verständlich, aber nicht zwangsläufig in derselben Hero-Komposition.
- Navigation bildet die reale Angebotstiefe ab. Eine kleine Einzweckseite darf zwei oder drei Ziele besitzen; ein gewachsener B2B-Auftritt darf viele klar gruppierte Ziele, Untermenüs oder Utility-Ebenen führen.
- Vertrauensaufbau folgt dem Geschäft: Team und Räume bei Praxen, Arbeitsproben und Medien bei Agenturen, Cases und Partner bei B2B, Ablauf und direkte Kontaktwege bei lokalen Diensten.
- Seitenlänge, Dichte, Bildanteil, Typografie, Farbstimmung und Motion dürfen stark variieren. Konsistenz gilt innerhalb der Website, nicht zwischen allen Builds des Brains.
- Wiederkehrende Conversion-Aktionen dürfen über lange Seiten hinweg stabil benannt und an sinnvollen Entscheidungspunkten wiederholt werden.
- Unterseiten, FAQ, Prozess, Referenzen und lange Erklärstrecken werden nur gebaut, wenn Angebot und Nutzerfragen sie tragen. Eine fokussierte kurze Seite ist ebenso professionell wie ein tiefer Informationsauftritt.

**Nicht übernehmen**

- unbelegte Garantien, Zahlen, Testimonials oder Superlative;
- redundante Inhaltsblöcke, veraltete Termine oder doppelt ausgelieferten Text;
- sichtbare Unfertigkeit, Attrappen und technisch nicht angebundene Kontaktwege;
- ein einzelnes Rocket-Sites-Beispiel als neue Vorlage für alle Branchen.

**Entscheidungsregel**

Der Design Contract beantwortet zuerst: Was muss diese konkrete Website verständlich, glaubwürdig und leicht handelbar machen? Erst danach werden Headerinventar, Seitentiefe, Beweisform, Typografie, Flächen, Motion und Interaktion gewählt. B6 darf alleiniger Leitbenchmark sein; es verlangt kein B5-Kartenrezept, kein interaktives Kernmodul und keine Mindestmenge an Bewegung.

## Gemeinsamer Handwerksnenner

Der gemeinsame Nenner der Benchmarks ist H0, nicht ein gemeinsames Aussehen: eindeutige Zustände, Kontextkontrast, verständliche Hierarchie und ein konsistentes System innerhalb der jeweiligen Website. Farbwelt, Radius, Schatten, Rahmenrhythmus, Flächenlogik, Kartenanteil, Kopfzeile, Zweitschrift und Bewegungscharakter bleiben Art-Direction-Entscheidungen.

## Anwendung

Im Design Contract **jeder gebauten Website** wird festgehalten:

- gewählter Leitbenchmark und Begründung,
- konkret übernommene Elemente je Benchmark,
- ausdrücklich nicht übernommene Elemente, insbesondere redundante Kicker und erfundene Belege aus B3 sowie die nicht übernommenen Muster aus B5,
- Abweichungen mit inhaltlicher Begründung,
- die H0-Nachweise und die frei gewählten Stilparameter für Radius, Rahmen, Flächen, Tiefe, Karten, Kopfzeile, Zweitschrift und Motion.

B5 wird wie B1 bis B4 bewusst gewählt. Wird B5 nicht gewählt, dürfen seine drei Flächenstufen, vier Radien, B5-Karte, durchscheinende Kopfzeile, Mono-Rollen und Bewegungswerte nicht still als Default einwandern.
