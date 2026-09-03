---
type: index
status: canonical
updated: 2026-09-03
---

# Routing Map

Lade nur die Zeilen, die zur Aufgabe passen.

| Aufgabe | Pflichtkontext | Abschlussartefakt |
|---|---|---|
| Neue Website beauftragt | [[00-Start/05 Web Product Workflow]], [[60-Operations/Delivery and Local Start]], [[60-Operations/Owner Hosting and Dashboard]], [[10-Strategy/Discovery and Scope]], [[20-Design/Motion and Interaction]], [[30-Frontend/SEO and Discoverability]] | Projektordner, owner-bearbeitbare Inhaltsblöcke mit stabilen Pointern, vollständige Websites mit Unterseiten und umgebungsgerechtem Zugriff, PROJECT.md und Pflichtartefakte |
| Bestehende Website komplett neu bauen | [[10-Strategy/Existing Website Rebuild]], [[50-Legal/Assets Copyright and Licenses]], [[50-Legal/Privacy and Consent]] | Quelleninventar, Content-Recovery, verifizierte Profile/Maps-Links, SOURCE-RIGHTS-REVIEW.md ohne Build-Sperre oder Asset-Ersatz |
| Navigation oder neue Seite | [[10-Strategy/Information Architecture and Sitemap]], [[30-Frontend/SEO and Discoverability]] | Sitemap und Navigation synchron |
| Inspirationsrecherche | [[90-References/Reference Research Workflow]], [[90-References/Website Reference Pool]], [[90-References/Inspiration Catalog]] | Referenzmodus nach Auftragszahl: Einzelwebsite als Eigenentwurf, bei mehreren genau eine referenzgeführte Fassung, sofern starke Passung gefunden wird; Entscheidungsmatrix und gegebenenfalls statischer/interaktiver Nachweis |
| Visuelles Konzept | alle Notizen unter `20-Design`, [[00-Start/04 Plugins and Skills]], [[90-References/pen.dev Workflow]] | Design Tokens, Direction, Leitbenchmark, UI UX Pro Max Nachweis und pen.dev-Entscheidung |
| Landing Page gestalten | [[20-Design/Landing Page Craft]], [[20-Design/Interface Benchmarks]], [[20-Design/Design Direction]], [[90-References/Derived Design Patterns]], [[20-Design/Anti AI Slop]], [[10-Strategy/Information Density and Mobile Clarity]] | gewählte Auftaktkomposition mit besetzten sechs Auftaktrollen, Seitenaufbau aus realen Nutzerfragen, zwei bis drei Überschriftenanordnungen, begründete Kopfzeilenrolle, Signaturdetail, lesbarer Display-Nachweis, Übergang zur nächsten Nutzerfrage, Logo-Platzierung, durchlaufene Slop-Signaturen |
| Auftakt oder Überschriftenanordnung überarbeiten | [[20-Design/Landing Page Craft]], [[20-Design/Design Direction#Komposition und Überschriften]], [[20-Design/Typography Layout and Spacing#Typografischer Feinschliff]] | neue Kompositionsentscheidung mit Begründung, geprüfte H1-Lesbarkeit an allen Prüfbreiten, erneuter Impeccable-Review |
| Dashboard, Datenansicht oder Verwaltungsoberfläche | [[20-Design/Interface Benchmarks]], [[30-Frontend/Components and UI States]], [[20-Design/Color System]]; bei Owner-Betrieb zusätzlich [[60-Operations/Owner Hosting and Dashboard]] | Benchmark B1/B4 geprüft, Kennzahlen mit Bezugsgröße, Leerzustände, Rollen- und Veröffentlichungsmodell |
| Bilder beschaffen oder überarbeiten | [[20-Design/Imagery and AI Editing]], [[80-Templates/Asset Register]] | Bildinventar mit Rolle, Bearbeitungsschritten und `ai-placeholder`-Liste |
| Texte und Informationsmenge festlegen | [[10-Strategy/Information Density and Mobile Clarity]], [[10-Strategy/Content and Conversion]], [[10-Strategy/Website Copy]] | Sektions- und Textbudget je Route, Copy-Prüffragen durchlaufen |
| Copy schreiben oder überarbeiten | [[10-Strategy/Website Copy]], [[20-Design/Anti AI Slop]] | Text ohne Meta-Sätze, Statementzeilen und unbegründete Dreierfiguren, mit ganzen Sätzen an den tragenden Stellen |
| Mehrere Websites im selben Auftrag | [[20-Design/Design Direction#Stilabstand bei mehreren Websites]], [[20-Design/Design Direction#Abstand zu Vorgängerfassungen]], [[00-Start/05 Web Product Workflow#Anzahl der Websites]], [[90-References/Reference Research Workflow]] | vor UI-Code ausgefüllte Unterscheidungsmatrix; genau eine referenzgeführte Fassung bei starker Passung, mindestens fünf wirksame Unterschiede ohne Verschlechterung der gemeinsamen Nutzstruktur, Vorgängerübernahme dokumentiert |
| Schriftwahl | [[20-Design/Typography Layout and Spacing]], [[20-Design/Interface Benchmarks]] | Type Ramp, Rollen und Nachweis der Zeitbezugsintensität; starkes Epochenzitat nur bei Nutzerwunsch oder tragendem Markenbezug |
| Kopfzeile und Hauptnavigation | [[30-Frontend/Components and UI States]], [[10-Strategy/Information Architecture and Sitemap]] | begründetes Inventar und Muster, Überlauf-/Reflow-Nachweis an realen Beschriftungen |
| Website fertig, vor Abnahme | [[20-Design/Anti AI Slop]], [[00-Start/04 Plugins and Skills]], [[70-QA/Quality Gates]] | Impeccable KI-Detail-Review je Website mit Befundliste |
| Einzelne Bewegung bauen oder prüfen | [[20-Design/Motion and Interaction]], [[00-Start/04 Plugins and Skills#Animate]], [[00-Start/04 Plugins and Skills#Review Animations]] | Bewegung mit Zweck, Kurve, Dauer und Reduced-Motion-Fallback, vor der Abnahme durch `review-animations` geprüft |
| Geste, Feder, Sheet oder Drag | [[90-References/Apple Fluid Interface]], [[20-Design/Motion and Interaction#Gestengeführte Bewegung]] | unterbrechbare Bewegung mit Geschwindigkeitsübergabe und projizierter Ruhelage |
| Komponente | [[30-Frontend/Components and UI States]], [[30-Frontend/Accessibility]] | Zustandsmatrix und Tests |
| Formular | Accessibility, Security Baseline, Privacy | Feldschema, Servervalidierung, Datenzweck |
| Login oder Signup | [[40-Backend-Security/Authentication and Accounts]] | Auth-Flow und Abuse-Tests |
| Nicht öffentliche Vorschau | [[40-Backend-Security/Preview Access Gate]] | Proxy-Gate, `noindex`, Ablage unter `vorschau/` |
| Datenbank oder API | [[40-Backend-Security/Data APIs and Billing]] | Datenmodell, RLS/AuthZ, Limits |
| Bezahlung oder Abo | Data APIs and Billing, Legal Decision Tree | Lifecycle und Webhook-Tests |
| Tracking oder Embed | [[50-Legal/Privacy and Consent]] | Consent-Kategorie und Dateninventar |
| Hosting oder Owner-Dashboard | [[60-Operations/Owner Hosting and Dashboard]], [[80-Templates/Owner Hosting Website Contract]], [[40-Backend-Security/Authentication and Accounts]], [[50-Legal/Privacy and Consent]] | zentraler Tenant-Plan, `tenant.json`, `_hosting`-Feldvertrag, registriertes Buildprofil, Vorschau/Publish/Rollback, Dateninventar und offene Anbieterentscheidungen |
| Developer-Plattform auf `johannstein.com` | [[60-Operations/Delivery and Local Start]], [[30-Frontend/Accessibility]], [[40-Backend-Security/Preview Access Gate]] | Archiv, aktuelle Projekte und Veröffentlichungsvorhaben; persistenter Status, Tastaturalternative, Login/Freigabe/noindex erhalten |
| Website-Build oder -Update | [[60-Operations/Release Readiness Register]] | eigenes, fortlaufend aktualisiertes `release-readiness/<website-slug>.md` je Website |
| Launch | [[70-QA/Quality Gates]], [[60-Operations/Delivery and Local Start]], [[60-Operations/Release Readiness Register]] | abgeglichenes Release-Readiness-Register je Website und signierte Launch-Checkliste |
| Brain-Update | [[00-Start/03 Update Protocol]], [[98-Maintenance/Coverage and Impact Map]] | atomarer Changelog-Eintrag |
| pen.dev oder `.pen` | [[90-References/pen.dev Workflow]], [[60-Operations/Delivery and Local Start]] | versionierte Designquelle, CLI-Exportprüfung und Decision Log |
