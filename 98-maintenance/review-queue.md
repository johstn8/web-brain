---
type: maintenance
status: canonical
updated: 2026-09-11
next_review: 2026-11-01
---
# Review Queue

Diese Liste enthält bewusst zeitabhängige oder noch nicht vollständig verifizierbare Punkte. Ein leerer Eintrag ist kein Qualitätsziel; eine nachvollziehbare Warteschlange ist besser als versteckte Unsicherheit.

> [!important] Grundsatz seit 2026-08-16
> Eine Prüfung steht hier nur, wenn sie einen echten Auslöser hat. Entweder läuft sie automatisch, oder sie hängt an einem Arbeitsschritt, der ohnehin stattfindet. Ein Datum allein ist kein Auslöser, weil niemand am Stichtag nachsieht. Die frühere Tabelle mit Fälligkeitsdaten und durchgehendem Status `offen` war eine Absichtserklärung ohne Wirkung und wurde ersetzt.

## Automatisch geprüft

Diese Quellen ändern sich real und sind teuer, wenn das Brain sie falsch wiedergibt. Sie laufen deshalb über eine geplante Cloud-Routine, nicht über Handarbeit.

| Gegenstand | Betroffene Notizen | Umfang | Mechanismus | Status |
|---|---|---|---|---|
| Sicherheits- und Authentifizierungsquellen | [[40-backend-security/security-baseline.md]], [[40-backend-security/authentication-and-accounts.md]] | OWASP, NIST, eingesetzte Auth-Anbieter und Abuse-Schutz | Routine `Web-Brain Quartalsprüfung Sicherheit und Billing`, 1. Februar, Mai, August und November, 7 Uhr UTC | auf Eis gelegt am 2026-08-16; siehe Hinweis unter der Tabelle |
| Plattform- und Billing-Dokumentation | [[40-backend-security/data-apis-and-billing.md]] | APIs, Webhooks, Kündigungs- und Löschabläufe | dieselbe Routine | auf Eis gelegt am 2026-08-16; siehe Hinweis unter der Tabelle |

**Auf Eis, Stand 2026-08-16.** Die Routine ist inhaltlich fertig, aber nicht angelegt. Das Claude-Konto ist inzwischen mit GitHub verknüpft, die GitHub-App hat jedoch keinen Zugriff auf das private Repository `johstn8/web-brain`, weshalb die API die Anlage ablehnt. Der Nutzer hat das Thema am 2026-08-16 ausdrücklich zurückgestellt. **Damit findet für diese beiden Zeilen derzeit keine Prüfung statt.** Zum Aufwecken genügt es, das Repository unter https://github.com/settings/installations für die Claude-App freizugeben und die Routine mit den Angaben aus der Tabelle und dem folgenden Absatz anzulegen.

Die Routine liest die Fußnoten-URLs der drei Notizen, vergleicht sie mit der abgeleiteten Aussage und schreibt ihr Ergebnis direkt nach `main`. Ohne Befund aktualisiert sie nur Datum und Status dieser beiden Zeilen, damit sichtbar bleibt, dass sie gelaufen ist. Mit Befund legt sie einen Abschnitt `Befunde der Quartalsprüfung` in dieser Notiz an. Eindeutige Änderungen übernimmt sie selbst, alles Abwägungsbedürftige markiert sie als offene Entscheidung. Den Graphen baut sie nicht neu; das holt die nächste lokale Sitzung nach.

## Anlassgebunden geprüft

Diese Quellen werden geprüft, wenn sie gebraucht werden, nicht nach Kalender. Der Auslöser ist jeweils ein Schritt, der im Projekt ohnehin stattfindet. Ergebnis und Datum werden in der jeweiligen kanonischen Notiz vermerkt.

