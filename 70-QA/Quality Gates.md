---
type: canonical
status: canonical
updated: 2026-08-19
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
- [ ] die beauftragte Anzahl vollständiger Websites unter `site/` beziehungsweise `versions/`, bei mehreren mit eigenständiger kohärenter Richtung und Unterschieden auf mindestens fünf wirksamen Achsen bei gleichem Scope; auf `217.154.218.30` über `johannstein.com/dev` ohne Projektport erreichbar, sonst auf eigenem geprüftem lokalen Port
- [ ] bei Relaunch: alte Website, externe Fundstellen, Maps-/Unternehmensprofil, Social Profiles und Dokumente inventarisiert; Konflikte markiert
- [ ] gefundenes Firmenlogo in jeder gebauten Website sichtbar eingesetzt und der Einsatzort dokumentiert, oder ausdrücklich festgehalten, dass kein Logo gefunden wurde
- [ ] je gebauter Website eigenes `release-readiness/<website-slug>.md` nach [[60-Operations/Release Readiness Register]] vorhanden und seit Projektbeginn fortgeschrieben

## G1 Design

- [ ] Design Direction und Tokens für Farbe, Typo, Spacing, Grid, Radius, Shadow, Motion
- [ ] **Tokenvertrag vollständig** nach [[20-Design/Color System#Tokenvertrag]]: jede Pflichtrolle hat einen gesetzten Wert in genau einer Tokenquelle, einschließlich `bg`, `surface`, `surface-alt`, drei Textstufen, `border`, `border-hover`, `accent`, `accent-subtle`, `accent-contrast`, `focus` und der semantischen Rollen; Light und Dark getrennt kuratiert
- [ ] **H0-Handwerksuntergrenze erfüllt** nach [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]]: vollständige Zustände, sichtbarer Fokus, Kontextkontrast, klare Hierarchie und ein konsistentes System innerhalb der Website
- [ ] **variable Formsprache dokumentiert**: Radiusskala, Rahmenbehandlung, Flächenlogik, Tiefe, Karten-/Zeilen-/Tabellen-/Listenrepertoire, Kopf- und Fußbereich, Chrome, Zweitschrift und Motion sind je Website entschieden; B5-Muster nur bei bewusster Wahl
- [ ] abgegrenzte Inhaltsflächen erfüllen [[30-Frontend/Components and UI States#Kartenentscheidung]]: interaktive und nicht interaktive Flächen verhalten sich unterscheidbar; Laden und Leerzustand sind gestaltet
- [ ] Kopfzeileninventar und -anordnung sind website-spezifisch; eine durchscheinende Kopfzeile erfüllt nur bei Wahl die Fallback-Regeln aus [[30-Frontend/Components and UI States#Option durchscheinende Kopfzeile]]
- [ ] eigener Zeit- und Kurvensatz als Tokens; die Beispiele aus [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] sind nur bei dokumentierter Übernahme Prüfmaß
- [ ] negatives Tracking nur auf großen Typostufen; tabellarische Ziffern für vergleichbare Zahlen; Mono nur in den begründeten technischen Rollen der Website, nie automatisch für Anschriften, Fließtext, Sektionstitel, Zeiten, Tags oder Abschnittsnummern
- [ ] **UI UX Pro Max wurde für diese Website ausgeführt** und unter `design-system/<website-slug>/MASTER.md` getrennt persistiert; keine projektweiten Global Rules ziehen Fassungen gleich
- [ ] Leitbenchmark aus [[20-Design/Interface Benchmarks]] benannt; übernommene und ausdrücklich nicht übernommene Elemente dokumentiert
- [ ] Schriftwahl, Rollen, Lizenz, Lesbarkeit und beabsichtigter Zeitbezug nach [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]] dokumentiert
- [ ] Bildplan nach [[20-Design/Imagery and AI Editing]] erfüllt: jedes Bild mit Rolle, geprüftem Winkel, Ausschnitt, Hintergrund und Auflösung; Serienkonsistenz belegt; Bearbeitungsschritte im Asset Register
- [ ] alle `ai-placeholder`-Bilder gelistet, mit Prompt und Ersetzungshinweis übergeben, ohne sichtbare Kennzeichnung auf der Website; keine leere oder graue Bildstelle im Layout
- [ ] Informations- und Textbudget je Route nach [[10-Strategy/Information Density and Mobile Clarity]] eingehalten; Prüffragen dieser Notiz durchlaufen
- [ ] **Copy-Prüfung nach [[10-Strategy/Website Copy]]** je gebauter Website bestanden: keine Meta-Sätze über die eigene Seite, keine sichtbaren Pflegedaten, keine Negativabgrenzung, keine Selbstverständlichkeit, kein verbloses Statement unter einer Überschrift, keine unbegründete Dreierfigur, kein Semikolon und kein Gedankenstrich als Einschub; auf jeder primären Route mindestens eine Stelle mit zusammenhängenden ganzen Sätzen
- [ ] bei mehreren Websites: Unterscheidungsmatrix vor UI-Code ausgefüllt; jede Website besitzt eine eigenständige kohärente Richtung und unterscheidet sich auf mindestens fünf für den Auftrag wirksamen Achsen
- [ ] bei vorhandenen Vorgängerfassungen: Übernahmeregister ausgefüllt; wiederholte Leitmotive, Fassungsnamen, Signalfarben oder primäre Beweisformen sind als bewusste sachliche Entscheidung dokumentiert
- [ ] primäre Beweisform je Landing Page dokumentiert; wenn ein interaktives Kernmodul gewählt wurde, erfüllt es [[20-Design/Motion and Interaction#Interaktives Kernmodul]] mit realen Daten, Tastaturbedienung, Zuständen und statischer Alternative
- [ ] UI UX Pro Max Abfrage und Auswahl dokumentiert; die Pflicht-Detailabfragen zu `landing`, `style`, `color`, `typography`, `ux`, `gsap` und Stack liegen mit Datum vor; projektspezifische Abweichungen begründet
- [ ] Referenzrecherche im Pflichtumfang: mindestens acht erneut angesehene Referenzen, mindestens zwei benannte Negativreferenzen, bei mehreren Websites je Website eine eigene Referenzkombination
- [ ] pen.dev Einsatz oder Verzicht entschieden; verwendete `.pen`-Dateien versioniert und visuell geprüft
- [ ] Anti-Slop-Review bestanden; keine unbegründeten Standardsektionen
- [ ] **Impeccable KI-Detail-Review je gebauter Website** durchgeführt, mit Datum, Befundliste und Umsetzungsstand dokumentiert, siehe [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review]]
- [ ] keine redundanten, rein dekorativen Kicker; echte Metainformation besitzt eine begründete, zugängliche Hierarchiestufe
- [ ] Kopfzeileninventar und Navigationsmuster sind aus der Informationsarchitektur begründet; bei 320, 375, 768, 1280 und 1920 Pixel, langen realen Beschriftungen, großer Systemschrift und 200 Prozent Zoom entstehen kein zufälliger Umbruch, Beschnitt oder Überlauf
- [ ] Logos, Wortzeichen und Controls behalten an jedem Prüfbreakpoint ihr Seitenverhältnis und werden nicht beschnitten
- [ ] jede Farbrolle hat eine benannte Herleitung; häufige Paletten sind bewusst gewählt statt reflexhaft übernommen
- [ ] Auftaktkomposition und Überschriftenanordnung sind bewusst gewählt und im Design Contract begründet; die Landing Page folgt [[20-Design/Design Direction#Landing Page]]
- [ ] **echte Darstellung** auf Mobile, Tablet, Desktop, Zoom und mit langen Inhalten geprüft; Screenshots oder gleichwertige Rendernachweise liegen für die vorgeschriebenen Prüfbreiten vor
- [ ] kann in der Abnahmeumgebung keine echte Darstellung erzeugt werden, ist dies **vor der Lieferung ein Blocker**. Textanalyse, bestandene Tokenpaare oder ein nachträglicher Hinweis ersetzen den Render nicht
- [ ] alle UI-Zustände gestaltet
- [ ] Motion-Referenzen interaktiv geprüft; Reduced-Motion- und Medienfallback belegt
- [ ] Motion-Budget `none | low | medium | high` ist begründet; jede tatsächlich eingesetzte relevante Bewegung steht im Motion Inventory, hat einen Zweck und besteht Reduced-Motion-, Eingabe- und Performanceprüfung
- [ ] **`review-animations` je gebauter Website ausgeführt** und mit Datum, Befundliste und Umsetzungsstand dokumentiert, siehe [[00-Start/04 Plugins and Skills#Review Animations]]; offene Befunde sind im Decision Log begründet
- [ ] Bewegungsentscheidungen enthalten Zweck, Häufigkeit, Easing/Dauer oder Scroll-Range, Eingabemethode, Unterbrechbarkeit und Reduced-Motion-Fallback; keine Animation verzögert häufige Tastaturbedienung

## G2 Funktion

- [ ] jeder Link, Button, Tab, Modal, Accordion, Carousel, Formular und Social Link funktioniert
- [ ] Loading, Empty, Error, Offline, Permission und Retry geprüft
- [ ] Browser Back/Forward, Deep Links und Refresh erhalten erwarteten Zustand
- [ ] keine Console Errors, Hydration Warnings oder unhandled Promises
- [ ] jedes Formular und jeder Nachrichtenfluss erreicht nachweislich seinen vorgesehenen Produktions-Endpunkt; bei E-Mail liegt eine eindeutige Testanfrage im realen Zielpostfach oder verbindlichen Betreiber-Posteingang, Fehlerfall und Retry/Alert sind belegt

## G3 Accessibility

- [ ] WCAG 2.2 AA Ziel geprüft; automatischer Scan ohne kritische Funde
- [ ] Tastatur, Fokus, Screenreader, Reflow 320px, Zoom 200/400 Prozent
- [ ] **Kontrast im Kontext**: jede tatsächlich im Markup vorkommende Komponentenvariante wird gegen jede ihrer realen Untergrundflächen geprüft, einschließlich invertierter/dunkler Bänder, Bildüberlagerungen, Hover, Fokus, Disabled und Fehlervarianten; keine handverlesene Liste isolierter Tokenpaare
- [ ] Alt-Texte, Labels, Fehlermeldungen und Reduced Motion
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
- [ ] Produktionsentsperrung nach [[60-Operations/Release Readiness Register#Produktionsentsperrung und Indexierung]] geprüft: kein Preview-`auth_basic`, kein blockierender `X-Robots-Tag` oder Robots-Meta, kein `Disallow: /`, Canonicals und Sitemap ausschließlich auf Produktions-HTTPS
- [ ] Search-Console-Property, Sitemap und gegebenenfalls API getrennt geprüft; bei API-Nutzung OAuth-/Dienstkonto-Berechtigung und echter Query-Nachweis vorhanden

## G8 Betrieb

- [ ] auf `217.154.218.30`: Eintrag und alle Routen über `johannstein.com/dev` geprüft, kein fester Projektport und kein neues `start-local.sh`; auf anderen Rechnern Ein-Klick-Start für geforderte OS, Healthchecks und verständliche Logs
- [ ] bei Owner-Hosting: `tenant.json` und `_hosting` bestehen [[80-Templates/Owner Hosting Website Contract]]; unbekannte oder gesperrte JSON-Pointer werden serverseitig abgewiesen
- [ ] bei Owner-Hosting: Contract-Plan belegt Erhalt oder explizite Migration aller vorhandenen Owner-Werte; offene Entwürfe alter Vertragsversionen sind behandelt
- [ ] bei Owner-Hosting: Hostname löst serverseitig genau einen Mandanten auf; negative Cross-Tenant-Tests für Inhalte, Assets, Builds, Releases, Nachrichten und Integrationen bestehen
- [ ] bei Owner-Hosting: statische öffentliche Website bleibt bei Dashboard-/API-Ausfall erreichbar; Worker baut isoliert, Buildfehler verändert weder aktive Inhaltsrevision noch Release; atomarer Publish, vollständiger Rollback und 503-Wartungsmodus nach [[60-Operations/Owner Hosting and Dashboard]] geprüft
- [ ] bei Deployment-Slots: ein Drop merkt nur vor; erst die ausdrückliche zweite Bestätigung baut und schaltet um; öffentlicher Release und Dashboard-Tenant wechseln atomar gemeinsam
- [ ] bei Deployment-Slots: Slotwechsel verändert weder Quellprojekt noch Katalogstatus der abgelegten Fassung; Archivfassungen bleiben im Archiv
- [ ] bei Deployment-Slots: Sitzungen sind an den Tenant gebunden und nach einem Wechsel wertlos; Suffix-Hosts und gefälschte `Host`-Header werden vor jeder Tenant-Abfrage abgewiesen
- [ ] bei Legacy-Adaptern: Quellhash ohne Buildausgaben vor und nach mehreren Builds identisch, vorhandenes `dist/` der Quelle unverändert; fest im Quelltext hinterlegte Kontaktdaten sind als Warnung gemeldet statt stillschweigend hingenommen
- [ ] bei Staging-Domains: Basic Auth aktiv, `X-Robots-Tag: noindex, nofollow, noarchive` und sperrende `robots.txt` ausgeliefert, ACME-Challenge auf Port 80 unverändert erreichbar
- [ ] bei Websites ohne Editorvertrag: Dashboard läuft schreibgeschützt; bearbeitbare Felder werden nicht aus Text oder HTML erraten
- [ ] Dependency-/Serverliste, `.env.example`, Deploy, Migration und Rollback
- [ ] Monitoring, Alerts, Backups und Restore-Test
- [ ] Subscription-Löschfluss, Datenlöschung und Supportpfad getestet
- [ ] Changelog und Übergabe aktuell
- [ ] jedes Release-Readiness-Register gegen Repository, ausgelieferten Produktionskandidaten und externe Infrastruktur abgeglichen; offene `P0` sichtbar, offene `P1` mit datierter Owner-Entscheidung
