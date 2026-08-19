---
type: canonical
status: canonical
updated: 2026-08-19
review_by: 2027-02-19
depends_on:
  - "[[40-Backend-Security/Preview Access Gate]]"
  - "[[30-Frontend/SEO and Discoverability]]"
impacts:
  - project-workflow
  - launch
  - qa
  - operations
  - seo
  - integrations
---

# Release Readiness Register

## Zweck

Jede gebaute Website führt ab Projektbeginn ein eigenes, dauerhaftes Register unter `release-readiness/<website-slug>.md`. Die Vorlage ist [[80-Templates/Release Readiness Register]]. Das Register sammelt alles, was vor einer öffentlichen Veröffentlichung noch aktiviert, ersetzt, entfernt, geprüft oder vom benannten Owner entschieden werden muss.

Es ist keine Checkliste, die erst am Launch-Tag entsteht. Eine neue provisorische Sperre, Attrappe, deaktivierte Integration oder sichtbare Unfertig-Aussage erzeugt in derselben Änderung einen Eintrag. Ein erledigter Eintrag wird mit Nachweis geschlossen und nicht gelöscht. Bei mehreren Websites sind getrennte Dateien Pflicht, weil Endpunkte, Domains, Sperren, Inhalte und Freigaben voneinander abweichen können.

Das Register liefert Fakten für die Veröffentlichung. Die Entscheidung `Go` oder `No-Go` trifft ausschließlich der Nutzer beziehungsweise der benannte Owner.

## Status und Priorität

Jeder Eintrag besitzt genau einen Status: `open`, `in_progress`, `ready_for_retest`, `verified`, `accepted_open` oder `not_applicable`. `verified` verlangt einen Nachweis aus der vorgesehenen Produktionsumgebung. `accepted_open` dokumentiert eine ausdrückliche Owner-Entscheidung mit Datum und ersetzt keinen technischen Nachweis.

Prioritäten:

- `P0 release-blocking`: Veröffentlichung würde Anfragen verlieren, falsche Erfolge melden, Daten gefährden, die gesamte Website unauffindbar machen oder eine ausdrücklich zugesagte Kernfunktion nicht liefern.
- `P1 owner-decision`: Inhalt, Anbieter, Zugang, Rechtstext oder Geschäftsentscheidung fehlt. Der Owner entscheidet, ob dies die Veröffentlichung stoppt.
- `P2 follow-up`: Verbesserung nach Veröffentlichung möglich, ohne eine sichtbare Zusage oder einen kritischen Fluss zu brechen.

## Was fortlaufend gesammelt wird

Das Register enthält mindestens:

1. **Öffentlichkeit und Entsperrung:** nginx `auth_basic`, Passwortseiten, IP-Allowlist, Wartungsmodus, Preview-Feature-Flags, `X-Robots-Tag`, Robots-Meta, `robots.txt`, entfernte oder ersetzte `sitemap.xml`, Canonicals auf Vorschauhosts, Test-DNS, Zertifikate und Redirects.
2. **Formulare und E-Mail:** jedes Formular, jeder API-Endpunkt, Empfänger, tatsächlicher Versand- oder Speicherweg, Provider, Domainauthentifizierung, Retry, Alert, Rate Limit, Datenschutzbezug und echter Ende-zu-Ende-Nachweis.
3. **Externe Integrationen:** Google Search Console, Site Verification, Analytics, Consent, Maps, Kalender, CRM, Webhooks, Zahlungsanbieter, Captcha, Social Feeds und sonstige Konten oder APIs einschließlich Berechtigung und Produktionsmodus.
4. **Sichtbare Unfertigkeit:** Hinweise wie „noch nicht verfügbar“, „Demo“, „Coming soon“, „Kontaktformular funktioniert noch nicht“, Platzhalter, Testdaten, Beispieladressen, auskommentierte Aktionen, deaktivierte Controls ohne fachlichen Grund, Wasserzeichen, Preview-Banner, Staging-Badges, leere `href="#"`-Links und temporäre Fehlertexte.
5. **Inhalt und Vertrauen:** noch zu bestätigende Fakten, ungeprüfte Öffnungszeiten, fehlende echte Belege, veraltete Termine, Dummy-Profile, unvollständige Rechtstextentwürfe und fehlende Owner-Entscheidungen. Diese Punkte bleiben von technischen Sperren getrennt.
6. **Betrieb:** Produktions-Secrets, erlaubte Origins, CSP/CORS, Cache, Logs, Monitoring, Alerts, Backups, Restore, Rollback, 404/500, Healthchecks und Verantwortliche.

Die Suche nach Unfertig-Aussagen ist semantisch. Ein Satz wie „Noch nicht sicher, welche Leistung passt?“ ist kein Befund. Ein Satz, der eine Funktion als unfertig oder nur simuliert bezeichnet, ist einer. Jeder sichtbare Befund nennt Route, exakten Text oder Selector, Quelle im Code, Zielzustand und die konkrete Entfernung oder Ersetzung.

## E-Mail und Formulare wirklich nachweisen

Ein Formular gilt nicht als versandbereit, weil ein `fetch` erfolgreich war oder die Oberfläche eine Erfolgsmeldung zeigt. Für jeden E-Mail- oder Nachrichtenfluss wird getrennt belegt:

