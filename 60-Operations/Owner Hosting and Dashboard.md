---
type: canonical
status: canonical
updated: 2026-08-24
review_by: 2027-02-24
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

### Eine weitere Hosting-Subdomain kostet keine Anpassung

Eine neue Hosting-Subdomain wird eingesetzt und ist sofort nutzbar. Was dafür geschieht, steht abschließend hier:

1. DNS-Eintrag auf den Server.
2. nginx-Serverblock und Zertifikat — die beiden Schritte, die root brauchen.
3. Der Name kommt in `OWNER_HOSTING_DASHBOARD_HOSTS` (kommagetrennt). Der Dienst trägt **bei jedem Start** jeden dort genannten Namen als Dashboard-Host des Slots ein und entfernt Namen, die nicht mehr darin stehen. Ein Dashboard, das unter einem abgeschalteten Namen erreichbar bliebe, wäre kein Rest, sondern eine offene Tür.

Kein Datenbankeingriff, keine Codeänderung, keine Anpassung im Dashboard. Insbesondere braucht **die gehostete Website selbst** keine Vorbereitung für den Editor: Kopfzeile, Navigation, Anschrift, Kontaktwege und die Namen der Rechtstexte sind über die allgemeinen Sperren von der ersten Sekunde an geschützt, und Bilder sind nur austauschbar, soweit ein Vertrag sie nennt. Was eine Website darüber hinaus freigibt, steht in ihrem Vertrag und in `owner-hosting/tenant.json` — nicht in einer Dashboard-Ansicht, die je Website angepasst werden müsste.

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
- Dasselbe gilt für `image`: Ein Bildfeld beschreibt die Dateien, die entstehen müssen, und den Alternativtext. Ein Feld, in das ein Dateiname eingetippt wird, ist kein Bildfeld.

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
    "scheduled_publish": true,
    "content_export": true,
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

Ob etwas bearbeitbar ist, und **wo** es bearbeitet wird, sind zwei getrennte Entscheidungen. Die zweite beantwortet eine einzige Frage: Erscheint der Wert an mehreren Stellen der Website? Dann ist er zentral. Steht er an genau einer Stelle, gehört er auf die Seite. Ein Fahrzeugbild ist danach keine Angabe über den Betrieb, sondern eine Stelle.

### Was auf keiner Website bearbeitet wird

Die Tabelle oben ist eine Entscheidungshilfe je Vertrag. Darunter liegt eine Liste, die **ohne Vertrag** gilt und von keinem Vertrag aufgehoben werden kann. Sie steht als Code in `packages/core/sperren.mjs` und wird beim Öffnen des Seiteneditors auf das gebaute Dokument angewendet, bevor irgendeine Stelle als bearbeitbar angeboten wird.

| Bereich | Erkannt an | Warum gesperrt |
|---|---|---|
| Kopfzeile | `header`, `[role=banner]` | Steht auf jeder Seite. Eine Änderung wirkt überall zugleich, sichtbar ist nur die eine Stelle. |
| Navigation und Menü | `nav`, `[role=navigation]`, Schublade, Sprungmarke | Namen und Reihenfolge hängen an den Adressen der Seiten und stehen zusätzlich in der Fußzeile. |
| Impressum, Datenschutz, AGB, Widerruf | Verweise, deren Adresse den Namen enthält | Eine Seite, die nicht so heißt, ist für ihre Pflicht nicht auffindbar. Umbenennen ist kein Textwunsch, sondern ein Rechtsverlust. |
| Seitenliste der Fußzeile | `footer nav`, `footer ul` | Führt dieselben Namen wie die Navigation. |
| Anschrift | `address` | Zentrale Angabe: Kontaktseite, Fußzeile, Impressum, strukturierte Daten. |
| Anruf- und Mailverweise | `a[href^=tel:]`, `a[href^=mailto:]`, WhatsApp | Zentrale Angabe. An einer Stelle geändert stünde im Impressum weiter die alte Nummer, und der Anruf-Link ginge weiter auf sie. |
| Angaben für Suchmaschinen und Technik | `[itemprop]`, `script`, `style`, `template`, `noscript` | Keine sichtbare Beschriftung. |

**Das Logo wird nicht ersetzt.** Ein Bild ist im Seiteneditor nur dann austauschbar, wenn der Vertrag es als Bildfeld nennt. Das Logo steht dort ausdrücklich nicht: Es erscheint in Kopfzeile, Menü, Fußzeile, als Favicon und im Vorschaubild für soziale Netzwerke — vier bis fünf Stellen, von denen der Editor nur eine kennt. Eine davon zu tauschen hieße, es an den übrigen nicht getauscht zu haben. Ein Fahrzeugbild ist der Gegenfall: Es steht an ein bis zwei Stellen, und beide gehören zu demselben Feld. Ein Logowechsel ist ein Builder-Auftrag, keine Bearbeitung.

Ein Vertrag **ergänzt** diese Liste über `gesperrt: [{ auswahl, grund }]` — für das, was an einer bestimmten Website besonders ist, etwa die Rechtszeile der Fußzeile oder die Beschriftungen von Kennzahlen. Aufheben kann er keine der allgemeinen Regeln.

Eine gesperrte Stelle ist nicht stumm. Sie lässt sich anklicken und antwortet mit ihrer Begründung — dieselbe, die in der Tabelle steht. Eine Stelle, auf die gar nichts passiert, sieht aus wie ein Fehler des Editors und nicht wie eine Entscheidung; jede Sperre trägt deshalb einen Grund und keine bloße Verweigerung.

### Der Owner ändert nichts Tiefgreifendes ohne Freigabe

Zentrale Angaben sind nicht deshalb harmlos, weil sie an einer Stelle gepflegt werden — sie sind es gerade deswegen nicht: Sie wirken überall zugleich. Für sie gilt eine zusätzliche Abstufung, unabhängig von `owner_editable`:

