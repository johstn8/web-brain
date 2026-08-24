---
type: template
status: canonical
updated: 2026-08-24
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

| `seite` | wo der Wert auf der gebauten Seite steht und ob er dort geändert werden darf; fehlend bedeutet „nirgends registriert, nicht auf der Seite änderbar“ |

Der Typkatalog umfasst mindestens `short_text`, `long_text`, `email`, `phone`, `url`, `integer`, `decimal`, `money`, `date`, `time`, `weekly-hours`, `abende`, `select`, `multi_select`, `boolean`, `image`, `image_list` und validierte strukturierte Listen. Ein unbekannter Typ ist ein Registrierungsfehler, kein generisches Textfeld.

### `seite` sagt, wo eine zentrale Angabe steht — und ob man sie dort anfassen darf

`surface` beantwortet, in welcher Ansicht ein Feld **gepflegt** wird. `seite` beantwortet etwas anderes: wo ein zentral gepflegter Wert auf der fertigen Website **erscheint**. Der Seiteneditor braucht das für drei Dinge — die Stelle als zentral zu erkennen, sie im Rahmen auf den Stand des Entwurfs zu bringen, und in den wenigen erlaubten Fällen ein Eingabefeld an ihr anzubieten.

```json
"teamGroesse": {
  "type": "integer",
  "surface": "zentral",
  "pointer": "/business/team_size",
  "label": "Fahrlehrer im Team",
  "min": 1,
  "max": 99,
  "seite": {
    "stellen": [{ "auswahl": ".hero__facts > div:nth-child(1) > dd", "form": "anzeige" }],
    "bearbeitbar": true
  }
}
```

- **`stellen[].auswahl`** ist eine CSS-Auswahl im gebauten Dokument. Sie wird gebraucht, wo der Text allein nicht trägt: Eine „6“ ist als Zeichenkette nichts Besonderes, als Zahl der Fahrlehrer im Team aber sehr wohl. Für Telefonnummern und Adressen genügt weiterhin der Textabgleich; ein Vertrag, der jede Stelle aufzählen müsste, wäre beim nächsten Absatz unvollständig.
- **`stellen[].form`** sagt, in welcher Schreibweise der Wert dort steht: `anzeige` (lesbar), `tel` (Wählform, auch im `href`) oder `anzahl` (Länge einer Liste). **Fehlt `form`**, ist die Stelle ein Bereich, der zu dem Feld gehört, aber nicht aus einem einzelnen Wert besteht — die Bürozeitentabelle etwa. Sie wird gesperrt und nicht fortgeschrieben.
- **`bearbeitbar`** ist ausdrücklich `false`, solange es nicht dasteht. Es auf `true` zu setzen heißt: Der Owner darf den Wert an der Stelle eintippen, an der er ihn sieht — gespeichert wird er trotzdem zentral, und alle Stellen werden zugleich fortgeschrieben. Erlaubt nur für `short_text` und `integer` und nur ohne Rechtswirkung. Eine Telefonnummer besteht aus Land und Ziffern und schreibt zwei Zeiger; ein Eingabefeld am Rand der Seite bekäme davon nur einen Teil zu fassen.
- **`grund`** ist der Satz, den der Owner beim Anklicken liest, wenn `bearbeitbar` fehlt. Er nennt die Stellen, an denen der Wert sonst noch steht — „auch im Impressum“ ist die Auskunft, die eine Sperre erklärt. Fehlt er, setzt das Dashboard einen allgemeinen Satz ein; für Felder mit `legalImpact` ist ein eigener Pflicht.

### Der Typ `abende`: wiederkehrende Termine, eine Zeit

Für Termine, die an mehreren Wochentagen zur selben Zeit stattfinden — Theorieabende, Sprechstunden, Kurse. In der Inhaltsdatei steht eine Liste aus Tag, Kurzform und Zeitspanne; im Formular werden die Tage angekreuzt und die Zeit **einmal** eingetragen.

```json
"theorieAbende": {
  "type": "abende",
  "surface": "zentral",
  "pointer": "/theorie/termine",
  "label": "Abende des Theorieunterrichts",
  "max": 7
}
```

Nicht `weekly-hours` nehmen: Öffnungszeiten haben je Tag eine eigene Spanne und kennen „geschlossen“. Mit ihnen müsste der Owner dieselbe Uhrzeit dreimal eintippen — und beim vierten Abend wäre sie einmal anders.

**Die Anzahl wird nie als eigenes Feld geführt.** Steht auf der Website „drei Abende pro Woche“, ist diese Zahl die Länge der Liste und wird über eine Stelle mit `"form": "anzahl"` daran gebunden. Ein zweites Feld dafür ist genau die Stelle, an der Zahl und Liste auseinanderlaufen.

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

