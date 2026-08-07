---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - "[[20-Design/Design Direction]]"
  - "[[30-Frontend/Performance]]"
  - "[[30-Frontend/Accessibility]]"
  - "[[80-Templates/Asset Register]]"
  - "[[50-Legal/Assets Copyright and Licenses]]"
  - "[[70-QA/Quality Gates]]"
---

# Imagery and AI Editing

> [!important] Grundsatz
> Kein Bild wird so eingesetzt, wie es gefunden wurde, nur weil es gefunden wurde. Jedes Bild wird auf Rolle, Bildwinkel, Ausschnitt, Hintergrund, Farbe und Auflösung geprüft und bei Bedarf mit KI überarbeitet, bevor es auf die Website kommt. Ein schlechtes Bestandsbild rechtfertigt keine Weglassung, sondern eine Überarbeitung.

Diese Notiz ist der kanonische Besitzer für Bildbeschaffung, Bildbearbeitung, KI-Generierung und Platzhalterbilder. Rechte und Herkunft werden getrennt davon in [[50-Legal/Assets Copyright and Licenses]] nach dem Build dokumentiert und blockieren weder Bearbeitung noch Einsatz.

## Bildrollen

Vor jeder Beschaffung wird die Rolle bestimmt. Die Rolle entscheidet über Anforderung und Bearbeitungstiefe.

