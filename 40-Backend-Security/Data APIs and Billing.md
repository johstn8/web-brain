---
type: canonical
status: canonical
updated: 2026-08-03
review_by: 2027-02-03
impacts:
  - privacy
  - security
  - operations
  - account-deletion
---

# Data APIs and Billing

## Daten und API

- Datenklassifikation, Owner, Zweck, Rechtsgrundlage, Aufbewahrung und Löschung pro Entität.
- Mandantenzugehörigkeit in jeder relevanten Zeile; RLS/AuthZ über unveränderliche interne IDs.
- API-Vertrag mit Schema, Versionierung, Pagination, Limits, Fehlercodes und Idempotenz.
- Timeouts, begrenzte Retries mit Backoff/Jitter, Circuit Breaker und Dead-Letter/Recovery für Jobs.
- Webhooks: Signatur und Timestamp prüfen, Event-ID deduplizieren, schnell bestätigen, asynchron verarbeiten, Reihenfolge nicht voraussetzen.
- Exporte und Löschungen als auditierbare Jobs mit Fortschritt und sicherem Download.

## Kostenwirksame APIs

Pro Nutzer/Tenant und global: Request-, Token-, Laufzeit-, Speicher- und Geldbudget. Harte Obergrenze plus Warnstufen, Forecast, Kill Switch und Fallback. Niemals Secret Key im Browser. Restricted Keys und Rotation bevorzugen.[^keys]

## Subscription State Machine

Mindestens: trialing, active, past_due, unpaid, paused, cancel_at_period_end, canceled. Zugriff nicht nur aus einem Client-Flag ableiten; verifizierte Provider-Events und lokale idempotente Projektion nutzen.

## Account-Löschung mit bezahltem Abo

1. Nutzer re-authentifizieren und Folgen anzeigen.
2. Löschanforderung mit Idempotency Key anlegen; parallele Änderungen sperren.
3. Alle aktiven/pending Abos beim Billing Provider ermitteln.
4. Gemäß bestätigter Nutzerentscheidung sofort oder zum Periodenende kündigen; offene Rechnungen, Guthaben und Refund-Regeln behandeln.
5. Provider-Antwort speichern und per Webhook `subscription.deleted` oder entsprechenden Endstatus bestätigen.[^webhooks]
6. Erst danach nicht aufbewahrungspflichtige Produktdaten löschen/anonymisieren. Falls Kündigung scheitert: Konto nicht endgültig löschen, Job erneut versuchen, Nutzer informieren und Support eskalieren.
7. Billing-/Steuerbelege gemäß Pflicht getrennt und minimal aufbewahren; Login und Produktzugriff entziehen.
8. Abschlussbestätigung ohne sensible Details senden.

Stripe unterstützt Idempotency Keys für sichere Retries und beschreibt Subscription-Ereignisse als asynchronen Integrationskern.[^idempotency][^cancel]

## Tests

Test Clock/Sandbox, doppelte und verspätete Webhooks, Out-of-order Events, Netzwerkfehler nach erfolgreichem Provider-Call, Kündigung während Zahlung, Löschung mit mehreren Abos, Refund, Chargeback und Wiederanmeldung.

[^keys]: [Stripe API keys](https://docs.stripe.com/keys)
[^webhooks]: [Stripe subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks)
[^idempotency]: [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests)
[^cancel]: [Stripe cancel subscriptions](https://docs.stripe.com/billing/subscriptions/cancel)