- **Zentral und mit Rechtswirkung** — Telefon, E-Mail, Anschrift, Bürozeiten. Bearbeitbar im Formular „Zentrale Angaben“, dort mit Kennzeichnung „auch in Rechtstexten“ und vor dem Veröffentlichen mit ausdrücklich bestätigter Prüfung. Auf der Seite gesperrt.
- **Zentral ohne Rechtswirkung** — Teamgröße, Theorieabende, Hinweistexte. Bearbeitbar im Formular, und wenn der Vertrag es ausdrücklich erlaubt, auch unmittelbar auf der Seite.
- **Zentral und gesperrt** — Firmenname, Inhaber, Navigation, Seitennamen, Logo. Nur über einen Builder-Auftrag. Der Owner sieht die Stelle, ihre Begründung und den Weg dorthin — nicht ein Eingabefeld.

Die Zuordnung ist Vertragssache und steht im Code, nicht in der Oberfläche. Ein Feld wird nicht dadurch änderbar, dass jemand im Dashboard etwas anklickt.

### Der Copyright-Hinweis steht immer

Jede gehostete Website zeigt in der Fußzeile einen Copyright-Hinweis — **immer**, auch wenn das Zeichen „©“ in der Vorlage fehlt oder in der Schrift nicht vorhanden ist. Fehlt es, wird es ergänzt; ist es nicht darstellbar, tritt „(c)“ an seine Stelle, nicht eine Lücke. Der Hinweis nennt das Jahr und den Betreiber und steht neben Impressum und Datenschutz.

Er ist kein Gestaltungselement und deshalb auch keine Stelle, die der Owner ändert: Er gehört zur Rechtszeile der Fußzeile und ist mit ihr gesperrt. Beim Anlegen einer Website ist er Teil der Abnahme — eine Fußzeile ohne ihn gilt als unvollständig, nicht als schlicht.

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

### Der Zeitpunkt gehört an die Veröffentlichung

Zeitgesteuertes Veröffentlichen wird **nicht** als Modus und **nicht** je Feld umgesetzt.

Ein Feld mit eigenem Termin erzeugt Zwischenstände, die niemand entworfen hat: die neue Telefonnummer ab Montag, die alten Öffnungszeiten noch bis Mittwoch. Die Vorschau kann die Frage „wie sieht die Website dann aus?“ dann nicht mehr beantworten, weil es kein *dann* mehr gibt, sondern eines je Feld.

Ein Modus ist versteckter Zustand. Er wird angeschaltet, vergessen, und eine dringende Korrektur erscheint Wochen später nicht — ohne dass irgendetwas danach aussieht, als sei etwas falsch. Ein Schalter, der die Bedeutung des Veröffentlichen-Knopfes umdeutet, ist eine der verlässlichsten Quellen für „ich habe es doch gemacht“.

Eine Vormerkung ist deshalb dasselbe wie eine Veröffentlichung — geprüfter Entwurf, sichtbarer Vergleich, bestätigte Rechtsprüfung — nur mit einem Zeitpunkt. Verbindlich:

- **Gebaut wird zum Termin, nicht vorher.** Sonst zählt der Stand der Quelle von heute statt der von dann. Damit ein Fehler nicht unbeobachtet auftritt, läuft beim Vormerken sofort ein Probebau, der nichts umschaltet.
- **Eine Vormerkung ist kein laufender Vorgang.** Sie darf die Veröffentlichungswarteschlange nicht belegen, sonst ist tagelang nichts anderes veröffentlichbar.
- **Höchstens eine offene Vormerkung je Website.** Wer währenddessen etwas anderes veröffentlicht, entscheidet ausdrücklich über sie. Bliebe sie stillschweigend bestehen, fiele die Zwischenkorrektur am Termin wieder heraus, und der Zusammenhang wäre für niemanden erkennbar.
- **Verspätet ja, vergessen nein.** War der Dienst zum Termin nicht verfügbar, wird innerhalb eines begrenzten Fensters nachgeholt und als verspätet protokolliert. Ältere Vormerkungen verfallen sichtbar, statt Werte nachzuschieben, deren Inhalt niemand mehr präsent hat.
- **Ein Neustart mitten in der Ausführung öffnet die Vormerkung wieder.** Genau das erzeugt ein Systemupdate: Der Termin war richtig, der Inhalt geprüft, nur der Bau kam nicht durch. Sie als „ausgeführt“ stehen zu lassen wäre die schlechteste aller Möglichkeiten — die Website bliebe alt, und niemand erführe davon. Das Nachholfenster bleibt dabei in Kraft, damit daraus kein endloses Wiederholen wird.
- **Gehört der Host inzwischen einer anderen Website, verfällt die Vormerkung.** Eine Veröffentlichung schaltet den Slot auf ihren Tenant um; eine alte Vormerkung würde eine zwischenzeitlich bereitgestellte Website nachts verdrängen, ohne Klick und ohne dass jemand die beiden Vorgänge in Verbindung brächte. Das ist der einzige Weg, auf dem dieser Dienst eine fremde Website vom Netz nehmen könnte, und er wird geschlossen.
- **Ein inhaltlich fehlgeschlagener Bau wird nicht wiederholt, sondern gemeldet.** Ein automatischer zweiter Versuch würde denselben Fehler erzeugen. Der Zustand wird nicht doppelt geführt, sondern am Job abgelesen; er ist die einzige Wahrheit über den Bau. Der Hinweis verschwindet von selbst, sobald danach etwas erfolgreich veröffentlicht wurde.
- **Datum und Uhrzeit, keine Tageszeit.** Eine gröbere Angabe verlagert die Entscheidung nur auf den Server und macht die Prüfung „ist das schon passiert?“ unbeantwortbar.
- **Zeitzone an genau einer Stelle.** Gespeichert in UTC, eingegeben und angezeigt in der Ortszeit der Website. An zwei Stellen gerechnet, weicht eine davon einmal im Jahr um eine Stunde ab — nachts, wenn niemand hinsieht.

