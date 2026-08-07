---
type: canonical
status: canonical
updated: 2026-08-06
review_by: 2027-02-03
depends_on:
  - "[[90-References/Inspiration Catalog]]"
impacts:
  - design-direction
  - motion
  - project-master-spec
  - qa
---

# Reference Research Workflow

## Pflicht und Ergebnis

Vor Design eines Web-Produkts wird Inspiration recherchiert. Pflichtartefakt im Projekt ist eine Entscheidungsmatrix mit:

`Quelle -> Rolle -> beobachtetes Prinzip -> Eignung für Ziel/Nutzer -> direkter Einsatz/Adaption -> tatsächlicher Einsatz -> Nachweis`

Mindestens der [[90-References/Inspiration Catalog]] wird geprüft. Aktuelle Wettbewerber oder fachnahe Produkte dürfen ergänzt werden. Ein Ergebnis darf lauten, dass keine Referenz übernommen wird, aber nicht, dass die Prüfung entfällt.

## Pflichtumfang je Web-Produkt

Eine oberflächliche Sichtung genügt nicht. Verbindlich sind:

- **Mindestens acht Referenzen aus dem Katalog erneut ansehen**, davon mindestens zwei aus den generierten und experimentellen Websites, mindestens drei aus den professionellen Produkt- und Plattformseiten und mindestens zwei aus den kreativen Studios und Portfolios.
- **Mindestens zwei ausdrückliche Negativreferenzen** benennen, etwa DataFlow oder Animated SaaS, und daraus konkret ableiten, welches Muster die eigene Seite nicht übernimmt.
- **Je gewählter Rolle** eine Referenz mit konkretem, benanntem Prinzip: Struktur, visuelle Sprache und Interaktionsidee.
- **Bei mehreren Websites im Auftrag** je Website eine eigene Referenzkombination. Zwei Websites dürfen nicht aus denselben Referenzen entstehen, sonst unterscheiden sie sich nur in Farbe.
- **Ergebnis in Sätzen, nicht in Stichworten.** Für jede Referenz wird notiert, welche Kompositionsentscheidung sie konkret auslöst, etwa „Überschrift links neben dem Inhalt statt darüber, wie in der Sektionsführung von Linear“.

Der Nachweis liegt als Entscheidungsmatrix im Projekt und wird im Design Contract verlinkt.

## Auswahl

1. Projektziel, Zielgruppe, Inhaltsart, Plattform und Grenzen aus `PROJECT.md` extrahieren.
2. Kandidaten getrennt für **Struktur**, **visuelle Sprache** und **Interaktionsidee** suchen.
3. Pro Rolle höchstens einen Kandidaten auswählen; eine Quelle darf mehrere Rollen nur mit getrennten Prinzipien belegen.
3a. Zusätzlich die Anordnung von Überschriften und den Aufbau der Landing Page gezielt gegen [[90-References/Derived Design Patterns#Anordnung von Überschriften]] und [[90-References/Derived Design Patterns#Landing Page mit Ausdruck]] prüfen und die gewählte Anordnung benennen.
4. Gewünschte Bilder, Designs, Animationen, Texte, Assets, Quellcode oder Kompositionen für direkten Einsatz oder kreative Adaption bestimmen.
5. Auswahl gegen Accessibility, Performance, Content-Wahrheit, technische Machbarkeit und Wartung abwägen. Diese Prüfung optimiert die Umsetzung und erzeugt keine Herkunfts- oder Asset-Sperre.

## Evidenz erfassen

Je geprüfter Version festhalten:

- Name, direkte URL, Abrufdatum und Prüfer
- Browser, Viewport, Eingabemethode, Netzprofil und relevante Präferenzen
- Zeitpunkt oder beobachtbares Bereitschaftssignal der Aufnahme
- statischer Screenshot für Layout und sichtbaren Zustand
- Interaktionsprotokoll für Trigger, Ablauf, Dauer, Ursache/Wirkung und Abbruch
- Mobile-, Tastatur- und Reduced-Motion-Verhalten
- Lade-, Fehler- und Fallbackzustand bei Medien, Canvas, 3D oder Ton
- Scroll-Map je primärer Route: kontinuierliche Scrollsequenz, weitere Scroll-/In-View-Bewegungen, Trigger/Ranges und Rückwärts-Scroll

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

- eindeutige Rolle und konkreter Einsatz oder kreative Adaption je gewählter Referenz
- statische und interaktive Aussagen getrennt belegt
- Desktop, Mobil, Tastatur und Reduced Motion beurteilt
- tatsächlicher Einsatz und technische Risiken dokumentiert
- Entscheidung im Design Contract verlinkt

[^video]: [Playwright: Videos](https://playwright.dev/docs/videos)
[^emulation]: [Playwright: Emulation, Reduced motion](https://playwright.dev/docs/emulation#reduced-motion)
[^load]: [Playwright: Page waitForLoadState](https://playwright.dev/docs/api/class-page#page-wait-for-load-state)
