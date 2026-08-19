---
type: template
status: canonical
updated: 2026-08-19
depends_on:
  - "[[60-Operations/Release Readiness Register]]"
---

# Release Readiness Register: `<website-slug>`

- Website/Pfad:
- Preview-URL:
- Produktionsdomain:
- Technischer Owner:
- Veröffentlichungs-Owner:
- Zieltermin:
- Letzter vollständiger Abgleich:
- Status: `not_ready | ready_for_owner_decision | owner_approved | launched`

## Offene und geschlossene Punkte

Eintrag beim Entstehen anlegen. Erledigte Zeilen mit Nachweis behalten. Status: `open | in_progress | ready_for_retest | verified | accepted_open | not_applicable`. Priorität: `P0 release-blocking | P1 owner-decision | P2 follow-up`.

| ID | Priorität | Bereich | Route/Endpoint/System | Istzustand und Fundstelle | Zielzustand/Entfernung | Owner | Status | Nachweis/Datum |
|---|---|---|---|---|---|---|---|---|
| RR-001 | | | | | | | | |

## Sichtbare Unfertig-Aussagen und Attrappen

| Route | exakter Text/Selector | Codequelle | warum unfertig | ersetzen, entfernen oder aktivieren | Retest |
|---|---|---|---|---|---|
| | | | | | |

Geprüfte Suchbegriffe und Muster, jeweils mit semantischer Sichtung: `noch nicht`, `derzeit nicht`, `bald`, `coming soon`, `demo`, `preview`, `staging`, `placeholder`, `test`, `dummy`, `mock`, `TODO`, `FIXME`, `example.`, `href="#"`, deaktivierte Submit-Controls, Testdaten, Sandbox- und Mail-Catcher-Ziele.

## Formulare, Nachrichten und E-Mail

Für jedes Formular eine Zeile.

| Formular/Route | Produktions-Endpunkt | Speicherung | E-Mail-Provider | From/Reply-To/Empfänger | Abuse/Retry/Alert | echter Empfangsnachweis | Fehlerfall | Status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

- [ ] serverseitige Validierung und Rate Limit
- [ ] echte Produktions-Secrets, kein Mock/Mail-Catcher/Sandbox-Ziel
- [ ] SPF, DKIM und vorgesehene DMARC-Policy geprüft
- [ ] Erfolgstext entspricht dem tatsächlich erreichten Zustellzustand
- [ ] eindeutige Testanfrage aus Produktion im echten Betreiberweg angekommen
- [ ] Reply-To, Umlaute, Anhänge, Spam-Einstufung und Zeitstempel geprüft
- [ ] Providerfehler absichtlich getestet; keine verlorene Anfrage; Retry/Alert belegt

## Zugang, Preview-Sperren und Indexierung

| Kontrolle | Preview-Soll | Produktion-Soll | Produktionsnachweis | Status |
|---|---|---|---|---|
| nginx `auth_basic` / Passwort / IP-Allowlist | aktiv nach Preview-Policy | entfernt | | |
| `X-Robots-Tag` | `noindex, nofollow, noarchive` | kein blockierender Header | | |
| Robots-Meta | `noindex` | indexierbare Policy | | |
| `robots.txt` | `Disallow: /` | beabsichtigte Regeln plus Sitemap | | |
| `sitemap.xml` | optional entfernt | vollständige Produktions-URLs | | |
| Canonical/OG/hreflang | Preview nicht kanonisch | öffentliche HTTPS-Domain | | |
| Wartungsmodus/Feature-Flags/Banner | nach Bedarf | entfernt oder fachlich beabsichtigt | | |
| DNS/TLS/Redirects | | endgültige Hosts, keine Kette | | |

- [ ] Startseite, primäre Routen, 404, Asset und PDF auf Status/Header/Meta geprüft
- [ ] Preview bleibt nach Produktionsentsperrung geschützt
- [ ] interne Links und Redirects führen nicht auf Preview-, Test- oder Alt-Domains
- [ ] Sitemap eingereicht und Stichproben zur erneuten Prüfung angestoßen

## Google Search Console und Site Verification

- Property-ID und Art:
- Inhaber-/Zugriffsmodell:
- Google-Cloud-Projekt:
- Auth: `OAuth client | service account`
- Dienstkonto/autorisiertes Konto:
- Scope:
- Secret-Ablage und Rotation:
- getrennter Netzwerkweg:

- [ ] Property verifiziert; DNS-/Dateitoken und verantwortliches Konto dokumentiert
- [ ] Search Console API aktiviert; kein API-Key als Ersatz für OAuth verwendet
- [ ] Konto beziehungsweise Dienstkonto hat Zugriff auf exakt diese Property
- [ ] echter `searchAnalytics.query` erfolgreich; leere/verspätete Daten korrekt dargestellt
- [ ] Sitemap in der richtigen Property sichtbar
- [ ] API-Fehler, Berechtigungsverlust und Tokenrotation alarmiert

## Weitere Produktionsintegrationen

| Integration | Konto/Owner | Produktionsmodus und Secret | Datenfluss/Consent | realer E2E-Test | Alert/Runbook | Status |
|---|---|---|---|---|---|---|
| Analytics | | | | | | |
| Maps | | | | | | |
| Kalender/CRM | | | | | | |
| Webhooks | | | | | | |
| Captcha | | | | | | |
| Zahlung | | | | | | |

## Betrieb und Owner-Entscheidungen

- [ ] Produktions-CSP/CORS/Allowed Origins, Cache und Security Header geprüft
- [ ] Monitoring, Fehler- und Kostenalerts aktiv; Empfänger reagieren nachweislich
- [ ] Backup, Restore und Rollback praktisch getestet
- [ ] 404/500/Offline/Timeout zeigen keine Preview- oder Unfertig-Hinweise
- [ ] Betreiberfakten, Kontaktdaten, Öffnungszeiten und primäre Belege bestätigt
- [ ] Rechtstext-, Consent-, Asset- und Quellenhinweise dem Owner vorgelegt
- [ ] offene `P1`-Punkte mit ausdrücklicher Owner-Entscheidung und Datum versehen

## Veröffentlichungsentscheidung

- Offene `P0`:
- Offene `P1` mit Owner-Entscheidung:
- Verweis auf [[80-Templates/Launch Checklist]]:
- Entscheidung `Go | No-Go`:
- Entscheider/Datum:
- Rollback-Schwelle und Beobachtungsfenster:
