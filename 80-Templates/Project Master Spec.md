---
type: template
status: canonical
updated: 2026-08-27
---

# Project Master Spec

`Status: draft | approved | building | launched | archived`

## 0 Project Contract

- Kanonischer Projektpfad: `../projekte/<Projektname>/`
- Pflichtdateien verlinkt: `SOURCE-RIGHTS-REVIEW.md`, `ASSET-REGISTER.md`, `DATA-PROCESSING-INVENTORY.md` und je Website `release-readiness/<website-slug>.md`
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
- Navigationsmodell: direkte Ziele, Gruppen/Untermenüs, Utility-Ebene, Footer, reale Beschriftungen und Responsive-Übergang mit Begründung
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

## 4 Design Contracts je Website

Dieser Unterabschnitt wird **für jede gebaute Website vollständig wiederholt**. Es gibt keine projektweiten „Global Rules“ für Art Direction, die mehrere Fassungen auf dieselbe Formsprache ziehen. Gemeinsame Fakten und Funktionsanforderungen bleiben außerhalb der Design Contracts kanonisch.

### Website `<website-slug>` Design Contract

- Pfad und Slug; zugehöriges UI-UX-Pro-Max-Artefakt `design-system/<website-slug>/MASTER.md`:
- Attribute/Anti-Attribute, visuelles Leitmotiv, primärer/sekundärer Archetyp:
- Leitbenchmark aus [[20-Design/Interface Benchmarks]], übernommene und ausdrücklich nicht übernommene Elemente:
- Primärschrift; Zweitschrift oder bewusster Verzicht; genaue Rollen, Lizenz, Lesbarkeit, beabsichtigter Zeitbezug und Herleitung nach [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]]:
- Bildplan nach [[20-Design/Imagery and AI Editing]]: Rolle je Bild, Bearbeitungsbedarf, Freistellungen, Serienkonsistenz, Liste der `ai-placeholder`-Bilder mit Prompt und Ersetzungshinweis:
- Informations- und Textbudget je Route nach [[10-Strategy/Information Density and Mobile Clarity]], einschließlich Sektionsliste mit je einer Nutzerfrage:
- Primäre Beweisform und konkreter Inhaltsanker je Landing Page; bei Interaktion zusätzlich Modul, Datenquelle, Bedienung, Zustände und Fallback:
- Auftaktkomposition und Anordnung der Überschriften je Sektionsart; Nachweis, dass H1, Inhaltsanker und primäre Handlung an den Prüfbreiten ohne Anschnitt, Überlagerung oder Kopfzeilenkollision lesbar sind:
- Kopfzeileninventar und -anordnung, Navigationsbeschriftung, Fußbereichsstruktur und sonstiges Seiten-Chrome:
- Landing-Page-Haltung: wodurch entsteht Nutzwert und Interesse; was ist ausdrucksstark, was bleibt ruhig; wann beginnt innerhalb der ersten zwei Bildschirmhöhen die nächste Nutzerfrage oder der erste Beweis:
- Firmenlogo: gefunden ja/nein, Quelle, sichtbarer Einsatzort je Website, Bearbeitungsschritte:
- Referenzmodus nach [[90-References/Reference Research Workflow]]: `Eigenentwurf | nutzer-vorgegeben | ausgewählte Leitreferenz`:
- Bei `Eigenentwurf`: Herleitung aus Projektwahrheit, Inhaltsanker, Leitbenchmark und Nutzerfragen; Bestätigung, dass keine externe Seite verdeckt als Vorlage dient:
- Nur bei `ausgewählte Leitreferenz`: Referenz-Shortlist aus [[90-References/Website Reference Pool]] mit mindestens drei plausiblen konkreten Live-Seiten, sofern vorhanden; je direkte URL, Passung und Entscheidung:
- Nur bei `nutzer-vorgegeben` oder `ausgewählte Leitreferenz`: direkte URL, fachliche und gestalterische Passung, Übernahmetiefe `punktuell | teilweise | prägend` mit optionaler Prozentangabe, statischer/interaktiver Nachweis, übernommene Grundstruktur/Design-/Motionprinzipien, bewusste Abweichungen und tatsächlicher Einsatz:
- Bei mehreren Websites: Nachweis, dass genau eine Fassung den Modus `ausgewählte Leitreferenz` besitzt, sofern starke Passung gefunden wurde, und die übrigen Eigenentwürfe die Referenz nicht quer übernehmen; andernfalls dokumentierte erfolglose Suche:
- Optionale Negativreferenzen und daraus abgeleitete Verbote:
- UI UX Pro Max: Query, Datum, **website-spezifisches** Ergebnisartefakt, Pflicht-Detailabfragen zu `landing`, `style`, `color`, `typography`, `ux`, `gsap` und Stack, gewählte Regeln und Abweichungen:
- Impeccable KI-Detail-Review je gebauter Website: Datum, Befunde, Umsetzungsstand:
- pen.dev: `use | skip`, Begründung, `.pen`-Pfade und Freigabestatus:
- H0-Handwerksuntergrenze nach [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]] und gewählte variable Stilparameter für Flächen, Radius, Rahmen, Tiefe, Karten, Kopfzeile, Zweitschrift und Motion:
- Farbrollen mit benannter Herleitung, Typografie, Spacing, Grid, Radius, Shadow und Motion; häufige Defaults bewusst entschieden:
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

