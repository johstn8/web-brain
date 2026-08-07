---
type: canonical
status: canonical
updated: 2026-08-05
review_by: 2026-11-03
impacts:
  - data-inventory
  - forms
  - analytics
  - embeds
  - privacy-policy
  - consent-ui
---

# Privacy and Consent

> Orientierung, keine Rechtsberatung. Inhalt ist ein prüfpflichtiger Entwurf für Betreiber oder Rechtsberatung. Er hält weder Build noch Auslieferung auf; was veröffentlicht wird, entscheidet ausschließlich Nutzer/Owner.

## Privacy by Design

- Nur notwendige Daten, Zwecke und Aufbewahrung.
- Datenschutzfreundliche Defaults, getrennte Zwecke, Least Privilege und frühzeitige Löschung.
- Datenschutz-Folgenabschätzung bei voraussichtlich hohem Risiko prüfen.
- Auftragsverarbeiter, internationale Transfers, Betroffenenrechte und Incident-Prozess dokumentieren.
- Technische und organisatorische Maßnahmen risikobasiert; DSGVO Art. 25 und 32 verlangen Datenschutz durch Gestaltung und angemessene Sicherheit.[^gdpr]

## Dateninventar vor Text

Pro Verarbeitung: Datenkategorie, betroffene Person, Quelle, Zweck, Rechtsgrundlage, Empfänger/Dienstleister, Land/Transfermechanismus, Speicherdauer/Kriterium, Pflicht/Freiwilligkeit, Folgen der Nichtangabe, automatisierte Entscheidung, Löschpfad, Security Controls.

## Relaunch einer vorhandenen Website

Alte Datenschutzhinweise unter `research/legacy-site/` archivieren und darin genannte Anbieter, Formulare, Embeds, Analytics, Fonts, Hosting- und Kontaktwege als Prüfkandidaten extrahieren. Das neue [[80-Templates/Data Processing Inventory|Dateninventar]] entsteht ausschließlich aus dem neuen Code, der Infrastruktur und den realen Dienstleistern. Entfernte Altdienste dürfen nicht im neuen Text verbleiben; neue Dienste dürfen nicht fehlen.

Google Maps, Social Feeds und andere Drittanbieter bevorzugt als normale Links statt als automatisch ladende Embeds einsetzen. Für Embed oder API-Aufruf Datenfluss, Endgerätzugriff, Drittlandtransfer, Consent und Fallback entscheiden.

## Datenschutzhinweise

Klar, konkret und leicht zugänglich. Je nach Fall Verantwortlicher, DSB, Zwecke/Rechtsgrundlagen, berechtigte Interessen, Empfänger, Transfers, Dauer, Rechte, Widerruf/Widerspruch, Beschwerde, Bereitstellungspflicht und Automatisierung. Layered Notice nahe Formular plus vollständige Policy. Keine Dienste nennen, die nicht eingesetzt werden, und keinen Dienst auslassen.

## Consent-Entscheidung

1. Speichert/liest die Funktion Information auf einem Endgerät?
2. Ist sie allein für Übertragung oder den vom Nutzer ausdrücklich gewünschten Dienst unbedingt erforderlich?
3. Wenn nein: vor Aktivierung informierte Einwilligung nach TDDDG/DSGVO einholen.[^tdddg]
4. Zusätzlich Rechtsgrundlage für nachfolgende personenbezogene Verarbeitung bestimmen.

## Consent UI

- `Alle ablehnen` so leicht und sichtbar wie `Alle akzeptieren`.
- Granulare Zwecke und Anbieter, keine voraktivierten optionalen Kategorien.
- Vor Entscheidung nur unbedingt Erforderliches laden.
- Entscheidung versioniert nachweisen, ohne unnötige Identifizierung.
- Widerruf jederzeit über dauerhaften `Cookie-Einstellungen`-Link; nach Widerruf Tags stoppen.
- Policy und Scanner bei Tag-/Vendor-Änderung gemeinsam aktualisieren.

BfDI unterscheidet technisch notwendige und nicht notwendige Tracking-Technologien und verweist für letztere auf Einwilligung.[^bfdi]

## Fonts und Embeds

Fonts bevorzugt selbst hosten. Remote Fonts, Maps, Videos, Captchas, Chat und Social Embeds können beim Laden IP-/Gerätedaten an Dritte übertragen. Privacy-Mode, Click-to-load oder Consent prüfen; lokaler Fallback.

[^gdpr]: [EUR-Lex: DSGVO, insbesondere Art. 24-32](https://eur-lex.europa.eu/eli/reg/2016/679/art_32/oj/eng)
[^tdddg]: [TDDDG § 25](https://www.gesetze-im-internet.de/ttdsg/__25.html)
[^bfdi]: [BfDI: Cookies und andere Tracking-Technologien](https://www.bfdi.bund.de/DE/Buerger/Inhalte/Telemedien/Cookies.html)
