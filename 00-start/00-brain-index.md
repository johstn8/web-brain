---
type: index
status: canonical
updated: 2026-09-19
---

# Brain Index

## Schnellstart für KI

1. Regeln: [[AGENTS.md]]
2. Minimaler Kontext: [[00-start/01-core-rules.md]]
3. Aufgabenrouting: [[00-start/02-routing-map.md]]
4. Verbindlicher Ablauf: [[00-start/05-web-product-workflow.md]]. Zuerst die Bahn wählen: die [[00-start/05-web-product-workflow.md#Bahnwahl: Fast Lane und Full Lane|Fast Lane]] ist der Standard
5. Website-Auftrag: der Skill `web-build` faehrt die Fast Lane, siehe [[00-start/04-plugins-and-skills.md#Web Build]]. Von Hand: zuerst `../projekte/<Projektname>/` samt `PROJECT.md`, Inventaren und eigenem Release-Readiness-Register je Website anlegen, danach die im Auftrag verlangte Anzahl vollständiger Websites mit Unterseiten, passendem Motion-Budget, SEO und umgebungsgerechtem Zugriff bauen. Ohne Angabe im Auftrag genau eine Website, siehe [[00-start/05-web-product-workflow.md#Anzahl der Websites]]
6. Bei jeder UI: Leitbenchmark aus [[20-design/interface-benchmarks.md]] wählen; UI UX Pro Max nutzen, wenn verfügbar, sonst die Ersatzstrecke aus [[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]]
7. Startseite oder Landing Page: [[20-design/landing-page-craft.md]] vor der ersten Zeile UI-Code lesen
8. Sobald UI gebaut wird: [[20-design/visual-iteration-loop.md]] — Auftaktfassungen bauen, dann iterieren am Render
9. Neues Projekt spezifizieren: [[80-templates/project-intake.md]] und [[80-templates/project-master-spec.md]]
10. Abschluss: [[70-qa/quality-gates.md]]

## Kanonische Bereiche

- Strategie: [[10-strategy/discovery-and-scope.md]], [[10-strategy/existing-website-rebuild.md]], [[10-strategy/information-architecture-and-sitemap.md]], [[10-strategy/content-and-conversion.md]], [[10-strategy/website-copy.md]], [[10-strategy/information-density-and-mobile-clarity.md]]
- Design: [[20-design/interface-benchmarks.md]], [[20-design/design-systems-und-artefakte.md]], [[20-design/design-direction.md]], [[20-design/landing-page-craft.md]], [[20-design/visual-iteration-loop.md]], [[20-design/color-system.md]], [[20-design/typography-layout-and-spacing.md]], [[20-design/imagery-and-ai-editing.md]], [[20-design/responsive-design.md]], [[20-design/motion-and-interaction.md]], [[20-design/anti-ai-slop.md]]
- Frontend: [[30-frontend/stack.md]], [[30-frontend/web-kit.md]], [[30-frontend/architecture-and-code-consistency.md]], [[30-frontend/components-and-ui-states.md]], [[30-frontend/accessibility.md]], [[30-frontend/performance.md]], [[30-frontend/seo-and-discoverability.md]]
- Backend und Sicherheit: [[40-backend-security/security-baseline.md]], [[40-backend-security/authentication-and-accounts.md]], [[40-backend-security/data-apis-and-billing.md]]
- Recht: [[50-legal/legal-decision-tree.md]], [[50-legal/privacy-and-consent.md]], [[50-legal/assets-copyright-and-licenses.md]]
- Betrieb: [[60-operations/delivery-and-local-start.md]], [[60-operations/owner-hosting-interface.md]], [[60-operations/release-readiness-register.md]], [[60-operations/dependencies-and-environments.md]], [[60-operations/observability-and-maintenance.md]]
- Qualität: [[70-qa/quality-gates.md]], [[70-qa/test-matrix.md]]
- Vorlagen: [[80-templates/templates-index.md]]
- Inspiration und Quellen: [[90-references/website-reference-pool.md]], [[90-references/reference-research-workflow.md]], [[90-references/inspiration-catalog.md]], [[90-references/apple-fluid-interface.md]], [[90-references/derived-design-patterns.md]], [[90-references/tools-and-libraries.md]], [[90-references/pen-dev-workflow.md]]
- Wartung: [[98-maintenance/coverage-and-impact-map.md]], [[98-maintenance/change-log.md]], [[98-maintenance/review-queue.md]]

## Scope

Das Brain liefert Entscheidungsrahmen und einen festgelegten Stack: Astro, Tailwind gegen die Tokenrollen, statischer Build, eigener Formular-Endpoint, Astro-Asset-Pipeline. Kanonisch in [[30-frontend/stack.md]]; eine Abweichung ist eine begründungspflichtige Ausnahme und wird in `PROJECT.md` dokumentiert. Jedes Projekt erzeugt eine eigene Master-Spezifikation, die beauftragte Anzahl vollständiger Websites, Unterseiten-Sitemaps und Nachweisartefakte. Quellen- und Rechtsinformationen werden nach dem Build für die spätere Owner-Einschätzung dokumentiert und verändern den Build nicht.
