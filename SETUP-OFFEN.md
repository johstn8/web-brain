# Offene Punkte nach dem Umbau

Stand 19.09.2026. Diese fünf Punkte lassen sich nicht im Repository
abschließen. Sie sind so weit vorbereitet, wie es hier möglich war; was
fehlt, ist jeweils ein Schritt in einer Oberfläche, auf einem Server oder
bei einem Anbieter.

Die Punkte folgen Abschnitt 5 des Arbeitsauftrags „Web-Brain Umbau".

---

## B1 — Basissystem als Design-System-Artifact anlegen

**Offen.** Ein Schritt in der Oberfläche.

Geliefert ist alles, was das Artifact als Inhalt braucht:

| Datei | Inhalt |
|---|---|
| `web-kit/tokens/tokens.json` | 18 Vertragsrollen, je Rolle Wert für Licht und Dunkel plus Usage-Notiz; dazu Type-Ramp, Spacing, Radius, Layout und Motion |
| `web-kit/tokens/design-system.json` | fertiger Export im Zielformat, jede Familie als Liste |
| `web-kit/scripts/tokens-to-designsystem.ts` | erzeugt den Export neu |
| `web-kit/scripts/check-contrast.ts` | belegt Kontrast in beiden Themes, 36 Paare, 0 unter dem Ziel |

**Nächster Schritt:** das Basissystem im Chat oder über `/design` aus
`web-kit` anlegen und `design-system.json` hineingeben. Es trägt bewusst
keine Kundenfarben; sein Akzent ist neutrale Tinte, damit niemand ihn für
eine Marke hält.

Der Ablauf ist kanonisch in [[20-design/design-systems-und-artefakte.md]]
beschrieben.

---

## B2 — Je Kunde ein abgeleitetes Design-System

**Entsteht pro Projekt, nicht beim Umbau.** Das ist kein Rückstand.

Der Ablauf ist in [[20-design/design-systems-und-artefakte.md]] kanonisch
beschrieben: die Werte entstehen im Design Contract, gehen über
`tokens-to-designsystem.ts` in das Artifact, und Änderungen am Artifact
kommen über `/design-sync` zurück in die Session. Welche Seite kanonisch
ist, hält `PROJECT.md` je Projekt als `Tokenquelle: projekt | artifact`
fest.

Die Rollennamen sind fix. Ein Kundenwechsel ist ein Wertewechsel, kein
Umbau.

---

## B3 — Playwright als MCP-Server verbinden

**Teilweise gelöst.** Screenshots funktionieren bereits, aber auf einem
Umweg.

`web-kit/scripts/render-shots.ts` ist geschrieben und läuft. Es versucht
zuerst Playwright und fällt sonst auf einen lokal vorhandenen Chromium über
das DevTools-Protokoll zurück. Auf `217.154.218.30` liegt Chromium unter
`~/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome`; seine
Systembibliotheken liegen entpackt unter
`~/.local/lib/chromium-deps/usr/lib/x86_64-linux-gnu` und werden vom Skript
über `LD_LIBRARY_PATH` mitgegeben.

Belegt am 19.09.2026: ganzseitige Screenshots bei 375 und 1280 Pixel für
drei Seiten des Starters, dazu `check-axe.ts` mit axe-core über denselben
Weg — 0 Verstöße gegen WCAG 2.1 AA.

**Was noch fehlt:** die Verbindung als MCP-Server in den Einstellungen.
Sie macht den Browser für den Agenten direkt steuerbar, statt nur über die
Skripte. Ohne sie bleibt der Renderdurchgang an `render-shots.ts` gebunden.

Auf anderen Maschinen ist zu prüfen, ob ein Browser vorhanden ist. Fehlt
einer, meldet das Skript einen Blocker statt still zu überspringen: ohne
echten Render ist `G1` nicht erfüllt.

---

## B4 — Skills installieren und Lizenzen klären

**Offen, aber entschärft.**

