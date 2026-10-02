---
type: canonical
status: canonical
updated: 2026-10-02
review_by: 2027-02-27
depends_on:
  - "[[20-design/qualitaetsraster.md]]"
  - "[[90-references/inspiration-catalog.md]]"
  - "[[90-references/website-reference-pool.md]]"
impacts:
  - design-direction
  - motion
  - project-master-spec
  - qa
---

# Reference Research Workflow

## Pflicht und Ergebnis

Vor dem Design jeder Website, **auch einer einzelnen**, steht der [[#Gattungsvergleich]]: gute und schlechte Websites derselben Gattung werden angesehen, nach dem [[20-design/qualitaetsraster.md]] bewertet, und die zwei bis drei besten werden zum Maßstab. Er ist unabhängig von Auftragszahl und Referenzmodus und entfällt nie.

Danach wird der Referenzmodus aus der Zahl der beauftragten Websites bestimmt. Pflichtartefakt im Projekt ist eine Entscheidungsmatrix mit:

`Website -> Referenzmodus -> direkte URL falls vorhanden -> Passung -> tragende Prinzipien oder Eigenentwurfsherleitung -> Übernahmetiefe -> bewusste Abweichungen -> tatsächlicher Einsatz -> Nachweis`

Die Modi sind `Eigenentwurf`, `nutzer-vorgegeben` und `ausgewählte Leitreferenz`. **`Eigenentwurf` heißt seit 2026-10-02: ohne prägende Einzelvorlage, aber auf Grundlage der Benchmarks des Gattungsvergleichs**, nicht mehr ohne Blick auf die Gattung. Eine vom Nutzer im Auftrag ausdrücklich benannte Website darf unabhängig von der Auftragszahl als `nutzer-vorgegeben` verwendet werden. Ohne solche Vorgabe gilt die folgende Quote:

| Anzahl gebauter Websites | Automatisch ausgewählte externe Leitreferenzen | Folge |
|---|---:|---|
| genau eine | `0` bis `1` | Die Website entsteht aus den übertragbaren Prinzipien der Benchmarks des Gattungsvergleichs. Passt eine Benchmark stark, darf sie als Leitreferenz prägen; Pflicht ist das nicht. Ein Entwurf ohne Blick auf die Gattung ist nicht mehr zulässig. |
| zwei oder mehr | `1` | Genau eine Fassung wird nach starker Passungsprüfung von genau einer konkreten Originalseite geprägt. Alle übrigen Fassungen sind Eigenentwürfe und verwenden diese Seite nicht verdeckt als zweite Vorlage. Nur wenn trotz dokumentierter Suche keine starke Passung existiert, entfällt die Referenz als begründete Ausnahme. |

Für die mögliche referenzgeführte Fassung wird mindestens der [[90-references/website-reference-pool.md]] geprüft. Aktuelle Wettbewerber oder fachnahe Produkte dürfen ergänzt werden, wenn ihre direkte Live-URL dokumentiert wird. Sammlungs-, Galerie-, Award- und Stilbibliotheksseiten sind nur Recherchewege und niemals die Leitreferenz selbst. Gibt es keine starke Passung, bleiben alle Fassungen Eigenentwürfe; eine beliebige Seite wird nicht erzwungen.

## Pflichtumfang je Web-Produkt

Verbindlich sind:

- **Die Quote ist bindend.** Eine einzelne Website erhält höchstens eine Leitreferenz, und nur aus den Benchmarks ihres Gattungsvergleichs. Bei mehreren Websites erhält genau eine Fassung genau eine ausgewählte Leitreferenz; die Entscheidung, welche Fassung das ist, fällt vor dem Direction Brief. Nur eine dokumentiert erfolglose Suche nach starker Passung erlaubt, dass alle Fassungen Eigenentwürfe bleiben.
- **Mindestens drei plausible Kandidaten einmal kurz vergleichen**, sofern der Pool drei fachlich sinnvolle Kandidaten enthält. Der Vergleich dient nur der möglichen referenzgeführten Fassung. Eigenentwürfe brauchen keine künstlichen Ablehnungsmatrizen.
- **Keine Quervererbung.** Raster, Auftakt, Sektionsdramaturgie, Typografie, Flächen und Motion der ausgewählten Referenz werden nur in der benannten Fassung adaptiert. Gemeinsame Fakten, Nutzerfragen und eine sachlich beste Grobstruktur dürfen in allen Fassungen gleich sein; Referenzdetails nicht.
- **Passung vor Spektakel.** Branche, Angebotslogik, Zielgruppe, Inhaltsmenge, benötigte Beweise und Markenwirkung zählen stärker als Awards oder technische Effekte. Unter ähnlich passenden Kandidaten wird die professionellere und sinnvoll animationsreichere Seite bevorzugt.
- **Übernahmetiefe offen benennen:** `punktuell`, `teilweise` oder `prägend`, optional mit grober Prozentangabe. 20, 30, 60 oder 70 Prozent können gleichermaßen richtig sein; kein Mindestwert wird erzwungen.
- **Der Eigenentwurf auf Grundlage der Gattungsbenchmarks ist der Normalmodus.** Er wird aus Projektwahrheit, den Prinzipien der Gattungsbenchmarks, realem Inhaltsanker und Brain-Regeln hergeleitet. Der frühere reine Eigenentwurf ohne Blick auf die Gattung entfällt: Er hat 2026 vier Restaurantfassungen hervorgebracht, die alle Messungen bestanden und neben realen Restaurantseiten trotzdem generiert wirkten. Nur wenn für eine geplante referenzgeführte Fassung keine starke Passung gefunden wurde, werden die geprüften Kandidaten und der Ablehnungsgrund dokumentiert.
- **Ergebnis in Sätzen, nicht in Stichworten.** Benannt werden konkrete Folgen für Auftakt, Raster, Sektionsdramaturgie, Typografie, Flächen, Medien und Motion sowie bewusste Abweichungen.

Der Nachweis liegt als Entscheidungsmatrix im Projekt und wird in jedem Design Contract verlinkt. Negative Muster und interne Benchmarks aus dem [[90-references/inspiration-catalog.md]] dürfen alle Fassungen informieren, sind aber keine verdeckten Leitreferenzen.

## Gattungsvergleich

Verbindlich für jede Website. Ergebnis ist ein Bogen mit bewerteten Seiten, zwei bis drei Benchmarks, ein bis zwei Negativbeispiele und die übertragbaren Prinzipien in Sätzen. Das Urteil folgt [[20-design/qualitaetsraster.md#Gattungsvergleich]]; hier steht, wie gesucht und aufgenommen wird.

1. **Zuerst den Pool lesen.** [[90-references/website-reference-pool.md]] führt für manche Gattungen bereits bewertete Benchmarks. Sind dort mindestens zwei Benchmarks der Gattung eingetragen, werden sie live neu aufgenommen und geprüft, ob sie noch gelten; zusätzlich werden drei neue Kandidaten gesucht.
2. **Suchen in dieser Reihenfolge:** Wettbewerber im selben Ort, dann dieselbe Stadt, dann Deutschland, dann international. Lokale Wettbewerber zeigen, gegen wen der Betrieb antritt; die besten Seiten finden sich meist national oder international.
3. **Gute Seiten findet man über gute Betriebe.** Auszeichnungs- und Restaurantführer, Fachmedien, die Bestenlisten der Stadtmagazine und die Kundenlisten guter Agenturen sind ergiebiger als Suchmaschinentreffer zu „schöne Website". Galerie- und Award-Seiten sind nur Entdeckungsweg, nie Benchmark.
4. **Acht bis zwölf Kandidaten aufnehmen**, je Auftakt bei 1440 und 390 Pixel und die ganze Startseite, nach der [[#Robuste Screenshot-Regel]]. Einwilligungsbanner werden geschlossen; eine Aufnahme, die nur ein Banner zeigt, ist `invalid` und wird nicht bewertet.
5. **Jede gültige Aufnahme nach den zehn Kriterien bewerten.** Für die Benchmarks zusätzlich `web-kit/scripts/check-slop.ts` gegen die Live-Seite laufen lassen; eine Benchmark mit harter Sperre wird nur mit dieser Einschränkung eingetragen.
6. **Bogen bauen:** Auftakte nebeneinander, Benchmarks und Negativbeispiele markiert. Der Bogen ist zugleich die Vorlage für den späteren [[20-design/qualitaetsraster.md#Benchmarkvergleich]].
7. **Neue starke Funde dem Nutzer vorschlagen.** Eine Seite mit mindestens 16 Punkten, die noch nicht im Pool steht, wird am Ende des Auftrags mit Aufnahme und Punkten zur Aufnahme vorgeschlagen. **Ob sie in den Pool kommt, entscheidet der Nutzer**, nicht der Agent. Bis dahin liegt sie als Rechercheevidenz unter `.research/screenshots/`.

Ablage im Projekt: `research/gattungsvergleich/<YYYY-MM-DD>/` mit den Aufnahmen, dem Bogen und einer `bewertung.md` mit Punkten je Kriterium, Einstufung und übertragbaren Prinzipien.

## Auswahl

1. Projektziel, Zahl der Websites, Branche, Zielgruppe, Inhaltsart, Beweisformen, Plattform und Grenzen aus `PROJECT.md` extrahieren.
2. Referenzmodus je Website festlegen. Bei genau einer Website `Eigenentwurf`; bei mehreren genau eine mögliche referenzgeführte Fassung bestimmen und alle übrigen als `Eigenentwurf` markieren. Nutzer-vorgegebene Referenzen gesondert kennzeichnen.
3. Nur für die mögliche referenzgeführte Fassung im [[90-references/website-reference-pool.md]] zuerst in der passenden Branchenkategorie suchen, dann bei Bedarf nach Wirkung oder Interaktionsniveau. Nur konkrete Live-Websites in die Shortlist aufnehmen.
4. Kandidaten nach `Branchenpassung`, `Angebots-/Inhaltspassung`, `Zielgruppenwirkung`, `übertragbarer Struktur`, `Motion-/Interaktionswert` und `technischer Machbarkeit` vergleichen. Fachliche Passung wiegt am stärksten.
5. Genau eine Leitreferenz für die benannte Fassung wählen oder alle Kandidaten begründet ablehnen. Übernahmetiefe und konkrete Übertragung festlegen: Was wird an Grundstruktur, Auftakt, Raster, Typografie, Flächen, Medienführung, Sektionsdramaturgie und Motion übernommen, adaptiert oder verworfen?
6. Für jeden Eigenentwurf die Herleitung aus Projektwahrheit, Inhaltsanker, den Prinzipien der Gattungsbenchmarks und Nutzerfragen in Sätzen festhalten. Keine fremde Seite als unausgesprochene Vorlage verwenden.
7. Die Anordnung von Überschriften und den Aufbau jeder Landing Page zusätzlich gegen [[90-references/derived-design-patterns.md#Anordnung von Überschriften]] und [[90-references/derived-design-patterns.md#Landing Page mit Ausdruck]] prüfen.
8. Auswahl gegen Accessibility, Performance, Content-Wahrheit, reale Markenidentität, technische Machbarkeit und Wartung abwägen. Inhalte, Claims, Identitätsmerkmale, Logos und rechtliche Aussagen der Referenz werden nicht auf das neue Unternehmen übertragen.

## Evidenz erfassen

Für die gewählte oder nutzer-vorgegebene Leitreferenz und alle tatsächlich übernommenen interaktiven Prinzipien festhalten:

- Name, direkte URL, Abrufdatum und Prüfer
- Browser, Viewport, Eingabemethode, Netzprofil und relevante Präferenzen
- Zeitpunkt oder beobachtbares Bereitschaftssignal der Aufnahme
- statischer Screenshot für Layout und sichtbaren Zustand
- Interaktionsprotokoll für Trigger, Ablauf, Dauer, Ursache/Wirkung und Abbruch
- Mobile-, Tastatur- und Reduced-Motion-Verhalten
- Lade-, Fehler- und Fallbackzustand bei Medien, Canvas, 3D oder Ton
- Scroll-Map je primärer Route: kontinuierliche Scrollsequenz, weitere Scroll-/In-View-Bewegungen, Trigger/Ranges und Rückwärts-Scroll

Für abgelehnte Shortlist-Kandidaten genügen direkte URL, Abrufdatum und ein kurzer, konkreter Ablehnungsgrund. Eine vollständige Browserbeweissammlung ist nur für die gewählte Leitreferenz erforderlich. Für Eigenentwürfe genügen die Aufnahmen und die Bewertung aus dem Gattungsvergleich; eine Interaktionsprüfung je Benchmark ist nur nötig, wenn deren Bewegung übernommen werden soll.

Ein Screenshot belegt nur den aufgenommenen Zustand. Animation, Scroll-Choreografie, Audio, Fokusführung und Zustandsübergänge benötigen ein Interaktionsprotokoll und, wenn möglich, eine kurze Video- oder Trace-Aufnahme. Playwright kann Browserkontexte als Video aufzeichnen und reduzierte Bewegung emulieren.[^video][^emulation]

## Robuste Screenshot-Regel

- Nicht allein auf einen festen Sleep vertrauen. Auf dokumentierte Readiness wie sichtbaren Kerninhalt, verschwundenen Loader oder geladenes Hero-Medium warten. Playwright stellt dafür Load States und explizite UI-Bedingungen bereit.[^load]
- JavaScript-, Font-, Bild-, Canvas- und WebGL-Inhalt nach dem Readiness-Signal zusätzlich visuell prüfen.
- Eine weiße, fast leere, reine Loader- oder Consent-Aufnahme ist `invalid`, nicht Evidenz.
- Schlägt Headless-Rendering fehl, einmal mit längerem Budget und passender Grafikunterstützung wiederholen. Bleibt der Fehler, als `manual-review` markieren und keine visuellen oder interaktiven Behauptungen daraus ableiten.
- Quelldatei nicht still überschreiben. Neue Aufnahme zunächst prüfen; danach Manifest und Status aktualisieren.

## Ablage

`../projekte/<Projektname>/research/references/<slug>/<YYYY-MM-DD>/`

Dateien: `source.md`, `desktop.png`, `mobile.png`, optional `interaction.webm` oder `trace.zip`. Globale Rechercheartefakte bleiben unter `.research/` und werden niemals als Projektasset ausgeliefert.

## Abnahme

- Referenzmodus je Website dokumentiert
- Gattungsvergleich je Website mit bewerteten Kandidaten, zwei bis drei Benchmarks, ein bis zwei Negativbeispielen und übertragbaren Prinzipien abgelegt
- Benchmarkvergleich vor der Lieferung mit Bogen, Rasterpunkten und den drei Antworten nach [[20-design/qualitaetsraster.md#Benchmarkvergleich]]
- bei genau einer Website höchstens eine Leitreferenz, und nur aus den Benchmarks des Gattungsvergleichs
- bei mehreren Websites genau eine ausgewählte konkrete Leitreferenz für genau eine Fassung; nur bei dokumentiert fehlender starker Passung keine, alle übrigen als Eigenentwurf hergeleitet
- keine Sammlung, Galerie, Award-Liste oder Stilbibliothek als Leitreferenz
- bei referenzgeführter Fassung Passungsbegründung, Übernahmetiefe, konkrete Übernahmen und bewusste Abweichungen
- bei Eigenentwürfen Herleitung aus Projektwahrheit, Inhaltsanker, den Prinzipien der Benchmarks und Nutzerfragen
- statische und interaktive Aussagen getrennt belegt
- Desktop, Mobil, Tastatur und Reduced Motion beurteilt
- tatsächlicher Einsatz und technische Risiken dokumentiert
- Entscheidung im Design Contract verlinkt

[^video]: [Playwright: Videos](https://playwright.dev/docs/videos)
[^emulation]: [Playwright: Emulation, Reduced motion](https://playwright.dev/docs/emulation#reduced-motion)
[^load]: [Playwright: Page waitForLoadState](https://playwright.dev/docs/api/class-page#page-wait-for-load-state)
