---
type: canonical
status: canonical
updated: 2026-08-06
---

# Update Protocol

## Ziel

Kein partielles Update darf widersprüchliche oder veraltete Projektinformationen hinterlassen.

## Ablauf

1. Änderung als Satz formulieren: `Was ändert sich, warum, ab wann?`
2. Kanonischen Besitzer über [[98-Maintenance/Coverage and Impact Map]] finden.
3. Direkte Auswirkungen und transitive Folgen markieren.
4. Kanonische Datei, Projekt-Master-Spec und alle erzeugten Artefakte in einer Änderung aktualisieren.
5. Doppelte Aussagen suchen. Nur die kanonische Aussage behalten.
6. Links, Fußnoten, Status, Datum und Review-Frist prüfen.
7. Betroffene Quality Gates ausführen.
8. [[98-Maintenance/Change Log]] ergänzen.

## Pflicht-Propagation

- Neue oder entfernte Seite: Sitemap, Navigation, Breadcrumbs, interne Links, Metadaten, Analytics, Tests, `sitemap.xml` und jede gebaute Website synchronisieren. Bei mehr als sechs Hauptnavigationspunkten die Navigation nach [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]] verdichten.
- Neues Formular oder Feld: Dateninventar, Rechtsgrundlage, Privacy Copy, Validierung, Rate Limit, Speicherung, Löschung, Tests.
- Neuer Drittanbieter: Dependencies, Datenfluss, Vertrag/AVV, Consent, CSP, Ausfallverhalten, Kostenlimit, Privacy Policy.
- Neues Asset oder Font: Asset Register, Quelle, tatsächlicher Einsatz, Hosting, Performancebudget und gegebenenfalls `SOURCE-RIGHTS-REVIEW.md` nach dem Build aktualisieren. Der Eintrag darf Verwendung, Preview, Deployment oder eine gebaute Website nicht sperren und erzeugt keinen Ersatz.
- Motion-Änderung: Motion Inventory, Implementierung, Reduced-Motion-Variante, Messung und Tests aller betroffenen Routen in jeder Website aktualisieren.
- Geänderte Anzahl der Websites: Ablagestruktur, Ports, Startskripte, Website-Matrix im Master Spec, Motion Inventory, QA-Nachweise und Impeccable-Reviews an die neue Anzahl anpassen. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]].
- Visuelle Änderung an Auftakt, Überschriftenanordnung, Kopfzeile oder Logo-Platzierung: Design Contract, betroffene Komponenten, Screenshots und der Impeccable KI-Detail-Review sind erneut zu führen.
- Neue Rolle oder Berechtigung: Rollenmatrix, Server-AuthZ/RLS, UI, Auditlog, negative Tests.
- Neues Abo-Verhalten: Produktcopy, Billing-State-Machine, Webhooks, Kündigung/Löschung, E-Mails, Rechtstexte, Tests.
- Design-Token-Änderung: Komponenten, Storybook/Preview, Kontrasttests, Screenshots, Dark Mode.

## Definition vollständig

Vollständig bedeutet: keine widersprüchlichen Quellen, keine offenen Seiteneffekte, alle erforderlichen Tests grün und die Änderung im Changelog nachvollziehbar.
