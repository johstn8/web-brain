# Graph Report - .  (2026-08-07)

## Corpus Check
- 63 files · ~86,975 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 334 nodes · 564 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 105 edges (avg confidence: 0.86)
- Token cost: 450,185 input · 0 output

## Community Hubs (Navigation)
- Anti-Slop und Pflichtskills
- Projektvorlagen und Designarchetypen
- Frontend-Umsetzung und Auslieferung
- Brain-Steuerung und Projektstrategie
- Recht, Datenschutz und Barrierefreiheit
- Backend-Sicherheit und Betrieb
- Referenzrecherche und Benchmarks
- Brutalist-Referenz SYS.INT
- DataFlow-Referenz Negativbeispiel
- Performance und Auffindbarkeit
- COMPUTE-Referenz Negativbeispiel
- Obsidian-Konfiguration

## God Nodes (most connected - your core abstractions)
1. `Inspirationskatalog` - 17 edges
2. `Routing Map` - 16 edges
3. `Core Rules` - 14 edges
4. `Anti AI Slop` - 13 edges
5. `Quality Gates` - 12 edges
6. `Legal Decision Tree` - 11 edges
7. `Brutalist Landing Page Reference (SYS.INT)` - 11 edges
8. `Information Density and Mobile Clarity` - 10 edges
9. `Interface Benchmarks` - 10 edges
10. `Abgeleitete Designmuster` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Conversion ohne Dark Patterns` --semantically_similar_to--> `Marke und Anti-Slop Regeln`  [INFERRED] [semantically similar]
  10-Strategy/Content and Conversion.md → 00-Start/01 Core Rules.md
- `Marke und Anti-Slop Regeln` --semantically_similar_to--> `Anti AI Slop`  [INFERRED] [semantically similar]
  00-Start/01 Core Rules.md → 20-Design/Anti AI Slop.md
- `Pflicht-Propagation` --conceptually_related_to--> `Zwei Sitemaps: Planung und sitemap.xml`  [INFERRED]
  00-Start/03 Update Protocol.md → 10-Strategy/Information Architecture and Sitemap.md
- `Beweis-Hierarchie` --semantically_similar_to--> `Qualitaetsschwelle fuer generierte Bilder`  [INFERRED] [semantically similar]
  10-Strategy/Content and Conversion.md → 20-Design/Imagery and AI Editing.md
- `375-Pixel-Viewport als Dosierungsmassstab` --semantically_similar_to--> `Reflow bei 320 CSS-Pixeln`  [INFERRED] [semantically similar]
  10-Strategy/Information Density and Mobile Clarity.md → 20-Design/Responsive Design.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Verbindlicher Website-Build-Ablauf von Auftrag bis Abnahme** — 00_start_05_web_product_workflow_auftragsschwelle_projektanlage, 00_start_05_web_product_workflow_anzahl_der_websites, 10_strategy_discovery_and_scope_discovery_and_scope, 20_design_design_direction_direction_brief, 00_start_04_plugins_and_skills_ausloesebedingung, 20_design_anti_ai_slop_impeccable_ki_detail_review [EXTRACTED 1.00]
- **Anti-Slop-Regelverbund aus Kicker, Farbe, Retro und Bildqualitaet** — 20_design_anti_ai_slop_kicker_verbot, 20_design_color_system_verbrauchte_farbwelten, 20_design_typography_layout_and_spacing_retro_verbot, 20_design_imagery_and_ai_editing_qualitaetsschwelle_generierte_bilder, 10_strategy_information_architecture_and_sitemap_sechs_navigationspunkte [EXTRACTED 1.00]
- **Mobile Dosierung: Budget, Viewport und Motion-Anpassung** — 10_strategy_information_density_and_mobile_clarity_mobile_375px_massstab, 10_strategy_information_density_and_mobile_clarity_textbudget, 10_strategy_information_density_and_mobile_clarity_sektionsbudget, 20_design_responsive_design_viewport_matrix, 20_design_motion_and_interaction_reduced_motion [INFERRED 0.85]
- **Account-Loeschung mit aktivem Abo als Gesamtfluss** — 40_backend_security_data_apis_and_billing_account_loeschung_mit_abo, 40_backend_security_data_apis_and_billing_idempotency_key, 40_backend_security_data_apis_and_billing_webhook_handling, 40_backend_security_data_apis_and_billing_subscription_state_machine, 40_backend_security_authentication_and_accounts_session_management, 50_legal_privacy_and_consent_dateninventar_vor_text [EXTRACTED 1.00]
- **Nachweiskette Quality Gates Test Matrix und Fachnotizen** — 70_qa_quality_gates, 70_qa_test_matrix_nachweispflicht, 70_qa_test_matrix_dimensionen, 70_qa_test_matrix_testpyramide, 80_templates_decision_log_entry_felder [EXTRACTED 1.00]
- **Asset-Dokumentation ohne Build-Sperre** — 50_legal_assets_copyright_and_licenses_build_zuerst, 50_legal_assets_copyright_and_licenses_nicht_blockierende_status, 50_legal_assets_copyright_and_licenses_owner_entscheidet, 80_templates_asset_register_ai_placeholder, 50_legal_legal_decision_tree_build_nicht_stoppen [EXTRACTED 1.00]
- **Fünf tragfähige Archetypen** — 90_references_derived_design_patterns_archetyp_produktbeweis, 90_references_derived_design_patterns_archetyp_redaktioneller_index, 90_references_derived_design_patterns_archetyp_immersive_erzaehlung, 90_references_derived_design_patterns_archetyp_brutalistisches_operationssystem, 90_references_derived_design_patterns_archetyp_produktkampagne, 90_references_derived_design_patterns_kombinationsregel [EXTRACTED 1.00]
- **Vier vom Nutzer bewertete Benchmarks mit Vorrang** — 90_references_inspiration_catalog_data_console_dashboard, 90_references_inspiration_catalog_180_grad_produktbetrachter, 90_references_inspiration_catalog_inizio_solar, 90_references_inspiration_catalog_ats_resume_analyzer_dashboard [EXTRACTED 1.00]
- **Projekt-Pflichtartefakte und Abnahmekette** — 80_templates_project_intake, 80_templates_project_master_spec, 80_templates_source_and_rights_review, 80_templates_launch_checklist, 80_templates_templates_index [EXTRACTED 1.00]
- **Machine-Instrument Visual System (dot matrix, dotted grid, monospace, dither, section slugs)** — _research_screenshots_brutalist_dot_matrix_display_type, _research_screenshots_brutalist_dotted_grid_canvas, _research_screenshots_brutalist_monospace_ui_system, _research_screenshots_brutalist_dithered_imagery, _research_screenshots_brutalist_section_slug_label [INFERRED 0.85]
- **Hero Conversion Flow: headline, interactive pipeline diagram, subcopy, CTA** — _research_screenshots_brutalist_no_kicker_headline, _research_screenshots_brutalist_pipeline_node_diagram, _research_screenshots_brutalist_split_cta_button, _research_screenshots_brutalist_header_nav [INFERRED 0.75]
- **Dark Hero Composition Pattern (eyebrow, headline, key visual, metric strip)** — _research_screenshots_compute_mono_eyebrow_rule, _research_screenshots_compute_oversized_grotesk_headline, _research_screenshots_compute_ai_generated_key_visual, _research_screenshots_compute_metric_strip, _research_screenshots_compute_faint_grid_overlay [INFERRED 0.85]
- **Hero-Conversion-Stack: Pille, Headline, CTA-Paar, Social Proof** — _research_screenshots_dataflow_status_pill, _research_screenshots_dataflow_hero_headline_highlight, _research_screenshots_dataflow_dual_cta, _research_screenshots_dataflow_social_proof_row [INFERRED 0.85]
- **Visuelle Sprache: Teal-Palette, geometrische Sans, isometrisches Visual, Wortmarke** — _research_screenshots_dataflow_color_palette, _research_screenshots_dataflow_geometric_sans_type, _research_screenshots_dataflow_isometric_illustration, _research_screenshots_dataflow_brand_mark [INFERRED 0.85]
- **Vertrauenssignale ohne Beleg: Metrik-Karten, Teamzahl, Beta-Status** — _research_screenshots_dataflow_floating_metric_cards, _research_screenshots_dataflow_social_proof_row, _research_screenshots_dataflow_status_pill, _research_screenshots_dataflow_unverified_claims [INFERRED 0.75]

## Communities (12 total, 1 thin omitted)

### Community 0 - "Anti-Slop und Pflichtskills"
Cohesion: 0.06
Nodes (64): Marke und Anti-Slop Regeln, Build zuerst, Rechte-Review danach, Core Rules, Engineering Baseline, Pflicht-Propagation, Ausloesebedingung UI UX Pro Max, Emil Design Engineering Skill, Impeccable Skill (+56 more)

### Community 1 - "Projektvorlagen und Designarchetypen"
Cohesion: 0.05
Nodes (58): Launch Checklist, Go/No-Go-Entscheidung, Post-Deploy Smoke Test kritischer Flows, Project Intake, Anzahl der Websites im Auftrag, Intake-KI-Regel: keine erfundenen Fakten, Project Master Spec, Design Contract (+50 more)

### Community 2 - "Frontend-Umsetzung und Auslieferung"
Cohesion: 0.06
Nodes (48): Accessibility Build-Checkliste, Manuelle Accessibility-Pruefung, Architecture and Code Consistency, Keine Abstraktion vor zwei Verwendungen, Dependency nur bei ueberwiegendem Nutzen, Eine primaere Styling-Strategie pro Projekt, Empfohlene Code-Schichten, Components and UI States (+40 more)

### Community 3 - "Brain-Steuerung und Projektstrategie"
Cohesion: 0.07
Nodes (38): Brain Index, Brain Scope: Entscheidungsrahmen statt Tech-Stack, Routing Map, Selektives Kontextladen, Definition vollstaendig, Update Protocol, Anzahl der Websites, Auftragsschwelle und Projektanlage (+30 more)

### Community 4 - "Recht, Datenschutz und Barrierefreiheit"
Cohesion: 0.10
Nodes (30): Accessibility, BFSG Rechtlicher Kontext Deutschland, WCAG 2.2 AA Zielstandard, Favicon- und Social-Metadaten-Set, API-Vertrag und Resilienz, Assets Copyright and Licenses, Build zuerst Einschaetzung danach, Nicht blockierende Asset-Status (+22 more)

### Community 5 - "Backend-Sicherheit und Betrieb"
Cohesion: 0.12
Nodes (25): Authentication and Accounts, Abuse-Schutz fuer Auth-Endpunkte, Account Linking Flow, User-Enumeration-Schutz, Interne user_id als Identitaet, Session-Rotation und Revocation, Data APIs and Billing, Account-Loeschung mit bezahltem Abo (+17 more)

### Community 6 - "Referenzrecherche und Benchmarks"
Cohesion: 0.14
Nodes (22): Anordnung von Überschriften, Landing Page mit Ausdruck, Inspirationskatalog, 180-Grad-Produktbetrachter (Benchmark), Animated SaaS (Negativreferenz), ATS Resume Analyzer Dashboard (Benchmark), Auswahlregel für Projekte, Claude Code Curriculum (+14 more)

### Community 7 - "Brutalist-Referenz SYS.INT"
Cohesion: 0.26
Nodes (13): Dithered Halftone Imagery (NEURAL_SCAN.DITHER), Dot-Matrix Display Typography, Dotted Grid Background Canvas, Four-Item Header Navigation with Theme Toggle, Machine/Instrument Brutalist Aesthetic, Monospace UI Type System, Kicker-Free Oversized Headline Stack, Single Orange Accent on Off-White Palette (+5 more)

### Community 8 - "DataFlow-Referenz Negativbeispiel"
Cohesion: 0.22
Nodes (13): DataFlow Wortmarke mit Teal-Layer-Icon, Farbsystem: Teal-Akzent auf Off-White, Korallrot und Gelb als Sekundärtöne, Duales CTA-Paar (Primär solide, Sekundär Outline mit Play-Icon), Schwebende Metrik-Karten (2,4M events/sec, 99,99% Uptime), Geometrische Sans-Typografie mit hohem Größenkontrast, Kopfzeile mit fünf Navigationspunkten und Auth-Aktionen, Hero-Headline mit farbig markiertem Schlüsselwort, Isometrische 3D-Infrastruktur-Illustration (+5 more)

### Community 9 - "Performance und Auffindbarkeit"
Cohesion: 0.22
Nodes (11): Performance, Core Web Vitals Schwellen LCP INP CLS, Motion-Dichte ueber Compositor statt Weglassen optimieren, Performance-Projektbudgets, RUM- und Felddatenmessung, SEO and Discoverability, AI-Discoverability, Structured Data nur wahrheitsgemaess (+3 more)

### Community 10 - "COMPUTE-Referenz Negativbeispiel"
Cohesion: 0.31
Nodes (10): AI-Generated Blossom Tree Key Visual, COMPUTE Landing Page Hero (Reference Screenshot), Dark Atmospheric Full-Bleed Hero Imagery, Faint Grid Overlay on Dark Canvas, Bottom Metric Strip (3500+, 99.7%, <50ms), Monospace Eyebrow Line with Leading Rule, Oversized Light-Weight Grotesk Headline, Six-Item Header Navigation with CTA (+2 more)

## Ambiguous Edges - Review These
- `Messplan` → `Information Density and Mobile Clarity`  [AMBIGUOUS]
  10-Strategy/Discovery and Scope.md · relation: conceptually_related_to
- `Isometrische 3D-Infrastruktur-Illustration` → `Unbelegte Leistungs- und Nutzerzahlen als Vertrauensanker`  [AMBIGUOUS]
  .research/screenshots/dataflow.png · relation: conceptually_related_to

## Knowledge Gaps
- **35 isolated node(s):** `alwaysUpdateLinks`, `Pflicht-Detailabfragen der Skill-Domaenen`, `Kernbotschaft-Formel`, `Projekttyp-Klassifikation`, `Quellenreihenfolge bei Relaunch` (+30 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Messplan` and `Information Density and Mobile Clarity`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Isometrische 3D-Infrastruktur-Illustration` and `Unbelegte Leistungs- und Nutzerzahlen als Vertrauensanker`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Routing Map` connect `Brain-Steuerung und Projektstrategie` to `Anti-Slop und Pflichtskills`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Why does `Quality Gates` connect `Frontend-Umsetzung und Auslieferung` to `Performance und Auffindbarkeit`, `Recht, Datenschutz und Barrierefreiheit`, `Backend-Sicherheit und Betrieb`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Why does `Inspirationskatalog` connect `Referenzrecherche und Benchmarks` to `Projektvorlagen und Designarchetypen`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Anti AI Slop` (e.g. with `Marke und Anti-Slop Regeln` and `ai-placeholder Status`) actually correct?**
  _`Anti AI Slop` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `alwaysUpdateLinks`, `Pflicht-Detailabfragen der Skill-Domaenen`, `Kernbotschaft-Formel` to the rest of the system?**
  _35 weakly-connected nodes found - possible documentation gaps or missing edges._