### Nach der Veröffentlichung: sagen, was jetzt anders ist

Der Vergleich vor der Entscheidung und die Auskunft danach sind zwei verschiedene Fragen. Vorher: „was werde ich ändern?“ Nachher: „was ist jetzt anders als vorher, und wer hat das wann entschieden?“

Jede veröffentlichte Fassung bekommt deshalb eine Ansicht in ganzen Sätzen, verglichen gegen die **vorherige** Revision und nicht gegen den heutigen Stand — sonst zeigt die Ansicht eines alten Standes etwas anderes, sobald danach etwas veröffentlicht wurde. Die Übersicht führt eine Zusammenfassung davon. Eine Zeile im Verlauf mit einer Uhrzeit ist keine Auskunft.

## Wie viel Text eine Oberfläche verträgt

Ein Dashboard bedient jemand, der eigentlich etwas anderes zu tun hat. Jeder Satz, den er lesen muss, um einen Knopf zu finden, ist ein Satz zu viel — und beim zweiten Besuch liest er ihn ohnehin nicht mehr.

Verbindlich:

- **Auf der Seite steht, was zu tun ist. Warum es so ist, steht dahinter.** Begründungen, Randfälle und Zusicherungen gehören hinter ein Erklärzeichen, das bei Zeigen oder Tippen aufgeht.
- Das Erklärzeichen funktioniert **ohne JavaScript**: ein fokussierbarer Knopf, `:hover` und `:focus-within`. Ein Fingertipp erzeugt Fokus, also gilt dieselbe Regel am Handy.
- **`aria-describedby` bleibt.** Text in eine Blase zu verschieben, die ein Screenreader nicht mehr findet, ist keine Reduktion, sondern Verlust.
- Ersatzlos verschwinden: Sätze, die nur beruhigen; Wiederholungen über gleichartige Felder hinweg; Erklärungen zu dem, was der Knopf selbst sagt.
- Eine Aktion, die man oft braucht, ist ein **Knopf mit Beschriftung**, keine Karte mit Erklärtext. „Website ansehen“ mit Pfeil nach rechts oben braucht keinen Satz darüber.
- Symbole werden **gezeichnet, nicht als Unicode gesetzt**. Ein Glyph wie ⓘ sieht je nach Schrift und System verschieden aus, mal zu groß, mal zu blass.

## Einführung beim ersten Besuch

Beim ersten Aufruf führt ein kurzer Rundgang durch die Stellen, die man kennen muss: Die Seite dunkelt ab, der jeweilige Bereich bleibt als ausgeschnittener Scheinwerfer frei.

- **Gemerkt wird im Browser, nicht an der IP-Adresse.** Eine IP wechselt im Mobilfunk mehrmals täglich und ist in einem Büro für alle dieselbe; die Einführung käme mal ständig wieder und bliebe mal jemandem vorenthalten, der sie nie gesehen hat. Ein Eintrag im lokalen Speicher trifft genau, was gemeint ist, und ist keine personenbezogene Angabe, die gespeichert werden müsste.
- Der Scheinwerfer ist ein **echtes Loch**, kein halbdurchsichtiger Kasten über dem Element. Sonst wird ausgerechnet das unlesbar, worauf gezeigt wird.
- Der Rundgang läuft **nur auf der Einstiegsseite**. Einer, der auf jeder Unterseite anspringt, ist eine Belästigung.
- Er ist jederzeit abbrechbar, mit Escape und mit einem Klick daneben, und über die Einstellungen wiederholbar.
- Ein Schritt ohne vorhandenes Ziel wird übersprungen, nicht auf einen leeren Bereich gezeigt.

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

### Bearbeiten: zwei Ansichten, eine Entscheidungsregel

Ein Dashboard mit **einer** Art zu ändern behandelt zwei verschiedene Dinge gleich. Eine Telefonnummer steht an sieben Stellen der Website und gehört an eine Stelle gepflegt. Ein Satz auf der Startseite steht an genau einer Stelle und gehört genau dort geändert. Ein Formular für beides macht das Formular lang und den Satz unauffindbar.

Verbindlich sind deshalb **zwei Ansichten unter einem Bereich** — nicht zwei Bereiche nebeneinander. Der Umschalter steht *innerhalb* von „Bearbeiten“ und benennt beide Ansichten jedes Mal, auch die, auf der man gerade ist.

| Ansicht | Was dort gehört | Warum |
|---|---|---|
| Auf der Seite | Texte, Ausrichtung, Textgröße, Versatz, Bilder | Die Stelle ist ihr eigener Kontext. Man sieht, was man ändert. |
| Zentrale Angaben | Telefon, Mobil, E-Mail, Öffnungszeiten, Stellenanzeige an/aus | Der Wert erscheint an vielen Stellen zugleich; er wird einmal gepflegt, nicht siebenmal. |

Die Zuordnung ist **keine Vermutung der Oberfläche**, sondern steht am Feld: `surface: "zentral"` oder `surface: "seite"`. Ein Feld erscheint in genau **einer** der beiden Ansichten. Zwei Wege zu derselben Änderung hießen, sich zwischen ihnen entscheiden zu müssen, bevor man weiß, worin sie sich unterscheiden.

Weiterhin gilt für die zentralen Angaben: ausschließlich `owner_editable: true`, Gruppierung nach Nutzeraufgabe statt nach JSON-Pfad, Autosave als Entwurf, getrenntes Veröffentlichen, sichtbarer Status.

