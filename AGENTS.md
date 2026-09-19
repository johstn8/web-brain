# Web-Brain Arbeitsanweisung

## Zweck

Kanonische Wissensbasis für KI-gestützte Web-Projekte. Fachwissen steht in den Notizen, nicht hier.

## Git

Remote `git@github.com:johstn8/web-brain`, Branch `main`, privat. Der Agent führt Git ohne Rückfrage aus.

- Vor jeder Nutzung, auch vor rein lesender: `git fetch origin`, `git status -sb`, bei Rückstand `git pull --rebase origin main`.
- Nach jeder abgeschlossenen Änderung: `git add -A`, `git commit`, `git push origin main`.
- **Commit-Konvention:** Betreffzeile benennt die kanonische Änderung, nicht die berührten Dateien. Body enthält die Begründung. Die Commit-Historie ist das Änderungsprotokoll des Vaults.
- Kein `--force`, kein `reset --hard` auf Gepushtes. Bei Konflikt nicht raten, sondern melden und den Nutzer entscheiden lassen; ebenso bei fehlgeschlagenem `fetch` oder `push`.

## Einstieg

1. Remote-Stand holen.
2. [[00-start/00-brain-index.md]] öffnen.
3. Über [[00-start/02-routing-map.md]] nur die aufgabenrelevanten Notizen laden.
4. Bei einem Projekt dessen `PROJECT.md` lesen; Bahnwahl nach [[00-start/05-web-product-workflow.md]].
5. Vor Abschluss [[70-qa/quality-gates.md]] abarbeiten.

## Verbindliche Regeln

- Eine Information hat genau eine kanonische Notiz. Andere Notizen verlinken dorthin und wiederholen sie nicht.
- Der kanonische Stand liegt im Git-Remote, nicht im lokalen Arbeitsverzeichnis.
- Externe Fakten erhalten Markdown-Fußnoten mit direkter URL, keine nackten Quellenlisten.
- Die Anzahl der zu bauenden Websites steht ausschließlich im Auftrag des Nutzers; keine Angabe bedeutet genau eine Website. Kanonisch in [[00-start/05-web-product-workflow.md#Anzahl der Websites]].
- Über Veröffentlichung, Rechtstexte und Asset-Freigabe entscheidet allein der Nutzer, nie die KI. Rechtliche Prüfhinweise sperren keinen Build und keine Vorschau.

Jede fachliche Regel zu Design, Copy, Komponenten, Farbe, Technik, Recht und Betrieb steht in den Notizen, beginnend bei [[00-start/01-core-rules.md]].

## Atomarer Update-Prozess

1. Kanonische Notiz bestimmen und dort ändern.
2. `impacts` und [[98-maintenance/coverage-and-impact-map.md]] prüfen.
3. Betroffene Projektartefakte in derselben Änderung nachziehen.
4. Veraltete Duplikate entfernen oder in Links umwandeln.
5. Quellen, `updated` und `review_by` aktualisieren.
6. Interne Links und Quality Gates prüfen, keine `TODO`-Reste in fertigen Dateien.
7. In einem Commit nach der Commit-Konvention sichern und pushen.

## Dateitypen

`canonical` maßgebliche Regel · `template` kopierbare Vorlage, nie mit Projektfakten gefüllt · `project` verbindliche Projektentscheidung · `reference` nicht automatisch verbindlich · `archive` nur Herkunftsnachweis.

## Priorität bei Konflikten

1. Auftragstext · 2. `PROJECT.md` · 3. dieses AGENTS.md · 4. kanonische Fachnotiz · 5. Vorlage · 6. Referenz. Konflikt dokumentieren, nicht still entscheiden.

## Graphify

`graphify-out/graph.json`, Pfad relativ zur Vault-Wurzel, bildet ausschließlich `web-brain/` ab. Hilfsmittel auf Bedarf, keine Pflicht: bei 69 Notizen ist `grep -r` meist schneller. Ab etwa 200 Notizen wird die Frage neu bewertet.
