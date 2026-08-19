# Graph Report - .  (2026-08-19)

## Corpus Check
- 68 files · ~115,402 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 651 nodes · 1430 edges · 46 communities (45 shown, 1 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 178 edges (avg confidence: 0.86)
- Token cost: 620,000 input · 0 output

## Community Hubs (Navigation)
- Design Contract und Referenznutzung
- Motion, Dichte und Bildarbeit
- Skillregister und Update-Ablauf
- Brain-Einstieg und Entscheidungsprotokoll
- Copy-Regeln und Textbudget
- Owner-Dashboard: Zweck und Bereiche
- Farbsystem und Markenauftritt
- Release, Rollback und Buildschnittstelle
- Tokenvertrag und B5-Kalibrierung
- Consent, Tracking und Umgebungen
- Website-Vertrag und Registrierung
- Bilder im Dashboard und Privacy by Design
- Architektur und Codekonsistenz
- Routing Map und Kontextladen
- Interface Benchmarks und Bildrollen
- Deployment-Slots und Legacy-Adapter
- Workspace, Ablage und pen.dev
- Identitaet und Kontenverknuepfung
- Anti-Slop und Negativreferenzen
- Rechtstexte und Datenklassifikation
- Komponenten und Kopfzeile
- Assetrechte und Herkunftsnachweis
- Scroll-Motion und Performance
- Integrationen, Nachrichten und Netzgrenze
- Core Rules
- Interaktion, Rendering und Metadaten
- APIs, Billing und Stripe
- Datenschutz, Inventar und Export
- Web-Produkt-Workflow und Projektanlage
- Relaunch aus Bestandsquellen
- SEO, Structured Data und Auffindbarkeit
- Vorschauzugang und Bedrohungsmodell
- Discovery, Scope und Sitemap
- UI-Zustaende, Sitzung und Autorisierung
- Lokaler Start, Ports und Observability
- Conversion und Kernbotschaft
- Schriftwahl und Assetstatus
- Geheimnisse und Zugriffsschutz
- Developer-Plattform und Katalogschluessel
- Abuse-Schutz und Kostengrenzen
- Stilabstand und Handwerksuntergrenze
- Datenmodell, Audit Log und Verlauf
- Vaultsynchronisation und Graphpflicht
- Dienstetrennung und Sockets
- Textmass und Einfuehrung
- Obsidian-Konfiguration

## God Nodes (most connected - your core abstractions)
1. `Brain Index` - 55 edges
2. `Owner Hosting and Dashboard` - 54 edges
3. `Inspirationskatalog` - 50 edges
4. `Kanonische Zuständigkeit` - 44 edges
5. `Routing Map` - 41 edges
6. `Design Direction` - 36 edges
7. `Interface Benchmarks` - 36 edges
8. `Motion and Interaction` - 34 edges
9. `Website Copy` - 33 edges
10. `Change Log` - 33 edges

## Surprising Connections (you probably didn't know these)
- `Entscheidung 2026-08-19: Erklärzeichen statt Erklärabsätze` --semantically_similar_to--> `Information Density and Mobile Clarity`  [INFERRED] [semantically similar]
  98-Maintenance/Change Log.md → 10-Strategy/Information Density and Mobile Clarity.md
- `Accessibility Build-Checkliste` --semantically_similar_to--> `Selbsterklärend`  [INFERRED] [semantically similar]
  30-Frontend/Accessibility.md → 10-Strategy/Information Density and Mobile Clarity.md
- `Screenshot: Brutalist AI SaaS (SYS.INT)` --conceptually_related_to--> `Color System`  [INFERRED]
  .research/screenshots/brutalist.png → 20-Design/Color System.md
- `Screenshot: COMPUTE` --conceptually_related_to--> `Imagery and AI Editing`  [INFERRED]
  .research/screenshots/compute.png → 20-Design/Imagery and AI Editing.md
- `H0 Handwerksuntergrenze` --semantically_similar_to--> `Zielstandard WCAG 2.2 AA`  [INFERRED] [semantically similar]
  20-Design/Interface Benchmarks.md → 30-Frontend/Accessibility.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Verbindliche Skill-Kette je gebauter Website** — 00_start_04_plugins_and_skills_ui_ux_pro_max, 00_start_04_plugins_and_skills_emil_design_engineering, 00_start_04_plugins_and_skills_animate, 00_start_04_plugins_and_skills_review_animations, 00_start_04_plugins_and_skills_impeccable [EXTRACTED 1.00]
- **Projektanlage mit Pflichtartefakten vor jedem Build** — 00_start_05_web_product_workflow_auftragsschwelle_und_projektanlage, 10_strategy_discovery_and_scope_projektpflicht, 10_strategy_existing_website_rebuild_pflichtartefakte, 00_start_01_core_rules_recht_und_betrieb [INFERRED 0.85]
- **Pflicht zur echten Unterseitenarchitektur** — 00_start_01_core_rules_unterseitenpflicht, 10_strategy_information_architecture_and_sitemap_unterseitenarchitektur, 10_strategy_information_architecture_and_sitemap_zwei_sitemaps, 10_strategy_discovery_and_scope_scope_regeln [EXTRACTED 1.00]
- **Anti-Slop-Regelwerk über Copy, Farbe und Typografie** — 20_design_anti_ai_slop_verbotsliste, 20_design_anti_ai_slop_kicker_und_ueberschriften, 10_strategy_website_copy_statementzeile, 10_strategy_website_copy_dreierfigur, 20_design_color_system_verbrauchte_farbwelten, 20_design_typography_layout_and_spacing_retro_verbot [EXTRACTED 1.00]
- **Pflichtbestandteile des Design Contract** — 20_design_design_direction_direction_brief, 20_design_color_system_tokenvertrag, 20_design_motion_and_interaction_motion_inventory, 20_design_imagery_and_ai_editing_bildrollen, 10_strategy_information_density_and_mobile_clarity_textbudget, 20_design_interface_benchmarks_anwendung [EXTRACTED 1.00]
- **H0-Handwerksuntergrenze als gemeinsamer Nenner** — 20_design_interface_benchmarks_h0_handwerksuntergrenze, 20_design_typography_layout_and_spacing_tiefe_und_rahmen, 20_design_color_system_kontrast_und_bedeutung, 30_frontend_accessibility_build_checkliste, 20_design_motion_and_interaction_reduced_motion [INFERRED 0.85]
- **Konto-Lebenszyklus von Signup bis Löschung mit Abo** — 40_backend_security_authentication_and_accounts_identitaetsmodell, 40_backend_security_authentication_and_accounts_account_linking, 40_backend_security_authentication_and_accounts_session_management, 40_backend_security_data_apis_and_billing_subscription_state_machine, 40_backend_security_data_apis_and_billing_account_loeschung_mit_abo [INFERRED 0.85]
- **Kontrollen des Preview Access Gate** — 40_backend_security_preview_access_gate_nginx_auth_basic, 40_backend_security_preview_access_gate_htpasswd_datei, 40_backend_security_preview_access_gate_x_robots_tag_noindex, 40_backend_security_preview_access_gate_https_hsts_pflicht, 40_backend_security_preview_access_gate_eigene_vorschaudomain, 40_backend_security_preview_access_gate_pruefpunkte [EXTRACTED 1.00]
- **Build-zuerst-Asset-Pipeline mit nachgelagerter Owner-Einschätzung** — 50_legal_assets_copyright_and_licenses_build_zuerst_einschaetzung_danach, 50_legal_assets_copyright_and_licenses_zweistufige_ki_aufgabe, 50_legal_assets_copyright_and_licenses_dokumentation_des_einsatzes, 50_legal_assets_copyright_and_licenses_asset_status, 50_legal_assets_copyright_and_licenses_veroeffentlichungsentscheidung, 50_legal_legal_decision_tree_assets_und_drittanbieter [EXTRACTED 1.00]
- **Veröffentlichungskette des Owner-Hostings** — 60_operations_owner_hosting_and_dashboard_veroeffentlichungsablauf, 60_operations_owner_hosting_and_dashboard_publish_lock_konflikt, 60_operations_owner_hosting_and_dashboard_build_schnittstelle, 60_operations_owner_hosting_and_dashboard_buildprofile, 60_operations_owner_hosting_and_dashboard_atomarer_symlink_rollback [EXTRACTED 1.00]
- **Betrieb eines Deployment-Slots** — 60_operations_owner_hosting_and_dashboard_deployment_slot, 60_operations_delivery_and_local_start_test_slot_johannstein_de, 60_operations_owner_hosting_and_dashboard_staging_domain_schutz, 60_operations_owner_hosting_and_dashboard_atomarer_doppelwechsel, 70_qa_test_matrix_deployment_slot_tests, 70_qa_quality_gates_g8_betrieb [INFERRED 0.95]
- **Datenschutz-Nachweiskette von Inventar bis Gate** — 50_legal_privacy_and_consent_dateninventar_vor_text, 80_templates_data_processing_inventory_verarbeitungsblock, 80_templates_data_processing_inventory_zusatz_owner_hosting, 60_operations_owner_hosting_and_dashboard_datenschutz_avv, 70_qa_quality_gates_g6_legal [INFERRED 0.85]
- **Fünf tragfähige Archetypen und ihre Kombinationsregel** — 90_references_derived_design_patterns_archetyp_produktbeweis, 90_references_derived_design_patterns_archetyp_redaktioneller_index, 90_references_derived_design_patterns_archetyp_immersive_erzaehlung, 90_references_derived_design_patterns_archetyp_brutalistisches_operationssystem, 90_references_derived_design_patterns_archetyp_produktkampagne, 90_references_derived_design_patterns_kombinationsregel [EXTRACTED 1.00]
- **Owner-Hosting-Vertragskette vom Manifest bis zur Synchronisierung** — 80_templates_owner_hosting_website_contract_tenant_json, 80_templates_owner_hosting_website_contract_hosting_editorvertrag, 80_templates_owner_hosting_website_contract_content_loader_integration, 80_templates_owner_hosting_website_contract_builder_checkliste, 80_templates_owner_hosting_website_contract_vertragssynchronisierung [EXTRACTED 1.00]
- **Kette von Referenzrecherche über Muster zum Design Contract und zur Freigabe** — 90_references_reference_research_workflow_entscheidungsmatrix, 90_references_inspiration_catalog_auswahlregel_fuer_projekte, 90_references_derived_design_patterns_anwendung_im_projekt, 80_templates_project_master_spec_design_contract_je_website, 80_templates_launch_checklist_pflichtgates [INFERRED 0.85]
- **Negativreferenzen der generischen KI-Anmutung** — _research_screenshots_brutalist, _research_screenshots_compute, _research_screenshots_dataflow, 98_maintenance_change_log_negativreferenzen_erhalten, 20_design_anti_ai_slop [EXTRACTED 1.00]
- **Wartungskreislauf: Update-Prozess, Impact Map, Change Log, Review Queue** — agents_atomarer_update_prozess, 98_maintenance_coverage_and_impact_map, 98_maintenance_change_log, 98_maintenance_review_queue, 00_start_03_update_protocol [EXTRACTED 1.00]
- **Owner-Hosting-Entscheidungen August 2026** — 98_maintenance_change_log_deployment_slots, 98_maintenance_change_log_eine_angabe_ist_ein_feld, 98_maintenance_change_log_bild_ist_eine_datei_an_einer_stelle, 98_maintenance_change_log_zeitpunkt_gehoert_an_die_veroeffentlichung, 98_maintenance_change_log_datensicherung [EXTRACTED 1.00]

## Communities (46 total, 1 thin omitted)

### Community 0 - "Design Contract und Referenznutzung"
Cohesion: 0.05
Nodes (69): Referenznutzung, Abstand zu Vorgängerfassungen, Copy-Entscheidung, Design Contract je Website, Inspirationsmatrix und Negativreferenzen, Keine projektweiten Global Rules für Art Direction, Motion Inventory je primärer Route, Novelty Budget (+61 more)

### Community 1 - "Motion, Dichte und Bildarbeit"
Cohesion: 0.06
Nodes (48): Motion als tragendes Gestaltungsmittel, Bewusst nicht installierte Skills (apple-design, find-animation-opportunities), Gestaffelte Tiefe, Mobile zuerst dosieren, Reparatur generierter Seiten, Kontrast und Bedeutung, Bestandsbilder überarbeiten, Bildumsetzung im Frontend (+40 more)

### Community 2 - "Skillregister und Update-Ablauf"
Cohesion: 0.06
Nodes (45): UI UX Pro Max bei jedem Website-Build, Update-Ablauf in neun Schritten, Kanonischer Besitzer einer Aussage, Plugins and Skills, animate Skill, Auslösebedingung für UI UX Pro Max, Eintragsformat für Plugins und Skills, Emil Design Engineering Skill (+37 more)

### Community 3 - "Brain-Einstieg und Entscheidungsprotokoll"
Cohesion: 0.06
Nodes (40): Brain Index, Kanonische Bereiche des Vaults, Brain Scope: Entscheidungsrahmen statt Tech-Stack, Verbindliche Reihenfolge in zehn Schritten, Vertikale Implementierung eines kritischen Nutzerflusses, Decision Log Entry, Alternativen, Trade-offs und Rollback-Plan, Review-Auslöser und Nachweispflicht (+32 more)

### Community 4 - "Copy-Regeln und Textbudget"
Cohesion: 0.15
Nodes (22): Core Rules: Copy, Copy-Regeln für Kernbotschaft und Aktionen, Information Density and Mobile Clarity, Eine Frage pro Abschnitt, Sektionsbudget je Route, Textbudget, Website Copy, Die Dreierfigur (+14 more)

### Community 5 - "Owner-Dashboard: Zweck und Bereiche"
Cohesion: 0.16
Nodes (22): Reihenfolge für den Bau des zentralen Produkts, Dashboard-Bereich Inhalte bearbeiten, Welche Inhalte der Owner bearbeiten darf, Owner Hosting and Dashboard, Stabiler Seitenrahmen mit scrollbar-gutter, Rechtstexte, Verantwortung und Haftungszuordnung, Statische Auslieferung ohne Laufzeitabhängigkeit, Topologie von Registrar, nginx, Dashboard und Worker (+14 more)

### Community 6 - "Farbsystem und Markenauftritt"
Cohesion: 0.13
Nodes (20): Core Rules: Design, Logo gezielt suchen und einsetzen, Kicker und Überschriften, Color System, Ablauf der Farbdefinition, Coolors, Farbverteilung in Produkt-UI, Farbharmonien (+12 more)

### Community 7 - "Release, Rollback und Buildschnittstelle"
Cohesion: 0.12
Nodes (18): Assets sind unveränderlich, Atomarer current-Symlink und vollständiger Rollback, Build-Schnittstelle OWNER_HOSTING_CONTENT_FILE, Website oder Vertrag später aktualisieren, Registrierte Buildprofile, Automatische Dashboard-Generierung aus dem Vertrag, Datensicherung und Restore-Prüflauf, Eine einzige Wahrheit: Projekt-Basis plus Owner-Overlay (+10 more)

### Community 8 - "Tokenvertrag und B5-Kalibrierung"
Cohesion: 0.15
Nodes (17): Erkennungsfragen, accent-subtle Rolle, border-hover Rolle, Tokenvertrag, Direction Brief, B5 Flächenlogik (drei nahe Helligkeitsstufen), B5 Kartenstil, B5 Modern Neutral Craft Web (+9 more)

### Community 9 - "Consent, Tracking und Umgebungen"
Cohesion: 0.13
Nodes (16): BfDI: Cookies und Tracking-Technologien, Consent-Entscheidung, Consent UI, Fonts und Embeds, TDDDG § 25, Environments-Trennung, Dependency-Auswahlkriterien, Dependencies and Environments (+8 more)

### Community 10 - "Website-Vertrag und Registrierung"
Cohesion: 0.20
Nodes (16): Owner Hosting Website Contract, Builder-Checkliste vor Registrierung, Capabilities als fachliche Absicht, Content-Loader und OWNER_HOSTING_CONTENT_FILE, _hosting Editorvertrag in der Inhaltsdatei, Legacy-Bridge-Vertrag als Ausnahme, Regeln für das Manifest, Pflichtattribute je Block (+8 more)

### Community 11 - "Bilder im Dashboard und Privacy by Design"
Cohesion: 0.13
Nodes (15): DSGVO Art. 25 und 32, Privacy by Design, Dashboard-Bereich Bilder, Ein Bild ist eine Datei an einer Stelle, kein Wert in der Inhaltsdatei, Bildumwandler als Betriebsvoraussetzung (libwebp), Zustände, die auseinanderlaufen können, Eine Angabe ist ein Feld, Feldtyp image (+7 more)

### Community 12 - "Architektur und Codekonsistenz"
Cohesion: 0.15
Nodes (14): Abhängigkeitsentscheidung, Abstraktionsregel (zwei reale Verwendungen), Architecture and Code Consistency, Architekturentscheidung, Codequalität, Einheitlichkeit, Empfohlene Schichten, Primäre Styling-Strategie (+6 more)

### Community 13 - "Routing Map und Kontextladen"
Cohesion: 0.21
Nodes (13): Schnellstart für KI, Routing Map, Aufgabenrouting: Pflichtkontext und Abschlussartefakt, Selektives Kontextladen, Update Protocol, Definition vollständig, Pflicht-Propagation, prototype Skill (+5 more)

### Community 14 - "Interface Benchmarks und Bildrollen"
Cohesion: 0.24
Nodes (13): Imagery and AI Editing, Bildrollen, Freistellen und Objektserien, Interface Benchmarks, Benchmark-Anwendung im Design Contract, B2 Rounded Selection Configurator, B3 Full-Bleed Leitbild-Landing, Interaktives Kernmodul (+5 more)

### Community 15 - "Deployment-Slots und Legacy-Adapter"
Cohesion: 0.19
Nodes (13): Release-Vorgehen, Betrieb: Backup, Incident, SLOs, Atomarer Wechsel von Release und Dashboard-Tenant, Dashboard ohne Vertrag: schreibgeschützter Modus, Deployment-Slot, JSON-Pointer-Allowlist und serverseitige Validierung, Legacy-Adapter für unveränderliche Altprojekte, Mindestnachweise vor Produktivbetrieb (+5 more)

### Community 16 - "Workspace, Ablage und pen.dev"
Cohesion: 0.20
Nodes (12): design-system/<website-slug>/MASTER.md Persistenz, pen.dev CLI, Ablage und Zugriff je Website-Anzahl, Anlage- und Schreibregeln, Delivery and Local Start, Projektordner projekte/<Projektname>, Workspace-Struktur, pen.dev Workflow (+4 more)

### Community 17 - "Identitaet und Kontenverknuepfung"
Cohesion: 0.20
Nodes (12): Account Linking, Authentication and Accounts, Authenticatoren, Clerk: OAuth account linking, Clerk: User enumeration protection, Enumeration-Schutz, Identitätsmodell, MFA (+4 more)

### Community 18 - "Anti-Slop und Negativreferenzen"
Cohesion: 0.25
Nodes (11): Vorrang der Brain-Regeln vor Skill-Vorschlägen, Anti AI Slop, Aftermark AI: Vibe Coded Website Report, Entscheidung 2026-08-08: Handwerksebene B5 mit Tokenvertrag und Bewegungswerten, Entscheidung 2026-08-06: Zwölf Beispielseiten entfernt, vier Negativreferenzen erhalten, Screenshot: Brutalist AI SaaS (SYS.INT), Terminal- und Rasterpastiche als KI-Slop-Muster, Screenshot: COMPUTE (+3 more)

### Community 19 - "Rechtstexte und Datenklassifikation"
Cohesion: 0.20
Nodes (11): Bestehendes Impressum und Datenschutz, Stand- und Datumsangaben in der Copy, Datenklassifikation, Row Level Security (RLS), Betreiber und Markt, Cookies und Endgerätzugriff, Datenschutz und Tracking, DDG § 5 (+3 more)

### Community 20 - "Komponenten und Kopfzeile"
Cohesion: 0.20
Nodes (11): Selbsterklärend, Hakenliste für konkrete Leistungen, B4 Data Product Depth, Components and UI States, Design Contract, Kartenentscheidung, Kopfzeile und Hauptnavigation, Option B5-Karte (+3 more)

### Community 21 - "Assetrechte und Herkunftsnachweis"
Cohesion: 0.24
Nodes (11): Medien und mehrere Websites, ASSET-REGISTER.md, Asset-Status, Assets Copyright and Licenses, Build zuerst, Einschätzung danach, Dokumentation des tatsächlichen Einsatzes, SOURCE-RIGHTS-REVIEW.md, Veröffentlichungsentscheidung beim Owner (+3 more)

### Community 22 - "Scroll-Motion und Performance"
Cohesion: 0.22
Nodes (11): CSS Scroll- und View-Timelines, GSAP ScrollTrigger, Motion useScroll, Technische Umsetzung von Motion, Core Web Vitals Nutzerziele, Media- und Font-Optimierung, Performance-Messung, Performance (+3 more)

### Community 23 - "Integrationen, Nachrichten und Netzgrenze"
Cohesion: 0.20
Nodes (11): tenant.json capabilities, Datenschutz und Auftragsverarbeitung nach Art. 28 DSGVO, Dienstkonto und Schlüsseldatei statt API-Schlüssel, Drei Integrationszustände: aus, hinterlegt, aktiv, Formular vor Versandweg, Nachrichten und Builder-Kontakt, Netzwerkisolierung des Hostingdienstes, Offene Produktentscheidungen (+3 more)

### Community 24 - "Core Rules"
Cohesion: 0.20
Nodes (10): Core Rules, Build vor Rechtsprüfung: Assets werden unmittelbar verwendet, Core Rules: Engineering, Core Rules: Produkt, Core Rules: Recht und Betrieb, Statische Website plus zentrales Owner-Dashboard, Unterseitenpflicht statt One-Pager, Quellen- und Owner-Einschätzung nach dem Build (+2 more)

### Community 25 - "Interaktion, Rendering und Metadaten"
Cohesion: 0.20
Nodes (10): Interaktionsregeln, Modal-Fokusmanagement, Motion Inventory, W3C WAI-ARIA Authoring Practices, Motion-Performance, Rendering und Hydration, Google Search Central: Meta descriptions, Technische SEO-Basis (+2 more)

### Community 26 - "APIs, Billing und Stripe"
Cohesion: 0.29
Nodes (10): Account-Löschung mit bezahltem Abo, API-Vertrag, Billing-Tests, Data APIs and Billing, Stripe cancel subscriptions, Stripe idempotent requests, Stripe subscription webhooks, Subscription State Machine (+2 more)

### Community 27 - "Datenschutz, Inventar und Export"
Cohesion: 0.27
Nodes (10): Dateninventar vor Text, Datenschutzhinweise, Privacy and Consent, Relaunch einer vorhandenen Website (Datenschutz), Eigene Inhalte mitnehmen: Selbstbedienungsexport, G6 Legal, Abgleich gegen Code, Tags, Logs und Anbieter, Data Processing Inventory (+2 more)

### Community 28 - "Web-Produkt-Workflow und Projektanlage"
Cohesion: 0.28
Nodes (9): Web Product Workflow, Auftragsschwelle und Projektanlage, Gemeinsame Fakten außerhalb der Websites unter content/, Herkunft und Anpassung des Ablaufs, Mehrere Websites und Parallelität, Projektpflicht vor Discovery, Pflichtartefakte des Rebuilds, site/ versus versions/ (+1 more)

### Community 29 - "Relaunch aus Bestandsquellen"
Cohesion: 0.25
Nodes (9): Quellenbasierter Bestand bei Relaunches, Existing Website Rebuild, Bestandsaufnahme der Altwebsite, Google Maps und Unternehmensdaten, Kein Scraping von Maps-Inhalten, Quellenreihenfolge, Speisekarten, Preislisten und Dokumente, Trigger und Ziel der Quellenwiederherstellung (+1 more)

### Community 30 - "SEO, Structured Data und Auffindbarkeit"
Cohesion: 0.25
Nodes (9): AI-Discoverability, Google Search Central: Search appearance and structured data, Internationalisierung, MDN: Web application manifest, SEO and Discoverability, Social und Marke, Structured Data, SEO-Verpflichtung je gebauter Website (+1 more)

### Community 31 - "Vorschauzugang und Bedrohungsmodell"
Cohesion: 0.28
Nodes (9): Vorschau-Ablagestruktur, Eigene Vorschau-Domain, Preview Access Gate, Gate-Prüfpunkte, Schutzziel und Abgrenzung, Bedrohungsmodell, OWASP Cheat Sheet Series, Security Baseline (+1 more)

### Community 32 - "Discovery, Scope und Sitemap"
Cohesion: 0.32
Nodes (8): Discovery and Scope, Projekttyp klassifizieren, Scope-Regeln (Must, Should, Could, Won't now), Information Architecture and Sitemap, Fehler-, Leer- und Redirect-Zustände einplanen, Sechs-Punkte-Grenze der Hauptnavigation, Seitenvertrag je Route, Sitemap-Zeile

### Community 33 - "UI-Zustaende, Sitzung und Autorisierung"
Cohesion: 0.25
Nodes (8): Komponentenvertrag, Verbotene dekorative Effekte, UI-Zustände, Zustände abgegrenzter Inhaltsflächen, Session Management, Autorisierung mit Default Deny, Barrierefreiheit (Rechtspfad), BFSG §§ 1 und 3

### Community 34 - "Lokaler Start, Ports und Observability"
Cohesion: 0.25
Nodes (8): Ein-Klick-Start, Festes Portschema 4310/4320/4330, Serverausnahme 217.154.218.30, start-local Skripte je Betriebssystem, Beobachtbarkeit: Logs, Metriken, Traces, Alerts, Liveness, Readiness und Deep Health, Observability and Maintenance, Dashboard-Bereich Übersicht

### Community 35 - "Conversion und Kernbotschaft"
Cohesion: 0.33
Nodes (7): Core Rules: Marke und Anti-Slop, Content and Conversion, Beweis-Hierarchie, Conversion ohne Dark Patterns, Kernbotschaft-Formel und Hero-Inhalt, Messplan, Interpunktion in Website-Copy

### Community 36 - "Schriftwahl und Assetstatus"
Cohesion: 0.29
Nodes (7): Schriftwahl, ai-placeholder, Asset Register, Erlaubte Asset-Status, 0 Project Contract, pen.dev CLI-Schleife, Jitter

### Community 37 - "Geheimnisse und Zugriffsschutz"
Cohesion: 0.29
Nodes (7): htpasswd-Datei, nginx auth_basic auf Serverebene, Nicht akzeptable Praktiken, OWASP Session Management Cheat Sheet, Secrets Management, Stripe: Best practices for secret API keys, Token-Speicherung (HttpOnly Cookie oder BFF)

### Community 38 - "Developer-Plattform und Katalogschluessel"
Cohesion: 0.33
Nodes (7): Developer-Plattform johannstein.com/dev, Drei Übersichten: Archiv, Aktuelle Projekte, Zur Veröffentlichung vorgesehen, Stabiler Katalogschlüssel group/project/variant, Keine Hosting-Subdomain für Unterseiten-Vorschauen, Test-Slot johannstein.de, Veröffentlichungsstatus als Metadatenstatus, Kritische Nutzerflüsse

### Community 39 - "Abuse-Schutz und Kostengrenzen"
Cohesion: 0.33
Nodes (6): Abuse-Schutz, Clerk: Bot protection, Clerk: Restrictions and disposable emails, Kostenwirksame APIs, Stripe API keys, Rate Limits und Kosten

### Community 40 - "Stilabstand und Handwerksuntergrenze"
Cohesion: 0.40
Nodes (5): Abstand zu Vorgängerfassungen, Stilabstand bei mehreren Websites, Unterscheidungsmatrix, H0 Handwerksuntergrenze, Tiefe und Rahmen

### Community 41 - "Datenmodell, Audit Log und Verlauf"
Cohesion: 0.40
Nodes (5): Unveränderliches Audit Log, Auskunft nach der Veröffentlichung, Dashboard-Bereich Verlauf und Rückgängig, Zentrales Datenmodell mit tenant_id, Umsetzungsabweichung: SQLite statt PostgreSQL

### Community 42 - "Vaultsynchronisation und Graphpflicht"
Cohesion: 0.40
Nodes (5): Graphify-Neubau 2026-08-19 (603 Knoten), Entscheidung 2026-08-07: Web-Brain als Git-Repository, Graphify-Regeln des Vaults, Pflicht zum Graph-Neubau, Synchronisation des Vaults

### Community 43 - "Dienstetrennung und Sockets"
Cohesion: 0.67
Nodes (4): Dienstetrennung owner-hosting-web, -worker und www-data, Umsetzungsabweichung: ein Dienst statt zwei, Unix-Socket und serverseitige Hostauflösung, Zentrale Dashboard-Codebasis unter projekte/owner-hosting

### Community 44 - "Textmass und Einfuehrung"
Cohesion: 0.67
Nodes (3): Erklärzeichen ohne JavaScript mit aria-describedby, Einführung beim ersten Besuch, Wie viel Text eine Oberfläche verträgt

## Knowledge Gaps
- **77 isolated node(s):** `alwaysUpdateLinks`, `Kanonische Bereiche des Vaults`, `Pflicht-Detailabfragen je Domäne`, `Eintragsformat für Plugins und Skills`, `Projekttyp klassifizieren` (+72 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Brain Index` connect `Brain-Einstieg und Entscheidungsprotokoll` to `Design Contract und Referenznutzung`, `Motion, Dichte und Bildarbeit`, `Skillregister und Update-Ablauf`, `Copy-Regeln und Textbudget`, `Owner-Dashboard: Zweck und Bereiche`, `Farbsystem und Markenauftritt`, `Tokenvertrag und B5-Kalibrierung`, `Consent, Tracking und Umgebungen`, `Architektur und Codekonsistenz`, `Routing Map und Kontextladen`, `Interface Benchmarks und Bildrollen`, `Workspace, Ablage und pen.dev`, `Identitaet und Kontenverknuepfung`, `Anti-Slop und Negativreferenzen`, `Rechtstexte und Datenklassifikation`, `Komponenten und Kopfzeile`, `Assetrechte und Herkunftsnachweis`, `Scroll-Motion und Performance`, `Core Rules`, `APIs, Billing und Stripe`, `Datenschutz, Inventar und Export`, `Web-Produkt-Workflow und Projektanlage`, `Relaunch aus Bestandsquellen`, `SEO, Structured Data und Auffindbarkeit`, `Vorschauzugang und Bedrohungsmodell`, `Discovery, Scope und Sitemap`, `Lokaler Start, Ports und Observability`, `Conversion und Kernbotschaft`?**
  _High betweenness centrality (0.270) - this node is a cross-community bridge._
- **Why does `Owner Hosting and Dashboard` connect `Owner-Dashboard: Zweck und Bereiche` to `Lokaler Start, Ports und Observability`, `Brain-Einstieg und Entscheidungsprotokoll`, `Release, Rollback und Buildschnittstelle`, `Consent, Tracking und Umgebungen`, `Datenmodell, Audit Log und Verlauf`, `Bilder im Dashboard und Privacy by Design`, `Textmass und Einfuehrung`, `Routing Map und Kontextladen`, `Dienstetrennung und Sockets`, `Deployment-Slots und Legacy-Adapter`, `Workspace, Ablage und pen.dev`, `Identitaet und Kontenverknuepfung`, `Website-Vertrag und Registrierung`, `Interface Benchmarks und Bildrollen`, `Integrationen, Nachrichten und Netzgrenze`, `Core Rules`, `Datenschutz, Inventar und Export`?**
  _High betweenness centrality (0.226) - this node is a cross-community bridge._
- **Why does `Kanonische Zuständigkeit` connect `Core Rules` to `Design Contract und Referenznutzung`, `Motion, Dichte und Bildarbeit`, `Skillregister und Update-Ablauf`, `Brain-Einstieg und Entscheidungsprotokoll`, `Copy-Regeln und Textbudget`, `Owner-Dashboard: Zweck und Bereiche`, `Farbsystem und Markenauftritt`, `Tokenvertrag und B5-Kalibrierung`, `Consent, Tracking und Umgebungen`, `Architektur und Codekonsistenz`, `Routing Map und Kontextladen`, `Interface Benchmarks und Bildrollen`, `Workspace, Ablage und pen.dev`, `Identitaet und Kontenverknuepfung`, `Anti-Slop und Negativreferenzen`, `Rechtstexte und Datenklassifikation`, `Komponenten und Kopfzeile`, `Assetrechte und Herkunftsnachweis`, `Scroll-Motion und Performance`, `APIs, Billing und Stripe`, `Datenschutz, Inventar und Export`, `Web-Produkt-Workflow und Projektanlage`, `Relaunch aus Bestandsquellen`, `SEO, Structured Data und Auffindbarkeit`, `Vorschauzugang und Bedrohungsmodell`, `Discovery, Scope und Sitemap`, `Lokaler Start, Ports und Observability`, `Conversion und Kernbotschaft`, `Vaultsynchronisation und Graphpflicht`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Inspirationskatalog` (e.g. with `MotionSites AI` and `Screenshot: Brutalist AI SaaS (SYS.INT)`) actually correct?**
  _`Inspirationskatalog` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `alwaysUpdateLinks`, `Kanonische Bereiche des Vaults`, `Pflicht-Detailabfragen je Domäne` to the rest of the system?**
  _77 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Design Contract und Referenznutzung` be split into smaller, more focused modules?**
  _Cohesion score 0.05328218243819267 - nodes in this community are weakly interconnected._
- **Should `Motion, Dichte und Bildarbeit` be split into smaller, more focused modules?**
  _Cohesion score 0.058673469387755105 - nodes in this community are weakly interconnected._