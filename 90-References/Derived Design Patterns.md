---
type: canonical
status: canonical
updated: 2026-08-08
depends_on:
  - "[[90-References/Inspiration Catalog]]"
---

# Abgeleitete Designmuster

> [!important] Einordnung
> Diese Muster sind redaktionelle Schlussfolgerungen aus dem [[Inspiration Catalog]], keine Aussagen der referenzierten Anbieter. Sie helfen bei der Wahl einer eigenständigen Richtung.
>
> Bei einem Konflikt mit [[20-Design/Interface Benchmarks]] gilt die Benchmark-Notiz, weil sie die ausdrücklich vom Nutzer bewerteten Oberflächen beschreibt.

## Was professionell wirkt

Professionelle Websites verbinden fünf Eigenschaften:

1. **Eine erkennbare Leitidee:** Typografie, Bildsprache, Layout und Bewegung folgen demselben Konzept.
2. **Das Produkt oder die Arbeit als Beweis:** Interface, Ergebnis, Case, Medium oder reales Artefakt ersetzt abstrakte Behauptungen.
3. **Belastbare Glaubwürdigkeit:** Kunden, Zahlen, Zitate und Zertifikate sind konkret, aktuell und belegbar.
4. **Redaktionelle Hierarchie:** Jede Sektion erfüllt eine andere Frage; Wiederholung ist bewusst, nicht automatisch.
5. **Vollständiges Verhalten:** Mobilansicht, Fokus, Ladezustand, Fehler, leere Zustände und reduzierte Bewegung gehören zur Gestaltung.

## Fünf tragfähige Archetypen

### Produktbeweis

Geeignet für SaaS, Entwicklerwerkzeuge und Plattformen.

**Dramaturgie:** Problem → direkt nutzbare oder realistische Demo → Kernworkflow → Integrationen → Sicherheit und Betrieb → Belege → Einstieg.

**Gestaltung:** Produktoberflächen sind das Leitmedium. Animation erklärt Zustandswechsel. Code, Diagramme und technische Texte erscheinen nur, wenn sie der Zielgruppe helfen.

**Risiko:** Eine erfundene Oberfläche ist dekorativer als eine abstrakte Illustration, aber nicht glaubwürdiger.

### Redaktioneller Index

Geeignet für Studios, Portfolios, Forschung und inhaltsreiche Marken.

**Dramaturgie:** klare Positionierung → kuratierte Beiträge oder Cases → Taxonomie → vertiefende Seiten → Kontakt oder nächste Lektüre.

**Gestaltung:** Typografie, Raster, Bildauswahl und Reihenfolge tragen die Identität. Filter dienen echter Orientierung.

**Risiko:** Ein vollständiges Archiv ohne Priorität wird zur Datenwand.

### Immersive Erzählung

Geeignet für besondere Kampagnen, Kultur, räumliche Produkte oder ein einzelnes starkes Narrativ.

**Dramaturgie:** Einladung und Bedienhinweis → Kapitel → interaktive Entdeckung → verständliche Zusammenfassung → klare Folgeaktion.

**Gestaltung:** 3D, Video, Ton oder Scroll-Choreografie tragen Bedeutung. Ton beginnt nur nach Einwilligung. Qualität ist anpassbar.

**Risiko:** Die Inszenierung darf Inhalt, Navigation, Barrierefreiheit und mobile Nutzung nicht blockieren.

### Brutalistisches Operationssystem

Geeignet für technische Produkte mit glaubwürdiger Systemnähe.

**Dramaturgie:** Status oder Kernfunktion → operative Daten → Prozess → Kontrolle und Sicherheit → Dokumentation oder Start.

**Gestaltung:** harte Raster, Monospace, nummerierte Bereiche und begrenzte Farben. Dichte wird durch strenge Ausrichtung beherrscht.

**Risiko:** Terminaloptik ohne echte Systemlogik ist Kostüm. Kleine Schrift und niedrige Kontraste zerstören den Nutzen.

### Produktkampagne

Geeignet für physische Produkte, Events und zeitlich begrenzte Veröffentlichungen.

**Dramaturgie:** unverwechselbares Produktbild → wichtigste Eigenschaft → Varianten oder Programm → Anwendung → Verfügbarkeit → Kauf oder Anmeldung.

