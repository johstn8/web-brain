---
type: canonical
status: canonical
updated: 2026-08-05
review_by: 2027-02-03
impacts:
  - design-direction
  - project-artifacts
  - plugins-and-skills
  - local-operations
---

# pen.dev Workflow

## Rolle und Einsatzgrenze

pen.dev wird in diesem Workflow ausschließlich headless über die CLI `pen` genutzt. Es ist ein Werkzeug für UI/UX, Webdesign, Wireframes, Layouts, Komponenten, Designsysteme und die Bearbeitung von `.pen`-Dateien. Für Backend-, Text- oder kleine, nicht visuelle Codeaufgaben wird es nicht eingesetzt.[^cli]

Desktop-App und ein externer MCP-Server gehören nicht zu diesem Workflow und werden nicht gestartet oder geprüft. `pen status` prüft Authentifizierung und Kontostatus, nicht einen laufenden Dienst.[^cli]

Für jede neue Website und wesentliche visuelle Neuausrichtung wird im `PROJECT.md` entschieden:

`pen.dev: use | skip -> Zweck -> erwartetes Artefakt -> Owner -> Begründung`

## Verfügbarkeit und sichere Ablage

Vor einer vorgesehenen Nutzung kann Codex `command -v pen` und bei Bedarf `pen status` ausführen. Ist die CLI nicht verfügbar oder nicht angemeldet, wird der visuelle Arbeitsschritt als Blocker oder Alternative im Projekt dokumentiert, ohne die Desktop-App zu starten.

- Projektwurzel: `../projekte/<Projektname>/`
- Designquellen: `../projekte/<Projektname>/design/`
- Beispiele: `design/main.pen`, `design/landing-page-v2.pen`
- Verbindliche Groß-/Kleinschreibung: `projekte` und `design`

Vor einer Änderung `PROJECT.md`, Design Contract und vorhandene `.pen`-Dateien lesen. Neue Ausgaben immer in einen benannten Zielpfad schreiben. Bestehende Dateien nicht still überschreiben: bei größeren Änderungen eine Version oder ein Backup anlegen und den gewählten Pfad im Master Spec oder Decision Log festhalten.

## CLI-Schleife

1. [[90-References/Reference Research Workflow|Referenzentscheidung]], UI UX Pro Max Ergebnis aus [[00-Start/04 Plugins and Skills]] sowie Tokens und reale Inhalte laden.
2. Neues Design erzeugen: `pen --out <file>.pen --prompt "<task>"`.
3. Bestehendes Design als neue Version ändern: `pen --in <file>.pen --out <file>.pen --prompt "<change>"`.
4. Für gezielte Bearbeitung die headless Shell nutzen: `pen interactive --in <file>.pen --out <file>.pen`.
5. Visuellen Nachweis exportieren: `pen --in <file>.pen --export <preview>.png`; dabei mobile, Desktop, lange Inhalte, Zustände, Fokus und Reduced Motion prüfen.
6. Freigegebene Tokens und Komponenten im Code umsetzen; Abweichungen im Design Contract oder Decision Log dokumentieren.

Generierte Bilder, Stockmaterial und Referenzassets können sofort eingesetzt oder adaptiert werden. Ihr tatsächlicher Einsatz wird anschließend im [[80-Templates/Asset Register]] erfasst und erzeugt keine Sperre oder Ersatzfassung.

## Fehlerpfad

1. `command -v pen` ausführen und den Projekt- sowie Ein-/Ausgabepfad bestätigen.
2. Bei Authentifizierungsbedarf `pen status` prüfen; nur mit Projektfreigabe anmelden.
3. Fehlerausgabe, verwendeten Befehl und unveränderte Quelldatei im Projekt dokumentieren.
4. Keine Desktop-App, keinen MCP-Server und keine Start-/Stoppskripte als Ersatz verwenden.

## Interne Verknüpfung

- Webdesign: [[00-Start/05 Web Product Workflow]]
- UI/UX: [[20-Design/Design Direction]] und [[30-Frontend/Components and UI States]]
- Designsysteme: [[20-Design/Color System]], [[20-Design/Typography Layout and Spacing]] und [[20-Design/Motion and Interaction]]
- Codex: [[00-Start/04 Plugins and Skills]] und [[80-Templates/AI Build Prompt]]
- Projektablage: [[60-Operations/Delivery and Local Start]]

[^cli]: [pen.dev CLI](https://docs.pen.dev/for-developers/pen-cli)
