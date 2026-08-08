---
type: template
status: canonical
updated: 2026-08-08
---

# Project Master Spec

`Status: draft | approved | building | launched | archived`

## 0 Project Contract

- Kanonischer Projektpfad: `../projekte/<Projektname>/`
- Pflichtdateien verlinkt: `SOURCE-RIGHTS-REVIEW.md`, `ASSET-REGISTER.md`, `DATA-PROCESSING-INVENTORY.md`
- Bestehendes Projekt geöffnet oder neuer Ordner kollisionsfrei angelegt:
- Zutreffende Brain-Notizen und Quality Gates:

## 1 Outcome

- Anzahl der beauftragten Websites und wörtliche Belegstelle aus dem Auftrag; ohne Angabe genau eine:
- Betreiber, Produkt, Zielgruppe, Problem:
- Primäre Nutzeraktion und KPI:
- Nicht-Ziele:
- Annahmen und offene Entscheidungen:

## 2 Scope und Sitemap

- Projekttyp:
- Must/Should/Could/Won't:
- Sitemap: `Route -> Zweck -> CTA -> Index -> Auth/Rolle -> Daten -> Status`; Startseite plus echte verlinkte Unterseiten, nicht nur One-Page-Anker
- Hauptnavigation: höchstens sechs Punkte, gewählte Beschriftungen und Kurzformen, Rest im Fußbereich
- Kritische Nutzerflüsse:

## 3 Content

- Bestandswebsite und Quelleninventar:
- Verifizierte Unternehmensfakten, Öffnungszeiten, Angebote, Preise/Speisekarte und Aktualitätsdatum; Maps-Hinweise nur mit Primärquellenbestätigung:
- Google Place ID/Maps-URL, erlaubter Integrationsweg und Fallback:
- Verifizierte offizielle Profile und Linkziele:
- Übernommene, neu formulierte, verworfene und noch zu bestätigende Inhalte:
- Value Proposition:
- Voice und verbotene Muster:
- Reale Belege:
- Content Owner und Status:

## 4 Design Contract

