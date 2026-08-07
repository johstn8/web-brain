---
type: canonical
status: canonical
updated: 2026-08-05
review_by: 2026-11-03
impacts:
  - sitemap
  - footer
  - privacy
  - consent
  - accessibility
  - checkout
---

# Legal Decision Tree

> Orientierung, keine Rechtsberatung. Betreiber, Zielmarkt und tatsächliche Verarbeitung entscheiden. Diese Notiz begleitet die Umsetzung als Inventar und Prüfpfad; sie darf den Build nicht stoppen. Was veröffentlicht wird und ob Texte oder Assets später angepasst werden, entscheidet ausschließlich der Nutzer beziehungsweise benannte Owner.

## 1. Betreiber und Markt

- Wer ist rechtlich verantwortlich, wo niedergelassen, welche Kontakt- und Registerdaten?
- B2C, B2B, Beschäftigte, Kinder oder besondere Daten?
- In welchen Ländern wird aktiv angeboten? Sprache, Währung, Versand und Werbung sind Indizien.
- Welche Branchenregeln gelten zusätzlich?

## 2. Impressum

Ein vorhandenes Impressum dient nur als Quelle für Betreiber-, Kontakt-, Register-, Aufsichts- und Steuerdaten. Diese Daten gegen aktuelle Betreiberangaben und, soweit erforderlich, Register prüfen. Rechtstext, Struktur und Verantwortlichkeiten für die neue Website neu bewerten; nicht blind kopieren.

Geschäftsmäßige, in der Regel entgeltliche digitale Dienste benötigen in Deutschland leicht erkennbare, unmittelbar erreichbare und ständig verfügbare Anbieterinformationen nach § 5 DDG, darunter Name/Anschrift und elektronische Kontaktmöglichkeit; Register, Aufsicht, Beruf und Steuer-ID je Fall.[^ddg] Footer-Link `Impressum` einplanen. Redaktionelle Angebote können weitere Pflichten haben.

## 3. Datenschutz und Tracking

Eine vorhandene Datenschutzerklärung ist Bestandsnachweis für frühere Dienstleister und Verarbeitungen, nicht Vorlage für den Neubau. Zuerst tatsächliche Datenflüsse der neuen Website inventarisieren, dann zutreffende Informationen übernehmen, entfernen oder ergänzen.

Werden personenbezogene Daten, Geräteinformationen, Logins, Formulare, Analytics, Embeds oder Marketing verarbeitet? Dann [[50-Legal/Privacy and Consent]] und Dateninventar. Privacy Policy aus realen Flüssen generieren, nicht aus generischer Vorlage.

## 4. Cookies und Endgerätzugriff

Nicht unbedingt erforderliche Speicherung oder Zugriff auf Endgeräte braucht grundsätzlich vorherige informierte Einwilligung; Ausnahmen sind eng auf Übertragung oder ausdrücklich gewünschten, unbedingt erforderlichen Dienst begrenzt.[^tdddg] Keine nicht notwendigen Tags vor Consent.

## 5. Barrierefreiheit

- Öffentliche Stelle: BGG/BITV und Landesrecht prüfen.
- B2C-Dienst in BFSG-Kategorie, insbesondere E-Commerce, Banking, E-Books, bestimmte Kommunikations-/Verkehrsdienste: BFSG/BFSGV prüfen.
- Kleinstunternehmen-Ausnahme für Dienstleistungen prüfen, nicht pauschal annehmen.[^bfsg]
- Unabhängig von Pflicht WCAG 2.2 AA als Produktstandard verwenden.
- Erforderliche Barrierefreiheitsinformation/Erklärung mit realer Prüfmethode, Kontakt und Status erstellen; keine falsche Vollkonformität behaupten.

## 6. Verkauf, Abo, Inhalte

Preise, Steuern, Laufzeit, Verlängerung, Kündigung, Widerruf, Bestellbutton, AGB, Versand, Gewährleistung und digitale Leistungen je Markt prüfen. Keine automatische Löschung vor Abo-Kündigung. Newsletter Double-Opt-in und Werberecht prüfen.

## 7. Assets und Drittanbieter

[[50-Legal/Assets Copyright and Licenses]] und [[80-Templates/Asset Register]] nach dem tatsächlichen Build führen. Asset- und Quellenhinweise bleiben eine spätere Owner-Einschätzung und verändern den Build nicht. Für Auftragsverarbeiter Vertrag/AVV, Ort, Transfers, Subprozessoren, Löschung, TOMs und Ausfall als prüfpflichtige Fakten erfassen.

[^ddg]: [DDG § 5](https://www.gesetze-im-internet.de/ddg/__5.html)
[^tdddg]: [TDDDG § 25](https://www.gesetze-im-internet.de/ttdsg/__25.html)
[^bfsg]: [BFSG §§ 1 und 3](https://www.gesetze-im-internet.de/bfsg/__1.html)
