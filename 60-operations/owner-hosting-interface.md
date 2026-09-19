---
type: canonical
status: canonical
updated: 2026-09-19
depends_on:
  - "[[30-frontend/stack.md]]"
  - "[[60-operations/delivery-and-local-start.md]]"
impacts:
  - "[[80-templates/owner-hosting-website-contract.md]]"
  - project-master-spec
  - content-schema
---

# Owner Hosting: Schnittstelle

Diese Notiz beantwortet genau eine Frage: **Was muss ein Website-Build liefern, damit das Owner-Dashboard ihn aufnehmen kann?**

Das Owner-Hosting selbst ist ein eigenes Produkt mit eigenem Repository. Seine Spezifikation — Tenant-Plan, Contract-Lint, Feldvertrag, Preview, Publish, Rollback, Datenmodell, Dashboardbereiche — steht dort unter `docs/hosting-and-dashboard.md` und nicht mehr im Brain. Sie ist Produktwissen, kein übertragbares Web-Wissen.

## Die vier Lieferpflichten

### 1. Eine Inhaltsdatei: `content/<website>.json`

Der gesamte owner-bearbeitbare Inhalt liegt in genau einer JSON-Datei. Keine Inhalte in Komponenten, keine zweite Quelle, kein verstreutes Frontmatter. Diese Datei ist die Projekt-Basis; das Dashboard legt ein Owner-Overlay darüber und schreibt nie in die Datei selbst.

### 2. Stabile Pointer

Jedes editierbare Feld ist über einen JSON-Pointer erreichbar, der sich nicht ändert, wenn Text, Reihenfolge oder Gestaltung sich ändern. Ein Pointer wird nicht umbenannt, sondern migriert; die Migration ist Teil derselben Änderung. Ein umbenannter Pointer ohne Migration löscht stillschweigend den Wert, den der Owner eingetragen hat.

### 3. Feldtypen und Grenzen

Je Block und Feld wird bei Erstellung **und bei jedem Update** entschieden und im Vertrag festgehalten:

| Angabe | Bedeutung |
|---|---|
| `owner_editable` | ob der Owner das Feld ohne Builder ändern darf |
| Pointer | stabiler JSON-Pointer auf den Wert |
| Feldtyp | bestimmt Control im Dashboard und Servervalidierung, etwa `text`, `money`, `weekly-hours`, `phone`, `image` |
| Grenzen | Länge, Bereich, erlaubte Formate, Pflicht oder optional |
| Label und Hilfe | damit die Oberfläche ohne Rückfrage verständlich ist |
| Veröffentlichungspolicy | direkt, mit Bestätigung oder nur mit Builder-Freigabe |

Die Form dieses Vertrags steht in [[80-templates/owner-hosting-website-contract.md]].

### 4. Preview-Route

Je Block ist benannt, welche statische Route ihn zeigt. Ohne Preview-Route kann der Owner seine Änderung vor der Veröffentlichung nicht sehen, und der Publish wird zu einem Blindflug.

## Build-Schnittstelle

Die Website liest ihren Content beim Build aus genau einer austauschbaren Quelle. Lokal ist das `content/<website>.json`, im Hosting-Build setzt der Worker `OWNER_HOSTING_CONTENT_FILE` auf eine validierte, aufgelöste Datei:

```text
wenn OWNER_HOSTING_CONTENT_FILE gesetzt:
  validierte Datei aus dem isolierten Build lesen
sonst:
  content/<website>.json lesen
```

Mehr braucht die Website nicht. Kein Dashboard-SDK im Browser, keine API-URL, keine Laufzeitabfrage, keine Datenbank. Der Build bleibt statisch nach [[30-frontend/stack.md]]. Fehlt dieser Content-Loader, schlägt die Registrierung im Dashboard fehl, und die Website wird nicht als scheinbar editierbar aktiviert.

## Wann das gilt

Nur wenn zentrales Owner-Hosting Teil des Auftrags ist. Ist es das nicht, entfallen Vertrag und Pointer-Disziplin; die Inhaltsdatei nach Punkt 1 bleibt trotzdem die bessere Form, weil sie eine spätere Anbindung ohne Umbau möglich macht.

## Nicht hier

Konten, Rollen, Sessions, Tokens, Serverpfade, Release-IDs, Deployment-Slots, Rollback, Wartungsmodus, Datensicherung und die Dashboard-Oberfläche selbst. Das alles gehört dem Owner-Hosting-Repository.
