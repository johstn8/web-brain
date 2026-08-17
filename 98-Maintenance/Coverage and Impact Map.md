---
type: canonical
status: canonical
updated: 2026-08-17
---

# Coverage and Impact Map

Diese Karte verhindert Teilupdates. Änderungen werden zuerst einem kanonischen Bereich zugeordnet und anschließend durch alle betroffenen Artefakte verfolgt.

## Kanonische Zuständigkeit

| Thema | Kanonische Notiz | Häufig betroffene Notizen |
|---|---|---|
| globale Arbeitsregeln | [[00-Start/01 Core Rules|Core Rules]] | `AGENTS.md`, AI Build Prompt, Quality Gates |
| Navigation und Lesereihenfolge | [[00-Start/00 Brain Index|Brain Index]] | Routing Map, README |
| Web-Produkt-Ablauf | [[00-Start/05 Web Product Workflow|Web Product Workflow]] | Routing Map, Intake, Master Spec, AI Build Prompt, Quality Gates |
| Anzahl der Websites | [[00-Start/05 Web Product Workflow|Web Product Workflow]] | Delivery, Master Spec, Sitemap, Design Direction, Motion, SEO, Tests, Quality Gates, Decision Log |
| Kopfzeile und Hauptnavigation | [[30-Frontend/Components and UI States|Components and UI States]] | Information Architecture, Design Direction, Test Matrix, Quality Gates |
| generische KI-Anmutung und Kicker | [[20-Design/Anti AI Slop|Anti AI Slop]] | Design Direction, Derived Design Patterns, Plugins and Skills, Quality Gates |
| Logo des Betriebs | [[20-Design/Design Direction|Design Direction]] | Existing Website Rebuild, Asset Register, Source and Rights Review, Quality Gates |
| Landing-Page-Anspruch | [[20-Design/Design Direction|Design Direction]] | Derived Design Patterns, Inspiration Catalog, Master Spec, QA |
| KI-Fähigkeiten und Pflichtskills | [[00-Start/04 Plugins and Skills|Plugins and Skills]] | Design Direction, Master Spec, Quality Gates, Review Queue |
| Aktualisierung | [[00-Start/03 Update Protocol|Update Protocol]] | Change Log, Review Queue, diese Karte |
| Synchronisation und Versionierung des Vaults | `AGENTS.md`, Abschnitt Synchronisation | Update Protocol, Change Log, `.gitignore` |
| Projektumfang | [[10-Strategy/Discovery and Scope|Discovery and Scope]] | Intake, Master Spec, Sitemap |
| Relaunch und Quellenwiederherstellung | [[10-Strategy/Existing Website Rebuild|Existing Website Rebuild]] | Project Workflow, Content, Legal, Privacy, Assets, Source and Rights Review, Master Spec, QA |
| Sitemap | [[10-Strategy/Information Architecture and Sitemap|Information Architecture and Sitemap]] | Master Spec, SEO, Accessibility, Tests |
| Inhalte und Conversion | [[10-Strategy/Content and Conversion|Content and Conversion]] | Design Direction, SEO, Legal |
| Formulierung, Satzform und Textmuster der Copy | [[10-Strategy/Website Copy|Website Copy]] | Content and Conversion, Information Density, Anti AI Slop, Design Direction, Components and UI States, Quality Gates |
| Stilabstand zwischen mehreren Websites und Vorgängerfassungen | [[20-Design/Design Direction#Stilabstand bei mehreren Websites|Design Direction]] | Web Product Workflow, Master Spec, Interface Benchmarks, Typography, Components, Motion, Quality Gates |
| H0-Handwerksuntergrenze, Stilprofile und Leitbenchmark | [[20-Design/Interface Benchmarks|Interface Benchmarks]] | AGENTS, Core Rules, Inspiration Catalog, Design Direction, Color System, Typography, Components, Motion, Derived Design Patterns, Quality Gates |
| Bilder, Bildbearbeitung und KI-Platzhalter | [[20-Design/Imagery and AI Editing|Imagery and AI Editing]] | Design Direction, Asset Register, Source and Rights Review, Performance, Accessibility, Quality Gates |
| Informationsmenge, Textbudget, mobile Dosierung | [[10-Strategy/Information Density and Mobile Clarity|Information Density and Mobile Clarity]] | Content and Conversion, Information Architecture, Design Direction, Responsive Design, Quality Gates |
| Retro-Verbot und Schriftwahl | [[20-Design/Typography Layout and Spacing|Typography Layout and Spacing]] | Anti AI Slop, Color System, Design Direction, Asset Register, Quality Gates |
| interaktives Kernmodul | [[20-Design/Motion and Interaction|Motion and Interaction]] | Design Direction, Components and UI States, Accessibility, Performance, Quality Gates |
| visuelle Richtung | [[20-Design/Design Direction|Design Direction]] | Farbe, Typografie, Motion, Master Spec |
| Tokenvertrag mit Pflichtrollen | [[20-Design/Color System#Tokenvertrag|Color System]] | Interface Benchmarks, Design Direction, Components and UI States, Architecture and Code Consistency, Master Spec, AI Build Prompt, Quality Gates |
| Radiusskala, Rahmenbehandlung und Tiefe je Website | [[20-Design/Typography Layout and Spacing#Radiusskala und Rahmenbehandlung|Typography Layout and Spacing]] | Interface Benchmarks, Anti AI Slop, Components, Design Direction, Master Spec, Quality Gates |
| Komponentenrepertoire und Kopfzeileninventar je Website | [[30-Frontend/Components and UI States|Components and UI States]] | Interface Benchmarks, Anti AI Slop, Design Direction, Accessibility, Quality Gates |
| website-spezifische Bewegungswerte und B5-Beispiele | [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele|Motion and Interaction]] | Interface Benchmarks, Components, Design Direction, Accessibility, Performance, Master Spec, AI Build Prompt, Quality Gates |
| Farbe | [[20-Design/Color System|Color System]] | Accessibility, Tokens, QA |
| Typografie und Layout | [[20-Design/Typography Layout and Spacing|Typography Layout and Spacing]] | Responsive Design, Assets, QA |
| responsive Verhalten | [[20-Design/Responsive Design|Responsive Design]] | Components, Accessibility, Test Matrix |
| Interaktion und Motion | [[20-Design/Motion and Interaction|Motion and Interaction]] | Performance, Accessibility, Tests |
| gestengeführte und federbasierte Bewegung | [[90-References/Apple Fluid Interface|Apple Fluid Interface]] | Motion and Interaction, Components and UI States, Accessibility |
| Architektur | [[30-Frontend/Architecture and Code Consistency|Architecture and Code Consistency]] | Dependencies, Delivery, Security |
| Komponenten und Zustände | [[30-Frontend/Components and UI States|Components and UI States]] | Accessibility, Test Matrix, Master Spec |
| Barrierefreiheit | [[30-Frontend/Accessibility|Accessibility]] | Design, Components, Legal, Tests |
| Performance | [[30-Frontend/Performance|Performance]] | Architecture, Media, Observability, Tests |
| SEO | [[30-Frontend/SEO and Discoverability|SEO and Discoverability]] | Sitemap, Content, Launch Checklist |
| Sicherheit | [[40-Backend-Security/Security Baseline|Security Baseline]] | Auth, APIs, Dependencies, QA |
| Konten | [[40-Backend-Security/Authentication and Accounts|Authentication and Accounts]] | Data APIs, Privacy, Test Matrix |
| Vorschau-Sperre | [[40-Backend-Security/Preview Access Gate|Preview Access Gate]] | Security Baseline, Delivery, SEO, QA |
| Daten, API, Billing | [[40-Backend-Security/Data APIs and Billing|Data APIs and Billing]] | Security, Privacy, Operations, Tests |
| Rechtliche Einordnung | [[50-Legal/Legal Decision Tree|Legal Decision Tree]] | Privacy, Assets, Accessibility, Launch |
| Datenschutz und Consent | [[50-Legal/Privacy and Consent|Privacy and Consent]] | Data Inventory, Analytics, Tests |
| Asset-Einsatz und spätere Owner-Einschätzung | [[50-Legal/Assets Copyright and Licenses|Assets Copyright and Licenses]] | Design, Performance, Source and Rights Review, Asset Register |
| lokale Ausführung, Serverzugriff und Developer-Plattform | [[60-Operations/Delivery and Local Start|Delivery and Local Start]] | Workflow, Dependencies, Accessibility, Preview Access Gate, Observability, Launch |
| Owner-Hosting, zentraler Mandantenbetrieb und editierbare Inhalte | [[60-Operations/Owner Hosting and Dashboard|Owner Hosting and Dashboard]] | Owner Hosting Website Contract, Core Rules, Routing Map, Workflow, Master Spec, Data Processing Inventory, Auth, Privacy, Legal, Delivery, Observability, Quality Gates |
| Abhängigkeiten | [[60-Operations/Dependencies and Environments|Dependencies and Environments]] | Architecture, Security, Delivery |
| Betrieb | [[60-Operations/Observability and Maintenance|Observability and Maintenance]] | Security, Billing, QA |
| Abnahme | [[70-QA/Quality Gates|Quality Gates]] | Test Matrix, Launch Checklist |
| Referenzmuster | [[90-References/Derived Design Patterns|Derived Design Patterns]] | Catalog, Design Direction, Master Spec |
| Inspirationsrecherche und Evidenz | [[90-References/Reference Research Workflow|Reference Research Workflow]] | Catalog, Motion, Master Spec, Test Matrix, Quality Gates |
| pen.dev und `.pen`-Designquellen | [[90-References/pen.dev Workflow|pen.dev Workflow]] | Tools and Libraries, Plugins and Skills, Design Direction, Delivery, Master Spec, QA |

## Auslöser und Pflichtfolgen

### Neuer Website-Auftrag

Bestimme zuerst die Anzahl der Websites aus dem Auftragstext nach [[00-Start/05 Web Product Workflow#Anzahl der Websites]]. Lege dann den kollisionsfreien Projektordner samt PROJECT.md, Source/Rights Review, Asset Register und Data Processing Inventory an. Baue anschließend genau diese Anzahl vollständiger Websites unter `site/` beziehungsweise `versions/NN-…`, jeweils mit allen Unterseiten, Motion Inventory, SEO-Artefakten und Nachweisen. Auf `217.154.218.30` erfolgt Zugriff über `johannstein.com/dev` ohne Projektport, sonst über einen eigenen festen Port. Verlinke zutreffende Brain-Regeln und Quality Gates. Keine Recherche- oder Build-Artefakte außerhalb des Projekts.

### Geänderte Anzahl der Websites

Aktualisiere Workflow, Delivery, Ablagestruktur, umgebungsabhängigen Zugriff, Master Spec mit Website-Matrix und Design Contract je Website, Sitemap, Design Direction, Motion-Nachweis, SEO, Tests, Impeccable-Reviews und Quality Gates. Alle gebauten Websites teilen Fakten, Scope, Accessibility und Sicherheit; Unterschiede gehören explizit in die Website-Matrix. Keine Auswahl-, Verwerfungs- oder Produktionskandidaten dokumentieren.

### Geänderte Kopfzeile oder Navigation

Aktualisiere Sitemap, Navigationsbeschriftungen, Kurzformen, Fußbereich, Brotkrumen, Komponentenvertrag und die Prüfung auf Einzeiligkeit, Innenhöhe, Mindestluft und width-/height-basierte Seitenverhältnisse bei 1280, 1440 und 1920 Pixel. Über sechs Hauptpunkte wird nicht das Layout gequetscht, sondern die Informationsarchitektur verdichtet.

### Neue oder geänderte Anti-Slop-Regel

Aktualisiere Anti AI Slop als kanonischen Besitzer, danach Design Direction, Derived Design Patterns, Color System, Core Rules, AGENTS.md, AI Build Prompt und Quality Gates. Prüfe bestehende Projektartefakte nur, wenn der Nutzer das ausdrücklich verlangt.

### Relaunch einer bestehenden Website

Aktualisiere Quelleninventar, Content-Inventar, Betreiberfakten, Maps-/Place-Verweis, offizielle Profile, Speisekarten/Preislisten, Asset Register, Rights Review, prüfpflichtige Impressum-/Privacy-Entwürfe, Dateninventar, Sitemap, Redirects und Tests. Die Umsetzung verwendet alle gewünschten Assets unmittelbar; offene Einträge halten nur tatsächlichen Einsatz, Owner und möglichen späteren Prüftermin fest, niemals einen Ersatz oder Launch-Blocker.

### Neue oder entfernte Seite

Aktualisiere Sitemap, Navigation, interne Links, Metadaten, strukturierte Daten, Tracking-/Consent-Einordnung, Zugriffsregeln, Testfälle und Launch-Checkliste in allen gebauten Websites. Prüfe dabei die Grenze von sechs Hauptnavigationspunkten.

### Neue Komponente oder Interaktion

Aktualisiere Komponentenvertrag, Zustände, Tastaturverhalten, Screenreader-Name, responsive Regeln, Motion-Fallback, Tests und gegebenenfalls das Designsystem.

### Zeitabhängige Quelle wird verwendet

Wird eine externe Quelle für eine Projektentscheidung herangezogen, etwa ein Grenzwert aus WCAG oder Core Web Vitals, eine Rechtsquelle, eine Bibliothek, die Maps-Nutzungsbedingungen oder ein Skill, wird sie in diesem Moment auf Aktualität geprüft und das Prüfdatum in der kanonischen Notiz vermerkt. Die Zuordnung von Auslöser zu Gegenstand steht in [[98-Maintenance/Review Queue#Anlassgebunden geprüft]]. Sicherheits-, Auth- und Billing-Quellen laufen stattdessen über die geplante Routine in [[98-Maintenance/Review Queue#Automatisch geprüft]] und werden nicht zusätzlich von Hand geprüft.

### Owner-Hosting, Dashboard oder neue owner-bearbeitbare Inhalte

Aktualisiere [[60-Operations/Owner Hosting and Dashboard]], [[80-Templates/Owner Hosting Website Contract]], Core Rules, Routing Map, Workflow, Content-Schema, Tenant-Manifest, Project Master Spec, Data Processing Inventory, Rollen/AuthZ, Uploads, Buildprofil, Publish/Rollback, Monitoring, Hostingvertrag/AVV-Prüfung, Rechtstext-Workflow und Quality Gates. Bei jedem Inhaltsupdate `owner_editable`, stabilen Pointer, Typ, Grenzen, Preview-Routen und Veröffentlichungspolicy erneut beantworten. Bei Vertragsänderung Owner-Overlays und offene Entwürfe planen und migrieren. Neue externe Integrationen bleiben deaktiviert, bis Capability, Konto, Anbieter, Datenfluss und Zugangsweg übereinstimmen.

### Developer-Plattform oder Veröffentlichungsstatus

Aktualisiere [[60-Operations/Delivery and Local Start]], Source-Roots, Statusspeicher unter `.runtime/previews/`, AuthZ, noindex, Freigaberouten, Tastaturbedienung und Build-/Smoke-Tests. `Old-Projects` bleibt Archiv; `vorschau` ist Legacy-Quelle im Veröffentlichungsbereich und keine vierte Übersicht.

### Neue externe Abhängigkeit

Aktualisiere Abhängigkeitsinventar, Lizenz, Versionierung, Datenflüsse, CSP-/Netzwerkbedarf, Sicherheitsprüfung, Startskripte und Updateplan.

### Neue Datenerhebung oder Drittanbieter

Aktualisiere Dateninventar, Rechtsgrundlage, Einwilligungslogik, Datenschutzerklärung, Lösch- und Exportprozesse, Auftragsverarbeitung, Security Review und Tests.

### Neue Anmeldung oder Kontenregel

Aktualisiere Authentifizierungsmodell, Verknüpfungsregeln, Abuse-Schutz, Recovery, Sessionverwaltung, Datenschutz, Billing-Abhängigkeiten und End-to-End-Tests.

### Neues Abo oder Preisangebot

Aktualisiere Produktlogik, serverseitige Berechtigungen, Webhooks, Kündigung, Rückerstattung, Datenlöschung, Rechtstexte, E-Mails, Monitoring und Tests.

### Neue visuelle Richtung

Aktualisiere Referenzentscheidung samt Negativreferenzen, getrennten UI-UX-Pro-Max-Nachweis unter `design-system/<website-slug>/MASTER.md`, Design Contract der betroffenen Website, Unterscheidungs- und Vorgängermatrix, Auftakt, Kopf-/Fußbereich, Navigation, Chrome, Komponentenrepertoire, Zweitschrift, Tokens, Motion, Asset Register, Master Spec, Impeccable-Review und echte visuelle QA. Referenzen dürfen direkt eingesetzt oder kreativ adaptiert werden; tatsächlicher Einsatz gehört nach dem Build ins Asset Register beziehungsweise Rights Review. Entferne keine gebaute Website aufgrund einer Auswahl- oder Quellenentscheidung.

### Neuer oder geänderter Benchmark

Aktualisiere zuerst [[20-Design/Interface Benchmarks]] als kanonischen Besitzer, danach den Beleg im [[90-References/Inspiration Catalog]] samt Prüfstatus und Fußnote, anschließend Design Direction, Color System, Typography, Components and UI States, Derived Design Patterns und Quality Gates. Ein Benchmark wird immer mit übernommenen **und** ausdrücklich nicht übernommenen Elementen erfasst. Änderungen an H0 dürfen keine konkrete Formsprache vorschreiben; Stilprofile bleiben wählbar.

### Neues oder geändertes Bildmaterial

Aktualisiere Bildrolle, Bearbeitungsschritte, Serienkonsistenz, `srcset`-Varianten, Alt-Texte, Kontrastprüfung bei Text auf Bild, Performancebudget, Asset Register und Source and Rights Review. Wird ein `ai-placeholder` ersetzt, bleiben Rolle, Seitenverhältnis und Pfad unverändert, damit kein Layout bricht.

### Geänderte Informationsmenge oder Textlänge

Aktualisiere Sektionsliste je Route, Textbudget, mobile Staffelung, Navigation, Sitemap, interne Verweise und Tests. Wird ein Abschnitt gestrichen, prüfe, ob die zugehörige Nutzerfrage an anderer Stelle beantwortet bleibt.

### Neues Designwerkzeug, Skill oder CLI

Aktualisiere Plugins and Skills, kanonischen Tool-Workflow, Berechtigungen und Datenzugriff, Version/Lizenz, Projektablage, Start-/Fehlerpfad, Master Spec, Quality Gates und Review Queue. Automatisch erzeugte Dateien dürfen bestehende Quellen nicht unkontrolliert überschreiben.

### Geänderte Vorschrift oder externer Standard

Prüfe das gesamte betroffene Thema, Quellen und Abrufdatum. Markiere rechtlich unsichere Schlüsse als prüfpflichtig und ändere keine Produktentscheidung nur auf Basis einer Zusammenfassung.

## Abschlussnachweis

Ein Update gilt erst als vollständig, wenn im [[Change Log]] festgehalten ist:

- was geändert wurde,
- welche Auslöser aus dieser Karte galten,
- welche Notizen geprüft wurden,
- welche Tests oder Linkprüfungen liefen,
- welche offenen Punkte in der [[Review Queue]] verblieben.
