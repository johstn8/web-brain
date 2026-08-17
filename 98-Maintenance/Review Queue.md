---
type: maintenance
status: canonical
updated: 2026-08-17
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
| Sicherheits- und Authentifizierungsquellen | [[40-Backend-Security/Security Baseline]], [[40-Backend-Security/Authentication and Accounts]] | OWASP, NIST, eingesetzte Auth-Anbieter und Abuse-Schutz | Routine `Web-Brain Quartalsprüfung Sicherheit und Billing`, 1. Februar, Mai, August und November, 7 Uhr UTC | auf Eis gelegt am 2026-08-16; siehe Hinweis unter der Tabelle |
| Plattform- und Billing-Dokumentation | [[40-Backend-Security/Data APIs and Billing]] | APIs, Webhooks, Kündigungs- und Löschabläufe | dieselbe Routine | auf Eis gelegt am 2026-08-16; siehe Hinweis unter der Tabelle |

**Auf Eis, Stand 2026-08-16.** Die Routine ist inhaltlich fertig, aber nicht angelegt. Das Claude-Konto ist inzwischen mit GitHub verknüpft, die GitHub-App hat jedoch keinen Zugriff auf das private Repository `johstn8/web-brain`, weshalb die API die Anlage ablehnt. Der Nutzer hat das Thema am 2026-08-16 ausdrücklich zurückgestellt. **Damit findet für diese beiden Zeilen derzeit keine Prüfung statt.** Zum Aufwecken genügt es, das Repository unter https://github.com/settings/installations für die Claude-App freizugeben und die Routine mit den Angaben aus der Tabelle und dem folgenden Absatz anzulegen.

Die Routine liest die Fußnoten-URLs der drei Notizen, vergleicht sie mit der abgeleiteten Aussage und schreibt ihr Ergebnis direkt nach `main`. Ohne Befund aktualisiert sie nur Datum und Status dieser beiden Zeilen, damit sichtbar bleibt, dass sie gelaufen ist. Mit Befund legt sie einen Abschnitt `Befunde der Quartalsprüfung` in dieser Notiz an. Eindeutige Änderungen übernimmt sie selbst, alles Abwägungsbedürftige markiert sie als offene Entscheidung. Den Graphen baut sie nicht neu; das holt die nächste lokale Sitzung nach.

## Anlassgebunden geprüft

Diese Quellen werden geprüft, wenn sie gebraucht werden, nicht nach Kalender. Der Auslöser ist jeweils ein Schritt, der im Projekt ohnehin stattfindet. Ergebnis und Datum werden in der jeweiligen kanonischen Notiz vermerkt.

