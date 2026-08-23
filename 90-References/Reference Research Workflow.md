---
type: canonical
status: canonical
updated: 2026-08-23
review_by: 2027-02-23
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

Vor Design eines Web-Produkts wird eine konkrete Leitreferenz gesucht. Pflichtartefakt im Projekt ist eine Entscheidungsmatrix mit:

`Website -> direkte URL -> Passung zu Branche/Zielgruppe/Inhalt -> tragende Prinzipien -> Übernahmetiefe -> bewusste Abweichungen -> tatsächlicher Einsatz -> Nachweis`

Mindestens der [[90-References/Website Reference Pool]] wird geprüft. Aktuelle Wettbewerber oder fachnahe Produkte dürfen ergänzt werden, wenn ihre direkte Live-URL dokumentiert wird. Sammlungs-, Galerie-, Award- und Stilbibliotheksseiten sind nur Recherchewege und niemals die Leitreferenz selbst. Ein Ergebnis darf nach ernsthafter Suche `Eigenentwurf` lauten, aber nicht, dass die Prüfung entfällt.

## Pflichtumfang je Web-Produkt

Verbindlich sind:

- **Pro Website genau eine konkrete primäre Leitreferenz wählen**, wenn eine fachlich und gestalterisch sinnvolle Passung existiert. Sie darf Struktur, visuelle Sprache und Interaktionsidee gemeinsam prägen.
- **Mindestens drei plausible Kandidaten kurz vergleichen**, sofern der Pool drei fachlich sinnvolle Kandidaten enthält. Das verhindert die Wahl nach dem ersten attraktiven Screenshot; es ist keine Pflicht, unpassende Seiten aufzufüllen.
- **Bei mehreren Websites im Auftrag pro Website eine andere Leitreferenz.** Drei Versionen erhalten drei verschiedene Originalseiten. Keine Leitreferenz wird innerhalb desselben Auftrags wiederverwendet.
- **Passung vor Spektakel.** Branche, Angebotslogik, Zielgruppe, Inhaltsmenge, benötigte Beweise und Markenwirkung zählen stärker als Awards oder technische Effekte. Unter ähnlich passenden Kandidaten wird die professionellere und sinnvoll animationsreichere Seite bevorzugt.
- **Übernahmetiefe offen benennen:** `punktuell`, `teilweise` oder `prägend`, optional mit grober Prozentangabe. 20, 30, 60 oder 70 Prozent können gleichermaßen richtig sein; kein Mindestwert wird erzwungen.
- **Eigenentwurf als ehrlicher Fallback.** Findet sich keine starke Passung, wird `Eigenentwurf` mit den geprüften Kandidaten und dem Grund der Ablehnung dokumentiert. Dann wird kreativ aus Projektwahrheit und Brain-Regeln gestaltet, ohne eine beliebige Referenz künstlich aufzuzwingen.
- **Ergebnis in Sätzen, nicht in Stichworten.** Benannt werden konkrete Folgen für Auftakt, Raster, Sektionsdramaturgie, Typografie, Flächen, Medien und Motion sowie bewusste Abweichungen.

Der Nachweis liegt als Entscheidungsmatrix im Projekt und wird im Design Contract verlinkt. Negative Muster aus dem [[90-References/Inspiration Catalog]] können ergänzend helfen, sind aber weder Mindestmenge noch Ersatz für die positive Leitreferenz.

## Auswahl

1. Projektziel, Branche, Zielgruppe, Inhaltsart, Beweisformen, Plattform und Grenzen aus `PROJECT.md` extrahieren.
2. Im [[90-References/Website Reference Pool]] zuerst in der passenden Branchenkategorie suchen, dann bei Bedarf nach Wirkung oder Interaktionsniveau. Nur konkrete Live-Websites in die Shortlist aufnehmen.
3. Kandidaten nach `Branchenpassung`, `Angebots-/Inhaltspassung`, `Zielgruppenwirkung`, `übertragbarer Struktur`, `Motion-/Interaktionswert` und `technischer Machbarkeit` vergleichen. Fachliche Passung wiegt am stärksten.
4. Eine Leitreferenz wählen oder `Eigenentwurf` begründen. Bei mehreren Websites die Auswahl paarweise auf unterschiedliche Originalseiten prüfen.
5. Übernahmetiefe und konkrete Übertragung festlegen: Was wird an Grundstruktur, Auftakt, Raster, Typografie, Flächen, Medienführung, Sektionsdramaturgie und Motion übernommen, adaptiert oder verworfen?
6. Die Anordnung von Überschriften und den Aufbau der Landing Page zusätzlich gegen [[90-References/Derived Design Patterns#Anordnung von Überschriften]] und [[90-References/Derived Design Patterns#Landing Page mit Ausdruck]] prüfen.
7. Auswahl gegen Accessibility, Performance, Content-Wahrheit, reale Markenidentität, technische Machbarkeit und Wartung abwägen. Inhalte, Claims, Identitätsmerkmale, Logos und rechtliche Aussagen der Referenz werden nicht auf das neue Unternehmen übertragen.

## Evidenz erfassen

Für die gewählte Leitreferenz und alle tatsächlich übernommenen interaktiven Prinzipien festhalten:

- Name, direkte URL, Abrufdatum und Prüfer
- Browser, Viewport, Eingabemethode, Netzprofil und relevante Präferenzen
- Zeitpunkt oder beobachtbares Bereitschaftssignal der Aufnahme
- statischer Screenshot für Layout und sichtbaren Zustand
- Interaktionsprotokoll für Trigger, Ablauf, Dauer, Ursache/Wirkung und Abbruch
- Mobile-, Tastatur- und Reduced-Motion-Verhalten
- Lade-, Fehler- und Fallbackzustand bei Medien, Canvas, 3D oder Ton
- Scroll-Map je primärer Route: kontinuierliche Scrollsequenz, weitere Scroll-/In-View-Bewegungen, Trigger/Ranges und Rückwärts-Scroll

Für abgelehnte Shortlist-Kandidaten genügen direkte URL, Abrufdatum und ein kurzer, konkreter Ablehnungsgrund. Eine vollständige Browserbeweissammlung ist nur für die gewählte Leitreferenz erforderlich.

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

- genau eine konkrete Leitreferenz je Website oder nachvollziehbar begründeter `Eigenentwurf`
- bei mehreren Websites paarweise verschiedene Leitreferenzen
- keine Sammlung, Galerie, Award-Liste oder Stilbibliothek als Leitreferenz
- Passungsbegründung, Übernahmetiefe, konkrete Übernahmen und bewusste Abweichungen
- statische und interaktive Aussagen getrennt belegt
- Desktop, Mobil, Tastatur und Reduced Motion beurteilt
- tatsächlicher Einsatz und technische Risiken dokumentiert
- Entscheidung im Design Contract verlinkt

[^video]: [Playwright: Videos](https://playwright.dev/docs/videos)
[^emulation]: [Playwright: Emulation, Reduced motion](https://playwright.dev/docs/emulation#reduced-motion)
[^load]: [Playwright: Page waitForLoadState](https://playwright.dev/docs/api/class-page#page-wait-for-load-state)
