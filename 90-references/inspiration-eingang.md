---
type: canonical
status: canonical
updated: 2026-11-05
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
   - **Erst trennen, was gelobt und was abgelehnt wurde.** Gespeichert wird nur das Gelobte. Was der Nutzer ablehnt, landet als Lehre in [[20-design/anti-ai-slop.md]] oder entfällt; eine Seite, die er verwirft, wird aus Pool, Katalog und Kit entfernt.
   - **Ganze Seite → Website-Vorlage**, nur wenn der Nutzer die Seite insgesamt stark nennt. Die Seite wird Abschnitt für Abschnitt aufgenommen (`--strecke 15`) und als eigene Vorlage unter `web-kit/vorlagen/<name>/` nachgebaut, dann neben das Original gelegt. Mehrere Seiten werden nie zu einer gemittelt.
   - **Einzelne Elemente → Kit-Block.** Nennt der Nutzer nur bestimmte Teile einer Seite, wird genau das als Block in `web-kit/blocks/` gebaut, damit es sich später in eine neue Website einsetzen lässt; die übrige Seite wird nicht aufgenommen. Das gilt seit 2026-11-07 als Markierung durch den Nutzer. Sonst wird sie als Muster in [[90-references/derived-design-patterns.md]] beschrieben und erst beim ersten echten Einsatz gebaut, nach [[30-frontend/web-kit.md#Wie das Kit wächst]].
   - **Referenz → Pool.** Die Seite kommt mit Einsatzfeld und Grundcharakter in den [[90-references/website-reference-pool.md]]. Der Eintrag durch den Nutzer gilt als Freigabe für den Pool.
3. **Grenzen:** Übernommen wird Grammatik, nicht Inhalt. Texte, Bilder, Logos, Markenfarben und Quellcode der Seite bleiben dort. Verletzt die Seite eine [[20-design/anti-ai-slop.md#Harte Sperren|harte Sperre]], wird alles andere übernommen und die Sperre im Eintrag benannt.
4. **Eintrag verschieben** von [[#Offen]] nach [[#Verarbeitet]], mit dem, was daraus wurde.

## Offen

| Adresse | Was gefällt | Eingetragen |
|---|---|---|

## Verarbeitet

Am 2026-11-07 hat der Nutzer 20 weitere Seiten als „Quatsch" verworfen: SocialNatives, Pexon, Julius Schaefer, eProc, Einstellungserfolg, KMC, Logokunst, Lieblingslead, Pink Elephant Coach, Matthias Niggehoff, Pflegequeen, Immobilien Einkauf, Barra, Lilia, CanDevsDoSomething, EVE BCN, ClaudeFolio, Thomas Stockham, das ATS-Dashboard und StepSafer. Sie sind aus Pool, Katalog und Kit entfernt.

| Adresse | Was gefiel | Daraus wurde | Nicht übernommen |
|---|---|---|---|
| [Glisse](https://glisse.kelvinzhang.ca/) | Apple-Design, Formen und Glas | `blocks/glas.css`, `GlasFilter.astro`; Werte in [[90-references/apple-fluid-interface.md#Liquid Glass im Web]] | die React-Bibliothek selbst; wir brauchen kein React |
| [comito](https://www.comito.de/) | Auftakt und Unterseitenköpfe, Minimalismus, Kopfzeile | Vorlage `system`, dazu `auftakt/Vollbild` | seitliche Kontaktleiste, dauerhaft schwebender Knopf |
| [ko:mon](https://www.ko-mon.de/) | Auftakt, Scrollen, Wörter färben sich ein, abgerundet | Vorlage `kongress`, dazu `Wortlicht`, `Kopfinsel` | – |
| [jovoco](https://jovoco.io/) | Rundungen, schlichter Auftakt mit Google-Bewertung, Sprachwahl, Kopfzeile | Vorlage `rund`, dazu `Bewertungszeile` | Pillen-Dachzeilen (S1), IBM Plex (Sperrliste) |
| [metagram](https://metagram-solutions.com/) | versetzte Boxen mit Kennzahlen, schräge Karte mit animierten Bögen | Vorlage `verlauf`, dazu `Kennzahlen`, `Bogenkarte` | Poppins- und Inter-Satz, Regenbogenflächen |
| [Scaly](https://scaly.com/) | Elemente, Aufbau, Design | Vorlage `kurs` | Chat-Fenster, Versal-Dachzeilen (S1) |
| [tunymedia](https://tunymedia.at/) | Elemente, Aufbau, Design | Vorlage `bogen` | – |
| [Lagalante](https://www.lagalante-restaurant.de/nuovo/) | Gerichte auf Weiß, Rechteckbilder am Rand, Textmenge | Vorlage `gericht`, dazu `Freisteller`, zweite Gastronomie-Form in [[20-design/landing-page-craft.md#Gattungsregeln für den Auftakt]] | blasses Riesenwort hinter der Karte |
| [MINE](https://minerestaurant.de/) | guter Grundaufbau | Vorlage `salon`; bestätigt `auftakt/Leitbild` als Grundform | Michelin-Plakette und Auszeichnungen, die Vorlage behauptet keinen Preis |
| [Carbone](https://carbonenewyork.com/) | kein KI-Eindruck, Geschichte, Bildplatzierung, Auftakt | Vorlage `abend`; Lehre: Bild und Geschichte tragen, nicht Effekte | – |
| [Standard Serious Pizza](https://www.standard-berlin.de/) | Weiß, Boxen und Bilder, große Schrift im Auftakt | Vorlage `wortmarke`, dazu `auftakt/Riesenwort` | Handzeichnungen und Schachbrett sind Marke, kein Baustein |
| [THE1](https://the1.amsterdam/) | große Bilder, Schrift, Farben, ganz große Überschriften, Einfachheit | Vorlage `hafen` mit Rot `#fa4d43`, Gelb `#fbb833`, Pink `#f19ec8`, Grün `#027b49` und den Riesenziffern, dazu `Farbfelder` | – |
| [Lightship](https://www.lightshiprv.com/) | Aufbau, Kopfzeile mit Morph, abgerundete Bilder, Überschrift auf Bild, Karten mit Plus | Vorlage `rahmen`, dazu `Kopfinsel`, `Querband` | der Stern-Logo-Morph selbst: gebaut ist das Schrumpfen, die Form hängt am Logo |
| [Meracinque](https://www.meracinque.com/) | Farbwahl, Platzierungen, Blöcke, Video | Vorlage `schmal`, dazu `Farbfelder` | – |
| [Mercury](https://mercury.com/) | kühler Look, Glasfelder im Auftakt | Vorlage `kuehl`, dazu `auftakt/Glasbuehne`, `Kacheln` | – |
| [Dentalize](https://www.dentalize.de/) | Kacheln, Videos in runden Boxen, Partner, Scrollanimationen, Überschriften in Schwarz und Grau | Vorlage `kachel` | ovale Stichwörter, die keine Knöpfe sind: vom Nutzer als KI-typisch benannt, siehe [[20-design/anti-ai-slop.md#Chrome und Beschriftung]] |
| [Inno ONE](https://inno-one.de/) | Abrundungen, die Kerbe durch die ganze Seite, Google-Bewertungen, Knöpfe, leichte Schrift, Farbwahl, Kreise und Pyramiden | Vorlage `kerbe` | eingebundene Kundenvideos |
| [Cornelia Poletto](https://cornelia-poletto.de/) | luxuriöser Eindruck, die Person im Auftakt | Vorlage `gastgeber` | Rubrikzeilen über den Überschriften (S1) |
| [Padella](https://www.padella.co/) | Scrollgefühl, Speisekarte, drei Bilder mit Hover | Vorlage `tageskarte`; Hover-Verhalten ist nachempfunden, das Original wurde nicht interaktiv gemessen | Lenis, ersetzt durch ein kleines eigenes Skript; handgezeichnete Wortmarke |
| [Salswee](https://salswee.com/) | ganze Seite | Vorlage `konditorei` | Bezahllogos im Fuß |
| [Zum Hecht](https://zum-hecht.de/) | professioneller Aufbau, Einbindung der Bilder, Texte; Schwarz austauschbar | Vorlage `gasthaus`, Kopffarbe als `--kopf` | Abschnitt „Termine", vom Nutzer abgelehnt; Karussellpfeile (S7), Einwilligungsleiste |
| [ESP Media](https://espmedia.de/) | Scrollanimationen, Kacheln, Creator-Bilder mit Zahlen, Team, schräge Handys, Fuß, Bewertung und Partner im Auftakt | Vorlage `creator`, Block `Bildwerte` | kursive Wörter in Überschriften, vom Nutzer abgelehnt; klassischer Verlaufsauftakt |
| [Fokus](https://fokus.so/planer/) | ganzer Aufbau, Landingpages je Kategorie, Bewertungen, Screenshots, Raster im Grund | Vorlage `raster` | KI-erzeugte Bilder, vom Nutzer abgelehnt; Rabattpille und farbiges Wort in der H1 (S1, S3) |
| [Zahnarzt Wels](https://zahnarzt-wels.at/) | Kacheln, Zufriedenheit, Team, leichte Schrift, Bilder bis an den Rand, Auszeichnungen und Glasfeld im Auftakt | Vorlage `praxishell` | Rubrik-Pillen über Kacheltiteln (S1) |
| [Big Mamma Group](https://www.bigmammagroup.com/) | Seite insgesamt, Auftakt, Einbindung der Elemente | Vorlage `trattoria` | Braun als Grundfarbe, vom Nutzer als altmodisch benannt; italienische Überschrift (S6) |
| [Pageou](https://www.pageou.de/) | ästhetische Bilder, simpel, luxuriös | Vorlage `licht` | – |
| [Sales Culture](https://sales-culture.de/) | nur: bewegter Flieger im Auftakt, Text neben Bild | Blöcke `auftakt/Pfadflug`, `BildText` | alles andere, vom Nutzer als schwach und mobil schlecht benannt |
| [Agency Invest](https://agencyinvest.de/) | nur: schwarzer Grund mit überlagerten Flächen und Fade | Block `Schwarzblende` | alles andere |
| [Modulo Consulting](https://www.modulo-consulting.de/) | nur: Text steigt aus dem Produkt, eckige Produktkacheln | Blöcke `Aufstieg`, `Produktkacheln` | Auftakt und Rest |
| [optiMICE](https://opti-mice.de/) | nur: Auftakt mit Farbelementen, Bildern und Zahlen | Block `auftakt/Farbbild` | der Rest |
| [Martina Halek](https://martinahalek.de/) | nur: Profilbild, Element Geschäftswachstum, Knopf | Block `auftakt/Profil` | der Rest |
| [Tulus Lotrek](https://www.tuluslotrek.de/) | nur: Idee des Reservierungsfensters | Block `Reservierung`, inhaltlich und gestalterisch verbessert | die Seite selbst |
| [Consile](https://consile.app/) | Konzept und Design einer Produktvorstellung | Block `Produktschritte` | Orange überall, zu wenig Abwechslung, Verläufe |
| [Saad Salman](https://saadsalman.org/) | schwebende Elemente, Hover | Block `Schwebend` | Ovale über Überschriften, Verläufe in Überschriften |
| [180 Product Viewer](https://tutor-timer-28553736.figma.site/) | Produktansichten, Knöpfe | Block `Produktansicht`; die Figma-Seite lud 2026-11-07 headless nicht, gebaut nach der Analyse vom August | – |
| [INIZIO Solar](https://sixth-powder-95605714.figma.site/) | stark | kein neuer Baustein; das Leitbild-Prinzip steht in B3 | Ovale über Überschriften, Verläufe |
| [RICO, Kempten](https://www.rico-gmbh.de/) | vom Nutzer am 2026-11-04 als Beispiel für einen Stil genannt, der „auch mal sinnvoll sein kann" | Kit-Preset `produkt`: Neo-Grotesk, weißer Grund, hellgraue Kacheln `#f0f2f5` mit 20 px Radius, Aktionen 8 px, keine Schatten, eine kräftige Markenfarbe. Muster „Produkt mit Kennwerten" in [[90-references/derived-design-patterns.md#Produktbeweis]]. Pool-Eintrag unter Hersteller und Technik. | farbige Wörter in Überschriften und Pillen-Dachzeilen (S1, S3), Inter (Sperrliste), Einwilligungsbanner für Werbetracking |
