---
type: reference
status: canonical
updated: 2026-08-16
review_by: 2027-02-16
depends_on:
  - "[[20-Design/Motion and Interaction]]"
---

# Apple Fluid Interface

> [!summary] Rolle
> Referenz für gestengeführte und federbasierte Bewegung. Sie ergänzt [[20-Design/Motion and Interaction]] dort, wo eine Bewegung vom Finger oder Zeiger geführt wird, und ersetzt keine kanonische Regel. Verbindlich bleibt der Wertesatz aus [[20-Design/Motion and Interaction#Standardrezepte mit Werten]].

Herkunft ist Apples Vortragsreihe zu flüssigen Oberflächen, vor allem *Designing Fluid Interfaces*, übersetzt auf das Web.[^wwdc-fluid] Der Skill `apple-design` aus dem Repository von Emil Kowalski war die Vorlage für diese Zusammenfassung und ist bewusst **nicht** installiert; sein Inhalt steht hier.[^emilskills] Die Typografieaussagen stammen aus *The Details of UI Typography*, die Prinzipien aus *Principles of Great Design*.[^wwdc-type][^wwdc-principles]

## Der tragende Gedanke

Eine Oberfläche wirkt lebendig, wenn Bewegung beim aktuell sichtbaren Wert beginnt, die Geschwindigkeit des Nutzers übernimmt, den Schwung nach vorn projiziert und jederzeit gegriffen und umgekehrt werden kann. Federn sind dafür das passende Werkzeug, weil sie von sich aus unterbrechbar und geschwindigkeitsbewusst sind.

## Wann diese Notiz gilt

Nur für Bewegung, die ein Nutzer direkt führt oder auslöst und deren Verlauf er beeinflussen kann: Ziehen, Wischen, Sheets und Drawer, Karussells, Slider, Press-Feedback, Momentum nach dem Loslassen. Für Scroll-Choreografie, Reveal, Zeichenauftakt und Sektionsübergänge gilt weiterhin allein die kanonische Motion-Notiz.

## Reaktion und direkte Führung

- Feedback beginnt beim Drücken, nicht beim Loslassen. Jede künstliche Verzögerung auf dem Eingabepfad ist ein Befund.
- Während der Geste wird fortlaufend aktualisiert, nicht erst am Ende.
- Beim Ziehen bleibt das Objekt am Zeiger und behält den Griffversatz. Ein Sprung in die Elementmitte beim Greifen zerstört den Eindruck sofort.
- Technisch über Pointer Events mit `setPointerCapture`, dazu eine kurze Historie aus Position und Zeitstempel, weil die Geschwindigkeit beim Loslassen gebraucht wird.

## Unterbrechbarkeit

Der wichtigste Punkt der ganzen Notiz. Jede geführte Bewegung muss mitten im Lauf greifbar und umkehrbar sein.

- Eingaben werden während einer Transition nie gesperrt.
- Eine neue Animation startet beim aktuell dargestellten Wert, nie beim logischen Zielwert. Sonst entsteht ein sichtbarer Sprung.
- CSS-Transitions und Keyframes sind für gestengeführte Bewegung ungeeignet, weil sie beim Neustart von vorn beginnen.
- Bei einer Umkehr wird die Geschwindigkeit übernommen und nicht hart geschnitten. Ein harter Schnitt fühlt sich wie eine Wand an.
- Zweidimensionale Bewegung wird in zwei unabhängige Federn für X und Y zerlegt.

## Federwerte

Zwei Parameter statt Masse, Steifigkeit und Dämpfung. `damping` steuert das Überschwingen, `response` in Sekunden die Annäherung an das Ziel. Eine Feder hat keine feste Dauer.

| Interaktion | damping | response |
|---|---|---|
| Verschieben und Neupositionieren | 1.0 | 0.4 |
| Rotation | 0.8 | 0.4 |
| Drawer und Sheet | 0.8 | 0.3 |

Standard ist kritisch gedämpft mit `1.0`. Ein Nachschwingen um `0.8` nur dann, wenn die Geste selbst Schwung getragen hat, also nach einem Schnippen, Werfen oder einem Loslassen aus der Bewegung. Ein Menü, das nur eingeblendet wurde, schwingt nicht nach.

## Geschwindigkeitsübergabe und Momentum

Beim Ende der Geste läuft die Bewegung mit genau der Geschwindigkeit des Fingers weiter. Das ist die Naht zwischen Ziehen und Animieren, und sie entscheidet über den Eindruck.

Der Zielpunkt wird nicht vom Loslasspunkt aus gewählt, sondern von der projizierten Ruhelage aus. Apples Projektion ist eine exponentielle Abklingform, nicht die Schulformel:

```js
function project(initialVelocity, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}
```

Erst wird der projizierte Endpunkt bestimmt, dann der nächstgelegene Rastpunkt gewählt, dann die Geschwindigkeit an die Feder übergeben. Ob eine Geste committet oder zurückfällt, entscheidet das Vorzeichen der Geschwindigkeit, nicht die zurückgelegte Strecke.

## Grenzen und Richtungshinweis

- An einer Kante wird progressiv gebremst statt hart gestoppt. Ein harter Stopp liest sich als eingefroren, ein weicher Widerstand als bedienbar und zu Ende.
- Zwischenbilder zeigen in die Richtung des Ergebnisses. Der Nutzer liest den Ausgang aus der Bahn, nicht erst aus dem Endzustand.
- Ein- und Austritt laufen denselben Weg. Was von rechts kommt, verschwindet nach rechts. Das deckt sich mit der Ursprungsregel für Popover und Menüs aus [[30-Frontend/Components and UI States#Kartenrezept]] und mit der Kompositionsregel in [[20-Design/Design Direction#Komposition und Überschriften]].

## Gestendetails

- Tippen hebt beim Berühren hervor und löst beim Loslassen aus. Rund zehn Pixel Toleranz, Abbruch durch Wegziehen ist möglich.
- Ziehen braucht eine kleine Schwelle vor der Richtungsentscheidung, danach eine Eins-zu-eins-Führung.
- Mögliche Gesten werden ab der ersten Bewegung parallel erkannt und die Verlierer werden verworfen, sobald die Absicht klar ist. Ereignisse, die nur einen Endzustand melden, verschenken die laufende Rückmeldung.

## Material und Tiefe

- Durchscheinende Leisten und Sheets als schwebende Ebene mit darunter laufendem Inhalt. Das Kontrast- und Fallbackrezept bleibt kanonisch in [[30-Frontend/Components and UI States#Rezept der durchscheinenden Kopfzeile]].
- Materialgewicht trägt Hierarchie. Schwerere Flächen trennen Regionen, leichtere heben Bedienelemente hervor. Zwei leichte durchscheinende Flächen übereinander zerstören die Lesbarkeit.
- Große Flächen wirken dicker als kleine, also stärkere Unschärfe und tieferer Schatten. Die eine erlaubte Schattenstufe aus [[20-Design/Typography Layout and Spacing#Tiefe und Rahmen]] bleibt davon unberührt.
- Ein modaler Vorgang bekommt Abdunklung, eine parallele Nebenfläche nicht, damit der Fluss nicht bricht.
- Statt einer Trennlinie unter einer klebenden Kopfzeile eine kleine Verlaufsmaske dort, wo Inhalt und schwebende Fläche sich tatsächlich überlappen.
- Eine Glasfläche materialisiert sich, sie blendet nicht nur ein. Unschärfe und Maßstab laufen dabei gemeinsam.

## Barrierefreiheit über Reduced Motion hinaus

Drei unabhängige Signale, nicht eines:

- `prefers-reduced-motion: reduce` ersetzt Versatz und Federung durch kurze Überblendungen, kanonisch geregelt in [[20-Design/Motion and Interaction#Reduced Motion]].
- `prefers-reduced-transparency: reduce` macht durchscheinende Flächen deckend und nimmt die Unschärfe heraus.
- `prefers-contrast: more` bringt nahezu deckende Flächen mit definiertem Rahmen.

Die beiden letzten sind im Brain bisher nicht geregelt und sollten in einem Projekt mitgeführt werden, sobald es durchscheinende Flächen einsetzt. Ergänzend gilt: keine vollflächig bewegten Hintergründe, keine langsamen Dauerschleifen um eine Sekunde je fünf Sekunden, keine abrupten Helligkeitssprünge beim Themenwechsel.

## Was hier bewusst nicht steht

Die Typografieaussagen der Vorlage zu größenabhängigem Tracking und Zeilenabstand sind bereits kanonisch in [[20-Design/Typography Layout and Spacing]] geregelt und werden hier nicht wiederholt. Haptik und Ton sind für Webprojekte dieses Brains ohne Anwendung. Die Systemschrift als Vorgabe wird nicht übernommen, weil die Schriftentscheidung aus [[20-Design/Design Direction#Direction Brief]] kommt.

[^wwdc-fluid]: [Apple WWDC 2018: Designing Fluid Interfaces](https://developer.apple.com/videos/play/wwdc2018/803/)
[^wwdc-type]: [Apple WWDC 2020: The Details of UI Typography](https://developer.apple.com/videos/play/wwdc2020/10175/)
[^wwdc-principles]: [Apple: Principles of Great Design](https://developer.apple.com/videos/design/)
[^emilskills]: [Emil Kowalski: Skills For Designers and Engineers, MIT-Lizenz](https://github.com/emilkowalski/skills)
