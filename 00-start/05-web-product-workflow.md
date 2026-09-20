---
type: canonical
status: canonical
updated: 2026-09-20
depends_on:
  - "[[10-strategy/discovery-and-scope.md]]"
  - "[[90-references/reference-research-workflow.md]]"
  - "[[70-qa/quality-gates.md]]"
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
4. [[80-templates/project-master-spec.md]] als `PROJECT.md`, [[80-templates/source-and-rights-review.md]] als `SOURCE-RIGHTS-REVIEW.md`, [[80-templates/asset-register.md]] als `ASSET-REGISTER.md` und [[80-templates/data-processing-inventory.md]] als `DATA-PROCESSING-INVENTORY.md` kopieren; zusätzlich für jede beauftragte Website [[80-templates/release-readiness-register.md]] als `release-readiness/<website-slug>.md` anlegen;
5. die Pflichtstruktur aus [[60-operations/delivery-and-local-start.md]] anlegen und alle projektspezifischen Artefakte ausschließlich dort speichern.

Kann die Projektwurzel nicht angelegt oder beschrieben werden, Blocker melden. Nicht ersatzweise im Brain, in einem temporären Ordner oder in einem anderen Projekt bauen. Das Brain wird nicht in den Projektordner kopiert; `PROJECT.md` verweist auf die zutreffenden kanonischen Regeln und dokumentiert deren Anwendung.

## Erst bauen, dann fragen

**Vor der ersten gerenderten Website wird nichts gefragt.** Nicht die Bahnwahl, nicht die Art Direction, nicht die fehlende Telefonnummer. Der Agent trifft die Entscheidung, die er für die beste hält, baut weiter und merkt sie an.

Der Grund ist der Unterschied zwischen zwei Gesprächen. Das eine beginnt mit sieben Fragen über eine Website, die es noch nicht gibt; jede Antwort ist geraten, weil niemand die Seite gesehen hat. Das andere beginnt mit einer fertigen Website und einer Liste von zwölf Entscheidungen, die daran sichtbar sind. Das zweite ist kürzer und führt zu besseren Antworten.

### Genau eine Ausnahme

Der Agent hält an, **bevor er etwas Vorhandenes überschreibt oder löscht** — einen bestehenden Projektordner, eine bestehende Datei, einen bestehenden Build. Das ist nicht umkehrbar, alles andere ist es.

Sonst nichts. Kein Halt für fehlende Angaben, widersprüchliche Quellen, Geschmacksfragen, Bahnwechsel oder eine Aufgabe, die größer ist als gedacht.

### Was an die Stelle der Frage tritt

