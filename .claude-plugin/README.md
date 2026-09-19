# Plugin `web-build`

Buendelt den Skill `web-build`, damit er auf Laptop und Server mit einem
Befehl installiert ist statt manuell nach `~/.claude/skills/` verlinkt.

## Installation

```
/plugin marketplace add johstn8/web-brain
/plugin install web-build@johstn8
```

Danach loest der Skill von selbst aus, sobald ein Website-Auftrag fuer einen
lokalen Betrieb kommt. Ein `/plugin update web-build@johstn8` holt spaetere
Aenderungen nach; ohne Plugin muesste jede Maschine einzeln nachgezogen
werden, und genau dabei laufen sie auseinander.

## Was das Plugin nicht mitbringt

Die Repositories `web-brain` und `web-kit` selbst. Der Skill setzt voraus,
dass beide nebeneinander geklont sind. Ebenso wenig bringt es UI UX Pro Max,
Impeccable oder `review-animations` mit; deren Stand fuehrt
`SETUP-OFFEN.md` unter B4.
