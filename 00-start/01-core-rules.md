---
type: canonical
status: canonical
updated: 2026-11-05
impacts:
  - "[[80-templates/project-master-spec.md]]"
  - "[[70-qa/quality-gates.md]]"
---

# Core Rules

## Produkt

- Beginne mit Zielgruppe, Problem, primärer Aktion und messbarem Erfolg. Kein Design vor klarer Aufgabe.
- Erstelle und pflege immer eine menschenlesbare Seitenstruktur plus technische `sitemap.xml`. Jede gebaute Website enthält echte, verlinkte Unterseiten; eine lange Startseite mit Ankern ist kein Ersatz für diese Seitenarchitektur.
- Jede Seite hat genau ein primäres Ziel, eine klare Hierarchie und belastbare Inhalte.
- Behauptungen benötigen Beleg oder werden als Annahme gekennzeichnet.

## Design

- **Vorrang der Vorbilder.** Eine Website entsteht aus dem Aufbau einer konkreten guten Seite, nicht aus diesen Regeln. Ausgangspunkt ist eine Vorlage aus [[30-frontend/web-kit.md#Website-Vorlagen]] oder eine vom Nutzer genannte Website. Alles in diesem Abschnitt gilt nur, soweit das Vorbild es nicht anders macht. Der Aufbau wechselt von Auftrag zu Auftrag; Text links, Bild rechts, Knöpfe darunter ist eine Möglichkeit von vielen und kein Standard.
- Ein visuelles Leitmotiv statt Effekt-Sammlung.
- **Vor jeder Website steht der Blick auf gute Seiten:** Vorlagen und Inspirationseingang zuerst, dazu der Gattungsvergleich nach [[90-references/reference-research-workflow.md#Gattungsvergleich]], soweit er neue Erkenntnis bringt.
- Eine Website darf von einem Vorbild stark geprägt sein; das ist der Normalfall. Bei mehreren Websites trägt jede ein anderes Vorbild.
- Definiertes Farb-, Typografie-, Spacing-, Grid-, Radius-, Schatten- und Motion-System.
- Farbrollen und Bildsprache aus Marke, Produkt, Ort, Referenzen oder realem Material ableiten. Bilder, Designs und Animationen dürfen für den kreativen Build direkt eingesetzt oder adaptiert werden; ihr tatsächlicher Einsatz wird danach dokumentiert.
- Farbwelten werden aus Marke, Material, Inhalt und realem Kontext hergeleitet. Eine häufig verwendete Palette ist kein Verbot, aber ein unbegründeter Generator-Default ist ein Befund. Siehe [[20-design/color-system.md#Häufige Defaults bewusst entscheiden]].
- **Sperren für Entwürfe ohne Vorbild:** keine Zeile über einer Überschrift, keine Nummern an Sektionen, kein farbig oder kursiv abgesetzter Teil einer Überschrift, kein Verlauf, der ein Foto ausblendet, keine drei gleich gebauten Sektionen in Folge. Sie fangen die typischen KI-Muster ab. Macht das Vorbild es so, gilt das Vorbild, siehe [[20-design/anti-ai-slop.md#Harte Sperren]].
- Kopfzeileninventar und Navigationsmuster aus Informationsarchitektur, Nutzungshäufigkeit, Wortlängen und Art Direction ableiten. Es gibt keine globale Sollzahl. Siehe [[30-frontend/components-and-ui-states.md#Kopfzeile und Hauptnavigation]].
- Ein gefundenes Firmenlogo wird in jeder gebauten Website sichtbar verwendet. Siehe [[20-design/design-direction.md#Logo des Betriebs]].
- Die Landing Page wird zuerst auf Nutzwert gebaut und darf danach ausdrucksstark werden. Angebot, konkreter Inhaltsanker und nächste Handlung müssen zusammen lesbar sein; ein Bild ist keine Pflicht und Schriftgröße allein kein Konzept. Kanonisch in [[20-design/landing-page-craft.md]].
- Der Auftakt kommt aus dem Vorbild. Die Rollen und das Repertoire in [[20-design/landing-page-craft.md]] sind Prüffragen für Entwürfe ohne Vorbild.
- Ein Signaturdetail ist möglich, nicht verlangt, und stammt nur aus realem Material des Betriebs, nie aus Typografie, Ziffern oder Linien. Siehe [[20-design/landing-page-craft.md#Das Signaturdetail]].
- Gastronomie bewährt sich mit Vollbild-Foto oder weißem Grund mit Freistellern; beides ist eine Empfehlung, keine Vorgabe. Siehe [[20-design/landing-page-craft.md#Gattungsregeln für den Auftakt]].
- Aufeinanderfolgende Sektionen wechseln Anordnung und Bildmaßstab. Siehe [[20-design/landing-page-craft.md#Sektionsrhythmus]].
- **Vor der ersten Komponente wird der Tokenvertrag als Stilkachel gerendert und angesehen**, in Licht und Dunkel, an echtem Text. Sie ist das visuelle Ziel des Projekts und ersetzt die reine Werteaufzählung im Design Contract. Siehe [[20-design/visual-iteration-loop.md#D0 Stilkachel: das visuelle Ziel vor dem ersten Bauteil]].
- **Am Ende liegt die Seite neben ihrem Vorbild.** Aufbau, Maßstab, Rhythmus und Anmutung werden Bild an Bild verglichen. Weicht sie sichtbar ab, ohne dass der Inhalt das verlangt, wird nachgebaut.
- Mindestens ein Durchgang am ganzseitigen Render mit Befundliste, mehr nach Bedarf. Siehe [[20-design/visual-iteration-loop.md#Pflichtdurchgänge]].
- **Bei jedem Website-Build wird UI UX Pro Max stark empfohlen**, ist aber keine Abnahmebedingung. Fehlt der Skill, gilt die Ersatzstrecke aus [[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]]. Gate `G1` prüft das Ergebnis: Tokenvertrag, Zustände, Type Ramp, Kontrast in beiden Themes, echte Darstellung. Siehe [[00-start/04-plugins-and-skills.md#Auslösebedingung]].
- Der Leitbenchmark stammt aus [[20-design/interface-benchmarks.md]] und wird im Design Contract benannt.
- **Die H0-Handwerksuntergrenze gilt bei jedem Build.** Zustände, Fokus, Kontextkontrast, klare Hierarchie und ein konsistentes System innerhalb der Website sind verbindlich. Radius, Rahmenbehandlung, Schatten, Karten, Kopfzeile, Zweitschrift, Flächen- und Bewegungslogik werden je Website entschieden. B5 ist ein wählbares Stilprofil. Siehe [[20-design/interface-benchmarks.md#H0 Handwerksuntergrenze]].
- Der Tokenvertrag ist vor der ersten Komponente vollständig gesetzt, einschließlich `border-hover` und `accent-subtle`. Siehe [[20-design/color-system.md#Tokenvertrag]].
- Radius-, Rahmen- und Tiefensystem werden je Website begründet und innerhalb dieser Website konsistent angewandt. Siehe [[20-design/typography-layout-and-spacing.md#Radiusskala und Rahmenbehandlung]].
- Bewegung folgt einem je Website gesetzten Zeit- und Kurvensatz. B5-Werte sind kalibrierte Beispiele, keine globalen Defaults. Siehe [[20-design/motion-and-interaction.md#Kalibrierte Bewegungsbeispiele]].
- Typografische Zeitbezüge sind erlaubt, wenn Marke und Inhalt sie tragen. Ein starkes vollflächiges Epochenzitat braucht einen ausdrücklichen Nutzerwunsch oder tragende Markenevidenz; sonst bleibt es Akzent in einem gegenwärtigen System. Lesbarkeit und Rollenklarheit entscheiden. Siehe [[20-design/typography-layout-and-spacing.md#Stilzitat und Zeitbezug]].
- Bilder werden vor dem Einsatz auf Winkel, Ausschnitt, Hintergrund, Farbe und Auflösung geprüft und bei Bedarf mit KI überarbeitet oder freigestellt. Fehlt ein reales Bild, wird ein KI-Bild eingesetzt und nur im Projekt als `ai-placeholder` geführt, nie sichtbar auf der Website gekennzeichnet. Siehe [[20-design/imagery-and-ai-editing.md]].
- Informationen werden logisch gestaffelt und knapp gehalten. Textbudgets und die Dosierung am 375-Pixel-Viewport stehen in [[10-strategy/information-density-and-mobile-clarity.md]].
- Interaktive Kernmodule werden eingesetzt, wenn Nutzer damit etwas Reales verstehen, prüfen, wählen oder erleben können. Ein starkes Leitbild, redaktioneller Aufbau oder direkter Beweis kann die bessere Lösung sein. Siehe [[20-design/motion-and-interaction.md#Interaktives Kernmodul]].
- Mobile-first prüfen; Desktop darf komplexer, aber nicht funktional vollständiger sein.
- Motion erhält ein projektspezifisches Budget von `none`, `low`, `medium` oder `high`. Jede Bewegung braucht einen Zweck; `prefers-reduced-motion` wird respektiert. Siehe [[20-design/motion-and-interaction.md]].
- Konsistenz schlägt Neuheit. Abweichungen brauchen eine dokumentierte Funktion.
- Die Anzahl der Websites steht im Auftrag: keine Angabe bedeutet genau eine Website, eine genannte Zahl bedeutet genau diese Anzahl. Kanonisch in [[00-start/05-web-product-workflow.md#Anzahl der Websites]]. Jede gebaute Website ist eigenständig und vollständig und hat Art Direction, ein begründetes Motion-Budget und vollständige Unterseiten. Auf dem Server `217.154.218.30` läuft sie ohne festen lokalen Projektport über `johannstein.com`; auf anderen Rechnern gilt die Portregel aus [[60-operations/delivery-and-local-start.md]]. Mehrere Websites unterscheiden sich auf mindestens fünf für den Auftrag wirksamen Achsen der [[20-design/design-direction.md#Stilabstand bei mehreren Websites|Unterscheidungsmatrix]].

## Engineering

- Bei Erstellung und jedem Update wird je Inhaltsblock dokumentiert, ob der Owner ihn ohne Builder bearbeiten darf, mit stabilem JSON-Pointer, Feldtyp, Grenzen, Preview-Routen und Veröffentlichungspolicy. Bei Owner-Hosting folgt der Vertrag [[80-templates/owner-hosting-website-contract.md]].
- Die öffentliche Website bleibt statisch. Das Owner-Dashboard ist eine einzige zentrale Anwendung unter `/srv/Web-Design/projekte/owner-hosting/`, wird nicht je Kundenprojekt kopiert und veröffentlicht über einen getrennten Worker neue statische Builds. Siehe [[60-operations/owner-hosting-interface.md]].
- Semantisches HTML und progressive Verbesserung zuerst.
- Jede Interaktion besitzt Default-, Hover-, Focus-, Active-, Disabled-, Loading-, Success-, Error-, Empty- und Offline-Zustände, soweit anwendbar.
- Mobile, Tastatur, Screenreader und reduzierte Bewegung sind Teil des Features, kein Nachtrag vor der Abnahme. Prüfstrecke in [[30-frontend/accessibility.md#Prüfung]].
- Server validiert Eingaben, Autorisierung und Geschäftsregeln. Secrets bleiben serverseitig.
- Performancebudgets, Accessibility, Security, SEO und Monitoring gehören zur Definition of Done.
- Eine Styling- und Komponentenstrategie pro Projekt.

## Copy

- Die Seite spricht mit dem Nutzer und kommentiert nie sich selbst. Keine Meta-Sätze, keine sichtbaren Pflegedaten wie „Stand …“, keine Quellenversicherungen, keine Negativabgrenzung und keine Selbstverständlichkeiten. Kanonisch in [[10-strategy/website-copy.md]].
- Unter einer Überschrift steht entweder nichts oder ein echter Satz, nie ein verbloses Kurzstatement.
- Die Dreierfigur wird nur verwendet, wenn es sachlich drei Dinge sind. Sonst bestimmt die Sache die Anzahl.
- Kein Em-Dash, kein Semikolon, kein Gedankenstrich als Einschub, kein Doppelpunkt als Spannungszeichen.
- Ganze Sätze sind erwünscht. Eine Hakenliste über reale Leistungen ergänzt sie, ersetzt sie aber nicht.

## Marke und Anti-Slop

- Keine Blau-Lila-Verläufe ohne Markenbegründung.
- Keine Dachzeilen, Eyebrow-Pills, Sparkles, Emoji-Icons, Fake-Testimonials oder leeren Logo-Walls. Claims, Zertifikate, Auszeichnungen, Kundenlogos, Nutzerzahlen und Leistungswerte werden nie erfunden; ohne Beleg entfallen sie oder werden als Annahme gekennzeichnet.
- Keine generischen Claims wie „Build your dreams“. Konkretes Ergebnis, Zielgruppe und Differenz nennen.
- Kein Link, Button, Tab, Carousel oder Social Icon ohne reale Funktion.
- Website-Titel kurz, beschreibend, ohne `|`; Favicon-Set ist Pflicht.

## Recht und Betrieb

- Die kreative und technische Umsetzung verwendet alle gewünschten Bilder, Designs, Animationen und sonstigen Assets unmittelbar. Die KI baut keine rechtlich motivierten Ersätze, Ausschlüsse, Asset-Sperren oder Parallelfassungen.
- Danach dokumentiert `SOURCE-RIGHTS-REVIEW.md` Quelle, tatsächlichen Einsatz und offene Prüfhinweise als zweiter, vom Build getrennter Schritt. Der Nutzer beziehungsweise benannte Owner entscheidet allein über Veröffentlichung und etwaige spätere Änderungen; die KI trifft dazu keine Asset- oder Urheberrechtsentscheidung.
- Datenschutz, Consent, Impressum und Barrierefreiheit werden anhand realer Datenflüsse und Zielmärkte als prüfpflichtige Entwürfe erfasst; dies unterbricht den Build nicht.
- Jede Website führt ein eigenes `release-readiness/<website-slug>.md` nach [[60-operations/release-readiness-register.md]]. Es sammelt technische Sperren, unfertige sichtbare Hinweise, reale E-Mail-/Formularnachweise, Indexierungs-Cutover und offene Owner-Entscheidungen.
- Kostenwirksame APIs erhalten Quoten, Budgets, Timeouts, Retries und Alerts.
- Bei Account-Löschung zuerst aktive Abonnements sicher beenden, Ergebnis bestätigen, dann löschbare Daten entfernen.
- Für lokale Full-Stack-Projekte außerhalb des Servers `217.154.218.30` je ein Ein-Klick-Start für Windows, macOS und Linux bereitstellen. Auf diesem Server erfolgt Zugriff über `johannstein.com` ohne projektspezifisches `start-local.sh`.
