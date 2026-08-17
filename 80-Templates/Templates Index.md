---
type: index
status: canonical
updated: 2026-08-17
---

# Templates Index

- [[80-Templates/Project Intake]]: kurze Eingabe für wenige gute Prompts
- [[80-Templates/Project Master Spec]]: Single Source of Truth je Projekt
- [[80-Templates/Decision Log Entry]]: dauerhafte Architektur-/Designentscheidung
- [[80-Templates/Source and Rights Review]]: tatsächlicher Asset-/Quelleneinsatz und spätere Owner-Einschätzung ohne Build-Sperre
- [[80-Templates/Asset Register]]: eingesetzte Assets mit Quelle, tatsächlicher Übernahme und nicht blockierendem Owner-Reviewstatus
- [[80-Templates/Data Processing Inventory]]: Datenschutz und Datenflüsse
- [[80-Templates/Owner Hosting Website Contract]]: `tenant.json`, `_hosting`-Feldvertrag und Synchronisierungscheck je zentral gehosteter Website
- [[80-Templates/Launch Checklist]]: projektspezifische Freigabe
- [[80-Templates/AI Build Prompt]]: kompakter Startprompt mit Brain-Routing

Bei einem Website-Auftrag zuerst die Anzahl der Websites nach [[00-Start/05 Web Product Workflow#Anzahl der Websites]] bestimmen und den Ordner nach [[60-Operations/Delivery and Local Start]] anlegen. Master Spec als `PROJECT.md` und die drei Inventarvorlagen unter ihren festgelegten Projektnamen kopieren, `type: project` setzen und aus `PROJECT.md` verlinken. Sobald zentrales Owner-Hosting zum Umfang gehört, zusätzlich [[80-Templates/Owner Hosting Website Contract]] anwenden und `owner-hosting/tenant.json` plus `_hosting`-Vertrag anlegen. Originalvorlagen nicht projektspezifisch verändern.
