---
type: maintenance
status: canonical
updated: 2026-08-16
next_review: 2026-11-03
---
# Review Queue

Diese Liste enthält bewusst zeitabhängige oder noch nicht vollständig verifizierbare Punkte. Ein leerer Eintrag ist kein Qualitätsziel; eine nachvollziehbare Warteschlange ist besser als versteckte Unsicherheit.

## Regelmäßige Prüfungen

| Fälligkeit | Gegenstand | Umfang | Status |
|---|---|---|---|
| quartalsweise, zuerst 2026-11-03 | Sicherheits- und Authentifizierungsquellen | OWASP, NIST, eingesetzte Auth-Anbieter und Abuse-Schutz | offen |
| quartalsweise, zuerst 2026-11-03 | Plattform- und Billing-Dokumentation | APIs, Webhooks, Kündigungs- und Löschabläufe | offen |
| halbjährlich, zuerst 2027-02-03 | Webstandards und Metriken | WCAG/WAI, Core Web Vitals, Browserunterstützung | offen |
| halbjährlich, zuerst 2027-02-03 | deutsche und europäische Rechtsquellen | DDG, TDDDG, BFSG, DSGVO und Aufsichtsbehörden | offen; fachliche Rechtsprüfung je Projekt |
| halbjährlich, zuerst 2027-02-03 | Tools und Bibliotheken | Lizenz, Wartungszustand, Integrationsweise | offen |
| halbjährlich, zuerst 2027-02-03 | Google Maps/Places | EWR-Bedingungen, erlaubte Speicherung, Attribution, Maps URLs, Embed/API und Datenschutz | offen |
| halbjährlich, zuerst 2027-02-03 | UI UX Pro Max und pen.dev | Version/Lizenz, CLI-Verfügbarkeit, Authentifizierung, Projektpfade, Codex-Konfiguration, Skill-Workflow und offizielle Dokumentation | offen |
| halbjährlich, zuerst 2027-02-04 | Emil Design Engineering, Impeccable und MotionSites AI | Skill-Versionen, Lizenz, lokale Integration, Quellen, Zugriffs-/Datenverhalten sowie die Übertragbarkeit der Promptmuster | offen |
| jährlich, zuerst 2027-08-03 | Inspirationskatalog | Erreichbarkeit, neue Fassung, fortbestehende Relevanz | offen |

## Eingeschränkt geprüfte Referenzen

Diese Seiten benötigen eine erneute manuelle Prüfung in einem vollständigen Browser:

- Die sieben Benchmarkseiten des Sets „Modern Neutral Craft" vom 8. August 2026: Consile, CanDevsDoSomething, Phillip Ohren, EVE BCN, ClaudeFolio, Saad Salman, Thomas Stockham. Belegt sind ausschließlich Markup und CSS. **Tastaturbedienung, Reduced-Motion-Verhalten und mobiles Verhalten sind nicht belegt** und werden vor einer Übernahme genau dieser Aspekte nach [[90-References/Reference Research Workflow]] interaktiv geprüft. Die daraus abgeleiteten Werte in [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]] gelten unabhängig davon, weil sie statisch belegt sind.

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
