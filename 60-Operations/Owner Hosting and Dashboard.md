---
type: canonical
status: canonical
updated: 2026-08-18
review_by: 2027-02-18
depends_on:
  - "[[60-Operations/Delivery and Local Start]]"
  - "[[40-Backend-Security/Authentication and Accounts]]"
  - "[[50-Legal/Privacy and Consent]]"
impacts:
  - project-master-spec
  - data-processing-inventory
  - content-schema
  - deployment
  - monitoring
  - legal-drafts
---

# Owner Hosting and Dashboard

## Zweck und Grenze

Der Builder hostet selbst erstellte Websites auf dem Server `217.154.218.30`. Die öffentliche Website bleibt ein statischer, von nginx ausgelieferter Build. Das Owner-Dashboard ist eine getrennte, angemeldete Anwendung unter `hosting.<domain>`. Es verändert nie eine laufzeitabhängige Datenquelle der öffentlichen Website, sondern erzeugt und veröffentlicht eine neue statische Fassung.

Eine Dashboard-Codebasis bedient alle Websites. Unterschiede entstehen ausschließlich über Mandantenkonfiguration, Inhalts- und Feldschema, Rollen, Domain, Buildadapter und Branding des Dashboard-Produkts. Es gibt keine Kopie des Dashboard-Codes je Website.

Das Dashboard hat eine eigene professionelle Produktanmutung. Es kopiert weder Farben, Schrift, Kopfzeile noch Komponentenstil der jeweiligen öffentlichen Website. Priorität haben verständliche Sprache, klare Zustände, Tastaturbedienung, Fehlertoleranz und sichere Veröffentlichungen.

## Verbindliche Architekturentscheidung

Das Dashboard wird **einmal zentral gebaut**, nicht innerhalb von `johannstein.com` und nicht in den einzelnen Kundenprojekten. Der Zielort für den eigenen Git-Bestand ist:

`/srv/Web-Design/projekte/owner-hosting/`

Dieser Bestand enthält die Dashboard-Webanwendung, den Build-Worker, die gemeinsame Vertragsprüfung, das Builder-CLI und die Betriebsdateien. Vorgesehene Struktur:

```text
/srv/Web-Design/projekte/owner-hosting/
  apps/dashboard/            # angemeldete Webanwendung
  apps/worker/               # Build-, Preview-, Publish- und Rollback-Jobs
  packages/contracts/        # Parser, JSON-Pointer-Regeln und Validierung
  packages/build-profiles/   # freigegebene Buildadapter
  packages/tenant-cli/       # lint, plan, register, sync, publish
  operations/nginx/
  operations/systemd/
  operations/migrations/
  docs/
```

Eine Installation bedient alle `hosting.<domain>`-Subdomains. nginx leitet jede Dashboard-Subdomain an denselben Unix-Socket `/run/owner-hosting/dashboard.sock`. Die Anwendung löst den normalisierten, ausdrücklich erlaubten Hostnamen serverseitig zu genau einem `tenant_id` auf. Ein Query-Parameter, Cookie oder vom Client gelieferter Mandantenname darf diese Zuordnung niemals überschreiben.

Die Webanwendung und der Build-Worker laufen als getrennte Dienste und Benutzer:

- `owner-hosting-web`: Anmeldung, Dashboard, Entwürfe und API; kein Schreibrecht auf Website-Quellordner oder öffentliche Releases.
- `owner-hosting-worker`: nimmt unveränderliche, einem Mandanten zugeordnete Jobs an; darf nur in temporäre Buildverzeichnisse und die Laufzeitpfade des betroffenen Mandanten schreiben.
- `www-data`: liest ausschließlich den aktiven öffentlichen Release; kein Zugriff auf Entwürfe, Konten, Tokens oder Quellcode.

> [!note] Stand der Umsetzung, 17. August 2026
> Die erste gebaute Fassung weicht in zwei Punkten begründet ab. Die Sicherheitsgrenzen bleiben dabei unverändert.
>
> **Ein Dienst statt zwei.** Dashboard, Control Plane und Worker laufen als ein Prozess unter dem Benutzer `owner-hosting`. Zwei Dienste bräuchten eine zweite Unit, einen zweiten Benutzer und einen Kanal dazwischen; für einen Slot mit einer aktiven Website ist das mehr Betriebsfläche als Nutzen. Die Trennung, auf die es ankommt, wurde stattdessen an den Sockets gezogen: `dashboard.sock` gehört der Gruppe `owner-hosting-web` und ist nur für `www-data` erreichbar, `control.sock` der Gruppe `owner-hosting-ctl` und nur für `web-johannstein`. Der Control-Socket ist in keiner nginx-Konfiguration eingebunden. Der Schutz der Quellen liegt bei `ProtectSystem=strict` mit drei `ReadWritePaths`, nicht bei der Benutzertrennung. Eine spätere Aufteilung in zwei Units bleibt möglich.
>
> **SQLite statt PostgreSQL.** Auf `217.154.218.30` ist kein PostgreSQL installiert. Für einen Slot mit einer aktiven Website liefert `node:sqlite` Transaktionen und WAL-Modus ohne zweiten Serverprozess und ohne Netzwerkgrenze. Alle Zugriffe laufen über ein Modul; ein Wechsel auf PostgreSQL betrifft nur dieses. Das Schema ist unverändert das hier beschriebene.
>
> Der Dienst hat keine Laufzeitabhängigkeiten außerhalb der Node-Standardbibliothek und läuft mit `PrivateNetwork=yes` ohne jeden Netzwerkzugang.

Ein fester Projektport je Kundenwebsite entsteht dadurch nicht. Das Dashboard ist ein zentraler Infrastrukturdienst am Unix-Socket, der Worker besitzt keinen öffentlichen Listener.

## Ablage von Code, Geheimnissen und Mandantendaten

| Art | Kanonischer Ort | Regel |
|---|---|---|
| Dashboard- und Worker-Code | `/srv/Web-Design/projekte/owner-hosting/` | Git-versioniert; keine Kundenkopien |
| globale Secrets | `/etc/owner-hosting/env` | nur für den Dienstbenutzer lesbar; nie im Repository |
| Schlüssel für Token-/Credential-Verschlüsselung | `/etc/owner-hosting/keys/` | getrennt von Datenbank und Backups sichern |
| relationale Zustände | zentrale PostgreSQL-Datenbank | Konten, Mandantenzuordnung, Entwürfe, Jobs, Audit Log und Integrationsmetadaten; jede Zeile mit `tenant_id`, soweit mandantenbezogen |
| veröffentlichte Owner-Werte | `/var/lib/owner-hosting/tenants/<tenant_id>/content/` | unveränderliche JSON-Revisionen plus Zeiger auf die aktive Revision |
| Uploads | `/var/lib/owner-hosting/tenants/<tenant_id>/assets/` | Original, geprüfte Varianten und Metadaten getrennt je Mandant |
| Build-Arbeit | `/var/lib/owner-hosting/tenants/<tenant_id>/builds/` | kurzlebig, quotiert und nach Jobende bereinigt |
| statische Releases | `/srv/www/owner-hosting/<tenant_id>/releases/<release_id>/` | unveränderlich; `current` zeigt atomar auf einen vollständigen Release |
| Wartungsstatus | zentraler Zustand plus statische Halteseite je Mandant | nginx kann ihn ohne Dashboard-Verfügbarkeit auswerten |

