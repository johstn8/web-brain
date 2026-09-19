---
name: web-build
description: Baut die Website eines lokalen Betriebs von der Beauftragung bis zur Abnahme, mit einer gewaehlten Art Direction statt der generischen Standardanmutung - Baeckerei, Fahrschule, Handwerk, Praxis, Restaurant, Kanzlei, Studio. Nutze diesen Skill, sobald jemand eine Website fuer einen Betrieb bauen, neu bauen, relaunchen oder von einer alten Seite ablösen will, auch wenn nur "mach mir eine Seite fuer X" gesagt wird. Fuehrt die Fast Lane aus dem Web-Brain aus: Projektordner, Extract der alten Seite, Recherche, Brief, Kit-Bloecke ziehen, Tokens setzen, Renderdurchgang, qa.sh, Release-Readiness. Nicht fuer Anwendungen mit Login, Zahlung oder eigener Datenhaltung - die laufen ueber die Full Lane.
---

# Website eines lokalen Betriebs bauen

Dieser Skill führt die **Fast Lane** aus. Er verweist auf die kanonischen
Notizen und wiederholt sie nicht: was hier steht, ist die Reihenfolge, nicht
die Fachregel.

Die Quellen liegen in zwei Repositories neben diesem Projekt:

- `web-brain/` — die Entscheidungen: wie gebaut wird
- `web-kit/` — das Material: womit gebaut wird

## Zuerst: ist es die Fast Lane?

Die Fast Lane ist der Standard. Auf die Full Lane wird gewechselt, sobald
eine dieser Bedingungen zutrifft: **Auth, Zahlung, eigene Datenhaltung,
Sonderfunktion oder mehr als eine Fassung.** Dann gilt
`web-brain/00-start/05-web-product-workflow.md#Verbindliche Reihenfolge`
statt dieser Strecke.

Die Bahnwahl kommt mit Begründung in `PROJECT.md`, bevor der erste Ordner
entsteht: `Bahn: fast, Grund: …`

## Die Strecke

### 1. Projektordner

`../projekte/<Projektname>/` anlegen, niemals einen vorhandenen still
überschreiben. In der Fast Lane nur zwei Pflichtdateien:

- `PROJECT.md` aus `web-brain/80-templates/project-master-spec.md`
- `release-readiness/<website-slug>.md` aus
  `web-brain/80-templates/release-readiness-register.md`

Die drei weiteren Inventare entstehen nur in der Full Lane.

### 2. Bestand sichern

Gibt es eine alte Website, zuerst ziehen, bevor irgendetwas neu geschrieben
wird:

```bash
node --experimental-strip-types web-kit/scripts/extract-old-site.ts \
  --url https://<alte-seite> --out ../projekte/<Projektname>/extract
```

Das Ergebnis ist ein **Rohbestand, keine Wahrheit**. Jede Angabe — Preise,
Öffnungszeiten, Leistungen — gegen eine Primärquelle prüfen. Veraltete
Angaben stehen genau dort am häufigsten. Ablauf in
`web-brain/10-strategy/existing-website-rebuild.md`.

### 3. Recherche und Brief

Betrieb, Angebot, Zielgruppe, Ort, Wettbewerb. Ergebnis als Kurzbrief in
`PROJECT.md`: Angebot, Zielgruppe, primäre Handlung, verfügbare
Beweisformen, Sitemap.

Keine Zahlen, Zertifikate, Auszeichnungen oder Kundenstimmen erfinden. Was
nicht belegt ist, entfällt oder wird als Annahme markiert.

### 4. Inhalt in Form bringen

`content/<website>.json` nach `web-kit/content/schema.json` füllen. Eine
Datei, stabile Pointer, keine Inhalte in Komponenten. Warum das so ist:
`web-brain/60-operations/owner-hosting-interface.md`.

### 5. Blöcke ziehen

Aus `web-kit/blocks/`. **Das Kit ist der Pflichtausgangspunkt.** Wer einen
Block neu schreibt, den es dort gibt, hat den falschen Weg genommen und
begründet das in `PROJECT.md`.