| Lage | Statt zu fragen |
|---|---|
| Pflichtangabe fehlt | plausiblen Platzhalter setzen, eintragen |
| Angabe steht auf der alten Seite | übernehmen nach [[10-strategy/existing-website-rebuild.md#Übernahme ohne Rückfrage]] |
| zwei Quellen widersprechen sich | plausiblere nehmen, Widerspruch notieren |
| Geschmacksfrage | entscheiden, im Design Contract begründen |
| der Auftrag ist mehrdeutig | die nächstliegende Lesart bauen, Auslegung notieren |
| Auth, Zahlung oder Datenhaltung tauchen auf | die statische Website fertig bauen, den Zusatzbedarf als Full-Lane-Vorschlag anmerken |
| eine Anforderung ist größer als der Auftrag | den kleineren, lauffähigen Stand bauen und den Rest anmerken |

### Platzhalter sind erlaubt

Ein fehlendes Bild, ein fehlender Text, eine fehlende Beschreibung halten den Build nicht auf. Der Agent setzt etwas Plausibles ein, macht es im Projekt kenntlich und trägt es als offenen Punkt ein. Platzhalter blockieren die **Veröffentlichung** nach [[70-qa/quality-gates.md#G0 Scope]], nicht die Arbeit.

Die eine Grenze: **belegbare Behauptungen werden nicht erfunden.** Kundenstimmen, Zertifikate, Auszeichnungen, Mitgliedschaften, Nutzerzahlen und Leistungswerte stehen auf der Website eines realen Betriebs für dessen Ruf gerade und treffen dessen Kunden. Fehlt der Beleg, entfällt die Aussage oder der Abschnitt. Beschreibender Text, Beispielinhalte und Bildplatzhalter fallen **nicht** darunter.

### Die Vorlage am Ende

Wenn die Website steht, gerendert und durch `qa.sh` gelaufen ist, kommt **eine** Nachricht. Kein Tröpfeln über den Tag:

1. **Der Link.** `johannstein.com/dev/<projekt>/` — bevor irgendetwas anderes gesagt wird.
2. **Was entschieden wurde**, mit Begründung in je einer Zeile: Bahn, Art Direction, Auftaktkomposition, Sektionsfolge.
3. **Was angenommen wurde.** Jede Annahme mit Quelle und Folge: *„Öffnungszeiten von der alten Seite, Stand dort 2023. Falls überholt, eine Zeile in `content/beispiel.json`."*
4. **Was offen ist.** Platzhalter, ungeprüfte Fakten, fehlende Bilder, Rechtstexte zur Freigabe — identisch mit `release-readiness/<website-slug>.md`.
5. **Was der Nutzer entscheiden muss**, sofern etwas übrig bleibt. Meist bleibt wenig übrig, weil Punkt 3 und 4 das meiste schon beantworten.

Diese Liste ist das Ergebnis der Arbeit, nicht ihr Anfang.

## Bahnwahl: Fast Lane und Full Lane

Es gibt zwei Bahnen durch diesen Workflow. Die **Fast Lane ist der Standard**; die Full Lane wird nur gefahren, wenn eine ihrer Auslösebedingungen zutrifft. Die Bahnwahl wird mit Begründung in `PROJECT.md` festgehalten, als `Bahn: fast | full, Grund: …`, bevor der erste Ordner angelegt wird.

| | **Fast Lane — Standard** | Full Lane |
|---|---|---|
| Auslöser | Standardwebsite eines lokalen Betriebs aus [[30-frontend/web-kit.md]], kein Login, keine Zahlung, keine eigene Datenhaltung, eine Fassung | Auth, Zahlung, eigene Datenhaltung, Sonderfunktion oder mehr als eine Fassung |
| Pflichtdateien | `PROJECT.md` und `release-readiness/<website-slug>.md` | zusätzlich `SOURCE-RIGHTS-REVIEW.md`, `ASSET-REGISTER.md`, `DATA-PROCESSING-INVENTORY.md` |
| Design | zwei Auftaktfassungen, ein Renderdurchgang | volle Strecke: `D0`-Stilkachel plus drei Durchgänge |
| Skills | optional | verbindlich |
| Gates | `G0` verkürzt, `G1`, `scripts/qa.sh` | alle Gates `G0` bis `G8` |
| Zielzeit | ein Arbeitstag | offen |

Die Qualitätsregeln gelten in beiden Bahnen unverändert. Verkürzt wird die Nachweisführung, nicht das Handwerk: Tokenvertrag, Zustände, Kontrast, Tastaturbedienung, Rechtsseiten, Performance und SEO sind in der Fast Lane genauso verbindlich, sie werden nur nicht in vier getrennten Inventaren nachgewiesen. Trifft während des Builds eine Full-Lane-Bedingung ein, wird auf die Full Lane gewechselt und der Wechsel in `PROJECT.md` vermerkt; die fehlenden Inventare werden nachgezogen.

### Fast Lane

1. Projektordner nach [[#Auftragsschwelle und Projektanlage]] anlegen, aber nur `PROJECT.md` und `release-readiness/<website-slug>.md`.
2. Bestehende Website nach [[10-strategy/existing-website-rebuild.md]] sichern; `scripts/extract-old-site.ts` aus dem Kit übernimmt Texte, Bilder, Kontakt- und Öffnungszeitendaten. Die Angaben werden nach [[10-strategy/existing-website-rebuild.md#Übernahme ohne Rückfrage]] übernommen und eingebaut, nicht erst bestätigt.
3. Betriebsdaten und Marktumfeld recherchieren, Kurzbrief in `PROJECT.md` schreiben: Angebot, Zielgruppe, primäre Handlung, Beweisformen, Sitemap.
4. Blöcke aus [[30-frontend/web-kit.md]] ziehen, statt sie neu zu schreiben. Das Kit ist der Pflichtausgangspunkt der Fast Lane.
   **Owner-Hosting wird dabei immer mitgebaut**, siehe [[#Owner-Hosting ist Standard]]: eine Inhaltsdatei, stabile Pointer, Feldtypen, Preview-Route. Es nachträglich einzuziehen kostet ein Vielfaches.
5. Tokenwerte dieses Betriebs setzen; die Rollennamen des Tokenvertrags aus [[20-design/color-system.md#Tokenvertrag]] bleiben unverändert. Ableitung und Artefaktweg in [[20-design/design-systems-und-artefakte.md]].
6. Zwei Auftaktfassungen mit verschiedenen Kompositionen aus [[20-design/landing-page-craft.md#Auftakt-Repertoire]] bauen, bei 375 und 1280 Pixel nebeneinander ansehen, eine mit Begründung wählen.
7. Ein Renderdurchgang am ganzseitigen Render mit schriftlicher Befundliste nach [[20-design/visual-iteration-loop.md]]. Ein Render ohne Befundliste ist kein Durchgang.
8. `scripts/qa.sh` aus dem Kit laufen lassen: Lighthouse, axe, interner Link-Check, Screenshots bei 375 und 1280, Prüfung auf Platzhalter- und `TODO`-Reste.
9. **Auf `johannstein.com/dev` verfügbar machen** — siehe [[#Jede Website liegt sofort auf /dev]]. Das geschieht, sobald der erste Build steht, nicht am Ende.
10. `G0` verkürzt und `G1` nach [[70-qa/quality-gates.md]] abnehmen, Release-Readiness-Register schließen.
11. **Eine** Nachricht nach [[#Die Vorlage am Ende]]: Link zuerst, dann Entscheidungen, Annahmen und Offenes.

Die Fast Lane läuft über den Skill `web-build`, der diese Strecke ausführt und auf die kanonischen Notizen verweist.

### Owner-Hosting ist Standard

**Jede gebaute Website erfüllt die Schnittstelle aus [[60-operations/owner-hosting-interface.md]]**, ohne dass es im Auftrag stehen muss. Vier Pflichten:

1. aller owner-bearbeitbare Inhalt in genau einer Datei `content/<website>.json`;
2. stabile JSON-Pointer, die nicht umbenannt, sondern migriert werden;
3. je Feld `owner_editable`, Feldtyp, Grenzen, Label und Veröffentlichungspolicy;
4. je Block eine benannte Preview-Route.

Dazu der Content-Loader: liest `OWNER_HOSTING_CONTENT_FILE`, sonst die Projektdatei. Der Starter aus [[30-frontend/web-kit.md]] bringt ihn mit, es ist also kein Zusatzaufwand, sondern ein unterlassener Rückbau.

Der Grund für „immer": Die Anbindung nachträglich einzuziehen heißt, jeden Text aus jeder Komponente herauszuoperieren und Pointer zu vergeben, während der Owner schon Werte eingetragen hat. Von Anfang an kostet sie nichts, weil das Kit ohnehin so gebaut ist.

Ob das Dashboard die Website am Ende wirklich aufnimmt, entscheidet der Nutzer. Die Website ist dafür bereit, in jedem Fall.

### Jede Website liegt sofort auf /dev

Auf dem Server `217.154.218.30` ist **jede gebaute Website unter `johannstein.com/dev` erreichbar**, sobald der erste Build steht — nicht erst zur Abnahme.

Die Developer-Plattform erkennt Builds selbst: Sie findet `site/` und `versions/<fassung>/` unterhalb von `../projekte/<Projektname>/` mit den Ausgabeordnern `dist/`, `build/` oder `public/`. Ein Build an der richtigen Stelle erscheint damit von allein.

- Erscheint er nicht, ist das ein **Delivery-Fehler** und wird dort behoben, nicht mit einem eigenen Port oder Prozess umgangen. Kanonisch in [[60-operations/delivery-and-local-start.md#Auf `217.154.218.30`]].
- Der Link gehört in `PROJECT.md` und ist die erste Zeile der Abschlussnachricht.
- Der Zugriff ist durch das Gate nach [[40-backend-security/preview-access-gate.md]] geschützt und trägt `noindex`. Eine Fassung unter `/dev` ist eine Vorschau, keine Veröffentlichung.
- Kein fester lokaler Projektport, kein `start-local.sh`. Auf anderen Rechnern gilt weiter die Portregel.

Der Nutzer soll die Seite ansehen können, während noch daran gearbeitet wird. Ein Build, den nur der Agent sieht, hilft niemandem.

### Full Lane

Die Full Lane fährt die vollständige [[#Verbindliche Reihenfolge]] mit allen Pflichtinventaren, allen Gates und dem vollständigen Visual Iteration Loop.

## Anzahl der Websites

Kanonische Regel. Die Anzahl der zu bauenden Websites steht immer im Auftrag des Nutzers und wird nie vom Brain vorgegeben.

| Angabe im Auftrag | Ergebnis |
|---|---|
| keine Angabe zur Anzahl | **genau eine** vollständige Website |
| eine Zahl oder ein Zahlwort, etwa „zwei Websites“, „drei Versionen“, „4 Varianten“ | **genau diese Anzahl** vollständiger Websites |

- Die Zahl wird vor der Projektanlage bestimmt und in `PROJECT.md` als `Anzahl Websites: N, Quelle: Auftragstext „…“` festgehalten.
- Ist die Angabe mehrdeutig, wird **eine** Website gebaut und die Auslegung als Annahme in `PROJECT.md` vermerkt. Der Auftrag wird dadurch nicht blockiert.
- Nachträgliche Änderung der Anzahl ist eine Auftragsänderung und läuft über [[00-start/03-update-protocol.md]].

### Folgen für Ablage und Zugriff

- **Eine Website:** Ablage unter `site/`.
- **Mehrere Websites:** Ablage unter `versions/01-<richtung>/`, `versions/02-<richtung>/` und so fort.
- **Build auf `217.154.218.30`:** kein fester lokaler Projektport und kein neues `start-local.sh`; Zugriff über die Developer-Plattform auf `johannstein.com`.
- **Build auf anderen Rechnern:** je Website ein eigener fester Port und die lokalen Startskripte.

Details in [[60-operations/delivery-and-local-start.md]].

### Was unabhängig von der Anzahl gilt

Jede gebaute Website ist ein fertiges Ergebnis, kein Entwurf und keine Auswahlvariante. Fakten, Funktionen, Datenflüsse, Unterseiten, Accessibility, Sicherheit und SEO sind in allen gebauten Websites identisch. Werden mehrere Websites verlangt, besitzt jede eine eigenständige kohärente Richtung und unterscheidet sich auf mindestens fünf für den Auftrag wirksamen Achsen, niemals im Umfang. Der Abstand ist in [[20-design/design-direction.md#Stilabstand bei mehreren Websites]] geregelt und wird vor dem ersten UI-Code in `PROJECT.md` festgehalten.

## Verbindliche Reihenfolge

Dies ist die Strecke der Full Lane. Die Fast Lane fährt die verkürzte Fassung aus [[#Fast Lane]]; die Qualitätsregeln der einzelnen Schritte gelten dort unverändert.

1. **Kontext laden:** [[00-start/00-brain-index.md]], neu angelegtes Projekt-`PROJECT.md` und nur die über [[00-start/02-routing-map.md]] bestimmten Notizen lesen.
2. **Intake schließen:** Muss-Entscheidungen mit [[80-templates/project-intake.md]] erheben. Fehlende Geschäfts-, Daten-, Zahlungs- oder Identitätsentscheidung als offene Annahme in `PROJECT.md` markieren. Für jeden Inhaltsblock bei Erstellung und bei jedem Update `owner_editable`, stabilen JSON-Pointer, Feldtyp, Grenzen, Preview-Routen und Veröffentlichungspolicy nach [[60-operations/owner-hosting-interface.md]] entscheiden. Ist zentrales Owner-Hosting Teil des Scopes, `content/<website>.json` und `owner-hosting/tenant.json` nach [[80-templates/owner-hosting-website-contract.md]] anlegen. Die Release-Readiness-Datei jeder Website fortlaufend pflegen; jede provisorische Sperre, Attrappe, unfertige sichtbare Aussage und noch nicht produktive Integration entsteht zusammen mit ihrem Eintrag. Gewünschte Bilder, Designs, Animationen und Quellen direkt für die Umsetzung einplanen; Quelle und tatsächlichen Einsatz anschließend im `SOURCE-RIGHTS-REVIEW.md` erfassen.
3. **Bestand sichern:** Bei vollständigem Neubau einer vorhandenen Website den [[10-strategy/existing-website-rebuild.md]] ausführen, bevor Inhalte oder Assets neu geschrieben werden.
4. **Referenzmodus nach Auftragszahl festlegen:** Den [[90-references/reference-research-workflow.md]] anwenden. Bei genau einer Website ohne ausdrücklich vom Nutzer vorgegebene Referenz keine Live-Leitreferenz auswählen; die Website entsteht als `Eigenentwurf`. Bei zwei oder mehr Websites wird der [[90-references/website-reference-pool.md]] einmal für die Fassung geprüft, die gegebenenfalls referenzgeführt sein soll. Genau eine fachlich stark passende Originalseite darf genau diese eine Fassung prägen. Alle übrigen Fassungen bleiben Eigenentwürfe und übernehmen die Referenz nicht verdeckt als zweite Vorlage. Gibt es keine starke Passung, bleiben alle Fassungen Eigenentwürfe. Galerie-, Award-, Stilbibliotheks- und Sammlungsseiten sind keine Leitreferenzen.
5. **Design Contract je Website erzeugen:** Für jede gebaute Website [[20-design/design-direction.md]] getrennt festlegen, ihren Referenzmodus dokumentieren und einen Leitbenchmark aus [[20-design/interface-benchmarks.md]] wählen. Bei mehreren Websites liefert genau eine fachlich passende Leitreferenz Inspiration und Grundstruktur für genau eine Fassung; nur eine dokumentiert erfolglose Suche hebt diese Quote auf. Brain, Projektwahrheit, Marke, Inhalte, Accessibility und Technik bleiben verbindlich. Eigenentwürfe entstehen aus derselben Projektwahrheit und dürfen dieselbe sachlich beste Grobstruktur verwenden, ohne sich künstlich über schlechtere Auftakte oder Sektionsfolgen abzusetzen. H0 gilt immer, Stilprofil, Radius, Rahmen, Flächen, Karten, Kopf-/Fußbereich, Chrome, Zweitschrift und Motion werden je Website entschieden. Existieren ältere Fassungen desselben Betriebs, wird das Übernahmeregister aus [[20-design/design-direction.md#Abstand zu Vorgängerfassungen]] vorher ausgefüllt. **UI UX Pro Max wird je Website getrennt ausgeführt und unter `design-system/<website-slug>/MASTER.md` persistiert**, siehe [[00-start/04-plugins-and-skills.md#Auslösebedingung]].
6. **Websites spezifizieren:** Die im Auftrag verlangte Anzahl vollständiger Websites anlegen. Jede erhält Art Direction, vollständige verlinkte Unterseiten, ein begründetes Motion-Budget, Visual-/SEO-Nachweise und ein eigenes Release-Readiness-Register. Port und Startanweisung folgen dem tatsächlichen Build-Rechner: auf `217.154.218.30` Developer-Plattform statt Projektport, sonst fester lokaler Port. Fakten, Funktionen, Datenflüsse, Accessibility und Sicherheit bleiben identisch.
7. **Master Spec freigeben:** [[80-templates/project-master-spec.md]] samt Sitemap, Website-Matrix, Designsystem, Zuständen, Budgets, Risiken und Akzeptanzkriterien auf `approved` setzen. Vorher kein produktiver UI-Code.
8. **Vertikal implementieren:** Einen realen kritischen Nutzerfluss einschließlich Serverregeln, Fehlern, Accessibility, responsivem Verhalten und Tests vollständig bauen. Danach weitere Flows im selben Architektur- und Designsystem ergänzen.
9. **Visual Iteration Loop je Website:** Zuerst die Stilkachel `D0` rendern und ansehen: Tokenvertrag, Type Ramp, Radius-/Rahmen-/Tiefengrammatik, Aktionszustände, Inhaltsgrundform und Signaturdetail auf einer Seite, in Licht und Dunkel, an echtem Text. Befunde dort beheben, bevor ein Auftakt entsteht. Danach zwei bis drei Auftaktfassungen mit verschiedenen Kompositionen aus [[20-design/landing-page-craft.md#Auftakt-Repertoire]] und denselben realen Inhalten bauen, nebeneinander bei 375 und 1280 Pixel ansehen, eine wählen und die Wahl begründen. Danach mindestens drei Durchgänge `D1 Komposition`, `D2 Rhythmus und Hierarchie`, `D3 Zustand und Detail` am ganzseitigen Render des laufenden Builds. Jeder Durchgang erzeugt eine schriftliche Befundliste mit Ort, Beobachtung und Änderung; ein Render ohne Befundliste ist kein Durchgang. Kanonisch in [[20-design/visual-iteration-loop.md]]. Ist in der Umgebung kein echter Render erzeugbar, ist das ein Blocker und kein Grund, den Loop zu überspringen.
10. **Kritikschleife mit Impeccable:** Jede gebaute Website gegen Master Spec, Referenzentscheidungen und [[70-qa/quality-gates.md]] prüfen. Zusätzlich verbindlich der KI-Detail-Review nach [[20-design/anti-ai-slop.md#Impeccable KI-Detail-Review|Anti AI Slop]]: Impeccable wird auf jede gebaute Website angewendet, um Details zu finden, die nach KI-Generat aussehen. Befunde werden korrigiert oder begründet im Decision Log dokumentiert. Keine Website wird als Auswahl-, Ersatz-, Preview- oder Produktionskandidatin abgewertet.
11. **Liefern und erhalten:** Alle gebauten Websites samt Unterseiten, SEO, gewählter Motion und dem für die Umgebung passenden Zugriff vollständig liefern. Vor der Veröffentlichungsentscheidung jedes Release-Readiness-Register gegen Repository, ausgelieferten Produktionskandidaten und externe Infrastruktur abgleichen. Bei Owner-Hosting zuerst Contract-Lint und Tenant-Plan durchführen; eine Website wird nie nur durch Ordnererkennung registriert. Projekt-Basis, Owner-Overlay, Vertragsversion und Release-ID bleiben getrennt nachvollziehbar. `SOURCE-RIGHTS-REVIEW.md` hält danach nur die Einschätzung für den Nutzer/Owner fest. Was veröffentlicht wird, entscheidet ausschließlich dieser Nutzer/Owner; die KI sperrt, ersetzt oder entfernt keine Assets und erklärt keine Website zu einer bloßen Preview. Danach Deployment, Monitoring, Rollback und Wartungsowner abschließen. Relevante Erkenntnisse atomar in das Brain zurückführen.

## Kontext- und Gedächtnisebenen

| Ebene | Kanonischer Speicher | Zulässiger Inhalt |
|---|---|---|
| global | dieses Vault | projektübergreifende Regeln, Methoden, Quellen und Templates |
| Projekt | `../projekte/<Projektname>/PROJECT.md` plus verlinkte Artefakte | verbindliche Produktentscheidung, Sitemap, Designsystem, Risiken und Nachweise |
| Aufgabe | aktueller Plan, Issue oder Sessionnotiz | temporäre Schritte, Befunde und noch unbestätigte Hypothesen |

Eine untere Ebene darf eine höhere konkretisieren, aber nicht still überschreiben. Dauerhafte Erkenntnisse werden nicht in Chats versteckt, sondern über [[00-start/03-update-protocol.md]] dem kanonischen Besitzer zugeführt.

## Mehrere Websites und Parallelität

Verlangt der Auftrag mehr als eine Website, sind alle gebauten Websites getrennt, vollständig, fertig, startbar und gleichwertig auslieferbar. Sie teilen Fakten, Funktionen, Accessibility, Sicherheit, Unterseiten und SEO, besitzen aber je eine eigenständige kohärente Richtung mit mindestens fünf wirksam verschiedenen Achsen. Es gibt keine Wahl-/Verwerfungsentscheidung und keine künstliche Aufteilung in Preview und Produktion. Gleichzeitige Schreibzugriffe auf dieselbe Datei sind untersagt.

Gemeinsame Fakten liegen kanonisch außerhalb der Websites, etwa unter `content/`, und werden nie in eine Website hineinkopiert. So bleibt eine Faktenänderung eine einzige Änderung, unabhängig davon, wie viele Websites gebaut wurden.

## Herkunft und Anpassung

Der Ablauf übernimmt aus der im [[90-references/inspiration-catalog.md|Inspirationskatalog]] erfassten Curriculum-Referenz insbesondere Research-vor-Spec, Spec-vor-Build, explizite Verifikation, Toolprüfung und getrennte Gedächtnisebenen. Das Vault ersetzt externe Wissensspeicher als kanonische Langzeitbasis. Produkt-, Rechts-, Sicherheits- und Qualitätsentscheidungen bleiben bei den verlinkten Fachnotizen.