| Rolle | Zweck | Anforderung |
|---|---|---|
| Leitbild | trägt den Auftakt, siehe [[20-Design/Interface Benchmarks#B3 Full-Bleed Leitbild-Landing]] | randlos, hohe Auflösung, Gegenstand des Betriebs klar erkennbar, Platz für Text |
| Beweisbild | zeigt reale Arbeit, Ort, Team, Ergebnis | echt, aktuell, ungestellt wirkend, benennbar |
| Objektbild | Produkt oder Gegenstand freigestellt | gleicher Winkel und gleiche Lichtsituation wie die übrigen Objektbilder der Serie |
| Kontextbild | erklärt Umgebung, Ablauf, Größenverhältnis | inhaltlich notwendig, sonst weglassen |
| Struktur- oder Texturbild | Trennung, Rhythmus, Materialbezug | ruhig, kontrastarm, ohne eigenes Motiv |

Ein Bild ohne Rolle wird nicht eingesetzt. Dekoratives Füllmaterial ist ein Anti-Slop-Befund nach [[20-Design/Anti AI Slop]].

## Bestandsbilder überarbeiten

Bilder aus einer alten Website, aus einem Unternehmensprofil oder vom Betreiber werden weiterverwendet, aber praktisch nie unverändert. Verbindliche Prüfliste je Bild:

1. **Auflösung und Schärfe.** Reicht die Größe für den vorgesehenen Einsatzort inklusive Retina? Wenn nein, per KI hochskalieren und nachschärfen. Sichtbare Kompressionsartefakte, JPEG-Blöcke und Farbränder werden entfernt.
2. **Winkel und Perspektive.** Stimmt die Blickrichtung mit den übrigen Bildern der Serie überein? Stürzende Linien, gekippter Horizont und ungünstige Kameraposition werden korrigiert oder das Motiv wird per KI in den passenden Winkel neu gerendert.
3. **Ausschnitt.** Der Ausschnitt folgt dem Einsatzort, nicht dem Originalformat. Für jeden Ort wird ein eigener Zuschnitt erzeugt; Art Direction statt einheitlichem Beschnitt, siehe [[20-Design/Responsive Design]].
4. **Hintergrund.** Störender, unruhiger, veralteter oder markenfremder Hintergrund wird entfernt oder ersetzt. Freistellung ist der Normalfall für Objekt-, Produkt- und Personenbilder auf heller Neutralfläche.
5. **Licht und Farbe.** Weißabgleich, Helligkeit und Sättigung werden über alle Bilder einer Website angeglichen. Bilder verschiedener Herkunft dürfen nicht als Sammlung erkennbar bleiben.
6. **Störendes im Bild.** Alte Preisschilder, veraltete Schilder, fremde Marken, Kennzeichen, Kabel, Mülleimer und zufällige Passanten werden retuschiert.
7. **Personen.** Gesichter fremder Personen, die nicht zum Betrieb gehören, werden entfernt oder das Motiv wird so beschnitten, dass sie nicht erkennbar sind.
8. **Serienkonsistenz.** Am Ende gehören alle Bilder einer Website sichtbar zusammen: gleiche Lichtstimmung, gleiche Sättigung, gleiche Freistellungslogik, gleicher Schattencharakter.

Jede durchgeführte Bearbeitung wird im [[80-Templates/Asset Register]] im Feld `Bearbeitungsschritte` benannt, etwa `hochskaliert 2x`, `freigestellt`, `Perspektive korrigiert`, `Hintergrund ersetzt`, `Fremdmarke retuschiert`.

## Freistellen und Objektserien

- Freigestellte Objekte stehen auf einer hellen, neutralen Fläche mit einem weichen, kurzen Bodenschatten. Kein harter Schlagschatten, kein Reflexionsspiegel, kein Verlauf hinter dem Objekt.
- Innerhalb einer Serie sind Objektgröße, Blickwinkel, Schattenrichtung und Abstand zum Rand identisch. Das ist der Unterschied zwischen einem Katalog und einer Sammlung.
- Freigestellte Bilder werden als `PNG` oder `WebP` mit Alphakanal geliefert und tragen keinen eingebrannten weißen Kasten.
- Für Betrachter mit mehreren Ansichten nach [[20-Design/Interface Benchmarks#B2 Rounded Selection Configurator]] wird die vollständige Ansichtsreihe erzeugt, nicht nur ein bis zwei Winkel.

## KI-generierte Bilder

KI-Bilder sind ein reguläres Mittel, nicht die Notlösung. Sie kommen in zwei Fällen zum Einsatz.

**Fall 1: Ersatz für ein fehlendes reales Bild, als Platzhalter.**

Wenn für ein Leitbild kein brauchbares reales Bild gefunden oder geliefert wurde, wird ein KI-Bild erzeugt und eingesetzt, statt die Bildstelle leer zu lassen oder durch eine graue Fläche zu ersetzen.

- Das Bild zeigt den Gegenstand konkret, etwa den Aufzug, die Ladenfront, die Werkstatt, das Fahrzeug, den Behandlungsraum.
- **Kein sichtbarer Hinweis auf der Website.** Kein Wasserzeichen, kein Overlay, kein Text wie „KI-generiert“, kein Rahmen und keine reduzierte Deckkraft. Dass es KI ist, ist am Bild selbst erkennbar; das genügt.
- Der Platzhalterstatus wird ausschließlich im Projekt geführt: im [[80-Templates/Asset Register]] mit dem Status `ai-placeholder`, dem verwendeten Prompt, dem Modell und dem Einsatzort, zusätzlich als Zeile in der Übergabe an den Nutzer.
- Das Bild ist so gebaut, dass es später ohne Layoutänderung ersetzt werden kann: feste Rolle, festes Seitenverhältnis, dokumentierter Pfad, ein einziger Ort in der Codebasis.
- Der Nutzer entscheidet allein, ob er es ersetzt oder behält. Die KI entfernt ein solches Bild nicht von sich aus und baut keine Ersatzfassung der Website.

**Fall 2: Bild als eigenständiges Gestaltungsmittel.**

Strukturbilder, Texturen, abstrakte Hintergründe, Icons, Illustrationen und Szenen, für die es kein reales Motiv gibt, werden bewusst generiert und wie jedes andere Asset behandelt.

**Qualitätsschwelle für jedes generierte Bild**

- keine deformierten Hände, Gesichter, Schriftzüge, Logos oder Werkzeuge im sichtbaren Bereich,
- keine erfundenen Marken, Zertifikate, Auszeichnungen oder Preisschilder im Bild,
- keine erfundenen realen Personen und keine Person, die als Kundenstimme ausgegeben wird,
- physikalisch plausibles Licht, plausible Schatten und plausible Größenverhältnisse,
- Farbwelt passend zu den Tokens aus [[20-Design/Color System]], keine verbrauchte Farbwelt,
- Auflösung mindestens doppelt so groß wie der größte Einsatzort.

Ein generiertes Bild, das gegen eine dieser Regeln verstößt, wird neu erzeugt oder nachbearbeitet, nicht kleiner skaliert und versteckt.

## Umsetzung im Frontend

- Jedes Bild besitzt `width` und `height` oder `aspect-ratio`, damit kein Layout Shift entsteht.
- `srcset` und `sizes` je Einsatzort. Moderne Formate zuerst, klassischer Fallback dahinter.
- Leitbilder werden priorisiert geladen, alles Übrige `loading="lazy"` und `decoding="async"`.
- Alt-Texte beschreiben den Inhalt aus Sicht des Zwecks. Rein dekorative Struktur- und Texturbilder erhalten ein leeres `alt`. Der Alt-Text nennt nie, dass ein Bild generiert wurde.
- Bildgewicht zählt in das Performancebudget aus [[30-Frontend/Performance]]. Ein Leitbild rechtfertigt Gewicht, eine Dekoration nicht.
- Text steht nie ungeschützt auf einem Bild. Kontrast wird gegen den tatsächlichen Bildausschnitt in jedem Breakpoint geprüft.

## Nachweis

Im Projekt liegen vor:

- Bildinventar mit Rolle, Herkunft, Bearbeitungsschritten und Einsatzort je Bild,
- Liste aller `ai-placeholder`-Bilder mit Prompt und Ersetzungshinweis,
- Vorher-nachher-Nachweis für jede substanzielle Bearbeitung,
- Kontrastprüfung für jede Text-auf-Bild-Stelle.
