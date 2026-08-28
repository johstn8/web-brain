---
type: canonical
status: canonical
updated: 2026-08-27
review_by: 2027-02-27
depends_on:
  - "[[90-References/Inspiration Catalog]]"
  - "[[90-References/Website Reference Pool]]"
impacts:
  - design-direction
  - motion
  - project-master-spec
  - qa
---

# Reference Research Workflow

## Pflicht und Ergebnis

Vor Design eines Web-Produkts wird zuerst der Referenzmodus aus der Zahl der beauftragten Websites bestimmt. Pflichtartefakt im Projekt ist eine Entscheidungsmatrix mit:

`Website -> Referenzmodus -> direkte URL falls vorhanden -> Passung -> tragende Prinzipien oder Eigenentwurfsherleitung -> Übernahmetiefe -> bewusste Abweichungen -> tatsächlicher Einsatz -> Nachweis`

Die Modi sind `Eigenentwurf`, `nutzer-vorgegeben` und `ausgewählte Leitreferenz`. Eine vom Nutzer im Auftrag ausdrücklich benannte Website darf unabhängig von der Auftragszahl als `nutzer-vorgegeben` verwendet werden. Ohne solche Vorgabe gilt die folgende Quote:

| Anzahl gebauter Websites | Automatisch ausgewählte externe Leitreferenzen | Folge |
|---|---:|---|
| genau eine | `0` | Die Website entsteht als Eigenentwurf aus Projektwahrheit, Leitbenchmark, Designregeln und UI UX Pro Max. Der Pool wird nicht pflichtweise nach einer Vorlage durchsucht. |
| zwei oder mehr | `1` | Genau eine Fassung wird nach starker Passungsprüfung von genau einer konkreten Originalseite geprägt. Alle übrigen Fassungen sind Eigenentwürfe und verwenden diese Seite nicht verdeckt als zweite Vorlage. Nur wenn trotz dokumentierter Suche keine starke Passung existiert, entfällt die Referenz als begründete Ausnahme. |

Für die mögliche referenzgeführte Fassung wird mindestens der [[90-References/Website Reference Pool]] geprüft. Aktuelle Wettbewerber oder fachnahe Produkte dürfen ergänzt werden, wenn ihre direkte Live-URL dokumentiert wird. Sammlungs-, Galerie-, Award- und Stilbibliotheksseiten sind nur Recherchewege und niemals die Leitreferenz selbst. Gibt es keine starke Passung, bleiben alle Fassungen Eigenentwürfe; eine beliebige Seite wird nicht erzwungen.

## Pflichtumfang je Web-Produkt

Verbindlich sind:

- **Die Quote ist bindend.** Eine einzelne Website erhält keine automatisch ausgewählte Leitreferenz. Bei mehreren Websites erhält genau eine Fassung genau eine ausgewählte Leitreferenz; die Entscheidung, welche Fassung das ist, fällt vor dem Direction Brief. Nur eine dokumentiert erfolglose Suche nach starker Passung erlaubt, dass alle Fassungen Eigenentwürfe bleiben.
- **Mindestens drei plausible Kandidaten einmal kurz vergleichen**, sofern der Pool drei fachlich sinnvolle Kandidaten enthält. Der Vergleich dient nur der möglichen referenzgeführten Fassung. Eigenentwürfe brauchen keine künstlichen Ablehnungsmatrizen.
- **Keine Quervererbung.** Raster, Auftakt, Sektionsdramaturgie, Typografie, Flächen und Motion der ausgewählten Referenz werden nur in der benannten Fassung adaptiert. Gemeinsame Fakten, Nutzerfragen und eine sachlich beste Grobstruktur dürfen in allen Fassungen gleich sein; Referenzdetails nicht.
- **Passung vor Spektakel.** Branche, Angebotslogik, Zielgruppe, Inhaltsmenge, benötigte Beweise und Markenwirkung zählen stärker als Awards oder technische Effekte. Unter ähnlich passenden Kandidaten wird die professionellere und sinnvoll animationsreichere Seite bevorzugt.
- **Übernahmetiefe offen benennen:** `punktuell`, `teilweise` oder `prägend`, optional mit grober Prozentangabe. 20, 30, 60 oder 70 Prozent können gleichermaßen richtig sein; kein Mindestwert wird erzwungen.
- **Eigenentwurf ist der Normalmodus.** Er wird aus Projektwahrheit, Leitbenchmark, realem Inhaltsanker und Brain-Regeln hergeleitet. Nur wenn für eine geplante referenzgeführte Fassung keine starke Passung gefunden wurde, werden die geprüften Kandidaten und der Ablehnungsgrund dokumentiert.
- **Ergebnis in Sätzen, nicht in Stichworten.** Benannt werden konkrete Folgen für Auftakt, Raster, Sektionsdramaturgie, Typografie, Flächen, Medien und Motion sowie bewusste Abweichungen.

