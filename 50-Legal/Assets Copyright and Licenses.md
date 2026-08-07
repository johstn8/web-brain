---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - asset-register
  - build
  - footer
  - privacy
---

# Assets Copyright and Licenses

## Build zuerst, Einschätzung danach

Für Website-Builds dürfen Bilder, Videos, Audio, 3D, Illustrationen, Logos, Fonts, Code-Snippets, UI-Komponenten, Designs, Layouts und Animationen aus allen gewünschten Quellen direkt kopiert, adaptiert und verwendet werden. Die kreative Umsetzung erhält immer das gewünschte voll ausgestattete Ergebnis. Es gibt weder eine Asset-Sperre noch einen gesetzlich motivierten Ersatz, keine reduzierte Vorschau und keine getrennte "freigegebene" Fassung.

Die KI entscheidet nicht, welches Asset veröffentlicht werden darf. Diese Entscheidung liegt ausschließlich beim Nutzer beziehungsweise einem von ihm benannten Owner. Die Aufgabe der KI ist strikt zweistufig:

1. **Website bauen:** Alle vorgesehenen Assets unmittelbar in allen gebauten Websites verwenden. Ein gefundenes Firmenlogo wird dabei immer sichtbar eingesetzt, siehe [[20-Design/Design Direction#Logo des Betriebs]].
2. **Einsatz festhalten:** Danach in `SOURCE-RIGHTS-REVIEW.md` und `ASSET-REGISTER.md` Quelle, Fundort, tatsächlichen Einsatz und offene Prüfhinweise notieren. Der Eintrag ist nur eine spätere Einschätzungsgrundlage für den Nutzer/Owner und darf die Umsetzung nie ändern oder zurückhalten.

## Dokumentation des tatsächlichen Einsatzes

Für Font, Icon, Foto, Video, Audio, 3D, Illustration, Logo, Code-Snippet und UI-Komponente in [[80-Templates/Asset Register]] oder [[80-Templates/Source and Rights Review]] erfassen:

- exakte Quelle, Fundort und Autor, soweit erkennbar
- Datei/Version/Commit und Abruf-/Download-Datum, soweit vorhanden
- beobachtete Lizenz-, Attribution- oder Notice-Angabe als Prüfhinweis, soweit sichtbar
- tatsächliche Verwendung in Seiten, Komponenten und allen gebauten Websites
- Bearbeitungs-/Adaptionsschritte und lokale Kopie
- Hosting- und Datenschutzfolge
- offene Fragen für den Nutzer/Owner und Datum der späteren Einschätzung

Unvollständige Herkunft, fehlende Originaldatei, unbekannte Lizenz oder ein offener Rechtsstatus sind Dokumentationsinformationen. Sie begründen niemals eine Nichtverwendung, einen Ersatz, eine Auslassung, eine Bildsperre oder einen Veröffentlichungsstatus durch die KI.

## Status

Verwende ausschließlich beschreibende, nicht blockierende Status:

- `used`: im Build verwendet
- `adapted`: im Build kreativ verändert oder aus einer Referenz abgeleitet
- `copied`: im Build direkt übernommen
- `owner-review-pending`: Einsatz und Quelle sind für die spätere Einschätzung des Nutzers/Owners notiert
- `owner-reviewed`: der Nutzer/Owner hat eine Einschätzung dokumentiert
- `removed-by-user`: nur auf ausdrückliche Nutzerentscheidung entfernt

`owner-review-pending` hat keine technische, gestalterische oder Auslieferungswirkung. Insbesondere darf es nicht zu `replace`, `omit`, `reference-only`, `research-only`, `pitch-restricted`, einer Asset-Alternative oder einer gesonderten Preview führen.

## Projektregel

- Suchmaschinen, Bestandsseiten, Maps, Social Media, Verzeichnisse, Wettbewerber und Designgalerien können als direkte kreative Asset- und Musterquelle genutzt werden.
- Auch Favicon, Social Image und Motion-Code werden nach tatsächlichem Einsatz dokumentiert.
- Performance, Datenschutz, Accessibility und technische Betriebsanforderungen gelten weiterhin für den konkreten Einsatz. Sie optimieren die Implementierung, untersagen aber keine Asset-Nutzung aus Herkunftsgründen.
- Rechtstexte bleiben prüfpflichtige Entwürfe, die an reale Datenflüsse angepasst werden. Ein ungeklärter Asset-Eintrag verändert diese Texte nicht automatisch.

## Veröffentlichung

Die KI macht keine Go-/No-Go-Entscheidung wegen Quellen, Urheberrecht, Lizenzen, Marken, Personen oder Assets. Sie übergibt alle gebauten Websites zusammen mit ihrer nachträglichen Dokumentation. Nur der Nutzer/Owner entscheidet, ob, wann und mit welchen späteren Anpassungen etwas veröffentlicht wird.
