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
Sonderfunktion oder mehr als drei Fassungen.**

**Eine bis drei Fassungen bleiben Fast Lane**, wenn jede ein eigenes Preset
trägt: gleicher Inhalt, verschiedene Tokens und Grammatik, Ablage unter
`versions/01-<preset>/`. Der Stilabstand ist damit von Bauart erfüllt.
Ohne Angabe im Auftrag wird **genau eine** gebaut. Dann gilt
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

**Übernehmen, nicht rückfragen.** Preise, Öffnungszeiten, Leistungen und
Kontaktdaten von der alten Seite gelten als richtig und werden eingebaut.
Die Website eines Betriebs ist für seine eigenen Angaben eine Primärquelle.

Wirkt etwas veraltet oder widersprechen sich zwei Quellen: plausiblere
Angabe nehmen, Anmerkung in `PROJECT.md` unter `Übernommene Angaben`, Eintrag
in `release-readiness/<website-slug>.md` — und weiterarbeiten. Regel in
`web-brain/10-strategy/existing-website-rebuild.md#Übernahme ohne Rückfrage`.

### 3. Recherche und Brief

Betrieb, Angebot, Zielgruppe, Ort, Wettbewerb. Ergebnis als Kurzbrief in
`PROJECT.md`: Angebot, Zielgruppe, primäre Handlung, verfügbare
Beweisformen, Sitemap.

Keine Zahlen, Zertifikate, Auszeichnungen oder Kundenstimmen erfinden. Was
nicht belegt ist, entfällt oder wird als Annahme markiert.

### 3b. Gattungsvergleich — auch bei genau einer Website

Bevor irgendetwas gestaltet wird: acht bis zwölf Websites **derselben
Gattung** aufnehmen (Ort, Stadt, Deutschland, international), je Auftakt bei
1440 und 390 Pixel, und nach dem Qualitätsraster bewerten. Ergebnis: zwei
bis drei **Benchmarks** mit mindestens 16 von 20 Punkten, ein bis zwei
**Negativbeispiele**, die übertragbaren Prinzipien in Sätzen. Zuerst in den
Pool schauen; für Gastronomie stehen dort schon Benchmarks.

- Ablauf: `web-brain/90-references/reference-research-workflow.md#Gattungsvergleich`
- Raster: `web-brain/20-design/qualitaetsraster.md`
- Pool: `web-brain/90-references/website-reference-pool.md`

Ohne diesen Schritt entsteht eine Seite, die alle Messungen besteht und neben
guten Seiten ihrer Gattung trotzdem generiert aussieht. Genau das ist bei der
Trattoria Alberto viermal passiert.

### 4. Inhalt in Form bringen

`content/<website>.json` nach `web-kit/content/schema.json` füllen. Eine
Datei, stabile Pointer, keine Inhalte in Komponenten. Warum das so ist:
`web-brain/60-operations/owner-hosting-interface.md`.

### 5. Blöcke ziehen — mit Owner-Hosting

Aus `web-kit/blocks/`. **Das Kit ist der Pflichtausgangspunkt.**

**Owner-Hosting wird immer mitgebaut**, auch wenn es nicht im Auftrag steht:
eine Datei `content/<website>.json`, stabile Pointer, Feldtypen, Preview-Route,
dazu der Content-Loader aus dem Starter. Der Starter bringt das alles mit — es
wegzulassen wäre Rückbau, es nachzurüsten kostet ein Vielfaches. Regel in
`web-brain/00-start/05-web-product-workflow.md#Owner-Hosting ist Standard`. Wer einen
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

**Schriften gegen die Sperrliste prüfen, auch die des Presets.** Bis
2026-10-02 schlugen drei der fünf Presets eine gesperrte Familie vor.
Liste: `web-brain/20-design/typography-layout-and-spacing.md#Sperrliste`.

**Die Sektionsfolge der Startseite vorher aufschreiben**, je Sektion mit
Anordnung und Bildmaßstab. Zwei gleiche Zeilen hintereinander: umplanen,
bevor gebaut wird. Regel: `web-brain/20-design/landing-page-craft.md#Sektionsrhythmus`.

### 6b. Die harten Sperren — vor der ersten Komponente lesen

Diese Muster werden **nicht gebaut**, auch nicht mit Begründung, auch nicht
als Signaturdetail:

- **keine Zeile über einer Überschrift** — kein Ort, kein „seit 2002", keine
  Gattung in Fremdsprache, kein Status, keine Rubrik
- **keine Nummern an Sektionen** — kein `01 ·`, keine Ziffer mit Linie
- **kein Wort einer Überschrift in anderer Farbe oder kursiv** — eine
  Überschrift, eine Farbe, ein Schnitt
- **kein Verlauf, der ein Foto in den Seitengrund ausblendet**
- **nie drei gleich gebaute Sektionen in Folge** auf der Startseite
- keine fremdsprachigen Zierwörter, keine Vorlagenmöbel

Kanonisch: `web-brain/20-design/anti-ai-slop.md#Harte Sperren`. `qa.sh` misst
die ersten fünf und scheitert daran; die Prüfung lässt sich nicht abwählen.
Ein Signaturdetail ist **nicht** verlangt — fehlt reales Material dafür,
entfällt es.

### 7. Auftakt: zwei Fassungen, wirklich gebaut

