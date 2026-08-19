---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - navigation
  - routes
  - breadcrumbs
  - metadata
  - sitemap.xml
  - tests
---

# Information Architecture and Sitemap

## Zwei Sitemaps

- Planungs-Sitemap: Seiten, Zweck, Zielgruppe, CTA, Status, Parent, Daten und Rechtsrelevanz.
- Technische `sitemap.xml`: nur kanonische, indexierbare Produktions-URLs; automatisiert aus derselben Routenquelle erzeugen.

## Seitenvertrag

Für jede Route dokumentieren:

- URL und Seitentyp
- Nutzerfrage und primäres Ergebnis
- genau ein H1 und primärer CTA
- benötigte Inhalte, Daten und Komponenten
- Auth-/Rollenbedarf
- SEO-Indexstatus, canonical, locale
- Analytics-Events mit Zweck
- Fehler-, Leer- und Ladezustände
- Datenschutz- oder Rechtsfolgen

## Regeln

- Jede Website besitzt eine Startseite und mehrere eigenständige, über die Navigation erreichbare Unterseiten. Die mindestens nötigen Inhaltsseiten werden aus Nutzerzielen abgeleitet, etwa Angebot/Leistungen, Ablauf/Über-uns, Kontakt; notwendige Rechtsseiten ergänzen sie. Anker auf der Startseite können unterstützen, ersetzen aber keine Unterseiten.
- Navigation nach Nutzerzielen, nicht interner Organisation benennen.
- Die sichtbare Hauptnavigation wird aus Nutzeraufgaben, Inhaltstiefe, Häufigkeit und realen Wortlängen entwickelt. Es gibt keine globale Höchstzahl. Direktlinks, Gruppen, Mega-Menü, Utility-Navigation, Seitenleiste und Fußbereich sind mögliche Ebenen; ihre Wahl und der Responsive-Übergang folgen [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]]. Rechtsseiten stehen in der Regel im Fußbereich, dürfen aber bei fachlichem Bedarf zusätzlich direkt erreichbar sein.
- Klicktiefe minimieren, ohne alles in die Hauptnavigation zu legen.
- Breadcrumbs bei echter Hierarchie; keine dekorativen Breadcrumbs.
- Filterzustände und Pagination erhalten stabile URLs, wenn teilbar oder indexierbar.
- 404, 500, Offline, Suche ohne Ergebnis und Rechtefehler explizit einplanen.
- Entfernte URL: Redirect oder begründetes `410`; niemals still brechen.
- Jede Sitemap-Änderung atomar nach [[00-Start/03 Update Protocol]] propagieren.
- Die identische Routenarchitektur, Navigation, internen Links und `sitemap.xml`-Inhalte in allen gebauten Websites vollständig umsetzen; jede Website hat ihre eigene auslieferbare Sitemap.

## Sitemap-Zeile

`Route -> Parent -> Zweck -> CTA -> Index? -> Auth/Rolle -> Daten -> Status -> Owner`
