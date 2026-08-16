---
type: canonical
status: canonical
updated: 2026-08-16
depends_on:
  - "[[70-QA/Test Matrix]]"
---

# Quality Gates

Ein Projekt ist nur fertig, wenn jedes zutreffende Gate belegt ist. `N/A` braucht Begründung.

## G0 Scope

- [ ] eigener Ordner unter `../projekte/<Projektname>/`; PROJECT.md und alle Pflichtinventare vorhanden und verlinkt
- [ ] Projekt-Master-Spec vollständig; Annahmen und Nicht-Ziele markiert
- [ ] Anzahl der Websites entspricht dem Auftrag; Quelle im Auftragstext ist in `PROJECT.md` zitiert. Ohne Angabe im Auftrag genau eine Website
- [ ] Sitemap, Seitenverträge und primäre Nutzerflüsse aktuell; jede gebaute Website enthält eine verlinkte Startseite und die vollständigen erforderlichen Unterseiten. One-Page/Anker allein ist nicht zulässig.
- [ ] echte Inhalte oder klar markierte Drafts, keine Produktions-Platzhalter
- [ ] Inspirationsmatrix mit Auswahl oder begründeter Ablehnung; statische und interaktive Evidenz getrennt
- [ ] die beauftragte Anzahl vollständiger Websites unter `site/` beziehungsweise `versions/`, bei mehreren mit klaren UI-, Unterseiten- und Motion-Unterschieden, gleichem Scope und eigener SEO-Auslieferung; jede startet mit allen Routen auf ihrem eigenen geprüften Port
- [ ] bei Relaunch: alte Website, externe Fundstellen, Maps-/Unternehmensprofil, Social Profiles und Dokumente inventarisiert; Konflikte markiert
- [ ] gefundenes Firmenlogo in jeder gebauten Website sichtbar eingesetzt und der Einsatzort dokumentiert, oder ausdrücklich festgehalten, dass kein Logo gefunden wurde

## G1 Design