Der Nachweis liegt als Entscheidungsmatrix im Projekt und wird in jedem Design Contract verlinkt. Negative Muster und interne Benchmarks aus dem [[90-References/Inspiration Catalog]] dürfen alle Fassungen informieren, sind aber keine verdeckten Leitreferenzen.

## Auswahl

1. Projektziel, Zahl der Websites, Branche, Zielgruppe, Inhaltsart, Beweisformen, Plattform und Grenzen aus `PROJECT.md` extrahieren.
2. Referenzmodus je Website festlegen. Bei genau einer Website `Eigenentwurf`; bei mehreren genau eine mögliche referenzgeführte Fassung bestimmen und alle übrigen als `Eigenentwurf` markieren. Nutzer-vorgegebene Referenzen gesondert kennzeichnen.
3. Nur für die mögliche referenzgeführte Fassung im [[90-References/Website Reference Pool]] zuerst in der passenden Branchenkategorie suchen, dann bei Bedarf nach Wirkung oder Interaktionsniveau. Nur konkrete Live-Websites in die Shortlist aufnehmen.
4. Kandidaten nach `Branchenpassung`, `Angebots-/Inhaltspassung`, `Zielgruppenwirkung`, `übertragbarer Struktur`, `Motion-/Interaktionswert` und `technischer Machbarkeit` vergleichen. Fachliche Passung wiegt am stärksten.
5. Genau eine Leitreferenz für die benannte Fassung wählen oder alle Kandidaten begründet ablehnen. Übernahmetiefe und konkrete Übertragung festlegen: Was wird an Grundstruktur, Auftakt, Raster, Typografie, Flächen, Medienführung, Sektionsdramaturgie und Motion übernommen, adaptiert oder verworfen?
6. Für jeden Eigenentwurf die Herleitung aus Projektwahrheit, Inhaltsanker, Leitbenchmark und Nutzerfragen in Sätzen festhalten. Keine fremde Seite als unausgesprochene Vorlage verwenden.
7. Die Anordnung von Überschriften und den Aufbau jeder Landing Page zusätzlich gegen [[90-References/Derived Design Patterns#Anordnung von Überschriften]] und [[90-References/Derived Design Patterns#Landing Page mit Ausdruck]] prüfen.
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

Für abgelehnte Shortlist-Kandidaten genügen direkte URL, Abrufdatum und ein kurzer, konkreter Ablehnungsgrund. Eine vollständige Browserbeweissammlung ist nur für die gewählte Leitreferenz erforderlich. Reine Eigenentwürfe ohne Referenzsuche brauchen keine externe Browserbeweissammlung.

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
- bei genau einer Website keine automatisch ausgewählte Leitreferenz
- bei mehreren Websites genau eine ausgewählte konkrete Leitreferenz für genau eine Fassung; nur bei dokumentiert fehlender starker Passung keine, alle übrigen als Eigenentwurf hergeleitet
- keine Sammlung, Galerie, Award-Liste oder Stilbibliothek als Leitreferenz
- bei referenzgeführter Fassung Passungsbegründung, Übernahmetiefe, konkrete Übernahmen und bewusste Abweichungen
- bei Eigenentwürfen Herleitung aus Projektwahrheit, Inhaltsanker, Leitbenchmark und Nutzerfragen
- statische und interaktive Aussagen getrennt belegt
- Desktop, Mobil, Tastatur und Reduced Motion beurteilt
- tatsächlicher Einsatz und technische Risiken dokumentiert
- Entscheidung im Design Contract verlinkt

[^video]: [Playwright: Videos](https://playwright.dev/docs/videos)
[^emulation]: [Playwright: Emulation, Reduced motion](https://playwright.dev/docs/emulation#reduced-motion)
[^load]: [Playwright: Page waitForLoadState](https://playwright.dev/docs/api/class-page#page-wait-for-load-state)
