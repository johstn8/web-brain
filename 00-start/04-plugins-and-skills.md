---
type: canonical
status: user-maintained
updated: 2026-09-19
---

# Plugins and Skills

Diese Liste beschreibt verfügbare KI-Fähigkeiten. Ein Eintrag ist keine Erlaubnis, ihn ungeprüft zu verwenden.

## UI UX Pro Max Skill

- Name: UI UX Pro Max
- Typ: lokaler Skill
- Status: installiert und **bei jedem Website-Build stark empfohlen**, keine Abnahmebedingung; Ersatzstrecke in [[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]]
- Version oder Commit: in der lokalen Metadatei nicht ausgewiesen; vor Upgrade erfassen
- Quelle und Lizenz: lokale Installation unter `~/.agents/skills/ui-ux-pro-max/`; Lizenz noch zu prüfen
- Fähigkeiten: durchsuchbare Empfehlungen zu Produkttyp, Stil, Farbe, Typografie, Landingpages, UX, Motion, Charts und unterstützten Stacks
- Grenzen und Risiken: Empfehlungen sind Kandidaten; sie dürfen Master Spec, echte Nutzeranforderungen, Brand, WCAG, Performance oder Quellprüfung nicht überschreiben
- Datenzugriff: mitgelieferte Suche nutzt lokale Datendateien; projektspezifische Prompts enthalten nur erforderliche Informationen
- In welchen Projekten erlaubt: alle; Pflicht, sobald eine Aufgabe Aussehen, Bedienung, Bewegung oder Interaktion einer UI verändert
- Letzte Prüfung: 2026-08-03
- Review bis: 2027-02-03

### Auslösebedingung

**Starke Empfehlung, keine Abnahmebedingung.** Wo UI UX Pro Max verfügbar ist, wird er bei jedem Website-Build verwendet, bei mehreren Websites je Website getrennt. Er ist der schnellste Weg zu einer belegten Design-Entscheidung, und wer ihn überspringt, zahlt die Zeit an anderer Stelle nach.

Die Abnahme hängt nicht daran. Gate `G1` in [[70-qa/quality-gates.md]] prüft seit dem 19.09.2026 das Ergebnis — vollständiger Tokenvertrag, vollständige Zustände, Type Ramp, Kontrast in beiden Themes, echte Darstellung — und nicht, welches Werkzeug es erzeugt hat. Der Grund ist betrieblich: Der Skill liegt unter einem lokalen Pfad, ruft ein Python-Skript auf, und seine Lizenzfrage ist nach [[98-maintenance/review-queue.md]] noch offen. Eine Auslieferung, die an drei Installationen auf einem einzelnen Rechner hängt, ist kein Qualitätsmaßstab, sondern ein Ausfallrisiko.

Ist der Skill nicht ausführbar, wird das im Decision Log festgehalten und die Ersatzstrecke gefahren. Das ist ein Vermerk, kein Blocker.

### Ersatzstrecke ohne Skills

Sind UI UX Pro Max, Impeccable oder `review-animations` auf der Maschine nicht verfügbar, wird dieselbe Arbeit ohne sie geleistet und genauso nachgewiesen:

