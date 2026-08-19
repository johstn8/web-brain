---
type: canonical
status: canonical
updated: 2026-08-19
review_by: 2027-02-09
impacts:
  - auth
  - operations
  - qa
  - architecture
---

# Preview Access Gate

## Zweck und Abgrenzung

Das Preview Access Gate sperrt eine ganze Vorschau-Domain gegen zufällige Besucher und Suchmaschinen, solange ein Projekt noch nicht offiziell ist. Es ist kein Login und kein Rollenmodell. Wer Konten, Rollen oder personenbezogene Sitzungen braucht, folgt [[40-Backend-Security/Authentication and Accounts]]; die Pflichtkontrollen aus [[40-Backend-Security/Security Baseline]] gelten unverändert zusätzlich.

Schutzziel ist ausschließlich: nicht öffentlich auffindbar und nicht versehentlich aufrufbar. Ein kurzer Zugangscode ist gegen gezielte Angreifer wertlos. Deshalb darf hinter dem Gate nichts liegen, dessen Offenlegung echten Schaden anrichtet, insbesondere keine echten Kundendaten, keine Produktionsschlüssel und keine Zahlungsvorgänge.

## Kanonische Umsetzung

- Durchsetzung serverseitig am Reverse Proxy, nicht in der Anwendung. Ein Client-Check ist nach [[40-Backend-Security/Security Baseline]] unzulässig, und ein Proxy-Gate schützt zusätzlich statische Dateien und Fehlerseiten.
- HTTP Basic Auth über nginx `auth_basic` auf Serverebene, damit jede Location erfasst ist. Eine Ausnahme gilt nur für `/.well-known/acme-challenge/`, sonst schlägt die Zertifikatserneuerung fehl.
- Das Passwort steht als Hash in einer `htpasswd`-Datei außerhalb des Webroots. Nie im Klartext, nie im Anwendungsrepository. Hash erzeugen mit `openssl passwd -apr1 <code>`.
- `X-Robots-Tag: noindex, nofollow` als Header und `noindex` in jeder ausgelieferten Seite. Das Gate allein hält Vorschauinhalte nicht aus Suchindizes fern, wenn eine URL geteilt wird.
- HTTPS mit HSTS ist Pflicht, weil Basic Auth die Zugangsdaten bei jedem Request mitsendet.
- Eigene Domain oder Subdomain für Vorschauen. Niemals ein Unterpfad der Produktionsdomain, sonst erben Vorschauen Cookies, Service Worker und Analytics der Live-Seite.

## Ablage

Vorschauprojekte liegen in `Web-Design/vorschau/<Projektname>/`, parallel zu `projekte/` für Live-Websites. Die gemeinsame Gate-Konfiguration liegt einmalig unter `vorschau/_gate/`. Jedes weitere Projekt bekommt eine eigene `location` mit eigenem lokalem Port nach der Portkonvention aus [[60-Operations/Delivery and Local Start]] und erbt das Gate automatisch, weil `auth_basic` auf Serverebene steht.

## Betrieb

- Codewechsel: neuen Hash erzeugen, `htpasswd` ersetzen, `nginx -t` und Reload. Kein Anwendungsdeploy nötig.
- Beim Übergang in den öffentlichen Betrieb wird das Gate auf dem Produktionshost entfernt und das Projekt nach `projekte/` verschoben. Dabei sind Domain, Zertifikat, `noindex`, Analytics und Sitemap neu zu entscheiden, nicht zu übernehmen. Die Entfernung von `auth_basic`, Headern, Robots-Regeln und anderen Sperren wird im `release-readiness/<website-slug>.md` nach [[60-Operations/Release Readiness Register]] mit Produktionsnachweis geschlossen; die Vorschau bleibt geschützt.
- Der Code gehört nicht in Tickets, Repositories oder Chatverläufe mit Dritten.

## Prüfpunkte

- Aufruf ohne Zugangsdaten liefert `401`, auch für Unterpfade, statische Dateien und eine nicht existierende URL.
- Falscher Code liefert `401`, korrekter Code liefert die Seite.
- HTTP leitet auf HTTPS um, Zertifikat gültig, Erneuerung läuft trotz Gate.
- `X-Robots-Tag` ist in der Antwort vorhanden.
- Die `htpasswd`-Datei enthält keinen Klartext und liegt außerhalb des Webroots.
