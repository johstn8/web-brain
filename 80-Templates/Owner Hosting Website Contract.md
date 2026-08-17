---
type: template
status: canonical
updated: 2026-08-17
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
            "pointer": "/business/phone",
            "label": "Telefonnummer",
            "type": "tel",
            "required": true,
            "max_length": 40,
            "help": "Mit Vorwahl, wie sie öffentlich erscheinen soll.",
            "example": "+49 30 123456",
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
    "phone": "+49 30 123456",
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
| stabiler Feldschlüssel und `pointer` | Berechtigung, Historie und Migration hängen daran |
| `label`, `help`, optional `example` | keine Builder-Fachsprache |
| `type` | aus dem zentral unterstützten Typkatalog |
| Validierungsgrenzen | passend zum Typ; keine nur clientseitige Grenze |
| `publish_policy` | `owner_confirm`, `scheduled` oder `builder_approval` |
| `responsible` | `owner`, `builder` oder benannte fachliche Rolle |
| `risk` | `low`, `medium` oder `high` |
| `privacy_ref` | ID im Dateninventar oder `null` |

Der Typkatalog umfasst mindestens `short_text`, `long_text`, `email`, `tel`, `url`, `integer`, `decimal`, `money`, `date`, `time`, `weekly-hours`, `select`, `multi_select`, `boolean`, `image`, `image_list` und validierte strukturierte Listen. Ein unbekannter Typ ist ein Registrierungsfehler, kein generisches Textfeld.

## Builder-Checkliste vor Registrierung

- [ ] Jede sichtbare Inhaltsgruppe besitzt eine stabile Block-ID.
- [ ] Für jeden Block ist `owner_editable` bewusst entschieden.
- [ ] Kein Rechtstext, Tracking-, Consent-, Rollen-, Navigations- oder Buildfeld ist frei editierbar.
- [ ] Jeder editierbare Pointer existiert in den Basiswerten und liegt innerhalb seines Blocks.
- [ ] Labels, Hilfen, Beispiele und Fehlergrenzen sind für einen Owner verständlich.
- [ ] Preview-Routen decken Desktop und Mobil ab.
- [ ] Lange Texte und Bilder wurden gegen reale Layoutgrenzen geprüft.
- [ ] Buildprofil und Ausgabeordner sind zentral freigegeben.
- [ ] Der Content-Loader verwendet lokal `content_file` und im Worker `OWNER_HOSTING_CONTENT_FILE`.
- [ ] Hosting-Variablen und `_hosting` gelangen nicht in Browserbundle, HTML oder Release-Metadaten.
- [ ] Smoke-Pfade sind echte statische Routen und enthalten Pflichtseiten.
- [ ] Capabilities stimmen mit Code, Dateninventar und aktivierten Adaptern überein.
- [ ] `PROJECT.md` dokumentiert Verantwortlichkeiten, Aufbewahrung, Rollback und offene Produktentscheidungen.

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
