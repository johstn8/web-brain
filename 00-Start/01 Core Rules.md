---
type: canonical
status: canonical
updated: 2026-08-23
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
- Pro Website eine fachlich passende konkrete Live-Seite als Leitreferenz suchen; bei mehreren Websites verschiedene Referenzen verwenden. Eine starke Referenz darf Struktur, visuelle Sprache und Motion prägen, ohne die reale Marke oder Inhalte zu ersetzen. Sammlungen sind nur Entdeckungsquellen; fehlt eine starke Passung, wird ein Eigenentwurf begründet. Siehe [[90-References/Reference Research Workflow]].
- Definiertes Farb-, Typografie-, Spacing-, Grid-, Radius-, Schatten- und Motion-System.
- Farbrollen und Bildsprache aus Marke, Produkt, Ort, Referenzen oder realem Material ableiten. Bilder, Designs und Animationen dürfen für den kreativen Build direkt eingesetzt oder adaptiert werden; ihr tatsächlicher Einsatz wird danach dokumentiert.
- Farbwelten werden aus Marke, Material, Inhalt und realem Kontext hergeleitet. Eine häufig verwendete Palette ist kein Verbot, aber ein unbegründeter Generator-Default ist ein Befund. Siehe [[20-Design/Color System#Häufige Defaults bewusst entscheiden]].
- Redundante oder rein dekorative Kicker über Überschriften vermeiden. Echte Rubrik-, Status-, Datums- oder Prozessinformation darf eine eigene Hierarchiestufe erhalten. Siehe [[20-Design/Anti AI Slop#Kicker und Überschriften]].
- Kopfzeileninventar und Navigationsmuster aus Informationsarchitektur, Nutzungshäufigkeit, Wortlängen und Art Direction ableiten. Es gibt keine globale Sollzahl. Siehe [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]].
- Ein gefundenes Firmenlogo wird in jeder gebauten Website sichtbar verwendet. Siehe [[20-Design/Design Direction#Logo des Betriebs]].
- Die Landing Page darf extravagant sein und bleibt dabei modern, übersichtlich und professionell. Siehe [[20-Design/Design Direction#Landing Page]].
- **Bei jedem Website-Build wird der UI UX Pro Max Skill verwendet, ausnahmslos.** Siehe [[00-Start/04 Plugins and Skills#Auslösebedingung]].
- Der Leitbenchmark stammt aus [[20-Design/Interface Benchmarks]] und wird im Design Contract benannt.
- **Die H0-Handwerksuntergrenze gilt bei jedem Build.** Zustände, Fokus, Kontextkontrast, klare Hierarchie und ein konsistentes System innerhalb der Website sind verbindlich. Radius, Rahmenbehandlung, Schatten, Karten, Kopfzeile, Zweitschrift, Flächen- und Bewegungslogik werden je Website entschieden. B5 ist ein wählbares Stilprofil. Siehe [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]].
- Der Tokenvertrag ist vor der ersten Komponente vollständig gesetzt, einschließlich `border-hover` und `accent-subtle`. Siehe [[20-Design/Color System#Tokenvertrag]].
- Radius-, Rahmen- und Tiefensystem werden je Website begründet und innerhalb dieser Website konsistent angewandt. Siehe [[20-Design/Typography Layout and Spacing#Radiusskala und Rahmenbehandlung]].
- Bewegung folgt einem je Website gesetzten Zeit- und Kurvensatz. B5-Werte sind kalibrierte Beispiele, keine globalen Defaults. Siehe [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]].
- Typografische Zeitbezüge sind erlaubt, wenn Marke und Inhalt sie tragen. Lesbarkeit, Rollenklarheit und konsequente Umsetzung entscheiden, nicht eine globale Verbotsliste. Siehe [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]].
- Bilder werden vor dem Einsatz auf Winkel, Ausschnitt, Hintergrund, Farbe und Auflösung geprüft und bei Bedarf mit KI überarbeitet oder freigestellt. Fehlt ein reales Bild, wird ein KI-Bild eingesetzt und nur im Projekt als `ai-placeholder` geführt, nie sichtbar auf der Website gekennzeichnet. Siehe [[20-Design/Imagery and AI Editing]].
- Informationen werden logisch gestaffelt und knapp gehalten. Textbudgets und die Dosierung am 375-Pixel-Viewport stehen in [[10-Strategy/Information Density and Mobile Clarity]].
- Interaktive Kernmodule werden eingesetzt, wenn Nutzer damit etwas Reales verstehen, prüfen, wählen oder erleben können. Ein starkes Leitbild, redaktioneller Aufbau oder direkter Beweis kann die bessere Lösung sein. Siehe [[20-Design/Motion and Interaction#Interaktives Kernmodul]].
- Mobile-first prüfen; Desktop darf komplexer, aber nicht funktional vollständiger sein.
- Motion erhält ein projektspezifisches Budget von `none`, `low`, `medium` oder `high`. Jede Bewegung braucht einen Zweck; `prefers-reduced-motion` wird respektiert. Siehe [[20-Design/Motion and Interaction]].
- Konsistenz schlägt Neuheit. Abweichungen brauchen eine dokumentierte Funktion.
- Die Anzahl der Websites steht im Auftrag: keine Angabe bedeutet genau eine Website, eine genannte Zahl bedeutet genau diese Anzahl. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]]. Jede gebaute Website ist eigenständig und vollständig und hat Art Direction, ein begründetes Motion-Budget und vollständige Unterseiten. Auf dem Server `217.154.218.30` läuft sie ohne festen lokalen Projektport über `johannstein.com`; auf anderen Rechnern gilt die Portregel aus [[60-Operations/Delivery and Local Start]]. Mehrere Websites unterscheiden sich auf mindestens fünf für den Auftrag wirksamen Achsen der [[20-Design/Design Direction#Stilabstand bei mehreren Websites|Unterscheidungsmatrix]].

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
- Jede Website führt ein eigenes `release-readiness/<website-slug>.md` nach [[60-Operations/Release Readiness Register]]. Es sammelt technische Sperren, unfertige sichtbare Hinweise, reale E-Mail-/Formularnachweise, Indexierungs-Cutover und offene Owner-Entscheidungen.
- Kostenwirksame APIs erhalten Quoten, Budgets, Timeouts, Retries und Alerts.
- Bei Account-Löschung zuerst aktive Abonnements sicher beenden, Ergebnis bestätigen, dann löschbare Daten entfernen.
- Für lokale Full-Stack-Projekte außerhalb des Servers `217.154.218.30` je ein Ein-Klick-Start für Windows, macOS und Linux bereitstellen. Auf diesem Server erfolgt Zugriff über `johannstein.com` ohne projektspezifisches `start-local.sh`.
