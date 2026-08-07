---
type: canonical
status: canonical
updated: 2026-08-03
review_by: 2027-02-03
impacts:
  - design
  - content
  - components
  - qa
  - legal
---

# Accessibility

## Zielstandard

WCAG 2.2 AA als technischer Mindeststandard für alle Projekte, auch wenn keine explizite gesetzliche Pflicht festgestellt wurde. WCAG deckt Wahrnehmbarkeit, Bedienbarkeit, Verständlichkeit und Robustheit ab und verlangt Konformität über vollständige Seiten und responsive Varianten.[^wcag]

## Build-Checkliste

- Semantische Landmarks, logische Überschriften, Skip Link, sinnvolle DOM-Reihenfolge.
- Vollständige Tastaturbedienung; sichtbarer, nicht verdeckter Focus.
- Accessible Name beschreibt Zweck, nicht Icon-Form.[^names]
- Aussagekräftige Alt-Texte; dekorative Bilder leer; komplexe Visuals mit Textalternative.
- Captions/Transkript für Medien; keine Information nur in Ton oder Bewegung.
- Textkontrast 4,5:1, großer Text 3:1; UI/Grafik 3:1.
- Zoom, Reflow, große Schrift, Orientierung und Textabstand ohne Verlust.
- Touch-/Pointer-Ziele nach WCAG 2.2 planen; Drag hat Alternative.
- Formulare mit Labels, Autocomplete, verständlichen Fehlern und erhaltenen Werten.
- Statusänderungen programmatisch melden, ohne Fokus unnötig zu verschieben.
- Authentifizierung ohne kognitive Rätsel; Passwortmanager und Paste nicht blockieren.
- Reduced Motion, Contrast, Color Scheme und erzwungene Farben berücksichtigen.
- `lang` korrekt, Sprachwechsel markieren; RTL bei relevanten Sprachen testen.[^lang]

## Prüfung

Automatisch: Axe/Lighthouse, HTML, Kontrast. Manuell: Tastatur, Screenreader, Zoom 200/400 Prozent, 320px Reflow, Reduced Motion, High Contrast, reale Fehlerflüsse. Automatisierung allein belegt keine Konformität.

## Rechtlicher Kontext Deutschland

Seit 28. Juni 2025 erfasst das BFSG unter anderem Dienstleistungen im elektronischen Geschäftsverkehr; Identifizierung, Authentifizierung, Sicherheit und Zahlung müssen wahrnehmbar, bedienbar, verständlich und robust sein.[^bfsg][^bfsgv] Kleinstunternehmen sind bei Dienstleistungen nach § 3 Abs. 3 BFSG ausgenommen, andere Gesetze oder Verträge können dennoch gelten.[^micro] Für jedes Projekt Scope über [[50-Legal/Legal Decision Tree]] prüfen. Eine Accessibility-Information oder Erklärung ersetzt keine barrierefreie Umsetzung.

[^wcag]: [W3C Recommendation: WCAG 2.2](https://www.w3.org/TR/WCAG22/)
[^names]: [W3C APG: Accessible Names and Descriptions](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)
[^lang]: [W3C: Language tags in HTML](https://www.w3.org/International/articles/language-tags/)
[^bfsg]: [BFSG § 1](https://www.gesetze-im-internet.de/bfsg/__1.html)
[^bfsgv]: [BFSGV § 19](https://www.gesetze-im-internet.de/bfsgv/BJNR092800022.html)
[^micro]: [BFSG § 3](https://www.gesetze-im-internet.de/bfsg/__3.html)