Absolute Projektpfade, Hostnamen und Buildprofile stehen in der serverseitigen Tenant Registry, nicht in Owner-editierbaren Daten. Backups trennen Datenbank, Content-Revisionen, Assets, Releases und Schlüssel; ein Restore wird mandantenweise getestet.

## Eigentum der Daten und eine einzige Wahrheit

Nach Aktivierung des Hostings gelten drei getrennte Quellen mit klarer Zuständigkeit:

1. Das Kundenprojekt besitzt Struktur, Komponenten, builder-gepflegte Fakten, den Website-Vertrag und die Standardwerte in `content/<website>.json`.
2. Der zentrale Hosting-Speicher besitzt die veröffentlichten Owner-Überschreibungen, Entwürfe und ihre Revisionen. Er speichert nur Werte an registrierten `owner_editable`-Pfaden, niemals Layout- oder Buildcode.
3. Ein Build erzeugt daraus eine aufgelöste Inhaltsdatei: Projekt-Basis plus Owner-Overlay der gewählten Revision. Diese Builddatei wird validiert, enthält keine editierbaren Metadaten und wird in den statischen Release eingebettet.

Damit gibt es keinen unkontrollierten Zwei-Wege-Abgleich. Für Owner-Pfade ist die veröffentlichte Overlay-Revision kanonisch; für alle anderen Pfade bleibt die Projektdatei kanonisch. Ein Builder-Update darf bestehende Owner-Werte nicht durch neue Projekt-Defaults überschreiben.

## Topologie

```text
Registrar
  └─ A-Record <domain> und hosting.<domain> -> 217.154.218.30
       ├─ nginx: <domain>
       │    └─ /srv/www/owner-hosting/<tenant_id>/current/ (statisch)
       └─ nginx: hosting.<domain>
            └─ /run/owner-hosting/dashboard.sock
                 └─ owner-hosting-web
                      ├─ PostgreSQL: Konten, Registry, Entwürfe, Jobs, Audit
                      ├─ /var/lib/owner-hosting/tenants/<tenant_id>/
                      └─ Job Queue -> owner-hosting-worker
                           ├─ isolierter Preview-/Release-Build
                           └─ /srv/www/owner-hosting/<tenant_id>/releases/
```

- Die Domain bleibt beim Registrar, etwa Strato oder IONOS.
- nginx terminiert TLS, liefert die öffentliche Website statisch aus und leitet die Dashboard-Subdomain an die getrennte Anwendung weiter.
- Dashboard, Build-Worker und Release-Speicher sind nicht Teil des öffentlichen Request-Pfads.
- Jeder veröffentlichte Build landet in einem neuen Release-Verzeichnis. Erst nach erfolgreichem Build, Smoke Test und Prüfstatus wird der aktive Symlink beziehungsweise die nginx-Zielreferenz atomar gewechselt.
- Rollback aktiviert eine bereits vollständige Release-Fassung; es baut nicht aus einem möglicherweise beschädigten aktuellen Entwurf neu.
- Öffentliche Website und Wartungsseite funktionieren auch dann, wenn Dashboard, Datenbank oder externe APIs ausfallen.

Damit bleibt die Core Rule „statische Auslieferung ohne Laufzeitabhängigkeit“ erhalten: Dynamik existiert im getrennten Verwaltungs- und Veröffentlichungsweg, nicht beim Seitenaufruf.

## Deployment-Slots

Ein **Deployment-Slot** ist eine eigene Entität zwischen Host und Tenant. Er bindet einen öffentlichen Host und einen Dashboard-Host an genau einen Tenant und genau einen Release:

```text
deployment_slot
  public_host        eine öffentliche Domain
  dashboard_host     die zugehörige hosting.<domain>
  active_tenant_id   serverseitig, genau einer
  active_release_id  serverseitig, genau einer
  candidate_tenant_id  vorgemerkt, noch nicht veröffentlicht
  gate_policy        protected | public
  robots_policy      noindex bei Testumgebungen
```

Ohne diese Entität gäbe es nur zwei schlechte Möglichkeiten: die Zieladresse als weiteren Katalogstatus zu führen, womit jede Website Anspruch auf sie hätte, oder einen Pseudo-Tenant für wechselnde Websites, womit Historien, Verträge und Zugänge verschiedener Websites vermischt würden. Beides ist ausgeschlossen.

Verbindlich:

- Ein Host bleibt serverseitig eindeutig einem Slot zugeordnet. Über einen ausdrücklich bestätigten Slotwechsel darf derselbe Host einem anderen Tenant zugeordnet werden.
- Jede Website behält ihre eigene `tenant_id` mit eigener Vertrags-, Draft- und Releasehistorie. Ein Slotwechsel führt Historien nicht zusammen.
- Öffentlicher Release und Dashboard-Tenant werden **atomar gemeinsam** umgeschaltet. Es darf keinen Zeitpunkt geben, an dem die öffentliche Website zu einer anderen Website gehört als das Dashboard.
- Sitzungen sind an den Tenant gebunden. Nach einem Slotwechsel sind bestehende Dashboard-Sitzungen wertlos, ohne dass sie einzeln gelöscht werden müssten.
- Ein Wechsel läuft immer in zwei Schritten: Vormerken zeigt nur an, was passieren würde; erst eine ausdrückliche zweite Bestätigung startet Build und Umschaltung.
- Ein fehlgeschlagener oder parallel gestarteter Kandidat lässt den aktiven Release vollständig unverändert.

### Passwortgeschützte Staging-Domain

Ein Slot, der als Testumgebung dient, wird zusätzlich abgesichert:

- Zugriffsschutz über ein eigenes nginx-Basic-Auth, ausdrücklich **nicht** das Passwort der Developer-Plattform. Die htpasswd-Datei liegt außerhalb aller Repositories.
- `X-Robots-Tag: noindex, nofollow, noarchive` bei jeder Auslieferung, zusätzlich eine `robots.txt` im Release, die den gesamten Auftritt sperrt. Der Worker schreibt sie unabhängig davon, was das Projekt selbst erzeugt hat, und entfernt eine vorhandene `sitemap.xml`.
- Die ACME-Challenge auf Port 80 bleibt vom Passwortschutz ausgenommen, sonst bricht die Zertifikatserneuerung.
- `noindex` wird erst nach einer ausdrücklichen Entscheidung entfernt, unabhängig davon, ob der Passwortschutz fällt.

### Legacy-Adapter für unveränderliche Altprojekte

Eng begrenzte Ausnahme für Projekte, die das Owner-Hosting nicht kennen und nicht geändert werden dürfen:

- Der Quellpfad wird ausschließlich serverseitig aus einer Registry aufgelöst, nie aus einer Anfrage übernommen.
- Der Quellhash wird gegen die registrierte Fassung geprüft und im Joblog geführt.
- Gebaut wird in einer isolierten Kopie ohne die vorhandenen `dist/`-Ordner. Die aufgelöste Inhaltsdatei entsteht nur dort.
- In die Quelle wird nie geschrieben. Das wird zusätzlich durch `ProtectSystem=strict` mit ausdrücklich aufgezählten `ReadWritePaths` erzwungen, nicht allein durch Wohlverhalten des Adapters.
- Trägt ein Altprojekt dieselben Angaben zusätzlich fest im Quelltext, ändern sie sich beim Bearbeiten nicht mit. Solche Stellen werden als Warnung im Joblog gemeldet, nicht stillschweigend hingenommen und nicht durch Änderung der Quelle „behoben“.
- Die Prüfung umfasst **alle** Kontaktangaben des Vertrags, nicht nur E-Mail-Adressen. Rufnummern werden auf reine Ziffern reduziert verglichen, sonst gälte jede andere Schreibweise derselben Nummer als Abweichung.
- Warnungen erscheinen zusätzlich sichtbar im Protokoll der Fassung, nicht nur als Zeile im Joblog. Ein Protokoll liest niemand Zeile für Zeile; eine dort begrabene Warnung wirkt wie keine.

