---
type: canonical
status: canonical
updated: 2026-08-17
---

# Test Matrix

## Dimensionen

- Viewport: 320, 375, 768, 1024, 1280, 1440, 1920; Portrait/Landscape. Jede Breite wird real gerendert. Bei 1280, 1440 und 1920 wird die Kopfzeile mit der längsten realen Beschriftung auf Einzeiligkeit, Mindestluft und überstehende width-basierte Kinder geprüft
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

## Nachweis

Jeder Gate-Check verweist auf Test, Screenshot, Report oder dokumentierte manuelle Prüfung mit Datum, Environment und Prüfer. „Sieht gut aus“ ist kein Nachweis. Für sichtbare UI-Fehler ist ein echter Rendernachweis zwingend; kann er nicht erzeugt werden, wird dies vor Lieferung als Blocker gemeldet.

Für Designreferenzen ist ein Screenshot nur statischer Nachweis. Bewegung, Fokus, Tastatur, Touch, Ton, 3D/Canvas und Reduced Motion benötigen ein Interaktionsprotokoll, Video oder Trace gemäß [[90-References/Reference Research Workflow]].

Für jede primäre Inhaltsroute zusätzlich Vorwärts-/Rückwärts-Scroll, schnelle Scrollbewegung, Deep Link/Reload innerhalb einer Scrollsequenz, Routewechsel während laufender Motion und die `prefers-reduced-motion`-Komposition prüfen.
