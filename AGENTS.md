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
- Inspiration ist Evidenz, keine Pflicht. Bei Website-Builds dürfen Bilder, Designs, Animationen, Layouts und weitere visuelle Referenzen kreativ kopiert, adaptiert und eingesetzt werden. Quelle und tatsächlicher Einsatz werden anschließend im Projekt dokumentiert; sie begründen keinen Build-, Preview- oder Veröffentlichungsstopp durch die KI.
- Keine unbelegten Claims, Zertifikate, Testimonials, Logos, Nutzerzahlen oder Leistungswerte erfinden.
- Rechtliche Texte nie als universelle Vorlage ausgeben. Datenflüsse, Zielmarkt, Betreiber und Dienstleister im Build erfassen; rechtliche Texte dürfen nur als prüfpflichtige Entwürfe markiert werden. Was veröffentlicht wird, entscheidet ausschließlich der Nutzer beziehungsweise benannte Owner, nie die KI.
- Sicherheit und Berechtigungen immer serverseitig erzwingen. Client-Code ist nicht vertrauenswürdig.
- Mobile, Tastatur, Screenreader, reduzierte Bewegung, Fehler-, Leer-, Lade- und Offline-Zustände sind Teil des Features.
- Die Anzahl der zu bauenden Websites steht ausschließlich im Auftrag des Nutzers. Keine Angabe bedeutet genau eine Website. Kanonisch in [[00-Start/05 Web Product Workflow#Anzahl der Websites]].
- Website-Titel kurz und ohne `|`. Immer Favicon-Set festlegen.
- In Website-Copy keine Em-Dashes. Keine unbegründeten Blau-Lila-Verläufe, Sparkles, Emojis als UI oder generischen Testimonials.
- Kein Kicker über einer Überschrift, weder als Pille noch als Versalzeile noch als Marker. Kanonisch in [[20-Design/Anti AI Slop]].
- Kopfzeile mit höchstens sechs Navigationspunkten; nichts in der Kopfzeile bricht um, ausgenommen Logos. Kanonisch in [[30-Frontend/Components and UI States]].
- Beige, Creme und Sand sind als dominante Grundfläche ausgeschlossen. Kanonisch in [[20-Design/Color System]].
- Ein gefundenes Firmenlogo wird in jeder gebauten Website sichtbar eingesetzt, unabhängig von seiner Qualität. Kanonisch in [[20-Design/Design Direction]].
- Bei **jedem** Website-Build wird der UI UX Pro Max Skill verwendet, ohne Ausnahme. Kanonisch in [[00-Start/04 Plugins and Skills#Auslösebedingung]].
- Der Leitbenchmark für Aussehen und Bedienung stammt aus [[20-Design/Interface Benchmarks]]. Diese Notiz steht bei visuellen Entscheidungen über den allgemeinen Referenzmustern.
- Keine Retro-Anmutung. Kein `Iowan Old Style` und keine typgleiche alte Buchserife als Markenschrift, keine Kombination aus Serife, gedecktem Erdton und Ornament. Kanonisch in [[20-Design/Typography Layout and Spacing#Retro-Verbot]].
- Bilder werden vor dem Einsatz überarbeitet: Winkel, Ausschnitt, Hintergrund, Farbe, Auflösung. Freistellen und KI-Bearbeitung sind der Normalfall. Fehlt ein reales Bild, wird ein KI-Bild eingesetzt und nur im Projekt als `ai-placeholder` geführt, niemals sichtbar auf der Website gekennzeichnet. Kanonisch in [[20-Design/Imagery and AI Editing]].
- Informationen bleiben knapp, logisch gestaffelt und am Mobilgerät dosiert. Kanonisch in [[10-Strategy/Information Density and Mobile Clarity]].
- Jede Landing Page besitzt mindestens ein interaktives Kernmodul. Kanonisch in [[20-Design/Motion and Interaction#Interaktives Kernmodul]].
- Nach dem Bau ist der Impeccable KI-Detail-Review je Website Pflicht.
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

[[TasksForAgent]] ist ein leerer Herkunftsnachweis und hat keine Steuerungswirkung mehr. Konflikt dokumentieren, nicht still entscheiden.

## Graphify

Der Graphify-Graph für dieses Web-Brain liegt im Repository unter:

`graphify-out/graph.json`

Pfad immer relativ zur Vault-Wurzel auflösen. Keine absoluten Gerätepfade in Notizen, da das Vault auf mehreren Geräten geklont wird.

Bei nicht trivialen Fragen zum Aufbau, zu Abhängigkeiten oder zu vorhandenen Inhalten zuerst eine gezielte Graphify-Abfrage durchführen, bevor das gesamte Vault breit durchsucht wird.

Der Graph bildet ausschließlich `web-brain/` ab. Ordner unter `../Projekte/` dürfen nicht in diesen Graphen aufgenommen werden.

Nach größeren strukturellen oder inhaltlichen Änderungen am Web-Brain den bestehenden Graphen aktualisieren. Nicht ungefragt einen zusätzlichen Graphen an anderer Stelle erzeugen.
