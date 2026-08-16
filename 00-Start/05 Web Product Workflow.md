---
type: canonical
status: canonical
updated: 2026-08-16
depends_on:
  - "[[10-Strategy/Discovery and Scope]]"
  - "[[90-References/Reference Research Workflow]]"
  - "[[70-QA/Quality Gates]]"
impacts:
  - project-master-spec
  - design
  - implementation
  - qa
---

# Web Product Workflow

## Auftragsschwelle und Projektanlage

Sobald der Nutzer die Umsetzung, den Neubau oder den vollständigen Relaunch einer Website beauftragt, vor Recherche, Downloads, Design oder Code:

1. eindeutigen Projektnamen bestimmen;
2. `../projekte/<Projektname>/` neu anlegen oder einen vorhandenen gleichnamigen Ordner bewusst als bestehendes Projekt öffnen;
3. niemals einen vorhandenen Projektordner oder dessen Dateien still überschreiben;
4. [[80-Templates/Project Master Spec]] als `PROJECT.md`, [[80-Templates/Source and Rights Review]] als `SOURCE-RIGHTS-REVIEW.md`, [[80-Templates/Asset Register]] als `ASSET-REGISTER.md` und [[80-Templates/Data Processing Inventory]] als `DATA-PROCESSING-INVENTORY.md` kopieren;
5. die Pflichtstruktur aus [[60-Operations/Delivery and Local Start]] anlegen und alle projektspezifischen Artefakte ausschließlich dort speichern.

Kann die Projektwurzel nicht angelegt oder beschrieben werden, Blocker melden. Nicht ersatzweise im Brain, in einem temporären Ordner oder in einem anderen Projekt bauen. Das Brain wird nicht in den Projektordner kopiert; `PROJECT.md` verweist auf die zutreffenden kanonischen Regeln und dokumentiert deren Anwendung.

## Anzahl der Websites

Kanonische Regel. Die Anzahl der zu bauenden Websites steht immer im Auftrag des Nutzers und wird nie vom Brain vorgegeben.

| Angabe im Auftrag | Ergebnis |
|---|---|
| keine Angabe zur Anzahl | **genau eine** vollständige Website |
| eine Zahl oder ein Zahlwort, etwa „zwei Websites“, „drei Versionen“, „4 Varianten“ | **genau diese Anzahl** vollständiger Websites |

- Die Zahl wird vor der Projektanlage bestimmt und in `PROJECT.md` als `Anzahl Websites: N, Quelle: Auftragstext „…“` festgehalten.
- Ist die Angabe mehrdeutig, wird **eine** Website gebaut und die Auslegung als Annahme in `PROJECT.md` vermerkt. Der Auftrag wird dadurch nicht blockiert.
- Nachträgliche Änderung der Anzahl ist eine Auftragsänderung und läuft über [[00-Start/03 Update Protocol]].

### Folgen für Ablage und Ports

- **Eine Website:** Ablage unter `site/`, ein fester lokaler Port.
- **Mehrere Websites:** Ablage unter `versions/01-<richtung>/`, `versions/02-<richtung>/` und so fort, je Website ein eigener fester Port.

Details zu Struktur, Portvergabe und Startskripten in [[60-Operations/Delivery and Local Start]].

### Was unabhängig von der Anzahl gilt