Eine Landesvorwahl wird in der aufgeklappten Liste mit dem Land dahinter gezeigt („+49 (Deutschland)“), im geschlossenen Feld nur als Vorwahl. Ohne Ländernamen wäre die Liste eine Zahlenkolonne, in der niemand +351 von +352 unterscheidet; im geschlossenen Feld ist die Frage dagegen beantwortet, und der Name drängt die Nummer daneben zusammen. Die kurze Anzeige wird erst im Browser aufgebaut — ohne Skript bleibt der volle Text stehen, statt eine falsche Vorwahl zu behaupten.

### Der Seiteneditor

Der Editor zeigt die **gebaute Website** in einem Rahmen und macht jede bearbeitbare Stelle anklickbar. Beim Klick wird die Stelle hervorgehoben, daneben erscheint eine kleine Leiste. An einem Bild sitzt der Knopf zum Ersetzen unten rechts im Bild.

Was dabei entsteht, ist eine **Darstellungsregel** neben der Website, kein Eingriff in die Quelle:

```text
{ seite: "kontakt/index.html", anker: "main:1/section:2/p:3",
  text:  "Neuer Satz",
  stil:  { ausrichtung, groesse, versatz } }
```

Verbindlich:

- **Der Anker ist eine Struktur, keine Suche.** Er zählt Elemente vom `<body>` aus, je Schritt Elementname und wievieltes Element dieses Namens. Er kann nicht „irgendwo passen“ und nichts einfügen, was es nicht schon gibt. Textsuche als Anker ist ausgeschlossen: Derselbe Satz kommt zweimal vor, und dann trifft es beim nächsten Bau die andere Stelle.
- **Nur reiner Text wird ersetzt.** Enthält die Stelle weitere Elemente, bleibt sie unangetastet. Über eine Regel kann deshalb weder Markup noch ein Skript in die Website gelangen; der neue Text wird maskiert.
- **Gestaltung ist eine aufgezählte Liste, kein CSS.** Vier Ausrichtungen, sechs Textgrößen, ein begrenzter Versatz. Ein Editor, mit dem sich eine Seite frei bauen lässt, baut sie irgendwann kaputt, und niemand kann sagen, wann das passiert ist. Ein Versatz über die Grenze hinaus wird begrenzt, nicht abgelehnt — er ist ein Ziehen über den Rand, kein Angriff.
- **Gestaltet wird über eine Datei, nicht über `style`-Attribute.** Eine Website mit `style-src 'self'` in ihrer eigenen Richtlinie ignoriert Inline-Stile, und zwar lautlos.
- **Der Rahmen zeigt den aktiven Release**, nicht die Quelle und keine eigens gebaute Vorschau. Die Quelle ist ein Buildeingang, kein Dokument; eine Vorschau je Tastendruck wäre langsam und prüfte den Anker gegen ein Dokument, das gleich wieder verschwindet.
- **Die Rahmensperre der Website wird nur in dieser Auslieferung entfernt**, nie im Release. Statt ihrer bekommt die Antwort eine eigene Richtlinie als Kopfzeile, die das Einbetten allein der eigenen Herkunft erlaubt.
- **Umrandung, Leiste und Bildknopf liegen außerhalb des Rahmens.** Nichts, was der Editor zeichnet, kann dadurch in einem Release landen. Die Farbe der Umrandung sagt, womit man es zu tun hat: blau für eine Stelle, die man hier ändert, warngelb für eine zentrale Angabe, grau für einen gesperrten Bereich. Eine Auswahl, die überall gleich aussieht, verspricht überall dasselbe.
- **Ein Bild hat genau einen Handgriff und genau ein Bedienelement dafür.** Der Knopf „Bild ersetzen“ sitzt unten rechts im Bild, leicht blau eingefärbt, damit er sich von einem Foto abhebt; frühere Fassungen stehen als Auswahl unmittelbar links daneben und nur dann, wenn es welche gibt. Eine zweite Leiste über dem Bild mit derselben Beschriftung und demselben Knopf gab es früher und ist entfallen: Zwei Bedienelemente für dieselbe Sache sind eines zu viel, und das obere lag zudem woanders als das Bild, um das es ging.
- **Angewendet wird nach dem Bau und vor den Prüfungen.** Nach dem Bau, weil die Quelle unangetastet bleibt und ein Legacy-Adapter davon nichts wissen muss. Vor den Prüfungen, weil das Ergebnis geprüft gehört: Ein Verweis auf ein Stylesheet, das es nicht gibt, muss dieselbe Prüfung reißen wie jeder andere tote Verweis.
- **Eine Regel ohne Stelle bricht den Bau nicht ab, sondern wird protokolliert.** Eine Website, die wegen eines verschobenen Absatzes nicht mehr baut, ist der schlechtere Zustand. Verhindert wird der Fall früher: Beim Speichern schickt der Editor den ursprünglichen Text der Stelle mit, der Server löst den Anker gegen das ausgelieferte Dokument auf und vergleicht. Stimmt es nicht überein, wird die Regel abgelehnt — statt später lautlos einen fremden Absatz zu überschreiben.
- **Der Server sagt, welche Stellen Text sind, nicht der Browser.** Beim Ausliefern der Seite liegt ein Index aller Stellen bei, die **im ausgelieferten Dokument** reinen Text enthalten, mit ihrem Text. Websites führen eigene Skripte aus, und einige schreiben Text nach dem Laden um; ein Editor, der den Ausgangstext aus dem fertigen Dokument nimmt, hielte den erzeugten Text für den ursprünglichen. Stellen, deren Text im fertigen Dokument abweicht, werden gar nicht erst zum Bearbeiten angeboten — eine Änderung daran würde beim nächsten Laden überschrieben.
- **Der Entwurf trägt den ganzen Stand, nicht die Änderung.** Ohne Entwurf lädt der Editor die Regeln des aktiven Release als Ausgangspunkt und speichert immer den vollständigen Satz. Andernfalls verschwände jede früher veröffentlichte Änderung beim nächsten Bau: Gebaut wird aus der Quelle, und die kennt sie nicht. Beim Veröffentlichen wird trotzdem nur gezeigt, was sich gegenüber dem veröffentlichten Stand geändert hat. Eine leere Regelliste ist dabei eine Aussage — sie heißt „alles zurückgenommen“ — und nicht dasselbe wie „keine Angabe“.
- **Die Adressen der Website werden für den Rahmen umgebogen.** Eine gebaute Website verweist auf ihre eigene Wurzel; im Rahmen ist die Wurzel das Dashboard. Umgeschrieben wird nur, was der Browser selbst lädt, samt `url(…)` in den ausgelieferten Stylesheets; Verweise in `<a>` bleiben unberührt, weil der Editor deren Klick selbst behandelt. Dazu gehören zwei Kopfzeilen: `X-Frame-Options: SAMEORIGIN` für diese eine Antwort und `frame-src 'self'` in der Richtlinie des Dashboards. Fehlt eines davon, bleibt der Rahmen leer — ohne Fehlermeldung.
- **Eine zentrale Angabe wird im Editor nie an einer Stelle überschrieben.** Klickt jemand die Telefonnummer auf der Seite an, benennt der Editor sie als zentral, sagt warum und führt zu ihrem Feld. Sie dort zu überschreiben würde sie an dieser einen Stelle ändern und im Impressum nicht. Erkannt wird sie auf **zwei** Wegen, und beide werden gebraucht:
    - über den **Text**, in beiden Schreibweisen — der des Vertrags und der, die tatsächlich in der Quelle steht. Nur die eine zu kennen hieße, die Stelle nicht wiederzuerkennen.
    - über **`seite.stellen`** aus dem Vertrag, eine Liste von CSS-Auswahlen. Nötig für alles, was als Text nichts Besonderes ist: Eine „6“ ist eine Sechs, die Zahl der Fahrlehrer im Team aber nur an ihrer Stelle.