Der Adapter ist kein Muster für neue Websites. Neue Websites verwenden weiterhin den regulären Content-Loader mit `OWNER_HOSTING_CONTENT_FILE`.

### Dashboard ohne Vertrag

Wird eine Website ohne registrierten Editorvertrag in einen Slot gelegt, läuft ihr Dashboard in einem ehrlich schreibgeschützten Betriebsmodus: Zustand, Release, Erreichbarkeit und Verlauf sind sichtbar, Formulare gibt es nicht.

Bearbeitbare Felder werden **niemals** aus vorhandenem Text oder HTML erraten. Welche Felder editierbar sind, wird serverseitig festgelegt oder es gibt keine.

## Pflichtfrage bei Erstellung und Update

Bei der **Erstellung und bei jedem Update** wird für jeden Inhaltsblock entschieden:

> Soll der Owner diesen Block selbst bearbeiten können, ohne den Builder zu kontaktieren?

Die Antwort wird nicht nur im UI, sondern in der kanonischen Inhaltsquelle dokumentiert. Das bestehende Muster `content/<projekt>.json` wird um ein maschinenlesbares Schema ergänzt. Das Dashboard rendert daraus Felder, Hilfe, Validierung, Vorschau und Berechtigungen.

Für jedes Feld beziehungsweise jeden Block sind mindestens zu erfassen:

| Eigenschaft | Zweck |
|---|---|
| stabile ID und Pfad | Änderung, Historie und Rollback eindeutig zuordnen |
| `owner_editable` | `true` oder `false`, serverseitig erzwungen |
| Feldtyp | Kurztext, Langtext, Zahl, Geld, Datum, Zeit, Auswahl, Schalter, Bild, Liste oder strukturierter Block |
| Grenzen | Pflichtstatus, Länge, Wertebereich, erlaubte Optionen, Zeitzone, Währung, Bildformat, Seitenverhältnis und Dateigröße |
| Hilfetext und Beispiel | verständliche Bedeutung ohne Builder-Fachsprache |
| Preview-Ziel | betroffene Route, Komponente und Sprache |
| Prüfregeln | syntaktische, fachliche und gegebenenfalls Vier-Augen-Prüfung |
| Veröffentlichung | sofort nach zweitem Klick, zeitgesteuert oder nur nach Builder-Freigabe |
| Verantwortlicher | Owner, Builder oder benannte fachliche Person |
| Änderungsrisiko | niedrig, mittel, hoch mit daraus folgender Bestätigung |
| Datenschutz-/Rechtsbezug | Verweis ins Dateninventar und auf prüfpflichtige Texte |

Das Dashboard vertraut dem Schema nicht clientseitig. Erlaubte Pfade, Typen und Grenzen werden beim Speichern und Veröffentlichen serverseitig erneut geprüft.

### Eine Angabe ist ein Feld

Manche Angaben stehen in der Inhaltsdatei mehrfach, weil die Website sie in verschiedenen Formen braucht. Eine Telefonnummer ist der Regelfall: als Text für die Anzeige und in E.164-Form für den `tel:`-Link.

**Solche Formen werden niemals zu zwei Owner-Feldern.** Zwei Felder für dieselbe Angabe erzeugen einen Zustand, den niemand bemerkt: Der Owner ändert die sichtbare Nummer, vergisst die Wählform, und der Anruf-Link führt weiter zum alten Anschluss. Der Fehler ist auf der Website unsichtbar, weil beide Werte für sich gültig aussehen.

Verbindlich:

- Ein Feldtyp darf mehrere registrierte Pointer schreiben. Sie werden gemeinsam aus **einer** Eingabe abgeleitet und gemeinsam geschrieben.
- Der Owner gibt die fachliche Angabe ein, nicht ihre Darstellungsform. Bei Telefonnummern heißt das: Land aus einer Liste, nationale Nummer ohne führende Null. Trennzeichen setzt das Feld.
- Die Formatierung im Browser und die auf dem Server sind **dieselbe** Implementierung, nicht zwei gleichlautende. Andernfalls zeigt das Formular beim Tippen etwas anderes an, als am Ende veröffentlicht wird.
- Deutsche Rufnummern folgen DIN 5008: Ortsnetzkennzahl mit führender Null, ein Leerzeichen, Teilnehmernummer ungetrennt. Blockgrenzen innerhalb der Teilnehmernummer sind willkürlich und werden nicht erfunden.
- Eine Nummer aus dem Land der Website erscheint national, jede andere international mit Pluszeichen.
- Der Typkatalog wird um `phone` erweitert. `tel` als einfaches Textfeld ist für neue Verträge nicht mehr zulässig.

### Vertragsänderungen und bereits veröffentlichte Werte

Ändert sich die Form eines Feldes, werden gespeicherte Wertesätze **beim Laden** auf die aktuelle Vertragsfassung gehoben, nicht in der Datenbank überschrieben. Eine Revision ist der Beleg dafür, was tatsächlich veröffentlicht wurde; sie wird nicht nachträglich verändert. Ein Rollback auf einen alten Stand muss die Migration durchlaufen und die heutige Prüfung bestehen — das ist ein eigener Testfall, kein Nebeneffekt.

## Vertrag, den jede Website mitbringt

Eine Website wird nicht durch Sondercode im Dashboard angebunden. Sie liefert zwei versionierte, secret-freie Dateien nach [[80-Templates/Owner Hosting Website Contract]]:

```text
<Projektwurzel>/
  content/<website>.json
  owner-hosting/tenant.json
```

`tenant.json` beschreibt Identität, Domains, Inhaltsdatei, freigegebenes Buildprofil, statischen Ausgabeordner, Preview-Routen und Smoke-Test-Pfade. Es enthält keinen Owner, kein Passwort, kein OAuth-Token, keine absolute Serverablage und keinen frei ausführbaren Shell-Befehl.

Die Inhaltsdatei behält ihre normalen Faktenpfade. Unter dem reservierten Top-Level-Schlüssel `_hosting` liegt der builder-gepflegte Editorvertrag. Beispiel:

```json
{
  "_hosting": {
    "contract_version": 1,
    "schema_version": "2026-08-17.1",
    "blocks": {
      "contact": {
        "pointer": "/contact",
        "label": "Kontakt",
        "owner_editable": true,
        "preview_routes": ["/", "/kontakt"],
        "fields": {
          "phone": {
            "pointer": "/contact/phone",
            "label": "Telefonnummer",
            "type": "tel",
            "required": true,
            "max_length": 40,
            "help": "Öffentlich angezeigte Telefonnummer",
            "publish_policy": "owner_confirm",
            "risk": "medium"
          }
        }
      },
      "legal": {
        "pointer": "/legal",
        "label": "Rechtstexte",
        "owner_editable": false,
        "change_path": "builder_request"
      }
    }
  },
  "contact": {
    "phone": "+49 30 123456"
  },
  "legal": {
    "imprint": "..."
  }
}
```

