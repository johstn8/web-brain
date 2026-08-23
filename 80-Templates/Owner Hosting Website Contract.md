---
type: template
status: canonical
updated: 2026-08-23
depends_on:
  - "[[60-Operations/Owner Hosting and Dashboard]]"
impacts:
  - project-master-spec
  - content-schema
  - deployment
  - data-processing-inventory
---

# Owner Hosting Website Contract

Diese Vorlage ist je gehosteter Website auszufüllen. Sie beschreibt die Daten, die das zentrale Owner-Hosting für Formulare, Validierung, Vorschau und statische Builds benötigt. Sie erzeugt keine Dashboard-Kopie im Kundenprojekt.

## Pflichtdateien

```text
<Projektwurzel>/
  content/<website>.json
  owner-hosting/tenant.json
  PROJECT.md
  DATA-PROCESSING-INVENTORY.md
```

Die Projektdatei enthält Basiswerte und den `_hosting`-Vertrag. `tenant.json` enthält nur portable, nicht geheime Integrationsdaten. Absolute Pfade, `tenant_id`, Konten, Rollen, Tokens und Release-Zustände entstehen erst in der zentralen Registry.

## tenant.json

```json
{
  "contract_version": 1,
  "tenant_slug": "<dauerhafter-kebab-slug>",
  "public_host": "example.de",
  "dashboard_host": "hosting.example.de",
  "content_file": "content/example.json",
  "build_profile": "static-site-v1",
  "output_dir": "dist",
  "preview_routes": ["/", "/leistungen", "/kontakt"],
  "smoke_paths": ["/", "/impressum", "/datenschutz"],
  "release_retention": 10,
  "capabilities": {
    "contact_messages": false,
    "search_console": false,
    "builder_requests": true,
    "appointment_requests": "suggestions",
    "image_uploads": true,
    "maintenance_mode": true
  }
}
```

### Regeln für das Manifest

- `tenant_slug` bleibt nach der ersten Registrierung unverändert. Marken- oder Domainwechsel ändern nicht die technische Identität.
- `public_host` und `dashboard_host` sind reine Hostnamen ohne Schema, Port, Pfad oder Wildcard.
- `content_file` und `output_dir` sind relative, normalisierte Pfade innerhalb des Projektroots; `..`, Symlinks aus dem Root und absolute Pfade sind unzulässig.
- `build_profile` verweist auf einen serverseitig registrierten Adapter. Das Manifest führt keine Shellbefehle.
- `preview_routes` enthält repräsentative Routen für Inhaltsprüfung; `smoke_paths` enthält mindestens Startseite, Impressum und Datenschutz.
- `release_retention` ist eine Projektentscheidung innerhalb der zentral gesetzten Mindest- und Höchstgrenzen.
- Eine Capability ist nur fachliche Absicht. Sie wird erst aktiv, wenn Registry, Berechtigung, Dateninventar, Anbieter und Tests vollständig sind.

## Build-Integration im Website-Projekt

Der Content-Loader der Website muss beim lokalen Build `content_file` aus `tenant.json` verwenden und beim zentralen Preview-/Release-Build auf `OWNER_HOSTING_CONTENT_FILE` umschalten. Diese Variable zeigt auf die vom Worker validierte Kombination aus Projekt-Basis und Owner-Overlay. Sie ist nur zur Buildzeit vorhanden und darf weder in Browsercode noch in statische Metadaten gelangen.

Wenn `image_uploads` aktiv ist, stellt das freigegebene Buildprofil zusätzlich `OWNER_HOSTING_ASSET_DIR` bereit. `OWNER_HOSTING_RELEASE_ID` darf für Diagnose und Buildprotokoll genutzt werden. Das Projekt liest nie direkt aus PostgreSQL, `/var/lib/owner-hosting/`, einer Dashboard-API oder einem laufenden Owner-Entwurf.

Preview und Veröffentlichung müssen denselben Content-Loader und dieselbe Komponentenlogik verwenden. Ein Projekt gilt nicht als angebunden, wenn sein normaler Build weiterhin fest nur die eingecheckte Basisdatei liest und Owner-Änderungen deshalb ignorieren würde.

## Inhaltsdatei mit Editorvertrag