### Was nie freigegeben wird, steht nicht im Vertrag

Ein Vertrag zählt auf, was der Owner ändern darf. Unabhängig davon gilt für **jede** gehostete Website eine Sperrliste, die im Owner-Hosting als Code liegt (`packages/core/sperren.mjs`) und die kein Vertrag aufheben kann:

Kopfzeile, Navigation und Menü, die Seitenliste der Fußzeile, `address`, Anruf- und Mailverweise, die Namen von Impressum, Datenschutz, AGB und Widerruf sowie Angaben für Suchmaschinen und Technik.

Zwei davon sind eigene Entscheidungen und keine bloße Vorsicht:

- **Kopfzeilen werden nicht bearbeitet.** Was dort steht, steht auf jeder Seite. Wer den Menüpunkt „Kontakt“ antippt, ändert ihn in der Kopfzeile, im Menü, in der Fußzeile und in der Sprungmarke für Bildschirmleser — sichtbar ist nur die eine Stelle. Eine Änderung, deren Umfang man nicht sehen kann, gehört nicht in ein Feld.
- **Impressum und Datenschutz werden nicht umbenannt.** Eine Seite, die nicht so heißt, ist für ihre Pflicht nicht auffindbar. Das ist kein Textwunsch, sondern ein Rechtsverlust.

Ein Vertrag darf die Liste über `gesperrt: [{ auswahl, grund }]` **ergänzen** — für das, was an dieser Website besonders ist: die Rechtszeile der Fußzeile mit Firmenname und Inhaber, die Beschriftungen von Kennzahlen, das Logo.

### Das Logo wird nicht ersetzt, Fahrzeugbilder schon

Ein Bild ist im Seiteneditor nur austauschbar, wenn der Vertrag es als Bildfeld nennt. **Das Logo gehört ausdrücklich nicht dazu.** Es erscheint an vier bis fünf Stellen — Kopfzeile, Menü, Fußzeile, Favicon, Vorschaubild für soziale Netzwerke —, von denen der Editor nur eine kennt. Eines davon zu tauschen hieße, es an den übrigen nicht getauscht zu haben. Das ist gewollt und keine Lücke: Ein Logowechsel ist ein Builder-Auftrag.

Ein Fahrzeugbild ist der Gegenfall. Es steht an ein bis zwei Stellen, beide gehören zu demselben Feld, und beide werden vom Buildadapter gemeinsam ersetzt. Dafür ist der Upload da.

Die Faustregel steht damit fest: **Hochladen darf der Owner ein Bild, das ein bis zwei Stellen hat und keine Marke ist.** Alles, was an mehr Stellen erscheint oder die Identität der Website trägt, wird registriert, aber gesperrt — und der Vertrag nennt es unter `gesperrt`, damit ein Klick darauf die Begründung zeigt statt gar nichts.

### Der Copyright-Hinweis steht immer

Jede gehostete Website zeigt in der Fußzeile einen Copyright-Hinweis, **auch wenn das Zeichen „©“ in der Vorlage fehlt**. Fehlt es, wird es ergänzt; ist es in der verwendeten Schrift nicht darstellbar, tritt „(c)“ an seine Stelle, nicht eine Lücke. Der Hinweis nennt Jahr und Betreiber und steht neben Impressum und Datenschutz.

Er ist kein Gestaltungselement, sondern Teil der Rechtszeile — und damit gesperrt. Beim Anlegen einer Website ist er Teil der Abnahme: Eine Fußzeile ohne ihn gilt als unvollständig, nicht als schlicht.

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
- [ ] Für jedes zentrale Feld, das auf der Website sichtbar ist, sind `seite.stellen` eingetragen — mit `form`, wo es ein einzelner Wert ist, und ohne, wo es ein Bereich ist.
- [ ] `seite.bearbeitbar: true` steht nur bei einfachen Werten ohne Rechtswirkung, und für jedes gesperrte zentrale Feld gibt es einen `grund`, der die anderen Stellen nennt.
- [ ] Eine Anzahl, die auf der Website steht, ist an ihre Liste gebunden (`"form": "anzahl"`) und nicht als zweites Feld geführt.
- [ ] Kopfzeile, Navigation und die Namen von Impressum und Datenschutz sind nirgends als editierbares Feld registriert.
- [ ] Das Logo ist kein Bildfeld; es steht unter `gesperrt` mit Begründung.
- [ ] Die Fußzeile zeigt einen Copyright-Hinweis, und er liegt in einem gesperrten Bereich.
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