**Zuerst prüfen, ob eine Gattungsregel greift**
(`web-brain/20-design/landing-page-craft.md#Gattungsregeln für den Auftakt`).
Für **Gastronomie** ist die Komposition gesetzt: das randlose Leitbild aus
`web-kit/blocks/auftakt/Leitbild.astro` — Foto oder Video über die volle
Höhe, H1 auf dem Bild, ein Satz, Band mit Zeiten, Adresse, Telefon, eine
Handlung. Die zwei Fassungen unterscheiden sich dann in Bild, Bildausschnitt,
Lage der H1 und Satz, nicht in der Komposition. Typo-, Kontakt- oder
Index-Auftakt für ein Restaurant wurden gebaut und vom Nutzer verworfen.

Ohne Gattungsregel: zwei Auftaktfassungen mit **verschiedenen
Kompositionen** aus `web-kit/blocks/auftakt/`. In beiden Fällen mit denselben
realen Inhalten bauen, bei 375 und 1280 Pixel **neben die Auftakte der
Benchmarks** legen, eine mit Begründung wählen.

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

**Danach der Benchmarkvergleich.** Eigene Startseite, Benchmarks und
Negativbeispiele auf einen Bogen, Auftakt bei 1440 und 390 Pixel und die
ganze Startseite. Schriftlich beantworten: Sieht die Seite aus wie die
Benchmarks oder wie die Negativbeispiele? Wie viele Rasterpunkte? Welche
Entscheidung der Benchmarks fehlt noch? **Unter 16 Punkten ist die Seite
nicht fertig.** Regel: `web-brain/20-design/qualitaetsraster.md#Benchmarkvergleich`.

### 9. QA

```bash
web-kit/scripts/qa.sh --dir <projekt>/site/dist
```

Platzhalter- und `TODO`-Reste, interne Links, Screenshots bei 375 und 1280,
axe gegen WCAG 2.1 AA, **harte Sperren gegen KI-Anmutung**, Lighthouse. Eine **übersprungene** Prüfung gilt nicht
als bestanden und gehört in `release-readiness/<website-slug>.md`.

### 10. Auf /dev sichtbar machen

**Sobald der erste Build steht**, nicht erst zur Abnahme. Die
Developer-Plattform erkennt `site/dist/` unterhalb von
`../projekte/<Projektname>/` von allein; erscheint der Eintrag nicht, ist das
ein Delivery-Fehler und wird dort behoben, nicht mit einem eigenen Port
umgangen.

Den Link in `PROJECT.md` eintragen. Der Nutzer soll mitschauen können, während
noch gebaut wird.

### 11. Abnahme

`G0` verkürzt und `G1` aus `web-brain/70-qa/quality-gates.md`. `G1` prüft
das Ergebnis, nicht das Werkzeug: vollständiger Tokenvertrag, vollständige
Zustände, Type Ramp, Kontrast in beiden Themes, echte Darstellung.

Danach das Release-Readiness-Register gegen Repository und ausgelieferten
Stand abgleichen und schließen.

## Erst bauen, dann fragen

**Vor der ersten gerenderten Website wird nichts gefragt.** Nicht die
Bahnwahl, nicht die Art Direction, nicht die fehlende Telefonnummer.
Entscheiden, weiterbauen, anmerken. Kanonisch in
`web-brain/00-start/05-web-product-workflow.md#Erst bauen, dann fragen`.

**Genau eine Ausnahme:** anhalten, bevor etwas Vorhandenes überschrieben
oder gelöscht wird. Das ist nicht umkehrbar, alles andere ist es.

Was an die Stelle der Frage tritt: fehlende Angabe → Platzhalter · Angabe
steht auf der alten Seite → übernehmen · Quellen widersprechen sich →
plausiblere nehmen · Geschmacksfrage → entscheiden und begründen ·
mehrdeutiger Auftrag → nächstliegende Lesart bauen · Auth oder Zahlung
taucht auf → die statische Seite fertig bauen und den Zusatzbedarf
anmerken.

Platzhalter sind erlaubt und blockieren nur die Veröffentlichung, nicht die
Arbeit. Die eine Grenze: Kundenstimmen, Zertifikate, Auszeichnungen und
Kennzahlen werden nicht erfunden — die Website eines realen Betriebs steht
damit für dessen Ruf gerade. Beschreibender Text und Bildplatzhalter fallen
nicht darunter.

### Die eine Nachricht am Ende

Wenn die Website steht, gerendert und durch `qa.sh` gelaufen ist, kommt
**eine** Nachricht, kein Tröpfeln über den Tag:

1. **Der Link** auf `johannstein.com/dev/<projekt>/`, vor allem anderen
2. **Entschieden:** Bahn, Benchmarks aus dem Gattungsvergleich, Art Direction, Auftaktkomposition, Sektionsfolge — je eine Zeile Begründung, dazu der Benchmarkbogen mit Rasterpunkten
3. **Angenommen:** je Annahme Quelle und Folge
4. **Offen:** identisch mit `release-readiness/<website-slug>.md`
5. **Zu entscheiden:** was nach 3 und 4 übrig bleibt, meist wenig, dazu neue Benchmark-Funde mit mindestens 16 Punkten, die der Nutzer in den Pool aufnehmen kann

## Was in dieser Bahn nicht verkürzt wird

Die Qualitätsregeln gelten unverändert. Verkürzt ist die Nachweisführung,
nicht das Handwerk. **Gattungsvergleich, harte Sperren und Benchmarkvergleich
werden nie verkürzt.** Tokenvertrag, Zustände, Kontrast, Tastaturbedienung,
Rechtsseiten, Performance und SEO sind genauso verbindlich wie in der Full
Lane.

Rechtstexte bleiben prüfpflichtige Entwürfe. Was veröffentlicht wird,
entscheidet der Nutzer beziehungsweise der benannte Owner, nie die KI.