Verbindliche Regeln:

- `_hosting` und `owner-hosting/tenant.json` sind Builder-Vertrag und im Dashboard niemals editierbar.
- Fehlt ein Pfad im registrierten Vertrag, gilt `owner_editable: false`.
- Der Browser sendet keine vollständige Inhaltsdatei zurück, sondern Änderungen an stabilen JSON-Pointern. Der Server wendet nur registrierte Pfade an.
- Block- und Feldfreigabe müssen zusammenpassen. Ein freigegebenes Feld in einem gesperrten Block bleibt gesperrt.
- Typen, Grenzen, erlaubte Optionen, Inhaltslänge, Bildregeln und Veröffentlichungsrichtlinie werden aus der registrierten Vertragsversion geprüft, nicht aus Clientdaten.
- Ein Feldname, Label oder Hilfetext ist keine Berechtigung. Autorisierung erfolgt ausschließlich über `tenant_id`, Rolle, Vertragsversion und JSON-Pointer.
- Der statische Website-Build erhält eine aufgelöste Datei ohne `_hosting`; vorhandener Website-Code muss keine Dashboard-API kennen.

Ein minimales `tenant.json` sieht so aus:

```json
{
  "contract_version": 1,
  "tenant_slug": "fahrschule-kladow",
  "public_host": "fahrschule-kladow.de",
  "dashboard_host": "hosting.fahrschule-kladow.de",
  "content_file": "content/fahrschule.json",
  "build_profile": "static-site-v1",
  "output_dir": "dist",
  "preview_routes": ["/", "/preise", "/kontakt"],
  "smoke_paths": ["/", "/impressum", "/datenschutz"],
  "release_retention": 10,
  "capabilities": {
    "contact_messages": false,
    "search_console": false,
    "builder_requests": true,
    "appointment_requests": "suggestions",
    "image_uploads": false,
    "maintenance_mode": true
  }
}
```

Buildprofile sind serverseitig registrierte Adapter, etwa `static-site-v1`, `astro-static-v1` oder `next-export-v1`. Das Manifest darf keinen String wie `npm run build` zur freien Ausführung liefern. Ein projektspezifischer Adapter wird als geprüfter, versionierter Code mit Hash in `packages/build-profiles/` aufgenommen.

## Was die Website tatsächlich an das Dashboard liefert

| Information | Quelle | Verwendung |
|---|---|---|
| öffentliche und Dashboard-Domain | `owner-hosting/tenant.json` | Host-zu-Mandant-Zuordnung, nginx und TLS |
| Inhaltsdatei | `content_file` | Import der Basiswerte und Auflösung beim Build |
| editierbare Blöcke/Felder | `_hosting.blocks` | Navigation und Formulare im Dashboard |
| Feldtypen und Grenzen | Feldvertrag | Controls und identische Servervalidierung |
| Labels, Hilfen und Beispiele | Feldvertrag | selbsterklärende Owner-Oberfläche |
| Preview-Routen | Blockvertrag und Manifest | gezielter Desktop-/Mobil-Preview |
| Veröffentlichungsrisiko und Policy | Feldvertrag | Bestätigung, Builder-Freigabe oder Zeitplanung |
| Buildprofil und Ausgabeordner | Manifest plus serverseitige Registry | reproduzierbarer statischer Build |
| Smoke-Test-Pfade | Manifest | Prüfung vor atomarer Aktivierung |
| Integrationsfähigkeiten | `capabilities` plus Freigabe in der Tenant Registry | Nachrichten, Search Console und Kalender nur bei vollständig aktiviertem Adapter |

Nicht von der Website geliefert werden Konten, Rollen, Passwörter, Sessions, Tokens, absolute Serverpfade, Release-IDs oder Betriebsgeheimnisse. Diese Informationen entstehen erst bei der serverseitigen Registrierung.

## Wie daraus automatisch das Dashboard entsteht

1. Die Registry lädt genau die aktive Vertragsversion des Mandanten, niemals `_hosting` aus einer vom Owner gesendeten Datei.
2. Das Dashboard gruppiert Blöcke nach `label`, `description` und Nutzeraufgabe. `owner_editable: false` erzeugt kein Formular, sondern gegebenenfalls den hinterlegten `change_path`.
3. Für jedes freigegebene Feld wählt die zentrale Typregistrierung das Control. `money` erzeugt beispielsweise Betrag plus feste Währung, `weekly-hours` einen Wocheneditor und `image` Upload, Zuschnitt, Alt-Text und Formatprüfung.
4. Dieselbe Contract-Bibliothek validiert im Browser für schnelle Rückmeldung und auf dem Server als verbindliche Entscheidung. Clientvalidierung allein gilt nie.
5. Autosave schreibt eine Draft-Revision mit Ausgangsrevision und Vertragsversion. Es verändert weder veröffentlichte Werte noch die Projektdatei.
6. `preview_routes` bestimmt, welche statischen Vorschauseiten der Worker aus Draft plus Projekt-Basis erzeugt. Das Dashboard zeigt diese Preview für Desktop und Mobil hinter der Owner-Sitzung.
7. Vor Veröffentlichung zeigt ein semantischer Vergleich nur geänderte Owner-Pfade mit alter und neuer verständlicher Darstellung. Der zweite Klick erzeugt den unveränderlichen Publish-Job.

Die Kundenwebsite braucht dafür kein Dashboard-SDK im Browser, keine API-URL und keine Laufzeitabfrage. Ihr einziger Integrationspunkt ist der Build: Das registrierte Buildprofil legt die vom Worker erzeugte, aufgelöste Inhaltsdatei an den vereinbarten Eingabepfad.

## Build-Schnittstelle zwischen Hosting und Website

Jede angebundene Website muss ihren Content beim Build aus genau einer austauschbaren Quelle lesen. Lokal bleibt `content_file` der Fallback. Im Hosting-Build setzt ausschließlich der Worker folgende Umgebungsvariablen:

| Variable | Inhalt | Regel |
|---|---|---|
| `OWNER_HOSTING_CONTENT_FILE` | absoluter Pfad zur validierten, aufgelösten JSON-Datei im isolierten Buildverzeichnis | Website liest diese Datei statt `content_file`; nicht in Client-JavaScript oder Release-Metadaten ausgeben |
| `OWNER_HOSTING_ASSET_DIR` | absoluter Pfad zu den für die gewählte Revision freigegebenen Assets | nur verwenden, wenn `image_uploads` aktiv und das Buildprofil dafür zugelassen ist |
| `OWNER_HOSTING_RELEASE_ID` | opake ID des Kandidatenrelease | nur für Buildprotokoll und Diagnose; nie als Inhaltsquelle verwenden |

Der projektspezifische Content-Loader folgt damit diesem festen Verhalten:

```text
wenn OWNER_HOSTING_CONTENT_FILE gesetzt:
  validierte Datei aus dem isolierten Build lesen
sonst:
  content_file aus tenant.json lesen
```

