---
type: canonical
status: canonical
updated: 2026-08-03
impacts:
  - dependencies
  - tests
  - local-start
---

# Architecture and Code Consistency

## Architekturentscheidung

Stack nach Anforderungen wählen: Rendering, Interaktivität, Content-Workflow, Teamkenntnis, Hosting, Compliance, Kosten und Lebensdauer. Kein Framework nur wegen Popularität.

## Einheitlichkeit

- Pro Projekt genau eine primäre Styling-Strategie: etwa CSS Modules, scoped CSS oder Utilities. Globales CSS nur für Reset, Tokens und echte Globals.
- Inline-Styles nur für dynamische Werte, die nicht sinnvoll als Klasse oder Variable ausdrückbar sind.
- Komponenten nach Domäne und Verantwortlichkeit organisieren, nicht in einer riesigen `components`-Ablage.
- Server-, Client- und Shared-Code sichtbar trennen.
- Imports, Naming, Error Handling, Datenzugriff und Tests projektweit einheitlich.
- Keine neue Abstraktion vor mindestens zwei realen, stabilen Verwendungen.

## Empfohlene Schichten

- `app/routes`: Routing und Komposition
- `features`: domänenspezifische UI und Logik
- `components/ui`: stabile, präsentationale Primitive
- `lib/server`: Serverintegration, Auth, Datenzugriff
- `lib/shared`: reine Typen und Funktionen
- `styles/tokens`: Design Tokens
- `tests`: Integration und End-to-End nahe am Nutzerfluss

An konkrete Frameworkkonventionen anpassen und in `PROJECT.md` festschreiben.

## Codequalität

- Typecheck, Lint, Format, Unit-, Integration- und E2E-Tests automatisieren.
- Dead Code, Platzhalter, auskommentierten Code und Warnungen vor Launch entfernen.
- Fehlergrenzen und verständliche Fallbacks an I/O-Grenzen.
- Abhängigkeit nur hinzufügen, wenn Nutzen Eigenimplementierung, Bundle, Lizenz und Wartungsrisiko überwiegt.

