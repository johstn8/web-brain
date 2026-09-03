---
type: canonical
status: canonical
updated: 2026-09-03
depends_on:
  - "[[10-Strategy/Information Architecture and Sitemap]]"
impacts:
  - "[[10-Strategy/Content and Conversion]]"
  - "[[20-Design/Design Direction]]"
  - "[[20-Design/Responsive Design]]"
  - "[[30-Frontend/Components and UI States]]"
  - "[[70-QA/Quality Gates]]"
---

# Information Density and Mobile Clarity

> [!important] Grundsatz
> Eine Website ist erst gut, wenn sie ohne Anstrengung verstanden wird. Sie zeigt genug, um die Frage des Nutzers zu beantworten, und nicht mehr. Der Maßstab dafür ist immer das Mobilgerät: Dieselbe Informationsmenge wirkt auf einem schmalen Display deutlich größer als im Entwurf am Desktop.

Diese Notiz ist der kanonische Besitzer für Informationsmenge, Textlänge und Verständlichkeit. Tonalität und Beweisführung bleiben bei [[10-Strategy/Content and Conversion]], Formulierung, Satzform und verbotene Textmuster bei [[10-Strategy/Website Copy]], die Seitenaufteilung bei [[10-Strategy/Information Architecture and Sitemap]].

## Eine Frage pro Abschnitt

Jeder Abschnitt beantwortet genau eine Frage eines realen Nutzers und wird nach dieser Frage benannt, nicht nach einem Schema. Beantwortet ein Abschnitt keine Frage, wird er gelöscht statt gekürzt.

Die Reihenfolge folgt der Reihenfolge, in der die Fragen entstehen:

1. Was ist das und für wen?
2. Was bekomme ich konkret?
3. Woran sehe ich, dass es stimmt?
4. Was kostet es, wie lange dauert es, was ist die Bedingung?
5. Was ist der nächste Schritt?

Eine Sektion, die zwei dieser Fragen mischt, wird geteilt. Eine Sektion, die eine Frage zum zweiten Mal beantwortet, wird entfernt.

## Textbudget

Richtwerte, die im Design Contract für das jeweilige Projekt bestätigt oder begründet geändert werden.

