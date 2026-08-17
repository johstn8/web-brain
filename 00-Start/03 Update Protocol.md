---
type: canonical
status: canonical
updated: 2026-08-17
---

# Update Protocol

## Ziel

Kein partielles Update darf widersprüchliche oder veraltete Projektinformationen hinterlassen.

## Ablauf

0. Remote-Stand holen. Kein Update auf einem veralteten Arbeitsverzeichnis. Kanonisch in `AGENTS.md`, Abschnitt Synchronisation.
1. Änderung als Satz formulieren: `Was ändert sich, warum, ab wann?`
2. Kanonischen Besitzer über [[98-Maintenance/Coverage and Impact Map]] finden.
3. Direkte Auswirkungen und transitive Folgen markieren.
4. Kanonische Datei, Projekt-Master-Spec und alle erzeugten Artefakte in einer Änderung aktualisieren.
5. Doppelte Aussagen suchen. Nur die kanonische Aussage behalten.
6. Links, Fußnoten, Status, Datum und Review-Frist prüfen.
7. Betroffene Quality Gates ausführen.
8. [[98-Maintenance/Change Log]] ergänzen.
9. Änderung und Change-Log-Eintrag in einem Commit sichern und pushen. Erst danach gilt das Update als abgeschlossen.

## Pflicht-Propagation

- Neue oder entfernte Seite: Sitemap, Navigation, Breadcrumbs, interne Links, Metadaten, Analytics, Tests, `sitemap.xml` und jede gebaute Website synchronisieren. Bei mehr als sechs Hauptnavigationspunkten die Navigation nach [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]] verdichten.
- Neues Formular oder Feld: Dateninventar, Rechtsgrundlage, Privacy Copy, Validierung, Rate Limit, Speicherung, Löschung, Tests.
- Neuer Drittanbieter: Dependencies, Datenfluss, Vertrag/AVV, Consent, CSP, Ausfallverhalten, Kostenlimit, Privacy Policy.
- Neues Asset oder Font: Asset Register, Quelle, tatsächlicher Einsatz, Hosting, Performancebudget und gegebenenfalls `SOURCE-RIGHTS-REVIEW.md` nach dem Build aktualisieren. Der Eintrag darf Verwendung, Preview, Deployment oder eine gebaute Website nicht sperren und erzeugt keinen Ersatz.
- Motion-Änderung: Motion Inventory, Implementierung, Reduced-Motion-Variante, Messung und Tests aller betroffenen Routen in jeder Website aktualisieren.
- Geänderte Anzahl der Websites: Ablagestruktur, Website-Matrix im Master Spec, Design Contracts, UI-UX-Pro-Max-Artefakte, Motion Inventory, QA-Nachweise und Impeccable-Reviews an die neue Anzahl anpassen. Außerhalb des Servers `217.154.218.30` zusätzlich Ports und Startskripte anpassen; auf diesem Server den Zugriff über `johannstein.com/dev` prüfen. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]].
- Visuelle Änderung an Auftakt, Überschriftenanordnung, Kopfzeile oder Logo-Platzierung: Den Design Contract und das UI-UX-Pro-Max-Artefakt der betroffenen Website, betroffene Komponenten, Screenshots und den Impeccable KI-Detail-Review erneut führen.
- Owner-editierbarer Inhaltsblock: stabilen JSON-Pointer, `owner_editable`, Typ, Grenzen, Preview-Routen, Veröffentlichungspolicy, Dashboardformular, Servervalidierung, Inhaltsrevisionen und Datenschutzinventar gemeinsam aktualisieren. Bei bestehendem Hosting den Contract-Plan aus [[80-Templates/Owner Hosting Website Contract]] ausführen; Owner-Werte erhalten, explizit migrieren oder dokumentiert archivieren.
- Neue Rolle oder Berechtigung: Rollenmatrix, Server-AuthZ/RLS, UI, Auditlog, negative Tests.
- Neues Abo-Verhalten: Produktcopy, Billing-State-Machine, Webhooks, Kündigung/Löschung, E-Mails, Rechtstexte, Tests.
- Design-Token-Änderung: Komponenten, Storybook/Preview, Kontrasttests, Screenshots, Dark Mode.

## Definition vollständig

Vollständig bedeutet: keine widersprüchlichen Quellen, keine offenen Seiteneffekte, alle erforderlichen Tests grün und die Änderung im Changelog nachvollziehbar.