Der Worker kopiert den Projektstand in ein isoliertes Arbeitsverzeichnis, erzeugt dort aus Projekt-Basis plus gewähltem Owner-Overlay die aufgelöste Datei und startet den registrierten Adapter mit diesen Variablen. Der Website-Build liest keine Datenbank, kein Dashboard-API und keinen Live-Projektordner. Preview und Veröffentlichung verwenden exakt dieselbe Schnittstelle; nur Overlay-Revision, Release-ID und Ausgabeziel unterscheiden sich.

Das Buildprofil legt Befehl, erlaubte Paketinstallation, Netzwerkregel, Zeit-, CPU-, Speicher- und Ausgabelimit zentral fest. Weder `tenant.json` noch die Inhaltsdatei dürfen einen ausführbaren Befehl, eine Umgebungsvariable oder einen absoluten Pfad vorgeben. Fehlt der Hosting-Content-Loader im Projekt, schlägt `tenant lint` beziehungsweise der Initialbuild fehl; das Dashboard wird nicht mit einer nur scheinbar editierbaren Website aktiviert.

## Zentrales Datenmodell

Mindestens diese Entitäten werden getrennt geführt:

| Entität | Aufgabe und Mindestbindung |
|---|---|
| `tenants` | unveränderliche `tenant_id`, Slug, erlaubte Hosts, Status und serverseitiger Projektpfad |
| `memberships` | Konto, `tenant_id`, Rolle, Einladungs- und Sperrstatus |
| `contract_versions` | Manifest, Feldvertrag, Basis-Hash, Buildprofil und Aktivierungsstatus |
| `content_revisions` | immutable Owner-Overlays mit Elternrevision, Vertragsversion und Autor |
| `drafts` | Arbeitsstand, Ausgangsrevision, Konfliktstatus und Autosave-Zeitpunkt |
| `assets` | Original, Varianten, Prüfergebnis, Feldpointer, Revision und Aufbewahrung |
| `build_jobs` | Tenant, Eingaberevisionen, Idempotenzschlüssel, Lock, Logs, Limits und Ergebnis |
| `releases` | Contract-, Basis-, Content- und Asset-Revision, Dateipfad, Tests und Aktivstatus |
| `integrations` | Capability, Anbieter, Status und Verweis auf verschlüsselte Credentials |
| `messages` | Kontakt-, Builder- und Terminanfragen nur für aktivierte Datenflüsse |
| `audit_events` | append-only Akteur, Tenant, Aktion, Ziel, Vorher/Nachher-Verweis, Zeitpunkt und Ergebnis |

Mandantenbezogene Tabellen tragen `tenant_id` und zusammengesetzte Eindeutigkeits- beziehungsweise Fremdschlüssel, die versehentliche Beziehungen zwischen Mandanten verhindern. Jede Anfrage wird aus Session und Host auf denselben Tenant eingeschränkt. Builder-Zugriff über mehrere Mandanten ist eine explizite Rolle und kein Auslassen des Filters.

## Welche Inhalte der Owner bearbeiten darf

| Standard | Beispiele | Leitplanke |
|---|---|---|
| meistens bearbeitbar | Preise, Öffnungszeiten, Termine, Kontaktdaten, kurze Leistungs- und Hinweistexte | Grenzen, Vorschau und zweite Veröffentlichungshandlung |
| bedingt bearbeitbar | Stellenangebot an/aus, Teamdaten, einzelne Bilder, Aktionshinweise, strukturierte Listen | feste Struktur, Uploadprüfung, Alt-Text und gegebenenfalls Ablaufdatum |
| nicht frei bearbeitbar | Navigation, Seitenstruktur, Buildkonfiguration, Tracking, Consent, Rollen, Integrationen | Builder-Anfrage statt direktem Feld |
| geschützt | Impressum, Datenschutz, AGB und andere Rechtstexte | nur dokumentierter Änderungsauftrag mit benannter fachlicher Prüfung |

Ein Feld wird nicht deshalb freigegeben, weil seine technische Bearbeitung einfach ist. Entscheidungskriterien sind Wirkung auf Layout, Aussagen, Recht, Datenschutz, SEO, Integrationen und Folgekosten.

## Eine Website einrichten

Das Builder-CLI aus `packages/tenant-cli/` bildet den einzigen regulären Registrierungsweg. Die folgenden Befehlsnamen definieren die Zieloberfläche; sie werden mit dem zentralen Produkt implementiert:

1. `owner-hosting tenant lint <Projektwurzel>` prüft `tenant.json`, `_hosting`, alle JSON-Pointer, Feldtypen, Limits, Preview-Routen, Buildprofil, Ausgabeordner und Smoke-Pfade. Es führt keinen Build und keine Serveränderung aus.
2. `owner-hosting tenant plan <Projektwurzel>` zeigt Hostnamen, neue beziehungsweise gesperrte Felder, Startwerte, Buildprofil, benötigte DNS-/nginx-Schritte, Datenflüsse und offene Produktentscheidungen. Geheimnisse werden nie ausgegeben.
3. Der Builder bestätigt den Plan. `owner-hosting tenant register <Projektwurzel>` erzeugt die unveränderliche `tenant_id`, registriert die erlaubten Hostnamen und den aufgelösten absoluten Projektpfad serverseitig und importiert Basiswerte plus Vertragsversion.
4. Der Worker führt mit der importierten Basis und leerem Owner-Overlay einen isolierten Initialbuild aus. Die Projektdatei oder das Arbeitsverzeichnis werden dabei nicht verändert.
5. Erst wenn Build, Linkcheck, Smoke-Pfade, Pflichtseiten und statischer Ausgabepfad bestehen, wird ein erster Release angelegt.
6. nginx erhält zwei getrennte Hosts: `<domain>` liest den aktiven statischen Release; `hosting.<domain>` zeigt auf den zentralen Unix-Socket. Unbekannte Hosts werden abgewiesen.
7. A-Records und TLS werden geprüft. Die Tenant Registry wechselt von `registered` über `dns_pending` erst nach erfolgreicher Prüfung zu `active`.
8. Rollen, Aufbewahrung, Backup, Wartungskontakt, Dateninventar und aktivierte Integrationen werden festgelegt. Nicht entschiedene Adapter bleiben aus.
9. Ein Owner wird erst eingeladen, nachdem Domain, Dashboard, Veröffentlichung, Rollback und Mandantentrennung technisch abgenommen sind.
10. Die Abnahme veröffentlicht einen ungefährlichen Testwert, vergleicht Desktop und Mobil, prüft den Audit-Eintrag und rollt einmal auf den vorherigen Release zurück.

Bloßes Ablegen eines Ordners unter `projekte/` registriert kein Hosting. Die Developer-Plattform entdeckt Builds; das Owner-Hosting entsteht nur durch den bestätigten Tenant-Plan.

## Website oder Vertrag später aktualisieren

Ein Builder-Update läuft nicht als erneuter Erstimport:

