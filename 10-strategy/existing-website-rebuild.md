---
type: canonical
status: canonical
updated: 2026-09-19
review_by: 2027-02-03
depends_on:
  - "[[00-start/05-web-product-workflow.md]]"
  - "[[50-legal/assets-copyright-and-licenses.md]]"
impacts:
  - content
  - sitemap
  - assets
  - legal
  - privacy
  - seo
---

# Existing Website Rebuild

## Trigger und Ziel

Bei vollständigem Neubau, Relaunch oder Modernisierung einer vorhandenen Website ist Quellenwiederherstellung Pflicht. Ziel ist, vorhandene Unternehmenssubstanz zu bewahren und den Neubau nicht mit erfundenem Ersatzinhalt zu füllen. Gefundene Angaben werden nach [[#Übernahme ohne Rückfrage]] übernommen, nicht erst bestätigt.

Vor Beginn muss der Projektordner nach [[00-start/05-web-product-workflow.md]] existieren. Sämtliche Fundstellen, Downloads und Entscheidungen bleiben in diesem Projekt.

## Übernahme ohne Rückfrage

**Die eigene Website des Betriebs ist für seine eigenen Angaben eine Primärquelle, keine Verdachtsquelle.** Preise, Öffnungszeiten, Leistungen, Kontaktdaten und Anschrift werden von dort übernommen, als richtig behandelt und eingebaut. Der Build hält dafür nicht an.

Das gilt ausdrücklich auch dann, wenn die Angabe alt aussehen könnte. Eine veraltete Öffnungszeit ist ein Fehler, der vor dem Launch in zwei Minuten korrigiert wird; eine unterbrochene Arbeit kostet mehr als sie verhindert.

**Was auffällt, wird notiert, nicht erfragt.** In `PROJECT.md` entsteht der Abschnitt `Übernommene Angaben` mit Quelle, Abrufdatum und — sofern vorhanden — dem Zweifel in einem Satz:

```
## Übernommene Angaben
Quelle: https://alte-seite.de, abgerufen am 2026-09-19

- Öffnungszeiten, Preise, Leistungen, Kontakt: übernommen
- Anmerkung: Die Preisliste nennt "Stand 2023". Wirkt alt, wurde trotzdem
  übernommen. Vor dem Launch bestätigen lassen.
```

Dieselbe Anmerkung geht als offener Punkt in `release-readiness/<website-slug>.md`. Dort gehört sie hin: Sie blockiert die **Veröffentlichung**, nicht die **Arbeit**.

**Widerspricht sich etwas, wird es benannt.** Sagen zwei Quellen Verschiedenes — die Website nennt andere Zeiten als das Maps-Profil, das Impressum eine andere Anschrift als die Kontaktseite — dann wird die plausiblere genommen, der Widerspruch notiert und weitergearbeitet. Ein Widerspruch ist eine Anmerkung, keine Rückfrage.

## Quellenreihenfolge

1. aktuelle eigene Website, eigene PDFs und verlinkte offizielle Profile
2. bereitgestellte oder sonst gefundene Originaldateien
3. amtliche oder fachlich zuständige Register und Behörden
4. Plattformoberflächen oder APIs
5. Social-, Lieferdienst-, Branchen- und Presseprofile
6. weitere Drittquellen und Designreferenzen

Konflikte nicht durch Mehrheitsentscheidung lösen. Quelle, Datum und Widerspruch im Projekt erfassen, die plausiblere Angabe verwenden und weiterarbeiten. Die Betreiberbestätigung holt der Nutzer vor dem Launch über [[60-operations/release-readiness-register.md]], nicht der Agent während des Builds.

## Bestandsaufnahme

- Alle erreichbaren Seiten, Navigation, Downloads, Metadaten, strukturierte Daten und Redirect-relevante URLs erfassen.
- Betreiber-, Kontakt-, Register-, Standort- und Branchenangaben extrahieren und übernehmen.
- Leistungen, Produkte, Preise, Öffnungszeiten, Reservierung, Liefer-/Abholwege, Speisekarten und zeitkritische Hinweise erfassen.
- Fotos, Logos, Videos, PDFs, Fonts und sonstige Medien mit Original-URL, erkennbarem Urheber und gewünschter beziehungsweise tatsächlicher Verwendung inventarisieren.
- **Logo gezielt suchen und einsetzen.** Das Logo des Betriebs wird aktiv gesucht: im Kopfbereich der alten Website, im Favicon, im Social-Asset, in PDFs, auf Fahrzeugen, Schildern oder Drucksachen und in offiziellen Profilen. Wird eines gefunden, wird es in jeder gebauten Website sichtbar verwendet, bevorzugt auf der Startseite. Auflösung, Alter oder gestalterische Qualität sind kein Grund, es wegzulassen oder durch ein eigenes Zeichen zu ersetzen. Platzierungsregeln in [[20-design/design-direction.md#Logo des Betriebs]]. Wird keines gefunden, wird das ausdrücklich als Befund dokumentiert.
- Offizielle Social-Media-, Bewertungs-, Lieferdienst-, Buchungs- und Branchenprofile suchen. Nur verlinken, wenn Identität anhand Name, Domain, Adresse, Telefon oder gegenseitiger Verlinkung belastbar ist.
- Veraltete Inhalte nicht still löschen: als `reuse`, `rewrite`, `verify`, `archive` oder `omit` entscheiden.

Bestandsinhalte, Bilder, Gestaltung, Dokumentlayouts und Interaktionen dürfen strukturiert übernommen, kopiert, kreativ adaptiert und im Build verwendet werden. Faktenkonflikte und die tatsächliche Verwendung werden anschließend im Review festgehalten; die Dokumentation führt zu keinem Build-Stopp oder Ersatz.

## Speisekarten, Preislisten und Dokumente

Gefundene Speisekarten, PDFs und Bilder sind wichtige Quellen und dürfen direkt im Build verwendet werden. Positionen, Varianten, Allergene, Preise und Gültigkeitsdatum getrennt extrahieren. Aktualität als Prüfhinweis dokumentieren, wenn sie für die Aussage wichtig ist. Es gibt weder `reference-only` noch einen rechtlich motivierten Ersatz.

## Google Maps und Unternehmensdaten

Google Maps intensiv zur Identifikation, Verifikation und Verlinkung nutzen, aber nicht scrapen. Die Google-Maps-Bedingungen untersagen insbesondere das Extrahieren und Speichern von Maps-Inhalten außerhalb der Dienste; Places-Inhalte unterliegen zusätzlichen Cache- und Attributionsregeln.[^maps-terms][^places-policy]

Projektablauf:

1. eindeutigen Eintrag und Place ID bestimmen; bei Mehrdeutigkeit Betreiber fragen;
2. Maps-URL für Ort, Suche oder Route dokumentieren. Maps URLs funktionieren ohne API-Key und öffnen Google Maps plattformübergreifend.[^maps-urls]
3. Name, Anschrift, Telefon, Öffnungszeiten, Reviews, Stoßzeiten und Website nicht allein aus Maps in den Projektbestand kopieren. Als temporären Recherchehinweis in `SOURCE-RIGHTS-REVIEW.md` mit `verify-required`, Abrufdatum, Owner, Frist und vorgesehener Primärquelle erfassen und vor der Übernahme bestätigen;
4. Places API nur bei projektspezifischer Freigabe, Abrechnung, erlaubten Feldern, Speicherung und Attribution einsetzen;
5. Google-Fotos oder Reviews nicht herunterladen und rehosten. Bei API-Ausgabe Autor-/Anbieterattribution und Quelllink gemäß Richtlinie erhalten;
6. automatisches Embed gegen normalen Link, Click-to-load, Consent, Performance und Fallback abwägen.

Fehlen API-Zugang, Billing, eindeutige Place ID oder zulässiger Datenweg, Blocker im PROJECT.md melden. Als sicherer Fallback normale Maps-URL und vom Betreiber bestätigte Kontaktdaten verwenden.

## Bestehendes Impressum und Datenschutz

- Altes Impressum als Quelle für Betreiber-, Kontakt-, Register-, Aufsichts- und Steuerdaten archivieren; Aktualität prüfen.
- Alte Datenschutzerklärung nach genannten Dienstleistern, Formularen, Tracking, Embeds, Fonts, Hosting und Aufbewahrung durchsuchen.
- Neue Rechtstexte nicht durch Kopieren erzeugen. Sie folgen [[50-legal/legal-decision-tree.md]], [[50-legal/privacy-and-consent.md]] und dem tatsächlichen neuen Dateninventar.
- Abweichungen zwischen Alttext und neuem System in `SOURCE-RIGHTS-REVIEW.md` festhalten und fachlich freigeben lassen.

## Quellen- und Owner-Einschätzung

Die Quellenarbeit wird nach [[50-legal/assets-copyright-and-licenses.md]] nach dem Build im Review protokolliert. Jeder Eintrag enthält tatsächlichen Einsatz, Owner, offene Frage und gewünschten späteren Prüftermin. Die KI trifft keine rechtliche Bewertung und baut keinen Fallback, Ersatz oder eine eingeschränkte Variante.

Lokale und ausgelieferte Websites verwenden die gewünschten Medien direkt. Der Owner kann die vollständige Review-Liste später einschätzen und ausdrücklich Änderungen beauftragen; bis zu dieser Nutzerentscheidung bleibt der tatsächliche Einsatz unverändert.

## Pflichtartefakte

- `PROJECT.md`: verbindliche Entscheidungen und offene Fragen
- `SOURCE-RIGHTS-REVIEW.md`: sämtliche Fundstellen, Übernahmeentscheidungen und Rechtsrisiken
- `ASSET-REGISTER.md`: nur ausgewählte Produktionsassets
- `DATA-PROCESSING-INVENTORY.md`: tatsächliche Datenflüsse des Neubaus
- `content/`: bestätigtes Content-Inventar und strukturierte Daten
- `research/legacy-site/`: Screenshots, URL-Inventar, gefundenes Logo und alte Rechtstexte
- `research/source-material/`: isolierte Quellenkandidaten mit Herkunft

[^maps-terms]: [Google Maps Platform Terms of Service, insbesondere No Scraping und No Caching](https://cloud.google.com/maps-platform/terms)
[^places-policy]: [Google Places API: Policies and attributions](https://developers.google.com/maps/documentation/places/web-service/policies)
[^maps-urls]: [Google Maps URLs: Get Started](https://developers.google.com/maps/documentation/urls/get-started)
