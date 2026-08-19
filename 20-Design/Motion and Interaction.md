---
type: canonical
status: canonical
updated: 2026-08-19
review_by: 2027-02-05
impacts:
  - accessibility
  - performance
  - component-states
  - routes
  - seo
---

# Motion and Interaction

## Motion-Budget

Jede Website entscheidet vor der Umsetzung ein Motion-Budget: `none`, `low`, `medium` oder `high`. Die Entscheidung folgt Zielgruppe, Inhalt, Nutzungshäufigkeit, Marke, Gerät, Performancebudget und gewünschter Aufmerksamkeit. Professionelle Qualität wird nicht an der Zahl sichtbarer Animationen gemessen.

Für jede tatsächlich eingesetzte, inhaltlich relevante Bewegung im Motion Inventory festhalten:

`Route -> Kapitel/Ziel -> Mechanik -> Trigger -> betroffene Elemente -> Zweck -> Start/Ende -> Dauer/Easing oder Scroll-Range -> Eingabemethode -> Unterbrechbarkeit -> Mobile-Verhalten -> Reduced-Motion-Variante -> Performance-Messung -> Testnachweis`

Mögliche Ebenen:

1. **Globale Bewegung:** Route-Übergang oder klarer Seitenwechsel, Navigationszustand und eine unaufdringliche Fortschritts-/Orientierungsebene.
2. **Einstieg je Route:** Ein choreografierter Inhalts- und Medienauftakt, der den Text nicht versteckt oder die primäre Aktion verzögert.
3. **Scroll-Erzählung:** nur wenn eine räumliche Beziehung, ein Prozess, ein Produktdetail oder ein narratives Kapitel dadurch verständlicher wird. Geeignet sind gestaffelte Informationsenthüllung, Ebenentiefe/Parallax, Bildausschnitt, Diagramm-/Prozessaufbau, Textmaskierung, horizontal geführte Galerie oder eine temporär klebende Kapitelinszenierung.
4. **Interaktionsdetails:** Press, Hover auf geeigneten Geräten, Fokus, Accordion, Tabs, Karten, Formular- und Zustandsfeedback. Diese Bewegung bestätigt die Handlung und bleibt unmittelbar.

Bei `none` bleiben nur unmittelbares Fokus-, Press-, Lade- und Zustandsfeedback, soweit funktional nötig. `low` konzentriert sich auf wenige Übergänge, `medium` darf Seitenrhythmus und Beweise choreografieren, `high` kann die Erfahrung tragen. Es gibt keine Mindestzahl. Eine statische Route muss ihre Ruhe nicht als Ausnahme rechtfertigen.

## Interaktives Kernmodul

Ein interaktives Kernmodul ist eine Option, wenn der Nutzer damit etwas Wahres über Angebot, Produkt, Prozess oder Auswahl besser verstehen kann. Es wird nicht erfunden, nur um eine Landing Page „interaktiv“ zu machen. Ein starkes Foto, Video, Fallbeispiel, Dokument, Produkt-Screenshot, redaktioneller Text oder klarer Kontaktweg kann der professionellere Beweis sein.

Geeignete Module, jeweils aus dem Gegenstand des Projekts abgeleitet:

