---
type: maintenance
status: canonical
updated: 2026-08-06
---

# Change Log

> [!important] Geltung
> Einträge vor dem 2026-08-06 sind historische Herkunftsnachweise. Wo sie eine feste Anzahl von drei Websites, Auswahlvarianten, Asset-Ausschlüsse, Ersatz, Preview-/Produktionssplit oder KI-Launchblocker nennen, sind sie durch den folgenden Eintrag ausdrücklich überholt.

## 2026-08-06 — Benchmarks, Bildbearbeitung, Informationsdosierung, Retro-Verbot und UI UX Pro Max als Pflicht

Auslöser waren sechs Anforderungen des Nutzers samt drei Referenz-URLs und einem Dashboard-Bild. Kein Projekt unter `../projekte/` wurde verändert.

- **Neue kanonische Notiz [[20-Design/Interface Benchmarks]].** Sie beschreibt die vier vom Nutzer bewerteten Oberflächen als anwendbare Regelsätze: `B1 Soft Neutral Product Console` aus dem gelieferten Dashboard-Bild als Standardhaltung für Produkt-UI, `B2 Rounded Selection Configurator` aus dem 180-Grad-Produktbetrachter, `B3 Full-Bleed Leitbild-Landing` aus der Solarseite und `B4 Data Product Depth` aus dem ATS-Dashboard. Die Notiz hat bei visuellen Entscheidungen Vorrang vor [[90-References/Derived Design Patterns]].
- **Belege im Katalog.** [[90-References/Inspiration Catalog]] führt die vier Benchmarks in einem eigenen, vorrangigen Abschnitt mit Beschreibung, Fußnote und ausdrücklicher Trennung zwischen übertragbaren und nicht übertragbaren Eigenschaften. Bei der Solarseite sind die gesperrten Versalzeilen als verbotene Kicker und die unbelegten Kennzahlen und Kundenstimmen ausdrücklich ausgenommen. Der Prüfstatus hält fest, dass die drei Figma-Seiten aus ausgelieferten Stilvariablen, Assets und Texten ausgewertet wurden und ihr Motion-, Tastatur- und Mobilverhalten damit nicht belegt ist.
- **Alte generierte Beispielseiten entfernt.** Zwölf generierte Beispielwebsites ohne eigenständige Erkenntnis wurden gelöscht: Optimus, GiGi Energy, Agentic, Everest, v0 IRL, AI Video Playground, Halcyon, Scale Hero, Retro CRT, Skydda, Evasion und Editorial SaaS / Cofounder samt ihren Fußnoten. Erhalten bleiben COMPUTE, DataFlow, Brutalist AI SaaS und Animated SaaS als Negativreferenzen. Die Rollentabellen und die Verweise in Derived Design Patterns wurden entsprechend neu belegt.
- **Neue kanonische Notiz [[20-Design/Imagery and AI Editing]].** Bilder werden vor dem Einsatz auf Rolle, Auflösung, Winkel, Ausschnitt, Hintergrund, Licht, Störobjekte und Serienkonsistenz geprüft und mit KI überarbeitet, hochskaliert, freigestellt oder perspektivisch korrigiert. Fehlt ein reales Leitbild, wird ein KI-Bild eingesetzt statt einer leeren Fläche; es wird auf der Website **nicht** gekennzeichnet und nur im Projekt als `ai-placeholder` mit Prompt, Modell und Ersetzungshinweis geführt. Qualitätsschwellen für generierte Bilder sind benannt.
- **Neue kanonische Notiz [[10-Strategy/Information Density and Mobile Clarity]].** Eine Frage pro Abschnitt, konkrete Textbudgets je Element, Sektionsbudgets je Route, dreistufige Tiefenstaffelung und Dosierung am 375-Pixel-Viewport. Menge und Textlänge sind damit kanonisch geregelt; [[10-Strategy/Content and Conversion]] verweist dorthin.
- **Retro-Verbot in der Typografie.** [[20-Design/Typography Layout and Spacing]] verbietet Epochen-Displayschriften, alte Buchserifen als Markenschrift einschließlich `Iowan Old Style`, deren Kombination mit Dunkelgrün und anderen gedeckten Erdtönen sowie Vintage-Ornamente. Eine zeitgenössische Serife auf klarer Neutralbasis bleibt erlaubt. Empfohlene Schriftfamilien und eine Radiusfamilie sind ergänzt; [[20-Design/Color System]] führt die Retro-Farbkombination als verbrauchte Farbwelt, [[20-Design/Anti AI Slop]] als Verbot.
- **Interaktives Kernmodul verbindlich.** [[20-Design/Motion and Interaction#Interaktives Kernmodul]] verlangt für jede Landing Page mindestens ein vom Nutzer bedienbares Modul mit realen Daten, Tastaturbedienung, Zuständen und statischer Alternative, samt Modulkatalog nach Projekttyp.
- **UI UX Pro Max ist bei jedem Website-Build Pflicht.** [[00-Start/04 Plugins and Skills#Auslösebedingung]] schließt jede Ausnahme aus, auch für kleine Aufträge, Korrekturen und vorgegebene Designs, und verlangt bei mehreren Websites eine getrennte Ausführung je Website. Ohne Nachweis ist Gate `G1` nicht erfüllt.

### Geprüfte Auswirkungen

Geprüft und synchronisiert wurden: `AGENTS.md`, Brain Index, Core Rules, Routing Map, Plugins and Skills, Web Product Workflow, Content and Conversion, Design Direction, Color System, Typography Layout and Spacing, Motion and Interaction, Anti AI Slop, Quality Gates, Asset Register, Inspiration Catalog, Derived Design Patterns sowie Coverage and Impact Map.

Offen und in der [[Review Queue]] vermerkt: interaktive Nachprüfung der drei Figma-Benchmarks auf Motion, Tastatur und Mobilverhalten.

## 2026-08-06 — Auftragsgesteuerte Websiteanzahl, Kopfzeilengrenze, Kicker-Verbot und Pflicht-Review mit Impeccable

Auslöser waren acht Anforderungen des Nutzers an das Brain. Kein Projekt unter `../projekte/` wurde dabei verändert; das war ausdrücklich ausgeschlossen.

- **Anzahl der Websites kommt jetzt aus dem Auftrag.** Die bisherige Festlegung auf genau drei Websites ist aufgehoben. Ohne Angabe im Auftragstext wird genau eine Website gebaut, mit genannter Zahl genau diese Anzahl. Kanonischer Besitzer ist der neue Abschnitt [[00-Start/05 Web Product Workflow#Anzahl der Websites]]. Zahl und wörtliche Belegstelle gehören in `PROJECT.md`; bei mehrdeutiger Angabe wird eine Website gebaut und die Auslegung als Annahme vermerkt.
- **Ablage und Ports folgen der Anzahl.** Eine Website liegt unter `site/`, mehrere unter `versions/NN-…`. Beide Formen stehen nie nebeneinander. Für Ports gilt jetzt ein dokumentiertes Schema mit einer Projektbasis und Zehnerschritten. Gemeinsame Fakten bleiben außerhalb der Websites kanonisch, damit eine Faktenänderung eine einzige Änderung bleibt.
- **Kopfzeile begrenzt.** Höchstens sechs sichtbare Navigationspunkte; Logo, Handlungsknopf und Kontaktangabe zählen nicht mit. Nichts in der Kopfzeile bricht um, ausgenommen bewusst mehrzeilige Logos. Geprüft wird bei 1280, 1440 und 1920 Pixel mit der längsten realen Beschriftung. Reicht der Platz nicht, wird die Informationsarchitektur verdichtet, nicht der Abstand verkleinert. Kanonischer Besitzer ist [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]].
- **Kicker über Überschriften verboten.** Keine Eyebrow-Zeile, kein Label, keine Kategoriezeile oberhalb einer Überschrift, weder als Pille noch als gesperrte Versalzeile noch als Marker mit Linie oder Ziffer. Die bisherige Regel gegen Eyebrow-Pills war zu eng gefasst und ist ersetzt. Einordnung gehört in die Überschrift selbst, in den Lead, in eine Bildunterschrift oder in die Navigation. Kanonisch in [[20-Design/Anti AI Slop#Kicker und Überschriften]].
- **Impeccable KI-Detail-Review ist Pflicht.** Nach der Implementierung wird jede gebaute Website mit Impeccable auf Details geprüft, die nach KI-Generat aussehen. Der Review läuft auf der real laufenden Website, wird je Website getrennt geführt und mit Datum, Befundliste und Umsetzungsstand dokumentiert. Ohne diesen Nachweis ist Gate `G1` nicht erfüllt.
- **Verbrauchte Farbwelten benannt.** Beige, Creme und Sand als dominante Grundfläche sind ausgeschlossen, ebenso Blau-Lila-Verlauf, Dunkelviolett mit Neon und durchgehend saturiertes Pastell. Erlaubt bleiben sie nur mit belegter Herleitung aus Marke, Material, Ort oder Produkt. Grundhaltung ist modern, klar und übersichtlich. Kanonisch in [[20-Design/Color System#Verbrauchte Farbwelten]].
- **Landing Page darf extravagant sein.** Neue Abschnitte in [[20-Design/Design Direction]] und [[90-References/Derived Design Patterns]] beschreiben Ausdruck, Freundlichkeit und Übersichtlichkeit der Startseite sowie sieben konkrete Anordnungen für Überschriften mit ihrer Herkunft aus dem Katalog. Unterseiten übernehmen dasselbe System, treten aber ruhiger auf.
- **Firmenlogo wird immer verwendet.** Wird in Auftrag oder Bestandsaufnahme ein Logo gefunden, ist es in jeder gebauten Website sichtbar einzusetzen, bevorzugt auf der Startseite. Auflösung, Alter oder gestalterische Qualität sind kein Grund zum Weglassen oder Ersetzen. Der Kopfbereich ist ein möglicher, kein zwingender Ort. Eine vereinfachte abgeleitete Marke für kleine Größen ersetzt den sichtbaren Einsatz nicht. Kanonisch in [[20-Design/Design Direction#Logo des Betriebs]].
- **UI-Skills und Referenzen werden intensiver genutzt.** Zu UI UX Pro Max sind jetzt Pflicht-Detailabfragen zu `landing`, `style`, `color`, `typography`, `ux`, `gsap` und dem realen Stack festgelegt, bei mehreren Websites je Art Direction erneut. Der Referenzworkflow verlangt mindestens acht erneut angesehene Referenzen, mindestens zwei ausdrückliche Negativreferenzen und je Website eine eigene Referenzkombination. Der Katalog führt dazu neue Tabellen mit Positiv- und Negativrollen.

### Geprüfte Auswirkungen

Geprüft und synchronisiert wurden: `AGENTS.md`, `README.md`, Brain Index, Core Rules, Routing Map, Update Protocol, Plugins and Skills, Web Product Workflow, Discovery and Scope, Existing Website Rebuild, Information Architecture and Sitemap, Design Direction, Color System, Anti AI Slop, Motion and Interaction, Components and UI States, SEO and Discoverability, Assets Copyright and Licenses, Delivery and Local Start, Quality Gates, Test Matrix, Project Intake, Project Master Spec, AI Build Prompt, Launch Checklist, Source and Rights Review, Templates Index, Inspiration Catalog, Reference Research Workflow, Derived Design Patterns sowie Coverage and Impact Map.

Zwei Altregeln wurden dabei bereinigt: die Priorität von [[TasksForAgent]] entfällt, weil die Datei leer ist und der aktuelle Auftragstext des Nutzers oberste Priorität hat; und die Auswahlregel des Inspirationskatalogs enthielt noch ein Kopierverbot für fremde Assets, das der seit 2026-08-05 geltenden Build-first-Regel widersprach.

Nicht geändert wurden Projektartefakte unter `../projekte/`, insbesondere `Fahrschule-Kladow`. Dieses Projekt bleibt auf dem Stand vom 2026-08-05 und ist damit ein dokumentierter Altstand gegenüber den neuen Regeln. Offen bleibt die Aktualisierung des Graphify-Graphen nach diesem Update.

## 2026-08-05 — Aufgabenpriorität: drei vollständige Motion-Websites, Unterseiten, SEO und Build-first-Assets

- [[TasksForAgent]] als innerhalb des Vaults übergeordnete Anforderung in `AGENTS.md` verankert. Widersprechende Regeln zu Asset-Sperren, Ersatz, Auswahlvarianten, Preview-/Produktionssplit und KI-Launchentscheidungen aufgehoben.
- Jeder Website-Auftrag endet jetzt zwingend mit genau drei vollständigen, gleichwertigen Websites auf getrennten lokalen Ports. Jede enthält dieselbe echte Unterseitenarchitektur, vollständige Navigation, eigene Sitemap-/Robots-/Metadata-Artefakte und SEO für jede Route. One-Page- oder Anker-only-Ausgaben sind ausgeschlossen.
- Das kanonische Motion-Niveau umfangreich erhöht: drei verschiedene Route-zu-Route-Choreografien, globaler Seitenwechsel, Einstieg je Route, je primärer Inhaltsroute eine kontinuierliche Scrollsequenz und zwei weitere Scroll-/In-View-Bewegungen sowie mindestens zwölf sichtbare, dokumentierte Motion-Entscheidungen je Website. Die Recherche zu CSS Scroll-/View-Timelines, Motion, GSAP ScrollTrigger, responsiven Setups, Compositor-Performance und Reduced Motion ist in [[20-Design/Motion and Interaction]] mit direkten Primärquellen dokumentiert.
- Asset-Prozess auf die gewünschte Zwei-Schritt-Regel umgestellt: erst alle gewünschten Bilder, Designs, Animationen und sonstigen Assets einsetzen oder kreativ adaptieren, danach Quelle und tatsächlichen Einsatz nur als spätere Owner-Einschätzung dokumentieren. Die KI baut keine rechtlich motivierten Ersätze, keine eingeschränkten Fassungen und keine Asset- oder Veröffentlichungsblocker.
- Workflow, Routing, Scope, Relaunch, IA, Design, Motion, Performance, Komponenten, SEO, Legal-, Asset- und Delivery-Regeln, QA, Tests, Vorlagen, AI-Build-Prompt, Referenzworkflow, Toolwissen, Wartungsmap und README atomar synchronisiert.

### Geprüfte Auswirkungen

Auslöser waren die übergeordnete Anforderung nach deutlich intensiverer, sinnvoller Motion, genau drei fertigen Websites, verpflichtenden Unterseiten, vollständigem SEO und einem nicht blockierenden Asset-Einsatz. Geprüft wurden alle direkten kanonischen Besitzer und ihre Vorlagen: Workflow, Motion, Sitemap, SEO, Asset-/Rights Review, Delivery, Quality Gates, Test Matrix, Master Spec, Intake, AI Build Prompt, Launch Checklist, Reference Research sowie die Maintenance-Artefakte. Die frühere Fahrschule-Kladow-Dokumentation ist auf die neue Build-first-Assetregel und die drei gleichwertigen Websites umgestellt; vorhandene Dateien werden dadurch nicht als neue Websiteimplementierung ausgegeben.

## 2026-08-04 — Relaunch-Preview für Fahrschule Kladow

- Kollisionsfreien Projektordner `../projekte/Fahrschule-Kladow/` mit Master Spec, Produkt-, Content-, Quellen-, Rechte-, Asset- und Dateninventar angelegt.
- Offizielle Bestandswebsite als Fakten-, Preis-, Kontakt-, Rechts- und Redirectquelle inventarisiert; Altgestaltung, Altlogo und Altbilder nicht übernommen.
- Drei eigenständig startbare Browservarianten auf Ports 4311 bis 4313 erstellt. Der Nutzer wählte den hochwertigen Kategorie-Standard `01-klarer-einstieg` mit direktem Split-Hero als einzige Produktionskandidatin; Fahrtenbuch und schematischer Stadtplan bleiben Vergleichsevidenz.
- Statische HTML/CSS/JavaScript-Architektur ohne Formular, Tracking, Cookies, Remote-Fonts oder Drittanbieter-Embed umgesetzt. Externe Anmeldung, Telefon, E-Mail und Maps werden erst nach bewusstem Klick geöffnet.
- Self-hosted Atkinson Hyperlegible Next unter OFL 1.1, eigenes Favicon-/Social-Set und projektspezifische synthetische Hero-Illustrationen mit Rechte- und Promptnachweis ergänzt.
- Lokalen Preview-Server mit festen Ports, Healthcheck, enger Dateifreigabe und restriktiven Headern sowie OS-Start-, Redirect-, Deployment- und Rollbackdokumentation erstellt.
- Drei Screenshot-Runden, Struktur-/Fakten-/Budgetvalidierung, Server-Smoke, Chromium-CDP-Reflow/Fokus/Reduced-Motion/AX-Prüfung, einmaligen Anti-Pattern-Scan und zwei unabhängige Finish-Reviews abgeschlossen. Nach Umsetzung der ersten Befunde lautet das Endurteil `PASS` ohne materielle Restbefunde.

### Geprüfte Auswirkungen

Auslöser waren neuer Website-Auftrag, Relaunch einer Bestandswebsite, drei Varianten, neue visuelle Richtung, selbst gehostete Schrift und ausgehende Drittanbieterlinks. Geprüft wurden Brain Index, Routing, Project Master Spec, Coverage and Impact Map, Design-, Accessibility-, Performance-, SEO-, Security-, Privacy-, Asset-, Delivery- und alle Quality-Gate-Regeln. Sitemap, Navigation, Dateninventar, Rechtstext-Preview, Tests, Abhängigkeiten, Betriebsdoku und Projekt-Changelog wurden synchronisiert. Öffentlicher Launch bleibt in `PROJECT.md`, `SOURCE-RIGHTS-REVIEW.md` und `tests/LAUNCH-CHECKLIST.md` bis Betreiber-, Fakten-, Asset-, Hosting- und Rechtsfreigabe ausdrücklich `NO-GO`.

## 2026-08-04 — Build-first mit dokumentierter Owner-Freigabe vor Launch

- Den Quellen- und Rechteprozess vom vorgelagerten Build-Stop zu einem parallelen Projektartefakt umgestellt. `SOURCE-RIGHTS-REVIEW.md` dokumentiert jetzt je Kandidat Nutzungsabsicht, Ersatz, Owner, Frist und die endgültige Launch-Entscheidung.
- Website-Builds dürfen ohne vorgezogene Rechtsbewertung fortschreiten. Reale Medien des Betreibers oder nachweislich autorisierte Medien können im Build verwendet werden; der benannte Owner führt vor öffentlicher Preview oder Produktion die dokumentierte Quellen-, Rechts- und Launch-Prüfung durch.
- Statusmodell und Vorlagen auf `reference-only`, `operator-provided`, `authorized`, `launch-decision-required`, `replace` und `omit` umgestellt. Offene externe Kandidaten erhalten bis zur Entscheidung einen eigenen oder autorisierten Ersatz.
- Workflow, Intake, Master Spec, Design Direction, Relaunch-Ablauf, Asset Register, AI-Build-Prompt, Quality Gates, Launch-Checkliste, Wartungsmap und README auf den neuen Verantwortungs- und Freigabezeitpunkt synchronisiert.
- Nicht übernommen wurde eine pauschale Erlaubnis, fremde geschützte Assets, Texte, Marken oder unverwechselbare Layouts ohne Berechtigung zu kopieren oder auszuliefern. Solche Inhalte bleiben Referenzmaterial beziehungsweise werden vor dem Launch ersetzt, entfernt oder durch den Owner als autorisiert dokumentiert.

### Geprüfte Auswirkungen

Auslöser war die Anforderung, die kreative und technische Umsetzung nicht durch eine vorgezogene Rechtsprüfung zu blockieren und Bedenken erst vor dem Launch verbindlich zu entscheiden. Aktualisiert wurden die globalen Regeln, der Produktworkflow, die kanonische Asset-Regel, der Legal Decision Tree, der Relaunch-Ablauf, die Designrichtung, Update-Prozess, Projekt- und Launchvorlagen, Quality Gates sowie die Zuständigkeits- und Wartungsnotizen. Die Entscheidung betrifft keine konkrete Website, keine Produktionsroute und keine externen Konfigurationen.

## 2026-08-04 — Drei Varianten, mediengetragene Art Direction und präzisere Motion

- Jeder Website-Auftrag erzeugt nun unter `versions/` drei eigenständig startbare, sichtbar verschiedene Richtungen auf getrennten lokalen Ports. Sie teilen Scope, Fakten, Sicherheits-, Accessibility- und Rechteanforderungen; nur die dokumentiert gewählte Variante ist für Preview oder Produktion zulässig.
- Design Direction, Intake, Master Spec, Delivery, KI-Build-Prompt und Quality Gates auf Variantenmatrix, Leitmedium, Start-/Portnachweis und Auswahlentscheidung synchronisiert.
- [[20-Design/Motion and Interaction]] um einen Entscheidungsrahmen für Häufigkeit, Zweck, Timing, Easing, Unterbrechbarkeit, Eingabemethode und Reduced Motion ergänzt. Komponenten- und Performance-Regeln führen diese Anforderungen bis zur Umsetzung fort.
- Die lokal verfügbaren Skills Emil Design Engineering und Impeccable sind neben UI UX Pro Max im verbindlichen Designablauf erfasst: Impeccable für visuelle UI-Arbeit, Emil für neue oder geänderte Motion.
- Acht bereitgestellte Prompt-Beispiele und MotionSites AI wurden als Inspiration ausgewertet. Übernommen sind ausschließlich abstrahierte Prinzipien wie mediengetragener Produktbeweis, präziser Responsive-/Motion-Contract und sparsame Choreografie. Die Beispiele, externe Medien, Marken, Copy, Quellcode, Zahlen und unverwechselbare Kompositionen werden nicht übernommen. MotionSites ist als eingeschränkt analysierte Referenz mit direkter Quelle dokumentiert.
- Die Anweisung, ungeklärte Internet-, Maps- oder Bestandsassets trotz möglicher Rechtsverletzung zu verwenden, wurde nicht übernommen. Sie widerspricht [[50-Legal/Assets Copyright and Licenses]] und den globalen Regeln. Ungeklärtes Material bleibt nur `research-only` oder ausdrücklich `pitch-restricted`, niemals in öffentlicher Preview oder Produktion.

### Geprüfte Auswirkungen

Auslöser waren neue verbindliche Varianten-, Medien- und Motion-Anforderungen sowie zusätzliche lokale Skills. Aktualisiert wurden globale Regeln, Produktworkflow, Auswirkungs- und Zuständigkeitskarte, visuelle Richtung, Motion, Komponenten, Performance, lokale Projektablage, Intake, Master Spec, KI-Build-Prompt, Quality Gates, Tool-/Referenzwissen und Review Queue. Die Prompt-Quelldateien wurden nach der Auswertung entfernt. Eine Suche auf veraltete MotionSites-Regeln, die neuen internen Links und die strukturelle Konsistenz der geänderten Markdown-Dateien sind noch vor Abschluss geprüft worden. Keine konkrete Website, Produktionsroute, Abhängigkeit oder externe Konfiguration wurde verändert.

## 2026-08-03 — pen.dev-CLI und zeitkritische Maps-Hinweise

- [[90-References/pen.dev Workflow]] auf den ausschließlichen headless-CLI-Workflow `pen` umgestellt: Einsatzgrenzen, Verfügbarkeit, versionierte Ein-/Ausgabepfade, interaktive Bearbeitung und Exportprüfung sind nun kanonisch; Desktop-App, Start-/Stoppskripte und MCP-Server-Prüfungen entfernt.
- Verlinkte Tool-, Routing-, Betriebs-, Skill- und Wartungsnotizen auf CLI statt App/MCP synchronisiert.
- [[80-Templates/Source and Rights Review]] erhält einen expliziten `verify-required`-Status für nicht persistierte Maps-Hinweise zu Öffnungszeiten, Reviews, Stoßzeiten und ähnlichen Fakten. Veröffentlichung erst nach Bestätigung durch Betreiber oder andere freigegebene Primärquelle.
- Relaunch-Ablauf, Intake, Master Spec, Launch-Checkliste und Quality Gates auf diese Verifikationsspur aktualisiert.
- Ungeklärte Bilder und andere Assets bleiben gemäß [[50-Legal/Assets Copyright and Licenses]] auf `research-only` oder `pitch-restricted`; öffentliche Preview und Produktion erfordern weiterhin `approved`.

### Geprüfte Auswirkungen

Auslöser waren ein geändertes Designwerkzeug sowie die Behandlung zeitkritischer Drittanbieterfakten. Geprüft und aktualisiert wurden Tool-Workflow, Codex-/Skill-Kontext, Routing, lokale Ablage, Relaunch, Projektvorlagen, Quellen-/Freigabeliste, Launch und QA. Eine Textsuche bestätigt, dass alte pen.dev-Anweisungen außerhalb des archivierten Auftrags [[TasksForAgent]] entfernt sind. Offen bleibt die reguläre Halbjahresprüfung der pen.dev-CLI und Google-Maps-/Places-Bedingungen in der [[98-Maintenance/Review Queue|Review Queue]].


Nur inhaltlich relevante Änderungen werden eingetragen. Reine Tippfehler ohne Bedeutungsänderung benötigen keinen eigenen Eintrag.

## 2026-08-03 — Projektanlage und Relaunch-Quellenwiederherstellung

- Website-Aufträge erzeugen jetzt zwingend vor Recherche oder Code einen kollisionsfreien Ordner unter `../projekte/<Projektname>/` mit PROJECT.md, Source/Rights Review, Asset Register, Data Processing Inventory und vollständiger Arbeitsstruktur.
- [[10-Strategy/Existing Website Rebuild]] als kanonischen Ablauf für Bestandswebsite, Webrecherche, Speisekarten/Preise, Unternehmensprofile, Google Maps und alte Rechtstexte ergänzt.
- [[80-Templates/Source and Rights Review]] als projektbezogene Fundstellen-, Übernahme- und Rechtsrisikoliste eingeführt.
- Bestandsfotos und Dokumente dürfen als klar isolierte Recherche- oder eingeschränkte Pitch-Kandidaten erfasst werden; ungeklärte Assets bleiben aus öffentlicher Preview und Produktion.
- Google-Maps-Nutzung auf offizielle Maps URLs, Place IDs und APIs mit Attribution und Speichergrenzen begrenzt; Scraping und Rehosting von Maps-Inhalten ausgeschlossen.
- Impressum und Datenschutz einer Altwebsite dienen als Fakten- und Dienstleisterquelle. Neue Texte werden aus aktuellem Betreiber, Markt und den tatsächlichen Datenflüssen abgeleitet.
- Brain Index, Routing, Discovery, Content, Legal, Privacy, Assets, Delivery, Intake, Master Spec, AI Build Prompt, Launch, Quality Gates, Impact Map, Review Queue, Templates Index und README synchronisiert.

### Geprüfte Auswirkungen

Projektanlage, Relaunch, Inhalte, Assets, Datenschutz, Recht, Maps-/Drittanbieterintegration, Templates und QA wurden gemeinsam geprüft. Keine konkrete Website, Produktionsroute oder externe Plattformkonfiguration wurde verändert.

## 2026-08-03 — KI-Workflow, Referenzevidenz, UI UX Pro Max und pen.dev

- Verbindlichen [[00-Start/05 Web Product Workflow|Web Product Workflow]] mit Intake, Inspiration, Design Contract, Spec-first, vertikaler Implementierung, Kritikschleife und getrennten Gedächtnisebenen ergänzt.
- [[90-References/Reference Research Workflow]] als kanonischen Besitzer für verpflichtende Inspiration, Screenshot-Readiness, Motion-/Interaktionsnachweis und Projektablage angelegt.
- Sieben der acht globalen Referenzscreenshots mit längeren Renderbudgets neu aufgenommen. `v0 IRL` blieb im Headless-WebGL-Loader und ist im [[.research/screenshots/README|Screenshot Manifest]] transparent `invalid`; Everest ist statisch nur als Einstiegsszene belegt.
- Curriculum-Referenz ausgewertet. Research-vor-Spec, Verifikation, Toolprüfung und Gedächtnisebenen wurden angepasst übernommen; externe Wissensspeicher und produktspezifische Defaults nicht.
- [[90-References/pen.dev Workflow]] mit Ubuntu-Start/Stop, MCP-Status, Log, sicherer `.pen`-Ablage, Designschleife, Fehlerpfad und offiziellen Quellen erstellt.
- UI UX Pro Max in [[00-Start/04 Plugins and Skills]] als Pflichtskill für alle UI-verändernden Aufgaben samt `--design-system`- und Validierungsablauf konkretisiert.
- Kanonische Projektstruktur auf `Web-Design/projekte/<Projektname>/` und Designquellen auf `design/` festgelegt; die abweichende Schreibweise im Herkunftstext ist nicht verbindlich.
- Routing, Design-/Motion-Regeln, Intake, Master Spec, AI Build Prompt, QA, Test Matrix, Impact Map, Review Queue, README und Aufgabenarchiv atomar aktualisiert.

### Geprüfte Auswirkungen

Betroffen waren Web-Produkt-Ablauf, Referenzmuster, visuelle Richtung, Motion, lokale Designwerkzeuge, Projektablage, Vorlagen und QA. Externe Runtime-Dependencies, Datenflüsse, Rechtstexte, Sitemap und Produktionscode änderten sich nicht. Offene interaktive Browserprüfungen und Toolversionsprüfungen stehen in der [[98-Maintenance/Review Queue|Review Queue]].

## 2026-08-03 — Initiales Web-Brain

- `INFOSFORU.md` vollständig ausgewertet und in kanonische Themenbereiche überführt.
- Regeln für Strategie, Informationsarchitektur, Design, Frontend, Sicherheit, Recht, Betrieb und QA angelegt.
- Vorlagen für Intake, Master Spec, AI-Build-Prompt, Assets, Datenverarbeitung, Entscheidungen und Launch erstellt.
- Alle 51 angegebenen Website-Referenzen katalogisiert; eingeschränkt prüfbare Seiten transparent markiert.
- Zusätzliche Primärquellen zu Barrierefreiheit, Performance, Sicherheit, Datenschutz, deutschem Digitalrecht, Authentifizierung, Billing und Suchdarstellung eingearbeitet.
- Updateprotokoll, Zuständigkeitskarte und Review Queue eingerichtet.
- Lokale Recherchebilder der ersten acht generierten Websites unter `.research/screenshots/` abgelegt.

### Geprüfte Auswirkungen

Navigation, Arbeitsregeln, Projektvorlagen, Qualitätsgates, Quellenführung und Wartungsprozess wurden gemeinsam initialisiert. Dies ist der Basisstand; offene zeitabhängige Prüfungen stehen in der [[Review Queue]].
