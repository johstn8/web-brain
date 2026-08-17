---
type: reference
status: canonical
updated: 2026-08-16
review_by: 2027-02-04
---

# Inspirationskatalog

> [!summary] Zweck
> Dieses Verzeichnis bewahrt Referenzen als analysierbare Quellen und unmittelbare kreative Bauquellen. Für ein Projekt werden passende Bilder, Designs, Layouts, Motion, Copy oder Code direkt eingesetzt oder kreativ adaptiert; der tatsächliche Einsatz wird anschließend dokumentiert und nicht vorab gesperrt.

## Prüfstatus

- **Analysiert:** Öffentlich erreichbare Seitenstruktur, Inhalte, Interaktionshinweise und technische Metadaten wurden am 3. August 2026 geprüft.
- **Eingeschränkt:** Die Seite war durch JavaScript, Bot-Schutz oder eine leere App-Shell nicht zuverlässig auslesbar. In diesen Fällen werden keine unbelegten visuellen Eigenschaften behauptet.
- `Analysiert` belegt keine vollständige Interaktionsprüfung. Statische Aufnahme, Motion, Tastatur, Mobil und Reduced Motion werden nach [[90-References/Reference Research Workflow]] getrennt nachgewiesen.
- Die drei Figma-Site-Benchmarks liefern ihre Oberfläche erst per JavaScript aus. Ihre Beschreibung beruht auf der Auswertung der ausgelieferten Stilvariablen, Bildassets und Textinhalte am 6. August 2026, nicht auf einer interaktiven Sitzung. Motion, Tastaturbedienung und mobiles Verhalten dieser drei Seiten sind damit **nicht** belegt und werden vor einer Übernahme dieser Aspekte erneut geprüft.
- Die Seiten können sich jederzeit ändern. Vor einer konkreten Übernahme muss die Referenz erneut geprüft werden.
- Lokale Momentaufnahmen der verbliebenen generierten Negativreferenzen und ihr aktueller Gültigkeitsstatus liegen im [[.research/screenshots/README|Screenshot Manifest]]. Sie sind Rechercheartefakte, keine freigegebenen Projektassets.

## Workflow- und Systemreferenzen

### Claude Code Curriculum — analysiert

Die Curriculum-Seite strukturiert KI-gestützte Webproduktion als Research, strukturierte Spezifikation, Design, Umsetzung und Verifikation. Zusätzlich trennt sie aktuellen Kontext, Projektgedächtnis und Langzeitwissen und behandelt Skills, MCP, Toolprüfung sowie Betrieb als Teil des Systems. Für dieses Brain übernommen wurden die verbindliche Inspirationsphase, Spec-first, Toolnachweise, Kritikschleife und Gedächtnisebenen. Nicht übernommen wurden produktspezifische Tooldefaults, externe Wissensspeicher als kanonische Basis, Marketing-Claims und pauschale Stackempfehlungen.[^curriculum]

### MotionSites AI — eingeschränkt analysiert

MotionSites veröffentlicht detaillierte Prompts für Landingpages und Hero-Sektionen in vielen Kategorien. Die frei sichtbaren Beschreibungen nennen Layout, Stil, Schrift, Animation, Responsive-Verhalten, Abhängigkeiten und Inhalte als Promptbausteine.[^motionsites] Für dieses Brain übernommen sind hohe Motion-Dichte, klare visuelle Leitmedien, choreografierte Scroll-Hierarchie und konkret ausformulierte Responsive-/Fallback-Regeln. Marken, Texte, Assets, Quellcode, externe Videos und Kompositionen können bei einem Projekt direkt eingesetzt oder kreativ adaptiert werden; ihr tatsächlicher Einsatz ist anschließend nach [[50-Legal/Assets Copyright and Licenses]] zu dokumentieren. Die dynamische Auslieferung erlaubte keine belastbare Vollprüfung jedes Prompts; konkrete Referenzen müssen projektbezogen erneut nach [[90-References/Reference Research Workflow]] geprüft werden.

## Vom Nutzer bewertete Benchmarks

