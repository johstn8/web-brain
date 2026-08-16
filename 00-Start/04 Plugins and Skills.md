---
type: canonical
status: user-maintained
updated: 2026-08-06
---

# Plugins and Skills

Diese Liste beschreibt verfügbare KI-Fähigkeiten. Ein Eintrag ist keine Erlaubnis, ihn ungeprüft zu verwenden.

## UI UX Pro Max Skill

- Name: UI UX Pro Max
- Typ: lokaler Skill
- Status: installiert und **bei jedem Website-Build ausnahmslos verbindlich**
- Version oder Commit: in der lokalen Metadatei nicht ausgewiesen; vor Upgrade erfassen
- Quelle und Lizenz: lokale Installation unter `~/.agents/skills/ui-ux-pro-max/`; Lizenz noch zu prüfen
- Fähigkeiten: durchsuchbare Empfehlungen zu Produkttyp, Stil, Farbe, Typografie, Landingpages, UX, Motion, Charts und unterstützten Stacks
- Grenzen und Risiken: Empfehlungen sind Kandidaten; sie dürfen Master Spec, echte Nutzeranforderungen, Brand, WCAG, Performance oder Quellprüfung nicht überschreiben
- Datenzugriff: mitgelieferte Suche nutzt lokale Datendateien; projektspezifische Prompts enthalten nur erforderliche Informationen
- In welchen Projekten erlaubt: alle; Pflicht, sobald eine Aufgabe Aussehen, Bedienung, Bewegung oder Interaktion einer UI verändert
- Letzte Prüfung: 2026-08-03
- Review bis: 2027-02-03

### Auslösebedingung

**Jeder Website-Build verwendet UI UX Pro Max, immer.** Es gibt keine Ausnahme für kleine Aufträge, Einzelseiten, Relaunches, Prototypen, Korrekturen an einer bestehenden Website oder Aufträge mit vorgegebenem Design. Bei mehreren Websites im Auftrag wird der Skill je Website getrennt ausgeführt.

Wird eine Website ohne dokumentierten Skill-Nachweis gebaut, ist Gate `G1` in [[70-QA/Quality Gates]] nicht erfüllt und die Website gilt als nicht abgenommen. Ist der Skill technisch nicht ausführbar, wird das als Blocker gemeldet und im Decision Log festgehalten; die fehlende Ausführung wird nicht stillschweigend übergangen.

### Verbindlicher Ablauf

1. Anforderungen, Plattform und tatsächlichen Stack bestimmen.
2. In der Projektwurzel vor der Designentscheidung `--design-system` mit Produkt, Branche, Markenattributen und Dichte/Motion-Ziel ausführen:

```bash
python3 ~/.agents/skills/ui-ux-pro-max/scripts/search.py "<Produkttyp> <Branche> <Markenattribute>" --design-system --persist -p "<Projektname>" --variance <1-10> --motion <1-10> --density <1-10>
```

   Ist Python 3 nicht verfügbar, nichts installieren; Blocker melden und bis zur Klärung nur die Quick Reference des Skills verwenden.
3. Ergebnis im Projekt unter `design-system/MASTER.md` persistieren oder als datierten Nachweis verlinken. Seitenabweichungen liegen unter `design-system/pages/` und überschreiben nur explizit benannte Regeln.
4. **Pflicht-Detailabfragen.** Die eine `--design-system`-Abfrage genügt nicht. Vor der Umsetzung werden mindestens diese Domänen zusätzlich abgefragt und ihr Ergebnis dokumentiert:

   | Domäne | Wofür | Beispielaufruf |
   |---|---|---|
   | `landing` | Aufbau und Dramaturgie der Startseite | `--domain landing --max-results 8` |
   | `style` | Stilrichtungen und ihre Grenzen | `--domain style --max-results 8` |
   | `color` | Farbrollen und Kontrastverhalten | `--domain color --max-results 6` |
   | `typography` | Schriftpaare und Type Ramp | `--domain typography --max-results 6` |
   | `ux` | Bedienmuster für den kritischen Fluss | `--domain ux --max-results 8` |
   | `gsap` | Scroll- und Interaktionsmechaniken | `--domain gsap --max-results 8` |
   | Stackdomäne | reale Umsetzung | `--stack <stack> --max-results 6` |

   Bei mehreren Websites im Auftrag wird `style` und `landing` je Art Direction erneut mit anderen Suchbegriffen abgefragt, damit die Richtungen nicht aus derselben Empfehlung entstehen.
5. Ergebnisse gegeneinander lesen, nicht einzeln übernehmen. Jede übernommene Regel und jede Abweichung wird im Design Contract mit einer Begründung festgehalten. Eine Empfehlung, die dem Anti-Slop-Katalog widerspricht, wird abgelehnt und die Ablehnung dokumentiert.
6. Vorschläge mit [[90-References/Reference Research Workflow]], [[20-Design/Design Direction]], [[20-Design/Anti AI Slop]], [[30-Frontend/Accessibility]] und [[30-Frontend/Performance]] abgleichen.
7. Vor Abgabe UX-Prüfung für Animation, Accessibility, Z-Index und Ladezustände durchführen.