1. `owner-hosting tenant plan <Projektwurzel>` vergleicht neue Projekt-Basis und Vertragsversion mit der aktiven Registry.
2. Unveränderte Owner-Pointer behalten ihre veröffentlichten und entworfenen Werte.
3. Neue editierbare Pointer starten mit dem Projektwert und erscheinen erst nach erfolgreicher Vertragsaktivierung im Dashboard.
4. Umbenannte Pointer benötigen eine explizite Migration `alt -> neu`; Ähnlichkeit des Namens reicht nicht.
5. Entfernte Pointer werden aus dem aktiven Overlay genommen, aber in alten Content- und Audit-Revisionen nicht gelöscht.
6. Typ-, Grenz- oder Optionsänderungen werden gegen alle vorhandenen Owner-Werte geprüft. Ein inkompatibler Wert blockiert die Vertragsaktivierung mit benanntem Feld und Migrationsbedarf.
7. Der Worker baut Vorschau und Kandidatenrelease mit neuer Basis, migriertem Overlay und neuer Vertragsversion. Bis alle Gates bestehen, bleiben Dashboard und Live-Website auf der vorherigen Vertragsversion.
8. Nach Aktivierung werden Vertragsversion, Basis-Hash, Overlay-Revision und Release-ID gemeinsam protokolliert. Offene Entwürfe auf alter Vertragsversion werden migriert oder sichtbar als konfliktbehaftet gesperrt.

Ein Builder kann aktuelle Owner-Werte über einen read-only Export in seine lokale Prüfung holen. Der Export überschreibt niemals still `content/<website>.json`; er erzeugt einen Vergleich beziehungsweise eine aufgelöste Testdatei unter `.runtime/owner-hosting/`.

## Veröffentlichungsablauf

1. Owner ändert nur freigegebene Felder in einem Entwurf.
2. Jede Änderung wird validiert und mit verständlicher Feldmeldung gespeichert.
3. Das Dashboard erzeugt eine Vorschau auf der realen Komponenten- und Flächenkombination, einschließlich Mobilansicht.
4. Eine Zusammenfassung zeigt geänderte Felder, betroffene Seiten, mögliche Risiken und den Vergleich zur laufenden Fassung.
5. Erst eine zweite, ausdrücklich als „Veröffentlichen“ beschriftete Handlung startet den Build.
6. Die Webanwendung schreibt einen unveränderlichen Job mit `tenant_id`, Vertragsversion, Basis-Hash, Entwurfsrevision und erwarteter aktiver Release-ID. Sie baut nicht selbst.
7. Der Worker erwirbt je Mandant ein Veröffentlichungs-Lock, prüft die erwartete aktive Revision erneut und bricht bei Paralleländerung mit Konfliktstatus ab.
8. In einem neuen, begrenzten Buildverzeichnis verbindet der Worker Projekt-Basis und Owner-Overlay, entfernt `_hosting`, prüft das Ergebnis gegen den registrierten Vertrag und startet ausschließlich das registrierte Buildprofil. Netzwerkzugriff ist standardmäßig aus; Laufzeit, CPU, Speicher, Zeit und Ausgabemenge sind begrenzt.
9. Der Worker führt Build, interne Links, Pflichtseiten, Smoke-Pfade und statische Dateiprüfung aus. Ein Fehler lässt Inhaltsrevision und Live-Symlink unverändert.
10. Nach Erfolg schreibt er den vollständigen Release in ein neues Verzeichnis, setzt erst dann den `current`-Symlink atomar und markiert Content-Revision und Release in einer Transaktion als aktiv.
11. Dashboard und Audit Log zeigen Zeitpunkt, Person, Vertragsversion, Content-Revision, Release-ID, Tests und Ergebnis.
12. Jede frühere veröffentlichte Fassung bleibt nach Aufbewahrungsregel wiederherstellbar. Rückgängig aktiviert eine vollständige Kombination aus Vertrag, Inhalt, Assets und Release; es löscht keine Historie.

Paralleländerungen werden vor Veröffentlichung erkannt. Der Owner sieht einen verständlichen Konfliktvergleich und überschreibt keine zwischenzeitlich veröffentlichte Änderung still.

## Dashboard-Bereiche

Der Seitenrahmen ist auf allen Unterseiten identisch. Seitenränder, Kopfzeile und die Position der Navigation dürfen sich beim Wechsel nicht verschieben. Zwei Ursachen sind dafür verantwortlich und beide werden gesetzt statt in Kauf genommen:

- Der Platz der Bildlaufleiste bleibt reserviert (`scrollbar-gutter: stable`). Sonst springt die ganze Seite um deren Breite, sobald eine Unterseite kürzer ist als die vorige.
- Die Kopfzeile steht in festen Spalten, nicht in umbrechender Flexbox. Sonst bestimmt die Länge des Websitenamens, wo die Navigation beginnt, und bei knappem Platz rutscht sie in eine zweite Zeile.

Ein springender Rahmen liest sich als Unruhe, noch bevor jemand ihn benennen kann. Er ist kein Schönheitsfehler, sondern das erste, was einer Verwaltungsoberfläche das Vertrauen entzieht.

### Übersicht

- Erreichbarkeit der öffentlichen Website und des Dashboards
- aktuell aktive Release-ID und Zeitpunkt der letzten Veröffentlichung
- Zertifikatsstatus und Ablaufwarnung
- letzte Störung, laufende Warnungen und Ergebnis des letzten Builds
- offene Entwürfe und ausstehende Builder-Anfragen
- verständliche Handlungsaufforderung statt roher Infrastrukturmeldungen

### Inhalte bearbeiten

- ausschließlich `owner_editable: true`
- Gruppierung nach Nutzeraufgabe und Website-Seite, nicht nach JSON-Pfad
- Autosave als Entwurf, explizite Vorschau, getrenntes Veröffentlichen
- mobile Vorschau und Warnung bei ungewöhnlicher Textlänge oder Bildwirkung
- sichtbarer Status „Entwurf“, „Wird geprüft“, „Veröffentlicht“, „Fehlgeschlagen“

### Bilder

- Upload nur für freigegebene Bildfelder
- vor Auswahl klare Vorgaben zu Motiv, Format, Mindestauflösung, Seitenverhältnis und maximaler Dateigröße
- serverseitige Typ- und Inhaltsprüfung, sichere Dateinamen, Metadatenbereinigung, Größenvarianten und moderne Formate
- Zuschnittsvorschau für alle betroffenen Breakpoints, Alt-Text und Rückkehr zum vorherigen Bild
- Original und erzeugte Varianten gehören zur Release-Historie

### Verlauf und Rückgängig

- unveränderliches Audit Log für Entwurf, Veröffentlichung, Rollback, Login, Rollen- und Wartungsmodusänderung
- Filter nach Datum, Person, Feld und Release
- Vergleich in verständlichen Vorher/Nachher-Werten
- Wiederherstellung einer vollständigen veröffentlichten Fassung

### Google Search Console

Das Dashboard kann Impressionen, Klicks, durchschnittliche Position, häufige Suchanfragen, starke Seiten und Indexierungsprobleme anzeigen. Die Search Analytics API liefert Klicks, Impressionen, Position und Dimensionen wie Anfrage oder Seite, kann aber insbesondere bei gruppierten Dimensionen begrenzt oder unvollständig sein; das UI erklärt deshalb Zeitraum, Datenverzug und Grenzen statt Vollständigkeit zu behaupten.[^gsc-query] Private Property-Daten benötigen autorisierten Zugriff und die passende Berechtigung.[^gsc-auth]

- Daten werden in Alltagssprache erklärt, etwa „So oft wurde die Website in Google gezeigt“.
- Zeitraum und Vergleichszeitraum stehen bei jeder Kennzahl.
- Es gibt keine SEO-Punktzahl und keine unbelegte Handlungsempfehlung.
- API-Fehler, fehlende Berechtigung und noch nicht verfügbare Daten besitzen eigene Zustände.
- OAuth-Tokens bleiben serverseitig, verschlüsselt und auf die kleinste erforderliche Berechtigung begrenzt.

