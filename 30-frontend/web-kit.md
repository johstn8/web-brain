---
type: canonical
status: canonical
updated: 2026-09-19
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
| `blocks/` | Kopfzeile, `auftakt/` mit vier Kompositionen, Leistungen, Öffnungszeiten, Anfahrt, Team, Kontaktformular, Bewertungen, Preise, FAQ, Fußzeile |
| `legal/` | Impressum, Datenschutz, `consent/` |
| `content/` | `schema.json` als Datenmodell für Betriebsdaten |
| `scripts/` | `extract-old-site.ts`, `render-shots.ts`, `check-axe.ts`, `check-contrast.ts`, `link-check.ts`, `tokens-to-css.ts`, `tokens-to-designsystem.ts`, `qa.sh` |
| `starter/` | lauffähiges Astro-Projekt, das alles einbindet |

## Die Rollennamen sind fix

Der Tokenvertrag aus [[20-design/color-system.md#Tokenvertrag]] liegt im Kit als `tokens/tokens.json`. Die Rollennamen sind in jedem Kundensystem identisch; deshalb laufen alle Blöcke ohne Änderung in jedem Kundensystem. Nur die Werte wechseln pro Kunde. Der Weg von den Projektwerten in ein Design-System-Artifact steht in [[20-design/design-systems-und-artefakte.md]].

Zwei Websites aus demselben Kit sehen deshalb nicht gleich aus: die Blöcke sind identisch, werden aber über andere Tokenwerte, eine andere Auftaktkomposition und eine andere Sektionsfolge gezogen.

## Art-Direction-Presets

`tokens/presets/` traegt fuenf vollstaendige Stilrichtungen als **Datei**, nicht als Prosa. Jede ist ein kompletter Tokensatz mit Schriftrollen, Palette fuer Licht und Dunkel, Radius-, Abstands- und Bewegungsgrammatik.

| Preset | Fuer | Abgrenzung | Display / Text |
|---|---|---|---|
| `werkstatt` | Handwerk, Fahrzeugservice, Logistik, Bau | Rahmen, Radius null | Archivo 800 / Public Sans |
| `praxis` | Gesundheit, Pflege, Therapie | Flaeche, weiche Rundung | Newsreader / Public Sans |
| `tisch` | Gastronomie, Baeckerei, Hotellerie | Flaeche, dunkler Grund | Fraunces 300 / Work Sans |
| `kanzlei` | Kanzlei, Steuerberatung, Verwaltung | Haarlinie, schmale Lesestrecke | Spectral / Spectral |
| `atelier` | Studio, Architektur, Fotografie | Weissraum als einziges Trennmittel | Bricolage Grotesque / Instrument Sans |

Jedes ist an drei konkreten Seiten aus [[90-references/website-reference-pool.md]] belegt. Ein Preset ist keine Kopie dieser Seiten, sondern die Ableitung ihrer Grammatik auf den Tokenvertrag.

**Warum das ein Artefakt und keine Regel ist.** Eine Stilrichtung als Prosa muss bei jeder Anwendung gelesen, verstanden und in CSS uebersetzt werden, und das Ergebnis faellt jedes Mal anders aus. Als Datei wird sie einmal gebaut und danach gewaehlt. Das ist derselbe Tausch, den der ganze Umbau macht: Regeln kosten bei jeder Anwendung, Artefakte kosten einmal.

**Der Grund, warum es sie braucht.** Ohne Vorgabe waehlt ein Sprachmodell die wahrscheinlichste Loesung. Sie ist ueber alle Auftraege dieselbe, und genau daraus entsteht die Anmutung, die [[20-design/anti-ai-slop.md#Bekannte Ballungen]] beschreibt. Ein Preset setzt den Startpunkt woanders hin.

Ein Preset ist ein Ausgangspunkt, kein Fertigprodukt. Die Werte des Betriebs - Akzentfarbe aus Marke, Material oder Ort - werden danach gesetzt; die Rollennamen bleiben unveraendert. Zwei Websites mit demselben Preset **und** denselben Werten waeren ein Befund nach [[20-design/design-direction.md#Stilabstand bei mehreren Websites]].

### Schriften

Keine der verwendeten Familien ist eine, zu der ein Modell ohne Vorgabe greift. Alle stehen unter der SIL Open Font License 1.1 und werden von `scripts/fetch-fonts.ts` heruntergeladen und **im Projekt gehostet**: eine Einbindung von `fonts.googleapis.com` waere ein Drittanbieter-Datenfluss und damit ein Consent-Fall nach [[50-legal/privacy-and-consent.md]] fuer etwas, das keinen Consent braucht. Die Lizenz gehoert danach in das Asset Register.

## qa.sh

`scripts/qa.sh` prüft in dieser Reihenfolge:

1. Platzhalter- und `TODO`-Reste im Build
2. interner Link-Check über das ausgelieferte HTML
3. ganzseitige Screenshots bei 375 und 1280 Pixel
4. axe gegen WCAG 2.1 AA
5. Lighthouse für Performance, Accessibility, Best Practices und SEO

Fehlt ein Werkzeug, meldet der Lauf die Prüfung als **übersprungen**, nie als bestanden. Eine übersprungene Prüfung gehört als offener Punkt in `release-readiness/<website-slug>.md` nach [[60-operations/release-readiness-register.md]]. Ohne echten Render ist `G1` nach [[70-qa/quality-gates.md#G1 Design]] nicht erfüllt; das ist ein Blocker vor der Lieferung.

## Wie das Kit wächst

Nicht aus einer Wunschliste, sondern aus echten Builds. Beim Kundenprojekt wird jeder Block herausgezogen, der ein **zweites Mal** vorkommen wird, nicht jeder, der vorkommen könnte. Ein Block, der nur einmal existiert, gehört in das Projekt, nicht in das Kit.

Wandert ein Block ins Kit, verliert er dabei jede projektspezifische Annahme: keine Kundennamen, keine festen Texte, keine Farbwerte außerhalb der Tokenrollen.
