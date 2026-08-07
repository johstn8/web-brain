---
type: canonical
status: canonical
updated: 2026-08-06
review_by: 2027-02-05
impacts:
  - accessibility
  - performance
  - component-states
  - routes
  - seo
---

# Motion and Interaction

## Verbindliches Motion-Niveau

Website-Aufträge erhalten eine hohe, inhaltsgetriebene Bewegungsdichte. Motion ist nicht auf den Hero oder ein einzelnes Reveal beschränkt: Jede fertig gebaute Website besitzt eine eigene Scroll-Choreografie über ihre verlinkten Unterseiten. Sie ist Teil der Informationsdramaturgie und wirkt nicht wie eine nachträglich aufgesetzte Effektsammlung.

Für jede primäre Inhaltsroute im Motion Inventory festhalten:

`Route -> Kapitel/Ziel -> Mechanik -> Trigger -> betroffene Elemente -> Zweck -> Start/Ende -> Dauer/Easing oder Scroll-Range -> Eingabemethode -> Unterbrechbarkeit -> Mobile-Verhalten -> Reduced-Motion-Variante -> Performance-Messung -> Testnachweis`

Die Website hat mindestens diese Ebenen:

1. **Globale Bewegung:** Route-Übergang oder klarer Seitenwechsel, Navigationszustand und eine unaufdringliche Fortschritts-/Orientierungsebene.
2. **Einstieg je Route:** Ein choreografierter Inhalts- und Medienauftakt, der den Text nicht versteckt oder die primäre Aktion verzögert.
3. **Scroll-Erzählung je primärer Inhaltsroute:** mindestens eine kontinuierlich scrollgebundene Sequenz und mindestens zwei weitere klar unterscheidbare In-View- oder scrollgetriggerte Bewegungen. Geeignet sind gestaffelte Informationsenthüllung, Ebenentiefe/Parallax, Bildausschnitt, Diagramm-/Prozessaufbau, Textmaskierung, horizontal geführte Galerie oder eine temporär klebende Kapitelinszenierung.
4. **Interaktionsdetails:** Press, Hover auf geeigneten Geräten, Fokus, Accordion, Tabs, Karten, Formular- und Zustandsfeedback. Diese Bewegung bestätigt die Handlung und bleibt unmittelbar.

Kompakte Pflicht- oder Rechtstextseiten brauchen keine künstliche Scrollinszenierung; Navigation, Seitenwechsel und Controls bleiben dennoch vollständig bewegt und zugänglich. Das Motion Inventory muss jede Ausnahme mit dem Seitenzweck begründen. Über die gesamten primären Inhaltsrouten dokumentiert jede Website mindestens zwölf eigenständige, sichtbare Bewegungsentscheidungen. Mehrere Elemente derselben Stagger-Gruppe zählen als eine Entscheidung.

## Interaktives Kernmodul

Jede Landing Page erhält zusätzlich zur Scroll-Choreografie **mindestens ein interaktives Kernmodul**: ein Element, das der Nutzer selbst bedient und das dabei etwas Wahres über den Betrieb zeigt. Das ist der wirksamste Unterschied zwischen einer animierten Seite und einer professionellen Seite: Der Nutzer handelt, statt zuzusehen.

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

Gibt es für ein Projekt nachweislich kein sinnvolles Modul, wird das im Design Contract begründet. Ersatzweise trägt dann ein scrollgebundenes Leitmedium nach [[20-Design/Interface Benchmarks#B3 Full-Bleed Leitbild-Landing]] den Auftakt.

## Choreografie statt Wiederholung

- Werden mehrere Websites beauftragt, erhält jede eine andere Bewegungsgrammatik, zum Beispiel editorielle Kapitelbewegung, produktnahe Interface-Choreografie oder räumlich-mediale Scroll-Erzählung. Sie darf Animationsreferenzen direkt übernehmen oder kreativ adaptieren.
- Scrollbewegung darf sichtbar mit Fortschritt gekoppelt sein, sie darf Leser aber nicht durch Scroll-Jacking, Zwangs-Scroll, unüberspringbare Intros oder gesperrte Navigation festhalten.
- Mindestens eine Scrollsequenz pro primärer Route verändert nicht nur Opazität: Sie erklärt eine räumliche Beziehung, einen Prozess, ein Produktdetail oder ein narratives Kapitel.
- Stagger, Parallax, Pinning, Clip/Mask, transformierende Medien, Zähler, SVG-Pfade und 3D/Canvas sind verfügbare Mittel. Auswahl und Kombination folgen Inhalt und Leitidee, nicht einer globalen Obergrenze.
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

## Medien, Eintritt und Belastung

- Inhalt wird nicht durch Introanimation blockiert. Medien starten erst, wenn ein sinnvoller Stillstand, Poster oder Kerninhalt verfügbar ist.
- Gemeinsame Einstiege dürfen 30–80 ms staffeln, ohne Fokus oder Interaktion aufzuhalten.[^emil]
- Bewegte Hero-Medien, Canvas und 3D erhalten sichtbare Steuerung, Pause-/Stopmöglichkeit, statische Alternative und ein realistisches Mobilbudget.
- Motion wird auf echtem Mobilprofil mit der vollständigen Route gemessen, nicht nur an einem isolierten Hero. Bei langen Frames oder beeinträchtigten CWV werden zuerst Runtime, Bildgewicht, Anzahl gleichzeitig aktiver Szenen und Paint/Layout-Effekte optimiert, nicht pauschal die geforderte Choreografie entfernt.

## Reduced Motion

Bei `prefers-reduced-motion: reduce` bleibt die Informations- und Seitenstruktur erhalten: Scroll-gekoppelte Positions-, Parallax-, Zoom-, Kamerafahrt- und Pin-Effekte werden zu einer unmittelbaren statischen Reihenfolge oder kurzen Opacity-/Farbwechseln. Interaktionsfeedback bleibt vorhanden, wenn es Funktion erklärt. Die Präferenz signalisiert einen Wunsch nach weniger nicht essenzieller Bewegung.[^mdn-reduced]

## Nachweis und Abnahme

Für jede gebaute Website belegen: Desktop und Mobil, Vorwärts- und Rückwärts-Scroll, schneller Scroll, Reload/Deep Link innerhalb einer Sequenz, Navigation während der Sequenz, Touch, Tastatur, Fehler-/Ladefallback, Reduced Motion und Performanceprofil. Ein Screenshot belegt nur einen Zustand; jede relevante Sequenz benötigt Trace oder Video sowie die Motion-Inventory-Zeile.

[^mdn-scroll]: [MDN: Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
[^motion-scroll]: [Motion: scroll](https://motion.dev/docs/scroll)
[^motion-react]: [Motion for React: useScroll](https://motion.dev/docs/react-use-scroll)
[^gsap-scrolltrigger]: [GSAP: ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
[^gsap-media]: [GSAP: matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/)
[^webdev-animation]: [web.dev: High-performance CSS animations](https://web.dev/articles/animations-guide)
[^mdn-reduced]: [MDN: Using media queries for accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility)
[^emil]: [Emil Kowalski: Animations on the Web](https://animations.dev/)