| Modul | Passt zu | Zeigt |
|---|---|---|
| Ansichtsbetrachter mit gezogener Drehung | Produkt, Gerät, Fahrzeug, Anlage | Objekt von allen Seiten, siehe [[20-Design/Interface Benchmarks#B2 Rounded Selection Configurator]] |
| Varianten- und Größenauswahl mit sofortiger Bildaktualisierung | Sortiment, Ausstattung, Pakete | Auswahl und ihre Folge |
| Vorher-nachher-Regler | Sanierung, Reinigung, Montage, Gestaltung | reales Ergebnis |
| Rechner mit sofortigem Ergebnis | Kosten, Verbrauch, Laufzeit, Ersparnis | Nachvollziehbarkeit, nur mit belegten Formeln |
| Karte oder Grundriss mit anwählbaren Bereichen | Standorte, Gebäude, Anlagen, Gebiete | räumlicher Zusammenhang |
| Zeitachse oder Prozessstrecke, scrollgebunden aufgebaut | Ablauf, Projektphasen, Herstellung | Reihenfolge und Dauer |
| Live-Ausschnitt der echten Oberfläche | Software, Portal, Dashboard | das Produkt selbst |
| Filterbarer Arbeitsindex | Portfolio, Referenzen, Sortiment | Umfang und Auswahl |

Pflichten für jedes Kernmodul:

- Es beruht auf realen Daten, realen Bildern oder einer realen Oberfläche. Eine Attrappe ist ein Anti-Slop-Befund.
- Es ist mit Maus, Touch und Tastatur vollständig bedienbar und besitzt einen sichtbaren Fokus.
- Es hat einen sinnvollen Ausgangszustand, der schon ohne Interaktion etwas aussagt.
- Es reagiert unmittelbar und unterbrechbar; es lädt nicht sichtbar nach.
- Es besitzt einen Lade-, Fehler- und Leerzustand sowie eine statische Alternative bei `prefers-reduced-motion` und ohne JavaScript.
- Es fällt auf Mobil nicht weg, sondern erhält eine für Touch entworfene Fassung.
- Es steht mit Zweck, Datenquelle und Fallback im Motion Inventory.

Wird kein Kernmodul eingesetzt, nennt der Design Contract stattdessen die primäre Beweisform. Dafür ist keine Ausnahmebegründung nötig.

## Choreografie statt Wiederholung

- Werden mehrere Websites beauftragt, erhält jede eine andere Bewegungsgrammatik, zum Beispiel editorielle Kapitelbewegung, produktnahe Interface-Choreografie oder räumlich-mediale Scroll-Erzählung. Sie darf Animationsreferenzen direkt übernehmen oder kreativ adaptieren.
- Scrollbewegung darf sichtbar mit Fortschritt gekoppelt sein, sie darf Leser aber nicht durch Scroll-Jacking, Zwangs-Scroll, unüberspringbare Intros oder gesperrte Navigation festhalten.
- Jede eingesetzte Scrollsequenz erklärt eine räumliche Beziehung, einen Prozess, ein Produktdetail oder ein narratives Kapitel; bloßes Pflicht-Parallax ist ein Befund.
- Stagger, Parallax, Pinning, Clip/Mask, transformierende Medien, Zähler, SVG-Pfade und 3D/Canvas sind verfügbare Mittel. Auswahl und Kombination folgen Inhalt, Leitidee und Motion-Budget.
- Ein Inhalt ist vor, während und nach einer Sequenz lesbar. Sehbare Bewegung darf weder DOM- noch Fokusreihenfolge verändern.
- Autoplay-Medien haben sichtbare Pause-/Stopmöglichkeit; Ton startet nie ungefragt.

## Technische Umsetzung

- Für einfache scrollgebundene Effekte zuerst CSS Scroll- und View-Timelines einsetzen; sie koppeln Keyframes ohne JavaScript direkt an Scroll- oder Sichtfortschritt.[^mdn-scroll]
- Für React-/JavaScript-Projekte kann Motion `scroll` beziehungsweise `useScroll` Scrollfortschritt mit Animationen verbinden; für mehrteilige Timelines, Pinning oder komplexe Trigger ist GSAP ScrollTrigger zulässig.[^motion-scroll][^motion-react][^gsap-scrolltrigger]
- Scroll-Range, Triggerpunkte und Mobile-Varianten explizit definieren. Bei GSAP responsive Setups sauber an Medienqueries binden und beim Unmount/Routewechsel bereinigen.[^gsap-media]
- Für die Mehrzahl der Frames `transform` und `opacity` priorisieren; Layout- oder Paint-Effekte nur mit gemessener Begründung einsetzen.[^webdev-animation]
- `position: sticky` ist für Pin-Erlebnisse bevorzugt, wenn die Struktur dies ermöglicht. Keine harte Abhängigkeit von Smooth-Scroll-Bibliotheken erzeugen.
- Wenn native Scroll-Timelines oder die gewählte Runtime fehlen, bleibt die Inhaltsreihenfolge vollständig sichtbar; der Fallback nutzt In-View-Eintritt oder eine statische Komposition statt einer gestoppten oder unsichtbaren Szene.

## Entscheidungsrahmen

Vor jeder Motion-Entscheidung dokumentieren: `Häufigkeit -> Zweck -> Trigger -> Dauer/Easing oder Scroll-Range -> Unterbrechbarkeit -> Eingabemethode -> Reduced-Motion-Fallback -> Messung`.

- Wiederholte Tastaturaktionen und sehr häufige Bedienhandlungen bleiben sofort. Seltene Overlays, Drawers und bestätigende Zustandswechsel dürfen präzise animieren.
- Button- und Control-Feedback ist unmittelbar und klein, etwa `scale(0.95–0.98)` beim Drücken. Hover gilt nur bei `hover: hover` und `pointer: fine`.
- Popover und Tooltips starten vom auslösenden Element; zentrierte Modals bleiben zentriert. Folge-Tooltips dürfen ohne neue Verzögerung erscheinen.
- Dynamische UI verwendet unterbrechbare CSS-Transitions oder WAAPI. Keyframes eignen sich für vorbestimmte Abläufe. Springs sind für direkt manipulierbare Gesten mit echter Unterbrechbarkeit reserviert.
- UI-Motion ist meist unter 300 ms: Press 100–160 ms, Tooltip/Popover 125–200 ms, Select/Dropdown 150–250 ms, Modal/Drawer 200–500 ms. Scrollgebundene Sequenzen folgen der gewählten Scroll-Range und nicht einer künstlichen Wartezeit.[^emil]

## Kalibrierte Bewegungsbeispiele

Diese Werte beschreiben die Bewegungsgrammatik des wählbaren B5-Stilprofils. Sie sind aus den sieben Referenzen in [[20-Design/Interface Benchmarks#B5 Modern Neutral Craft Web]] ausgelesen und in [[90-References/Inspiration Catalog#Sieben-Seiten-Set „Modern Neutral Craft" — analysiert am 8. August 2026]] belegt. Sie sind **keine** kanonischen Basiswerte für jede Website. Jeder Website-Contract setzt seinen eigenen Zeit- und Kurvensatz; die Beispiele dürfen vollständig, teilweise oder gar nicht übernommen werden.

### Zeit- und Kurvensatz

| Token | Wert | Rolle |
|---|---|---|
| `ease-out` | `cubic-bezier(0, 0, .2, 1)` | Eintritt, Reveal, alles was erscheint |
| `ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Zustandswechsel, Farbe, Rahmen, Position |
| `ease-in` | `cubic-bezier(.4, 0, 1, 1)` | Austritt, alles was verschwindet |
| `dur-instant` | `100` bis `160 ms` | Press, Farbe, Rahmen, Hover |
| `dur-quick` | `150` bis `200 ms` | Tooltip, Popover, Kopfzeilenwechsel |
| `dur-normal` | `250` bis `300 ms` | Dropdown, Tab, Accordion |
| `dur-slow` | `400` bis `500 ms` | Reveal im Sichtbereich, Modal, Drawer |

Für eine Website, die diese Grammatik übernimmt, kann `150 ms` mit `ease-in-out` der Standard für Farb-, Rahmen- und Hoverübergänge sein.

### Die Rezepte

| Rezept | Werte | Einsatz |
|---|---|---|
| **Reveal** | `opacity: 0` und `translateY(12px)` gegen den Endzustand, `500 ms`, `ease-out`, Endzustand gehalten | möglicher B5-Eintritt eines Inhaltsblocks |
| **Stagger** | `30` bis `80 ms` Versatz je Element, höchstens sechs Elemente in einer Gruppe | Listen, Kartenreihen, Kennzahlenreihen |
| **Zeichen- oder Wortauftakt** | je Einheit `opacity: 0`, `translateY(0.4em)`, `blur(6px)` gegen null, `500` bis `700 ms`, `ease-out`, Versatz `20` bis `40 ms` | optionale B5-Auftaktzeile; der Text bleibt im Markup vollständig und für Screenreader eine Zeile |
| **Maßstabseintritt** | `scale(.96)` und `opacity: 0` gegen den Endzustand, `200` bis `300 ms`, `ease-out` | Popover, Menü, eingeblendetes Panel; startet am auslösenden Element |
| **Panel-Eintritt** | `scale(.9)` mit `translateY(12px)` gegen den Endzustand, `300 ms` | Modal, Drawer, überlagerndes Panel |
| **Karten-Hover** | `translateY(-1px)` bis `-2px` plus Rahmenwechsel auf `border-hover`, `150 ms`, `ease-out`, nur bei `hover: hover` und `pointer: fine` | optionale B5-Kartenvariante |
| **Press** | `scale(0.95)` bis `0.98`, `100` bis `160 ms` | jeder pressbare Control |
| **Accordion** | Höhe von null auf die Inhaltshöhe, `200` bis `300 ms`, `ease-in-out`, Gegenrichtung symmetrisch | FAQ, aufklappbare Abschnitte |
| **Atmender Statusring** | `box-shadow` von `0 0 0 3px` bei 25 Prozent Deckung auf `0 0 0 6px` bei 10 Prozent und zurück, `2 s`, unendlich | ausschließlich echte Live-Zustände |
| **Wandernde Aufhellung** | Hintergrundposition von `-200%` nach `200%`, `1.5` bis `2 s`, unendlich, nur solange geladen wird | Ladeplatzhalter |
| **Weiche Maskenausblendung** | `mask-image: radial-gradient(ellipse 70% 60% at 50% 40%, black, transparent 80%)` | dekorative Hintergründe, Raster, Leuchtflächen. Sie enden weich statt an einer harten Kante |
| **Zähler** | einmal beim ersten Sichtbarwerden auf den Zielwert, `800` bis `1200 ms`, tabellarische Ziffern, Endwert steht im Markup | belegte Kennzahlen |

### Handwerklich bindende Nebenbedingungen

- Für die Mehrzahl der Frames nur `transform`, `opacity` und `filter`. `will-change: transform` nur auf tatsächlich dauerhaft bewegten Elementen und dort begrenzt.
- Ein Reveal lässt den Inhalt nach dem Eintritt zugänglich und stabil. Wiederholtes Verbergen braucht einen dokumentierten Informationszweck.
- Startversatz, Unschärfe und Dauer werden je Website so kalibriert, dass nichts sichtbar springt oder die Lesereihenfolge verzögert.
- Ein Zeichenauftakt darf die primäre Aktion nicht verzögern und wird nur verwendet, wenn er zur gewählten Bewegungsgrammatik gehört.
- Bei `prefers-reduced-motion: reduce` fallen Versatz, Maßstab, Unschärfe, atmender Ring, wandernde Aufhellung und Zähler weg. Reveal wird zu einem Opazitätswechsel unter `200 ms` oder zum sofortigen Endzustand. Press- und Fokusfeedback bleiben, weil sie Funktion erklären.
- Wird dieses B5-Beispielset übernommen, stehen Auswahl und Abweichungen im Motion Inventory. Eine andere konsistente Bewegungsgrammatik ist kein Befund.

## Medien, Eintritt und Belastung

- Inhalt wird nicht durch Introanimation blockiert. Medien starten erst, wenn ein sinnvoller Stillstand, Poster oder Kerninhalt verfügbar ist.
- Gemeinsame Einstiege dürfen 30–80 ms staffeln, ohne Fokus oder Interaktion aufzuhalten.[^emil]
- Bewegte Hero-Medien, Canvas und 3D erhalten sichtbare Steuerung, Pause-/Stopmöglichkeit, statische Alternative und ein realistisches Mobilbudget.
- Motion wird auf echtem Mobilprofil mit der vollständigen Route gemessen, nicht nur an einem isolierten Hero. Bei langen Frames oder beeinträchtigten CWV werden zuerst Runtime, Bildgewicht, Anzahl gleichzeitig aktiver Szenen und Paint/Layout-Effekte optimiert, nicht pauschal die geforderte Choreografie entfernt.

## Reduced Motion

Bei `prefers-reduced-motion: reduce` bleibt die Informations- und Seitenstruktur erhalten: Scroll-gekoppelte Positions-, Parallax-, Zoom-, Kamerafahrt- und Pin-Effekte werden zu einer unmittelbaren statischen Reihenfolge oder kurzen Opacity-/Farbwechseln. Interaktionsfeedback bleibt vorhanden, wenn es Funktion erklärt. Die Präferenz signalisiert einen Wunsch nach weniger nicht essenzieller Bewegung.[^mdn-reduced]

## Gestengeführte Bewegung

Führt der Nutzer eine Bewegung selbst, also beim Ziehen, Wischen, bei Sheets, Slidern, Karussells und beim Momentum nach dem Loslassen, gelten zusätzlich die Muster aus [[90-References/Apple Fluid Interface]]: Rückmeldung ab dem Drücken, Eins-zu-eins-Führung mit Griffversatz, Start jeder neuen Bewegung beim aktuell dargestellten Wert, Übergabe der Loslassgeschwindigkeit, projizierte Ruhelage statt nächstgelegener Kante und weicher Widerstand an Grenzen. Für gestengeführte Bewegung sind Keyframes ungeeignet, weil sie nicht mitten im Lauf gegriffen werden können. Die Werte dieser Notiz bleiben bei einem Widerspruch maßgeblich.

## Nachweis und Abnahme

Vor der Abnahme wird `review-animations` nach [[00-Start/04 Plugins and Skills#Review Animations]] je gebauter Website ausdrücklich aufgerufen. Jeder Befund wird behoben oder mit Grund im Decision Log festgehalten.

Für jede gebaute Website belegen: Desktop und Mobil, Vorwärts- und Rückwärts-Scroll, schneller Scroll, Reload/Deep Link innerhalb einer Sequenz, Navigation während der Sequenz, Touch, Tastatur, Fehler-/Ladefallback, Reduced Motion und Performanceprofil. Ein Screenshot belegt nur einen Zustand; jede relevante Sequenz benötigt Trace oder Video sowie die Motion-Inventory-Zeile.

[^mdn-scroll]: [MDN: Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
[^motion-scroll]: [Motion: scroll](https://motion.dev/docs/scroll)
[^motion-react]: [Motion for React: useScroll](https://motion.dev/docs/react-use-scroll)
[^gsap-scrolltrigger]: [GSAP: ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
[^gsap-media]: [GSAP: matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/)
[^webdev-animation]: [web.dev: High-performance CSS animations](https://web.dev/articles/animations-guide)
[^mdn-reduced]: [MDN: Using media queries for accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility)
[^emil]: [Emil Kowalski: Animations on the Web](https://animations.dev/)
