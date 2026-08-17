---
type: canonical
status: canonical
updated: 2026-08-17
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
        │   └── <website-slug>/MASTER.md
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
- `site/` beziehungsweise `versions/` enthält genau die im Auftrag verlangte Anzahl vollständiger Websites. Jede Unterstruktur enthält Unterseiten, Navigation, `sitemap.xml`, robots-/Meta-Konfiguration, verwendete Konfiguration sowie Visual-, Motion- und SEO-Nachweise. Port und Startbefehl sind nur außerhalb des Servers `217.154.218.30` Pflicht; auf diesem Server übernimmt `johannstein.com` den Zugriff. Gemeinsame Fakten, Daten und Secrets bleiben außerhalb der Websites kanonisch und werden nicht dupliziert.

## Ein-Klick-Start und Serverausnahme

Zuerst wird festgestellt, ob der Build auf dem Server mit IP `217.154.218.30` läuft.

### Auf `217.154.218.30`

- Website-Projekte bekommen **keinen festen lokalen Port** und kein neues `start-local.sh`, `start-local.command` oder `start-local.cmd`.
- Fertige Fassungen werden über die Developer-Plattform auf `johannstein.com/dev` entdeckt und unter deren geschütztem Unterpfad ausgeliefert.
- Die Erkennung folgt der realen Struktur `site/`, `versions/<fassung>/` sowie den unterstützten Buildausgaben `dist/`, `build/` und `public/`.
- Ein fehlender Eintrag in der Developer-Plattform ist ein Delivery-Fehler und wird dort behoben, nicht mit einem separaten Prozess oder Port umgangen.

### Auf anderen Rechnern

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

Je gebauter Website wird dort genau ein fester, explizit dokumentierter lokaler Port reserviert. Empfohlenes Schema: eine Projektbasis wählen, etwa `4310`, und je weiterer Website in Zehnerschritten erhöhen, also `4310`, `4320`, `4330`. Bei einer einzelnen Website wird nur die Basis verwendet.

Der Start prüft Portkollisionen, startet alle vollständigen Routenbäume und nennt alle lokalen URLs. Es darf nie still auf einen zufälligen Port ausweichen. Ist ein Port belegt, bricht der Start mit einer verständlichen Meldung und einem Hinweis ab, wie der belegende Prozess ermittelt wird.

Container/Compose kann gemeinsame Grundlage sein; OS-Skripte bleiben dünne Wrapper. Secrets nie im Skript einbetten.

## Developer-Plattform

Die geschützte Developer-Plattform zeigt genau drei visuell getrennte Übersichten:

1. **Archiv:** alle entdeckten statischen Fassungen aus `/srv/Web-Design/Old-Projects`; unveränderlicher Bereich ohne Statusverschiebung.
2. **Aktuelle Projekte:** alle entdeckten Websites aus `/srv/Web-Design/projekte`, standardmäßig hier eingeordnet.
3. **Zur Veröffentlichung vorgesehen:** nicht archivierte Fassungen, deren Status der Nutzer ausdrücklich hierhin verschoben hat.

Der Veröffentlichungsstatus ist Metadatenstatus, kein Datei-Move. Er wird atomar unter `/srv/Web-Design/projekte/johannstein.com/.runtime/previews/` persistiert. Drag and Drop zwischen den beiden veränderlichen Bereichen besitzt eine sichtbare, gleichwertige Tastatur- und Buttonbedienung; Statusmeldungen werden assistiven Technologien angekündigt.

`/srv/Web-Design/vorschau` bleibt vorerst als Legacy-Quelle eingebunden. Seine vorhandenen Einträge starten im Bereich „Zur Veröffentlichung vorgesehen“, bilden aber keine vierte Übersicht. Der bestehende Basic-Auth-Schutz für direkte Legacy-Zugriffe bleibt erhalten, bis die Inhalte bewusst in `projekte/` migriert sind. Die Anmeldung von `/dev`, einzelne passwortgeschützte Freigabeadressen und `noindex` bleiben unabhängig davon unverändert.

### Test-Slot johannstein.de