- **Eine zentrale Angabe darf ausnahmsweise auf der Seite geändert werden — und wird trotzdem zentral gespeichert.** Sagt der Vertrag `seite.bearbeitbar: true`, erscheint an der Stelle ein Eingabefeld statt eines Verweises. Was dort eingetippt wird, geht über einen eigenen Weg (`POST /seite/zentral`) in das Overlay des Entwurfs — nicht in eine Darstellungsregel. Anschließend schreibt der Editor **alle** Stellen im Rahmen fort, an denen der Wert vorkommt. Genau das ist der Sinn der Ausnahme: Man ändert die Zahl dort, wo man sie sieht, und sieht dabei, dass sie überall mitgeht.
    Erlaubt ist das nur für einfache Werte — Text und ganze Zahl — und nur ohne Rechtswirkung. Eine Telefonnummer besteht aus Land und Ziffern und schreibt zwei Zeiger; Bürozeiten sind eine Tabelle aus sieben Tagen. Ein Eingabefeld am Rand der Seite bekäme davon nur einen Teil zu fassen. Die Grenze wird serverseitig gezogen, nicht in der Oberfläche: Eine Anfrage für ein nicht freigegebenes Feld wird abgewiesen, auch wenn sie von Hand gestellt wird.
- **Der Rahmen zeigt den Entwurf, nicht nur den Release.** Zentrale Werte, die im Entwurf anders sind als im aktiven Release, werden beim Öffnen im Rahmen fortgeschrieben — gleich ob sie im Formular oder auf der Seite geändert wurden. Sonst stünde im Editor bis zur nächsten Veröffentlichung der alte Wert, und zwar an jeder Stelle zugleich.
    Fortgeschrieben wird nur, was einen einzelnen Wert hat: Anzeige, Wählform, Anzahl. Bürozeiten und Theorieabende sind Tabellen und bleiben im Rahmen in der veröffentlichten Fassung stehen; ihre Bereiche werden dafür gesperrt, damit niemand sie für den aktuellen Stand hält.
    Geschrieben wird in das Element, das **nur** aus Text besteht. Ein Anruf-Verweis ist `<a><svg/><span>030 …</span></a>`; wer dort `textContent` setzt, hat die Nummer geschrieben und das Symbol daneben gelöscht. Gibt es kein eindeutiges Textelement, wird gar nichts geschrieben.
    Die Skripte der Website bekommen dabei den Vortritt und werden danach überschrieben: Ein Zähler, der eine Kennzahl beim Erscheinen hochlaufen lässt, liest sein Ziel beim Laden und schreibt am Ende den alten Wert zurück. Der Editor zieht deshalb innerhalb der ersten anderthalb Sekunden mehrfach nach — und danach nicht mehr. Ein Dauerbeobachter schriebe gegen jede Animation an, die eine Website je hat.

Ein Editor, der auf der Seite arbeitet, ist ausdrücklich **kein** Freibrief für freies Layout. Er verschiebt die Grenze nicht, an welchen Stellen der Owner etwas ändern darf, sondern nur den Ort, an dem er es tut.

### Der Entwurf ist eine Sache, kein Zustand

Alles Bearbeitete landet in **genau einem Entwurf je Website** — zentrale Angaben und Änderungen auf der Seite gemeinsam. Beide Teile stehen in getrennten Spalten (`overlay_json`, `layout_json`), beide jeweils als vollständiger Satz und nicht als Differenz, und beide werden über **eine** Schreibfunktion gepflegt: Wer nur einen Teil ändert, übergibt nur ihn; der andere bleibt stehen, statt lautlos leer zu werden.

