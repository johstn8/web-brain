---
type: canonical
status: canonical
updated: 2026-08-03
---

# Observability and Maintenance

## Beobachtbarkeit

- Strukturierte Logs mit Request-/Trace-ID, Severity und Deploy-Version.
- Keine Passwörter, Tokens, vollständigen Zahlungsdaten oder unnötige PII loggen.
- Metriken für Verfügbarkeit, Latenz, Fehler, Queues, Webhooks, Rate Limits, API-Kosten und Core Web Vitals.
- Traces an externen I/O-Grenzen nach Risiko und Datenschutz.
- Alerts brauchen Schwelle, Zeitraum, Owner, Runbook und Eskalation. Keine Alarmflut.

## Health

- Liveness: Prozess lebt.
- Readiness: notwendige Abhängigkeiten erreichbar und Instanz kann Traffic bedienen.
- Deep Health nicht öffentlich mit sensiblen Details.

## Betrieb

- Backup mit Verschlüsselung, Aufbewahrung und regelmäßigem Restore-Test.
- Incident-Prozess: erkennen, eindämmen, kommunizieren, beheben, lernen.
- SLOs für kritische Nutzerflüsse; Wartungsfenster und Statuskommunikation.
- Domain, DNS, TLS, Zertifikate, Mailzustellung, Queues, Speicher und Kostenlimits überwachen.
- Datenschutz-Löschfristen und Consent-/Vendor-Änderungen regelmäßig prüfen.

## Übergabe

Architektur, Dependencies, Konfiguration, Deploy, Rollback, Datenmodell, Jobs, Integrationen, Dashboards, Alerts, Backups, bekannte Risiken und Owner dokumentieren.