- Produktions-Endpunkt und serverseitige Validierung sind aktiv; Test-, Mock- und Mail-Catcher-Ziele sind entfernt.
- Provider, Absenderdomain, `From`, `Reply-To`, Empfänger und Secret-Quelle sind dokumentiert. SPF, DKIM und soweit vorgesehen DMARC sind für die echte Domain geprüft.
- Missbrauchsschutz, Größenlimits, Timeouts, idempotente Verarbeitung beziehungsweise Deduplizierung, Retry und Fehlerprotokoll sind vorhanden.
- Die Website meldet Erfolg erst, wenn der definierte Übergabepunkt erreicht ist. `gespeichert`, `an Provider übergeben` und `im Zielpostfach angekommen` werden nicht gleichgesetzt.
- Eine eindeutige Testanfrage aus der öffentlichen Produktionsfassung kommt im realen Zielpostfach oder im verbindlichen Betreiber-Posteingang an. Inhalt, Anhänge, Umlaute, Antwortadresse, Spam-Einstufung und Zeitstempel werden geprüft.
- Der Fehlerfall wird absichtlich ausgelöst. Die Anfrage geht nicht verloren, der Nutzer erhält eine ehrliche Rückmeldung und der Betreiber einen Alert oder einen nachweisbaren Retry-Pfad.

Kann ein Formular Anfragen zuverlässig serverseitig speichern und der Betreiber sie dort lesen, darf es ohne E-Mail-Benachrichtigung betrieben werden. Dann nennt die Website diesen tatsächlichen Zustand und das Register führt den fehlenden E-Mail-Versand nicht als erledigt, sondern als bewusst gewählte Betriebsform mit Owner-Entscheidung.

## Produktionsentsperrung und Indexierung

Preview-Schutz wird nicht blind in die Produktion kopiert. Der Cutover wird als zusammenhängende Änderung vorbereitet und in einer Vorschau der endgültigen nginx- und Release-Konfiguration geprüft:

1. Produktionshost und TLS stehen fest; alle Canonicals, OG-URLs, hreflang-Ziele und die `sitemap.xml` verwenden ausschließlich die öffentliche HTTPS-Domain.
2. Für den Produktionshost werden `auth_basic`, IP-Sperren, Wartungsmodus und Preview-Flags entfernt. Die Vorschau-Domain bleibt geschützt.
3. `X-Robots-Tag: noindex, nofollow, noarchive` und Robots-Meta mit `noindex` werden auf **allen** Produktionsantworten entfernt. `noarchive` wird von Google zwar nicht mehr verwendet, kann aber als Rest einer Vorschaukonfiguration auf andere Crawler oder Audits wirken und wird deshalb ebenfalls entfernt.[^robots-meta]
4. `robots.txt` wird von `Disallow: /` auf die beabsichtigte Produktionspolicy umgestellt und verweist auf die Produktions-Sitemap. Die Umstellung wird mit dem Entfernen von `noindex` koordiniert: Ein per `robots.txt` gesperrter Crawler kann ein `noindex` auf der Seite nicht sehen.[^robots-meta]
5. Stichproben prüfen Status, Header und HTML für Startseite, jede primäre Route, 404, Asset und PDF. Zusätzlich werden `robots.txt`, `sitemap.xml`, Canonical, interne Links und Redirectketten maschinell geprüft.
6. Erst nach dem öffentlichen Cutover werden Sitemap-Einreichung, URL-Prüfung und erneutes Crawlen angestoßen. Eine Crawl-Anforderung garantiert keine sofortige Indexierung.[^recrawl]

## Google Search Console und APIs

Die Search-Console-Integration und die Indexierbarkeit der Website sind getrennte Einträge. Eine grüne API-Verbindung beweist keine Indexierung; eine indexierbare Website beweist keine aktive API.

Vor `verified` sind mindestens belegt:

- richtige Property-ID und Property-Art, etwa `sc-domain:example.de` oder eine exakte URL-Prefix-Property;
- bestätigte Inhaberschaft beziehungsweise delegierter Zugriff des vorgesehenen Kontos;
- aktiviertes Google-Cloud-Projekt und OAuth-2.0-Zugang. Ein API-Key allein genügt für private Property-Daten nicht.[^gsc-auth]
- bei einem Dienstkonto: dessen E-Mail ist der Property mit der benötigten Rolle hinzugefügt; Secret liegt ausschließlich serverseitig und minimal berechtigt;
- ein echter `searchAnalytics.query` mit dem vorgesehenen Read-only-Scope funktioniert gegen genau diese Property; Zeitraum, Datenverzug, leere Daten und API-Grenzen werden korrekt behandelt.[^gsc-query]
- der getrennte Netzwerkweg, Token-/Secret-Rotation, Fehleralert und Verantwortliche sind dokumentiert;
- falls die Site Verification API verwendet wird: Token wurde über den gewählten DNS- oder Dateiweg gesetzt und die Verifikation im Kontext des authentifizierten Kontos abgeschlossen.[^site-verification]

## Abgleich vor Veröffentlichung

Unmittelbar vor der Owner-Entscheidung werden vier Quellen gegeneinander geprüft:

1. Registereinträge und ihre Nachweise,
2. Repository-Suche nach provisorischen Texten, Flags, Testschlüsseln und Dummy-Zielen,
3. tatsächlich ausgelieferte Produktionskandidaten einschließlich Response-Header und externer Flows,
4. Infrastruktur außerhalb des Repositories: nginx, DNS, Zertifikate, Providerkonten, Google-Propertys, Secret Store und Monitoring.

Die [[80-Templates/Launch Checklist]] fasst die Freigabe zusammen. Sie ersetzt dieses laufende Register nicht.

[^robots-meta]: [Google Search Central: Robots-Meta und X-Robots-Tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
[^recrawl]: [Google Search Central: Erneutes Crawlen anfordern](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
[^gsc-auth]: [Google Search Console API: Voraussetzungen und OAuth-Berechtigung](https://developers.google.com/webmaster-tools/v1/prereqs)
[^gsc-query]: [Google Search Console API: Search Analytics query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
[^site-verification]: [Google Site Verification API: Getting Started](https://developers.google.com/site-verification/v1/getting_started)