| Gegenstand | Auslöser | Umfang |
|---|---|---|
| Webstandards und Metriken | bevor ein Grenzwert aus diesen Quellen in einem Projekt gesetzt wird, spätestens bei den Gates `G3` und `G4` in [[70-QA/Quality Gates]] | WCAG/WAI, Core Web Vitals, Browserunterstützung |
| deutsche und europäische Rechtsquellen | sobald ein Projekt Rechtstexte, Consent oder Datenerhebung erhält, über [[50-Legal/Legal Decision Tree]] | DDG, TDDDG, BFSG, DSGVO und Aufsichtsbehörden; die fachliche Rechtsprüfung je Projekt ersetzt das nicht |
| Tools und Bibliotheken | bevor eine Bibliothek neu in ein Projekt aufgenommen wird, nach [[60-Operations/Dependencies and Environments]] | Lizenz, Wartungszustand, Integrationsweise |
| Google Maps/Places | sobald eine Website Karte, Ortsdaten oder ein Unternehmensprofil einbindet | EWR-Bedingungen, erlaubte Speicherung, Attribution, Maps URLs, Embed/API und Datenschutz |
| UI UX Pro Max und pen.dev | vor dem ersten Einsatz in einem neuen Projekt und nach jedem Update des Skills | Version/Lizenz, CLI-Verfügbarkeit, Authentifizierung, Projektpfade, Codex-Konfiguration, Skill-Workflow und offizielle Dokumentation |
| installierte Design- und Motion-Skills | nach einem Skill-Update und immer dann, wenn ein Skill-Vorschlag einer kanonischen Regel widerspricht, siehe [[00-Start/04 Plugins and Skills#Vorrang der Brain-Regeln vor Skill-Vorschlägen]] | Version, Lizenz, lokale Einbindung, Zugriffs- und Datenverhalten |
| Inspirationskatalog | wenn eine Referenz für ein Projekt tatsächlich herangezogen wird; [[90-References/Reference Research Workflow]] verlangt die erneute Prüfung ohnehin vor jeder Übernahme | Erreichbarkeit, neue Fassung, fortbestehende Relevanz |

## Eingeschränkt geprüfte Referenzen

Diese Seiten benötigen eine erneute manuelle Prüfung in einem vollständigen Browser:

- Die sieben Benchmarkseiten des Sets „Modern Neutral Craft" vom 8. August 2026: Consile, CanDevsDoSomething, Phillip Ohren, EVE BCN, ClaudeFolio, Saad Salman, Thomas Stockham. Belegt sind ausschließlich Markup und CSS. **Tastaturbedienung, Reduced-Motion-Verhalten und mobiles Verhalten sind nicht belegt** und werden vor einer Übernahme genau dieser Aspekte nach [[90-References/Reference Research Workflow]] interaktiv geprüft. Die statisch belegten Werte bleiben als wählbares Stilprofil in [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]] erhalten; sie sind keine websiteübergreifende Vorgabe.

- Perplexity
- Locomotive
- Active Theory
- Resn
- Studio SPIN
- Humaan

Die Einträge zu Scale Hero, Retro CRT, v0 IRL und Everest entfallen am 2026-08-06, weil diese Referenzen aus dem Katalog entfernt wurden.

Bei der erneuten Prüfung erfassen: Desktop und Mobil, Tastatur, reduzierte Bewegung, Ladeverhalten, Kernstruktur, Interaktionszweck und übertragbares Risiko. Danach Status und Datum im [[90-References/Inspiration Catalog|Inspiration Catalog]] sowie den Eintrag im [[Change Log]] aktualisieren.

## Benchmarks

- **Interaktive Nachprüfung der drei Figma-Benchmarks.** Der 180-Grad-Produktbetrachter, die INIZIO-Solarseite und das ATS-Dashboard wurden am 2026-08-06 nur über ausgelieferte Stilvariablen, Bildassets und Textinhalte ausgewertet. Motion, Tastaturbedienung, Fokusführung und Mobilverhalten sind nicht belegt. Vor einer Übernahme dieser Aspekte in ein Projekt interaktiv nachprüfen und Status in [[90-References/Inspiration Catalog#Vom Nutzer bewertete Benchmarks]] aktualisieren.
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
- Sind die Copy-Prüffragen aus [[10-Strategy/Website Copy#Prüffragen vor der Abnahme]] auf jeden sichtbaren Text angewandt?
- Ist UI UX Pro Max für jede gebaute Website ausgeführt und mit Datum belegt?
- Ist der Leitbenchmark aus [[20-Design/Interface Benchmarks]] benannt, samt nicht übernommener Elemente?
- Sind alle Bilder überarbeitet, zu einer Serie angeglichen und alle `ai-placeholder`-Bilder mit Ersetzungshinweis übergeben?
- Halten alle Routen das Textbudget aus [[10-Strategy/Information Density and Mobile Clarity]] ein?
- Hält die Kopfzeile bei 1280, 1440 und 1920 Pixel die Grenze von sechs Punkten und die Einzeiligkeit ein?
- Beschreibt `SOURCE-RIGHTS-REVIEW.md` jeden tatsächlich verwendeten Asset-Eintrag samt Quelle und offenem Hinweis für den Nutzer/Owner, ohne den Build zu verändern?
- Haben sich eingesetzte Frameworks, Browserziele oder Anbieter geändert?
- Sind Datenschutzverträge, Löschfristen und Datenflüsse aktuell?
- Stimmen Sitemap, Rollenmodell, Billing und Deployment noch mit dem Master Spec überein?

## Offene Brain-Themen

- `prefers-reduced-transparency` und `prefers-contrast` sind noch nicht kanonisch geregelt. Aufgenommen am 2026-08-16 aus [[90-References/Apple Fluid Interface#Barrierefreiheit über Reduced Motion hinaus]]. Kanonischer Besitzer wäre [[30-Frontend/Accessibility]] zusammen mit [[20-Design/Color System]].
- `improve-animations` aus dem Skillset von Emil Kowalski ist bewusst nicht installiert. Bei einem echten Bestandsaudit erneut bewerten.