| Statt | Ersatz | Nachweis unter `design-system/<website-slug>/` |
|---|---|---|
| UI UX Pro Max `--design-system` | Design Contract direkt aus [[20-design/design-direction.md]], [[20-design/interface-benchmarks.md]] und dem gewählten Leitbenchmark füllen; Farb-, Typo-, Dichte- und Motion-Entscheidung je einzeln begründen | `DESIGN-CONTRACT.md` mit Datum |
| UI UX Pro Max Detailabfragen | die Prüffragen der jeweiligen kanonischen Notiz durchgehen: Landing Page Craft, Color System, Typography, Components and UI States, Motion and Interaction | Antwortliste je Domäne mit Datum |
| Impeccable KI-Detail-Review | den Befundkatalog aus [[20-design/anti-ai-slop.md#Impeccable KI-Detail-Review]] und die [[20-design/anti-ai-slop.md#Slop-Signaturen]] manuell am ganzseitigen Render durchgehen | Befundliste mit Ort, Beobachtung, Änderung |
| `review-animations` | die zehn Prüfstandards aus [[00-start/04-plugins-and-skills.md#Review Animations]] je eingesetzter Bewegung durchgehen | Motion Inventory mit Prüfspalte |
| `prototype` für das Auftaktfeld | die Auftaktfassungen von Hand bauen; das Kit liefert die Blöcke, verglichen wird trotzdem nebeneinander bei 375 und 1280 Pixel | Screenshots und Wahlbegründung |

Die Ersatzstrecke kostet mehr Zeit und liefert dasselbe Ergebnis. Sie ist kein Grund, einen Prüfpunkt zu streichen.

### Verbindlicher Ablauf

1. Anforderungen, Plattform und tatsächlichen Stack bestimmen.
2. In der Projektwurzel vor der Designentscheidung `--design-system` mit Produkt, Branche, Markenattributen und Dichte/Motion-Ziel ausführen:

```bash
python3 ~/.agents/skills/ui-ux-pro-max/scripts/search.py "<Produkttyp> <Branche> <Markenattribute>" --design-system --persist -p "<Projektname>" --variance <1-10> --motion <1-10> --density <1-10>
```

   Ist Python 3 nicht verfügbar, nichts installieren; Blocker melden und bis zur Klärung nur die Quick Reference des Skills verwenden.
3. Das Ergebnis **je gebauter Website** unter `design-system/<website-slug>/MASTER.md` persistieren oder dort als datierten Nachweis verlinken. Bei einer einzelnen Website ist der Slug `site`, bei mehreren entspricht er `01-<richtung>`, `02-<richtung>` und so fort. Seitenabweichungen liegen innerhalb dieses Website-Ordners unter `pages/`. Es gibt keine projektweite Datei `design-system/MASTER.md` mit globalen Stilregeln, die alle Fassungen gleichzieht.
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
5. Ergebnisse gegeneinander lesen, nicht einzeln übernehmen. Jede übernommene Regel und jede Abweichung wird im Design Contract der betreffenden Website begründet. Bei mehreren Websites werden auch Struktur, Komponentenrepertoire, Kopf-/Fußbereich, Chrome und Zweitschrift je Website getrennt abgefragt und persistiert. Eine Empfehlung, die dem Anti-Slop-Katalog widerspricht, wird abgelehnt und die Ablehnung dokumentiert.
6. Vorschläge mit [[90-references/reference-research-workflow.md]], [[20-design/design-direction.md]], [[20-design/anti-ai-slop.md]], [[30-frontend/accessibility.md]] und [[30-frontend/performance.md]] abgleichen.
7. Vor Abgabe UX-Prüfung für Animation, Accessibility, Z-Index und Ladezustände durchführen.

## pen.dev

- Name: pen.dev CLI `pen`
- Typ: headless CLI
- Status: nur für visuelle Designaufgaben vorgesehen; kein Desktop-App- oder MCP-Server-Workflow
- Kanonische Einrichtung, Pfade, Grenzen und Workflow: [[90-references/pen-dev-workflow.md]]
- Letzte Prüfung: 2026-08-03
- Review bis: 2027-02-03

## Emil Design Engineering

- Name: Emil Design Engineering
- Typ: lokaler Skill
- Status: für Motion- und Interaktionsentscheidungen stark empfohlen; Ersatzstrecke in [[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]]
- Quelle und Lizenz: lokale Installation unter `~/.agents/skills/emil-design-eng/`; Quellen und Lizenz vor einem externen Einsatz prüfen
- Fähigkeiten: Bewegungsentscheidung nach Häufigkeit und Zweck, Timing/Easing, Unterbrechbarkeit, Gesten sowie Performance- und Reduced-Motion-Prüfung
- Grenzen und Risiken: bei der verbindlich hohen Bewegungsdichte Choreografie, Accessibility und Performance gemeinsam planen; konkrete Projektanforderungen gehen vor
- Datenzugriff: keine projektspezifischen Daten erforderlich
- In welchen Projekten erlaubt: alle UI-Projekte mit neuer oder veränderter Motion
- Letzte Prüfung: 2026-08-04
- Review bis: 2027-02-04

## Animate

- Name: animate
- Typ: lokaler Skill aus dem Skillset von Emil Kowalski
- Status: für den Bau einzelner Bewegungen empfohlen, sobald eine neue Animation geschrieben wird
- Quelle und Lizenz: [emilkowalski/skills](https://github.com/emilkowalski/skills), MIT; Installation unter `/srv/Web-Design/shared-agent-skills/animate/`, verlinkt nach `~/.claude/skills/` und `~/.agents/skills/`
- Fähigkeiten: Entscheidungsreihenfolge von der Frage, ob überhaupt animiert wird, über Zweck, Werkzeug, Eigenschaften, Kurve und Dauer bis zu Unterbrechung und Austritt, dazu die Implementierung
- Grenzen und Risiken: er entscheidet je Einzelbewegung und ersetzt die Route-Choreografie aus [[20-design/motion-and-interaction.md]] nicht; er darf keine Bewegung streichen, die das verbindliche Motion-Niveau trägt
- Datenzugriff: nur die betroffenen Projektdateien
- In welchen Projekten erlaubt: alle UI-Projekte
- Letzte Prüfung: 2026-08-16
- Review bis: 2027-02-16

## Review Animations

- Name: review-animations
- Typ: lokaler Skill aus dem Skillset von Emil Kowalski
- Status: vor der Abnahme jeder gebauten Website empfohlen; verbindlich ist die geprüfte Bewegung, nicht der Skill-Lauf
- Auslösung: `disable-model-invocation` ist gesetzt, der Skill startet nie von selbst und wird ausdrücklich aufgerufen
- Quelle und Lizenz: [emilkowalski/skills](https://github.com/emilkowalski/skills), MIT; Installation unter `/srv/Web-Design/shared-agent-skills/review-animations/`, verlinkt nach `~/.claude/skills/` und `~/.agents/skills/`
- Fähigkeiten: zehn Prüfstandards mit Werten für Begründung, Häufigkeit, Easing, Dauer unter 300 ms, Ursprungspunkt, Unterbrechbarkeit, GPU-Eigenschaften, Reduced Motion, asymmetrischen Ein- und Austritt und Kohärenz
- Grenzen und Risiken: prüft nur Bewegung, kein anderer Code; die Standards sind Prüfmaß, nicht Ersatz für den je Website dokumentierten Wertesatz. Die [[20-design/motion-and-interaction.md#Kalibrierte Bewegungsbeispiele|B5-Beispiele]] sind nur bei bewusster Übernahme Prüfmaß; Konflikte kommen in das Decision Log
- Datenzugriff: die Motion-Dateien des Projekts
- In welchen Projekten erlaubt: alle UI-Projekte
- Letzte Prüfung: 2026-08-16
- Review bis: 2027-02-16

## Prototype

- Name: prototype
- Typ: lokaler Skill aus dem Skillset von Emil Kowalski
- Status: **für das Auftaktfeld jeder gebauten Website empfohlen**, darüber hinaus optional für Divergenz in der Entwurfsphase; Auslöser und Umfang in [[20-design/visual-iteration-loop.md#Divergenz vor Konvergenz: das Auftaktfeld]]
- Auslösung: `disable-model-invocation` ist gesetzt, der Skill startet nie von selbst und wird ausdrücklich aufgerufen
- Quelle und Lizenz: [emilkowalski/skills](https://github.com/emilkowalski/skills), MIT; Installation unter `/srv/Web-Design/shared-agent-skills/prototype/`, verlinkt nach `~/.claude/skills/` und `~/.agents/skills/`
- Fähigkeiten: mehrere echte Fassungen eines beschriebenen UI-Teils, jede auf einer benannten Achse verschieden, hinter einem sichtbaren Umschalter zum Durchklicken
- Grenzen und Risiken: **nur für einzelne Bauteile, Auftaktkompositionen und Interaktionsmuster.** Eine gebaute Website ist nach [[00-start/05-web-product-workflow.md#Anzahl der Websites]] nie eine Auswahlvariante, deshalb wird der Skill niemals auf ganze Websites angewandt. Diese Grenze bleibt durch die neue Pflicht unberührt: Das Auftaktfeld vergleicht Kompositionen eines einzelnen Bauteils, keine Websites. Prototypen liegen außerhalb des Produktionscodes und werden nicht ausgeliefert
- Datenzugriff: Projekttokens und die betroffene Komponente
- In welchen Projekten erlaubt: alle UI-Projekte in der Entwurfsphase
- Letzte Prüfung: 2026-08-16
- Review bis: 2027-02-16

## Impeccable

- Name: Impeccable
- Typ: lokaler Skill
- Status: für visuelle UI-Arbeit, Reviews und Verfeinerungen stark empfohlen; Ersatzstrecke in [[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]]
- Version oder Commit: 4.0.4
- Quelle und Lizenz: lokale Installation unter `~/.agents/skills/impeccable/`; Lizenz vor externem Einsatz prüfen
- Fähigkeiten: visuelle Richtung, Hierarchie, responsive und zugängliche UI-Qualität, Zustände und begrenzte Verifikationsschleifen
- Grenzen und Risiken: ersetzt weder Projektbrief, Markenrechte, echte Inhalte noch die Quality Gates; keine unautorisierte Ersetzung von Fakten oder Copy
- Datenzugriff: nur erforderliche lokale Projektartefakte
- In welchen Projekten erlaubt: alle UI-Projekte
- Letzte Prüfung: 2026-08-04
- Review bis: 2027-02-04

### Ergänzung zum verbindlichen Ablauf

- Vor einer neuen visuellen Richtung oder einem umfassenden UI-Refinement Impeccable mit dem passenden Arbeitsmodus nutzen und die Entscheidung im Design Contract der betreffenden Website festhalten.
- **Nach der Implementierung ist der KI-Detail-Review je gebauter Website Pflicht**, das Werkzeug dafür nicht. Ablauf und Prüfliste stehen in [[20-design/anti-ai-slop.md#Impeccable KI-Detail-Review]]; Impeccable arbeitet sie am schnellsten ab, die manuelle Strecke oben liefert denselben Nachweis. `G1` verlangt die Befundliste, nicht das Werkzeugprotokoll.
- Bei jeder neuen Website und jeder geänderten Motion Emil Design Engineering vor der Implementierung anwenden. Das Motion Inventory dokumentiert das gewählte Motion-Budget sowie für tatsächlich eingesetzte Bewegungen Zweck, Häufigkeit, Timing/Scroll-Range, Easing, Unterbrechbarkeit und Reduced-Motion-Fallback.
- Beim Schreiben einer einzelnen Bewegung `animate` verwenden. Emil Design Engineering liefert die Haltung, `animate` die Entscheidungsreihenfolge und die Umsetzung.
- **Vor der Abnahme jeder gebauten Website die Bewegungen gegen die zehn Prüfstandards prüfen**, bevorzugt mit `review-animations`, sonst manuell. Befunde beheben oder mit Grund im Decision Log festhalten. `G1` verlangt die geprüfte Bewegung, nicht den Skill-Lauf.
- **Für das Auftaktfeld jeder gebauten Website die Fassungen wirklich bauen**, bevorzugt mit `prototype`, danach den Visual Iteration Loop nach [[20-design/visual-iteration-loop.md]] führen. Darüber hinaus `prototype` nur in der Entwurfsphase und nur für einzelne Bauteile, nie für ganze Websites.
- Der Loop braucht ein Browserwerkzeug, mit dem der Agent den laufenden Build selbst ganzseitig rendert und ansieht. Welches Werkzeug das ist, wird hier geführt; fehlt eines, ist das ein Blocker nach [[70-qa/quality-gates.md]] und wird im Decision Log festgehalten.
- Der Skill `apple-design` desselben Repositorys ist bewusst **nicht** installiert. Sein Inhalt steht als Referenz in [[90-references/apple-fluid-interface.md]] und wird von dort gelesen.
- Der Skill `find-animation-opportunities` desselben Repositorys ist derzeit **nicht** installiert. Sein Auswahlprinzip widerspricht dem [[20-design/motion-and-interaction.md#Motion-Budget]] nicht mehr; bei künftiger Verfügbarkeit wird er nach Nutzen, Überschneidung und Wartungsaufwand neu bewertet.

## Frontend Design

- Name: `frontend-design`
- Typ: offizielles Plugin von Anthropic fuer Claude Code
- Status: **stark empfohlen vor jeder neuen visuellen Richtung**, keine Abnahmebedingung
- Ausloesung: die Beschreibung triggert auf den Bau neuer UI und auf das Umgestalten bestehender
- Quelle und Lizenz: [anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design), Lizenz im Repository; Installation ueber `/plugin install frontend-design@anthropics`
- Faehigkeiten: erzwingt eine aesthetische Festlegung **vor** der ersten CSS-Zeile, fuehrt einen Zwei-Pass-Ablauf aus Designplan und Pruefung gegen den Brief und benennt die derzeit bekannten Ballungen generierter Oberflaechen
- Grenzen und Risiken: die Anweisung ist auf Produkt- und Marketingoberflaechen zugeschnitten und kennt die deutschen Rechts- und Betriebsanforderungen nicht. Bei Widerspruch gilt die kanonische Notiz nach [[00-start/04-plugins-and-skills.md#Vorrang der Brain-Regeln vor Skill-Vorschlägen]]
- Datenzugriff: die Projektdateien
- In welchen Projekten erlaubt: alle UI-Projekte
- Letzte Pruefung: 2026-09-19
- Review bis: 2027-03-19

### Was davon kanonisch uebernommen ist

Die Anweisung diagnostiziert dieselbe Ursache, die dieses Vault beschreibt, und benennt sie praeziser: **Verteilungskonvergenz.** Ohne Vorgabe waehlt ein Modell die wahrscheinlichste Loesung, und die ist ueber alle Auftraege dieselbe. Drei Punkte sind daraus in die kanonischen Notizen uebernommen:

- die bekannten Ballungen und das Vorlagen-Chrome in [[20-design/anti-ai-slop.md#Bekannte Ballungen]];
- der Pruefsatz *Waere ich bei einem anderen Auftrag derselben Gattung an derselben Stelle gelandet?* ebenda;
- der Gewichtsraum als Hierarchiemittel in [[20-design/typography-layout-and-spacing.md#Kalibrierte Type Ramp]].

Nicht uebernommen ist die dortige Empfehlung, Hintergruende mit Verlaeufen, geometrischen Mustern und Effekten zu schichten. Fuer Websites lokaler Betriebe bleibt es bei [[20-design/anti-ai-slop.md]]: dekoratives Rasternetz, Streifenverlauf und radialer Farbschein ohne Lichtquelle sind Befunde. Der Unterschied ist der Gegenstand, nicht die Qualitaet des Rats.

## Web Build

- Name: `web-build`
- Typ: eigener Skill dieses Repositorys, unter `.claude/skills/web-build/`
- Status: Standardweg fuer Website-Auftraege lokaler Betriebe
- Auslösung: die Beschreibung triggert auf Website-Auftraege fuer lokale Betriebe; der Skill laedt sich selbst, statt gelesen werden zu muessen
- Quelle und Lizenz: eigenes Werk, mit diesem Vault versioniert
- Fähigkeiten: fuehrt die Fast Lane aus [[00-start/05-web-product-workflow.md#Fast Lane]] aus - Projektordner, Extract der alten Seite, Recherche, Brief, Kit-Bloecke ziehen, Tokens setzen, Auftaktfassungen, Renderdurchgang, `qa.sh`, Release-Readiness
- Grenzen und Risiken: nur Fast Lane. Auth, Zahlung, eigene Datenhaltung, Sonderfunktion oder mehrere Fassungen loesen den Wechsel auf die Full Lane aus. Der Skill verweist auf die kanonischen Notizen und dupliziert sie nicht; bei Widerspruch gilt die Notiz
- Datenzugriff: der Projektordner, `web-kit/` und dieses Vault
- In welchen Projekten erlaubt: Websites lokaler Betriebe
- Letzte Prüfung: 2026-09-19
- Review bis: 2027-03-19

### Installation ueber das Plugin

`.claude-plugin/` buendelt den Skill als Plugin, damit er auf Laptop und Server mit einem Befehl installiert ist statt manuell verlinkt:

```
/plugin marketplace add johstn8/web-brain
/plugin install web-build@johstn8
```

Ein manuell verlinkter Skill laeuft auf zwei Maschinen frueher oder spaeter auseinander; das Plugin macht `/plugin update` zur einzigen noetigen Handlung.

## Vorrang der Brain-Regeln vor Skill-Vorschlägen

Skills liefern Vorschläge, keine Freigaben. Widerspricht ein Skill-Vorschlag einer kanonischen Notiz, gilt die Notiz, und der Konflikt wird im Decision Log des Projekts vermerkt, statt ihn stillschweigend zugunsten des Skills zu entscheiden.

Bekannte, wiederkehrende Konfliktstellen:

- Copy-Vorschläge mit Kurzstatements unter Überschriften, Dreierrastern aus Vorteilen oder Vertrauenszeilen mit Datums- und Quellenangabe. Es gilt [[10-strategy/website-copy.md]].
- Sektionsvorschläge mit Eyebrow- oder Kickerzeile. Es gilt [[20-design/anti-ai-slop.md#Kicker und Überschriften]].
- Vorschläge, mehrere Varianten als Auswahlkandidaten zu behandeln. Es gilt [[00-start/05-web-product-workflow.md#Anzahl der Websites]] zusammen mit [[20-design/design-direction.md#Stilabstand bei mehreren Websites]].

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