- Formsprache: gewählte Radiusskala und Rahmenbehandlung nach [[20-Design/Typography Layout and Spacing#Radiusskala und Rahmenbehandlung]], Tiefenregeln und Einsatzorte:
- Komponentenrepertoire: Karte gegen Zeile gegen Tabelle gegen Liste je Inhaltsart; optionale B5-Karte ausdrücklich benannt:
- Bewegungstokens: eigener Kurven- und Dauersatz, Grammatik je Komponente; B5-Beispiele aus [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] nur bei bewusster Übernahme:
- Kernartefakt/Leitmedium, direkter Einsatz/Adaption, Quelle für spätere Owner-Einschätzung, Poster und Fallback:
- Responsive, Zustände und Reduced-Motion-Verhalten:
- Motion-Budget `none | low | medium | high` und Inventory der tatsächlich eingesetzten relevanten Bewegungen: Zweck, Trigger, Interaktionsdetails, Fallback, Messung und Trace/Video:
- Novelty Budget:

### Abstand zu Vorgängerfassungen

Vor UI-Code ausfüllen, wenn frühere Fassungen desselben Betriebs existieren.

| Vorgänger | Fakten/Infrastruktur/Assets bewusst übernommen | Leitmotiv/Fassungsname/Signalfarbe/Kernmodul bewusst anders | begründete Wiederholung |
|---|---|---|---|
| | | | |

### Website-Matrix

Genau so viele Zeilen wie im Auftrag verlangte Websites. Bei einer Website liegt der Pfad unter `site/`, bei mehreren unter `versions/NN-…`.

| Website und Pfad | Leitidee / UI- und Unterseiten-Unterschied | Zugriff: `johannstein.com/dev` auf 217.154.218.30 oder lokaler Port/Start außerhalb | Motion-Choreografie und Fallback | Visual-/A11y-/Performance-/SEO-Nachweis | Impeccable-Review | Lieferstatus |
|---|---|---|---|---|---|---|
| | | | | | | |

### Unterscheidungsmatrix

Pflicht bei mehr als einer Website und **vor der ersten Zeile UI-Code** auszufüllen. Für jede weitere Website eine Spalte ergänzen. Zuerst gemeinsame Nutzerfragen, stärkste Beweisformen und sachlich beste Grobstruktur festhalten; erst danach mindestens fünf wirksame Gestaltungsachsen unterscheiden. Dieselbe sachlich beste Lösung darf wiederkehren. Keine Fassung wird durch einen schwächeren Auftakt, fehlenden Inhaltsanker, unlesbare Typografie oder ein lautereres Epochenzitat künstlich abgesetzt. Siehe [[20-Design/Design Direction#Stilabstand bei mehreren Websites]].

| Pflichtachse | Website 01 | Website 02 | weitere Website(s) | paarweiser Nachweis |
|---|---|---|---|---|
| Grundhelligkeit und Farbwelt | | | | |
| Primärschrift | | | | |
| Zweitschrift und ihre Rollen oder bewusster Verzicht | | | | |
| Auftaktkomposition | | | | |
| Raster- und Flächenlogik | | | | |
| Kopfzeileninventar und -anordnung | | | | |
| Navigationsbeschriftung | | | | |
| Fußbereichsstruktur | | | | |
| Seitenmöblierung/Chrome | | | | |
| Komponentenrepertoire: Karte/Zeile/Tabelle/Liste | | | | |
| Leitbewegung | | | | |
| Sektionsreihenfolge und Dramaturgie | | | | |
| primäre Beweisform | | | | |
| Tonfall der Copy | | | | |

### Copy-Entscheidung

Nach [[10-Strategy/Website Copy]] festhalten:

- Anrede und Tonfall je Website:
- Stellen mit zusammenhängenden ganzen Sätzen je Route:
- geprüfte Verbotsliste durchlaufen am (Datum):

## 5 Engineering Contract

- Stack und Begründung:
- Ordner-, Styling-, State- und Datenstrategie:
- Inhaltsblöcke: stabile Block-ID und JSON-Pointer, `owner_editable`, Feldtyp, Grenzen, Preview-Routen, Veröffentlichungspolicy, Risiko und Verantwortlicher nach [[80-Templates/Owner Hosting Website Contract]]:
- bei Owner-Hosting: Pfade zu `content/<website>.json` und `owner-hosting/tenant.json`, `tenant_slug`, Domains, Buildprofil, Ausgabeordner, Smoke-Pfade und Capabilities:
- bei Vertragsupdate: alte/neue `schema_version`, erhaltene, neue, migrierte, entfernte und inkompatible Owner-Pointer sowie Behandlung offener Entwürfe:
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
- Dienstleister/Transfers/AVV; bei Owner-Hosting Rollenverteilung und AVV-Prüfung nach [[60-Operations/Owner Hosting and Dashboard]]:
- tatsächlicher Asset- und Quelleneinsatz; spätere Owner-Hinweise in `SOURCE-RIGHTS-REVIEW.md`, ohne Ersatz, Auslassung oder KI-Entscheidung:
- Altes Impressum/Privacy als Faktenquelle ausgewertet; neue Datenflüsse abgeglichen:
- spätere fachliche Einschätzung durch Nutzer/Owner, ohne technische Sperre durch die KI:

## 8 SEO Analytics

- Titelkonvention ohne `|`, Metadaten, Canonical, Structured Data für jede Route jeder gebauten Website:
- sitemap.xml, robots, Redirects für jede gebaute Website:
- Messplan und Consent-Kategorie:
- Search-Console-Property, Verifikationsweg, Sitemap-Einreichung und bei API-Nutzung Auth-/Query-Nachweis:

## 9 Delivery Operations

- Projektwurzel unter `../projekte/<Projektname>/`, Environments und Dependencies; auf `217.154.218.30` Developer-Plattform ohne Projektport, sonst Ein-Klick-Start:
- Deploy, Migration, atomarer Release und Rollback; bei Owner-Hosting zentrale Registry, Dashboard-Subdomain, Projekt-Basis/Owner-Overlay, Wartungsmodus und Release-Historie:
- Monitoring, Alerts, Backup, Owner:
- Release-Readiness-Register je Website: Pfad, offene P0/P1, letzter Produktionsabgleich und Owner:

## 10 Acceptance

- Verweis auf [[70-QA/Quality Gates]] und projektspezifische Kriterien:
- Nachweise, einschließlich echter Darstellung an allen Prüfbreiten, Kontextkontrast und Kopfzeilengeometrie:
- Bekannte Restrisiken:
- Nutzer-/Owner-Entscheidung über eine spätere Veröffentlichung mit Datum/Owner; keine KI-Freigabe:

## Change Impact

Bei jeder Änderung: kanonischer Owner, betroffene Abschnitte/Artefakte, Tests, Changelog.
