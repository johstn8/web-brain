---
type: canonical
status: canonical
updated: 2026-08-05
review_by: 2027-02-03
impacts:
  - media
  - motion
  - dependencies
  - qa
---

# Performance

## Nutzerziele

Am 75. Perzentil realer Seitenaufrufe gelten als gut: LCP höchstens 2,5 s, INP höchstens 200 ms, CLS höchstens 0,1.[^cwv] Laborwerte helfen bei Diagnose, Felddaten entscheiden.

## Projektbudgets festlegen

- initiales JavaScript, CSS, Fonts, Hero-Media und Gesamttransfer
- Anzahl Third-Party Requests
- Main-Thread-Zeit und lange Tasks
- Route-spezifische LCP- und Interaktionsziele
- Mobile Mittelklassegerät und langsames Netz als Testprofil

## Umsetzung

- Server/Static Rendering für sofort benötigten Inhalt; Hydration nur für Interaktion.
- Code splitten nach Route und schwerer Funktion, nicht jede kleine Komponente.
- Bilder richtig dimensionieren, moderne Formate, responsive Sources, Above-the-fold priorisieren.
- `width`/`height`, Platzhalter und reservierte Flächen gegen CLS.
- Kritische Fonts lokal, subsetten, preload nur tatsächlich kritische Datei; Fallback-Metrik angleichen.
- Third Parties verzögern oder entfernen; Consent und Ausfall berücksichtigen.
- Die geforderte hohe Motion-Dichte auf Compositor-Eigenschaften umsetzen; Canvas/3D adaptiv und pausierbar. Bewegungsumfang wird über Route-Level-Messung, Ladepriorisierung und nur sichtbare aktive Szenen optimiert, nicht durch das Weglassen der Choreografie.
- Für einfache scrollgebundene und vorbestimmte Effekte CSS Scroll-Timelines oder WAAPI bevorzugen; Motion/GSAP für dynamische, mehrteilige oder unterbrechbare Choreografie. Keine geerbten CSS-Variablen pro Frame auf großen Komponentenbäumen verändern.
- Cache-Control, CDN, Kompression, Request-Deduplizierung und Datenpagination.
- Keine Lade-Skeletons, die mehr Layout Shift erzeugen als echter Inhalt.

## Messung

CI: Lighthouse oder gleichwertiges Budget. Produktion: RUM nach Route, Gerät und Region; Fehler und Deploy-Version korrelieren. PageSpeed Insights zeigt CrUX-Felddaten über 28 Tage, falls genügend Daten existieren.[^tools]

[^cwv]: [web.dev: Core Web Vitals thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds)
[^tools]: [web.dev: Core Web Vitals workflows](https://web.dev/articles/vitals-tools)
