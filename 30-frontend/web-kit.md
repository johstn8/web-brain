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
