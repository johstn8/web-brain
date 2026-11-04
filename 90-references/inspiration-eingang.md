---
type: canonical
status: canonical
updated: 2026-11-04
review_by: 2027-02-27
depends_on:
  - "[[90-references/reference-research-workflow.md]]"
  - "[[30-frontend/web-kit.md]]"
impacts:
  - "[[90-references/website-reference-pool.md]]"
  - "[[90-references/derived-design-patterns.md]]"
  - design-direction
---

# Inspirationseingang

## Zweck

Hier landen Websites, die der Nutzer selbst gefunden hat und gut findet. Sie sind die stärkste Quelle für den Stil: Eine eigene Recherche des Agenten findet, was gut bewertet ist. Der Eingang zeigt, was dem Nutzer gefällt. Jede [[90-references/reference-research-workflow.md#Stilrecherche|Stilrecherche]] liest ihn zuerst.

## Eintragen

Eine Zeile je Fund in die Tabelle [[#Offen]]: Adresse, und ein Satz, **was** daran gefällt, so konkret wie möglich. „Die runden Produktkacheln auf Hellgrau" hilft mehr als „modern". **Ohne Notiz gilt das ganze Designkonzept der Seite als Fund:** Typografie, Farb- und Flächenlogik, Radien, Aktionsform, Raster, Sektionsaufbau und Bewegung werden gemessen und eingeordnet. Mit Notiz liegt der Schwerpunkt auf dem Genannten. Bewertung, Gattung und Einordnung sind nicht nötig, die übernimmt der Agent. Ein Fund darf auch nur ein Detail betreffen, etwa wie ein Menü aufklappt oder wie Preise gesetzt sind.

Auf Zuruf („Eingang verarbeiten") oder zu Beginn der nächsten Stilrecherche wird jeder offene Eintrag verarbeitet.

## Verarbeiten

1. **Aufnehmen und messen:** `web-kit/scripts/stil-messen.ts --url <adresse> --out .research/eingang/<slug>`. Ergebnis sind Messung und Auftakte bei 1440 und 390 Pixel.
2. **Einordnen in eine oder mehrere von drei Ablagen:**
   - **Stilgrammatik → Kit-Preset.** Unterscheidet sich die gemessene Grammatik sichtbar von allen Presets im Übersichtsbogen `web-kit/tokens/presets/kacheln/uebersicht.webp`, entsteht ein neues Preset; sonst wird das nächste vorhandene nachgeschärft. Prüfsatz: Wäre die Richtung auf dem Bogen als eigene erkennbar?
   - **Baustein → Kit-Block oder Muster.** Eine Komponente oder Interaktion, etwa eine Produktkachel mit Kennwerten, wird als Block ins Kit gehoben, wenn ein laufender oder absehbarer Auftrag sie braucht oder der Nutzer sie dafür markiert. Sonst wird sie als Muster in [[90-references/derived-design-patterns.md]] beschrieben und erst beim ersten echten Einsatz gebaut, nach [[30-frontend/web-kit.md#Wie das Kit wächst]].
   - **Referenz → Pool.** Die Seite kommt mit Einsatzfeld und Grundcharakter in den [[90-references/website-reference-pool.md]]. Der Eintrag durch den Nutzer gilt als Freigabe für den Pool.
3. **Grenzen:** Übernommen wird Grammatik, nicht Inhalt. Texte, Bilder, Logos, Markenfarben und Quellcode der Seite bleiben dort. Verletzt die Seite eine [[20-design/anti-ai-slop.md#Harte Sperren|harte Sperre]], wird alles andere übernommen und die Sperre im Eintrag benannt.
4. **Eintrag verschieben** von [[#Offen]] nach [[#Verarbeitet]], mit dem, was daraus wurde.

## Offen

| Adresse | Was gefällt | Eingetragen |
|---|---|---|

## Verarbeitet

| Adresse | Was gefiel | Daraus wurde | Nicht übernommen |
|---|---|---|---|
| [RICO, Kempten](https://www.rico-gmbh.de/) | vom Nutzer am 2026-11-04 als Beispiel für einen Stil genannt, der „auch mal sinnvoll sein kann" | Kit-Preset `produkt`: Neo-Grotesk, weißer Grund, hellgraue Kacheln `#f0f2f5` mit 20 px Radius, Aktionen 8 px, keine Schatten, eine kräftige Markenfarbe. Muster „Produkt mit Kennwerten" in [[90-references/derived-design-patterns.md#Produktbeweis]]. Pool-Eintrag unter Hersteller und Technik. | farbige Wörter in Überschriften und Pillen-Dachzeilen (S1, S3), Inter (Sperrliste), Einwilligungsbanner für Werbetracking |
