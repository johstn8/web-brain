---
type: reference
status: canonical
updated: 2026-11-07
review_by: 2027-02-27
---

# Inspirationskatalog

> [!summary] Zweck
> Dieses Verzeichnis bewahrt ausführliche Analysen, Benchmarks und Negativbeispiele. Der kompakte, nach Einsatzfeldern kategorisierte Auswahlbestand konkreter Live-Seiten liegt in [[90-references/website-reference-pool.md]]. Externe Leitreferenzen werden nach [[90-references/reference-research-workflow.md]] dosiert: keine automatisch ausgewählte Referenz bei einer Einzelwebsite und genau eine referenzgeführte Fassung je Mehrfachauftrag bei starker Passung.

## Aktiver Pool und Sammlungsgrenze

Wenn ein Mehrfachauftrag eine referenzgeführte Fassung erhalten soll, ist [[90-references/website-reference-pool.md]] für genau diese Fassung der erste Einstieg. Bei einer Einzelwebsite und den übrigen Eigenentwürfen dient dieser Katalog nur als interne Muster-, Benchmark- und Negativreferenz, nicht als Vorlage. Im Pool stehen ausschließlich direkt aufrufbare Originalseiten. Designsammlungen, Galerien, Award-Listen und Stilbibliotheken werden nicht als Referenz ausgewählt; aus ihnen werden konkrete Originalseiten extrahiert. Die ausführlichen Befunde dieses Katalogs bleiben für die Interpretation, Negativmuster und historische Herkunft erhalten.

## Prüfstatus

- **Analysiert:** Öffentlich erreichbare Seitenstruktur, Inhalte, Interaktionshinweise und technische Metadaten wurden am 3. August 2026 geprüft.
- **Eingeschränkt:** Die Seite war durch JavaScript, Bot-Schutz oder eine leere App-Shell nicht zuverlässig auslesbar. In diesen Fällen werden keine unbelegten visuellen Eigenschaften behauptet.
- `Analysiert` belegt keine vollständige Interaktionsprüfung. Statische Aufnahme, Motion, Tastatur, Mobil und Reduced Motion werden nach [[90-references/reference-research-workflow.md]] getrennt nachgewiesen.
- Die drei Figma-Site-Benchmarks liefern ihre Oberfläche erst per JavaScript aus. Ihre Beschreibung beruht auf der Auswertung der ausgelieferten Stilvariablen, Bildassets und Textinhalte am 6. August 2026, nicht auf einer interaktiven Sitzung. Motion, Tastaturbedienung und mobiles Verhalten dieser drei Seiten sind damit **nicht** belegt und werden vor einer Übernahme dieser Aspekte erneut geprüft.
- Die Seiten können sich jederzeit ändern. Vor einer konkreten Übernahme muss die Referenz erneut geprüft werden.
- Lokale Momentaufnahmen der verbliebenen generierten Negativreferenzen und ihr aktueller Gültigkeitsstatus liegen im [[.research/screenshots/README.md|Screenshot Manifest]]. Sie sind Rechercheartefakte, keine freigegebenen Projektassets.

## Workflow- und Systemreferenzen

### Claude Code Curriculum — analysiert

Die Curriculum-Seite strukturiert KI-gestützte Webproduktion als Research, strukturierte Spezifikation, Design, Umsetzung und Verifikation. Zusätzlich trennt sie aktuellen Kontext, Projektgedächtnis und Langzeitwissen und behandelt Skills, MCP, Toolprüfung sowie Betrieb als Teil des Systems. Für dieses Brain übernommen wurden die verbindliche Inspirationsphase, Spec-first, Toolnachweise, Kritikschleife und Gedächtnisebenen. Nicht übernommen wurden produktspezifische Tooldefaults, externe Wissensspeicher als kanonische Basis, Marketing-Claims und pauschale Stackempfehlungen.[^curriculum]

### MotionSites AI — eingeschränkt analysiert

