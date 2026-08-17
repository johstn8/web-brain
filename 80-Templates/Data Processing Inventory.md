---
type: template
status: canonical
updated: 2026-08-17
---

# Data Processing Inventory

Ein Block pro Verarbeitung:

- ID und Feature/Route:
- Verantwortlicher und technischer Owner:
- Betroffene Personen und Datenkategorien:
- Quelle und Pflicht/Freiwilligkeit:
- präziser Zweck:
- Rechtsgrundlage und ggf. berechtigtes Interesse:
- Endgerätzugriff/Consent-Kategorie:
- Empfänger, Auftragsverarbeiter, Subprozessoren:
- Verarbeitungsland und Transfermechanismus:
- Aufbewahrungsfrist oder Kriterium:
- Lösch-/Export-/Korrekturpfad:
- automatisierte Entscheidung/Profiling:
- Security Controls, Logs, Backups:
- Privacy-Policy-Abschnitt und UI-Hinweis:
- Status, Freigabe, Review-Datum:

Inventar gegen Netzwerk-Scan, Code, Environment, CSP, Tags, Datenbank, Logs und Anbieter-Dashboard abgleichen.

## Zusatz bei Owner-Hosting

Gilt das Betriebsmodell aus [[60-Operations/Owner Hosting and Dashboard]], werden getrennte Blöcke mindestens für diese Verarbeitungen angelegt:

- Owner-Konto, Passwort-Hash, Einladung, Recovery und Sitzungen
- Audit Log aus Login, Entwurf, Veröffentlichung, Rollback, Rollen- und Wartungsmodusänderung
- owner-bearbeitbare Inhaltsfelder samt verantwortlicher Person und Änderungshistorie
- Bildoriginale, erzeugte Varianten, Alt-Texte und Upload-Prüfprotokolle
- Kontaktformular-Nachrichten der öffentlichen Website
- Builder- und Terminanfragen einschließlich E-Mail-Dienst oder Kalender
- Search-Console-Property, OAuth-Tokens, Suchanfragen, Seiten- und Leistungsdaten
- Build-, Release-, Monitoring-, Zertifikats- und Störungsprotokolle
- Backups und Wiederherstellungsfassungen

Je Block zusätzlich dokumentieren: `tenant_id`, betroffene zentrale Entität, Speicherung in PostgreSQL beziehungsweise unter `/var/lib/owner-hosting/tenants/<tenant_id>/`, Zugriff von `owner-hosting-web`, `owner-hosting-worker` und `www-data`, Mandantentrennungs-Control, Aufbewahrung alter Draft-/Content-/Asset-/Release-Revisionen sowie Export- und Löschwirkung auf Backups.

Übergreifend dokumentieren: Rollenverteilung zwischen Owner und Builder, AVV-Prüfung, Weisungsweg, Unterauftragsverarbeiter, Incident-Kommunikation, Datenexport und Löschung nach Vertragsende. Deaktivierte Integrationen werden als `N/A` mit Begründung erfasst, nicht still ausgelassen. Die Website-Capability in `tenant.json`, die serverseitig aktivierte Integration und der Dateninventarblock müssen denselben Zustand zeigen.