**Gestaltung:** Produkt, Verpackung, Ort oder Eventmotiv bestimmt Farbe und Form. Die Seite darf lauter sein als eine langlebige Produktplattform.

**Risiko:** Dringlichkeit, Social Proof und Kennzahlen dürfen nicht simuliert werden.

## Kombinationsregel

Wähle einen primären Archetyp und höchstens einen unterstützenden. Beispielsweise kann eine SaaS-Seite primär **Produktbeweis** und sekundär **redaktioneller Index** für ihre Ressourcen nutzen. Eine Mischung aller Stile erzeugt keine Eigenständigkeit, sondern visuelles Rauschen.

## Kompositionsprinzipien

- Beginne nicht automatisch mit Badge, großer Überschrift, Unterzeile und zwei Buttons. Wähle eine Auftaktkomposition, die nur zu diesem Inhalt passt.
- Setze **keinen Kicker über eine Überschrift**. Verbindlich nach [[20-Design/Anti AI Slop#Kicker und Überschriften]].
- Nutze pro Sektion eine neue Aufgabe: orientieren, erklären, beweisen, vergleichen, absichern oder handeln lassen.
- Zeige ein Kernartefakt früh. Bei Software ist das oft die Oberfläche, bei Agenturen die Arbeit, bei Produkten das Produkt.
- Variiere Rhythmus über Maßstab und Weißraum, nicht über ständig neue Kartenstile.
- Verwende Wiederholung, wenn sie Lernen oder Marke unterstützt. Entferne sie, wenn nur dieselbe Behauptung neu verpackt wird.
- Gib längeren Seiten erkennbare Kapitel, Inhaltsanker oder Fortschritt, sofern dies die Orientierung verbessert.

## Anordnung von Überschriften

Aus den Referenzen lassen sich mehrere tragfähige Anordnungen ableiten. Wähle bewusst und wechsle innerhalb einer Seite begründet:

| Anordnung | Beobachtet bei | Wirkt | Geeignet für |
|---|---|---|---|
| Überschrift links, Inhalt rechts in eigener Spalte | Linear, Stripe | ruhig, scanbar | erklärende Abschnitte mit vielen Punkten |
| sehr große Überschrift über die volle Breite, Inhalt darunter versetzt | Obys, INIZIO Solar | laut, plakativ | Auftakt, Kampagne, Kapitelanfang |
| Überschrift mit Ziffer in derselben Zeile | brutalistische Systeme | ordnend | nummerierte Prozesse ohne Kicker |
| Überschrift als Bildunterschrift unter dem Medium | Apple, 180-Grad-Produktbetrachter | medienführend | Produkt, Ort, Arbeit als Beweis |
| Überschrift in eine schmale Randspalte gesetzt, Text daneben | redaktionelle Seiten | textführend | lange Inhaltsseiten |
| Überschrift überlappt das Medium oder wird angeschnitten | Studioseiten | expressiv | Landing Page mit starkem Kernartefakt |
| Überschrift zwischen zwei Inhaltsblöcken als Zäsur | Anthropic, OpenAI | gliedernd | lange Lesestrecken |

Prüfe bei jeder Anordnung: Lesereihenfolge im DOM, Fokusreihenfolge, Verhalten bei 320 Pixel, Verhalten bei 400 Prozent Zoom und Verhalten bei sehr langen Überschriften in anderen Sprachen.

## Landing Page mit Ausdruck

Die Startseite trägt den Ausdruck, die Unterseiten tragen die Verlässlichkeit. Aus dem Katalog übertragbar:

- **Kernartefakt sofort und groß**, wie beim 180-Grad-Produktbetrachter, bei Framer oder ElevenLabs. Das reale Produkt, die reale Arbeit oder der reale Ort ist der beste Effekt.
- **Typografie als Hauptmotiv**, wie bei Obys. Große Schrift ersetzt Dekoration und braucht keine erfundenen Zahlen.
- **Farbstatement statt Farbverlauf**, wie bei Figma oder INIZIO Solar. Eine kräftige Fläche mit klarer Herkunft wirkt stärker als jeder Verlauf.
- **Bewegung, die etwas erklärt**, wie bei Rive oder Railway. Der Effekt zeigt einen Zustand, einen Weg oder einen Zusammenhang.
- **Wärme über echte Motive**, wie bei Notion oder Figma. Freundlichkeit entsteht über Menschen, Handschrift, Illustration mit eigener Handschrift oder Farbe, nicht über Emojis.
- **Ruhige Zonen zwischen lauten Zonen.** Ohne Pause wirkt Ausdruck wie Lärm.

Negativabgleich: DataFlow und Animated SaaS im Katalog zeigen, wie eine Startseite aussieht, die nur erwartbare Blöcke aneinanderreiht. Wenn die eigene Landing Page dieser Beschreibung ähnelt, ist sie nicht fertig.

## Bewegungsbudget

| Ebene | Zweck | Richtwert |
|---|---|---|
| Mikro | Rückmeldung auf Eingabe | kurz, lokal, unterbrechbar |
| Komponenten | Zustandswechsel erklären | einmalig und zielgerichtet |
| Sektion | Aufmerksamkeit und Narrativ über Scroll führen | auf jeder primären Inhaltsroute bewusst choreografiert |
| Immersiv | Kern des Erlebnisses | hohe Dichte mit eigenem Fallback, Qualitätswahl und Abbruchmöglichkeit |

Bewegung darf weder Inhalte verzögern noch die Reihenfolge für Tastatur oder Screenreader verändern. Die reduzierte Variante bewahrt Information und Bedienbarkeit, nicht zwingend jeden visuellen Effekt.

## Muster gegen generische KI-Ästhetik

| Generisches Muster | Bessere Entscheidung |
|---|---|
| Kicker oder Eyebrow-Zeile über jeder Überschrift | Einordnung in die Überschrift selbst legen, Zusatzinformation in den Lead |
| beige oder cremefarbene Grundfläche als Signal für Hochwertigkeit | Neutralskala aus realem Material, Ort oder Produkt ableiten |
| Kopfzeile mit acht bis zwölf Menüpunkten | höchstens sechs Punkte, Rest in Fußbereich oder Unterseite |
| abstrakter Farbverlauf ohne Markenbezug | Farbidee aus Produkt, Material oder Inhalt ableiten |
| Karten für jeden Satz | semantisch passende Formen wie Liste, Vergleich, Demo oder Fließtext nutzen |
| erfundene Kennzahlen und Logos | verifizierte Belege oder ehrliche qualitative Aussagen |
| Sparkles, Emojis und Glows als Innovationssignal | konkrete Arbeitsweise oder Output zeigen |
| der einheitliche Karten-Hover als einzige Bewegung der Website | Der einheitliche kleine Lift ist die richtige System-Affordanz und bleibt; er ersetzt aber keine Erzählung. Zusätzlich pro Route eine inhaltsspezifische Choreografie nach [[20-Design/Motion and Interaction]] |
| Hoverbewegung auf Flächen, die nichts auslösen | Bewegung nur dort, wo sie eine Handlung ankündigt |
| große Icons mit sehr kleinem Text | Inhaltshierarchie über Typografie und Raum lösen |
| transparente Navigation über jedem Medium | Lesbarkeit und Zustand der Navigation explizit gestalten |
| viel Animation beim Laden | sofortiger Inhaltszugang, dann volle Scroll- und Interaktionschoreografie |

## Fallback für intensive Erlebnisse

Jede 3D-, Canvas-, Audio- oder schwere Videoseite definiert vor der Umsetzung:

- statische oder lineare Inhaltsalternative,
- Tastatur- und Touch-Bedienung,
- sichtbare Anweisungen und einen Weg zurück,
- freiwilligen Ton mit sichtbarem Stummschalter,
- reduzierte Bewegung,
- Qualitätsstufen oder vereinfachte Assets,
- Lade-, Fehler- und Nicht-WebGL-Zustand,
- messbares Gewicht und Laufzeitbudget.

## Anwendung im Projekt

Im [[80-Templates/Project Master Spec|Project Master Spec]] werden festgehalten:

- primärer und optionaler sekundärer Archetyp,
- drei projektspezifische visuelle Prinzipien,
- ein Kernartefakt, das früh als Beweis dient,
- die gewählte Anordnung für Auftakt und Sektionsarten,
- der sichtbare Einsatzort des Firmenlogos,
- explizit ausgeschlossene Stilklischees,
- hohes Bewegungsniveau, Route-Level-Motion Inventory und Fallback,
- Referenzen samt genauer Übernahme- oder Adaptionsabsicht.