- Attribute/Anti-Attribute, visuelles Leitmotiv, primärer/sekundärer Archetyp:
- Leitbenchmark aus [[20-Design/Interface Benchmarks]], übernommene und ausdrücklich nicht übernommene Elemente:
- Schriftentscheidung mit Herleitung und Nachweis, dass kein Retro-Verstoß nach [[20-Design/Typography Layout and Spacing#Retro-Verbot]] vorliegt:
- Bildplan nach [[20-Design/Imagery and AI Editing]]: Rolle je Bild, Bearbeitungsbedarf, Freistellungen, Serienkonsistenz, Liste der `ai-placeholder`-Bilder mit Prompt und Ersetzungshinweis:
- Informations- und Textbudget je Route nach [[10-Strategy/Information Density and Mobile Clarity]], einschließlich Sektionsliste mit je einer Nutzerfrage:
- Interaktives Kernmodul je Landing Page: Modul, Datenquelle, Bedienung, Zustände, Fallback:
- Auftaktkomposition und Anordnung der Überschriften je Sektionsart, mit Begründung der Abweichung vom Standardmuster:
- Landing-Page-Haltung: was ist extravagant, was bleibt ruhig, wo liegt die Grenze:
- Firmenlogo: gefunden ja/nein, Quelle, sichtbarer Einsatzort je Website, Bearbeitungsschritte:
- Inspirationsmatrix: Quellen, Rollen, statischer/interaktiver Nachweis, direkt übernommene/adaptierte Prinzipien und tatsächlicher Einsatz:
- Negativreferenzen und daraus abgeleitete Verbote:
- UI UX Pro Max: Query, Datum, Ergebnisartefakt, Pflicht-Detailabfragen zu `landing`, `style`, `color`, `typography`, `ux`, `gsap` und Stack, gewählte Regeln und Abweichungen:
- Impeccable KI-Detail-Review je gebauter Website: Datum, Befunde, Umsetzungsstand:
- pen.dev: `use | skip`, Begründung, `.pen`-Pfade und Freigabestatus:
- Farbrollen mit benannter Herleitung, Typografie, Spacing, Grid, Radius, Shadow, Motion; keine verbrauchte Farbwelt als dominante Fläche:
- Tokenvertrag nach [[20-Design/Color System#Tokenvertrag]] mit gesetztem Wert je Pflichtrolle für Light und Dark, Quelle der Werte im Code:

| Rolle | Wert hell | Wert dunkel | Herleitung |
|---|---|---|---|
| `bg` | | | |
| `surface` | | | |
| `surface-alt` | | | |
| `text` / `text-secondary` / `text-tertiary` | | | |
| `border` / `border-hover` | | | |
| `accent` / `accent-subtle` / `accent-contrast` | | | |
| `focus` | | | |
| `success` / `warning` / `danger` je mit `-subtle` | | | |

- Formsprache: die vier Radiusstufen nach [[20-Design/Typography Layout and Spacing#Radiusskala]] mit gesetzten Werten, die eine Rahmenstärke, die eine Schattenstufe und ihre Einsatzorte:
- Bewegungstokens nach [[20-Design/Motion and Interaction#Standardrezepte mit Werten]]: Kurvensatz, vier Dauerstufen, gewählte Rezepte je Komponente, begründete Abweichungen:
- Kernartefakt/Leitmedium, direkter Einsatz/Adaption, Quelle für spätere Owner-Einschätzung, Poster und Fallback:
- Responsive, Zustände und Reduced-Motion-Verhalten:
- Motion Inventory je primärer Route: globale Bewegung, Einstieg, kontinuierliche Scrollsequenz, zwei weitere Scroll-/In-View-Bewegungen, Interaktionsdetails, Messung und Trace/Video:
- Novelty Budget:

### Website-Matrix

Genau so viele Zeilen wie im Auftrag verlangte Websites. Bei einer Website liegt der Pfad unter `site/`, bei mehreren unter `versions/NN-…`.

| Website und Pfad | Leitidee / UI- und Unterseiten-Unterschied | Lokaler Port und Startbefehl | Motion-Choreografie und Fallback | Visual-/A11y-/Performance-/SEO-Nachweis | Impeccable-Review | Lieferstatus |
|---|---|---|---|---|---|---|
| | | | | | | |

## 5 Engineering Contract

- Stack und Begründung:
- Ordner-, Styling-, State- und Datenstrategie:
- Komponenten/Zustände:
- Browser-/Gerätesupport:
- Performancebudgets:

## 6 Data Security Billing

- Datenmodell, Rollen, RLS/AuthZ:
- Auth- und Account-Linking-Flows:
- API-/Upload-/AI-Limits und Kostenbudgets:
- Subscription State Machine und Account-Löschung:
- Bedrohungen und Controls:

## 7 Legal

- Märkte, Impressum, Privacy, Consent, Accessibility, Verbraucherpflichten; nur prüfpflichtige Entwürfe und benannter Owner für eine spätere Einschätzung:
- Dienstleister/Transfers/AVV:
- tatsächlicher Asset- und Quelleneinsatz; spätere Owner-Hinweise in `SOURCE-RIGHTS-REVIEW.md`, ohne Ersatz, Auslassung oder KI-Entscheidung:
- Altes Impressum/Privacy als Faktenquelle ausgewertet; neue Datenflüsse abgeglichen:
- spätere fachliche Einschätzung durch Nutzer/Owner, ohne technische Sperre durch die KI:

## 8 SEO Analytics

- Titelkonvention ohne `|`, Metadaten, Canonical, Structured Data für jede Route jeder gebauten Website:
- sitemap.xml, robots, Redirects für jede gebaute Website:
- Messplan und Consent-Kategorie:

## 9 Delivery Operations

- Projektwurzel unter `../projekte/<Projektname>/`, Environments, Dependencies, Ein-Klick-Start:
- Deploy, Migration, Rollback:
- Monitoring, Alerts, Backup, Owner:

## 10 Acceptance

- Verweis auf [[70-QA/Quality Gates]] und projektspezifische Kriterien:
- Nachweise:
- Bekannte Restrisiken:
- Nutzer-/Owner-Entscheidung über eine spätere Veröffentlichung mit Datum/Owner; keine KI-Freigabe:

## Change Impact

Bei jeder Änderung: kanonischer Owner, betroffene Abschnitte/Artefakte, Tests, Changelog.
