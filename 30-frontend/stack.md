---
type: canonical
status: canonical
updated: 2026-09-19
depends_on:
  - "[[30-frontend/architecture-and-code-consistency.md]]"
  - "[[20-design/color-system.md]]"
impacts:
  - "[[30-frontend/web-kit.md]]"
  - "[[00-start/05-web-product-workflow.md]]"
  - "[[70-qa/quality-gates.md]]"
  - project-master-spec
---

# Stack

## Entscheidung

Websites für lokale Betriebe werden auf einem festen Stack gebaut. Der Stack ist keine Empfehlung und keine Auswahl je Projekt, sondern der Normalfall.

| Schicht | Festlegung |
|---|---|
| Framework | Astro |
| Styling | Tailwind, ausschließlich gegen die Tokenrollen aus [[20-design/color-system.md#Tokenvertrag]] |
| Ausgabe | statischer Build, kein Serverrendering zur Laufzeit |
| Formulare | eigener Endpoint mit Servervalidierung nach [[40-backend-security/security-baseline.md]], kein Drittanbieterformular |
| Bilder | Astro-Asset-Pipeline mit responsiven Varianten und modernen Formaten |
| Material | Blöcke, Starter und Skripte aus [[30-frontend/web-kit.md]] |

## Begründung

Ohne festen Stack gibt es keine Blockbibliothek, ohne Blockbibliothek keine Wiederverwendung und ohne Wiederverwendung keine Geschwindigkeit. Die Fast Lane aus [[00-start/05-web-product-workflow.md#Bahnwahl: Fast Lane und Full Lane]] setzt genau darauf auf: die Blöcke laufen unverändert, weil die Rollennamen des Tokenvertrags in jedem Projekt gleich heißen und nur die Werte wechseln.

Der Stack ist auf die tatsächliche Aufgabe zugeschnitten. Eine Website mit Öffnungszeiten, Leistungen, Anfahrt und Kontaktformular braucht zur Laufzeit keinen Server. Statisch ausgeliefertes HTML ist schnell, billig zu hosten, ohne Wartungsfenster und macht Performance- und SEO-Budgets von vornherein erreichbar.

## Regeln

- Tailwind konfiguriert seine Farb-, Abstands- und Radiuswerte aus den Tokenrollen. Keine Rohwerte in Klassen, wo eine Rolle existiert.
- Eine Styling-Strategie pro Projekt nach [[30-frontend/architecture-and-code-consistency.md#Einheitlichkeit]]. Globales CSS nur für Reset, Tokens und echte Globals.
- Der Formular-Endpoint validiert serverseitig, begrenzt die Rate und hält Secrets serverseitig. Consent-Mechanik nach [[50-legal/privacy-and-consent.md]].
- Bilder gehen vor dem Einbinden durch die Aufbereitung aus [[20-design/imagery-and-ai-editing.md]] und danach durch die Asset-Pipeline, nicht umgekehrt.
- Abhängigkeiten werden nach [[60-operations/dependencies-and-environments.md]] bewertet. Das Kit bringt seine eigenen Blöcke mit; eine Komponentenbibliothek wird nicht zusätzlich eingezogen.

## Abweichung

Eine Abweichung von diesem Stack ist eine begründungspflichtige Ausnahme. Sie wird vor dem ersten UI-Code in `PROJECT.md` dokumentiert, mit:

- der abweichenden Festlegung,
- der Anforderung, die sie erzwingt,
- dem Grund, warum Astro mit statischem Build sie nicht trägt,
- den Folgen für Kit-Wiederverwendung, Performance-Budget und Betrieb.

Eine Abweichung ohne diese vier Angaben ist ein Befund in `G0`.