## pen.dev

- Name: pen.dev CLI `pen`
- Typ: headless CLI
- Status: nur für visuelle Designaufgaben vorgesehen; kein Desktop-App- oder MCP-Server-Workflow
- Kanonische Einrichtung, Pfade, Grenzen und Workflow: [[90-References/pen.dev Workflow]]
- Letzte Prüfung: 2026-08-03
- Review bis: 2027-02-03

## Emil Design Engineering

- Name: Emil Design Engineering
- Typ: lokaler Skill
- Status: für Motion- und Interaktionsentscheidungen verbindlich
- Quelle und Lizenz: lokale Installation unter `~/.agents/skills/emil-design-eng/`; Quellen und Lizenz vor einem externen Einsatz prüfen
- Fähigkeiten: Bewegungsentscheidung nach Häufigkeit und Zweck, Timing/Easing, Unterbrechbarkeit, Gesten sowie Performance- und Reduced-Motion-Prüfung
- Grenzen und Risiken: bei der verbindlich hohen Bewegungsdichte Choreografie, Accessibility und Performance gemeinsam planen; konkrete Projektanforderungen gehen vor
- Datenzugriff: keine projektspezifischen Daten erforderlich
- In welchen Projekten erlaubt: alle UI-Projekte mit neuer oder veränderter Motion
- Letzte Prüfung: 2026-08-04
- Review bis: 2027-02-04

## Impeccable

- Name: Impeccable
- Typ: lokaler Skill
- Status: für visuelle UI-Arbeit, Reviews und Verfeinerungen verbindlich
- Version oder Commit: 4.0.4
- Quelle und Lizenz: lokale Installation unter `~/.agents/skills/impeccable/`; Lizenz vor externem Einsatz prüfen
- Fähigkeiten: visuelle Richtung, Hierarchie, responsive und zugängliche UI-Qualität, Zustände und begrenzte Verifikationsschleifen
- Grenzen und Risiken: ersetzt weder Projektbrief, Markenrechte, echte Inhalte noch die Quality Gates; keine unautorisierte Ersetzung von Fakten oder Copy
- Datenzugriff: nur erforderliche lokale Projektartefakte
- In welchen Projekten erlaubt: alle UI-Projekte
- Letzte Prüfung: 2026-08-04
- Review bis: 2027-02-04

### Ergänzung zum verbindlichen Ablauf

- Vor einer neuen visuellen Richtung oder einem umfassenden UI-Refinement Impeccable mit dem passenden Arbeitsmodus nutzen und die Entscheidung im Design Contract festhalten.
- **Nach der Implementierung ist der KI-Detail-Review mit Impeccable Pflicht**, je gebauter Website getrennt. Ablauf, Prüfliste und Nachweispflicht stehen in [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review]]. Ohne diesen Nachweis ist Gate `G1` nicht erfüllt.
- Bei jeder neuen Website und jeder geänderten Motion Emil Design Engineering vor der Implementierung anwenden. Das Motion Inventory dokumentiert die hohe Route-zu-Route-Choreografie, Bewegungszweck, Häufigkeit, Timing/Scroll-Range, Easing, Unterbrechbarkeit und Reduced-Motion-Fallback.

## Vorrang der Brain-Regeln vor Skill-Vorschlägen

Skills liefern Vorschläge, keine Freigaben. Widerspricht ein Skill-Vorschlag einer kanonischen Notiz, gilt die Notiz, und der Konflikt wird im Decision Log des Projekts vermerkt, statt ihn stillschweigend zugunsten des Skills zu entscheiden.

Bekannte, wiederkehrende Konfliktstellen:

- Copy-Vorschläge mit Kurzstatements unter Überschriften, Dreierrastern aus Vorteilen oder Vertrauenszeilen mit Datums- und Quellenangabe. Es gilt [[10-Strategy/Website Copy]].
- Sektionsvorschläge mit Eyebrow- oder Kickerzeile. Es gilt [[20-Design/Anti AI Slop#Kicker und Überschriften]].
- Vorschläge, mehrere Varianten als Auswahlkandidaten zu behandeln. Es gilt [[00-Start/05 Web Product Workflow#Anzahl der Websites]] zusammen mit [[20-Design/Design Direction#Stilabstand bei mehreren Websites]].

## Vorgemerkt

- kickbacks.ai - genauer Zweck, Version und Quelle eintragen

## Eintragsformat

- Name:
- Typ: Plugin, Skill, MCP, CLI oder Dienst
- Version oder Commit:
- Quelle und Lizenz:
- Fähigkeiten:
- Grenzen und Risiken:
- Datenzugriff:
- In welchen Projekten erlaubt:
- Letzte Prüfung:
- Review bis:

Vor Verwendung prüfen: passt die Fähigkeit zum Stack, ist die Lizenz geeignet, verarbeitet sie Projektdaten extern, und erzeugt sie Code, der die Quality Gates erfüllt?
