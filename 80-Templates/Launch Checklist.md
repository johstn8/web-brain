---
type: template
status: canonical
updated: 2026-08-19
---

# Launch Checklist

- Projekt/Version/Commit:
- Environment/URL:
- Datum/Owner:

## Pflicht

- [ ] alle Gates in [[70-QA/Quality Gates]] mit Nachweis
- [ ] Sitemap, Navigation und alle Unterseiten in jeder gebauten Website abgeglichen
- [ ] Kopfzeileninventar und Responsive-Muster jeder Website mit realen Beschriftungen, großer Systemschrift und Zoom ohne zufälligen Umbruch, Beschnitt oder Überlauf geprüft
- [ ] `release-readiness/<website-slug>.md` je Website gegen Repository, Produktionskandidat und externe Infrastruktur abgeglichen; offene P0/P1 und Owner-Entscheidungen sichtbar
- [ ] Impeccable KI-Detail-Review je gebauter Website vorhanden, Befunde umgesetzt oder begründet
- [ ] Firmenlogo sichtbar eingesetzt oder dokumentiert, dass keines gefunden wurde
- [ ] keine Platzhalter, Fake-Links, Testkonten, Sandbox-Schlüssel, Preview-Banner oder sichtbaren Hinweise auf unfertige Funktionen; Fundstellenregister abgearbeitet
- [ ] Privacy-/Consent-Scan entspricht Inventar
- [ ] `SOURCE-RIGHTS-REVIEW.md` dokumentiert tatsächlichen Asset-/Quelleneinsatz; spätere Owner-Einschätzungen sind als Information ergänzt, ohne Ersatz oder KI-Sperre
- [ ] Google-Maps-Integration, Attribution, Consent/Fallback und offizielle Profilziele geprüft; zeitkritische Drittanbieterhinweise primärquellenbestätigt oder entfernt
- [ ] Quellen-/Asset-Hinweise sowie prüfpflichtige Impressum-/Privacy-/Accessibility-Entwürfe für den Nutzer/Owner sichtbar dokumentiert; keine KI-Entscheidung darüber, was veröffentlicht werden darf
- [ ] Migration, Backup, Restore und Rollback bereit
- [ ] Monitoring, Kosten- und Fehleralerts aktiv
- [ ] kritische Flows nach Deploy als Smoke Test
- [ ] Produktionshost ohne `auth_basic`, Passwort-/IP-Sperre und Wartungsflag; Preview-Schutz bleibt auf der Vorschau aktiv
- [ ] kein blockierender `X-Robots-Tag` oder Robots-Meta auf Produktion; `robots.txt` enthält nicht `Disallow: /`; Sitemap, Canonicals und OG-URLs zeigen auf Produktions-HTTPS
- [ ] Search-Console-Property verifiziert und Sitemap eingereicht; bei API-Nutzung OAuth-/Dienstkonto-Zugriff und echter Query geprüft
- [ ] jedes Formular erreicht den realen Produktions-Endpunkt; eindeutige E-Mail-Testanfrage im echten Ziel angekommen; Fehlerfall, Retry und Alert geprüft
- [ ] DNS, TLS, weitere Webhooks und Drittanbieter-Produktionsmodi geprüft
- [ ] bekannte Restrisiken akzeptiert und Owner benannt

## Entscheidung

- Go/No-Go:
- Freigegeben durch:
- Rollback-Schwelle:
- Beobachtungsfenster:
