---
type: canonical
status: canonical
updated: 2026-08-19
---

# Test Matrix

## Dimensionen

- Viewport: 320, 375, 768, 1024, 1280, 1440, 1920; Portrait/Landscape. Jede Breite wird real gerendert. Die Kopfzeile wird mit längster realer Beschriftung, großer Systemschrift und 200 Prozent Zoom auf beabsichtigten Reflow, Überlauf, Beschnitt und erreichbare Ziele geprüft
- Browser: aktuelle stabile Chromium, Firefox, Safari/WebKit; erforderliche ältere Versionen laut Projekt
- Input: Tastatur, Touch, Maus, Screenreader, Voice/Zoom nach Zielgruppe
- Preferences: Reduced Motion, Dark/Light, High Contrast/Forced Colors, große Systemschrift
- Netz: offline, langsam, hohe Latenz, Request Timeout, Teil-Ausfall
- Session: anonym, eingeloggt, abgelaufen, gesperrt, jede Rolle, fremder Tenant
- Daten: leer, eins, viele, sehr lang, Unicode, RTL, ungültig, konfliktbehaftet
- API: Erfolg, 4xx, 5xx, Rate Limit, Retry, doppelte/späte Webhooks

## Testpyramide

- Static: Typecheck, lint, format, schema, links, licenses, secrets.
- Unit: reine Geschäftsregeln, Parser, Limits, Token-/Preisberechnung.
- Component: Semantik, Tastatur, Zustände und responsive Varianten; jede im Markup vorkommende Komponentenvariante gegen jede tatsächliche Untergrundfläche auf Kontextkontrast.
- Integration: Datenbank, RLS/AuthZ, Provider und Fehlergrenzen.
- E2E: wenige kritische Nutzerflüsse einschließlich negativer und Recovery-Pfade.
- Manuell: visuelle Qualität, Screenreader, reale Geräte, Motion, Copy, tatsächlicher Asset-Einsatz, sichtbarer Logo-Einsatz, Impeccable KI-Detail-Review und prüfpflichtige Rechtsentwürfe.

## Kritische Flüsse

Immer aufnehmen: Navigation und vollständige Unterseiten jeder gebauten Website, primäre Conversion, Formularfehler, Signup/Login/Recovery, Rollenwechsel, Zahlung/Kündigung, Account-Löschung, Consent/Widerruf, 404/500/Offline, Sitemap/Meta/Canonical/Robots je Route und Motion Inventory. Auf `217.154.218.30` alle Fassungen über `johannstein.com/dev` prüfen, außerhalb alle reservierten Ports.

Zusätzlich je Website den Produktions-Cutover aus [[60-Operations/Release Readiness Register]] als E2E-Kette prüfen: Preview-Sperren bleiben auf Preview aktiv, fehlen aber auf Produktion; Formulare erreichen echte Produktionsziele; eine eindeutige E-Mail-Testanfrage kommt an; Search-Console-Property, Sitemap und gegebenenfalls API zeigen exakt auf die Produktionsdomain.

## Deployment-Slots und Owner Hosting

Wo ein Deployment-Slot nach [[60-Operations/Owner Hosting and Dashboard#Deployment-Slots]] betrieben wird, sind zusätzlich zu prüfen:

- **Slotwechsel:** Ein Drop merkt nur vor und verändert weder Website noch Katalogstatus. Erst die zweite Bestätigung baut. Nach Erfolg zeigen öffentliche Website und Dashboard dieselbe Website.
- **Atomarer Doppelwechsel:** Zu keinem Zeitpunkt gehört der öffentliche Release zu einer anderen Website als der Dashboard-Tenant.
- **Cross-Tenant-Hostbindung:** Ein unbekannter Host, ein gefälschter `Host`-Header und ein Suffix-Host wie `hosting.<domain>.fremd.example` werden abgewiesen, bevor ein Tenant geladen wird. Eine Sitzung des vorherigen Tenants ist nach einem Slotwechsel wertlos.
- **Quellimmutabilität:** Der Hash der Website-Quelle ohne Buildausgaben ist vor und nach mehreren Builds identisch. Ein vorhandenes `dist/` der Quelle wird nicht überschrieben.
- **Fehlerfall:** Ein fehlgeschlagener oder parallel gestarteter Build lässt den aktiven Release unverändert; der gescheiterte Kandidat hinterlässt kein Releaseverzeichnis.
- **Passwortgate und noindex:** Die Staging-Domain verlangt Basic Auth, liefert `X-Robots-Tag: noindex, nofollow, noarchive` und eine sperrende `robots.txt`. Die ACME-Challenge auf Port 80 bleibt unverändert erreichbar.
- **Rollback:** Ein früherer Inhaltsstand wird neu gebaut, besteht die Prüfungen und ersetzt den aktiven Release vollständig; ebenso ist der Rollback der nginx-Konfiguration praktisch getestet.
- **Unabhängigkeit:** Bei gestopptem Dashboard und gestoppter Datenbank bleibt die öffentliche Website statisch erreichbar.
- **Vertragsgrenzen:** Nicht registrierte Pointer, Rechtstexte, Pfadtraversal, aus dem Baum zeigende Symlinks und freie Shellbefehle werden abgewiesen. Der Release enthält weder `_hosting` noch Secrets, interne Pfade oder Server-Logs.
- **Rechtsbezug:** Ändert ein Entwurf ein Feld mit `legalImpact`, verlangt das Dashboard vor dem Veröffentlichen eine sichtbare, ausdrücklich bestätigte Prüfung.

## Nachweis

Jeder Gate-Check verweist auf Test, Screenshot, Report oder dokumentierte manuelle Prüfung mit Datum, Environment und Prüfer. „Sieht gut aus“ ist kein Nachweis. Für sichtbare UI-Fehler ist ein echter Rendernachweis zwingend; kann er nicht erzeugt werden, wird dies vor Lieferung als Blocker gemeldet.

Für Designreferenzen ist ein Screenshot nur statischer Nachweis. Bewegung, Fokus, Tastatur, Touch, Ton, 3D/Canvas und Reduced Motion benötigen ein Interaktionsprotokoll, Video oder Trace gemäß [[90-References/Reference Research Workflow]].

Für jede primäre Inhaltsroute zusätzlich Vorwärts-/Rückwärts-Scroll, schnelle Scrollbewegung, Deep Link/Reload innerhalb einer Scrollsequenz, Routewechsel während laufender Motion und die `prefers-reduced-motion`-Komposition prüfen.