Jede gebaute Website ist ein fertiges Ergebnis, kein Entwurf und keine Auswahlvariante. Fakten, Funktionen, Datenflüsse, Unterseiten, Accessibility, Sicherheit und SEO sind in allen gebauten Websites identisch. Werden mehrere Websites verlangt, unterscheiden sie sich sichtbar in Art Direction, Komposition und Motion, niemals im Umfang. Der geforderte Abstand ist als Unterscheidungsmatrix kanonisch in [[20-Design/Design Direction#Stilabstand bei mehreren Websites]] geregelt und wird vor dem ersten UI-Code in `PROJECT.md` festgehalten.

## Verbindliche Reihenfolge

1. **Kontext laden:** [[00-Start/00 Brain Index]], neu angelegtes Projekt-`PROJECT.md` und nur die über [[00-Start/02 Routing Map]] bestimmten Notizen lesen.
2. **Intake schließen:** Muss-Entscheidungen mit [[80-Templates/Project Intake]] erheben. Fehlende Geschäfts-, Daten-, Zahlungs- oder Identitätsentscheidung als offene Annahme in `PROJECT.md` markieren. Gewünschte Bilder, Designs, Animationen und Quellen direkt für die Umsetzung einplanen; Quelle und tatsächlichen Einsatz anschließend im `SOURCE-RIGHTS-REVIEW.md` erfassen. Dieser zweite Schritt hält die kreative oder technische Umsetzung nicht auf.
3. **Bestand sichern:** Bei vollständigem Neubau einer vorhandenen Website den [[10-Strategy/Existing Website Rebuild]] ausführen, bevor Inhalte oder Assets neu geschrieben werden.
4. **Inspiration untersuchen:** Für jedes Web-Produkt den [[90-References/Reference Research Workflow]] ausführen. Struktur, visuelle Sprache und Interaktion getrennt bewerten. Referenzen, Bilder, Designs und Animationen dürfen kreativ direkt übernommen oder adaptiert werden. Das Ergebnis dokumentiert den konkreten Einsatz, ohne daraus eine Build- oder Asset-Sperre abzuleiten.
5. **Design Contract erzeugen:** [[20-Design/Design Direction]] festlegen und den Leitbenchmark aus [[20-Design/Interface Benchmarks]] wählen. Bildplan nach [[20-Design/Imagery and AI Editing]] und Informationsbudget nach [[10-Strategy/Information Density and Mobile Clarity]] festlegen. **Der UI UX Pro Max Skill wird bei jedem Website-Build ausgeführt, ausnahmslos und je Website getrennt**, siehe [[00-Start/04 Plugins and Skills#Auslösebedingung]]; zusätzlich Impeccable verwenden; bei Motion zusätzlich Emil Design Engineering. Einsatz oder begründeter Verzicht auf [[90-References/pen.dev Workflow|pen.dev]] protokollieren.
6. **Websites spezifizieren:** Die im Auftrag verlangte Anzahl vollständiger Websites nach dem Abschnitt [[00-Start/05 Web Product Workflow#Anzahl der Websites|Anzahl der Websites]] anlegen. Jede erhält Art Direction, vollständige verlinkte Unterseiten, eine eigene Motion-Choreografie, einen eindeutigen lokalen Port, eine Startanweisung sowie Visual-/Motion-/SEO-Nachweise. Fakten, Funktionen, Datenflüsse, Accessibility und Sicherheit bleiben identisch; jede Website ist ein fertiges Ergebnis, keine Auswahlvariante.
7. **Master Spec freigeben:** [[80-Templates/Project Master Spec]] samt Sitemap, Website-Matrix, Designsystem, Zuständen, Budgets, Risiken und Akzeptanzkriterien auf `approved` setzen. Vorher kein produktiver UI-Code.
8. **Vertikal implementieren:** Einen realen kritischen Nutzerfluss einschließlich Serverregeln, Fehlern, Accessibility, responsivem Verhalten und Tests vollständig bauen. Danach weitere Flows im selben Architektur- und Designsystem ergänzen.
9. **Kritikschleife mit Impeccable:** Jede gebaute Website gegen Master Spec, Referenzentscheidungen und [[70-QA/Quality Gates]] prüfen. Zusätzlich verbindlich der KI-Detail-Review nach [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review|Anti AI Slop]]: Impeccable wird auf jede gebaute Website angewendet, um Details zu finden, die nach KI-Generat aussehen. Befunde werden korrigiert oder begründet im Decision Log dokumentiert. Keine Website wird als Auswahl-, Ersatz-, Preview- oder Produktionskandidatin abgewertet.
10. **Liefern und erhalten:** Alle gebauten Websites samt Unterseiten, SEO, Motion, Startanweisung und Ports vollständig liefern. `SOURCE-RIGHTS-REVIEW.md` hält danach nur die Einschätzung für den Nutzer/Owner fest. Was veröffentlicht wird, entscheidet ausschließlich dieser Nutzer/Owner; die KI sperrt, ersetzt oder entfernt keine Assets und erklärt keine Website zu einer bloßen Preview. Danach Deployment, Monitoring, Rollback und Wartungsowner abschließen. Relevante Erkenntnisse atomar in das Brain zurückführen.

## Kontext- und Gedächtnisebenen

| Ebene | Kanonischer Speicher | Zulässiger Inhalt |
|---|---|---|
| global | dieses Vault | projektübergreifende Regeln, Methoden, Quellen und Templates |
| Projekt | `../projekte/<Projektname>/PROJECT.md` plus verlinkte Artefakte | verbindliche Produktentscheidung, Sitemap, Designsystem, Risiken und Nachweise |
| Aufgabe | aktueller Plan, Issue oder Sessionnotiz | temporäre Schritte, Befunde und noch unbestätigte Hypothesen |

Eine untere Ebene darf eine höhere konkretisieren, aber nicht still überschreiben. Dauerhafte Erkenntnisse werden nicht in Chats versteckt, sondern über [[00-Start/03 Update Protocol]] dem kanonischen Besitzer zugeführt.

## Mehrere Websites und Parallelität

Verlangt der Auftrag mehr als eine Website, sind alle gebauten Websites getrennt, vollständig, fertig, startbar und gleichwertig auslieferbar. Sie teilen Fakten, Funktionen, Accessibility, Sicherheit, Unterseiten und SEO, unterscheiden sich aber sichtbar in Komposition und Motion. Es gibt keine Wahl-/Verwerfungsentscheidung und keine künstliche Aufteilung in Preview und Produktion. Gleichzeitige Schreibzugriffe auf dieselbe Datei sind untersagt.

Gemeinsame Fakten liegen kanonisch außerhalb der Websites, etwa unter `content/`, und werden nie in eine Website hineinkopiert. So bleibt eine Faktenänderung eine einzige Änderung, unabhängig davon, wie viele Websites gebaut wurden.

## Herkunft und Anpassung

Der Ablauf übernimmt aus der im [[90-References/Inspiration Catalog|Inspirationskatalog]] erfassten Curriculum-Referenz insbesondere Research-vor-Spec, Spec-vor-Build, explizite Verifikation, Toolprüfung und getrennte Gedächtnisebenen. Das Vault ersetzt externe Wissensspeicher als kanonische Langzeitbasis. Produkt-, Rechts-, Sicherheits- und Qualitätsentscheidungen bleiben bei den verlinkten Fachnotizen.