#### Ein API-Schlüssel genügt nicht

Die Search Console API arbeitet ausschließlich mit einem autorisierten Konto: Die Daten gehören einer Property, nicht der API. Ein einfacher API-Schlüssel identifiziert nur ein Projekt und reicht deshalb nicht.[^gsc-auth] Verwendet wird ein **Dienstkonto**, dessen E-Mail-Adresse in der Search Console für die Property freigegeben wird.

Die Schlüsseldatei wird beim Einfügen geprüft und **nicht in der Datenbank** abgelegt, sondern als Datei mit Rechten `0600` daneben. Ein Datenbank-Backup enthält damit keine fremden Zugangsdaten. Zurückgezeigt wird sie nie; sichtbar bleiben Dienstkonto, Property und eine Prüfsumme.

#### Drei Zustände, nicht zwei

Zugangsdaten hinterlegen und Daten abrufen sind verschiedene Dinge und bekommen verschiedene Zustände: `aus`, `hinterlegt`, `aktiv`. „Hinterlegt“ heißt: Der Schlüssel liegt vor, abgerufen wird noch nichts.

Der Grund ist eine bewusst gesetzte Grenze: Der Hostingdienst läuft ohne Netzwerkzugang, weil er fremde Websites baut. Diese Grenze wird für eine Statistik nicht aufgehoben. Ein Abruf braucht einen getrennten, ausschließlich für Google freigegebenen Weg — eine eigene Entscheidung mit eigenem Datenfluss, nicht ein Nebeneffekt der Search-Console-Anzeige.

Solange kein Abruf möglich ist, zeigt das Dashboard Striche mit Begründung. **Keine Beispielzahlen.** Eine erfundene Kennzahl fällt erst auf, wenn jemand eine Entscheidung darauf gestützt hat.

Unabhängig davon liefert eine Property ohne Indexierung keine Zahlen. Eine Testfassung mit `noindex` ist kein Fehlerfall der Integration, sondern deren Voraussetzung, die noch fehlt.

### Nachrichten und Builder-Kontakt

- Kontaktformular-Nachrichten erscheinen nur, wenn die öffentliche Website dieses Feature tatsächlich besitzt und sein Datenfluss im Inventar steht.
- „Anfrage an den Builder“ sendet an `webdesign@johannstein.com` und klassifiziert Kleinigkeit, größeres Update oder Fehler.
- „Gesprächstermin anfragen“ sammelt mehrere Terminvorschläge; eine Kalenderintegration wird erst nach der offenen Produktentscheidung aktiviert.
- Versand zeigt Zustellung, Fehler und erneuten Versuch. Keine Anfrage gilt nur wegen eines optimistischen UI-Zustands als gesendet.

#### Formular vor Versandweg

Das Kontaktformular darf vor der Entscheidung über den E-Mail-Versand gebaut und freigeschaltet werden. Bedingung ist, dass die Anfrage tatsächlich ankommt und ihr Zustand benannt wird:

- Die Anfrage wird serverseitig gespeichert, nicht nur im Browser bestätigt.
- Der Zustellzustand ist ein eigenes Feld. `gespeichert` heißt: liegt beim Betreiber vor, es ging keine Benachrichtigung hinaus. Das steht im UI, nicht nur im Datenmodell.
- Der Betreiber hat einen belegten Weg, die Anfragen zu lesen und ihren Bearbeitungsstand zu setzen, auch ohne E-Mail.
- Ein Formular, das nur eine Erfolgsmeldung zeigt und nirgends ankommt, ist schlechter als kein Formular: Der Owner hält sein Anliegen für übermittelt und wartet.

### Zugang

- sichere Passwortspeicherung, Rate Limits, Sessionübersicht, Abmelden einzelner oder aller Sitzungen und protokollierte Passwortänderung
- Rollen mindestens `owner`, `editor` und `builder`; Berechtigung serverseitig je Mandant und Aktion
- CSRF-Schutz, sichere Cookies, zeitlich begrenzte Sitzungen, Login- und Änderungsprotokoll
- Einladungen und Recovery geben keine Kontenexistenz preis und laufen über einen zeitlich begrenzten Einmalweg

## Wartungsmodus statt Abschalten

Die Danger Zone bietet **kein** „Website offline nehmen“. Sie aktiviert einen reversiblen Wartungsmodus:

- alle öffentlichen Routen antworten mit HTTP `503 Service Unavailable` und einem plausiblen `Retry-After`; beide Semantiken sind im HTTP-Standard definiert.[^rfc-503][^rfc-retry]
- eine gestaltete Halteseite zeigt weiterhin Telefonnummer, Anschrift und Öffnungszeiten;
- Bestätigung erst nach Eingabe der vollständigen Domain;
- dauerhaft sichtbares Banner im Dashboard, solange der Modus aktiv ist;
- automatische Nachricht an den Builder und Erinnerung nach wenigen Tagen;
- ein Klick deaktiviert den Modus ohne Inhalts- oder Releaseverlust;
- Monitoring unterscheidet den geplanten Wartungsmodus von einer Störung.

Google empfiehlt für vorübergehende Ausfälle einen `503` und kann `Retry-After` beim erneuten Crawlen berücksichtigen; ein über längere Zeit bestehender `503` kann jedoch zur Entfernung von URLs aus dem Index führen.[^google-downtime] Deshalb braucht der Modus Erinnerung, Monitoring und eine klar begrenzte Dauer.

## Rechtstexte, Verantwortung und Haftungszuordnung

Impressum, Datenschutz, AGB und vergleichbare Texte sind keine frei editierbaren Textfelder. Das Dashboard zeigt den aktuellen Stand, fachlichen Owner, letzte Prüfung und „Änderung anfragen“. Eine Änderung wird als eigener Auftrag mit betroffenen Datenflüssen, Dienstleistern und fachlichem Review dokumentiert.

Für gewöhnliche, freigegebene Inhaltsfelder gilt als Betriebsmodell:

- Der Owner verantwortet Auswahl, Richtigkeit und Veröffentlichungsentscheidung seiner redaktionellen Änderung.
- Der Builder verantwortet die vereinbarte technische Plattform, serverseitige Grenzen, korrekte Übernahme und den dokumentierten Betriebsumfang.
- Die konkrete Haftungsverteilung, Freistellung, Prüfpflicht, Reaktionszeit und Versicherung werden im Hostingvertrag festgelegt. Das Brain trifft keine universelle Rechtsaussage; Texte bleiben prüfpflichtige Entwürfe.
- Das Dashboard zeigt vor Veröffentlichung, wer als Verantwortlicher des Feldes eingetragen ist, und protokolliert die bestätigende Person.

## Datenschutz und Auftragsverarbeitung

Je Projekt werden mindestens Zugangsdaten, Sitzungen, Audit Logs, Inhaltsänderungen, Uploads, Kontaktanfragen und Builder-Nachrichten inventarisiert. Hinzu kommen Search-Console-Daten und OAuth-Metadaten, wenn die Integration aktiv ist. Zweck, Rechtsgrundlage, Empfänger, Speicherort, Aufbewahrung, Löschung, Export, Backups und Subprozessoren stehen im [[80-Templates/Data Processing Inventory]].