Ein Entwurf ist der einzige Zustand des Dashboards, den man anlegt, ohne es zu wollen — zwei Tastendrücke im Formular genügen. Er muss deshalb dieselbe Sichtbarkeit und dieselbe Beiläufigkeit beim Loswerden haben:

- Er erscheint auf Übersicht, Bearbeiten und Veröffentlichen als **Karte**: was darin steht, wann er entstand, wer ihn bearbeitet hat.
- Er lässt sich an jeder dieser Stellen **weiterbearbeiten oder verwerfen**. „Verwerfen“ betrifft den ganzen Entwurf; eine Auswahl zwischen seinen Teilen hat niemand im Kopf, wenn er darauf drückt.
- Verworfen wird mit Rückfrage und mit Eintrag im Protokoll. Die veröffentlichte Website ist davon nicht betroffen; sie hat den Entwurf nie gesehen.
- Ein Entwurf ohne Inhalt wird gelöscht, nicht leer gespeichert. Sonst stünde überall „Du hast einen Entwurf“, obwohl nichts darin ist.

#### Verworfen heißt im Papierkorb, nicht weg

Verwerfen ist die eine Handlung im Dashboard, die auf einen Klick alles beseitigt. Gerade sie darf nicht die einzige ohne Weg zurück sein — aber der Weg zurück gehört dorthin, wo man ihn sucht, wenn man erschrocken ist.

Ein verworfener Entwurf geht deshalb in einen **Papierkorb**: genau einer je Website, mit Zeitpunkt, Person und Umfang. Unter „Veröffentlichen“ steht er oben auf der Seite als eigener Kasten — „Ein verworfener Entwurf liegt bereit“ — mit zwei Knöpfen: **zurückholen** oder **endgültig löschen**. Er steht dort auch dann, wenn längst wieder etwas Offenes da ist; gerade dann sucht man ihn. Zurückholen ersetzt in diesem Fall den angefangenen Entwurf, und die Rückfrage sagt das.

Er verschwindet beim Zurückholen, beim endgültigen Löschen und beim Veröffentlichen. Ein Papierkorb, der einen älteren Stand über eine gerade beschlossene Fassung legen könnte, wäre eine Falle statt einer Hilfe.

Früher war das Verwerfen ein Schritt im Rückgängig-Stapel — ein Pfeil, dessen Tooltip „Entwurf verworfen“ trug. Zwei Dinge waren daran falsch: Man musste den Tooltip lesen, um zu wissen, dass es die Rettung ist, und der Pfeil stand im Seiteneditor, während das Verwerfen von jeder Seite aus geht.

#### Zurücknehmen gehört zur Seite

**Zurück** und **wieder vor** stehen ausschließlich im Seiteneditor, zusammen mit **Vollbild**, über dem Rahmen. Über dem Formular der zentralen Angaben stehen sie nicht mehr und wirken dort auch nicht.

Der Grund ist die Art der Handlung. Auf der Seite macht man Bewegungen, die man hinterher nicht benennen kann: einen Satz umgeschrieben, eine Überschrift verschoben, ein Bild getauscht. Genau dafür gibt es das Zurücknehmen. Die zentralen Angaben sind ein Formular mit benannten Feldern und sichtbaren Werten — wer dort eine Bürozeit zurückstellen will, stellt sie zurück; ein Pfeil, der stattdessen „2 zentrale Angaben“ zurücknimmt, verlangt Vertrauen in etwas, das man nicht sieht.

Ein Schritt merkt sich außerdem, **worauf** er wirkt, und stellt auch nur das wieder her: die Darstellungsregeln der Seite (`layout`) oder genau ein Bildfeld (`bild:<feld>`). Vorher lag im Stapel der ganze Entwurf; wer auf der Seite einen Satz änderte und danach zentral die Telefonnummer, verlor beim Drücken die Telefonnummer gleich mit — im Stand von vorher stand sie schlicht noch nicht drin.

Was **keinen** Schritt erzeugt: eine Änderung im Formular der zentralen Angaben, eine zentrale Angabe von der Seite aus, das Zurückholen einer Vormerkung und das Verwerfen des Entwurfs. Nach dem Veröffentlichen enden beide Stapel; von dort führt der Verlauf zurück.

Eine **Vormerkung** wird dagegen nicht bearbeitet. Sie ist ein geprüfter, festgeschriebener Stand mit einem Termin; an ihr herumzuändern verbände die Prüfung von gestern mit dem Inhalt von heute. Statt dessen holt eine ausdrückliche Handlung ihre Werte **zurück in den Entwurf** und beendet sie. Danach ist die Reihenfolge wieder sichtbar: bearbeiten, prüfen, vormerken.

### Bilder

- Upload nur für freigegebene Bildfelder
- vor Auswahl klare Vorgaben zu Motiv, Format, Mindestauflösung, Seitenverhältnis und maximaler Dateigröße
- serverseitige Typ- und Inhaltsprüfung, sichere Dateinamen, Metadatenbereinigung, Größenvarianten und moderne Formate
- Zuschnittsvorschau für alle betroffenen Breakpoints, Alt-Text und Rückkehr zum vorherigen Bild
- Original und erzeugte Varianten gehören zur Release-Historie

#### Ein Bild ist eine Datei an einer Stelle, kein Wert in der Inhaltsdatei

Ein Bildfeld schreibt keinen Dateinamen, sondern ersetzt eine Datei an einem registrierten Pfad. Der Name in der Inhaltsdatei bleibt unverändert; in sie geht nur der Alternativtext.

Der Grund ist Bestandsschutz: Sobald der Owner Dateinamen beeinflusst, kann er jede Verlinkung im Projekt brechen — Vorschaubilder, Open-Graph-Angaben, CSS-Hintergründe, Manifest-Einträge. Diese Stellen kennt das Dashboard nicht und kann sie nicht mitziehen. Ein Pfad ist außerdem nichts, was ein Owner sehen oder entscheiden sollte.

