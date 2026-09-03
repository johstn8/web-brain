---
type: canonical
status: canonical
updated: 2026-09-03
sources_checked: 2026-09-03
review_by: 2027-03-01
depends_on:
  - "[[20-Design/Design Direction]]"
  - "[[10-Strategy/Information Density and Mobile Clarity]]"
  - "[[20-Design/Interface Benchmarks]]"
impacts:
  - "[[20-Design/Anti AI Slop]]"
  - "[[20-Design/Design Direction]]"
  - "[[30-Frontend/Components and UI States]]"
  - "[[10-Strategy/Content and Conversion]]"
  - "[[70-QA/Quality Gates]]"
---

# Landing Page Craft

> [!important] Rang
> Diese Notiz ist der kanonische Besitzer für Aufbau, Auftaktkomposition, Überschriftenanordnung, Kopfzeilenrolle, Beweisreihenfolge und Handlungsdichte der Startseite beziehungsweise Landing Page sowie für die konkrete Abgrenzung zwischen professioneller und generierter Anmutung an dieser Seite.
> Angrenzende Besitzer bleiben unverändert: [[20-Design/Design Direction]] für die Art Direction der gesamten Website, [[10-Strategy/Information Density and Mobile Clarity]] für Informationsmenge und Textbudget, [[10-Strategy/Website Copy]] für Formulierung, [[10-Strategy/Content and Conversion]] für Kernbotschaft und Beweis-Hierarchie, [[30-Frontend/Components and UI States]] für Kopfzeilengeometrie und Komponentenverträge, [[20-Design/Anti AI Slop]] für den vollständigen Befundkatalog.

## Warum diese Seite eine eigene Notiz hat

Die Landing Page ist die einzige Seite, die eine Entscheidung auslöst, bevor sie gelesen wird. Alle anderen Seiten werden von jemandem betreten, der sich bereits entschieden hat weiterzugehen. Deshalb gilt hier ein höherer Anspruch, und deshalb ist hier auch der Schaden am größten, wenn die Seite aussieht wie jede andere generierte Seite.

## Die drei Zeitfenster

Der Auftakt wird in drei getrennten Zeitfenstern beurteilt. Jedes hat eine eigene Aufgabe, und eine Seite kann das erste bestehen und am zweiten scheitern.

| Fenster | Was passiert | Was die Seite dafür braucht |
|---|---|---|
| unter 100 ms | rein visuelles Urteil, noch ohne Lesen | eine ruhige, gegliederte, im Umriss vertraute Fläche. Geringe visuelle Komplexität und eine erkennbare Grundordnung schlagen Originalität in diesem Fenster.[^google50] |
| etwa 5 Sekunden | erste Lesebewegung | Was ist das, für wen, und was ist der nächste Schritt. Wer das nicht beantworten kann, verlässt die Seite.[^fivesecond] |
| erste zwei Bildschirmhöhen | Entscheidung weiterzugehen | ein konkreter Beweis oder die nächste reale Nutzerfrage muss sichtbar begonnen haben |

Die Aufmerksamkeit ist über die Seite hinweg stark ungleich verteilt: die erste Bildschirmhöhe erhält rund 57 Prozent der Betrachtungszeit, die zweite etwa 17 Prozent, der Rest verteilt sich in einem langen Ausläufer. Innerhalb der ersten Bildschirmhöhe liegt der größte Teil davon in der oberen Hälfte.[^nngscroll]

Zwei Folgerungen für den Entwurf:

- **Ungewöhnlichkeit kostet dort am meisten, wo sie die Orientierung kostet.** Ein eigenwilliges Raster, eine eigenwillige Farbwelt und ein eigenwilliges Medium sind erlaubt. Eine eigenwillige Grundordnung, in der nicht erkennbar ist, was Marke, was Aussage und was Handlung ist, ist es nicht.
- **Der obere Rand der ersten Bildschirmhöhe ist der teuerste Platz der Website.** Was dort steht, wird bewusst hingesetzt und nicht von Kopfzeile, Cookie-Leiste, Dekoration oder ungenutztem Weißraum belegt.

## Es gibt keinen Standardaufbau, sondern eine Standardaufgabe