MotionSites veröffentlicht detaillierte Prompts für Landingpages und Hero-Sektionen in vielen Kategorien. Die frei sichtbaren Beschreibungen nennen Layout, Stil, Schrift, Animation, Responsive-Verhalten, Abhängigkeiten und Inhalte als Promptbausteine.[^motionsites] Für dieses Brain übernommen sind klare visuelle Leitmedien, zweckbezogene Scroll-Hierarchie und konkret ausformulierte Responsive-/Fallback-Regeln. Hohe Motion-Dichte bleibt eine mögliche Richtung, aber keine allgemeine Qualitätsbedingung. Marken, Texte, Assets, Quellcode, externe Videos und Kompositionen können bei einem Projekt direkt eingesetzt oder kreativ adaptiert werden; ihr tatsächlicher Einsatz ist anschließend nach [[50-legal/assets-copyright-and-licenses.md]] zu dokumentieren. Die dynamische Auslieferung erlaubte keine belastbare Vollprüfung jedes Prompts; konkrete Referenzen müssen projektbezogen erneut nach [[90-references/reference-research-workflow.md]] geprüft werden.

## Vom Nutzer bewertete Benchmarks

> [!important] Vorrang
> Diese Referenzen hat der Nutzer ausdrücklich als gut benannt: am 6. August 2026 ein Dashboard-Bild und drei Figma-Seiten, am 8. August 2026 sieben Websites. Am 7. November 2026 hat er sie erneut bewertet: Das ATS-Dashboard, StepSafer, CanDevsDoSomething, EVE BCN, ClaudeFolio und Thomas Stockham hat er verworfen, sie stehen hier nicht mehr. Bei den übrigen gilt jetzt nur, was er dabei gelobt hat. Die daraus abgeleiteten Regeln stehen kanonisch in [[20-design/interface-benchmarks.md]].

### Data Console Dashboard — analysiert, Bildvorlage

Vom Nutzer als Bild geliefert und als perfekte Benchmark für Design und UI bezeichnet. Ein Datenbank-Adminbereich auf weißer Fläche: Seitenleiste mit Marke oben und flacher Navigationsliste, aktiver Punkt als gefüllte fast schwarze abgerundete Fläche mit heller Schrift. Inhaltsbereich mit Seitentitel und einer grauen Erklärzeile, darunter vier gleich breite Kennzahlenfelder aus Beschriftung, Linienicon in eigener Farbe, großer Zahl und Veränderungswert. Darunter zwei ungleich breite Blöcke, „Storage Usage“ mit flachen Fortschrittsbalken und „Recent Activity“ mit rund getönten Icon-Trägern und Metazeilen im Muster `Name · Zeitangabe`, darunter ein voll breiter Block „System Health“ mit drei Spalten und grüner Statuspille. Abgrenzung ausschließlich über Hairline-Rahmen und Weißraum, eine Radiusstufe, keine Schatten, keine Verläufe, Farbe nur semantisch oder als kleiner Kategorieton. Als Positivreferenz für Produkt-UI ohne Einschränkung übertragbar.[^benchdash]

### 180-Grad-Produktbetrachter — analysiert

Vom Nutzer wegen des weich abgerundeten Charakters und des Zusammenspiels aus Objekt und Auswahl benannt. Eine einzelne Produktseite für einen Hoodie: ein freigestelltes schwarzes Objekt auf heller Studiofläche mit weichem Bodenschatten, benannte Ansichten wie `Front-Left View`, `Left Side View`, `Back-Left View`, dazu `Available Colors`, Größenauswahl mit `Size Guide` und eine kurze Detailliste mit Angaben wie `Unisex Regular` und `Machine Washable`. Der Betrachter selbst ist der Inhalt; Text tritt vollständig zurück. Übertragbar sind Objektfreistellung, Ansichtsreihe, weiche Auswahlformen und die extreme Textknappheit. Übertragbar ist ausdrücklich nicht das Erfinden einer Auswahlmechanik dort, wo es nichts zu wählen gibt.[^benchrotate]

### INIZIO Solar — analysiert, teilweise übertragbar

