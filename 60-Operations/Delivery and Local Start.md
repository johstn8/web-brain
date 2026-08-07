---
type: canonical
status: canonical
updated: 2026-08-06
impacts:
  - dependencies
  - environments
  - qa
---

# Delivery and Local Start

## Workspace-Struktur

Dieses Brain liegt unter `Web-Design/web-brain/`. Der physische Projektordner heißt kanonisch `projekte`; englische Formulierungen wie „projects folder“ meinen denselben Ordner. Jeder Umsetzungsauftrag erhält vor weiterer Arbeit einen eigenen Geschwisterordner `Web-Design/projekte/<Projektname>/` mit `PROJECT.md` und den Pflichtartefakten. Projektbezogene Recherche, Designsysteme und `.pen`-Dateien bleiben im Projekt, nicht im Brain:

```text
Web-Design/
├── web-brain/
└── projekte/
    └── <Projektname>/
        ├── PROJECT.md
        ├── SOURCE-RIGHTS-REVIEW.md
        ├── ASSET-REGISTER.md
        ├── DATA-PROCESSING-INVENTORY.md
        ├── content/
        ├── design/
        ├── design-system/
        ├── research/
        │   ├── legacy-site/
        │   └── source-material/
        ├── legal/
        ├── operations/
        ├── tests/
        └── site/            bei genau einer beauftragten Website
```

Verlangt der Auftrag mehrere Websites, tritt `versions/` an die Stelle von `site/`:

```text
        └── versions/
            ├── 01-<richtung>/
            ├── 02-<richtung>/
            └── …
```

Welche der beiden Formen gilt, entscheidet allein die im Auftrag genannte Anzahl nach [[00-Start/05 Web Product Workflow#Anzahl der Websites]]. Beide Formen enthalten dieselben Pflichtinhalte je Website. `site/` und `versions/` stehen nie nebeneinander.

Die Detailregeln für `.pen`-Dateien und die headless CLI `pen` stehen in [[90-References/pen.dev Workflow]]. Für Code kommen nach Stackentscheidung die einheitliche Quellstruktur und Konfigurationsdateien hinzu.

## Anlage- und Schreibregeln

- Projektname und Zielpfad vor dem ersten Schreibzugriff ausgeben.
- Existiert der Zielordner, `PROJECT.md` lesen und Fortsetzung oder neue Version eindeutig entscheiden.
- Kein Artefakt eines Auftrags im Ordner eines anderen Projekts ablegen.
- Das Projekt gilt erst als angelegt, wenn die vier Pflichtdateien existieren und in `PROJECT.md` verlinkt sind.
- Fehlende Schreibberechtigung oder unklarer Zielordner ist ein zu meldender Blocker.
- `site/` beziehungsweise `versions/` enthält genau die im Auftrag verlangte Anzahl eigenständig startbarer, vollständiger Websites. Jede Unterstruktur enthält ihre Unterseiten, Navigation, `sitemap.xml`, robots-/Meta-Konfiguration, eigenen Port, Startbefehl, verwendete Konfiguration sowie Visual-, Motion- und SEO-Nachweise. Gemeinsame Fakten, Daten und Secrets bleiben außerhalb der Websites kanonisch und werden nicht dupliziert; eine Faktenänderung bleibt dadurch eine einzige Änderung.

## Ein-Klick-Start

Full-Stack-Projekte liefern:

- Windows: `start-local.cmd` oder signiertes PowerShell-Skript
- macOS: `start-local.command`
- Linux: `start-local.sh` plus optional `.desktop`

Jedes Skript:

1. prüft Runtime, Paketmanager, Ports und benötigte Konfiguration
2. installiert nie ungefragt globale Software
3. startet Datenbank, Backend, Worker und Frontend in definierter Reihenfolge
4. wartet auf echte Health Endpoints statt fester Sleeps
5. zeigt pro Dienst Status und Logs
6. öffnet Browser erst bei erreichbarem Frontend
7. beendet eigene Child-Prozesse sauber und lässt externe Dienste unangetastet
8. gibt klare Fehlerbehebung und Exit Codes aus

Je gebauter Website wird genau ein fester, explizit dokumentierter lokaler Port reserviert. Empfohlenes Schema: eine Projektbasis wählen, etwa `4310`, und je weiterer Website in Zehnerschritten erhöhen, also `4310`, `4320`, `4330`. Bei einer einzelnen Website wird nur die Basis verwendet.

Der Start prüft Portkollisionen, startet alle vollständigen Routenbäume und nennt alle lokalen URLs. Es darf nie still auf einen zufälligen Port ausweichen. Ist ein Port belegt, bricht der Start mit einer verständlichen Meldung und einem Hinweis ab, wie der belegende Prozess ermittelt wird.

Container/Compose kann gemeinsame Grundlage sein; OS-Skripte bleiben dünne Wrapper. Secrets nie im Skript einbetten.

## Environments

- local, test, preview/staging, production strikt trennen.
- `.env.example` enthält Namen und Kommentare, nie Werte.
- Sandbox-Dienste und Testschlüssel lokal; Produktionsschlüssel nur Secret Manager.
- Migrationspfad vor App-Deploy, mit Rückwärtskompatibilität oder Wartungsplan.
- Lokale Startumgebungen und externe Deployments werden nur über ihren tatsächlichen Datenstand und die Entscheidung des Nutzers/Owners unterschieden, niemals über eine reduzierte Asset-, Motion-, SEO- oder Seitenfassung.

## Release

Reproduzierbarer Build, Lockfile, CI-Gates, Preview, Migration, Smoke Test, Monitoring, Rollback und Verantwortlicher. Deployment und Datenmigration getrennt rollbackbar planen.
