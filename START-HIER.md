# Eine Website bauen: Anleitung für den Menschen

Alle anderen Dateien in diesem Repository sind für den Agenten geschrieben.
Diese hier ist für dich.

---

## Einmal einrichten

Drei Dinge, danach nie wieder:

1. **Claude Code auf `/srv/Web-Design` öffnen**, nicht auf `web-brain/`.
   Von dort aus sieht der Agent alle drei Repositories. `/srv/Web-Design/CLAUDE.md`
   lädt die Regeln automatisch mit.
2. **Skill verfügbar machen.** Auf dem Server ist er bereits nach
   `~/.claude/skills/web-build` verlinkt. Auf einem weiteren Rechner:
   ```
   /plugin marketplace add johstn8/web-brain
   /plugin install web-build@johstn8
   ```
3. **Prüfen, dass es greift.** Frag in einer neuen Sitzung:
   *„Welche Bahn gilt für eine Bäckerei-Website und welches Preset würdest du nehmen?"*
   Kommt eine Antwort mit `Fast Lane` und einem Presetnamen, sitzt alles.

---

## Was der Agent schon hat

Das musst du **nicht** mitliefern:

| Er hat | Bedeutet |
|---|---|
| das ganze Regelwerk | Copy-Regeln, Anti-Slop-Katalog, Auftakt-Repertoire, Zustandsmatrix, Rechtsseiten-Logik, Quality Gates |
| `web-kit` | Blöcke, Tokenvertrag, fünf Art-Direction-Presets, Rechtsseiten, Consent, QA-Skripte, lauffähiger Astro-Starter |
| über 150 belegte Referenzseiten | nach Gewerk sortiert in `90-references/website-reference-pool.md` |
| einen Browser | er rendert den Build selbst und sieht ihn sich an, bei 375 und 1280 Pixel |
| Netz | er kann deine alte Website ziehen und recherchieren |
| Erinnerung | frühere Projekte und deine Vorlieben |

Du musst ihm also **nichts** über Design, Barrierefreiheit, SEO, DSGVO oder
den Aufbau einer Landing Page erklären. Das steht alles schon drin.

---

## Was du mitbringen musst

Nur das, was er nicht wissen kann. Je mehr davon echt ist, desto weniger
erfindet er.

**Pflicht — ohne das geht es nicht:**

- **Wer ist der Betrieb?** Name, Gewerk, Ort.
- **Was bietet er an?** Die realen Leistungen, nicht die Kategorie.
- **Wie erreicht man ihn?** Telefon, E-Mail, Anschrift.
- **Gibt es eine alte Website?** Die URL. Er zieht sie selbst.

**Stark empfohlen — sonst rät er:**

- **Öffnungszeiten** und ob es Abweichungen gibt.
- **Preise**, falls sie auf die Seite sollen.
- **Logo und Fotos**, als Dateien oder als Ordnerpfad. Ein gefundenes Logo
  wird immer eingesetzt, auch ein schlechtes.
- **Für wen ist die Seite?** Wer ruft an, und warum?
- **Was soll passieren?** Anruf, Formular, Terminbuchung, Besuch.
- **Was ist an dem Betrieb besonders?** Ein Satz reicht. Das ist die Stelle,
  an der eine Website aufhört, austauschbar zu sein.

**Optional, wenn du eine Meinung hast:**

- Art Direction: `werkstatt`, `praxis`, `tisch`, `kanzlei` oder `atelier`.
  Sagst du nichts, schlägt er eine vor und begründet sie.
- Eine Seite, die dir gefällt. Dann prägt sie die Fassung.
- Anzahl der Fassungen. **Ohne Angabe wird genau eine gebaut.**

**Was du nie erfinden sollst:** Kundenstimmen, Zertifikate, Auszeichnungen,
Nutzerzahlen. Was nicht belegt ist, lässt er weg — das ist Absicht.

---

## Der Auftrag

Zum Kopieren. Alles in eckigen Klammern ersetzen, den Rest stehen lassen:

```
Bau eine Website für [Betrieb], [Gewerk] in [Ort].

Alte Website: [URL oder "keine"]
Telefon: [...]   E-Mail: [...]
Adresse: [...]
Öffnungszeiten: [...]

Leistungen:
- [...]
- [...]

Zielgruppe: [wer ruft an, und warum]
Wichtigste Handlung: [Anruf | Formular | Termin | Besuch]
Besonderheit: [ein Satz, warum man dorthin geht und nicht woandershin]

Material: [Ordnerpfad zu Logo und Fotos, oder "nichts vorhanden"]
```

Das reicht. Alles Weitere fragt er nach oder entscheidet er begründet.

---

## Was dann passiert

Er fährt die **Fast Lane** — Zielzeit ein Arbeitstag:

1. Legt `projekte/<name>/` an
2. Zieht die alte Seite, falls es eine gibt
3. Recherchiert und schreibt einen Kurzbrief in `PROJECT.md`
4. Füllt `content/<website>.json` mit den echten Daten
5. Zieht die Blöcke aus dem Kit
6. Wählt eine Art Direction, setzt die Farben des Betriebs, rechnet den
   Kontrast in hell **und** dunkel nach
7. Baut **zwei** Auftaktfassungen und sieht sie sich nebeneinander an
8. Rendert die ganze Seite, schreibt eine Befundliste, korrigiert
9. Lässt `qa.sh` laufen: Platzhalterreste, Links, Screenshots, axe, Lighthouse
10. Nimmt gegen die Gates ab

