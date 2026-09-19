---
type: canonical
status: canonical
updated: 2026-09-19
depends_on:
  - "[[20-design/color-system.md]]"
  - "[[30-frontend/web-kit.md]]"
impacts:
  - "[[20-design/design-direction.md]]"
  - "[[00-start/02-routing-map.md]]"
  - project-master-spec
---

# Design Systems und Artefakte

Ohne eine kanonische Regel dazu entscheidet jede Session neu, wo Tokens, Auftaktfassungen und Kundendokumente leben. Genau daraus entsteht die doppelte Haltung, die es im Brain nicht geben darf.

## Zwei Ebenen von Design Systems

**Das Basissystem** trägt den neutralen Referenzsatz: die Vertragsrollen aus `web-kit/tokens/tokens.json`, die Struktur der Type Ramp, die Spacing- und Radiusskala und die Kernkomponenten mit Live-Preview. Es trägt **keine Kundenfarben**. Sein Akzent ist bewusst neutrale Tinte, damit niemand ihn versehentlich für eine Marke hält.

**Je Kunde** entsteht daraus ein abgeleitetes System mit den Werten dieses Betriebs: Farben, Schriften, Radius, Logo, Bildsprache. Die Rollennamen bleiben in beiden identisch. Deshalb laufen alle Kit-Blöcke ohne Änderung in jedem Kundensystem, und deshalb ist ein Kundenwechsel ein Wertewechsel, kein Umbau.

Ein abgeleitetes System entsteht **pro Projekt**, nicht auf Vorrat.

## Zuordnung, verbindlich

| Sache | Ort |
|---|---|
| Tokens, Komponenten, Assets einer Marke | Design-System-Artifact, je Kunde eines |
| Auftaktfassungen nebeneinander beurteilen | Design-Canvas-Artifact |
| Angebot, Briefing, Übergabe an den Kunden | Docs-Artifact |
| Regeln über Tokens, Zustände, Komposition | bleibt kanonische Notiz im Brain |
| Blöcke, Starter, Skripte | bleibt [[30-frontend/web-kit.md]] |

Die Begründung je Zeile: Ein Design-System-Artifact bietet Live-Preview, On-Canvas-Editing und einen teilbaren Link. Artboards nebeneinander sind die native Form des Auftaktfelds aus [[20-design/visual-iteration-loop.md#Divergenz vor Konvergenz: das Auftaktfeld]]. In einem Docs-Artifact kommentiert der Kunde direkt im Dokument, statt Änderungswünsche per Mail zu sammeln.

## Richtung des Abgleichs

Die Werte eines Kunden entstehen im Design Contract nach [[20-design/design-direction.md]] und gehen über `web-kit/scripts/tokens-to-designsystem.ts` in das Artifact:

```bash
node --experimental-strip-types web-kit/scripts/tokens-to-designsystem.ts \
  --project ../projekte/<kunde>/design-system/site/tokens.json \
  --out     ../projekte/<kunde>/design-system/site/design-system.json \
  --name    "<Betrieb>"
```

Änderungen, die **am Artifact** vorgenommen werden, kommen über `/design-sync` zurück in die Session und werden dort in die Projektdateien geschrieben. Ohne diesen Rückweg entsteht innerhalb eines Tages eine zweite Wahrheit.

**Ein Wert existiert immer nur an einer Stelle kanonisch.** Welche das ist, hält `PROJECT.md` je Projekt fest, als `Tokenquelle: projekt | artifact`. Steht dort nichts, gilt die Projektdatei.

## Was beim Import wegfällt

Das Zielformat verlangt je Tokenfamilie eine **Liste** von Einträgen, nicht eine Name-zu-Wert-Zuordnung. Farbwerte sind Hex, `rgb()`, `hsl()`, `oklch()` oder ein Alias auf einen existierenden Token.

Benannte Farben, `var()` und `color-mix()` fallen beim Import weg. Deshalb bricht `tokens-to-designsystem.ts` bei solchen Werten ab, statt sie zu exportieren: ein stiller Verlust im Artifact ist teurer als ein lauter Abbruch im Terminal.

## Grenze

Ein Artifact ersetzt keine kanonische Notiz. Es hält Werte und zeigt sie; die Regeln über Tokens, Zustände und Komposition bleiben hier im Vault. Wer eine Regel im Artifact notiert, hat sie an einem Ort abgelegt, an dem die nächste Session sie nicht sucht.