```json
{
  "_hosting": {
    "contract_version": 1,
    "schema_version": "<YYYY-MM-DD.N>",
    "blocks": {
      "business_details": {
        "pointer": "/business",
        "label": "Betriebsdaten",
        "description": "Kontaktdaten, die auf der Website erscheinen.",
        "owner_editable": true,
        "preview_routes": ["/", "/kontakt"],
        "fields": {
          "phone": {
            "pointers": {
              "anzeige": "/business/phone/display",
              "tel": "/business/phone/dial"
            },
            "label": "Telefonnummer",
            "type": "phone",
            "required": true,
            "help": "Nur die Ziffern ohne führende Null.",
            "example": "30 123456",
            "publish_policy": "owner_confirm",
            "responsible": "owner",
            "risk": "medium",
            "privacy_ref": null
          },
          "email": {
            "pointer": "/business/email",
            "label": "E-Mail-Adresse",
            "type": "email",
            "required": true,
            "max_length": 160,
            "publish_policy": "owner_confirm",
            "responsible": "owner",
            "risk": "medium",
            "privacy_ref": "contact-address"
          }
        }
      },
      "opening_hours": {
        "pointer": "/opening_hours",
        "label": "Öffnungszeiten",
        "owner_editable": true,
        "preview_routes": ["/", "/kontakt"],
        "fields": {
          "weekly": {
            "pointer": "/opening_hours/weekly",
            "label": "Reguläre Zeiten",
            "type": "weekly-hours",
            "required": true,
            "timezone": "Europe/Berlin",
            "publish_policy": "owner_confirm",
            "responsible": "owner",
            "risk": "low",
            "privacy_ref": null
          }
        }
      },
      "job_offer": {
        "pointer": "/job_offer",
        "label": "Stellenangebot",
        "owner_editable": true,
        "preview_routes": ["/karriere"],
        "fields": {
          "enabled": {
            "pointer": "/job_offer/enabled",
            "label": "Stellenangebot anzeigen",
            "type": "boolean",
            "required": true,
            "publish_policy": "owner_confirm",
            "responsible": "owner",
            "risk": "low",
            "privacy_ref": null
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
  "business": {
    "phone": { "display": "030 123456", "dial": "+4930123456" },
    "email": "kontakt@example.de"
  },
  "opening_hours": {
    "weekly": []
  },
  "job_offer": {
    "enabled": false
  },
  "legal": {
    "imprint": "<prüfpflichtiger Entwurf>",
    "privacy": "<prüfpflichtiger Entwurf>"
  }
}
```

## Pflichtattribute je Block

| Attribut | Regel |
|---|---|
| stabile Block-ID | ändert sich nicht nur wegen einer neuen Beschriftung |
| `pointer` | eindeutiger absoluter JSON-Pointer in derselben Inhaltsdatei |
| `label` | verständliche Bezeichnung im Dashboard |
| `owner_editable` | explizit `true` oder `false`; fehlend bedeutet `false` |
| `preview_routes` | jede sichtbare Route, auf der der Block wirkt |
| `fields` | nur bei editierbaren strukturierten Blöcken |
| `change_path` | für gesperrte, aber anfragbare Bereiche |

## Pflichtattribute je editierbarem Feld

| Attribut | Regel |
|---|---|
| stabiler Feldschlüssel und `pointer` beziehungsweise `pointers` | Berechtigung, Historie und Migration hängen daran |
| `label`, `help`, optional `example` | keine Builder-Fachsprache |
| `type` | aus dem zentral unterstützten Typkatalog |
| Validierungsgrenzen | passend zum Typ; keine nur clientseitige Grenze |
| `surface` | `zentral` oder `seite`; fehlend bedeutet `zentral` |
| `publish_policy` | `owner_confirm`, `scheduled` oder `builder_approval` |
| `responsible` | `owner`, `builder` oder benannte fachliche Rolle |
| `risk` | `low`, `medium` oder `high` |
| `privacy_ref` | ID im Dateninventar oder `null` |

Der Typkatalog umfasst mindestens `short_text`, `long_text`, `email`, `phone`, `url`, `integer`, `decimal`, `money`, `date`, `time`, `weekly-hours`, `select`, `multi_select`, `boolean`, `image`, `image_list` und validierte strukturierte Listen. Ein unbekannter Typ ist ein Registrierungsfehler, kein generisches Textfeld.

### Der Typ phone schreibt zwei Pointer

Eine Telefonnummer steht in der Inhaltsdatei zweimal: als Text für die Anzeige und in E.164-Form für den `tel:`-Link. Sie bleibt trotzdem **ein** Feld. Der Typ `phone` deklariert deshalb `pointers` statt `pointer`:

```json
"phone": {
  "type": "phone",
  "pointers": { "anzeige": "/business/phone/display", "tel": "/business/phone/dial" },
  "label": "Telefonnummer",
  "help": "Nur die Ziffern ohne führende Null.",
  "required": true,
  "publish_policy": "owner_confirm",
  "responsible": "owner",
  "risk": "medium"
}
```

Der Owner wählt links das Land und tippt rechts die nationale Nummer ohne führende Null; Trennzeichen setzt das Feld. Beide Pointer werden daraus gemeinsam geschrieben. Beide Zielpointer müssen in den Basiswerten existieren.