- [ ] Design Direction und Tokens für Farbe, Typo, Spacing, Grid, Radius, Shadow, Motion
- [ ] **Tokenvertrag vollständig** nach [[20-Design/Color System#Tokenvertrag]]: jede Pflichtrolle hat einen gesetzten Wert in genau einer Tokenquelle, einschließlich `bg`, `surface`, `surface-alt`, drei Textstufen, `border`, `border-hover`, `accent`, `accent-subtle`, `accent-contrast`, `focus` und der semantischen Rollen; Light und Dark getrennt kuratiert
- [ ] **Formsprache kalibriert**: alle Radien auf den vier Stufen aus [[20-Design/Typography Layout and Spacing#Radiusskala]], genau eine Rahmenstärke, genau eine Schattenstufe und diese nur bei Hover, Fokus oder echten Ebenen; im Ruhezustand keine Fläche mit Schatten
- [ ] **Kartenrezept angewandt** nach [[30-Frontend/Components and UI States#Kartenrezept]]: Hover wechselt Rahmen und Position, nicht nur Farbe; kein Hover-Lift auf nicht klickbaren Flächen; alle Kartenzustände einschließlich Laden und Leerzustand gestaltet
- [ ] **Kopfzeilenrezept angewandt** nach [[30-Frontend/Components and UI States#Rezept der durchscheinenden Kopfzeile]]: Kontrast gegen den ungünstigsten darunterliegenden Inhalt gemessen, deckender `@supports`-Fallback vorhanden
- [ ] **Bewegungswerte gesetzt** nach [[20-Design/Motion and Interaction#Standardrezepte mit Werten]]: Zeit- und Kurvensatz als Tokens, Reveal hält seinen Endzustand, Startversatz höchstens 24 Pixel, Zeichenauftakt höchstens einmal je Website, jede Abweichung mit Grund im Motion Inventory
- [ ] negatives Tracking nur auf den großen Typostufen; Werte, Tags und Zahlen in der Mono-Familie mit tabellarischen Ziffern
- [ ] **UI UX Pro Max wurde für diese Website ausgeführt**, je gebauter Website getrennt und mit Datum belegt; ohne diesen Nachweis ist die Website nicht abgenommen, siehe [[00-Start/04 Plugins and Skills#Auslösebedingung]]
- [ ] Leitbenchmark aus [[20-Design/Interface Benchmarks]] benannt; übernommene und ausdrücklich nicht übernommene Elemente dokumentiert
- [ ] keine Retro-Anmutung nach [[20-Design/Typography Layout and Spacing#Retro-Verbot]]; Schriftwahl mit Herleitung dokumentiert
- [ ] Bildplan nach [[20-Design/Imagery and AI Editing]] erfüllt: jedes Bild mit Rolle, geprüftem Winkel, Ausschnitt, Hintergrund und Auflösung; Serienkonsistenz belegt; Bearbeitungsschritte im Asset Register
- [ ] alle `ai-placeholder`-Bilder gelistet, mit Prompt und Ersetzungshinweis übergeben, ohne sichtbare Kennzeichnung auf der Website; keine leere oder graue Bildstelle im Layout
- [ ] Informations- und Textbudget je Route nach [[10-Strategy/Information Density and Mobile Clarity]] eingehalten; Prüffragen dieser Notiz durchlaufen
- [ ] **Copy-Prüfung nach [[10-Strategy/Website Copy]]** je gebauter Website bestanden: keine Meta-Sätze über die eigene Seite, keine sichtbaren Pflegedaten, keine Negativabgrenzung, keine Selbstverständlichkeit, kein verbloses Statement unter einer Überschrift, keine unbegründete Dreierfigur, kein Semikolon und kein Gedankenstrich als Einschub; auf jeder primären Route mindestens eine Stelle mit zusammenhängenden ganzen Sätzen
- [ ] bei mehreren Websites: Unterscheidungsmatrix nach [[20-Design/Design Direction#Stilabstand bei mehreren Websites]] in `PROJECT.md` ausgefüllt und in mindestens vier Merkmalen tatsächlich umgesetzt
- [ ] mindestens ein interaktives Kernmodul je Landing Page nach [[20-Design/Motion and Interaction#Interaktives Kernmodul]], mit realen Daten, Tastaturbedienung, Zuständen und statischer Alternative
- [ ] UI UX Pro Max Abfrage und Auswahl dokumentiert; die Pflicht-Detailabfragen zu `landing`, `style`, `color`, `typography`, `ux`, `gsap` und Stack liegen mit Datum vor; projektspezifische Abweichungen begründet
- [ ] Referenzrecherche im Pflichtumfang: mindestens acht erneut angesehene Referenzen, mindestens zwei benannte Negativreferenzen, bei mehreren Websites je Website eine eigene Referenzkombination
- [ ] pen.dev Einsatz oder Verzicht entschieden; verwendete `.pen`-Dateien versioniert und visuell geprüft
- [ ] Anti-Slop-Review bestanden; keine unbegründeten Standardsektionen
- [ ] **Impeccable KI-Detail-Review je gebauter Website** durchgeführt, mit Datum, Befundliste und Umsetzungsstand dokumentiert, siehe [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review]]
- [ ] kein Kicker über einer Überschrift auf keiner Seite
- [ ] Kopfzeile mit höchstens sechs Navigationspunkten, bei 1280, 1440 und 1920 Pixel einzeilig, mit der längsten realen Beschriftung geprüft
- [ ] keine verbrauchte Farbwelt als dominante Fläche; jede Farbrolle hat eine benannte Herleitung
- [ ] Auftaktkomposition und Überschriftenanordnung sind bewusst gewählt und im Design Contract begründet; die Landing Page folgt [[20-Design/Design Direction#Landing Page]]
- [ ] Mobile, Tablet, Desktop, Zoom und lange Inhalte geprüft
- [ ] alle UI-Zustände gestaltet
- [ ] Motion-Referenzen interaktiv geprüft; Reduced-Motion- und Medienfallback belegt
- [ ] jede Website erfüllt das hohe Motion-Niveau aus [[20-Design/Motion and Interaction]]: eigene Route-zu-Route-Choreografie, Motion Inventory, mindestens zwölf sichtbare Bewegungsentscheidungen und pro primärer Inhaltsroute eine Scrollsequenz plus zwei weitere differenzierte Scroll-/In-View-Bewegungen
- [ ] **`review-animations` je gebauter Website ausgeführt** und mit Datum, Befundliste und Umsetzungsstand dokumentiert, siehe [[00-Start/04 Plugins and Skills#Review Animations]]; offene Befunde sind im Decision Log begründet
- [ ] Bewegungsentscheidungen enthalten Zweck, Häufigkeit, Easing/Dauer oder Scroll-Range, Eingabemethode, Unterbrechbarkeit und Reduced-Motion-Fallback; keine Animation verzögert häufige Tastaturbedienung

## G2 Funktion

- [ ] jeder Link, Button, Tab, Modal, Accordion, Carousel, Formular und Social Link funktioniert
- [ ] Loading, Empty, Error, Offline, Permission und Retry geprüft
- [ ] Browser Back/Forward, Deep Links und Refresh erhalten erwarteten Zustand
- [ ] keine Console Errors, Hydration Warnings oder unhandled Promises

## G3 Accessibility

- [ ] WCAG 2.2 AA Ziel geprüft; automatischer Scan ohne kritische Funde
- [ ] Tastatur, Fokus, Screenreader, Reflow 320px, Zoom 200/400 Prozent
- [ ] Kontrast, Alt-Texte, Labels, Fehlermeldungen, Reduced Motion
- [ ] Accessibility-Information/Erklärung korrekt, falls erforderlich

## G4 Performance

- [ ] budgets in CI eingehalten
- [ ] LCP-, INP- und CLS-Risiken auf realistischem Mobilprofil geprüft
- [ ] Bilder, Fonts, JS, Third Parties, Cache und die vollständige Motion-Choreografie auf realen Routen optimiert
- [ ] Felddaten/RUM und Alert nach Launch vorgesehen

## G5 Security und Daten

- [ ] Bedrohungsmodell, AuthZ/RLS und negative Rollentests
- [ ] Servervalidierung, Rate Limits, Kostenlimits, Secrets und Header
- [ ] Session nicht in LocalStorage; CSRF/CORS/CSP geprüft
- [ ] Webhooks signiert, dedupliziert, idempotent und fehlertolerant
- [ ] Dependency-, Secret- und Vulnerability-Scan

## G6 Legal

- [ ] Betreiber, Zielmärkte und Seitentyp rechtlich klassifiziert
- [ ] Impressum, Privacy, Consent, Barrierefreiheit und Verbraucherpflichten entschieden
- [ ] Dateninventar stimmt exakt mit Code, Tags, Logs und Dienstleistern überein
- [ ] `SOURCE-RIGHTS-REVIEW.md` vollständig; tatsächlicher Einsatz, Quelle und offene Hinweise für den Nutzer/Owner dokumentiert, ohne Ersatz, Auslassung, Build-Sperre oder KI-Freigabeentscheidung
- [ ] Asset Register vollständig; jeder verwendete Eintrag mit tatsächlichem Einsatz und späterem Owner-Reviewstatus dokumentiert
- [ ] altes Impressum/Privacy nur als Faktenquelle; neue Texte entsprechen Betreiber, Markt, Code, Tags und Dienstleistern
- [ ] Rechtstexte als prüfpflichtige Entwürfe und tatsächliche Asset-/Quellenhinweise für die spätere Entscheidung des Nutzers/Owners dokumentiert; keine KI-Go-/No-Go-Entscheidung

## G7 SEO und Marke

- [ ] in jeder gebauten Website und auf jeder indexierbaren Unterseite: kurze Titel ohne `|`, einzigartige Meta Descriptions, Canonical und bewusster Indexstatus
- [ ] Favicon-Set, OG Asset, `lang`, structured data nur wenn wahr
- [ ] je gebauter Website: Sitemap.xml, robots, Redirects, 404 und interne Links; alle Unterseiten sind crawlbar und SEO-vollständig
- [ ] Google Maps, Anfahrt und verifizierte offizielle Unternehmens-/Social-Profile funktionieren; zeitkritische Maps-Hinweise wie Öffnungszeiten, Reviews oder Stoßzeiten sind primärquellenbestätigt oder nicht veröffentlicht
- [ ] keine Fake-Claims, Testimonials, Logos oder Zahlen

## G8 Betrieb

- [ ] Ein-Klick-Start für geforderte OS, Healthchecks und verständliche Logs
- [ ] Dependency-/Serverliste, `.env.example`, Deploy, Migration und Rollback
- [ ] Monitoring, Alerts, Backups und Restore-Test
- [ ] Subscription-Löschfluss, Datenlöschung und Supportpfad getestet
- [ ] Changelog und Übergabe aktuell
