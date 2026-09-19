---
type: canonical
status: canonical
updated: 2026-09-19
depends_on:
  - "[[70-qa/test-matrix.md]]"
---

# Quality Gates

Ein Projekt ist nur fertig, wenn jedes zutreffende Gate belegt ist. `N/A` braucht Begründung.

## G0 Scope

In der Fast Lane nach [[00-start/05-web-product-workflow.md#Bahnwahl: Fast Lane und Full Lane]] gilt `G0` **verkürzt**: die ersten fünf Punkte plus Logo und Release-Readiness. Die Punkte zu Referenzmodus, mehreren Fassungen und Relaunch-Inventar entfallen, weil ihre Auslöser dort definitionsgemäß nicht vorliegen. In der Full Lane gilt die vollständige Liste.

- [ ] eigener Ordner unter `../projekte/<Projektname>/`; PROJECT.md und alle Pflichtinventare vorhanden und verlinkt
- [ ] Projekt-Master-Spec vollständig; Annahmen und Nicht-Ziele markiert
- [ ] Anzahl der Websites entspricht dem Auftrag; Quelle im Auftragstext ist in `PROJECT.md` zitiert. Ohne Angabe im Auftrag genau eine Website
- [ ] Sitemap, Seitenverträge und primäre Nutzerflüsse aktuell; jede gebaute Website enthält eine verlinkte Startseite und die vollständigen erforderlichen Unterseiten. One-Page/Anker allein ist nicht zulässig.
- [ ] echte Inhalte oder klar markierte Drafts. Platzhalter sind **während des Builds erlaubt** nach [[00-start/05-web-product-workflow.md#Platzhalter sind erlaubt]]; zur Abnahme sind sie entweder ersetzt oder stehen vollzählig als offener Punkt im Release-Readiness-Register. Ein unbekannter Platzhalter ist der Befund, nicht der bekannte
- [ ] Referenzmodus je Website dokumentiert; bei genau einer Website keine automatisch ausgewählte Live-Leitreferenz, bei mehreren genau eine referenzgeführte Fassung bei starker Passung und alle übrigen als Eigenentwürfe hergeleitet; eine Ausnahme ohne Referenz enthält die dokumentierte erfolglose Suche; nutzer-vorgegebene Referenzen gesondert markiert
- [ ] die beauftragte Anzahl vollständiger Websites unter `site/` beziehungsweise `versions/`, bei mehreren mit eigenständiger kohärenter Richtung und Unterschieden auf mindestens fünf wirksamen Achsen bei gleichem Scope; auf `217.154.218.30` über `johannstein.com/dev` ohne Projektport erreichbar, sonst auf eigenem geprüftem lokalen Port
- [ ] bei Relaunch: alte Website, externe Fundstellen, Maps-/Unternehmensprofil, Social Profiles und Dokumente inventarisiert; Konflikte markiert
- [ ] gefundenes Firmenlogo in jeder gebauten Website sichtbar eingesetzt und der Einsatzort dokumentiert, oder ausdrücklich festgehalten, dass kein Logo gefunden wurde
- [ ] je gebauter Website eigenes `release-readiness/<website-slug>.md` nach [[60-operations/release-readiness-register.md]] vorhanden und seit Projektbeginn fortgeschrieben

## G1 Design

`G1` prüft das **Ergebnis**, nicht das Werkzeug, das es erzeugt hat. Welcher Skill, welches Plugin und welche Maschine im Spiel waren, ist für die Abnahme ohne Belang; entscheidend ist, dass die folgenden Eigenschaften am laufenden Build nachweisbar sind. Die Nachweisform je Punkt ist der Render, die Tokenquelle oder der Design Contract, nicht ein Werkzeugprotokoll.

### Kernprüfung

Diese fünf Punkte tragen das Gate. Fällt einer, ist `G1` nicht erfüllt, unabhängig davon, wie die Website entstanden ist.

- [ ] **Tokenvertrag vollständig und gerendert**: jede Pflichtrolle aus [[20-design/color-system.md#Tokenvertrag]] hat einen gesetzten Wert in genau einer Tokenquelle, für Licht und Dunkel getrennt kuratiert, und ist an realem Text angesehen worden
- [ ] **Zustände vollständig**: jede Interaktion zeigt ihre anwendbaren Zustände nach [[30-frontend/components-and-ui-states.md]] — Default, Hover, Focus, Active, Disabled, Loading, Success, Error, Empty, Offline; sichtbarer Fokus, unterscheidbares Verhalten interaktiver und nicht interaktiver Flächen
- [ ] **Type Ramp vorhanden und angewandt**: die Stufen sind benannt, haben je eine Aufgabe, benachbarte Stufen unterscheiden sich um mindestens den Faktor 1,25, und die Zuordnung ist auf jeder primären Route eingehalten
- [ ] **Kontrast in beiden Themes**: jede Text-auf-Fläche-Kombination des Tokenvertrags erfüllt den Zielstandard aus [[30-frontend/accessibility.md#Zielstandard]] in Licht **und** Dunkel, einschließlich der dritten Textstufe auf `surface-alt` und der Zustände von `accent`
- [ ] **echte Darstellung geprüft**: ganzseitige Renders bei 375 und 1280 Pixel liegen vor, mit langen Inhalten, Zoom und Fehlerzuständen; ein nicht renderbarer Build ist vor der Lieferung ein Blocker, den Textanalyse nicht ersetzt

### Handwerk und Komposition

- [ ] Design Direction und Tokens für Farbe, Typo, Spacing, Grid, Radius, Shadow, Motion
- [ ] **Tokenvertrag vollständig** nach [[20-design/color-system.md#Tokenvertrag]]: jede Pflichtrolle hat einen gesetzten Wert in genau einer Tokenquelle, einschließlich `bg`, `surface`, `surface-alt`, drei Textstufen, `border`, `border-hover`, `accent`, `accent-subtle`, `accent-contrast`, `focus` und der semantischen Rollen; Light und Dark getrennt kuratiert
- [ ] **H0-Handwerksuntergrenze erfüllt** nach [[20-design/interface-benchmarks.md#H0 Handwerksuntergrenze]]: vollständige Zustände, sichtbarer Fokus, Kontextkontrast, klare Hierarchie und ein konsistentes System innerhalb der Website
- [ ] **variable Formsprache dokumentiert**: Radiusskala, Rahmenbehandlung, Flächenlogik, Tiefe, Karten-/Zeilen-/Tabellen-/Listenrepertoire, Kopf- und Fußbereich, Chrome, Zweitschrift und Motion sind je Website entschieden; B5-Muster nur bei bewusster Wahl
- [ ] abgegrenzte Inhaltsflächen erfüllen [[30-frontend/components-and-ui-states.md#Kartenentscheidung]]: interaktive und nicht interaktive Flächen verhalten sich unterscheidbar; Laden und Leerzustand sind gestaltet
- [ ] Kopfzeileninventar und -anordnung sind website-spezifisch; eine durchscheinende Kopfzeile erfüllt nur bei Wahl die Fallback-Regeln aus [[30-frontend/components-and-ui-states.md#Option durchscheinende Kopfzeile]]
- [ ] eigener Zeit- und Kurvensatz als Tokens; die Beispiele aus [[20-design/motion-and-interaction.md#Kalibrierte Bewegungsbeispiele]] sind nur bei dokumentierter Übernahme Prüfmaß
- [ ] negatives Tracking nur auf großen Typostufen; tabellarische Ziffern für vergleichbare Zahlen; Mono nur in den begründeten technischen Rollen der Website, nie automatisch für Anschriften, Fließtext, Sektionstitel, Zeiten, Tags oder Abschnittsnummern
- [ ] die Designentscheidungen dieser Website sind unter `design-system/<website-slug>/` getrennt festgehalten; keine projektweiten Global Rules ziehen Fassungen gleich. Wurde UI UX Pro Max genutzt, liegt sein `MASTER.md` dort; wurde die Ersatzstrecke aus [[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]] gefahren, liegt dort deren Nachweis
- [ ] Leitbenchmark aus [[20-design/interface-benchmarks.md]] benannt; übernommene und ausdrücklich nicht übernommene Elemente dokumentiert
- [ ] Schriftwahl, Rollen, Lizenz, Lesbarkeit und beabsichtigter Zeitbezug nach [[20-design/typography-layout-and-spacing.md#Stilzitat und Zeitbezug]] dokumentiert
- [ ] ein starkes vollflächiges Retro- oder Epochenzitat liegt nur bei ausdrücklichem Nutzerwunsch oder tragender Markenevidenz vor; Stilabstand allein ist keine Begründung
- [ ] Bildplan nach [[20-design/imagery-and-ai-editing.md]] erfüllt: jedes Bild mit Rolle, geprüftem Winkel, Ausschnitt, Hintergrund und Auflösung; Serienkonsistenz belegt; Bearbeitungsschritte im Asset Register
- [ ] alle `ai-placeholder`-Bilder gelistet, mit Prompt und Ersetzungshinweis übergeben, ohne sichtbare Kennzeichnung auf der Website; keine leere oder graue Bildstelle im Layout
- [ ] Informations- und Textbudget je Route nach [[10-strategy/information-density-and-mobile-clarity.md]] eingehalten; Prüffragen dieser Notiz durchlaufen
- [ ] **Copy-Prüfung nach [[10-strategy/website-copy.md]]** je gebauter Website bestanden: keine Meta-Sätze über die eigene Seite, keine sichtbaren Pflegedaten, keine Negativabgrenzung, keine Selbstverständlichkeit, kein verbloses Statement unter einer Überschrift, keine unbegründete Dreierfigur, kein Semikolon und kein Gedankenstrich als Einschub; auf jeder primären Route mindestens eine Stelle mit zusammenhängenden ganzen Sätzen
- [ ] bei mehreren Websites: Unterscheidungsmatrix vor UI-Code ausgefüllt; jede Website besitzt eine eigenständige kohärente Richtung und unterscheidet sich auf mindestens fünf für den Auftrag wirksamen Achsen
- [ ] bei vorhandenen Vorgängerfassungen: Übernahmeregister ausgefüllt; wiederholte Leitmotive, Fassungsnamen, Signalfarben oder primäre Beweisformen sind als bewusste sachliche Entscheidung dokumentiert
- [ ] primäre Beweisform je Landing Page dokumentiert; wenn ein interaktives Kernmodul gewählt wurde, erfüllt es [[20-design/motion-and-interaction.md#Interaktives Kernmodul]] mit realen Daten, Tastaturbedienung, Zuständen und statischer Alternative
- [ ] die Entscheidungen zu Landing, Stil, Farbe, Typografie, UX und Motion sind mit Datum und Begründung dokumentiert, gleich ob aus einer Skill-Abfrage oder aus der Ersatzstrecke
- [ ] Referenzrecherche nach [[90-references/reference-research-workflow.md]]: keine Sammlungs-/Galerie-/Award-/Stilbibliotheksseite als Leitreferenz; bei einer Einzelwebsite kein zufällig ausgewähltes Beispiel; bei mehreren Websites genau eine ausgewählte Originalseite für genau eine Fassung, sofern starke Passung gefunden wurde; keine Quervererbung in die Eigenentwürfe
- [ ] pen.dev Einsatz oder Verzicht entschieden; verwendete `.pen`-Dateien versioniert und visuell geprüft
- [ ] Anti-Slop-Review bestanden; keine unbegründeten Standardsektionen
- [ ] **KI-Detail-Review je gebauter Website** durchgeführt, mit Datum, Befundliste und Umsetzungsstand dokumentiert. Der Befundkatalog steht in [[20-design/anti-ai-slop.md#Impeccable KI-Detail-Review]]; ob Impeccable ihn abarbeitet oder der Agent ihn manuell durchgeht, ist für dieses Gate ohne Belang
- [ ] keine redundanten, rein dekorativen Kicker; echte Metainformation besitzt eine begründete, zugängliche Hierarchiestufe
- [ ] Kopfzeileninventar und Navigationsmuster sind aus der Informationsarchitektur begründet; bei 320, 375, 768, 1280 und 1920 Pixel, langen realen Beschriftungen, großer Systemschrift und 200 Prozent Zoom entstehen kein zufälliger Umbruch, Beschnitt oder Überlauf
- [ ] Logos, Wortzeichen und Controls behalten an jedem Prüfbreakpoint ihr Seitenverhältnis und werden nicht beschnitten
- [ ] jede Farbrolle hat eine benannte Herleitung; häufige Paletten sind bewusst gewählt statt reflexhaft übernommen
- [ ] Auftaktkomposition und Überschriftenanordnung sind bewusst gewählt und im Design Contract begründet; Angebot, konkreter Inhaltsanker und primäre Handlung bilden eine gemeinsame Komposition, ein Bild ist optional; die Landing Page folgt [[20-design/landing-page-craft.md]]
- [ ] **die sechs Auftaktrollen** aus [[20-design/landing-page-craft.md#Der Auftakt: sechs Rollen, eine Komposition]] sind je Landing Page benannt besetzt, insbesondere Beweisanker und Fortschritt; die gewählte Komposition stammt aus dem [[20-design/landing-page-craft.md#Auftakt-Repertoire]] und ist begründet
- [ ] die Abschnittsfolge der Landing Page ist aus den realen Nutzerfragen dieser Zielgruppe hergeleitet und nicht aus der Blockkette Hero, drei Karten, Logo-Wand, Stimmen, Preise, FAQ; jeder Abschnitt beantwortet genau eine Frage
- [ ] zwei bis drei verschiedene Überschriftenanordnungen je Seite, jede der Aufgabe ihres Abschnitts entsprechend; benachbarte Typostufen unterscheiden sich um mindestens den Faktor 1,25; der Abstand über einer Überschrift ist größer als darunter
- [ ] Kopfzeilenrolle der Landing Page entschieden: Einzweckseite oder Unternehmensstartseite, Form aus dem [[30-frontend/components-and-ui-states.md#Kopfzeilen-Repertoire]], Höhenanteil auf 375 Pixel geprüft, höchstens eine primäre Aktion in der Kopfzeile
- [ ] **Slop-Signaturen durchgegangen** nach [[20-design/anti-ai-slop.md#Slop-Signaturen]]; jede bewusst eingesetzte Signatur ist im Design Contract begründet
- [ ] Signaturdetail je Website benannt, hergeleitet und mit seinen Wiederholungsorten dokumentiert
- [ ] typografischer Feinschliff nach [[20-design/typography-layout-and-spacing.md#Typografischer Feinschliff]] geprüft: Umbruch der H1, Schusterjungen, optischer Randausgleich, Ziffernform, Zeilenlänge, Mindestgrößen
- [ ] die erste Bildschirmhöhe zeigt auf 375 Pixel Angebot, Zielgruppe beziehungsweise Ort und die primäre Handlung, und sie sieht nicht abgeschlossen aus; der Übergang in den Folgeinhalt ist sichtbar
- [ ] das Auftaktmedium ist vorrangig geladen; kein Inhalt der Landing Page bleibt bis zum Ende einer Einblendung unsichtbar
- [ ] die Prüffragen aus [[20-design/landing-page-craft.md#Prüffragen vor der Abnahme]] sind je gebauter Landing Page am laufenden Build beantwortet
- [ ] die vollständige semantische H1 ist bei 320, 375, 768, 1280 und 1440 Pixel, 200 Prozent Zoom und großer Systemschrift ohne Anschnitt, Maske, Überlagerung oder Kollision mit der realen klebenden Kopfzeile lesbar
- [ ] auf Mobil beginnt spätestens innerhalb der zweiten Bildschirmhöhe sichtbar die nächste reale Nutzerfrage oder der erste konkrete Beweis; Schriftgröße, Kontaktmetadaten, Dekoration und ungenutzter Weißraum halten den Seitenfortschritt nicht auf
- [ ] **Stilkachel `D0` gerendert und angesehen** (Full Lane; in der Fast Lane deckt die Kernprüfung dieselben Eigenschaften ab) nach [[20-design/visual-iteration-loop.md#D0 Stilkachel: das visuelle Ziel vor dem ersten Bauteil]]: jede Pflichtfarbrolle mit ihrem realen Text in Licht und Dunkel, Type Ramp an echtem Text, Radius-/Rahmen-/Tiefengrammatik, Aktionen in allen Zuständen, gewählte Inhaltsgrundform mit Leer- und Ladezustand, Signaturdetail; Befunde daran vor dem ersten Auftakt behoben
- [ ] **Auftaktfeld gebaut** (Fast Lane: zwei Fassungen): zwei bis drei Auftaktfassungen mit verschiedenen Kompositionen und denselben realen Inhalten liegen vor, wurden nebeneinander bei 375 und 1280 Pixel beurteilt; Wahl, verworfene Fassungen und Grund stehen im Design Contract, siehe [[20-design/visual-iteration-loop.md#Divergenz vor Konvergenz: das Auftaktfeld]]
- [ ] **Visual Iteration Loop durchlaufen**: in der Full Lane mindestens die Durchgänge `D1`, `D2` und `D3` aus [[20-design/visual-iteration-loop.md#Pflichtdurchgänge]], in der Fast Lane ein Durchgang, je gebauter Website, jeweils mit Datum, benannten Stopps, schriftlicher Befundliste und der daraufhin vorgenommenen Änderung. Renders ohne zugehörige Befundliste erfüllen dieses Gate nicht
- [ ] **echte Darstellung** auf Mobile, Tablet, Desktop, Zoom und mit langen Inhalten geprüft; die Rendernachweise sind **ganzseitig** und nicht nur der sichtbare Auftakt, damit Überlauf, Kollision und Fehlerzustände unterhalb der Falz sichtbar werden
- [ ] kann in der Abnahmeumgebung keine echte Darstellung erzeugt werden, ist dies **vor der Lieferung ein Blocker**. Textanalyse, bestandene Tokenpaare oder ein nachträglicher Hinweis ersetzen den Render nicht
- [ ] alle UI-Zustände gestaltet
- [ ] Motion-Referenzen interaktiv geprüft; Reduced-Motion- und Medienfallback belegt
- [ ] Motion-Budget `none | low | medium | high` ist begründet; jede tatsächlich eingesetzte relevante Bewegung steht im Motion Inventory, hat einen Zweck und besteht Reduced-Motion-, Eingabe- und Performanceprüfung
- [ ] jede eingesetzte Bewegung ist gegen die zehn Prüfstandards aus [[00-start/04-plugins-and-skills.md#Review Animations]] geprüft und mit Datum, Befundliste und Umsetzungsstand dokumentiert; ob `review-animations` das leistet oder die Liste manuell durchlaufen wird, ist für dieses Gate ohne Belang
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
- [ ] Produktionsentsperrung nach [[60-operations/release-readiness-register.md#Produktionsentsperrung und Indexierung]] geprüft: kein Preview-`auth_basic`, kein blockierender `X-Robots-Tag` oder Robots-Meta, kein `Disallow: /`, Canonicals und Sitemap ausschließlich auf Produktions-HTTPS
- [ ] Search-Console-Property, Sitemap und gegebenenfalls API getrennt geprüft; bei API-Nutzung OAuth-/Dienstkonto-Berechtigung und echter Query-Nachweis vorhanden

## G8 Betrieb

- [ ] auf `217.154.218.30`: Eintrag und alle Routen über `johannstein.com/dev` geprüft, kein fester Projektport und kein neues `start-local.sh`; auf anderen Rechnern Ein-Klick-Start für geforderte OS, Healthchecks und verständliche Logs
- [ ] bei Owner-Hosting: `tenant.json` und `_hosting` bestehen [[80-templates/owner-hosting-website-contract.md]]; unbekannte oder gesperrte JSON-Pointer werden serverseitig abgewiesen
- [ ] bei Owner-Hosting: Contract-Plan belegt Erhalt oder explizite Migration aller vorhandenen Owner-Werte; offene Entwürfe alter Vertragsversionen sind behandelt
- [ ] bei Owner-Hosting: im Seiteneditor sind Kopfzeile, Navigation, Anschrift, Anruf- und Mailverweise, die Namen von Impressum und Datenschutz sowie das Logo nachweislich nicht bearbeitbar; ein Klick darauf zeigt die Begründung statt gar nichts `owner-hosting: docs/hosting-and-dashboard.md#Was auf keiner Website bearbeitet wird`
- [ ] bei Owner-Hosting: eine zentrale Angabe, die auf der Seite geändert wurde, steht danach an allen Stellen des Rahmens neu — samt `href` bei Kontaktwegen — und liegt im Overlay, nicht in einer Darstellungsregel
- [ ] bei Owner-Hosting: ein Schritt zurück nach einer zwischenzeitlichen zentralen Änderung nimmt ausschließlich den Seitenschritt zurück; ein verworfener Entwurf ist unter „Veröffentlichen“ zurückholbar
- [ ] bei Owner-Hosting: die Fußzeile zeigt einen Copyright-Hinweis (`©`, ersatzweise `(c)`) in einem gesperrten Bereich
- [ ] bei Owner-Hosting: Hostname löst serverseitig genau einen Mandanten auf; negative Cross-Tenant-Tests für Inhalte, Assets, Builds, Releases, Nachrichten und Integrationen bestehen
- [ ] bei Owner-Hosting: statische öffentliche Website bleibt bei Dashboard-/API-Ausfall erreichbar; Worker baut isoliert, Buildfehler verändert weder aktive Inhaltsrevision noch Release; atomarer Publish, vollständiger Rollback und 503-Wartungsmodus nach [[60-operations/owner-hosting-interface.md]] geprüft
- [ ] bei Deployment-Slots: ein Drop merkt nur vor; erst die ausdrückliche zweite Bestätigung baut und schaltet um; öffentlicher Release und Dashboard-Tenant wechseln atomar gemeinsam
- [ ] bei Deployment-Slots: Slotwechsel verändert weder Quellprojekt noch Katalogstatus der abgelegten Fassung; Archivfassungen bleiben im Archiv
- [ ] bei Deployment-Slots: Sitzungen sind an den Tenant gebunden und nach einem Wechsel wertlos; Suffix-Hosts und gefälschte `Host`-Header werden vor jeder Tenant-Abfrage abgewiesen
- [ ] bei Legacy-Adaptern: Quellhash ohne Buildausgaben vor und nach mehreren Builds identisch, vorhandenes `dist/` der Quelle unverändert; fest im Quelltext hinterlegte Kontaktdaten sind als Warnung gemeldet statt stillschweigend hingenommen
- [ ] bei Staging-Domains: Basic Auth aktiv, `X-Robots-Tag: noindex, nofollow, noarchive` und sperrende `robots.txt` ausgeliefert, ACME-Challenge auf Port 80 unverändert erreichbar
- [ ] bei Websites ohne Editorvertrag: Dashboard läuft schreibgeschützt; bearbeitbare Felder werden nicht aus Text oder HTML erraten
- [ ] Dependency-/Serverliste, `.env.example`, Deploy, Migration und Rollback
- [ ] Monitoring, Alerts, Backups und Restore-Test
- [ ] Subscription-Löschfluss, Datenlöschung und Supportpfad getestet
- [ ] Übergabe aktuell; Entscheidungen des Builds im Decision Log des Projekts und in der Commit-Historie nachvollziehbar
- [ ] jedes Release-Readiness-Register gegen Repository, ausgelieferten Produktionskandidaten und externe Infrastruktur abgeglichen; offene `P0` sichtbar, offene `P1` mit datierter Owner-Entscheidung
