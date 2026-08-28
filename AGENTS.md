# Web-Brain Arbeitsanweisung

## Zweck

Dieses Vault ist die kanonische Wissensbasis für KI-gestützte Web-Projekte. Optimiere für schnelle, eindeutige Modellauswertung. Human-Komfort ist nachrangig.

## Synchronisation

Dieses Vault ist ein Git-Repository. Remote `git@github.com:johstn8/web-brain`, Branch `main`, privat, Einzelnutzer auf mehreren Geräten. Der Agent führt Git eigenständig und ohne Rückfrage aus.

### Vor jeder Nutzung

Gilt auch für rein lesende Nutzung und für jede Verwendung des Brains in einem Web-Produkt:

1. `git fetch origin`
2. Stand mit `git status -sb` prüfen.
3. Bei Rückstand `git pull --rebase origin main`.
4. Erst danach Notizen lesen oder anwenden.

### Nach jeder abgeschlossenen Änderung

Abgeschlossen heißt: alle Schritte aus [[#Atomarer Update-Prozess]] sind erledigt, einschließlich Change-Log-Eintrag.

1. `git add -A`
2. `git commit` mit einer Zeile, die die kanonische Änderung benennt, nicht die berührten Dateien.
3. `git push origin main`

Change-Log-Eintrag und zugehörige Notizänderung gehören in denselben Commit.

### Grenzen

- Kein `git push --force`, kein `git reset --hard` auf bereits gepushte Commits, kein Umschreiben veröffentlichter Historie.
- Bei Rebase- oder Merge-Konflikt nicht raten. Konflikt und betroffene Notizen melden und den Nutzer entscheiden lassen, welche Fassung kanonisch ist.
- Schlägt `fetch` oder `push` fehl, etwa mangels Netz oder Auth, wird das gemeldet. Arbeit an einem nicht synchronisierten Vault nur auf ausdrückliche Ansage des Nutzers.
- Lokale Sitzungsnotizen und Obsidian-UI-Zustand stehen in `.gitignore` und werden nie committet.

## Einstieg

0. Zuerst den Remote-Stand nach [[#Synchronisation]] holen. Kein Lesen und kein Verwenden des Brains auf einem veralteten Arbeitsverzeichnis.
1. Öffne immer zuerst [[00-Start/00 Brain Index]].
2. Bei einem konkreten Projekt lies dessen `PROJECT.md` und [[80-Templates/Project Master Spec]].
3. Nutze [[00-Start/02 Routing Map]], um nur die aufgabenrelevanten Notizen zu laden.
4. Vor Umsetzung: fehlende Muss-Entscheidungen aus [[80-Templates/Project Intake]] klären oder ausdrücklich als Annahme markieren.
5. Vor Abschluss: [[70-QA/Quality Gates]] vollständig abarbeiten.

## Verbindliche Regeln

- Eine Information hat genau eine kanonische Notiz. Andere Notizen verlinken dorthin und wiederholen sie nicht.
- Der kanonische Stand des Brains liegt im Git-Remote, nicht im lokalen Arbeitsverzeichnis. Vor Nutzung holen, nach Änderung committen und pushen. Kanonisch in [[#Synchronisation]].
- Externe Fakten und Empfehlungen erhalten Markdown-Fußnoten mit direkter URL. Keine nackten Quellenlisten ohne Zuordnung.
- Externe Leitreferenzen werden nach der Auftragszahl dosiert. Bei genau einer Website entsteht ein Eigenentwurf ohne automatisch ausgewählte Live-Leitreferenz, außer der Nutzer gibt selbst eine Referenz vor. Bei zwei oder mehr Websites wird genau eine Website des Auftrags von genau einer fachlich passenden konkreten Live-Seite geprägt; alle übrigen entstehen als eigenständige Entwürfe aus Projektwahrheit und Brain-Regeln. Nur wenn trotz dokumentierter Suche keine starke Passung existiert, bleiben ausnahmsweise alle Fassungen Eigenentwürfe. Sammlungs-, Galerie-, Award- und Stilbibliotheksseiten sind nur Entdeckungsquellen. Kanonisch in [[90-References/Reference Research Workflow]].
- Inspiration ist Evidenz, keine starre Schablone. Bei Website-Builds dürfen Bilder, Designs, Animationen, Layouts und weitere visuelle Referenzen kreativ kopiert, adaptiert und eingesetzt werden. Quelle und tatsächlicher Einsatz werden anschließend im Projekt dokumentiert; sie begründen keinen Build-, Preview- oder Veröffentlichungsstopp durch die KI.
- Keine unbelegten Claims, Zertifikate, Testimonials, Logos, Nutzerzahlen oder Leistungswerte erfinden.
- Rechtliche Texte nie als universelle Vorlage ausgeben. Datenflüsse, Zielmarkt, Betreiber und Dienstleister im Build erfassen; rechtliche Texte dürfen nur als prüfpflichtige Entwürfe markiert werden. Was veröffentlicht wird, entscheidet ausschließlich der Nutzer beziehungsweise benannte Owner, nie die KI.
- Sicherheit und Berechtigungen immer serverseitig erzwingen. Client-Code ist nicht vertrauenswürdig.
- Mobile, Tastatur, Screenreader, reduzierte Bewegung, Fehler-, Leer-, Lade- und Offline-Zustände sind Teil des Features.
- Die Anzahl der zu bauenden Websites steht ausschließlich im Auftrag des Nutzers. Keine Angabe bedeutet genau eine Website. Auf `217.154.218.30` erfolgt der Zugriff ohne festen Projektport über `johannstein.com`, auf anderen Rechnern gilt die Portregel. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]].
- Website-Titel kurz und ohne `|`. Immer Favicon-Set festlegen.
- In Website-Copy keine Em-Dashes. Keine unbegründeten Blau-Lila-Verläufe, Sparkles, Emojis als UI oder generischen Testimonials.
- Website-Copy kommentiert nie sich selbst: keine Meta-Sätze, keine sichtbaren „Stand“-Daten, keine Negativabgrenzung, keine Selbstverständlichkeiten, kein verbloses Statement unter einer Überschrift, keine erfundene Dreierfigur, kein Semikolon und kein Gedankenstrich als Einschub. Kanonisch in [[10-Strategy/Website Copy]].
- Mehrere Websites im selben Auftrag besitzen jeweils eine eigenständige, kohärente Richtung und unterscheiden sich paarweise auf mindestens fünf für den Auftrag wirksamen Achsen der vor UI-Code ausgefüllten Unterscheidungsmatrix. Kanonisch in [[20-Design/Design Direction#Stilabstand bei mehreren Websites]].
- Redundante, rein dekorative Kicker über Überschriften sind ein Anti-Slop-Befund. Echte Rubrik-, Status-, Datums- oder Prozessinformation darf als eigene Hierarchiestufe erscheinen. Kanonisch in [[20-Design/Anti AI Slop]].
- Die Kopfzeile folgt Sitemap, Nutzungshäufigkeit, verfügbaren Beschriftungen und gewählter Art Direction. Es gibt keine globale Sollzahl für Navigationspunkte; Überlauf, zufälliger Umbruch und unverständliche Verdichtung bleiben Befunde. Kanonisch in [[30-Frontend/Components and UI States]].
- Keine Farbwelt wird allein wegen ihrer Kategorie verboten oder vorgeschrieben. Auch Beige, Creme, Sand, Neon oder Blau-Lila sind erlaubt, wenn Marke, Material, Inhalt und Kontrast sie tragen; unbegründete Generator-Defaults bleiben ein Befund. Kanonisch in [[20-Design/Color System]].
- Ein gefundenes Firmenlogo wird in jeder gebauten Website sichtbar eingesetzt, unabhängig von seiner Qualität. Kanonisch in [[20-Design/Design Direction]].
- Bei **jedem** Website-Build wird der UI UX Pro Max Skill verwendet, ohne Ausnahme. Kanonisch in [[00-Start/04 Plugins and Skills#Auslösebedingung]].
- Der Leitbenchmark für Aussehen und Bedienung stammt aus [[20-Design/Interface Benchmarks]]. Diese Notiz steht bei visuellen Entscheidungen über den allgemeinen Referenzmustern.
- Die stilneutrale **H0-Handwerksuntergrenze** gilt bei jedem Build. B5 Modern Neutral Craft Web ist ein wählbares Stilprofil, kein Pflichtaussehen. Kanonisch in [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]].
- Der Tokenvertrag ist vor der ersten Komponente vollständig gesetzt, einschließlich `border-hover` und `accent-subtle`. Kanonisch in [[20-Design/Color System#Tokenvertrag]].
- Radius, Rahmenbehandlung, Flächenlogik, Tiefe, Komponentenrepertoire, Kopf- und Fußbereich, Zweitschrift und Motion werden je Website begründet und intern konsistent umgesetzt. Schatten, Rahmen, Hairlines und rahmenlose Flächen sind gleichwertige Mittel, sofern Hierarchie und Zustände funktionieren. Kanonisch in [[20-Design/Interface Benchmarks#H0 Handwerksuntergrenze]].
- Karten, Zeilen, Tabellen und Listen sowie das Kopfzeileninventar sind Art-Direction-Entscheidungen nach [[30-Frontend/Components and UI States#Kartenentscheidung]] und [[30-Frontend/Components and UI States#Kopfzeile und Hauptnavigation]].
- Jede Website setzt ihren eigenen Bewegungswertesatz. B5-Werte aus [[20-Design/Motion and Interaction#Kalibrierte Bewegungsbeispiele]] sind optionale Kalibrierung.
- Historische, retrohafte, sachliche, expressive und neutrale Typografie sind mögliche Richtungen. Ein starkes, vollflächiges Epochenzitat ist jedoch eine begründungspflichtige Ausnahme und kein Mittel, um Fassungen künstlich auseinanderzuziehen. Ohne ausdrücklichen Nutzerwunsch oder tragenden Markenbezug bleibt der Grundcharakter gegenwärtig; historische Signale dürfen akzentuieren. Lesbarkeit, Lizenz und konsequente Rollen bleiben verbindlich. Kanonisch in [[20-Design/Typography Layout and Spacing#Stilzitat und Zeitbezug]].
- Bilder werden vor dem Einsatz überarbeitet: Winkel, Ausschnitt, Hintergrund, Farbe, Auflösung. Freistellen und KI-Bearbeitung sind der Normalfall. Fehlt ein reales Bild, wird ein KI-Bild eingesetzt und nur im Projekt als `ai-placeholder` geführt, niemals sichtbar auf der Website gekennzeichnet. Kanonisch in [[20-Design/Imagery and AI Editing]].
- Informationen bleiben knapp, logisch gestaffelt und am Mobilgerät dosiert. Kanonisch in [[10-Strategy/Information Density and Mobile Clarity]].
- Der Auftakt priorisiert Nutzwert vor Stilintensität: Angebot, konkrete Beweis- oder Gegenstandsform und nächste Handlung bilden eine lesbare Komposition; ein Bild ist optional. Übergröße, Retro-Zitat oder Differenzdruck ersetzen keinen Inhaltsanker. Kanonisch in [[20-Design/Design Direction#Landing Page]].
- Interaktive Kernmodule und aufwendige Motion werden nur eingesetzt, wenn sie Angebot, Beweis, Orientierung oder Bedienung verbessern. Eine professionelle, weitgehend statische Website ist ausdrücklich gültig. Kanonisch in [[20-Design/Motion and Interaction]].
- Nach dem Bau ist der Impeccable KI-Detail-Review je Website Pflicht. Die Abnahme verlangt echte Darstellung; fehlende Renderfähigkeit wird vor Lieferung als Blocker gemeldet.
- Bei Erstellung und jedem Update wird je Inhaltsblock `owner_editable`, stabiler JSON-Pointer, Feldtyp, Grenze, Preview-Routen und Veröffentlichungspolicy nach [[60-Operations/Owner Hosting and Dashboard]] entschieden. Bei zentralem Hosting sind `content/<website>.json` und `owner-hosting/tenant.json` nach [[80-Templates/Owner Hosting Website Contract]] Pflicht.
- Jede gebaute Website führt ab Projektbeginn ein eigenes `release-readiness/<website-slug>.md` nach [[60-Operations/Release Readiness Register]]. Neue provisorische Sperren, Attrappen, unfertige Hinweise und noch nicht produktive Endpunkte werden in derselben Änderung eingetragen und erst mit Produktionsnachweis geschlossen.
- Projektweit einheitliche Architektur. Keine willkürliche Mischung aus Inline-Stilen, CSS-Modulen, Utility-Klassen und globalem CSS.

## Atomarer Update-Prozess

Jede Änderung ist erst vollständig, wenn alle Schritte erledigt sind:

1. Kanonische Notiz bestimmen und dort ändern.
2. `impacts` und [[98-Maintenance/Coverage and Impact Map]] prüfen.
3. Alle betroffenen Projektartefakte aktualisieren, insbesondere Sitemap, Routen, Navigation, Dateninventar, Rechtstexte, Tests, Abhängigkeiten und Betriebsdoku.
4. Veraltete Duplikate entfernen oder in Links umwandeln.
5. Quellen, tatsächlichen Asset-Einsatz und `updated`-Datum aktualisieren; zeitkritische Aussagen mit `review_by` versehen.
6. Entscheidung in [[98-Maintenance/Change Log]] protokollieren.
7. Interne Links und Quality Gates prüfen. Keine `TODO`- oder Platzhalter-Reste in einem als fertig markierten Projekt.

## Dateitypen

- `canonical`: maßgebliche Regel oder Wissen.
- `template`: kopierbare Projektdatei; nie projektspezifische Fakten im Original eintragen.
- `project`: konkrete, verbindliche Projektentscheidung.
- `reference`: Inspiration oder Quelle; nicht automatisch verbindlich.
- `archive`: nur Herkunftsnachweis; nicht zur Implementierung verwenden.

## Priorität bei Konflikten

Reihenfolge von oben nach unten:

1. der aktuelle Auftragstext des Nutzers, insbesondere die genannte Anzahl der Websites
2. konkrete Projektentscheidung im jeweiligen `PROJECT.md`
3. dieses AGENTS.md
4. kanonische Fachnotiz
5. Vorlage
6. Referenz

`TasksForAgent.md` ist ein leerer, nicht versionierter Herkunftsnachweis und hat keine Steuerungswirkung mehr. Konflikt dokumentieren, nicht still entscheiden.

## Graphify

Der Graphify-Graph für dieses Web-Brain liegt im Repository unter:

`graphify-out/graph.json`

Pfad immer relativ zur Vault-Wurzel auflösen. Keine absoluten Gerätepfade in Notizen, da das Vault auf mehreren Geräten geklont wird.

Bei nicht trivialen Fragen zum Aufbau, zu Abhängigkeiten oder zu vorhandenen Inhalten zuerst eine gezielte Graphify-Abfrage durchführen, bevor das gesamte Vault breit durchsucht wird.

Der Graph bildet ausschließlich `web-brain/` ab. Ordner unter `../Projekte/` dürfen nicht in diesen Graphen aufgenommen werden.

### Pflicht zum Neubau

Der Graph wird bei **jeder** Aktualisierung des Brains neu gebaut, nicht nur bei großen Änderungen. Ein Graph, der den aktuellen Notizenstand nicht abbildet, führt zu falschen Antworten und ist schlechter als kein Graph.

1. Notizänderung nach [[#Atomarer Update-Prozess]] abschließen.
2. Graphen über den Graphify-Skill am bestehenden Ort `graphify-out/` neu bauen. Keinen zusätzlichen Graphen an anderer Stelle erzeugen.
3. Graph-Artefakte zusammen mit der Notizänderung committen und pushen.

Versioniert werden `graph.json`, `graph.html`, `GRAPH_REPORT.md`, `manifest.json`, `cost.json` und die Community-Labels, damit ein frisch geklontes Gerät ohne Neuberechnung abfragen kann. Nicht versioniert werden der Extraktions-Cache und die Marker mit absoluten Gerätepfaden; beide entstehen beim nächsten Lauf neu.

Weicht die Knotenzahl beim Neubau deutlich nach unten ab, greift der Shrink-Schutz von Graphify. Das ist kein Fehler, sondern eine Rückfrage: Ursache prüfen und die Abweichung im [[98-Maintenance/Change Log]] festhalten, statt sie stillschweigend zu überschreiben.
