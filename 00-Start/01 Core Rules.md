---
type: canonical
status: canonical
updated: 2026-08-17
impacts:
  - "[[80-Templates/Project Master Spec]]"
  - "[[70-QA/Quality Gates]]"
---

# Core Rules

## Produkt

- Beginne mit Zielgruppe, Problem, primärer Aktion und messbarem Erfolg. Kein Design vor klarer Aufgabe.
- Erstelle und pflege immer eine menschenlesbare Seitenstruktur plus technische `sitemap.xml`. Jede gebaute Website enthält echte, verlinkte Unterseiten; eine lange Startseite mit Ankern ist kein Ersatz für diese Seitenarchitektur.
- Jede Seite hat genau ein primäres Ziel, eine klare Hierarchie und belastbare Inhalte.
- Behauptungen benötigen Beleg oder werden als Annahme gekennzeichnet.

## Design

- Ein visuelles Leitmotiv statt Effekt-Sammlung.
- Definiertes Farb-, Typografie-, Spacing-, Grid-, Radius-, Schatten- und Motion-System.
- Farbrollen und Bildsprache aus Marke, Produkt, Ort, Referenzen oder realem Material ableiten. Bilder, Designs und Animationen dürfen für den kreativen Build direkt eingesetzt oder adaptiert werden; ihr tatsächlicher Einsatz wird danach dokumentiert.
- Keine verbrauchte Farbwelt als dominante Fläche, insbesondere kein Beige oder Creme als Hauptfarbe. Siehe [[20-Design/Color System#Verbrauchte Farbwelten]].
- Kein Kicker über einer Überschrift. Siehe [[20-Design/Anti AI Slop#Kicker und Überschriften]].
- Kopfzeile mit höchstens sechs Navigationspunkten; kein Text und kein Knopf in der Kopfzeile bricht um. Siehe [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]].
- Ein gefundenes Firmenlogo wird in jeder gebauten Website sichtbar verwendet. Siehe [[20-Design/Design Direction#Logo des Betriebs]].
- Die Landing Page darf extravagant sein und bleibt dabei modern, übersichtlich und professionell. Siehe [[20-Design/Design Direction#Landing Page]].
- **Bei jedem Website-Build wird der UI UX Pro Max Skill verwendet, ausnahmslos.** Siehe [[00-Start/04 Plugins and Skills#Auslösebedingung]].
- Der Leitbenchmark stammt aus [[20-Design/Interface Benchmarks]] und wird im Design Contract benannt.
- **Die H0-Handwerksuntergrenze gilt bei jedem Build.** Zustände, Fokus, Kontextkontrast, ruhende Flächen ohne dekorativen Schatten, Hairlines als mögliches Abgrenzungsmittel und ein konsistentes System innerhalb der Website sind verbindlich. Radius, Rahmenbehandlung, Karten, Kopfzeile, Zweitschrift, Flächen- und Bewegungslogik werden je Website entschieden. B5 ist ein wählbares Stilprofil. Siehe [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]].
- Der Tokenvertrag ist vor der ersten Komponente vollständig gesetzt, einschließlich `border-hover` und `accent-subtle`. Siehe [[20-Design/Color System#Tokenvertrag]].
- Radius-, Rahmen- und Tiefensystem werden je Website begründet und innerhalb dieser Website konsistent angewandt; im Ruhezustand kein dekorativer Schatten. Siehe [[20-Design/Typography Layout and Spacing#Radiusskala und Rahmenbehandlung]].
- Bewegung folgt einem je Website gesetzten Zeit- und Kurvensatz. B5-Werte sind kalibrierte Beispiele, keine globalen Defaults. Siehe [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]].
- Keine Retro-Anmutung: keine Epochen-Displayschrift, keine alte Buchserife als Markenschrift, keine Serife plus Erdton plus Ornament. Siehe [[20-Design/Typography Layout and Spacing#Retro-Verbot]].
- Bilder werden vor dem Einsatz auf Winkel, Ausschnitt, Hintergrund, Farbe und Auflösung geprüft und bei Bedarf mit KI überarbeitet oder freigestellt. Fehlt ein reales Bild, wird ein KI-Bild eingesetzt und nur im Projekt als `ai-placeholder` geführt, nie sichtbar auf der Website gekennzeichnet. Siehe [[20-Design/Imagery and AI Editing]].
- Informationen werden logisch gestaffelt und knapp gehalten. Textbudgets und die Dosierung am 375-Pixel-Viewport stehen in [[10-Strategy/Information Density and Mobile Clarity]].
- Jede Landing Page besitzt mindestens ein interaktives Kernmodul nach [[20-Design/Motion and Interaction#Interaktives Kernmodul]].
- Mobile-first prüfen; Desktop darf komplexer, aber nicht funktional vollständiger sein.
- Motion ist ein tragendes Gestaltungsmittel: Jede Website erhält eine bewusst hohe, inhaltsgeleitete Dichte aus Scroll-, Eintritts-, Übergangs- und Interaktionsbewegung nach [[20-Design/Motion and Interaction]]. `prefers-reduced-motion` respektieren.
- Konsistenz schlägt Neuheit. Abweichungen brauchen eine dokumentierte Funktion.
- Die Anzahl der Websites steht im Auftrag: keine Angabe bedeutet genau eine Website, eine genannte Zahl bedeutet genau diese Anzahl. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]]. Jede gebaute Website ist eigenständig und vollständig und hat Art Direction, Motion-Choreografie und vollständige Unterseiten. Auf dem Server `217.154.218.30` läuft sie ohne festen lokalen Projektport über `johannstein.com`; auf anderen Rechnern gilt die Portregel aus [[60-Operations/Delivery and Local Start]]. Mehrere Websites unterscheiden sich auf jeder Pflichtachse der [[20-Design/Design Direction#Stilabstand bei mehreren Websites|Unterscheidungsmatrix]].

## Engineering

- Bei Erstellung und jedem Update wird je Inhaltsblock dokumentiert, ob der Owner ihn ohne Builder bearbeiten darf, mit stabilem JSON-Pointer, Feldtyp, Grenzen, Preview-Routen und Veröffentlichungspolicy. Bei Owner-Hosting folgt der Vertrag [[80-Templates/Owner Hosting Website Contract]].
- Die öffentliche Website bleibt statisch. Das Owner-Dashboard ist eine einzige zentrale Anwendung unter `/srv/Web-Design/projekte/owner-hosting/`, wird nicht je Kundenprojekt kopiert und veröffentlicht über einen getrennten Worker neue statische Builds. Siehe [[60-Operations/Owner Hosting and Dashboard]].
- Semantisches HTML und progressive Verbesserung zuerst.
- Jede Interaktion besitzt Default-, Hover-, Focus-, Active-, Disabled-, Loading-, Success-, Error- und Empty-Zustände, soweit anwendbar.
- Server validiert Eingaben, Autorisierung und Geschäftsregeln. Secrets bleiben serverseitig.
- Performancebudgets, Accessibility, Security, SEO und Monitoring gehören zur Definition of Done.
- Eine Styling- und Komponentenstrategie pro Projekt.

## Copy

- Die Seite spricht mit dem Nutzer und kommentiert nie sich selbst. Keine Meta-Sätze, keine sichtbaren Pflegedaten wie „Stand …“, keine Quellenversicherungen, keine Negativabgrenzung und keine Selbstverständlichkeiten. Kanonisch in [[10-Strategy/Website Copy]].
- Unter einer Überschrift steht entweder nichts oder ein echter Satz, nie ein verbloses Kurzstatement.
- Die Dreierfigur wird nur verwendet, wenn es sachlich drei Dinge sind. Sonst bestimmt die Sache die Anzahl.
- Kein Em-Dash, kein Semikolon, kein Gedankenstrich als Einschub, kein Doppelpunkt als Spannungszeichen.
- Ganze Sätze sind erwünscht. Eine Hakenliste über reale Leistungen ergänzt sie, ersetzt sie aber nicht.

## Marke und Anti-Slop

- Keine Blau-Lila-Verläufe ohne Markenbegründung.
- Keine Eyebrow-Pills, Sparkles, Emoji-Icons, Fake-Testimonials oder leeren Logo-Walls.
- Keine generischen Claims wie „Build your dreams“. Konkretes Ergebnis, Zielgruppe und Differenz nennen.
- Kein Link, Button, Tab, Carousel oder Social Icon ohne reale Funktion.
- Website-Titel kurz, beschreibend, ohne `|`; Favicon-Set ist Pflicht.

## Recht und Betrieb

- Die kreative und technische Umsetzung verwendet alle gewünschten Bilder, Designs, Animationen und sonstigen Assets unmittelbar. Die KI baut keine rechtlich motivierten Ersätze, Ausschlüsse, Asset-Sperren oder Parallelfassungen.
- Danach dokumentiert `SOURCE-RIGHTS-REVIEW.md` Quelle, tatsächlichen Einsatz und offene Prüfhinweise als zweiter, vom Build getrennter Schritt. Der Nutzer beziehungsweise benannte Owner entscheidet allein über Veröffentlichung und etwaige spätere Änderungen; die KI trifft dazu keine Asset- oder Urheberrechtsentscheidung.
- Datenschutz, Consent, Impressum und Barrierefreiheit werden anhand realer Datenflüsse und Zielmärkte als prüfpflichtige Entwürfe erfasst; dies unterbricht den Build nicht.
- Kostenwirksame APIs erhalten Quoten, Budgets, Timeouts, Retries und Alerts.
- Bei Account-Löschung zuerst aktive Abonnements sicher beenden, Ergebnis bestätigen, dann löschbare Daten entfernen.
- Für lokale Full-Stack-Projekte außerhalb des Servers `217.154.218.30` je ein Ein-Klick-Start für Windows, macOS und Linux bereitstellen. Auf diesem Server erfolgt Zugriff über `johannstein.com` ohne projektspezifisches `start-local.sh`.