Die verbreitete Reihenfolge aus Hero, drei Karten, Logo-Wand, Kundenstimmen, Preistabelle, FAQ und Abschluss-CTA ist kein Aufbau, sondern eine Gewohnheit. Sie ist der häufigste einzelne Grund, warum eine Seite generiert wirkt.

Der Aufbau entsteht stattdessen aus der Reihenfolge, in der beim realen Besucher Fragen und Einwände entstehen. Die Grundreihenfolge steht in [[10-Strategy/Information Density and Mobile Clarity#Eine Frage pro Abschnitt]]. Diese Notiz ergänzt, wie sich die Reihenfolge nach Seitentyp verschiebt und welche Beweisform jeweils zuerst trägt.

| Seitentyp | Erste echte Frage | Stärkste erste Beweisform | Was hier typischerweise falsch zuerst kommt |
|---|---|---|---|
| lokaler Dienstleister oder Betrieb | Macht ihr das, was ich brauche, und wie erreiche ich euch | der reale Ort, das reale Fahrzeug, die reale Werkstatt, das Team bei der Arbeit | eine abstrakte Nutzenüberschrift ohne Ort und ohne Gegenstand |
| Praxis, Kanzlei, Beratung | Wer behandelt oder berät mich, und wie läuft das ab | Personen, Räume, Ablauf, Terminweg | Kundenstimmen vor der Vorstellung der Personen |
| Handwerk und Bau | Könnt ihr so etwas wie meines, und was hat es gekostet | eine abgeschlossene Arbeit mit Ausgangslage und Ergebnis | eine Leistungsliste ohne ein einziges Ergebnis |
| Produkt oder Software | Was macht das Ding, wenn ich es benutze | die reale Oberfläche, ein Ausschnitt daraus, ein bedienbares Modul | Feature-Karten vor der ersten Produktansicht |
| Studio, Portfolio, Agentur | Wie sieht eure Arbeit aus | die Arbeit selbst, groß, mit Auftraggeber und Aufgabe | ein Manifest über die eigene Haltung vor der ersten Arbeit |
| Verzeichnis oder Katalog | Finde ich hier, was ich suche | die Suche oder der Index selbst als Auftakt | ein Marketingauftakt vor dem Suchfeld |
| Veranstaltung | Was, wann, wo, für wen, was kostet es | Datum, Ort, Programm, Preis in einer Zeile | eine Stimmungsfläche ohne Datum |
| Kampagnen- oder Anzeigenziel | Bekomme ich, was mir versprochen wurde | die wortgleiche Wiederaufnahme des Versprechens aus Anzeige oder Mail | ein allgemeiner Firmenauftakt statt des versprochenen Angebots |

Ein Abschnitt, der keine dieser Fragen beantwortet, wird gelöscht, nicht gekürzt. Ein Abschnitt, der eine bereits beantwortete Frage erneut beantwortet, ebenfalls.

## Der Auftakt: sechs Rollen, eine Komposition

Ein Auftakt besteht nicht aus Blöcken, sondern aus Rollen. Jede Rolle muss besetzt sein. Wie sie besetzt wird, ist frei.

| Rolle | Was sie beantwortet | Übliche, aber nicht zwingende Form |
|---|---|---|
| Identität | Bei wem bin ich | Logo, Wortmarke, Ortsangabe, Absender im Bild |
| Angebot | Was ist das | die semantische H1 |
| Einordnung | Für wen, wo, unter welcher Bedingung | Lead, Faktenzeile, Bildunterschrift, Metazeile |
| Beweisanker | Woran sehe ich, dass es stimmt | reales Objekt, Ort, Arbeit, Oberfläche, Rechner, Ablauf, Dokument |
| Handlung | Was tue ich jetzt | primäre Aktion, gegebenenfalls eine klar andersartige zweite |
| Fortschritt | Geht es weiter, und wohin | angeschnittene Folgesektion, Kapitelmarke, Faktenband, Sprungziel |

Die Rolle `Beweisanker` ist die, die in generierten Auftakten fast immer fehlt. Stimmung, große Schrift und leere Fläche besetzen sie nicht. Ein Bild besetzt sie nur dann, wenn darauf tatsächlich der Gegenstand des Betriebs zu sehen ist.

Die Rolle `Fortschritt` ist die, die am zweithäufigsten fehlt. Ein Auftakt, der die Bildschirmhöhe exakt füllt und sauber abschließt, sieht fertig aus, und ein fertiger Bildschirm wird nicht gescrollt. Das ist die Illusion der Vollständigkeit.[^completeness] Ein absichtlich angeschnittener Folgeinhalt, eine über die Kante laufende Bildkante oder eine halb sichtbare Faktenzeile lösen sie auf. Ein Pfeil nach unten ist die schwächste und generischste Lösung dieses Problems.

## Auftakt-Repertoire

Die Auftaktkomposition wird gewählt, nicht geerbt. Die folgende Liste ist ein Entscheidungsraum, keine Rangfolge. Genau eine Komposition wird gewählt und im Design Contract begründet.

| Komposition | Wie sie funktioniert | Passt zu | Woran sie scheitert |
|---|---|---|---|
| **Randloses Leitbild** | ein einziges großes Bild trägt die Fläche, Text liegt auf einer geprüften Zone darin | Betriebe, Orte, Anlagen, Gastronomie, alles Fotografierbare | schwaches Bildmaterial, Text über unruhigem Bereich, Kontrast nur im Entwurf geprüft |
| **Asymmetrischer Split mit Überlappung** | Typografie und Medium teilen sich das Raster und überlappen in zwei bis drei Spalten | Produkt, Studio, Kampagne | fehlende Ausrichtungsachse, Überlappung, die Text verdeckt |
| **Typo-Auftakt mit Faktenspur** | keine Bildfläche, dafür Überschrift plus eine Zeile echter Fakten wie Ort, Zeitraum, Preisrahmen, Kapazität | Dienstleistung ohne gutes Bildmaterial, B2B, Beratung | Übergröße ohne Fakten, dann bleibt nur Dekoration |
| **Werkzeug zuerst** | Rechner, Suchfeld, Konfigurator, Verfügbarkeitsprüfung steht im Auftakt und ist sofort bedienbar | Verzeichnis, Buchung, Preisfindung, Auswahl | ein Modul ohne reale Daten, oder eines, das nur so aussieht |
| **Beweis zuerst** | eine abgeschlossene Arbeit, ein Objekt oder eine Oberfläche steht groß, die Überschrift steht als Bildunterschrift darunter | Portfolio, Handwerk, Fallstudien | die Arbeit ist nicht selbsterklärend und trägt keine Einordnung |
| **Index-Auftakt** | eine redaktionelle Liste, Tabelle oder Karte ist selbst der Auftakt | Katalog, Archiv, Programm, Speisekarte | ein Index ohne Filter, Sortierung oder Zustände |
| **Ortsfeste Bühne** | ein Medium bleibt stehen, der Text wechselt beim Scrollen | Produktkampagne mit mehreren gleichwertigen Aussagen | mehr als drei Wechsel, kein Fortschrittsgefühl, kein Reduced-Motion-Weg |
| **Kontaktauftakt** | Ort, Zeiten, Weg und Kontaktweg stehen bereits im Auftakt, gestaltet und nicht als Fußnote | lokale Dienste, deren häufigste Aufgabe der Kontakt ist | Kontaktdaten ohne Angebot, dann fehlt die Antwort auf die erste Frage |
| **Materialfläche** | eine kräftige, aus Marke oder Material hergeleitete Farb- oder Materialfläche ersetzt das Bild | Marken mit starker Farbherkunft, fehlendem Bildmaterial | eine Farbfläche ohne Herleitung, dann ist sie ein Verlauf mit anderen Mitteln |
| **Ruhiger Mittelsatz** | mittig gesetzter Titel, Unterzeile, eine Aktion, sehr viel Ruhe | Angebote, deren Wert gerade in Zurückhaltung liegt | wenn er ungeprüfter Default ist statt einer Entscheidung. Diese Komposition ist erlaubt und muss ausdrücklich begründet werden, weil sie zugleich die häufigste generierte Form ist |

**Novelty Budget bleibt gültig.** Höchstens ein bis zwei auffällige Mechaniken pro Bildschirmausschnitt, siehe [[20-Design/Design Direction#Premium-Heuristik]].

## Überschriften: Ort, Maßstab, Beziehung

Die Anordnung der Überschriften entscheidet mehr über die Anmutung als die Schriftwahl. Eine Seite, auf der jede Sektion mit Titel, Lead und Raster beginnt, wirkt generiert, auch wenn jedes einzelne Element gut ist.

**Regeln für die Landing Page:**

- Die semantische H1 ist der Anker der Auftaktkomposition, nicht ihre Überschrift. Sie steht dort, wo sie mit dem Beweisanker in Beziehung tritt: über ihm, neben ihm, unter ihm als Bildunterschrift, in ihn hineinragend oder um ihn herum gesetzt.
- **Zwei bis drei verschiedene Überschriftenanordnungen pro Landing Page.** Eine einzige wiederholte Anordnung wirkt generiert, mehr als drei wirken zufällig. Die Auswahl wird im Design Contract genannt.
- Die Anordnung folgt der Aufgabe des Abschnitts: erklärende Abschnitte vertragen die Überschrift seitlich, zählbare Abschnitte vertragen Ziffer und Wort in derselben Zeile, medienführende Abschnitte vertragen die Überschrift als Bildunterschrift, Zäsuren vertragen eine Überschrift zwischen zwei Blöcken.
- Der Abstand über einer Überschrift ist größer als der Abstand darunter. Eine Überschrift, die näher am vorangehenden Block steht als an ihrem eigenen Inhalt, zerstört den Lesefluss.
- Der Größenabstand zwischen zwei Stufen beträgt mindestens den Faktor 1,25. Stufen, die sich um wenige Pixel unterscheiden, erzeugen keine Hierarchie, sondern Unschärfe.
- Sektionsüberschriften dürfen typografisch groß, gebrochen, überlappend oder mit einem Medium verschränkt sein. Die einzige semantische H1 bleibt vollständig lesbar; Anschnitt ist ausschließlich an einem dekorativen Duplikat zulässig.
- Der Kicker über der Überschrift ist ein Befund, sobald er die Überschrift wiederholt oder mechanisch auf jedem Abschnitt erscheint. Echte Rubrik-, Datums-, Status- oder Prozessinformation darf eine eigene Stufe erhalten. Kanonisch in [[20-Design/Anti AI Slop#Kicker und Überschriften]].

Der Katalog der beobachteten Anordnungen mit ihren Belegen steht in [[90-References/Derived Design Patterns#Anordnung von Überschriften]].

## Die Kopfzeile auf der Landing Page

Die Kopfzeile ist auf dieser Seite kein neutrales Möbel. Sie verbraucht den teuersten Platz der Website und bestimmt, wie viele Auswege der Besucher im ersten Blick sieht.

- **Höhenbudget.** Die Kopfzeile belegt auf einem 375 Pixel breiten Gerät höchstens etwa ein Achtel der sichtbaren Höhe. Alles darüber geht der Auftaktkomposition verloren.
- **Aufmerksamkeitsverhältnis.** Auf einer reinen Kampagnenseite mit genau einem Ziel ist das Verhältnis von anklickbaren Wegen zu Zielen idealerweise eins zu eins; jeder zusätzliche Weg ist ein Ausgang.[^attentionratio] Eine Unternehmensstartseite hat dagegen mehrere legitime Ziele und braucht eine vollständige Navigation. Der Design Contract benennt, welcher der beiden Fälle vorliegt, und begründet daraus das Kopfzeileninventar.
- **Aktion in der Kopfzeile.** Eine Aktion gehört dorthin, wenn sie über die gesamte Seite hinweg dieselbe bleibt und häufig gebraucht wird, etwa Termin, Anfrage, Anruf. Sie unterscheidet sich sichtbar von den Navigationslinks und ist auf Touch mindestens 48 mal 48 Pixel groß. Zwei gleich starke Aktionen in der Kopfzeile sind ein Befund.
- **Über dem Leitmedium.** Eine über dem Auftaktbild transparente Kopfzeile ist eine gültige Entscheidung, aber nie eine Voreinstellung. Sie braucht einen geprüften Kontrast gegen den tatsächlich darunterliegenden Bildbereich, einen Zustandswechsel beim Scrollen ohne Höhensprung und einen deckenden Fallback.
- Inventar, Muster, Geometrie, Prüfbreiten und das Repertoire möglicher Kopfzeilenformen sind kanonisch in [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]] geregelt.

## Die erste Bildschirmhöhe

Prüfmaß ist das Mobilgerät. Bei 375 Pixel Breite bleiben nach Adressleiste und Systemleisten grob 600 bis 700 Pixel nutzbare Höhe. In dieser Fläche stehen Angebot, Zielgruppe beziehungsweise Ort und die primäre Handlung.

- Die H1 wird so bemessen, dass sie mobil höchstens drei Zeilen belegt. Wenn sie das nicht tut, ist zuerst der Satz zu lang und erst danach die Schrift zu groß.
- Ein Auftaktbild darf die primäre Handlung nicht unter die Kante schieben.
- Fließtext unter 16 Pixel und Beschriftungen unter 11 Pixel sind ein Befund.
- Die vollständige H1 bleibt bei 320, 375, 768, 1280 und 1440 Pixel, bei 200 Prozent Zoom und bei großer Systemschrift ohne Anschnitt, Maske, Überlagerung und ohne Kollision mit der klebenden Kopfzeile lesbar.
- Spätestens innerhalb der zweiten Bildschirmhöhe beginnt sichtbar die nächste reale Nutzerfrage oder der erste Beweis, siehe [[10-Strategy/Information Density and Mobile Clarity]].

**Wahrgenommene Geschwindigkeit gehört zum ersten Eindruck.** Auf der Mehrzahl mobiler Seiten ist das LCP-Element ein Bild des Auftakts; ein Wert über 2,5 Sekunden wird als langsam erlebt, unabhängig davon, wie gut die Komposition ist.[^lcp] Das Auftaktmedium wird deshalb vorrangig geladen, in moderner Kodierung ausgeliefert und mit festen Maßen reserviert. Ein Auftakt, dessen Inhalt bis zum Ende einer Einblendung unsichtbar bleibt, ist ein Befund und kein Effekt.

## Beweis und Handlung über die Seite hinweg

- Die Rangfolge der Beweisformen ist kanonisch in [[10-Strategy/Content and Conversion#Beweis-Hierarchie]]. Diese Notiz regelt nur ihre Platzierung.
- Der erste Beweis steht innerhalb der ersten zwei Bildschirmhöhen. Er ist die stärkste Form, die für diesen Betrieb real verfügbar ist, nicht die am leichtesten zu gestaltende.
- Die Beweisdichte nimmt nach unten ab, die Konkretheit nimmt zu: oben das Sichtbare, in der Mitte das Nachvollziehbare, unten Bedingungen, Preise und Fristen.
- Die primäre Handlung wird an Entscheidungspunkten wiederholt, nicht in einem festen Rhythmus. Ein Entscheidungspunkt ist das Ende eines Beweises, das Ende einer Preis- oder Bedingungsangabe und das Seitenende.
- Pro Bildschirmausschnitt gibt es genau eine primäre Handlung. Eine sekundäre Handlung unterscheidet sich in der Form, nicht nur in der Farbe.
- Die Benennung bleibt über die gesamte Seite identisch. Wechselnde Bezeichnungen für dieselbe Handlung lesen sich als mehrere verschiedene Angebote.
- Kommt der Besucher aus einer Anzeige, einer Mail oder einem Profil, nimmt der Auftakt das dortige Versprechen wörtlich wieder auf. Eine Landing Page, die etwas anderes verspricht als ihre Quelle, verliert unabhängig von ihrer Qualität.

## Professionell gegen generiert

Der Unterschied liegt fast nie an einem einzelnen Element. Er liegt daran, ob eine Entscheidung getroffen und irgendwo festgehalten wurde. Generierte Seiten sehen einander ähnlich, weil bei fehlender Vorgabe immer dieselbe wahrscheinlichste Lösung entsteht.[^slopcause] Das Gegenmittel des Brains ist deshalb kein Stil, sondern der Design Contract.

| Ebene | Generiert | Professionell |
|---|---|---|
| Aufbau | feste Blockkette aus Hero, drei Karten, Logo-Wand, Stimmen, Preisen, FAQ | Reihenfolge aus den realen Fragen dieser Zielgruppe, jeder Abschnitt beantwortet genau eine |
| Auftakt | Badge, Überschrift, Unterzeile, zwei Buttons, mittig | eine gewählte Komposition aus dem Repertoire, mit besetztem Beweisanker |
| Beweis | erfundene Zahlen, Stimmen ohne Person, leere Logo-Wand | reale Arbeit, realer Ort, reale Oberfläche, benannte Fallstudie |
| Typografie | eine Standardfamilie in allen Rollen, Stufen zu nah beieinander | begründete Familie und Rollen, Stufen mit mindestens Faktor 1,25, kalibriertes Tracking |
| Farbe | Verlauf als Hochwertigkeitssignal, Palette ohne Herkunft | Farbrollen aus Marke, Material, Ort oder Produkt hergeleitet, Farbe überwiegend semantisch |
| Fläche | alles ist eine Karte mit gleicher Rundung | Karte, Zeile, Tabelle, Liste und Fließtext nach Informationsart gewählt |
| Bild | Bestandsbild, abstraktes 3D-Objekt, Verlauf als Bildersatz | reales Motiv, bearbeitet, im Raster verankert, mit Rolle in der Aussage |
| Bewegung | dieselbe Einblendung auf allem, Hover-Effekte ohne Ziel | Bewegung erklärt einen Zustand, einen Weg oder eine Beziehung |
| Copy | austauschbare Behauptungen, Buzzwords, Meta-Sätze | konkrete Fakten, ganze Sätze, Bedingungen nahe der Entscheidung |
| Detail | einheitliche Rundung überall, Hairline plus weiter Schatten, seitlicher Farbbalken | eine dokumentierte Radius-, Rahmen- und Tiefengrammatik |
| Zustände | nur der Ruhezustand ist gestaltet | Fokus, Laden, Fehler, Leer und Deaktiviert sind gestaltet |

Der vollständige Katalog erkennbarer Einzelsignaturen steht in [[20-Design/Anti AI Slop#Slop-Signaturen]]. Er wird bei jeder Landing Page durchgegangen.

**Der Umkehrschluss gilt nicht.** Eine Seite wird nicht dadurch professionell, dass sie ungewöhnlicher wird. Eine schlichte, ruhige, weitgehend statische Landing Page mit echtem Inhalt, sauberer Hierarchie und einem realen Beweis ist professioneller als eine expressive Seite ohne Gegenstand. Die Entscheidung für Ruhe wird genauso dokumentiert wie die für Ausdruck.

## Das Signaturdetail

Jede Landing Page erhält genau ein wiedererkennbares gestalterisches Detail, das aus dem Projekt selbst stammt und auf den Unterseiten in ruhigerer Form wiederkehrt. Es ersetzt die Sammlung austauschbarer Effekte durch ein Motiv.

Mögliche Träger: eine Maßlinie, eine Rasterkante, ein Schnittwinkel aus dem Logo, eine Materialkante, eine Ziffernlogik, eine wiederkehrende Bildbeschneidung, eine besondere Behandlung der Metazeile, eine Farbe, die ausschließlich an einer Stelle vorkommt.

Bedingungen: Es leitet sich aus Marke, Material, Ort, Produkt oder Inhalt her. Es funktioniert auch bei 320 Pixel und bei reduzierter Bewegung. Es ist ein Detail und keine zweite Art Direction. Es steht im Design Contract mit Herleitung und Wiederholungsorten.

## Feinschliff, der zuerst auffällt

Diese Punkte trennen einen sauberen Entwurf von einem fertigen. Sie werden am realen Render geprüft, nicht am Entwurf.

- Typografischer Feinschliff nach [[20-Design/Typography Layout and Spacing#Typografischer Feinschliff]]: Zeilenumbruch der H1, Schusterjungen, optischer Randausgleich, Ziffernform, Zeilenlänge.
- Optische statt mathematischer Ausrichtung: große Überschriften, freigestellte Objekte und Icons werden auf die wahrgenommene Kante ausgerichtet.
- Ein einziger Rhythmus für vertikale Abstände. Innerhalb einer Gruppe eng, zwischen Gruppen deutlich größer, zwischen Sektionen am größten.
- Gleiche Höhen für gleichrangige Controls. Uneinheitliche Buttonhöhen ohne funktionalen Grund sind ein Befund.
- Kein Layoutsprung beim Laden von Schrift und Auftaktmedium.
- Touchziele mindestens 48 mal 48 Pixel mit mindestens 8 Pixel Abstand.
- Jede Fläche, die sich beim Überfahren verändert, löst auch etwas aus.
- Der Fokus ist auf jedem tatsächlich vorkommenden Untergrund sichtbar, einschließlich Bild und dunklem Band.

## Prüffragen vor der Abnahme

Diese Fragen werden je gebauter Landing Page am laufenden Build beantwortet und ergänzen die Prüffragen aus [[20-Design/Anti AI Slop#Erkennungsfragen]] und [[10-Strategy/Information Density and Mobile Clarity#Prüffragen vor der Abnahme]].

1. Beantwortet der erste Bildschirm auf 375 Pixel, was das ist, für wen, und was der nächste Schritt ist?
2. Welche der sechs Auftaktrollen ist besetzt, und womit genau ist der Beweisanker besetzt?
3. Welche Komposition aus dem Auftakt-Repertoire wurde gewählt, und warum diese?
4. Sieht die erste Bildschirmhöhe abgeschlossen aus, oder ist erkennbar, dass es weitergeht?
5. Welche reale Nutzerfrage beginnt in der zweiten Bildschirmhöhe?
6. Wie viele Überschriftenanordnungen kommen auf der Seite vor, und folgt jede der Aufgabe ihres Abschnitts?
7. Wie viel der ersten mobilen Bildschirmhöhe verbraucht die Kopfzeile?
8. Ist dies eine Seite mit einem Ziel oder mit mehreren, und passt das Kopfzeileninventar dazu?
9. Welcher Beweis steht in den ersten zwei Bildschirmhöhen, und ist er die stärkste real verfügbare Form?
10. Heißt die primäre Handlung überall gleich, und gibt es pro Bildschirmausschnitt genau eine?
11. Welches Signaturdetail trägt die Seite, woher stammt es, und wo kehrt es wieder?
12. Würde diese Startseite mit ausgetauschtem Logo für einen beliebigen anderen Betrieb derselben Branche funktionieren?
13. Wie lange dauert es, bis das Auftaktmedium sichtbar ist?
14. Welche Entscheidung dieser Seite steht nicht im Design Contract?

[^google50]: [Google Research: Users love simple and familiar designs](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/) sowie die zugrunde liegende Studie zu visueller Komplexität und Prototypikalität, [research.google/pubs](https://research.google.com/pubs/archive/38315.pdf). Geprüft am 3. September 2026.
[^fivesecond]: [Lyssna: Five second testing guide](https://www.lyssna.com/guides/five-second-testing-guide/). Geprüft am 3. September 2026.
[^nngscroll]: [Nielsen Norman Group: Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/). Geprüft am 3. September 2026.
[^completeness]: [Scrolling and the illusion of completeness](https://digitalcommunications.wp.st-andrews.ac.uk/2020/09/21/scrolling-and-the-illusion-of-completeness/). Geprüft am 3. September 2026.
[^attentionratio]: [Unbounce: Attention Ratio](https://unbounce.com/conversion-glossary/definition/attention-ratio/). Die Kennzahl stammt aus der Conversion-Centered-Design-Systematik und gilt für Kampagnenseiten, nicht für Unternehmensstartseiten. Geprüft am 3. September 2026.
[^lcp]: [Core Web Vitals: Fix slow hero images](https://www.corewebvitals.io/pagespeed/fix-slow-hero-images-core-web-vitals). Grenzwerte gegen [[30-Frontend/Performance]] halten. Geprüft am 3. September 2026.
[^slopcause]: [925 Studios: AI Slop Web Design Guide](https://www.925studios.co/blog/ai-slop-web-design-guide) und [Monet: Escape AI Slop](https://www.monet.design/blog/posts/escape-ai-slop-landing-page-design). Beide beschreiben dieselbe Ursache: ohne festgelegte Entscheidung entsteht die wahrscheinlichste Lösung. Geprüft am 3. September 2026.
