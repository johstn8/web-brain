---
type: canonical
status: canonical
updated: 2026-08-03
review_by: 2027-02-03
impacts:
  - architecture
  - auth
  - api
  - operations
  - qa
---

# Security Baseline

## Bedrohungsmodell zuerst

Für System, Nutzerrollen, Daten, Geldflüsse und Drittanbieter dokumentieren: Assets, Vertrauensgrenzen, Angreifer, Missbrauchsfälle, Folgen und Controls. OWASP ASVS und Cheat Sheets als Prüfbasis, nicht als Ersatz für projektspezifische Analyse.[^owasp]

## Pflichtkontrollen

- Autorisierung bei jeder Serveraktion und jedem Objektzugriff; Default Deny und Least Privilege.
- RLS bei mandantenfähiger Datenbank, ergänzt durch serverseitige Tests. Service-Role-Schlüssel nie im Client.
- Strikte serverseitige Allowlist-Validierung für Typ, Länge, Format, Bereich und Geschäftsregel. Ausgabe kontextgerecht encoden.
- Parametrisierte Queries; keine String-Konkatenation für SQL, HTML, Shell oder URLs.
- CSRF-Schutz bei Cookie-Sessions; CORS eng; sichere Redirect-Allowlist.
- Security Header: CSP, HSTS, `nosniff`, Referrer Policy, Permissions Policy, Frame-Schutz passend zum Embed-Bedarf.
- Uploads: Typ anhand Inhalt prüfen, Größe/Anzahl limitieren, zufällige Namen, getrennte Domain/Storage, Malware-Scan nach Risiko.
- Secrets in Secret Manager/Environment, nie Repo, Client, Logs oder Fehlermeldungen; Rotation und Least-Privilege-Key.[^stripekeys]
- Dependency- und Secret-Scanning, Lockfile, zeitnahe Security-Updates, SBOM bei erhöhtem Risiko.
- Strukturierte Auditlogs für sicherheitsrelevante Aktionen, ohne Secrets oder unnötige PII.

## Rate Limits und Kosten

Mehrdimensional nach IP, Account, Tenant, Route und Ressource. Unterschiedliche Limits für Login, Signup, Reset, Upload, Suche, E-Mail und kostenpflichtige AI/API. Distributed Store, atomare Zähler, sinnvolle `429`-Antwort, Retry-After und Alert. Zusätzlich harte Tages-/Monatsbudgets, maximale Tokens/Dateigrößen, Timeouts, Concurrency, Circuit Breaker und Kill Switch.

## Nicht akzeptabel

- Session-/Refresh-Token in `localStorage` oder `sessionStorage`; JavaScript und XSS können sie lesen. Bevorzugt `HttpOnly; Secure; SameSite` Cookies oder BFF.[^session]
- Admin- oder Rollencheck nur im Client.
- Vertrauen in versteckte Felder, UI-Zustand oder signierte-in-Behauptung ohne serverseitige Prüfung.
- Unbegrenzte APIs, offene Webhooks, unverifizierte Callback-Signaturen.

## Verifikation

Negative Tests je Rolle und Objekt, Abuse-/Rate-Limit-Tests, SAST/DAST, Dependency Scan, Secret Scan, Header/CSP-Test, Backup-Restore und Incident-Übung. Vor hochriskantem Launch unabhängiger Security Review.

[^owasp]: [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
[^session]: [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
[^stripekeys]: [Stripe: Best practices for secret API keys](https://docs.stripe.com/keys-best-practices)