Seit A8 hängt die Auslieferung nicht mehr an diesen Installationen. Gate
`G1` prüft das Ergebnis, nicht das Werkzeug, und
[[00-start/04-plugins-and-skills.md#Ersatzstrecke ohne Skills]] dokumentiert
je Skill, wie dieselbe Arbeit ohne ihn geleistet und nachgewiesen wird.

| Skill | Stand |
|---|---|
| UI UX Pro Max | installiert unter `~/.agents/skills/ui-ux-pro-max/`; **Lizenz offen** |
| Impeccable | installiert unter `~/.agents/skills/impeccable/`; Lizenz vor externem Einsatz prüfen |
| Emil Design Engineering | installiert unter `~/.agents/skills/emil-design-eng/`; Quellen und Lizenz vor externem Einsatz prüfen |
| `animate`, `review-animations`, `prototype` | installiert unter `/srv/Web-Design/shared-agent-skills/`, MIT |

**Zwei nächste Schritte:**

1. Verfügbarkeit auf allen Maschinen herstellen, bevorzugt über das Plugin
   aus A12: `/plugin marketplace add johstn8/web-brain`, dann
   `/plugin install web-build@johstn8`. Das Plugin bringt den eigenen Skill
   `web-build` mit, nicht die fremden Skills.
2. **Die Lizenzfrage zu UI UX Pro Max klären, bevor er in einem
   Kundenprojekt eingesetzt wird.** Sie steht in
   [[00-start/04-plugins-and-skills.md]] und
   [[98-maintenance/review-queue.md]] seit Längerem offen. Für den eigenen
   Gebrauch ist das eine Notiz, für ein bezahltes Kundenprojekt ein Risiko.

---

## B5 — Server und Auslieferung

**Vorbereitet, Installation offen.**

Geschrieben und im Kit abgelegt:

| Datei | Zweck |
|---|---|
| `web-kit/scripts/deploy.sh` | Build, QA, atomarer Symlink-Wechsel nach Smoke-Test, fünf Releases für Rollback; `--preview` setzt `robots.txt` auf Disallow und entfernt die `sitemap.xml` |
| `web-kit/scripts/nginx-site.conf.template` | öffentliche Route mit CSP und Cache-Regel, Proxy auf den Formular-Endpoint, getrennte Vorschau-Subdomain mit `auth_basic` und `X-Robots-Tag` |
| `web-kit/scripts/kontakt-endpoint.mjs` | Formular-Endpoint: Origin-Prüfung, Ratelimit, Größengrenze, serverseitige Allowlist-Validierung, Honeypot, Versand über `sendmail` |

**Was der Nutzer selbst tun muss**, weil der Agent es nicht darf oder nicht
entscheiden kann:

1. **nginx-Konfiguration installieren.** Der Agent hat kein Schreibrecht in
   `/etc`; seine NOPASSWD-Liste erlaubt nur `systemctl reload nginx`.
   Vorlage ausfüllen, nach `/etc/nginx/sites-available/<slug>` legen,
   verlinken, `nginx -t`, neu laden.
2. **Vorschau-Zugang setzen.** `htpasswd`-Datei außerhalb des Webroots
   anlegen, Hash mit `openssl passwd -apr1 <code>`. Regeln in
   [[40-backend-security/preview-access-gate.md]].
3. **Zertifikate** für `<domain>` und `vorschau.<domain>` ausstellen. Die
   ACME-Location ist in der Vorlage bereits von `auth_basic` ausgenommen;
   ohne das schlägt jede Erneuerung fehl.
4. **Deploy-Key für `web-kit`** im Repository hinterlegen, damit der Server
   ohne persönliche Zugangsdaten klonen kann.
5. **Formular-Endpoint als Dienst** einrichten, mit `MAIL_TO`, `MAIL_FROM`
   und `ALLOWED_HOSTS`. Als `systemctl --user`-Unit mit Linger, weil
   systemweite Units hier root brauchen. `Protect*`-Direktiven scheitern in
   der Nutzerinstanz.
6. **Domain und DNS** entscheiden. Bleibt bewusst außerhalb des
   Repositories.

---

## Was nicht offen ist

Zur Abgrenzung, damit kein falscher Rückstand entsteht: Der Umbau selbst
ist abgeschlossen. A1 bis A12 sind umgesetzt und committet, der vault-weite
Link-Check läuft ohne toten Link durch, und `web-kit` steht mit einem
Starter, der baut, und einem QA-Lauf, der alle fünf Prüfungen besteht.