> [!important] Vorrang
> Diese Referenzen hat der Nutzer ausdrücklich als gut oder als perfekte Messlatte benannt: vier am 6. August 2026, sieben weitere am 8. August 2026, StepSafer am 16. August 2026. Sie haben bei visuellen Entscheidungen Vorrang vor allen übrigen Einträgen dieses Katalogs. Die daraus abgeleiteten Regeln stehen kanonisch in [[20-Design/Interface Benchmarks]].

### Data Console Dashboard — analysiert, Bildvorlage

Vom Nutzer als Bild geliefert und als perfekte Benchmark für Design und UI bezeichnet. Ein Datenbank-Adminbereich auf weißer Fläche: Seitenleiste mit Marke oben und flacher Navigationsliste, aktiver Punkt als gefüllte fast schwarze abgerundete Fläche mit heller Schrift. Inhaltsbereich mit Seitentitel und einer grauen Erklärzeile, darunter vier gleich breite Kennzahlenfelder aus Beschriftung, Linienicon in eigener Farbe, großer Zahl und Veränderungswert. Darunter zwei ungleich breite Blöcke, „Storage Usage“ mit flachen Fortschrittsbalken und „Recent Activity“ mit rund getönten Icon-Trägern und Metazeilen im Muster `Name · Zeitangabe`, darunter ein voll breiter Block „System Health“ mit drei Spalten und grüner Statuspille. Abgrenzung ausschließlich über Hairline-Rahmen und Weißraum, eine Radiusstufe, keine Schatten, keine Verläufe, Farbe nur semantisch oder als kleiner Kategorieton. Als Positivreferenz für Produkt-UI ohne Einschränkung übertragbar.[^benchdash]

### 180-Grad-Produktbetrachter — analysiert

Vom Nutzer wegen des weich abgerundeten Charakters und des Zusammenspiels aus Objekt und Auswahl benannt. Eine einzelne Produktseite für einen Hoodie: ein freigestelltes schwarzes Objekt auf heller Studiofläche mit weichem Bodenschatten, benannte Ansichten wie `Front-Left View`, `Left Side View`, `Back-Left View`, dazu `Available Colors`, Größenauswahl mit `Size Guide` und eine kurze Detailliste mit Angaben wie `Unisex Regular` und `Machine Washable`. Der Betrachter selbst ist der Inhalt; Text tritt vollständig zurück. Übertragbar sind Objektfreistellung, Ansichtsreihe, weiche Auswahlformen und die extreme Textknappheit. Übertragbar ist ausdrücklich nicht das Erfinden einer Auswahlmechanik dort, wo es nichts zu wählen gibt.[^benchrotate]

### INIZIO Solar — analysiert, teilweise übertragbar