Oberhalb der drei Übersichten steht eine rote Zielfläche. Sie ist **keine vierte Lane**, sondern ein einzelnes Deployment-Ziel nach [[60-Operations/Owner Hosting and Dashboard#Deployment-Slots]]:

- Genau eine Website ist gleichzeitig unter `johannstein.de` aktiv, mit Dashboard unter `hosting.johannstein.de`.
- Jede erkannte Fassung darf hierher gezogen werden, auch eine unveränderliche Archivfassung. Sie bleibt dabei in ihrem Bereich; der Veröffentlichungsstatus in `catalog.json` wird nicht angefasst und nicht umgedeutet.
- Ein Drop legt nur einen Kandidaten fest und zeigt Quelle, Fassung, betroffene Adressen und den bisherigen Release. Erst ein zweiter, klar beschrifteter Klick startet Build und Umschaltung.
- Drag and Drop hat wie bei den Übersichten eine sichtbare, gleichwertige Tastatur- und Buttonbedienung. Auch Archivkacheln tragen diese Schaltfläche.
- Während eines Jobs sind Doppelstarts blockiert; ein zwischenzeitlich geänderter Kandidat wird als Konflikt gemeldet statt still ersetzt.
- Der Browser überträgt ausschließlich den stabilen Katalogschlüssel `group/project/variant`. Absolute Pfade aus dem Browser sind verboten; der Server entdeckt die Website neu und prüft sie gegen die erlaubten Wurzeln.
- Fällt der Hosting-Dienst aus, bleibt `/dev` vollständig benutzbar. Die rote Fläche meldet dann verständlich, dass sie den Dienst nicht erreicht.

Der Test-Slot ist ausdrücklich getrennt von „Zur Veröffentlichung vorgesehen“. Der eine ist ein Deployment-Ziel, der andere ein Metadatenstatus im Katalog.

### Keine Hosting-Subdomain für Unterseiten-Vorschauen

Fassungen, die unter `johannstein.com/dev/site/…` betrachtet werden, erhalten **kein** simuliertes Hosting-Dashboard und keine nachgebildete Subdomain. Hostbindung, Cookies, relative Pfade und Tenant-Sicherheit würden dort gegeneinander arbeiten, und ein Dashboard ohne echten Tenant wäre eine Attrappe.

Die Website-Vorschau bleibt wie bisher erreichbar. Ein Dashboard-Link fehlt dort oder ist deaktiviert, mit dem Hinweis, dass das Hosting-Dashboard nur für die aktuell im Test-Slot bereitgestellte Fassung verfügbar ist.

Die öffentliche Freigabefunktion referenziert weiterhin die konkrete Quellgruppe, das Projekt und die Fassung. Eine Statusverschiebung ändert weder Freigabeadresse noch Dateipfad.

## Owner-Hosting

Das zentrale Produkt wird einmal unter `/srv/Web-Design/projekte/owner-hosting/` gebaut. Kundenprojekte liefern ausschließlich den versionierten Vertrag aus `content/<website>.json` und `owner-hosting/tenant.json` nach [[80-Templates/Owner Hosting Website Contract]]. Registrierung, Vorschau, Publish/Rollback, Wartungsmodus, Laufzeitpfade und Datenschutz stehen in [[60-Operations/Owner Hosting and Dashboard]].

## Environments

- local, test, preview/staging, production strikt trennen.
- `.env.example` enthält Namen und Kommentare, nie Werte.
- Sandbox-Dienste und Testschlüssel lokal; Produktionsschlüssel nur Secret Manager.
- Migrationspfad vor App-Deploy, mit Rückwärtskompatibilität oder Wartungsplan.
- Lokale Startumgebungen und externe Deployments werden nur über ihren tatsächlichen Datenstand und die Entscheidung des Nutzers/Owners unterschieden, niemals über eine reduzierte Asset-, Motion-, SEO- oder Seitenfassung.

## Release

Reproduzierbarer Build, Lockfile, CI-Gates, Preview, Migration, Smoke Test, Monitoring, Rollback und Verantwortlicher. Deployment und Datenmigration getrennt rollbackbar planen.