#### Was hochgeladen wird, wird gelesen, nicht geglaubt

- Dateiendung und der vom Browser gemeldete Typ entscheiden nichts. Maßgeblich sind die ersten Bytes.
- Aus ihnen ergeben sich Format und Maße; geprüft wird gegen die Vorgabe des Feldes. Jede Meldung nennt den geforderten Wert, nicht nur das Scheitern.
- **Metadaten werden entfernt**: EXIF, XMP, IPTC, Kommentare. Ein Foto vom Handy trägt regelmäßig GPS-Koordinaten und Gerätekennung; wer ein Bild hochlädt, veröffentlicht sonst nebenbei, wo es aufgenommen wurde. Das ist der Regelfall, nicht die Ausnahme.
- Das Farbprofil bleibt erhalten. Ohne es verschieben sich die Farben sichtbar.
- Gespeichert wird nur die bereinigte Fassung. Das Original aufzubewahren wäre kein Vorteil, sondern genau die Koordinaten, die gerade entfernt wurden.

#### Assets sind unveränderlich

Ein neues Bild überschreibt kein altes; es entsteht daneben, mit eigener Kennung, und die Revision zeigt darauf. Nur so stellt ein Rollback den alten Stand vollständig her statt des alten Textes mit dem neuen Bild. Die Rückkehr zu einer früheren Fassung ist damit kein eigenes Feature, sondern eine Folge davon.

#### Eine Datei genügt, die übrigen Fassungen entstehen daraus

Braucht eine Stelle mehrere Formate — etwa PNG und WebP für ein `<picture>` —, lädt der Owner trotzdem **eine** Datei hoch. Der Feldvertrag beschreibt, **welche Dateien entstehen müssen**, nicht, wie viele hochgeladen werden.

Ein Bildumwandler ist deshalb eine Betriebsvoraussetzung wie eine Node-Version, keine Bequemlichkeit: Ohne ihn müsste ein Owner wissen, was WebP ist, und es selbst erzeugen. Auf `217.154.218.30` leistet das `libwebp`.

Gibt es keinen unmittelbaren Weg zwischen zwei Formaten, ist ein verlustfreier Umweg zulässig und dem Verzicht vorzuziehen — er verändert kein Bildpixel.

Ausdrücklich **nicht** zulässig bleibt die naheliegende Abkürzung, dieselbe Datei unter beiden Namen abzulegen. Ein PNG, das als `image/webp` angekündigt wird, ist eine Falschangabe; sie fällt irgendwann auf irgendeinem Gerät auf und ist dann schwer zu finden. Ebenso wenig zulässig ist, eine Ableitung wegzulassen und im Release einen Verweis ins Leere stehen zu lassen.

Vier Regeln für jedes Programm, das der Dienst zu diesem Zweck startet:

1. Aufruf mit **absolutem Pfad**, nie über `PATH`.
2. Kein Netzwerk, keine geerbte Umgebung, ein eigenes Arbeitsverzeichnis innerhalb der beschreibbaren Pfade des Dienstes.
3. Begrenzte Laufzeit und begrenzte Ausgabegröße; ein hängender Aufruf wird abgebrochen.
4. Das Ergebnis durchläuft **dieselbe Prüfung wie ein Upload von außen**. Ein Werkzeug kommt nicht durch, nur weil der Dienst es selbst gestartet hat.

Maße werden **vor** der Umwandlung am Original geprüft. Scheitert umgekehrt eine abgeleitete Fassung an einer Größengrenze, sagt die Meldung, dass die hochgeladene Datei in Ordnung war — der Owner hat dann nichts falsch gemacht und darf nicht nach einem Fehler bei sich suchen.

Fehlt der Umwandler, fällt die Oberfläche auf einen Upload je Fassung zurück und erklärt das. Ein stillschweigend halbierter Funktionsumfang wäre schlimmer als ein benannter.

### Verlauf und Rückgängig

Drei Wege zurück, mit verschiedener Reichweite und an verschiedenen Orten. Wer sie vermischt, bekommt einen Knopf, der mal einen Tastendruck und mal einen Arbeitstag zurücknimmt:

| Weg | Reichweite | Wo |
|---|---|---|
| Zurück / wieder vor | ein Schritt auf der Seite oder ein Bildfeld | Seiteneditor, über dem Rahmen |
| Papierkorb | der ganze verworfene Entwurf | Veröffentlichen, oben |
| Rollback | eine vollständige veröffentlichte Fassung | Verlauf |

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

Property, Konto, Berechtigung, echter API-Abruf und die davon getrennte Indexierbarkeit werden je Website im [[60-Operations/Release Readiness Register]] geführt. Ein erfolgreicher API-Test schließt einen offenen `noindex`- oder `robots.txt`-Befund nicht.

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
- Produktions-Endpunkt, realer Betreiberzugang, optionaler E-Mail-Versand und Ende-zu-Ende-Nachweis werden je Website im [[60-Operations/Release Readiness Register]] geführt. Sichtbare Übergangshinweise bleiben dort bis zu ihrer Entfernung oder bewussten Owner-Freigabe verortet.
- Der Betreiber hat einen belegten Weg, die Anfragen zu lesen und ihren Bearbeitungsstand zu setzen, auch ohne E-Mail.
- Ein Formular, das nur eine Erfolgsmeldung zeigt und nirgends ankommt, ist schlechter als kein Formular: Der Owner hält sein Anliegen für übermittelt und wartet.

### Eigene Inhalte mitnehmen

Der Owner kann jederzeit und ohne Rückfrage alles herunterladen, was zu seiner Website gespeichert ist: aktuell veröffentlichte Werte, jeden früheren Stand mit Zeitpunkt und Person, Bildmetadaten, Vormerkungen, Anfragen und das Zugriffsprotokoll.