Ob Builder und Owner im konkreten Modell Verantwortlicher, Auftragsverarbeiter oder gemeinsam Verantwortliche sind, wird fachlich geprüft. Erfolgt Verarbeitung im Auftrag, verlangt Art. 28 DSGVO einen Vertrag und hinreichende technische und organisatorische Garantien.[^gdpr-28] Der AVV, Unterauftragsverarbeiter, Weisungsweg, Löschung nach Vertragsende, Incident-Kommunikation und Rückgabe/Export sind daher vor Produktivbetrieb zu klären.

## Offene Produktentscheidungen

Diese Punkte werden dem Nutzer vor Implementierung des Dashboard-Produkts vorgelegt und nicht geraten:

1. **Search Console:** Läuft jede Property im Google-Konto des Owners mit delegiertem Zugriff für den Builder, oder zentral im Builder-Konto mit Owner-Zugriff? Wird als Domain-Property per DNS oder als URL-Prefix verifiziert? Die Site Verification API arbeitet im Kontext des authentifizierten Kontos und kann Ownership-Verifikation automatisieren.[^site-verification] Zusätzlich offen: über welchen Weg der Dienst Google erreichen darf, ohne seine Netzwerkisolierung insgesamt aufzugeben.
2. **E-Mail-Versand:** Welcher Dienst versendet transaktionale Nachrichten an `webdesign@johannstein.com`, und wer hält Vertrag, Domainauthentifizierung, Logs und Löschfristen?
3. **Termine:** Wird ein echter Kalender mit Verfügbarkeiten und Konfliktprüfung angebunden, oder sendet das Formular nur mehrere Vorschläge?
4. **Erstzugang:** Erhält der Owner einen zeitlich begrenzten Einladungslink über einen verifizierten Kanal, oder werden Zugangsdaten persönlich beziehungsweise getrennt übermittelt?

Bis zur Entscheidung bleiben Integrationsadapter deaktiviert. Das Konzept und die statische Website werden dadurch nicht blockiert.

Die **Oberfläche** einer offenen Entscheidung darf trotzdem gebaut werden — Kontaktformular, Search-Console-Einrichtung, Terminvorschläge. Sie muss dann ihren tatsächlichen Zustand benennen und darf keinen Erfolg behaupten, den es nicht gibt. Was der Owner eingibt, wird gespeichert und geht nicht verloren.

## Reihenfolge für den Bau des zentralen Produkts

1. **Fundament:** Repository unter `/srv/Web-Design/projekte/owner-hosting/`, PostgreSQL-Migrationen, Tenant Registry, Hostauflösung, getrennte Dienstbenutzer, Unix-Socket und Basis-Observability.
2. **Vertrag und CLI:** Parser für `tenant.json` und `_hosting`, JSON-Pointer-Allowlist, Typkatalog, `lint`, `plan`, `register` und Contract-Diff ohne Dashboard-UI.
3. **Release-Kern:** isolierter Worker, registrierte Buildprofile, Projekt-Basis plus Owner-Overlay, Preview-Release, Smoke-Tests, atomarer Symlink, Rollback und Wartungsmodus.
4. **Owner-Oberfläche:** Anmeldung, Mandantenrollen, generierte Formulare, Draft-Autosave, Vergleich, Preview, Publish, Verlauf und verständliche Fehlerzustände.
5. **Pilot:** genau eine ungefährliche Website mit wenigen Feldern wie Telefon, Öffnungszeiten und Stellen-Schalter; Cross-Tenant-, Fehler-, Restore- und Rollback-Tests vor einem zweiten Mandanten.
6. **Erweiterungen:** Bilder, Nachrichten, Search Console, E-Mail und Kalender jeweils erst nach eigenem Datenfluss, Anbieterentscheidung, Berechtigungsmodell und Betriebsnachweis.

Das zentrale Produkt wird also vor der ersten Kundenanbindung gebaut. Eine neue Website erweitert anschließend nur Vertrag, Registry und Content; sie erzeugt keine neue Dashboard-Anwendung.

**Umsetzungsstatus am 17. August 2026:** Dies ist die verbindliche Zielarchitektur und der Vertrag für die Umsetzung. Repository, Dienste, CLI, Datenbank und Tenant Registry sind noch nicht angelegt. Der Pfad `/srv/Web-Design/projekte/owner-hosting/` bezeichnet den beschlossenen Bauort, nicht bereits laufende Infrastruktur. Bis Fundament, Release-Kern und Mindestnachweise umgesetzt sind, wird keine Website als Owner-editierbar beworben oder registriert.

## Mindestnachweise vor Produktivbetrieb

- Mandantentrennung und negative Rollentests
- unbekannter oder nicht zum Session-Tenant passender Host wird vor jeder Datenabfrage abgewiesen
- Schema-Manipulation und nicht freigegebene Feldpfade serverseitig abgewiesen
- absolute Pfade, `..`, Root-verlassende Symlinks, unbekannte Buildprofile und Manifest-Shellbefehle werden abgewiesen
- unveränderte Owner-Werte bleiben bei Basis- und Vertragsupdates erhalten; Umbenennung, Typwechsel und alte Entwürfe sind als Migration oder Konflikt getestet
- ein Rollback auf eine Revision der vorigen Vertragsfassung läuft durch die Migration und besteht die heutige Prüfung
- ein Feld mit mehreren Pointern schreibt alle gemeinsam; Anzeige- und Wählform einer Rufnummer können nicht auseinanderlaufen
- fest im Quelltext hinterlegte Kontaktangaben werden als Warnung gemeldet und sind im Protokoll der Fassung sichtbar
- hinterlegte Integrations-Credentials erscheinen in keiner HTML-Antwort, keinem Protokoll und keinem Datenbank-Backup
- Buildfehler lässt aktive Website unverändert
- Preview und Release lesen dieselbe aufgelöste Build-Schnittstelle; der statische Release enthält weder `_hosting` noch Secrets oder interne Pfade
- atomarer Publish und vollständiger Rollback getestet
- Uploads gegen Typ, Größe, Inhalt und Pfadmanipulation geprüft
- Session-, Rate-Limit-, CSRF-, Recovery- und Audit-Log-Tests
- Wartungsseite liefert auf jeder öffentlichen Route `503`, `Retry-After` und die vorgesehenen Kontaktdaten
- öffentliche Website bleibt ohne Dashboard, Datenbank und externe APIs erreichbar
- Backup und Restore von Schema, Entwürfen, Releases, Audit Logs und Integrationskonfiguration getestet
- Dateninventar, Hostingvertrag, AVV-Prüfung und prüfpflichtige Rechtstexte aktuell

[^gsc-query]: [Google Search Console API: Search Analytics query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
[^gsc-auth]: [Google Search Console API: Voraussetzungen und Berechtigungen](https://developers.google.com/webmaster-tools/v1/prereqs)
[^rfc-503]: [RFC 9110, 503 Service Unavailable](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6.4)
[^rfc-retry]: [RFC 9110, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3)
[^google-downtime]: [Google Search Central: Planned site downtime](https://developers.google.com/search/blog/2011/01/how-to-deal-with-planned-site-downtime)
[^gdpr-28]: [EUR-Lex: DSGVO, Artikel 28](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679)
[^site-verification]: [Google Site Verification API: Getting Started](https://developers.google.com/site-verification/v1/getting_started)