| Element | Budget |
|---|---|
| Seitentitel und Sektionsüberschrift | höchstens 8 Wörter, auf Mobil höchstens 2 Zeilen |
| erklärender Text unter einer Überschrift | ein bis drei ganze Sätze, zusammen höchstens 45 Wörter. Ein verbloses Fragment ist keine zulässige Fassung, siehe [[10-Strategy/Website Copy#Die Statementzeile unter der Überschrift]] |
| Fließtextabsatz | höchstens 3 Sätze, ein Gedanke |
| Karten- oder Listeneintrag | Titel bis 4 Wörter, Beschreibung eine Zeile |
| Aufzählung | 2 bis 6 Punkte, je höchstens eine Zeile. Die Anzahl folgt der Sache; drei Punkte nur, wenn es sachlich drei sind, siehe [[10-Strategy/Website Copy#Die Dreierfigur]] |
| Beschriftung eines Bedienelements | 1 bis 3 Wörter, Ergebnis benennend |
| primäre Inhaltsroute gesamt | so viel Inhalt, dass ein Nutzer die Route in unter 90 Sekunden überfliegen kann |

Längere Sachtexte sind erlaubt, gehören aber auf eine eigene Detailseite und werden von der übergeordneten Seite nur angerissen und verlinkt. Eine Startseite ist keine Textseite.

## Sektionsbudget je Route

- Startseite: 5 bis 8 Abschnitte einschließlich Auftakt und Abschluss. Mehr bedeutet, dass Inhalte auf Unterseiten gehören.
- Unterseite: 3 bis 6 Abschnitte.
- Rechts- und Pflichtseiten: keine Begrenzung, aber mit Sprungnavigation gegliedert.

Jeder zusätzliche Abschnitt über dem Budget braucht eine benannte Nutzerfrage im Design Contract.

## Gestaffelte Tiefe

Information wird nicht weggelassen, sondern gestaffelt. Auf jeder Ebene steht nur, was zur Entscheidung auf dieser Ebene nötig ist.

- Ebene 1: die Aussage, sofort sichtbar.
- Ebene 2: Details in Akkordeon, Tabs, Detailseite oder Dialog, jeweils mit sprechender Beschriftung.
- Ebene 3: vollständige Daten, Tabellen, Bedingungen, Dokumente.

Regeln dafür: Ebene 2 wird nie für den Kernnutzen verwendet. Ein zugeklapptes Element trägt eine Beschriftung, die seinen Inhalt verrät. Auf Mobil ist Ebene 2 der Normalfall, auf Desktop darf mehr davon offen liegen. Der Inhalt bleibt in allen Fällen im DOM auffindbar und suchbar.

## Mobile zuerst dosieren

Die Aufmerksamkeit verteilt sich stark ungleich: die erste Bildschirmhöhe erhält rund 57 Prozent der Betrachtungszeit, die zweite etwa 17 Prozent. Für die Startseite folgen daraus eigene Regeln zur nutzbaren Höhe, zum Höhenbudget der Kopfzeile und zur sichtbaren Fortsetzung, kanonisch in [[20-Design/Landing Page Craft#Die erste Bildschirmhöhe]].

Die Informationsmenge wird am schmalsten Viewport entschieden und erst danach auf Desktop erweitert.

- Der Entwurf beginnt bei 375 Pixeln Breite. Was dort zu viel ist, ist überall zu viel.
- Innerhalb der ersten Bildschirmhöhe auf Mobil stehen: worum es geht, für wen, und die primäre Aktion. Nichts sonst.
- Innerhalb der zweiten Bildschirmhöhe beginnt sichtbar die nächste reale Nutzerfrage oder der erste konkrete Beweis. Ein großer Titel, Kontaktdaten, Dekoration oder Weißraum dürfen nicht zwei Bildschirmhöhen lang dieselbe Aussage fortsetzen.
- Ein Bildschirm auf Mobil zeigt höchstens einen abgeschlossenen Gedanken. Wer scrollt, soll etwas Neues finden, nicht dieselbe Aussage in neuer Verpackung.
- Vier gleichartige Karten nebeneinander am Desktop werden auf Mobil nicht zu vier gleich hohen Blöcken untereinander. Sie werden zu einer kompakten Liste, einer horizontal geführten Reihe mit sichtbarem Fortschritt oder zu einer gekürzten Auswahl mit Verweis auf die Detailseite.
- Lange Tabellen erhalten auf Mobil eine echte alternative Darstellung, siehe [[20-Design/Responsive Design]].
- Zahl der Bedienelemente pro Bildschirm auf Mobil klein halten. Eine primäre Aktion ist sichtbar, alles Weitere ist sekundär gestaltet.
- Bewegung wird auf Mobil nicht gestrichen, aber sie darf die Lesbarkeit nie verringern. Regeln in [[20-Design/Motion and Interaction]].

## Selbsterklärend

- Beschriftungen benennen das Ergebnis, nicht die Technik. `Termin anfragen` statt `Formular`.
- Jede Zahl trägt Einheit, Bezugsgröße und Zeitraum. Ohne Bezug wird sie weggelassen.
- Abkürzungen und Fachbegriffe werden beim ersten Auftreten in derselben Zeile erklärt oder ersetzt.
- Der aktuelle Ort in der Website ist immer erkennbar.
- Ein Nutzer, der die Branche nicht kennt, versteht Auftakt und primäre Aktion ohne Rückfrage. Das wird an einer realen Person oder mindestens an einer schriftlichen Gegenprobe geprüft.
- Icons erscheinen nie ohne Beschriftung, außer bei allgemein bekannten Symbolen wie Suche, Schließen und Menü.

## Prüffragen vor der Abnahme

- Lässt sich jeder Abschnitt einer Nutzerfrage zuordnen?
- Gibt es zwei Abschnitte, die dieselbe Aussage tragen?
- Überschreitet ein Textblock sein Budget?
- Wie viele Bildschirmhöhen braucht die Startseite auf 375 Pixeln, und passiert auf jeder etwas Neues?
- Ist auf Mobil in der ersten Bildschirmhöhe die primäre Aktion sichtbar?
- Beginnt auf Mobil innerhalb der zweiten Bildschirmhöhe eine neue Nutzerfrage oder ein konkreter Beweis?
- Steht irgendwo eine Zahl ohne Bezugsgröße?
- Kann ein Abschnitt ersatzlos entfallen, ohne dass eine Frage unbeantwortet bleibt? Dann entfällt er.