| Gegenstand | Auslöser | Umfang |
|---|---|---|
| Webstandards und Metriken | bevor ein Grenzwert aus diesen Quellen in einem Projekt gesetzt wird, spätestens bei den Gates `G3` und `G4` in [[70-qa/quality-gates.md]] | WCAG/WAI, Core Web Vitals, Browserunterstützung |
| deutsche und europäische Rechtsquellen | sobald ein Projekt Rechtstexte, Consent oder Datenerhebung erhält, über [[50-legal/legal-decision-tree.md]] | DDG, TDDDG, BFSG, DSGVO und Aufsichtsbehörden; die fachliche Rechtsprüfung je Projekt ersetzt das nicht |
| Tools und Bibliotheken | bevor eine Bibliothek neu in ein Projekt aufgenommen wird, nach [[60-operations/dependencies-and-environments.md]] | Lizenz, Wartungszustand, Integrationsweise |
| Google Maps/Places | sobald eine Website Karte, Ortsdaten oder ein Unternehmensprofil einbindet | EWR-Bedingungen, erlaubte Speicherung, Attribution, Maps URLs, Embed/API und Datenschutz |
| UI UX Pro Max und pen.dev | vor dem ersten Einsatz in einem neuen Projekt und nach jedem Update des Skills | Version/Lizenz, CLI-Verfügbarkeit, Authentifizierung, Projektpfade, Codex-Konfiguration, Skill-Workflow und offizielle Dokumentation |
| installierte Design- und Motion-Skills | nach einem Skill-Update und immer dann, wenn ein Skill-Vorschlag einer kanonischen Regel widerspricht, siehe [[00-start/04-plugins-and-skills.md#Vorrang der Brain-Regeln vor Skill-Vorschlägen]] | Version, Lizenz, lokale Einbindung, Zugriffs- und Datenverhalten |
| Inspirationskatalog | wenn eine Referenz für ein Projekt tatsächlich herangezogen wird; [[90-references/reference-research-workflow.md]] verlangt die erneute Prüfung ohnehin vor jeder Übernahme | Erreichbarkeit, neue Fassung, fortbestehende Relevanz |

## Entschieden am 2026-09-11: visuelles Ziel intern statt extern

Die Quellenauswertung vom 11. September 2026 ergab, dass beide Anbieter erstanbieterlich empfehlen, einem Modell ein Bild als Ziel zu geben — Screenshot, Mockup oder Skizze, in frei wählbarem Detailgrad. Das steht in Spannung zur Regel, bei genau einer Website keine Live-Leitreferenz zu wählen.

**Entscheidung: Die Referenzregel bleibt unverändert.** Der Mechanismus wird übernommen, die Quelle nicht. Das visuelle Ziel entsteht projektintern als Stilkachel `D0` und als gebautes Auftaktfeld, beides kanonisch in [[20-design/visual-iteration-loop.md]]. Begründung: Die Regel gegen eine externe Leitreferenz bei Einzelwebsites ist eine bewusste, am 2026-08-19 kanonisierte Entscheidung über Herkunft und Eigenständigkeit; die hier belegte Lücke betrifft dagegen das Fehlen **irgendeines** visuellen Ziels. Ein intern erzeugtes Ziel schließt die Lücke, ohne die Herkunftsfrage neu aufzumachen.

**Auslöser für eine erneute Prüfung:** wenn eine Einzelwebsite trotz vollständig durchlaufenem Loop generisch bleibt. Dann ist zu prüfen, ob das interne Ziel wirklich ausreicht oder ob eine dokumentierte externe Leitreferenz auch bei genau einer Website zugelassen werden muss.

## Offene Frage: Design Contract aus der Stilkachel erzeugen

Im Ablauf eines OpenAI-Mitarbeiters (`Make Work Flow`, 11. September 2026 ausgewertet) entsteht die Design-Dokumentation **aus** Screenshots eines gelungenen Zustands und wird bei jeder Rückmeldung fortgeschrieben, statt vorab von Hand gefüllt zu werden. Der hiesige Design Contract läuft umgekehrt: erst ausfüllen, dann bauen.

Beides hat einen Zweck. Vorab festlegen verhindert die wahrscheinlichste Lösung; nachträglich erfassen hält die Dokumentation am tatsächlich Gebauten. Mit der `D0 Stilkachel` aus [[20-design/visual-iteration-loop.md]] existieren jetzt beide Artefakte nebeneinander.

**Zu prüfen:** ob Teile des Design Contracts künftig aus der gerenderten Kachel abgeleitet statt doppelt gepflegt werden. **Auslöser:** wenn beim nächsten Build auffällt, dass Kachel und Contract auseinanderlaufen.

## Offene Lücke: keine Referenzimplementierung im Brain

Das gesamte Design- und Frontend-Layer ist reine Prosa. In den vierzehn Notizen unter `20-Design/` und `30-Frontend/` steht **kein einziger Codeblock**. Es gibt damit kein Beispiel dafür, wie ein vollständiger Tokenvertrag nach [[20-design/color-system.md#Tokenvertrag]], eine Radius- und Rahmengrammatik nach [[20-design/typography-layout-and-spacing.md#Radiusskala und Rahmenbehandlung]] oder eine Auftaktkomposition nach [[20-design/landing-page-craft.md#Auftakt-Repertoire]] konkret als HTML und CSS aussieht. Jeder Build übersetzt dieselben Regeln neu und landet dabei wieder beim Generator-Default.

Erstanbieterliche Gegenposition aus dem Codex-Bootcamp vom Juni 2026: „Lay the foundation by hand, then let Codex scale it. Manually build a couple of representative features end-to-end. Show Codex what ‚correct' looks like on your team. Codex mimics your best-practices and builds upon them.", dazu das Anti-Muster „Skipping foundations forces constant explicit instruction or costly rewrites."

**Status: offen, bewusst nicht in der Änderung vom 2026-09-11 gelöst.** Eine belastbare Referenzimplementierung ist ein eigener Auftrag und kein Nebenprodukt eines Quellen-Ingests. Zu entscheiden ist vorher, ob sie im Vault oder außerhalb liegt, denn ein mitgeliefertes Beispiel wird von Modellen leicht als Pflichtaussehen gelesen — genau das Problem, das [[20-design/interface-benchmarks.md#H0 Handwerksuntergrenze]] bei B5 bereits einmal korrigieren musste. Auslöser für die Entscheidung: der nächste Website-Auftrag, bei dem dieselbe Tokenlücke erneut auftritt.

## Eingeschränkt geprüfte Referenzen

Diese Seiten benötigen eine erneute manuelle Prüfung in einem vollständigen Browser:

- Die sieben Benchmarkseiten des Sets „Modern Neutral Craft" vom 8. August 2026: Consile, CanDevsDoSomething, Phillip Ohren, EVE BCN, ClaudeFolio, Saad Salman, Thomas Stockham. Belegt sind ausschließlich Markup und CSS. **Tastaturbedienung, Reduced-Motion-Verhalten und mobiles Verhalten sind nicht belegt** und werden vor einer Übernahme genau dieser Aspekte nach [[90-references/reference-research-workflow.md]] interaktiv geprüft. Die statisch belegten Werte bleiben als wählbares Stilprofil in [[20-design/interface-benchmarks.md#B5 Modern Neutral Craft Web]] erhalten; sie sind keine websiteübergreifende Vorgabe.

- Perplexity
- Locomotive
- Active Theory
- Resn
- Studio SPIN
- Humaan

Die Einträge zu Scale Hero, Retro CRT, v0 IRL und Everest entfallen am 2026-08-06, weil diese Referenzen aus dem Katalog entfernt wurden.

Bei der erneuten Prüfung erfassen: Desktop und Mobil, Tastatur, reduzierte Bewegung, Ladeverhalten, Kernstruktur, Interaktionszweck und übertragbares Risiko. Danach Status und Datum im [[90-references/inspiration-catalog.md|Inspiration Catalog]] sowie den Eintrag im [[98-maintenance/change-log.md]] aktualisieren.

## Benchmarks

- **Interaktive Nachprüfung der drei Figma-Benchmarks.** Der 180-Grad-Produktbetrachter, die INIZIO-Solarseite und das ATS-Dashboard wurden am 2026-08-06 nur über ausgelieferte Stilvariablen, Bildassets und Textinhalte ausgewertet. Motion, Tastaturbedienung, Fokusführung und Mobilverhalten sind nicht belegt. Vor einer Übernahme dieser Aspekte in ein Projekt interaktiv nachprüfen und Status in [[90-references/inspiration-catalog.md#Vom Nutzer bewertete Benchmarks]] aktualisieren.
- **Herkunft der Dashboard-Bildvorlage.** Für `B1` liegt nur ein vom Nutzer geliefertes Bild ohne öffentliche Quelle vor. Falls die Originalquelle bekannt wird, Fußnote und Prüfstatus ergänzen.

## Projektbezogene Wiedervorlagen

Projektbezogene Wiedervorlagen können hier gespeichert werden.

Für jedes neue Projekt zusätzlich prüfen:

- Welche Rechtsräume, Zielgruppen und Geschäftsmodelle gelten tatsächlich?
- Sind Marken, Zahlen, Kundenstimmen, Zertifikate und Medien belegbar?
- Sind Bestandswebsite, Speisekarten, Preise, Öffnungszeiten, Google Place ID/Maps-URL und offizielle Profile noch aktuell?
- Steht die im Auftrag genannte Anzahl der Websites in `PROJECT.md` mit wörtlicher Belegstelle?
- Ist das Firmenlogo gefunden und in jeder gebauten Website sichtbar eingesetzt, oder ist sein Fehlen dokumentiert?
- Liegt für jede gebaute Website ein datierter Impeccable KI-Detail-Review mit Befundliste vor?
- Liegt für jede gebaute Website ein datierter `review-animations`-Durchlauf mit Befundliste vor?
- Sind die Copy-Prüffragen aus [[10-strategy/website-copy.md#Prüffragen vor der Abnahme]] auf jeden sichtbaren Text angewandt?
- Ist UI UX Pro Max für jede gebaute Website ausgeführt und mit Datum belegt?
- Ist der Leitbenchmark aus [[20-design/interface-benchmarks.md]] benannt, samt nicht übernommener Elemente?
- Sind alle Bilder überarbeitet, zu einer Serie angeglichen und alle `ai-placeholder`-Bilder mit Ersetzungshinweis übergeben?
- Halten alle Routen das Textbudget aus [[10-strategy/information-density-and-mobile-clarity.md]] ein?
- Bildet die Kopfzeile die tatsächlichen Nutzerziele bei 320, 375, 768, 1280 und 1920 Pixel sowie 200 Prozent Zoom verständlich und ohne unbedienbaren Überlauf ab?
- Ist je Website `release-readiness/<website-slug>.md` aktuell, und stimmen offene sichtbare Hinweise, Vorschau-Sperren, E-Mail-Endpunkte, Integrationen, Search Console sowie Indexierungszustand mit dem ausgelieferten System überein?
- Beschreibt `SOURCE-RIGHTS-REVIEW.md` jeden tatsächlich verwendeten Asset-Eintrag samt Quelle und offenem Hinweis für den Nutzer/Owner, ohne den Build zu verändern?
- Haben sich eingesetzte Frameworks, Browserziele oder Anbieter geändert?
- Sind Datenschutzverträge, Löschfristen und Datenflüsse aktuell?
- Stimmen Sitemap, Rollenmodell, Billing und Deployment noch mit dem Master Spec überein?

## Offene Brain-Themen

- `prefers-reduced-transparency` und `prefers-contrast` sind noch nicht kanonisch geregelt. Aufgenommen am 2026-08-16 aus [[90-references/apple-fluid-interface.md#Barrierefreiheit über Reduced Motion hinaus]]. Kanonischer Besitzer wäre [[30-frontend/accessibility.md]] zusammen mit [[20-design/color-system.md]].
- `improve-animations` aus dem Skillset von Emil Kowalski ist bewusst nicht installiert. Bei einem echten Bestandsaudit erneut bewerten.
