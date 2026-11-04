---
type: canonical
status: canonical
updated: 2026-11-04
depends_on:
  - "[[30-frontend/stack.md]]"
  - "[[20-design/color-system.md]]"
impacts:
  - "[[00-start/05-web-product-workflow.md]]"
  - "[[20-design/design-systems-und-artefakte.md]]"
  - "[[70-qa/quality-gates.md]]"
---

# web-kit

## Was es ist

`git@github.com:johstn8/web-kit.git`, geklont neben diesem Vault. Das Kit hält das Material: Tokens, Blöcke, Rechtsseiten, Datenmodell, Skripte und einen lauffähigen Starter. Dieses Vault hält die Entscheidungen. Nichts wird doppelt gehalten.

**Das Kit ist der Pflichtausgangspunkt der Fast Lane** nach [[00-start/05-web-product-workflow.md#Bahnwahl: Fast Lane und Full Lane]]. Wer einen Block neu schreibt, den es dort gibt, hat den falschen Weg genommen und begründet das in `PROJECT.md`.

## Struktur

| Ordner | Inhalt |
|---|---|
| `tokens/` | `tokens.json` als Quelle, `tokens.css` generiert, Theme-Ableitung |
| `blocks/` | Kopfzeile, `auftakt/` mit fünf Kompositionen, darunter `Leitbild` als gesetzter Auftakt der Gastronomie, Leistungen, Öffnungszeiten, Anfahrt, Team, Kontaktformular, Bewertungen, Preise, `Karte` für Speise-, Getränke- und Preiskarten mit Gruppen, FAQ, Fußzeile |
| `blocks/` neu | `auftakt/Vollbild`, `Schlicht`, `Riesenwort`, `Glasbuehne`, `Kopfinsel`, `Bewertungszeile`, `Wortlicht`, `Kennzahlen`, `Bogenkarte`, `Querband`, `Kacheln`, `Freisteller`, `Farbfelder`, Glasmaterial `glas.css`; Herkunft und Voraussetzungen in `blocks/README.md` |
| `legal/` | Impressum, Datenschutz, `consent/` |
| `content/` | `schema.json` als Datenmodell für Betriebsdaten, mit `karten` (Gruppen, Positionen, Varianten, Merkmale) und `texte` (owner-bearbeitbare Fließtexte je stabilem Schlüssel) |
| `scripts/` | `extract-old-site.ts`, `render-shots.ts`, `check-axe.ts`, `check-slop.ts`, `check-contrast.ts`, `link-check.ts`, `tokens-to-css.ts`, `tokens-to-designsystem.ts`, `fetch-fonts.ts`, `stil-messen.ts`, `stilverlauf.ts`, `qa.sh` |
| `starter/` | lauffähiges Astro-Projekt, das alles einbindet |

## Die Rollennamen sind fix

Der Tokenvertrag aus [[20-design/color-system.md#Tokenvertrag]] liegt im Kit als `tokens/tokens.json`. Die Rollennamen sind in jedem Kundensystem identisch; deshalb laufen alle Blöcke ohne Änderung in jedem Kundensystem. Nur die Werte wechseln pro Kunde. Der Weg von den Projektwerten in ein Design-System-Artifact steht in [[20-design/design-systems-und-artefakte.md]].

Zwei Websites aus demselben Kit sehen deshalb nicht gleich aus: die Blöcke sind identisch, werden aber über andere Tokenwerte, eine andere Auftaktkomposition und eine andere Sektionsfolge gezogen.

## Art-Direction-Presets

`tokens/presets/` trägt dreizehn vollständige Stilrichtungen als **Datei**, nicht als Prosa. Jede ist ein kompletter Tokensatz mit Schriftrollen, Palette für Licht und Dunkel, Radius-, Abstands-, Aktions- und Bewegungsgrammatik. Alle mit derselben Auftaktzeile gerendert liegen als `tokens/presets/kacheln/uebersicht.webp` im Kit.

| Preset | Anmutung | Für | Abgrenzung, Aktion | Display / Text |
|---|---|---|---|---|
| `glas` | gegenwärtig | Finanzen, Software, hochwertige Dienstleistung | Glas über Bild, Aktion Pille | Albert Sans |
| `nord` | gegenwärtig | Kreative Betriebe, Kultur, Marken mit Haltung | Farbfelder auf Hellgrau, Aktion Pille | Familjen Grotesk |
| `teller` | gegenwärtig | Gastronomie, Manufaktur, starke Fotos | Reinweiß, Aktion Pille | Jost |
| `dienst` | gegenwärtig | IT, Agentur, Weiterbildung, Veranstaltung | weiche Kacheln, Aktion Pille | Manrope |
| `genuss` | gegenwärtig | Lebensmittelmarke, Hofladen, Feinkost | Farbfelder auf Creme, Aktion weich | Gupter / Readex Pro |
| `produkt` | gegenwärtig | Hersteller, Industrie, Technik | Kacheln mit 20 px Radius, Aktion weich | Onest |
| `freundlich` | gegenwärtig | Kita, Friseur, Café, Sport, Fahrschule | Farbfläche, Aktion Pille | Gabarito / Figtree |
| `klar` | gegenwärtig | Beratung, Immobilien, IT, moderne Praxis | Haarlinie, Aktion rund | Golos Text |
| `atelier` | gegenwärtig | Studio, Architektur, Fotografie | Weißraum, Aktion Pille | Bricolage Grotesque / Hanken Grotesk |
| `werkstatt` | gegenwärtig | Handwerk, Fahrzeugservice, Bau | Rahmen, Aktion Kante | Archivo 800 / Public Sans |
| `praxis` | klassisch | Gesundheit, Pflege, Therapie | Fläche, Aktion rund | Source Serif 4 / Public Sans |
| `tisch` | klassisch | Gastronomie, Bäckerei, Hotellerie | Fläche dunkel, Aktion weich | Alegreya 400 / Work Sans |
| `kanzlei` | klassisch | Kanzlei, Steuerberatung | Haarlinie, Aktion Kante | Spectral |

**Ein Preset ist der technische Startpunkt, nicht der Stil.** Der Stil eines Auftrags entsteht aus der Stilrecherche dieses Laufs nach [[20-design/design-direction.md#Stilwahl je Auftrag]] und liegt als projekteigenes Preset unter `<projekt>/design/<name>.json`; `--preset` nimmt dafür einen Pfad. Die Spalte „Für" ist ein Hinweis, keine Zuordnung: Ein Café kann `produkt` tragen, ein Handwerker `freundlich`. Die drei klassischen Presets tragen eine Serife und werden nur mit einem Bezug aus Marke, Ort oder Auftrag gewählt.

**Warum das ein Artefakt und keine Regel ist.** Eine Stilrichtung als Prosa muss bei jeder Anwendung gelesen, verstanden und in CSS übersetzt werden, und das Ergebnis fällt jedes Mal anders aus. Als Datei wird sie einmal gebaut und danach gewählt oder abgeleitet.

**Warum es dreizehn sind und nicht mehr fünf.** Bis 2026-11-04 hatten drei der fünf Presets Radius null, drei eine Serife, und die Buttons hingen an `radius-sm`. Das Ergebnis über mehrere Projekte war ein einheitlicher, älterer Hausstil, siehe [[20-design/anti-ai-slop.md#Bekannte Ballungen]]. Seitdem ist die Aktionsform ein eigenes Feld `grammar.aktionsform` (`kante`, `weich`, `rund`, `pille`), das `tokens-to-css.ts` als `--aktion-radius` ausgibt, und drei gegenwärtige Presets sind dazugekommen. Fünf weitere stammen aus den Funden des Nutzers vom selben Tag, siehe [[90-references/inspiration-eingang.md#Verarbeitet]]. Kräftige Flächen außerhalb der Farbrollen stehen in `grammar.farbfelder`, der Kontrastlauf prüft sie mit.

### Werkzeuge für die Stilwahl

- `scripts/stil-messen.ts --url <adresse> --out <ordner>` misst an einer Referenzseite Schriften, Type Ramp, Radien von Aktionen, Kacheln und Bildern, Grund- und Akzentfarben und nimmt den Auftakt bei 1440 und 390 Pixel auf. Grundlage der [[90-references/reference-research-workflow.md#Stilrecherche]] und des [[90-references/inspiration-eingang.md]].
- `scripts/stilverlauf.ts --kandidat <preset>` liest Displayschrift, Aktionsform, Grundhelligkeit und Papiergrund aus dem ausgelieferten CSS der letzten Websites unter `projekte/` und meldet Wiederholungen nach [[20-design/design-direction.md#Abstand zu den letzten Projekten]].

### Schriften

`fetch-fonts.ts` lädt eine variable Familie einmal je Zeichensatz mit Gewichtsbereich; vorher kam sie für jedes Gewicht einzeln, bei Nush O Jan dreimal. Keine der verwendeten Familien steht auf der [[20-design/typography-layout-and-spacing.md#Sperrliste]]. **Das galt bis 2026-10-02 nicht**: `tisch` schlug Fraunces vor, `praxis` Newsreader, `atelier` Instrument Sans, also genau die Familien, zu denen ein Modell ohne Vorgabe greift. Eine Fassung der Trattoria Alberto wurde damit gebaut, bevor es auffiel. Jede Familie eines Presets wird deshalb vor dem Eintrag gegen die Sperrliste geprüft, und ein Projekt prüft die Familie des gewählten Presets trotzdem noch einmal. Alle stehen unter der SIL Open Font License 1.1 und werden von `scripts/fetch-fonts.ts` heruntergeladen und **im Projekt gehostet**: eine Einbindung von `fonts.googleapis.com` waere ein Drittanbieter-Datenfluss und damit ein Consent-Fall nach [[50-legal/privacy-and-consent.md]] fuer etwas, das keinen Consent braucht. Die Lizenz gehoert danach in das Asset Register.

## qa.sh

`scripts/qa.sh` prüft in dieser Reihenfolge:

1. Platzhalter- und `TODO`-Reste im Build
2. interner Link-Check über das ausgelieferte HTML
3. ganzseitige Screenshots bei 375 und 1280 Pixel
4. axe gegen WCAG 2.1 AA
5. harte Sperren gegen KI-Anmutung über `check-slop.ts`, siehe [[#Harte Sperren im QA-Lauf]]
6. Lighthouse für Performance, Accessibility, Best Practices und SEO

Screenshots, axe und harte Sperren laufen über alle Routen der Website: die Sitemap vereinigt mit den HTML-Dateien im Build, damit auch Seiten mit `noindex` wie Impressum und Datenschutz geprüft werden. Bis 2026-11-04 stand dort die feste Starterliste `/,/leistungen,/kontakt`, und Projekte mit anderen Routen bekamen Fehlseiten geprüft.

Fehlt ein Werkzeug, meldet der Lauf die Prüfung als **übersprungen**, nie als bestanden. Eine übersprungene Prüfung gehört als offener Punkt in `release-readiness/<website-slug>.md` nach [[60-operations/release-readiness-register.md]]. Ohne echten Render ist `G1` nach [[70-qa/quality-gates.md#G1 Design]] nicht erfüllt; das ist ein Blocker vor der Lieferung.

### Harte Sperren im QA-Lauf

`scripts/check-slop.ts` öffnet jede Route aus der Sitemap im Browser und misst am gerenderten Dokument die Sperren S1 bis S5 aus [[20-design/anti-ai-slop.md#Harte Sperren]]: Dachzeile über einer Überschrift, Nummernmarke, Teilauszeichnung in einer Überschrift, Ausblendung eines Fotos über Verlauf oder Maske und drei gleich gebaute Sektionen in Folge auf der Startseite. Jede Sperre lässt `qa.sh` scheitern; die Prüfung kann nicht über `--skip` abgewählt werden.

Gemessen wird am Render, nicht am Quelltext, weil eine Dachzeile ein Absatz, ein Span, eine Pseudo-Zeile oder Teil eines Blocks sein kann. Die Schwellen sind an realen Seiten geeicht: Die Gastronomie-Benchmarks MINE, Pageou, Barra, Lilia und Carbone bestehen ohne Sperre, Impasto Rosso fällt mit zwei Dachzeilen durch, und alle vier Fassungen der Trattoria Alberto fallen genau an den Stellen durch, die der Nutzer kritisiert hat. Ein leichter Lesbarkeitsschleier über einem Foto ist erlaubt; gesperrt ist nur der Verlauf, der an einem Ende deckend wird, und die Maske, die das Bild transparent auslaufen lässt.

Die unveränderte Startseite des Starters besteht die Prüfung nicht: Sie ist ein technisches Gerüst mit vier gleich gebauten Sektionen und wird im Projekt umgebaut.

## Wie das Kit wächst

Nicht aus einer Wunschliste, sondern aus echten Builds. Beim Kundenprojekt wird jeder Block herausgezogen, der ein **zweites Mal** vorkommen wird, nicht jeder, der vorkommen könnte. Ein Block, der nur einmal existiert, gehört in das Projekt, nicht in das Kit.

Ein zweiter Weg ins Kit ist der [[90-references/inspiration-eingang.md]]: Websites, die der Nutzer gesammelt hat, werden gemessen und als Preset, Block oder Muster eingeordnet. Auch dann entsteht ein Block erst, wenn ein Auftrag ihn braucht oder der Nutzer ihn dafür markiert.

Wandert ein Block ins Kit, verliert er dabei jede projektspezifische Annahme: keine Kundennamen, keine festen Texte, keine Farbwerte außerhalb der Tokenrollen.