- Der Export ist eine Selbstbedienung, kein Auskunftsverfahren. Er dient auch der Auskunftspflicht nach Art. 15 DSGVO, ist aber zuerst eine Frage der Anständigkeit: Es sind seine Inhalte.
- **Nicht enthalten sind Passwort-Hashes, Sitzungen und hinterlegte Zugangsdaten fremder Dienste.** Ein Export soll Inhalte herausgeben, nicht eine Datei erzeugen, mit der sich anderswo etwas übernehmen ließe.
- Das Format ist maschinenlesbar und selbsterklärend benannt, damit es ohne dieses Dashboard verwendbar bleibt.

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

## Datensicherung

Backups trennen Datenbank, Content-Revisionen, Assets, Releases und Schlüssel; ein Restore wird mandantenweise getestet. Verbindlich dabei:

- Eine laufende Datenbank wird **nicht kopiert**, sondern als in sich stimmige Momentaufnahme herausgeschrieben. Eine Dateikopie mitten in einer Transaktion ergibt einen Stand, den es nie gab, und bei WAL-Journalen fehlt zusätzlich der jüngste Teil.
- **Assets gehören dazu.** Ohne sie zeigt jeder wiederhergestellte Stand auf Bilder, die es nicht mehr gibt — ein Rollback wäre dann Text ohne Bild.
- **Releases gehören nicht dazu.** Sie sind aus Quelle und Revision reproduzierbar und machen den Löwenanteil des Platzes aus. Wiederhergestellt wird der Stand, nicht sein Bauergebnis.
- **Zugangsdaten fremder Dienste nur auf ausdrücklichen Wunsch** und nur auf ein Ziel mit denselben Rechten. Eine Sicherung, die unbemerkt fremde Schlüssel enthält, wandert sonst irgendwann auf ein Laufwerk mit schwächeren.
- Eine **halb geschriebene Sicherung wird gelöscht**, nicht liegengelassen. Sie sähe sonst aus wie eine.
- Eine Sicherung, die nie geöffnet wurde, ist eine Vermutung. Zur Sicherung gehört ein Prüflauf, der die Integrität bestätigt, die Zeilen der tragenden Tabellen zählt und die Zahl gesicherter Assetdateien gegen die Assets in der Datenbank hält.
- Der regelmäßige Lauf **prüft sich selbst und räumt erst danach auf**. Eine unbrauchbare neue Sicherung darf nicht dazu führen, dass die letzte brauchbare gelöscht wird.
- Ein verpasster Lauf wird beim nächsten Start **nachgeholt**. Sonst hätte ausgerechnet ein Ausfalltag keine Sicherung — der Tag, an dem man sie am ehesten braucht.

## Zustände, die auseinanderlaufen können

Wo zwei Stellen dasselbe wissen müssen, entsteht die unangenehmste Sorte Fehler: Beide sehen für sich richtig aus, nur zusammen ergeben sie eine Lüge. Verbindlich:

- **Zuerst die Stelle schreiben, die wirkt, dann die, die anzeigt.** Der Wartungsmodus etwa wird von nginx über eine Datei gelesen und im Dashboard aus der Datenbank angezeigt. In der falschen Reihenfolge meldet das Dashboard nach einem Schreibfehler einen Zustand, den die Website nicht hat.
- **Einen Zustand nicht doppelt führen.** Ob ein Bau gelang, steht im Job. Eine zweite Kopie davon in einer anderen Tabelle wird irgendwann falsch.
- **Formularfelder, die zusammengehören, über einen Index verbinden, nicht über die Reihenfolge.** Ohne JavaScript sendet ein Formular andere Felder als mit; eine Zuordnung über die Reihenfolge verschiebt dann Werte, ohne dass etwas nach einem Fehler aussieht.
- **Eine Sitzung verlängert sich beim Arbeiten.** Läuft sie mitten im Bearbeiten ab, meldet das Autosave nur noch Fehler und der Speichern-Knopf führt auf eine Fehlerseite — die Eingaben sind weg.
- **Keinen Verweis anbieten, dessen Ziel gelöscht sein kann.** Eine Vorschau, deren Release die Aufbewahrung entfernt hat, gehört nicht mehr angezeigt.

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
- Uploads gegen Typ, Größe, Inhalt und Pfadmanipulation geprüft; Metadaten nachweislich entfernt und das Ergebnis weiterhin ein gültiges Bild
- ein Upload geht beim gewöhnlichen Speichern des Formulars nicht verloren
- eine geplante Veröffentlichung überlebt einen Dienstneustart, blockiert keine andere Veröffentlichung und löst zur richtigen Ortszeit aus
- ein laufender Probebau verdeckt weder Fehlermeldungen noch offene Entscheidungen
- der Export enthält keine Zugangsdaten, Sitzungen oder fremden Schlüssel
- aus einer hochgeladenen Datei entstehen alle geforderten Fassungen, mit unveränderten Maßen und innerhalb ihrer Grenzen
- ein Neustart während der Ausführung einer Vormerkung führt zur Wiederholung, ein inhaltlicher Fehlschlag zu einer sichtbaren Meldung
- eine Sicherung lässt sich öffnen, ihre Integrität bestätigen und ihre Vollständigkeit gegen die Assets prüfen; ein verpasster Lauf wird nachgeholt
- eine Vormerkung, deren Host inzwischen einer anderen Website gehört, wird nicht ausgeführt
- jedes Formular liefert dieselben Werte mit und ohne JavaScript
- jede Erklärung hinter einem Erklärzeichen bleibt über `aria-describedby` mit ihrem Feld verbunden
- die Einführung beim ersten Besuch lässt sich abbrechen, wiederholen und übersteht fehlenden lokalen Speicher
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