Fehlt ein Block wirklich, wird er im Projekt gebaut — und nur dann ins Kit
gehoben, wenn er ein zweites Mal vorkommen wird. Regel in
`web-brain/30-frontend/web-kit.md`.

### 6. Art Direction wählen, dann Tokens setzen

Zuerst ein Preset aus `web-kit/tokens/presets/` wählen — `werkstatt`,
`praxis`, `tisch`, `kanzlei` oder `atelier`. Jedes bringt Schriftwahl,
Palette, Radius- und Trenngrammatik mit.

```bash
node --experimental-strip-types web-kit/scripts/tokens-to-css.ts --preset <name> --out <projekt>/src/styles/tokens.css
node --experimental-strip-types web-kit/scripts/fetch-fonts.ts   --preset <name> --out <projekt>/public/fonts
```

**Nicht ohne Preset starten.** Ohne Vorgabe entsteht die wahrscheinlichste
Lösung, und die ist über alle Aufträge dieselbe — genau die Anmutung, die
`web-brain/20-design/anti-ai-slop.md#Bekannte Ballungen` beschreibt.

Danach die Werte dieses Betriebs setzen: Akzent aus Marke, Material oder
Ort, mit Herleitung je Farbrolle in den Design Contract. Die **Rollennamen
bleiben unverändert**.

```bash
node --experimental-strip-types web-kit/scripts/check-contrast.ts --preset <name>
```

Der Kontrastlauf ist keine Kür: `G1` verlangt Kontrast in **beiden** Themes.
Erst danach entsteht die erste Komponente.

Vor der Festlegung lohnt der Prüfsatz: **Wäre ich bei einem anderen
Auftrag derselben Gattung an derselben Stelle gelandet?** Wenn ja, ist es
kein Entwurf, sondern ein Default.

### 7. Auftakt: zwei Fassungen, wirklich gebaut

Zwei Auftaktfassungen mit **verschiedenen Kompositionen** aus
`web-kit/blocks/auftakt/` und denselben realen Inhalten bauen, bei 375 und
1280 Pixel nebeneinander ansehen, eine mit Begründung wählen.

Gedanklich wählen zählt nicht. Ein Sprachmodell wählt dabei die
wahrscheinlichste Lösung, und genau die sieht generiert aus. Repertoire in
`web-brain/20-design/landing-page-craft.md#Auftakt-Repertoire`.

### 8. Ein Renderdurchgang

Ganzseitigen Render ansehen, schriftliche Befundliste mit Ort, Beobachtung
und Änderung schreiben, Befunde beheben.

```bash
node --experimental-strip-types web-kit/scripts/render-shots.ts \
  --base http://localhost:4321 --out qa-bericht/shots
```

**Ein Render ohne Befundliste ist kein Durchgang.** Ist in der Umgebung kein
echter Render erzeugbar, ist das ein Blocker vor der Lieferung, kein Grund
zum Überspringen.

### 9. QA

```bash
web-kit/scripts/qa.sh --dir <projekt>/site/dist
```

Platzhalter- und `TODO`-Reste, interne Links, Screenshots bei 375 und 1280,
axe gegen WCAG 2.1 AA, Lighthouse. Eine **übersprungene** Prüfung gilt nicht
als bestanden und gehört in `release-readiness/<website-slug>.md`.

### 10. Abnahme

`G0` verkürzt und `G1` aus `web-brain/70-qa/quality-gates.md`. `G1` prüft
das Ergebnis, nicht das Werkzeug: vollständiger Tokenvertrag, vollständige
Zustände, Type Ramp, Kontrast in beiden Themes, echte Darstellung.

Danach das Release-Readiness-Register gegen Repository und ausgelieferten
Stand abgleichen und schließen.

## Was in dieser Bahn nicht verkürzt wird

Die Qualitätsregeln gelten unverändert. Verkürzt ist die Nachweisführung,
nicht das Handwerk: Tokenvertrag, Zustände, Kontrast, Tastaturbedienung,
Rechtsseiten, Performance und SEO sind genauso verbindlich wie in der Full
Lane.

Rechtstexte bleiben prüfpflichtige Entwürfe. Was veröffentlicht wird,
entscheidet der Nutzer beziehungsweise der benannte Owner, nie die KI.