Zwei Dinge macht er dabei immer mit, auch wenn du nichts sagst:

- **Owner-Hosting-Anbindung.** Die Seite ist von Anfang an so gebaut, dass
  das Dashboard sie aufnehmen kann — eine Inhaltsdatei, stabile Pointer,
  Preview-Routen. Nachrüsten kostet ein Vielfaches, mitbauen kostet nichts.
- **`johannstein.com/dev`.** Sobald der erste Build steht, ist die Seite
  dort erreichbar. Du kannst mitschauen, während noch gebaut wird.

Auf die **Full Lane** wechselt er bei Login, Zahlung, eigener Datenhaltung
oder Sonderfunktion — aber er fragt dich nicht vorher. Er baut die statische
Seite fertig und merkt den Zusatzbedarf an.

### Er fragt dich erst, wenn die Seite steht

Das ist die wichtigste Regel für dich: **Vor der ersten fertigen Website
fragt er nichts.** Keine Bahnwahl, keine Farbfrage, keine fehlende
Telefonnummer. Er entscheidet, baut weiter und merkt es an.

Genau eine Ausnahme: Er hält an, **bevor er etwas Vorhandenes überschreibt
oder löscht.** Das ist nicht umkehrbar, alles andere ist es.

Am Ende bekommst du **eine** Nachricht, nicht zwölf:

1. der **Link** auf `johannstein.com/dev/<projekt>/`
2. was er **entschieden** hat, je eine Zeile Begründung
3. was er **angenommen** hat, mit Quelle und Folge
4. was **offen** ist — Platzhalter, ungeprüfte Fakten, Rechtstexte
5. was **du entscheiden musst**, meist wenig

Du siehst die Seite also, bevor du die erste Frage beantwortest. Das ist
der Punkt.

Das Einzige, was er nie erfindet: Kundenstimmen, Zertifikate,
Auszeichnungen und Kennzahlen. Deine Website steht damit für den Ruf des
Betriebs gerade. Beschreibender Text und Bildplatzhalter sind davon nicht
betroffen.

### Was du bekommst

- die Website live unter `johannstein.com/dev/<projekt>/`, geschützt und `noindex`
- die Quellen unter `projekte/<name>/site/`
- Screenshots bei 375 und 1280 in `qa-bericht/shots/`
- Lighthouse- und axe-Bericht
- Impressum und Datenschutz als **prüfpflichtige Entwürfe**
- `release-readiness/<slug>.md` mit allem, was vor dem Livegang offen ist

---

## Was du selbst tun musst

Er darf oder kann das nicht:

| Sache | Warum |
|---|---|
| **Rechtstexte freigeben** | Impressum und Datenschutz sind Entwürfe. Was veröffentlicht wird, entscheidest du. |
| **Domain und DNS** | liegt außerhalb des Repositories |
| **nginx installieren** | er hat kein Schreibrecht in `/etc`, nur `systemctl reload nginx`. Vorlage liegt in `web-kit/scripts/nginx-site.conf.template` |
| **Zertifikate** | für Domain und Vorschau-Subdomain |
| **Formular-Endpoint als Dienst** | `web-kit/scripts/kontakt-endpoint.mjs`, braucht `MAIL_TO` |
| **Fakten bestätigen — am Ende, nicht vorher** | Er übernimmt Preise und Zeiten von der alten Seite und arbeitet weiter. Was ihm auffiel, steht gesammelt in `PROJECT.md` und im Release-Readiness-Register. |

Alles davon steht auch in `SETUP-OFFEN.md`.

---

## Wenn etwas nicht stimmt

**„Sieht generisch aus."** Sag genau das. Er hat den Signaturkatalog in
`20-design/anti-ai-slop.md` und die Prüffrage: *Wäre ich bei einem anderen
Auftrag derselben Gattung an derselben Stelle gelandet?* Oder gib ihm ein
anderes Preset.

**„Falsche Richtung."** Nenn ein anderes Preset oder eine Seite, die dir
gefällt. Er baut den Auftakt neu, nicht die ganze Seite.

**„Zu viel Text."** `10-strategy/information-density-and-mobile-clarity.md`
hat Budgets je Route. Sag ihm, er soll sie durchgehen.

**„Er hat etwas erfunden."** Sollte nicht passieren — Behauptungen brauchen
Beleg. Wenn doch, melde die Stelle; das ist ein Regelverstoß, kein
Geschmacksthema.

**„Der Build läuft nicht."** Node liegt unter `/opt/node-v24.19.0/bin`, nicht
im Standardpfad.

---

## Zwei Dinge, die sich lohnen

**Sag ihm, was du am Ergebnis nicht magst, in Worten.** Er rendert die Seite
selbst und sieht sie sich an — aber er kennt deinen Geschmack nicht. Ein
Satz Kritik ersetzt eine Stunde Nachbessern.

**Lass ihn das Kit füttern.** Wenn beim Projekt ein Block entsteht, den es
ein zweites Mal geben wird, gehört er nach `web-kit/blocks/`. Sag ihm das am
Ende. Das Kit wächst aus echten Builds, nicht aus einer Wunschliste — und
jeder Block, der drin ist, muss beim nächsten Mal nicht mehr gebaut werden.
