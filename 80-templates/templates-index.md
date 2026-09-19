---
type: index
status: canonical
updated: 2026-08-19
---

# Templates Index

- [[80-templates/project-intake.md]]: kurze Eingabe für wenige gute Prompts
- [[80-templates/project-master-spec.md]]: Single Source of Truth je Projekt
- [[80-templates/decision-log-entry.md]]: dauerhafte Architektur-/Designentscheidung
- [[80-templates/source-and-rights-review.md]]: tatsächlicher Asset-/Quelleneinsatz und spätere Owner-Einschätzung ohne Build-Sperre
- [[80-templates/asset-register.md]]: eingesetzte Assets mit Quelle, tatsächlicher Übernahme und nicht blockierendem Owner-Reviewstatus
- [[80-templates/data-processing-inventory.md]]: Datenschutz und Datenflüsse
- [[80-templates/owner-hosting-website-contract.md]]: `tenant.json`, `_hosting`-Feldvertrag und Synchronisierungscheck je zentral gehosteter Website
- [[80-templates/release-readiness-register.md]]: fortlaufende technische, sichtbare und organisatorische Restliste je Website bis zum Produktionsnachweis
- [[80-templates/launch-checklist.md]]: projektspezifische Freigabe
- [[80-templates/ai-build-prompt.md]]: kompakter Startprompt mit Brain-Routing

Bei einem Website-Auftrag zuerst die Anzahl der Websites nach [[00-start/05-web-product-workflow.md#Anzahl der Websites]] bestimmen und den Ordner nach [[60-operations/delivery-and-local-start.md]] anlegen. Master Spec als `PROJECT.md`, die drei Inventarvorlagen unter ihren festgelegten Projektnamen und je Website ein `release-readiness/<website-slug>.md` kopieren, `type: project` setzen und aus `PROJECT.md` verlinken. Sobald zentrales Owner-Hosting zum Umfang gehört, zusätzlich [[80-templates/owner-hosting-website-contract.md]] anwenden und `owner-hosting/tenant.json` plus `_hosting`-Vertrag anlegen. Originalvorlagen nicht projektspezifisch verändern.
