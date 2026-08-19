---
type: canonical
status: canonical
updated: 2026-08-19
review_by: 2027-02-03
impacts:
  - sitemap
  - content
  - metadata
  - redirects
---

# SEO and Discoverability

## Verpflichtung je gebauter Website

Jede gebaute Website wird unabhängig vollständig SEO-optimiert. Sie enthält dieselben kanonischen, verlinkten Unterseiten und erzeugt für jede Route eigene crawlbare HTML-Inhalte, Titel, Description, Canonical, Social-Metadaten, Sitemap und interne Links. Die Umsetzung darf SEO nicht auf die Startseite, auf eine ausgewählte Website oder auf eine spätere Produktionsfassung verschieben.

## Technische Basis

- Einzigartiger, kurzer, beschreibender `<title>` pro Seite, ohne `|`.
- Einzigartige Meta Description für wichtige Seiten; sie beschreibt die konkrete Seite, nicht Keywords.[^snippet]
- Canonical nur auf die tatsächlich bevorzugte URL.
- Index/noindex bewusst; Staging, Accounts und interne Suche nicht versehentlich indexieren.
- `robots.txt` steuert Crawling, schützt keine Geheimnisse.
- `sitemap.xml` aus kanonischen Routen; `lastmod` nur bei echter Inhaltsänderung.
- Sinnvolle interne Links, Breadcrumbs, Redirects und 404/410-Verhalten.
- Semantisches HTML, serverseitig sichtbarer Hauptinhalt und stabile URLs.
- Jede Inhaltsseite hat eine eindeutige Suchintention, genau ein H1, schlüssige H2-Struktur, hilfreiche interne Links und für relevante Bilder passende Alt-Texte. Scroll- und JavaScript-Motion darf den Hauptinhalt nicht erst erzeugen oder vor Crawlern verstecken.

## Von Vorschau zu Produktion

Vorschau-Sperren und produktive Auffindbarkeit sind verschiedene Zustände. Für jede Website führt `release-readiness/<website-slug>.md` nach [[60-Operations/Release Readiness Register]] den Ist- und Zielzustand von nginx `auth_basic`, `X-Robots-Tag`, Robots-Meta, `robots.txt`, Canonicals, Sitemap, Redirects, DNS und Zertifikaten. Eine Seite gilt nicht als indexierbar, nur weil ein einzelnes `noindex` entfernt wurde.

Vor der Veröffentlichung werden Produktionsantworten und die tatsächlich ausgelieferte `robots.txt` geprüft, danach die Produktions-Property in Google Search Console verifiziert und die Sitemap eingereicht. API-Nutzung benötigt OAuth-Berechtigung und Property-Zugriff; ein API-Schlüssel allein genügt nicht.[^gsc-auth] Indexierungsanfragen ersetzen weder crawlbare interne Links noch eine korrekte Sitemap.[^recrawl]

## Social und Marke

- Favicon als `.ico` plus moderne SVG/PNG- und Apple-Varianten.
- OG/Twitter-Metadaten und echtes 1200x630-Social-Asset pro Seitentyp.
- Site Name, Theme Color, Canonical und Locale konsistent.
- Web App Manifest nur wenn Installierbarkeit oder App-Identität gebraucht wird.[^manifest]

## Structured Data

Nur einen von Google unterstützten Typ verwenden, der sichtbaren, wahren Seiteninhalt exakt abbildet. Keine erfundenen Reviews oder Ratings. Google nutzt strukturierte Daten zum Verständnis und für mögliche Rich Results, garantiert deren Anzeige aber nicht.[^appearance]

## Internationalisierung

`lang`, locale-spezifische URLs, `hreflang`, canonical und Sitemap gemeinsam planen. Übersetzte Copy redaktionell prüfen; keine Textlängenannahmen.

## AI-Discoverability

Klare Entitäten, Autoren, Daten, Quellen, Definitionen und crawlbare Inhalte verbessern maschinelles Verständnis. Keine separate „LLM-SEO“-Behauptung ohne messbaren Nutzen; Nutzerwert und technische Zugänglichkeit bleiben Grundlage.

[^snippet]: [Google Search Central: Meta descriptions](https://developers.google.com/search/docs/appearance/snippet)
[^appearance]: [Google Search Central: Search appearance and structured data](https://developers.google.com/search/docs/appearance)
[^manifest]: [MDN: Web application manifest](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/index.html)
[^gsc-auth]: [Google Search Console API: Voraussetzungen und Berechtigungen](https://developers.google.com/webmaster-tools/v1/prereqs)
[^recrawl]: [Google Search Central: URLs erneut crawlen lassen](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
