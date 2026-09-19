---
type: canonical
status: canonical
updated: 2026-08-03
review_by: 2027-02-03
impacts:
  - security
  - licenses
  - local-start
  - deployment
---

# Dependencies and Environments

## Dependency Register

Für Runtime, Server, Datenbank, Buildtool, Library, Dienst und Systempaket:

`Name -> Zweck -> Version/Range -> direkt/transitiv -> Lizenz -> Environment -> Owner -> Datenzugriff -> Kostenlimit -> Update-Kanal -> EOL/Review -> Ersatz/Fallback`

## Auswahl

- Native Plattform oder vorhandene Dependency vor neuer Library.
- Aktivität, Security-Prozess, Bundle-/Runtime-Kosten, SSR-Kompatibilität, Accessibility, Lizenz und Lock-in prüfen.
- Exakte Runtime- und Package-Manager-Version pinnen; Lockfile committen.
- Produktionssystempakete und externe Dienste inklusive Mindestversion dokumentieren.
- Kein `latest` für reproduzierbare Deployments.

## Updates

Automatisierte PRs sind Vorschläge. Changelog, Breaking Changes, Migration, Lizenz, Bundle und Tests prüfen. Security-Update priorisieren. Entfernte Dependency samt Config, Secret, CSP, Consent, Doku und Datenfluss vollständig entfernen.

## Konfiguration

Konfigurationsschema mit Typ, Pflicht, Default, Sensitivität, erlaubten Environments und Rotation. Beim Start validieren und ohne Secret-Wert verständlich fehlschlagen.