Vom Nutzer wegen des Leitbilds benannt. Eine Solaranbieterseite auf mattschwarzer Grundfläche mit einer einzigen kräftigen Signalfarbe im Neongrün-Bereich, dazu eine abstrakte grüne Wortmarke und großformatige Fotos von Anlage und Montageteam. Auftakt „Powering the Future with Solar Revolution“ mit einem erklärenden Satz und zwei Aktionen, danach vier bis sechs benannte Leistungen mit je einer Zeile, Werteabschnitt, Kennzahlenband, Kundenstimmen und Newsletter. Übertragbar sind das großformatige Leitbild des tatsächlichen Gegenstands, die eine Signalfarbe gegen dunkle Fläche und die knappe Leistungsgruppe. Ausdrücklich nicht übertragbar sind die gesperrten Versalzeilen über den Überschriften wie `COMPREHENSIVE SOLUTIONS` oder `CLIENT TESTIMONIALS`, die nach [[20-design/anti-ai-slop.md#Kicker und Überschriften]] verbotene Kicker sind, sowie die Kennzahlen zu erzeugter Energie, Projektzahl, Zufriedenheit und Jahren Erfahrung und die namentlichen Kundenstimmen, für die kein Beleg vorliegt.[^benchsolar]

### Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026

Am 8. August 2026 hat der Nutzer sieben Websites für Oberfläche, Bedienung, Animation und Kastengestaltung benannt. Am 7. November 2026 hat er vier davon verworfen: CanDevsDoSomething, EVE BCN, ClaudeFolio und Thomas Stockham. Ihre Werte sind aus dem Brain entfernt. Übrig bleiben drei:

| Seite | Was der Nutzer am 2026-11-07 gelobt hat | Was er abgelehnt hat |
|---|---|---|
| [Consile](https://consile.app/) | Konzept und Aufbau einer Produktvorstellung | die eine Markenfarbe Orange überall, zu wenig Abwechslung, viele Verläufe: „da merkt man die KI" |
| [Saad Salman](https://saadsalman.org/) | schwebende Einzelelemente, Hover-Effekte | kleine Ovale über Überschriften, Verläufe in Überschriften |
| [Phillip Ohren](https://phillipohren.com/) | nicht neu bewertet; Leitmedium je Leistung, Text auf dem Bild, großer Weißraum | – |

Belegt waren 2026-08-08 Markup und CSS. Gemessene Werte: Consile führt einen Zeichenauftakt mit `translateY(.4em)` und `blur(6px)` gegen null; Saad Salman einen sehr flachen Hover-Schatten `0 8px 30px rgba(0,0,0,.06)`, `rounded-2xl` für große Flächen und eine Kopfzeile mit `backdrop-blur-sm`, deren Rahmen beim Hover den Akzent annimmt. Was davon im Kit steht, führt [[90-references/inspiration-eingang.md#Verarbeitet]].

### Rocket-Sites-Referenzgruppe — strukturell analysiert am 19. August 2026

Vom Nutzer im August 2026 als professionell und wegen ihrer Bandbreite benannt, 37 Domains. Am 4. und 7. November 2026 hat er jede einzeln bewertet und 16 verworfen; sie stehen nicht mehr im Brain. Von den übrigen bleibt je Seite nur, was er gelobt hat: eine ganze Vorlage, wenn er die Seite insgesamt stark fand, sonst die genannten Elemente. Der Stand je Seite steht im [[90-references/website-reference-pool.md]] und in [[90-references/inspiration-eingang.md#Verarbeitet]].[^rocket-a][^rocket-b]

**Was als Haltung bleibt:** Inhalt, Geschäft, Zielgruppe und Beweisform bestimmen Struktur und Sprache. Keine feste Zahl an Kopfzeilenlinks, keine Pflichtmenge an Bewegung.

**Was ausdrücklich nicht mehr gilt:** Die Auswertung vom August hielt Kicker, Serifenschrift und warme Farben für „nicht pauschal verboten". Das ist überholt: Dachzeilen sind seit 2026-10-02 harte Sperre, und der Nutzer hat Kicker, Ovale über Überschriften und den warmen Altstil mehrfach als KI-typisch oder altmodisch benannt, siehe [[20-design/anti-ai-slop.md#Harte Sperren]].

## Gastronomie: Negativbeispiele

Bewertet nach dem [[20-design/qualitaetsraster.md]]. Sie zeigen, wie eine Restaurantseite nicht aussehen soll, und gehören in jeden Benchmarkvergleich dieser Gattung als Gegenpol.

### Impasto Rosso, Berlin — vom Nutzer als schwach benannt, 6 Punkte

[impastorosso.de](https://impastorosso.de/), aufgenommen am 2. Oktober 2026. Die Fotos des Raums sind brauchbar, die Seite ist es nicht: Baukastenvorlage mit Bildkarussell und Pfeilen im Auftakt, der Satz „Genießen Sie die Aromen des authentischen Italiens" fällt durch den Namenstausch-Test, zwei Dachzeilen in Versalien über den Überschriften, Doppellinien als Ornament, drei Karten mit Skizzensymbolen für Menü, Reservierung und Standort, ein Newsletter-Kasten, zwei gleich starke umrandete Aktionen in der Kopfzeile. `check-slop.ts` meldet zwei harte Sperren. Lehre: Gute Fotos retten keine Vorlagenseite.

### Weitere Negativbeispiele, vom Nutzer am 2. Oktober 2026 bestätigt

| Seite | Raster | Warum sie schwach ist |
|---|---:|---|
| [Trattoria Portofino, Mülheim](https://www.trattoria-portofino.de/) | 3 | Holzmaserung als Hintergrund, Trikolore-Linien als Ornament, Navigation in Signalorange, freigestellte Pizza als Dekoration |
| [Muret La Barba, Berlin](https://www.muretlabarba.de/) | 6 | Shop-Navigation und ein Bildraster aus gemischten Quellen verdrängen das Restaurant, kein Bild trägt |
| [Ottenthal, Berlin](https://www.ottenthal.com/) | 7 | Fotocollage ohne Serie, kein Leitbild, kein Satz |

### Trattoria Alberto, Fassungen 01 bis 04 — interne Negativbeispiele vom 12. und 20. September 2026

Unter `projekte/trattoria-alberto/versions/`. Alle vier haben Kontrast, Rhythmus, Zustände, axe und Lighthouse bestanden und wurden vom Nutzer trotzdem als generiert erkannt. Sie bleiben unverändert erhalten, weil sie zeigen, was Messungen nicht finden.

| Fassung | Raster | Was der Nutzer kritisiert hat | Sperre nach heutigem Stand |
|---|---:|---|---|
| `01-sala` | 11 | Der Auftakt ist der einzige der vier, der für eine Trattoria trägt. Danach sind alle Blöcke gleich gebaut, und das Auftaktbild läuft über einen Verlauf in den dunklen Seitengrund aus | S4 Ausblendung, S5 drei gleiche Sektionen in Folge |
| `02-carta` | 10 | Speisekarte als Auftakt: für eine Trattoria keine Landingpage | S3 Zählplakette „8 Weine" in Überschriften |
| `03-kladow` | 9 | Kontaktauftakt mit Tageslinie: Auskunft statt Atmosphäre | S1 Statuspille über der H1 |
| `04-tavola` | 12 | Dachzeile „Cucina Italiana · seit 2002 in Berlin-Kladow", Nummernmarken als „Signaturdetail", das letzte Wort der H1 rot und kursiv | S1, S2, S3, S6 auf fast jeder Route |

## Generierte und experimentelle Websites

Dieser Abschnitt wurde am 6. August 2026 auf reine Negativreferenzen reduziert. Die früher hier geführten generierten Beispielseiten trugen keine eigenständige Erkenntnis mehr und wurden entfernt; ihre übertragbaren Prinzipien stehen in [[90-references/derived-design-patterns.md]] und in [[20-design/interface-benchmarks.md]].

### COMPUTE — analysiert

Wiederkehrende Engineering-Module, Messwerte, Integrationen und Sicherheitsinhalte erzeugen technische Glaubwürdigkeit. Als Warnung dient die große strukturelle Nähe zu typischen Infrastruktur-Landingpages: Ohne eigene Produktbelege wirkt das Ergebnis schnell wie eine Vorlage.[^compute]

### DataFlow — analysiert

Zentrierter Hero, Kennzahlen, Featurekarten, Testimonials und Abschluss-CTA bilden ein vollständiges Standardgerüst. Genau dadurch eignet sich die Seite als Negativreferenz für generische KI-Landingpages: wenig Eigenart, viele erwartbare Karten und potenziell erfundene Behauptungen.[^dataflow]

### Brutalist AI SaaS — analysiert

Monospace-Typografie, Terminalmotive, harte Raster und Abschnittsnummern bilden ein konsequentes System. Das funktioniert, wenn Produkt und Tonalität dazu passen. Lesbarkeit, Informationsdichte und die Wahrheit aller technischen Anzeigen müssen besonders geprüft werden.[^brutalist]

### Animated SaaS — analysiert

Features, Prozess, Testimonials und Preise folgen einem verbreiteten SaaS-Schema. Die Referenz ist vor allem nützlich, um das bloße Aneinanderreihen erwartbarer Landingpage-Blöcke zu erkennen und durch echte Produktbeweise zu ersetzen.[^animated]

### Apple — analysiert

Bildgetriebene Produktmodule, knappe Texte und wenige klare Folgeaktionen schaffen Fokus. Übertragbar sind die modulare Dramaturgie und präzise Bildbeschreibungen, nicht die bloße Ästhetik ohne entsprechende Assets.[^apple]

### Stripe — analysiert

Eine breite Informationsarchitektur verbindet Produktdemos, Entwicklerdetails, reale Kundengeschichten und mehrere Zielgruppenebenen. Das zeigt, wie Komplexität über progressive Vertiefung statt über einen überladenen Hero beherrscht wird.[^stripe]

### Linear — analysiert

Ruhige dunkle Flächen, präzise Sprache und echte Produktoberflächen tragen die Glaubwürdigkeit. Dichte Informationen werden über Hierarchie und Rhythmus kontrolliert, nicht durch beliebig viele Karten.[^linear]

### Vercel — analysiert

Monochromes Raster, technische Architektur und echte Interface-Ausschnitte bilden ein konsistentes System. Besonders nützlich ist die Verbindung aus Plattformmodell, Live-Produkt und klaren Einstiegspfaden.[^vercel]

### Framer — analysiert

Arbeitsfläche, veröffentlichte Ergebnisse, CMS und Animationen werden als sichtbares Produkt statt als abstrakte Featureliste gezeigt. Expressive Gestaltung bleibt an konkrete Bedienhandlungen gebunden.[^framer]

### Webflow — analysiert

Zielgruppenpfade, Templates, Enterprise-Belege und Produktmodule decken ein breites Angebot ab. Die Referenz zeigt sowohl gute progressive Auswahl als auch das Risiko einer historisch gewachsenen, komplexen Navigation.[^webflow]

### Notion — analysiert

Warme Illustrationen, vertraute UI und modulare Anwendungsfälle verbinden eine große Produktfamilie. Das Produkt bleibt durch wiederkehrende Arbeitsoberflächen erkennbar, obwohl verschiedene Zielgruppen angesprochen werden.[^notion]

### Figma — analysiert

Farbe, kollaborative Canvas-Motive und Produktcollagen vermitteln gemeinsames Gestalten. Die Expressivität funktioniert, weil sie das Verhalten des Produkts und nicht bloß Dekoration visualisiert.[^figma]

### Anthropic — analysiert

Zurückhaltende redaktionelle Gestaltung, Mission, Forschung und wenige Aktionen stellen Inhalte vor Effekte. Das ist eine gute Referenz für Marken, deren Seriosität aus Positionierung und Publikationen entsteht.[^anthropic]

### OpenAI — analysiert

Ein minimalistischer redaktioneller Hub priorisiert reale Nachrichten, Forschung und Produkte. Das Muster zeigt, dass hochwertige Inhalte und klare Taxonomie einen großen Teil der visuellen Arbeit leisten können.[^openai]

### ElevenLabs — analysiert

Direkt eingebettete Audiointeraktion, Kategorien und reale Anwendungsbeispiele machen das Kernmedium sofort erfahrbar. Produktdemo und Vertrauensbelege stehen vor allgemeinen Behauptungen.[^elevenlabs]

### Runway — analysiert

Filmische Arbeiten, Plattformbereiche und Forschung machen das Medium selbst zum Beweis. Video ist hier Inhalt; deshalb müssen Poster, Ladeverhalten, Untertitel und reduzierte Alternativen mitgestaltet werden.[^runway]

### Perplexity — eingeschränkt

Die öffentliche Seite lieferte bei der Prüfung überwiegend eine Anwendungshülle. Eine belastbare Detailanalyse ist erst nach erneuter interaktiver Prüfung sinnvoll.[^perplexity]

### Raycast — analysiert

Tastaturmetapher, Erweiterungen und konkrete Befehle erklären das Verhalten des Produkts. Interaktion wird nicht als Showeffekt, sondern als komprimierte Produkterfahrung eingesetzt.[^raycast]

### Pitch — analysiert

Galerien, Vorlagen, Markenbibliothek und Bewegungsbeispiele zeigen die Qualität des Outputs. Wiederholte Medienloops brauchen dabei kontrollierte Dateigrößen und Respekt vor reduzierter Bewegung.[^pitch]

### Rive — analysiert

Interaktive Ergebnisse, Editor, Laufzeitumgebungen und konkrete Cases verbinden Gestaltung und Implementierung. Das Muster ist besonders wertvoll für technische Kreativprodukte: Output, Workflow und Integration werden gemeinsam gezeigt.[^rive]

### Spline — analysiert

Interaktive 3D-Szenen, Handlungsanweisungen und Produktionsfälle laden zur direkten Erkundung ein. Jede räumliche Demo braucht jedoch eine verständliche Bedienung, einen statischen Fallback und ein Performancebudget.[^spline]

### Jitter — analysiert

Motion-Galerie und Vorlagen zeigen Ergebnisse bereits auf der Startseite. Das ist ein starkes Proof-first-Muster, sofern Autoplay, Dateigröße und `prefers-reduced-motion` berücksichtigt werden.[^jitter]

### Railway — analysiert

Produktoberflächen, Architekturdiagramme, konkrete Workflows und Vergleiche erklären eine technische Plattform. Visuelle Präzision entsteht aus Systemwahrheit, nicht aus futuristischer Dekoration.[^railway]

### Liveblocks — analysiert

Interaktive Kollaborationsmuster, Codebeispiele und vertraute Produktfälle sprechen Entwickler direkt an. Das Zusammenspiel aus Demo und Implementierung reduziert die Distanz zwischen Versprechen und Machbarkeit.[^liveblocks]

## Kreative Studios und experimentelle Portfolios

### Locomotive — eingeschränkt

Bot-Verifikation verhinderte eine verlässliche Prüfung. Vor einer Ableitung muss die aktuelle Seite manuell und auf mehreren Eingabegeräten getestet werden.[^locomotive]

### Hello Monday — analysiert

Ein filterbares Projektarchiv, spielerische Sprache und eine große Bandbreite an Cases machen Arbeit zum Hauptinhalt. Die Homepage funktioniert als kuratierter Index statt als generische Agenturargumentation.[^hellomonday]

### Dogstudio — analysiert

Showreel, Tonoption, starke Persönlichkeit und konkrete Cases erzeugen ein immersives Studioerlebnis. Ton muss freiwillig bleiben; Navigation, Fokusführung und Inhalt dürfen nicht hinter der Inszenierung verschwinden.[^dogstudio]

### Active Theory — eingeschränkt

Die Seite war ohne vollständige JavaScript-Ausführung nicht belastbar auslesbar. Räumliche oder experimentelle Eigenschaften werden daher erst nach einer erneuten interaktiven Prüfung bewertet.[^activetheory]

### Obys — analysiert

Ein großer Portfolioindex, Taxonomien und redaktionelle Raster inszenieren Design als Kuration. Die Informationsfülle ist inspirierend, kann aber ohne klare Einstiegspfade und mobile Priorisierung überfordern.[^obys]

### Resn — eingeschränkt

Die ausgelieferte Hülle enthielt zu wenig verlässlichen Inhalt für eine Detailanalyse. Die Referenz bleibt für eine spätere interaktive Prüfung markiert.[^resn]

### BASIC/DEPT® — analysiert

Typografischer Index, Reel und kulturell eingebettete Case Studies verbinden Portfolio und Haltung. Bewegungsinteraktion muss eine normale Bedienalternative behalten; Consent-Oberflächen brauchen gleichwertige Auswahlmöglichkeiten.[^basic]

### Build in Amsterdam — analysiert

Eine knappe Commerce-Positionierung, Showreel und ein fokussiertes Case-Raster reichen als Hauptargument. Die Seite zeigt den Wert von Auswahl: wenige starke Arbeiten statt vollständiger Leistungslisten.[^buildinamsterdam]

### Unseen Studio — analysiert

Optionaler Ton, räumliche Navigation und gefilterte Projekte erzeugen eine unverwechselbare Welt. Für reale Projekte sind eine lineare Alternative, sichtbarer Fokus, Touch-Bedienung und reduzierte Bewegung zwingend.[^unseen]

### Lusion — analysiert

3D, Storytelling, Showreel, Projekte und klar benannte Leistungen verbinden kreative Wirkung mit einem verständlichen Angebot. Diese Balance ist stärker als ein rein experimentelles Intro ohne Geschäftskontext.[^lusion]

### Cuberto — analysiert

Motion und 3D treffen auf klare Leistungen, ausführliche FAQ und praktische Projektinformationen. Die Referenz zeigt, dass expressive Oberflächen trotzdem auffindbar, erklärbar und geschäftlich konkret sein können.[^cuberto]

### Bruno Simon — analysiert

Ein vollständig steuerbares Portfolio nutzt Fahrphysik, sichtbare Steuerhinweise, Qualitätsoptionen, Respawn und mehrere Eingabegeräte. Das ist ein Spezialformat mit hohem Erinnerungswert, aber keine Standardvorlage für informationskritische Websites.[^bruno]

### Immersive Garden — analysiert

Großformatige Case-Narrative und luxuriöse Bildführung machen Portfolioarbeit zum Erlebnis. Der Ansatz verlangt sorgfältige Medienoptimierung und einen Inhaltszugang, der nicht von Animationen abhängt.[^immersive]

### Studio SPIN — eingeschränkt

Die Prüfung lieferte nur eine minimale, nicht ausreichend belastbare Darstellung. Vor einer Ableitung sind Desktop, Mobilgerät und Tastatur manuell zu prüfen.[^spin]

### Humaan — eingeschränkt

Ein Crawlerfehler verhinderte die verlässliche Analyse. Die Referenz wird nicht als Grundlage für konkrete Designentscheidungen verwendet, bis sie erneut geprüft wurde.[^humaan]

## Positiv- und Negativrollen

Der Katalog enthält bewusst beides. Beim Bauen werden beide Seiten gebraucht.

**Als Positivreferenz besonders ergiebig**

| Zweck | Referenzen |
|---|---|
| Produkt-UI, Dashboard, Verwaltung | **Data Console Dashboard**, Linear, Vercel |
| Objekt, Variante, Konfiguration | **180-Grad-Produktbetrachter**, Apple, Framer |
| Landing Page mit Leitbild | **INIZIO Solar**, Apple, Figma, Framer, Obys |
| Kernartefakt als Beweis | Linear, Vercel, Railway, Rive, ElevenLabs |
| redaktionelle Ruhe und Ernsthaftigkeit | Anthropic, OpenAI |
| Bewegung, die etwas erklärt | Rive, Spline, Jitter, Liveblocks |
| Wärme und Freundlichkeit ohne Kitsch | Notion, Figma, Hello Monday |
| dichte Information beherrschen | Stripe, Webflow, Linear |

**Als Negativreferenz zu verwenden**

| Muster | Referenz | Was daraus folgt |
|---|---|---|
| erwartbares Landingpage-Gerüst aus Hero, Kennzahlen, Featurekarten, Testimonials, CTA | DataFlow | Sektionen aus echten Nutzerfragen ableiten, nicht aus dem Schema |
| SaaS-Baukasten aus Features, Prozess, Testimonials, Preisen | Animated SaaS | jede Sektion muss einen eigenen Beweis tragen |
| Infrastrukturseite, die aussieht wie jede andere Infrastrukturseite | COMPUTE | eigene Systemwahrheit zeigen statt Kategoriekostüm |
| Terminaloptik ohne Systemlogik | Brutalist AI SaaS | Stil nur wählen, wenn das Produkt ihn trägt |
| gesperrte Versalzeile über jeder Sektionsüberschrift | INIZIO Solar | Einordnung in die Überschrift legen, siehe [[20-design/anti-ai-slop.md#Kicker und Überschriften]] |
| Kennzahlenband und Kundenstimmen ohne Beleg | INIZIO Solar | nur belegte Zahlen und benannte, eingewilligte Stimmen zeigen |

## Auswahlregel für Projekte

1. Führe für jedes Web-Produkt den [[90-references/reference-research-workflow.md]] aus und bestimme zuerst die Auftragszahl.
2. Bei genau einer Website entsteht ohne Nutzerreferenz ein Eigenentwurf. Der Pool muss nicht nach einer Vorlage durchsucht werden.
3. Bei mehreren Websites wird genau eine Fassung von genau einer konkreten Live-Seite geprägt, sofern starke Passung gefunden wird. Beginne nur für diese Fassung im [[90-references/website-reference-pool.md]]. Alle übrigen Fassungen bleiben Eigenentwürfe; ohne starke Passung dokumentiere die Suche und erzwinge kein zufälliges Beispiel.
4. Notiere bei der referenzgeführten Fassung Passungsbegründung, Übernahmetiefe, konkret übernommene Prinzipien, bewusste Abweichungen und tatsächlichen Einsatz im Master Spec. Herleite Eigenentwürfe aus Projektwahrheit, Inhaltsanker, Leitbenchmark und Nutzerfragen.
5. Prüfe die aktuelle Version einschließlich relevanter Bewegung erneut. Galerie-, Award-, Stilbibliotheks- und Sammlungsseiten sind Recherchewege, keine Leitreferenzen.
6. Gibt es keine überzeugende Passung, dokumentiere die geprüften Kandidaten und lasse alle Fassungen als `Eigenentwurf` weiterarbeiten.
7. Übersetze das Referenzprinzip nur in die benannte Fassung und dort in reale Marke, Inhalte, Tokens, Komponenten, Accessibility und Technik. Kopiere keine fremden Claims, Unternehmensfakten, Logos oder Identitätsmerkmale.

[^curriculum]: [Claude Code FULL COURSE: The Curriculum](https://claude-code-curriculum-deploy.vercel.app/)
[^motionsites]: [MotionSites AI: Premium AI Website Prompts](https://motionsites.ai/lesson)

[^benchdash]: Vom Nutzer am 6. August 2026 als Bild übergebene Dashboard-Aufnahme ohne öffentliche Quell-URL; Beschreibung beruht auf der direkten Bildauswertung.
[^benchrotate]: https://tutor-timer-28553736.figma.site/
[^benchsolar]: https://sixth-powder-95605714.figma.site/

[^rocket-a]: Als Vorlage oder Element verarbeitet: [comito](https://www.comito.de/), [ko:mon](https://www.ko-mon.de/), [jovoco](https://jovoco.io/), [metagram Solutions](https://metagram-solutions.com/), [Scaly](https://scaly.com/), [tunymedia](https://tunymedia.at/), [Dentalize](https://dentalize.de/), [Inno One](https://inno-one.de/), [ESP Media](https://espmedia.de/), [Fokus](https://fokus.so/), [Zahnarzt Wels](https://zahnarzt-wels.at/), [Sales Culture](https://sales-culture.de/), [Agency Invest](https://agencyinvest.de/), [Modulo Consulting](https://www.modulo-consulting.de/), [optiMICE](https://opti-mice.de/), [Martina Halek](https://martinahalek.de/).
[^rocket-b]: Nur als Bezug eines Presets, nicht neu bewertet: [car-tex](https://www.car-tex.de/), [Dr. Quidenus](https://drquidenus.at/), [Sacherer Partner](https://sacherer-partner.de/), [Zahnarztpraxis Uhlenhorst](https://zahnarztpraxis-uhlenhorst.de/), [Spedition Stuckmann](https://spedition-stuckmann.de/).

[^compute]: https://v0-compute-11.vercel.app/
[^dataflow]: https://v0-playful-engineering-landing-page.vercel.app/
[^brutalist]: https://v0-design-brutalist-ai-saa-s.vercel.app/
[^animated]: https://v0-saa-s-hero-section-blond.vercel.app/
[^apple]: https://www.apple.com/
[^stripe]: https://stripe.com/
[^linear]: https://linear.app/
[^vercel]: https://vercel.com/
[^framer]: https://www.framer.com/
[^webflow]: https://webflow.com/
[^notion]: https://www.notion.com/
[^figma]: https://www.figma.com/
[^anthropic]: https://www.anthropic.com/
[^openai]: https://openai.com/
[^elevenlabs]: https://elevenlabs.io/
[^runway]: https://runwayml.com/
[^perplexity]: https://www.perplexity.ai/
[^raycast]: https://www.raycast.com/
[^pitch]: https://pitch.com/
[^rive]: https://rive.app/
[^spline]: https://spline.design/
[^jitter]: https://jitter.video/
[^railway]: https://railway.com/
[^liveblocks]: https://liveblocks.io/
[^locomotive]: https://locomotive.ca/
[^hellomonday]: https://www.hellomonday.com/
[^dogstudio]: https://dogstudio.co/
[^activetheory]: https://activetheory.net/
[^obys]: https://obys.agency/
[^resn]: https://resn.co.nz/
[^basic]: https://www.basicagency.com/
[^buildinamsterdam]: https://www.buildinamsterdam.com/
[^unseen]: https://unseen.co/
[^lusion]: https://lusion.co/
[^cuberto]: https://cuberto.com/
[^bruno]: https://bruno-simon.com/
[^immersive]: https://immersive-g.com/
[^spin]: https://spin.co.uk/
[^humaan]: https://humaan.com/
