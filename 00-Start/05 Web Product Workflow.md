---
type: canonical
status: canonical
updated: 2026-08-19
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
4. [[80-Templates/Project Master Spec]] als `PROJECT.md`, [[80-Templates/Source and Rights Review]] als `SOURCE-RIGHTS-REVIEW.md`, [[80-Templates/Asset Register]] als `ASSET-REGISTER.md` und [[80-Templates/Data Processing Inventory]] als `DATA-PROCESSING-INVENTORY.md` kopieren; zusätzlich für jede beauftragte Website [[80-Templates/Release Readiness Register]] als `release-readiness/<website-slug>.md` anlegen;
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

### Folgen für Ablage und Zugriff

- **Eine Website:** Ablage unter `site/`.
- **Mehrere Websites:** Ablage unter `versions/01-<richtung>/`, `versions/02-<richtung>/` und so fort.
- **Build auf `217.154.218.30`:** kein fester lokaler Projektport und kein neues `start-local.sh`; Zugriff über die Developer-Plattform auf `johannstein.com`.
- **Build auf anderen Rechnern:** je Website ein eigener fester Port und die lokalen Startskripte.

Details in [[60-Operations/Delivery and Local Start]].

### Was unabhängig von der Anzahl gilt

Jede gebaute Website ist ein fertiges Ergebnis, kein Entwurf und keine Auswahlvariante. Fakten, Funktionen, Datenflüsse, Unterseiten, Accessibility, Sicherheit und SEO sind in allen gebauten Websites identisch. Werden mehrere Websites verlangt, besitzt jede eine eigenständige kohärente Richtung und unterscheidet sich auf mindestens fünf für den Auftrag wirksamen Achsen, niemals im Umfang. Der Abstand ist in [[20-Design/Design Direction#Stilabstand bei mehreren Websites]] geregelt und wird vor dem ersten UI-Code in `PROJECT.md` festgehalten.

## Verbindliche Reihenfolge

1. **Kontext laden:** [[00-Start/00 Brain Index]], neu angelegtes Projekt-`PROJECT.md` und nur die über [[00-Start/02 Routing Map]] bestimmten Notizen lesen.
2. **Intake schließen:** Muss-Entscheidungen mit [[80-Templates/Project Intake]] erheben. Fehlende Geschäfts-, Daten-, Zahlungs- oder Identitätsentscheidung als offene Annahme in `PROJECT.md` markieren. Für jeden Inhaltsblock bei Erstellung und bei jedem Update `owner_editable`, stabilen JSON-Pointer, Feldtyp, Grenzen, Preview-Routen und Veröffentlichungspolicy nach [[60-Operations/Owner Hosting and Dashboard]] entscheiden. Ist zentrales Owner-Hosting Teil des Scopes, `content/<website>.json` und `owner-hosting/tenant.json` nach [[80-Templates/Owner Hosting Website Contract]] anlegen. Die Release-Readiness-Datei jeder Website fortlaufend pflegen; jede provisorische Sperre, Attrappe, unfertige sichtbare Aussage und noch nicht produktive Integration entsteht zusammen mit ihrem Eintrag. Gewünschte Bilder, Designs, Animationen und Quellen direkt für die Umsetzung einplanen; Quelle und tatsächlichen Einsatz anschließend im `SOURCE-RIGHTS-REVIEW.md` erfassen.
3. **Bestand sichern:** Bei vollständigem Neubau einer vorhandenen Website den [[10-Strategy/Existing Website Rebuild]] ausführen, bevor Inhalte oder Assets neu geschrieben werden.
4. **Inspiration untersuchen:** Für jedes Web-Produkt den [[90-References/Reference Research Workflow]] ausführen. Struktur, visuelle Sprache und Interaktion getrennt bewerten. Referenzen, Bilder, Designs und Animationen dürfen kreativ direkt übernommen oder adaptiert werden. Das Ergebnis dokumentiert den konkreten Einsatz, ohne daraus eine Build- oder Asset-Sperre abzuleiten.
5. **Design Contract je Website erzeugen:** Für jede gebaute Website [[20-Design/Design Direction]] getrennt festlegen und einen Leitbenchmark aus [[20-Design/Interface Benchmarks]] wählen. H0 gilt immer, Stilprofil, Radius, Rahmen, Flächen, Karten, Kopf-/Fußbereich, Chrome, Zweitschrift und Motion werden je Website entschieden. Existieren ältere Fassungen desselben Betriebs, wird das Übernahmeregister aus [[20-Design/Design Direction#Abstand zu Vorgängerfassungen]] vorher ausgefüllt. **UI UX Pro Max wird je Website getrennt ausgeführt und unter `design-system/<website-slug>/MASTER.md` persistiert**, siehe [[00-Start/04 Plugins and Skills#Auslösebedingung]].
6. **Websites spezifizieren:** Die im Auftrag verlangte Anzahl vollständiger Websites anlegen. Jede erhält Art Direction, vollständige verlinkte Unterseiten, ein begründetes Motion-Budget, Visual-/SEO-Nachweise und ein eigenes Release-Readiness-Register. Port und Startanweisung folgen dem tatsächlichen Build-Rechner: auf `217.154.218.30` Developer-Plattform statt Projektport, sonst fester lokaler Port. Fakten, Funktionen, Datenflüsse, Accessibility und Sicherheit bleiben identisch.
7. **Master Spec freigeben:** [[80-Templates/Project Master Spec]] samt Sitemap, Website-Matrix, Designsystem, Zuständen, Budgets, Risiken und Akzeptanzkriterien auf `approved` setzen. Vorher kein produktiver UI-Code.
8. **Vertikal implementieren:** Einen realen kritischen Nutzerfluss einschließlich Serverregeln, Fehlern, Accessibility, responsivem Verhalten und Tests vollständig bauen. Danach weitere Flows im selben Architektur- und Designsystem ergänzen.
9. **Kritikschleife mit Impeccable:** Jede gebaute Website gegen Master Spec, Referenzentscheidungen und [[70-QA/Quality Gates]] prüfen. Zusätzlich verbindlich der KI-Detail-Review nach [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review|Anti AI Slop]]: Impeccable wird auf jede gebaute Website angewendet, um Details zu finden, die nach KI-Generat aussehen. Befunde werden korrigiert oder begründet im Decision Log dokumentiert. Keine Website wird als Auswahl-, Ersatz-, Preview- oder Produktionskandidatin abgewertet.
10. **Liefern und erhalten:** Alle gebauten Websites samt Unterseiten, SEO, gewählter Motion und dem für die Umgebung passenden Zugriff vollständig liefern. Vor der Veröffentlichungsentscheidung jedes Release-Readiness-Register gegen Repository, ausgelieferten Produktionskandidaten und externe Infrastruktur abgleichen. Bei Owner-Hosting zuerst Contract-Lint und Tenant-Plan durchführen; eine Website wird nie nur durch Ordnererkennung registriert. Projekt-Basis, Owner-Overlay, Vertragsversion und Release-ID bleiben getrennt nachvollziehbar. `SOURCE-RIGHTS-REVIEW.md` hält danach nur die Einschätzung für den Nutzer/Owner fest. Was veröffentlicht wird, entscheidet ausschließlich dieser Nutzer/Owner; die KI sperrt, ersetzt oder entfernt keine Assets und erklärt keine Website zu einer bloßen Preview. Danach Deployment, Monitoring, Rollback und Wartungsowner abschließen. Relevante Erkenntnisse atomar in das Brain zurückführen.

## Kontext- und Gedächtnisebenen

| Ebene | Kanonischer Speicher | Zulässiger Inhalt |
|---|---|---|
| global | dieses Vault | projektübergreifende Regeln, Methoden, Quellen und Templates |
| Projekt | `../projekte/<Projektname>/PROJECT.md` plus verlinkte Artefakte | verbindliche Produktentscheidung, Sitemap, Designsystem, Risiken und Nachweise |
| Aufgabe | aktueller Plan, Issue oder Sessionnotiz | temporäre Schritte, Befunde und noch unbestätigte Hypothesen |

Eine untere Ebene darf eine höhere konkretisieren, aber nicht still überschreiben. Dauerhafte Erkenntnisse werden nicht in Chats versteckt, sondern über [[00-Start/03 Update Protocol]] dem kanonischen Besitzer zugeführt.

## Mehrere Websites und Parallelität

Verlangt der Auftrag mehr als eine Website, sind alle gebauten Websites getrennt, vollständig, fertig, startbar und gleichwertig auslieferbar. Sie teilen Fakten, Funktionen, Accessibility, Sicherheit, Unterseiten und SEO, besitzen aber je eine eigenständige kohärente Richtung mit mindestens fünf wirksam verschiedenen Achsen. Es gibt keine Wahl-/Verwerfungsentscheidung und keine künstliche Aufteilung in Preview und Produktion. Gleichzeitige Schreibzugriffe auf dieselbe Datei sind untersagt.

Gemeinsame Fakten liegen kanonisch außerhalb der Websites, etwa unter `content/`, und werden nie in eine Website hineinkopiert. So bleibt eine Faktenänderung eine einzige Änderung, unabhängig davon, wie viele Websites gebaut wurden.

## Herkunft und Anpassung

Der Ablauf übernimmt aus der im [[90-References/Inspiration Catalog|Inspirationskatalog]] erfassten Curriculum-Referenz insbesondere Research-vor-Spec, Spec-vor-Build, explizite Verifikation, Toolprüfung und getrennte Gedächtnisebenen. Das Vault ersetzt externe Wissensspeicher als kanonische Langzeitbasis. Produkt-, Rechts-, Sicherheits- und Qualitätsentscheidungen bleiben bei den verlinkten Fachnotizen.