Ein einfaches Textfeld `tel` ist für neue Verträge nicht mehr zulässig. Begründung und Regeln in [[60-Operations/Owner Hosting and Dashboard#Eine Angabe ist ein Feld]].

### `surface` sagt, wo ein Feld bearbeitet wird

Jedes editierbare Feld trägt zusätzlich, **wo** der Owner es ändert:

- `zentral` — im Formular „Zentrale Angaben“. Zu wählen, wenn der Wert an mehreren Stellen der Website erscheint: Telefon, E-Mail, Öffnungszeiten, Schalter wie „Stellenangebot anzeigen“.
- `seite` — im Seiteneditor, dort wo der Wert steht. Zu wählen, wenn er an genau einer Stelle erscheint: einzelne Bilder, Texte einer bestimmten Seite.

Die Entscheidung ist Teil des Vertrags und nicht der Oberfläche überlassen. Ein Feld erscheint in genau einer der beiden Ansichten; zwei Wege zu derselben Änderung zwingen den Owner zu einer Wahl, deren Unterschied er nicht kennen kann.

Ein Bildfeld ist im Regelfall `seite`. Es beschreibt keine Angabe über den Betrieb, sondern eine Stelle — und stand im gemeinsamen Formular weit weg von dem Ort, an dem man es sieht. An seiner Registrierung ändert das nichts: Pfade, `spec`, Assets, Historie und Rollback bleiben unverändert.

### Änderungen auf der Seite sind kein Vertragsfeld

Was der Owner unmittelbar auf der Seite ändert — dieser Satz, diese Ausrichtung —, wird **nicht** als Vertragsfeld nachgetragen. Die Quelle kennt diesen Satz nicht als Feld, sondern nur als Text im Markup; ein Feld dafür wäre eine Erfindung.

Solche Änderungen sind **Darstellungsregeln**: Seite, Anker im Dokument, optionaler Text, aufgezählte Gestaltung. Sie stehen in einer eigenen Spalte neben dem Overlay, werden nach dem Bau auf das Release angewendet und sind in [[60-Operations/Owner Hosting and Dashboard#Der Seiteneditor]] verbindlich geregelt. Für die Vertragsvorlage folgt daraus nur eines: Ein Vertrag muss dafür **nichts** vorsehen, und es ist kein Grund, ein Feld zu erfinden.

### Der Typ image beschreibt Dateien, keinen Dateinamen

Ein Bildfeld ersetzt eine Datei an einem registrierten Pfad. Der Dateiname in der Inhaltsdatei bleibt unverändert, damit keine Verlinkung im Projekt bricht; in die Inhaltsdatei geht nur der Alternativtext:

```json
"fleet_photo": {
  "type": "image",
  "pointers": { "alt": "/fleet/0/alt" },
  "files": {
    "png":  { "path": "content/assets/wagen.png",  "label": "PNG",
              "spec": { "type": "png",  "width": 1100, "minHeight": 440, "maxHeight": 500, "maxBytes": 921600 } },
    "webp": { "path": "content/assets/wagen.webp", "label": "WebP",
              "spec": { "type": "webp", "width": 1100, "minHeight": 440, "maxHeight": 500, "maxBytes": 256000 } }
  },
  "label": "Fahrzeugbild",
  "help": "Seitenansicht auf freigestelltem Hintergrund.",
  "publish_policy": "owner_confirm",
  "responsible": "owner",
  "risk": "low"
}
```

- Jeder Pfad unter `files` muss in der Quelle bereits existieren. Ein Vertrag darf ein Bild ersetzen, aber keines erfinden, das die Website gar nicht einbindet.
- `spec` ist verbindlich und wird serverseitig gegen die tatsächlichen Bilddaten geprüft, nicht gegen Endung oder gemeldeten Typ.
- Sind mehrere Formate nötig, genügt **eine** hochgeladene Datei; die übrigen entstehen serverseitig. Dieselbe Datei unter zwei Namen abzulegen ist ausgeschlossen. Begründung in [[60-Operations/Owner Hosting and Dashboard#Eine Datei genügt, die übrigen Fassungen entstehen daraus]].
- Der Alternativtext ist Pflicht. Ein Bild ohne ihn ist ein Fehler, keine Geschmacksfrage.

## Builder-Checkliste vor Registrierung

- [ ] Jede sichtbare Inhaltsgruppe besitzt eine stabile Block-ID.
- [ ] Für jeden Block ist `owner_editable` bewusst entschieden.
- [ ] Für jedes editierbare Feld ist `surface` bewusst entschieden: zentral bei Werten an mehreren Stellen, `seite` bei Werten an genau einer.
- [ ] Kein Feld erscheint in beiden Bearbeitungsansichten.
- [ ] Kein Rechtstext, Tracking-, Consent-, Rollen-, Navigations- oder Buildfeld ist frei editierbar.
- [ ] Jeder editierbare Pointer existiert in den Basiswerten und liegt innerhalb seines Blocks.
- [ ] Angaben, die in mehreren Formen in der Datei stehen, bilden ein Feld mit mehreren Pointern, nicht mehrere Felder.
- [ ] Jedes Bildfeld nennt alle Dateien, die entstehen müssen, samt Maßen, Format und Größengrenze; alle Zielpfade existieren in der Quelle.
- [ ] Labels, Hilfen, Beispiele und Fehlergrenzen sind für einen Owner verständlich.
- [ ] Preview-Routen decken Desktop und Mobil ab.
- [ ] Lange Texte und Bilder wurden gegen reale Layoutgrenzen geprüft.
- [ ] Buildprofil und Ausgabeordner sind zentral freigegeben.
- [ ] Der Content-Loader verwendet lokal `content_file` und im Worker `OWNER_HOSTING_CONTENT_FILE`.
- [ ] Hosting-Variablen und `_hosting` gelangen nicht in Browserbundle, HTML oder Release-Metadaten.
- [ ] Smoke-Pfade sind echte statische Routen und enthalten Pflichtseiten.
- [ ] Capabilities stimmen mit Code, Dateninventar und aktivierten Adaptern überein.
- [ ] `PROJECT.md` dokumentiert Verantwortlichkeiten, Aufbewahrung, Rollback und offene Produktentscheidungen.

## Legacy-Bridge-Vertrag als Ausnahme

Der reguläre Weg oben gilt für alle neuen Websites: Sie bringen `content/<website>.json` und `owner-hosting/tenant.json` selbst mit, und ihr Content-Loader akzeptiert `OWNER_HOSTING_CONTENT_FILE`.

Für **unveränderliche Altprojekte** gibt es eine eng begrenzte Ausnahme. Ein Altprojekt kennt das Owner-Hosting nicht, liest seine Inhaltsdatei über einen festen Pfad und darf nicht geändert werden. Der Vertrag wird dann **von außen** beschrieben und liegt zentral im Owner-Hosting-Bestand statt im Projekt:

- Der Vertrag ist Code in `packages/contracts/`, keine Daten in der Datenbank. Er kann deshalb nicht über das Dashboard erweitert werden.
- Er listet jeden bearbeitbaren Pointer mit Typ, Grenzen, Hilfetext und den betroffenen Stellen der Website auf. Was nicht aufgeführt ist, existiert für den Eigentümer nicht.
- Jeder Pointer muss in der Quelldatei bereits existieren. Overlays legen keine neuen Ebenen an; ein Vertrag kann keine Felder erfinden, die die Website gar nicht rendert.
- Pointer mit `legalImpact` erscheinen auch in Impressum oder Datenschutzerklärung. Für sie verlangt das Dashboard vor dem Veröffentlichen eine sichtbare, ausdrücklich bestätigte Rechtsprüfung. Alternativ bleibt das Feld im ersten Pilot gesperrt.
- Gebaut wird über einen Legacy-Buildadapter nach [[60-Operations/Owner Hosting and Dashboard#Legacy-Adapter für unveränderliche Altprojekte]]: isolierte Kopie, gepinnter Quellhash, kein Schreiben in die Quelle.

Ein Legacy-Vertrag beginnt bewusst klein. Für den ersten vertikalen Schnitt genügen Kontaktwege, strukturierte Öffnungszeiten und ein Schalter. Rechtstexte, Navigation, Routen, Preise, Tracking und Buildkonfiguration bleiben gesperrt.

Die Ausnahme wird nicht ausgeweitet. Sobald ein Altprojekt ohnehin überarbeitet wird, erhält es den regulären Vertrag.

## Vertragssynchronisierung bei Website-Updates

Im `PROJECT.md` wird je Synchronisierung protokolliert:

- bisherige und neue `schema_version`
- Hash der Projekt-Basis
- unveränderte Owner-Pointer
- neue Owner-Pointer mit Startwert
- Umbenennungen samt expliziter Migration
- entfernte beziehungsweise gesperrte Pointer
- Typ-/Grenzänderungen und Ergebnis der Prüfung vorhandener Werte
- betroffene Preview-Routen und Smoke-Pfade
- Kandidatenrelease, Testergebnis und Aktivierungszeitpunkt
- Behandlung offener Entwürfe der alten Vertragsversion

Ein Update ist unvollständig, solange der Plan nicht beweist, dass veröffentlichte Owner-Werte entweder erhalten, explizit migriert oder mit dokumentierter Entscheidung archiviert werden.
