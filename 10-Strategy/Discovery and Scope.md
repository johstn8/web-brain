---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - "[[10-Strategy/Information Architecture and Sitemap]]"
  - "[[10-Strategy/Content and Conversion]]"
  - "[[80-Templates/Project Master Spec]]"
---

# Discovery and Scope

## Projektpflicht

Ein Umsetzungsauftrag beginnt mit der Projektanlage nach [[00-Start/05 Web Product Workflow]]. Discovery-Ergebnisse werden in diesem Projekt-`PROJECT.md` gespeichert; eine Unterhaltung allein ist keine Projektdokumentation.

## Reihenfolge vor Design

0. Anzahl der zu bauenden Websites aus dem Auftragstext bestimmen und in `PROJECT.md` mit Quelle festhalten
1. Geschäftsmodell und Betreiber
2. Primäre Zielgruppe, Kontext, Fähigkeiten und Geräte
3. Zu lösendes Problem und Alternative heute
4. Primäre Nutzeraktion und Erfolgskennzahl
5. Angebot, Differenzierung und belastbare Belege
6. Inhalte, Funktionen, Integrationen und Daten
7. Zielmärkte, Sprachen, regulatorische Grenzen
8. Budget, Termin, Team, Betrieb und Risikotoleranz

## Bestandsprojekt

Existiert bereits eine Website, vor Scope und Copy den [[10-Strategy/Existing Website Rebuild]] anwenden. Bestehende Inhalte, Bilder, Designs und Interaktionen sind nutzbare Wiederherstellungs- und Kreativquelle. Aktualität wird getrennt dokumentiert, sie erzeugt keinen Build-Stopp oder visuellen Ersatz.

## Projekttyp klassifizieren

- Marketing-Site: Vertrauen, Erklärung, Lead oder Conversion.
- Content-Site: Auffindbarkeit, redaktioneller Workflow, Taxonomie.
- E-Commerce: Produktfindung, Warenkorb, Checkout, Verbraucherpflichten.
- Web-App/SaaS: Aufgabenfluss, Zustände, Auth, Daten, Abrechnung.
- Portfolio/Experience: Erinnerung und Marke, aber stets nutzbarer Fallback.

## Scope-Regeln

- `Must`, `Should`, `Could`, `Won't now` festlegen.
- `Must`: die im Auftrag verlangte Anzahl vollständiger Websites mit festen Ports und einer echten Unterseitenarchitektur. Ohne Angabe im Auftrag genau eine Website, siehe [[00-Start/05 Web Product Workflow#Anzahl der Websites]]. Eine One-Page-Website oder reine Ankernavigation genügt nicht.
- `Must`: SEO für jede Route und jede gebaute Website vollständig planen und testen.
- `Must`: Hauptnavigation auf höchstens sechs Punkte auslegen, siehe [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]]. Die Sitemap wird von Anfang an so geschnitten, dass diese Grenze ohne Notlösung eingehalten wird.
- `Must`: hohes Motion-Niveau nach [[20-Design/Motion and Interaction]] samt einer eigenen Choreografie je Website planen.
- Jede Funktion braucht Nutzerwert, Owner, Datenbedarf, Missbrauchsfall und Abnahmekriterium.
- Unsichere Hypothesen zuerst mit dem kleinsten realen Test validieren.
- Keine Funktion nur hinzufügen, weil eine Inspiration sie zeigt.
- Harte Nicht-Ziele festhalten. Sie schützen vor schleichendem Scope.

## Messplan

Maximal eine primäre und wenige sekundäre Kennzahlen. Ereignisse nur erfassen, wenn eine Entscheidung daran hängt. Datenschutzfreundliche, aggregierte Messung bevorzugen. Baseline, Zielwert, Zeitraum und Verantwortlichen definieren.