Vom Nutzer wegen des Leitbilds benannt. Eine Solaranbieterseite auf mattschwarzer Grundfläche mit einer einzigen kräftigen Signalfarbe im Neongrün-Bereich, dazu eine abstrakte grüne Wortmarke und großformatige Fotos von Anlage und Montageteam. Auftakt „Powering the Future with Solar Revolution“ mit einem erklärenden Satz und zwei Aktionen, danach vier bis sechs benannte Leistungen mit je einer Zeile, Werteabschnitt, Kennzahlenband, Kundenstimmen und Newsletter. Übertragbar sind das großformatige Leitbild des tatsächlichen Gegenstands, die eine Signalfarbe gegen dunkle Fläche und die knappe Leistungsgruppe. Ausdrücklich nicht übertragbar sind die gesperrten Versalzeilen über den Überschriften wie `COMPREHENSIVE SOLUTIONS` oder `CLIENT TESTIMONIALS`, die nach [[20-Design/Anti AI Slop#Kicker und Überschriften]] verbotene Kicker sind, sowie die Kennzahlen zu erzeugter Energie, Projektzahl, Zufriedenheit und Jahren Erfahrung und die namentlichen Kundenstimmen, für die kein Beleg vorliegt.[^benchsolar]

### ATS Resume Analyzer Dashboard — analysiert

Vom Nutzer als gefallendes Dashboard benannt. Eine Auswertungsoberfläche für Bewerbungen mit Kennzahlen wie `Total Applications`, `Average Score`, `Avg. Processing Time` und `Excellent Candidates`, einem Vergleich aus `Current Performance` und `Industry Benchmark`, festen Kategoriefarben für Fähigkeitsgruppen, ausgearbeiteten Leerzuständen wie `No Job Profiles Found` mit `Create your first job profile to get started.` sowie echten Einstellungen für Benachrichtigungen, Datenaufbewahrung, Export und Löschung. Übertragbar sind die Einordnung jeder Zahl über eine Vergleichsgröße, feste Kategoriefarben mit Beschriftung und die Ernsthaftigkeit der Leer- und Verwaltungszustände. Zu prüfen bleibt, dass jede angezeigte Funktion serverseitig real durchgesetzt wird.[^benchats]

### Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026

Der Nutzer hat am 8. August 2026 sieben live erreichbare Websites als gut in Design und Bedienung benannt, ausdrücklich für **Oberfläche, Bedienung, Animation und Kastengestaltung**, ausdrücklich **nicht** als Maßstab für Rechtstexte, Belege oder Inhaltswahrheit. Die daraus kanonisch abgeleitete Regel steht in [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]].

**Prüfstatus:** Ausgeliefertes Markup und die vollständigen CSS-Bündel wurden am 8. August 2026 abgerufen und ausgewertet. Belegt sind damit Tokenwerte, Radien, Rahmen- und Hoverrezepte, Keyframes, Easings, Blur- und Maskenwerte sowie die eingesetzten Bibliotheken. **Nicht** belegt sind Tastaturbedienung, Reduced-Motion-Verhalten und mobiles Verhalten dieser sieben Seiten; sie werden vor einer Übernahme dieser Aspekte nach [[90-References/Reference Research Workflow]] erneut geprüft.

| Seite | Rolle | Belegte Eigenschaften |
|---|---|---|
| Consile | Produkt-Landing mit Demo | Vollständiger eigener Keyframe-Satz: `hero-letter` mit `translateY(.4em)` und `blur(6px)` gegen null, `fade-in` mit 12 Pixel Versatz, `scale-in` von `.96`, `shimmer` als Flächenwanderung, `accordion-down`/`-up` für FAQ, `fin-panel-in` mit gleichzeitigem Maßstab und Versatz. Dekorative Hintergründe werden per `mask-image: radial-gradient(ellipse 70% 60% at 50% 40%, black, transparent 80%)` ausgeblendet statt hart beschnitten. Fluide Sektionspolster über `clamp()`. Drawer über Vaul.[^bm5consile] |
| CanDevsDoSomething | Community-Index | Tokenisierter `--radius` mit abgeleiteter Controlstufe `calc(var(--radius) - 2px)`, durchgehend Hairline `border-zinc-200` mit Dark-Gegenstück `zinc-800`, Kategorietöne ausschließlich als getönte Pille aus Farbe bei 100 hell und 900 bei 30 Prozent Deckung im Dunkelmodus. Linienicons aus Lucide in einer Strichstärke. Horizontal gewischte Reihen mit sichtbarem Bedienhinweis.[^bm5candevs] |
| Phillip Ohren | Beratungs-Portfolio | Leitmedium je Leistungskarte, Text direkt auf dem Bild, keine Rahmenkaskade, sehr große Sektionsabstände. Bestätigt die Wirkung von Weißraum als einziges Trennmittel.[^bm5ohren] |
| EVE BCN | Erlebnis-Buchung | Karten mit Bildfläche ohne Rahmen, linksbündige Detailhierarchie aus Dauer, Personenzahl und Preis, Aktion als `View →` in kleiner Stufe. Bestätigt die knappe, gestaffelte Metazeile statt Fließtext.[^bm5eve] |
| ClaudeFolio | Kuratiertes Verzeichnis | Das dichteste Hover-Vokabular des Sets: `hover:-translate-y-0.5` und `hover:-translate-y-px` auf klickbaren Karten, `transition-[transform,background-color,border-color,color]`, zwei Rahmenstufen `--color-border` und `--color-border-strong`, Hover hebt den Rahmen bis auf die Vordergrundfarbe. Kartenradius `10px`, Pillen `rounded-full`. Warme, sehr dunkle Grundfläche `#1d1a14`.[^bm5claudefolio] |
| Saad Salman | Fachprofil | Weicher, sehr flacher Hover-Schatten `0 8px 30px rgba(0,0,0,.06)` als einzige Tiefe, `rounded-2xl` für große Flächen, Kopfzeile `bg-background/70` mit `backdrop-blur-sm`, Hover setzt die Rahmenfarbe auf den Akzent.[^bm5saad] |
| Thomas Stockham | Entwickler-Portfolio | Vollständig ausgelesener Tokensatz: `bg #fafafa`, `surface #fff`, `surface-alt #f5f5f5`, `text #0a0a0a`, `text-secondary #525252`, `text-tertiary #a3a3a3`, `border #e5e5e5`, `border-hover #d4d4d4`, `accent #6366f1`, `accent-subtle #6366f114`. Radien `.25/.375/.5/.75/1/1.5rem`, Tracking `-.025em`, Standarddauer `.15s` mit `cubic-bezier(.4,0,.2,1)`, Ease-out `cubic-bezier(0,0,.2,1)`. `fade-in-up` als `opacity 0 + translateY(12px)` über `.5s ease-out both`. Statuspunkt `pulse-dot` als atmender Ring von 3 auf 6 Pixel bei sehr niedriger Deckung. Mono `JetBrains Mono` für Werte und Tags.[^bm5stockham] |

**Übertragbar und kanonisch übernommen**

- Der benannte Tokensatz einschließlich `border-hover` und `accent-subtle`. Diese zwei Rollen fehlten bisher und sind der Grund, weshalb Hoverzustände im eigenen Build flach wirkten. Kanonisch in [[20-Design/Color System#Tokenvertrag]].
- Das Kartenrezept aus Hairline im Ruhezustand und Rahmenaufhellung plus Ein- bis Zwei-Pixel-Lift beim Hover. Kanonisch in [[30-Frontend/Components and UI States#Kartenentscheidung]].
- Die durchscheinende Kopfzeile mit Blur und deckendem Fallback. Kanonisch in [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]].
- Die vierstufige Radiusskala und das negative Tracking großer Stufen. Kanonisch in [[20-Design/Typography Layout and Spacing#Radiusskala und Rahmenbehandlung]].
- Die Bewegungsrezepte mit konkreten Werten, insbesondere Reveal, Zeichenauftakt mit Blur, Maskenausblendung und Statuspunkt. Kanonisch in [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]].

**Ausdrücklich nicht übernommen**

- Der Verlaufstext aus Indigo, Violett und Pink bei Thomas Stockham. Das ist genau der Blau-Lila-Verlauf aus [[20-Design/Color System#Verbrauchte Farbwelten]] und bleibt verboten.
- Emojis als Sektionszeichen bei CanDevsDoSomething. Verboten nach [[20-Design/Anti AI Slop]].
- Die Verlaufsflächen als Ersatz für fehlende Vorschaubilder bei ClaudeFolio. Ein Platzhalter bleibt ein Befund nach [[20-Design/Imagery and AI Editing]], kein Gestaltungsmittel.
- Alles Rechtliche, alle Kennzahlen, Kundenlisten und Referenzangaben dieser sieben Seiten. Der Nutzer hat sie ausdrücklich vom Benchmarkstatus ausgenommen.
- Die Kartenraster als Standardantwort für jede Sektion. Das Verbot aus [[20-Design/Anti AI Slop]] bleibt unberührt; das Set liefert die Detailqualität der Kästen, nicht die Erlaubnis, alles in Kästen zu legen.

### StepSafer — analysiert am 16. August 2026, Copy-Benchmark

Vom Nutzer am 16. August 2026 als sehr gut benannt. Eine deutschsprachige Produktseite für eine Sprachassistenz in der Pflegedokumentation. Für dieses Brain ist sie vor allem ein **Text**-Benchmark, nicht in erster Linie ein visueller.

Belegt und übertragbar ist die Copy-Führung. Die Überschriften sind vollständige Aussagen mit Verb, etwa „Mehr Pflege. Weniger alles andere." oder „Wenn Pflege zur Verwaltung wird, verliert jeder.". Unter jeder Überschrift steht ein erklärender Fließtext von zwei bis vier Sätzen, nicht ein Kurzetikett. Die Satzlängen wechseln bewusst, ein sehr kurzer Satz wie „Ein Satz reicht." steht neben einem beschreibenden Satz aus dem Arbeitsalltag der Zielgruppe. Die Seite beschreibt das Problem in der Sprache der Nutzer, statt Eigenschaften zu behaupten, und sie kommentiert an keiner Stelle ihre eigene Machart. Die Aktionen sind über die ganze Seite hinweg gleich benannt.

Diese Eigenschaften sind in [[10-Strategy/Website Copy]] kanonisch verarbeitet. Nicht übertragbar sind die dortigen Zahlenangaben und Nutzenaussagen; für sie liegt kein Beleg vor, und die Beweisregeln aus [[10-Strategy/Content and Conversion#Beweis-Hierarchie]] gelten unverändert.[^stepsafer]

## Generierte und experimentelle Websites

Dieser Abschnitt wurde am 6. August 2026 auf reine Negativreferenzen reduziert. Die früher hier geführten generierten Beispielseiten trugen keine eigenständige Erkenntnis mehr und wurden entfernt; ihre übertragbaren Prinzipien stehen in [[90-References/Derived Design Patterns]] und in [[20-Design/Interface Benchmarks]].

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
| Produkt-UI, Dashboard, Verwaltung | **Data Console Dashboard**, ATS Resume Analyzer Dashboard, Linear, Vercel |
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
| gesperrte Versalzeile über jeder Sektionsüberschrift | INIZIO Solar | Einordnung in die Überschrift legen, siehe [[20-Design/Anti AI Slop#Kicker und Überschriften]] |
| Kennzahlenband und Kundenstimmen ohne Beleg | INIZIO Solar | nur belegte Zahlen und benannte, eingewilligte Stimmen zeigen |

## Auswahlregel für Projekte

1. Führe für jedes Web-Produkt den [[90-References/Reference Research Workflow]] aus und halte dessen Pflichtumfang ein.
2. Wähle je Rolle genau eine Referenz: Struktur, visuelle Sprache und Interaktionsidee. Bei mehreren Websites im Auftrag je Website eine eigene Kombination.
3. Benenne zusätzlich mindestens zwei Negativreferenzen und das daraus abgeleitete Verbot.
4. Notiere pro Referenz genau das zu übernehmende Prinzip und das zu vermeidende Risiko im Master Spec.
5. Prüfe die aktuelle Version einschließlich relevanter Bewegung erneut. Eine Referenz ist Inspiration, keine Anforderung.
6. Übersetze die Prinzipien in eigene Tokens, Komponenten, Inhalte und Belege.

[^curriculum]: [Claude Code FULL COURSE: The Curriculum](https://claude-code-curriculum-deploy.vercel.app/)
[^motionsites]: [MotionSites AI: Premium AI Website Prompts](https://motionsites.ai/lesson)

[^benchdash]: Vom Nutzer am 6. August 2026 als Bild übergebene Dashboard-Aufnahme ohne öffentliche Quell-URL; Beschreibung beruht auf der direkten Bildauswertung.
[^benchrotate]: https://tutor-timer-28553736.figma.site/
[^benchsolar]: https://sixth-powder-95605714.figma.site/
[^benchats]: https://pookie-blinders-777.figma.site/

[^bm5consile]: https://consile.app/
[^bm5candevs]: https://candevsdosomething.com/
[^bm5ohren]: https://phillipohren.com/
[^bm5eve]: https://evebcn.com/
[^bm5claudefolio]: https://claudefolio.com/
[^bm5saad]: https://saadsalman.org/
[^bm5stockham]: https://www.tstockham.com/
[^stepsafer]: https://www.stepsafer.de/

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
