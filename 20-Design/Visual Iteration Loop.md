---
type: canonical
status: canonical
updated: 2026-09-11
sources_checked: 2026-09-11
review_by: 2027-03-11
depends_on:
  - "[[20-Design/Landing Page Craft]]"
  - "[[20-Design/Interface Benchmarks]]"
  - "[[20-Design/Anti AI Slop]]"
impacts:
  - "[[00-Start/05 Web Product Workflow]]"
  - "[[00-Start/04 Plugins and Skills]]"
  - "[[20-Design/Design Direction]]"
  - "[[70-QA/Quality Gates]]"
  - "[[70-QA/Test Matrix]]"
---

# Visual Iteration Loop

> [!important] Rang
> Diese Notiz ist der kanonische Besitzer dafür, **durch welche Arbeit** eine gebaute
> Oberfläche ihre Qualität erreicht: Divergenz vor der Wahl, Iteration am gerenderten
> Bild, Pflichtdurchgänge, Befundform, Abbruchregel und Nachweis.
> Angrenzende Besitzer bleiben unverändert: [[20-Design/Landing Page Craft]] für den
> Aufbau der Startseite, [[20-Design/Anti AI Slop]] für den Befundkatalog,
> [[20-Design/Interface Benchmarks]] für H0 und Leitbenchmark, [[70-QA/Quality Gates]]
> für die Abnahme und [[70-QA/Test Matrix]] für die Prüfumgebung.

## Warum diese Notiz existiert

Das Brain beschreibt sehr genau, **was** eine gute Oberfläche ausmacht und woran eine
generierte erkennbar ist. Es beschrieb bisher nicht, **wodurch** eine Fassung von
regelkonform zu gut wird.

Regeln verhindern Fehler; sie erzeugen keine Qualität. Eine Fassung, die jede Regel
dieses Brains erfüllt und jeden Befund aus [[20-Design/Anti AI Slop#Slop-Signaturen]]
vermeidet, ist damit neutral, noch nicht professionell. Professionelle Anmutung
entsteht in den Durchgängen danach, und zwar ausschließlich am tatsächlich
gerenderten Bild.

Die erste Fassung ist nie die Lieferfassung. Wer sie in einem Zug erzeugen will,
arbeitet gegen das Werkzeug; der Bau wird stattdessen wie die Zusammenarbeit mit einer
Person geführt, die einen Anfang macht und danach Rückmeldung bekommt.[^oneshot]

Der Render war im Brain bisher ein **Nachweisartefakt** für die Abnahme. Ein
Screenshot, der erzeugt, abgelegt und nie angesehen wird, verbessert nichts. Ab jetzt
ist der Render zuerst ein **Arbeitsmittel** und erst danach ein Nachweis.

Die zweite Lücke liegt davor: Das [[20-Design/Landing Page Craft#Auftakt-Repertoire]]
bietet zehn Auftaktkompositionen an, aber nichts verlangte, dass mehr als eine davon je
gebaut und angesehen wird. Eine Komposition, die nur gedanklich gewählt wird, ist bei
einem Sprachmodell faktisch die wahrscheinlichste — also genau die Ursache der
generischen Anmutung, die [[20-Design/Landing Page Craft#Professionell gegen generiert]]
selbst benennt.

## Der Loop

`rendern -> ansehen -> benennen -> ändern -> erneut rendern`

- **Ansehen heißt ansehen.** Der Agent betrachtet den erzeugten Render als Bild und
  beurteilt ihn. Eine Beurteilung aus dem Quelltext, aus der eigenen Absicht, aus
  bestandenen Tokenpaaren oder aus der Beschreibung der geplanten Wirkung ersetzt das
  nicht. Das Hin und Her aus Bild und Rückmeldung ist nicht ein Teil der
  Frontend-Arbeit, sondern ihr Hauptteil.[^mainwork]
- **Benennen heißt schreiben.** Jeder Durchgang erzeugt eine kurze Befundliste mit Ort,
  Beobachtung und beabsichtigter Änderung. Ein Durchgang ohne schriftlichen Befund hat
  nicht stattgefunden.
- **Ein Durchgang ändert eine Klasse von Dingen**, nicht alles gleichzeitig. Sonst ist
  nicht mehr zuzuordnen, welche Änderung gewirkt hat.
- Kann in der Umgebung kein echter Render erzeugt werden, ist das nach
  [[70-QA/Quality Gates]] ein Blocker vor der Lieferung und keine Ausnahme, unter der
  weitergebaut wird.

Der Loop gehört in die Bauphase, nicht in die Abnahme. Er läuft vor dem
KI-Detail-Review aus [[20-Design/Anti AI Slop#Impeccable KI-Detail-Review]] und ersetzt
ihn nicht: Der Loop bringt die Fassung auf Qualität, der Review prüft sie gegen den
Befundkatalog.

## Der Render

Für jeden Durchgang gilt:

- **Ganzseitig, nicht nur der Auftakt.** Ein Render, der an der Falz endet, verbirgt
  Überlauf, Kollision, abgeschnittene Popover und Fehlerzustände weiter unten.[^fullpage]
- **Am laufenden Build**, nicht an einer Entwurfsdatei, einem Mockup oder einer
  Beschreibung.
- **An den Stopps, die vorher festgelegt wurden.** Prüfbreiten, Licht- und Dunkelmodus
  und weitere Zustände werden vor dem Durchgang benannt und dann alle erzeugt, nicht
  nachträglich ausgewählt.
- Erzeugt wird über ein Browserwerkzeug des Agenten. Fehlt eines, ist das ein
  dokumentierter Blocker nach [[70-QA/Quality Gates]] und kein Grund, den Loop zu
  überspringen.

## D0 Stilkachel: das visuelle Ziel vor dem ersten Bauteil

Ein Modell ohne konkretes visuelles Ziel erzeugt die wahrscheinlichste Lösung. Das
Brain setzt dem bewusst **kein externes Live-Vorbild** entgegen: Bei genau einer
Website bleibt es nach [[90-References/Reference Research Workflow]] beim
Eigenentwurf. Das Ziel entsteht deshalb im Projekt selbst, und es entsteht als Bild.

Vor dem Auftaktfeld und vor der ersten echten Komponente wird der Tokenvertrag aus
[[20-Design/Color System#Tokenvertrag]] als **eine gerenderte Seite** ausgegeben und
angesehen. Die Stilkachel zeigt an realem Text der Website:

- jede Pflichtfarbrolle als Fläche mit dem Text, der real darauf steht, in Licht und
  Dunkel;
- die Type Ramp aus [[20-Design/Typography Layout and Spacing]] mit echten
  Überschriften und einem echten Absatz, nicht mit Blindtext;
- die gewählte Radius-, Rahmen- und Tiefengrammatik an je einem Beispiel;
- die primäre und sekundäre Aktion in allen Zuständen, einschließlich `focus-visible`,
  Laden und deaktiviert;
- die gewählte Grundform für Inhalte nach
  [[30-Frontend/Components and UI States#Kartenentscheidung]], also Karte, Zeile,
  Tabelle oder Liste, mit Leer- und Ladezustand;
- das Signaturdetail nach [[20-Design/Landing Page Craft#Das Signaturdetail]].

**Die Stilkachel ersetzt eine Nachweispflicht, sie kommt nicht zu ihr hinzu.** Wo der
Design Contract bisher Werte je Rolle aufzählte, verweist er künftig auf die gerenderte
Kachel und trägt nur noch die Herleitung. Eine Tabelle gesetzter Werte belegt nicht,
dass `text-tertiary` auf `surface-alt` lesbar ist; die Kachel zeigt es.

Findet ein Befund an der Kachel statt, wird er dort behoben, bevor ein Auftakt gebaut
wird. Ein Tokenfehler, der erst an der fertigen Seite auffällt, ist bereits über alle
Komponenten verteilt.

Die Kachel liegt außerhalb des Produktionscodes und wird nicht ausgeliefert.

## Divergenz vor Konvergenz: das Auftaktfeld

Vor der Konvergenz steht die Auswahl, und die Auswahl entsteht am Bild.

Für die Landing Page jeder gebauten Website werden **zwei bis drei Auftaktfassungen
tatsächlich gebaut und gerendert**, bevor eine weiterverfolgt wird.

- Jede Fassung wählt eine **andere Komposition** aus dem
  [[20-Design/Landing Page Craft#Auftakt-Repertoire]] und besetzt alle sechs Rollen aus
  [[20-Design/Landing Page Craft#Der Auftakt: sechs Rollen, eine Komposition]].
- Alle Fassungen verwenden **dieselben realen Inhalte, Fakten und Bilder**. Verglichen
  wird die Komposition, nicht der Textaufwand.
- Die Aufgabe an den Bauschritt bleibt für das Aussehen bewusst offen und für die
  Bedingungen hart: Responsivität, Systemkonsistenz, Tokenvertrag und Inhaltswahrheit
  sind gesetzt, die Gestaltung ist es nicht.[^openprompt]
- **Die Anzahl wird ausdrücklich verlangt.** Ohne die Ansage, alle Fassungen zu bauen,
  liefert ein Modell eine und hat damit die Auswahl bereits für sich entschieden.[^askforn]
- Die Fassungen werden nebeneinander bei 375 und 1280 Pixel angesehen. Gewählt wird
  die, die die drei Zeitfenster aus [[20-Design/Landing Page Craft#Die drei Zeitfenster]]
  am besten besteht, nicht die ungewöhnlichste.
- Wahl, verworfene Fassungen und Grund stehen im Design Contract. Die verworfenen
  Fassungen sind Arbeitsmaterial, liegen außerhalb des Produktionscodes und werden
  nicht ausgeliefert.

**Das ist keine Auswahlvariante im Sinne von
[[00-Start/05 Web Product Workflow#Anzahl der Websites]].** Dort geht es um
vollständige, gleichwertig auslieferbare Websites. Hier geht es um ein einzelnes
Bauteil einer einzigen Website im Entwurfsstadium. Das Werkzeug dafür ist der Skill
`prototype` nach [[00-Start/04 Plugins and Skills#Prototype]]; seine Einsatzgrenze
„nur für einzelne Bauteile, Auftaktkompositionen und Interaktionsmuster" gilt
unverändert und wechselt nur von optional auf verbindlich.

Dasselbe Vorgehen ist für jedes weitere Bauteil zulässig, dessen Grundform noch offen
ist, etwa die Kartenentscheidung nach
[[30-Frontend/Components and UI States#Kartenentscheidung]]. Verbindlich ist es nur für
den Auftakt.

## Pflichtdurchgänge

Mindestens drei Durchgänge je gebauter Website, nach der Wahl der Auftaktfassung und
vor dem KI-Detail-Review. Jeder Durchgang hat eine eigene Frage; sie werden nicht
vermischt.

| Durchgang | Frage | Stopps | Woran gearbeitet wird |
|---|---|---|---|
| **D1 Komposition** | Stimmt die Grundordnung, bevor ein Detail verbessert wird? | 375, 1280 | Auftaktrollen besetzt, Inhaltsanker sichtbar, Fortschritt erkennbar, Abschnittsfolge aus realen Nutzerfragen, Kopfzeilenanteil an der ersten mobilen Bildschirmhöhe |
| **D2 Rhythmus und Hierarchie** | Ist die Seite gegliedert oder nur gefüllt? | 375, 768, 1280 | Abstandsrhythmus eng in der Gruppe und weit zwischen Gruppen, Abstand über der Überschrift größer als darunter, Maßstabssprünge, Anzahl der Überschriftenanordnungen, Flächen- und Rahmengrammatik, optische statt mathematischer Ausrichtung, typografischer Feinschliff nach [[20-Design/Typography Layout and Spacing#Typografischer Feinschliff]] |
| **D3 Zustand und Detail** | Ist die Seite fertig oder nur im Ruhezustand fertig? | 375, 1280, 200 Prozent Zoom, Licht und Dunkel, sofern beide ausgeliefert werden | Fokus auf jedem realen Untergrund, Hover nur auf Auslösendem, Laden, Leer, Fehler, deaktiviert, Buttonhöhen, Touchziele, Kontrast in der realen Kombination, Layoutsprung beim Laden von Schrift und Auftaktmedium |

Weitere Durchgänge sind erlaubt und häufig nötig. Drei sind die Untergrenze, nicht das
Ziel.

Bei mehreren gebauten Websites läuft der Loop je Website getrennt. Ein gemeinsamer
Durchgang über alle Fassungen genügt nicht, weil sie unterschiedliche Art Directions
haben.

## Wie ein Befund formuliert wird

Ein brauchbarer Befund benennt Ort, Beobachtung und Änderung. Eine Wertung allein ist
kein Befund.

- Unbrauchbar: `Der Auftakt wirkt noch etwas generisch.`
- Brauchbar: `Auftakt bei 375: H1 belegt vier Zeilen, die primäre Aktion rutscht unter
  die Kante. Satz kürzen, Display-Obergrenze von 4.5rem auf 3.5rem.`

Typische brauchbare Befunde sind bewusst banal: Der Abstand ist zu eng, die Kachelreihe
ist zu dicht zum Überfliegen, ein Pfeil stößt an den Rand, dieses Element wird zur
vertikalen Liste. Solche Sätze sind an einem Bild sofort zu treffen und im Quelltext
fast nie.[^concretefeedback]

Befunde sind ortsgebunden und möglichst parametrisch: Sie benennen das eine Element und
den Wert, der sich ändert, statt einen ganzen Abschnitt neu zu beschreiben. Ein Entwurf
wird verstellt, nicht neu geschrieben.[^tweaks] Dieselbe Bewegung liegt bei ChatGPT
Sites als Annotation direkt auf dem gerenderten Element.[^annotation]

Befunde aus dem Loop gehören in das Decision Log des Projekts, nicht in den Change Log
des Brains. Nur ein **wiederholt** auftretender Befund wird nach
[[00-Start/03 Update Protocol]] als Regel zurückgeführt; der Ort dafür ist
[[20-Design/Anti AI Slop#Slop-Signaturen]] oder die zuständige Fachnotiz.

## Abbruchregel

Der Loop endet, wenn einer der Fälle eintritt:

- Ein Durchgang erzeugt keinen Befund mehr, der eine Entscheidung ändert.
- Die verbleibenden Befunde sind bewusste Entscheidungen und stehen mit Grund im Design
  Contract.
- Die Änderungen eines Durchgangs machen die Seite nicht mehr besser, sondern nur noch
  anders. Dann wird der letzte Stand behalten.

Der Loop ist kein Freibrief für unbegrenzten Aufwand. Er verschiebt Arbeit von der
Nachweisproduktion in die Gestaltung; er kommt nicht zu ihr hinzu.

## Nachweis

Je gebauter Website im Projekt, nicht im Brain:

- die gerenderte Stilkachel aus `D0` samt der daran behobenen Befunde;
- die gebauten Auftaktfassungen mit gewählter Komposition, Wahl und Grund;
- je Durchgang Datum, Stopps, Befundliste und was daraufhin geändert wurde;
- die Renders, auf denen beurteilt wurde.

Dieser Nachweis ersetzt in [[70-QA/Quality Gates]] den bisherigen passiven Beleg
„Screenshots liegen vor". Vorhandene Renders ohne zugehörige Befundliste erfüllen das
Gate nicht mehr.

## Herkunft

Der Grundsatz stammt erstanbieterlich aus dem Codex-Forschungsteam von OpenAI: Ein
Modell arbeitet besser, wenn es seine eigene Arbeit prüfen kann, und dieses Prüfen war
bis zur multimodalen Werkzeugausstattung auf Backend-Code beschränkt. Für
Frontend-Arbeit ist es der eigentliche Qualitätsmechanismus, nicht eine
Zusatzprüfung.[^checkwork] Das Werkzeug dafür ist ein Browser, den der Agent während
der Arbeit selbst bedient.[^browsertool]

Die Trennung in Divergenz am Bild und anschließende Konvergenz ist an derselben Quelle
belegt: Eine einzelne Bildschirmaufgabe erzeugt mehrere nebeneinander gerenderte
Fassungen, zwischen denen im selben Vorgang umgeschaltet wird; die Auswahl erfolgt am
Bild, nicht an der Beschreibung.[^codexvariants]

Beide Anbieter empfehlen ausdrücklich, dem Modell ein Bild als Ziel zu geben, etwa
einen Screenshot oder ein Mockup.[^mockinput] Das Brain folgt dem im Mechanismus, nicht
in der Quelle: Das Ziel ist die projekteigene Stilkachel und das eigene Auftaktfeld,
nicht eine fremde Live-Seite. Die Regel gegen eine automatisch gewählte
Live-Leitreferenz bei genau einer Website bleibt damit unberührt; sie wird durch ein
intern erzeugtes Ziel beantwortet statt aufgehoben.

Claude Design von Anthropic Labs legt dieselbe Bewegung in die Oberfläche: Ein Entwurf
wird über offengelegte Parameter verstellt, an einem eingebauten Breakpoint- und
Themenumschalter beurteilt und über eine ortsgebundene Anmerkung an genau einem Element
korrigiert.[^tweaks]

[^checkwork]: `Build beautiful frontends with OpenAI Codex`, 00:00:04–00:00:45 und
00:07:37–00:08:19. Channing, Research Team Codex: „In the same way that I might check my
own work and make sure that things visually look the way I expect them to, we want to
have the model be able to do that in a tight iteration." und „We know models perform
better when they can check their own work. And previously we could only do that with
backend code, but now … we've also unlocked that for front-end coding." Transkript in
`.analysis/transcripts/` des Ingest-Workspaces, nicht im Vault.

[^browsertool]: Ebenda, 00:03:27–00:04:08: „They're using the Playwright MCP. So actually
giving the tool … the ability to open a browser and look at the web app. They're running
in their loop. They're able to have the model take a look at the application as they're
working on it and check its own work." Die konkrete Werkzeugwahl ist zeitkritisch und
gehört nach [[00-Start/04 Plugins and Skills]], nicht in diese Notiz.

[^fullpage]: Ebenda, 00:06:55–00:07:37: zwei Renders je Aufgabe, eine gängige
Desktop- und eine gängige Mobilbreite, jeweils als ganze Seite — „Even if it's not in
that above the fold section, you can still see if there's an error or some overlap."
Ergänzt um: „Our design team has like different stops. They want to make sure everything
looks good at. And so you can actually make that part of your prompt … and make sure you
check it before it gets PR."

[^codexvariants]: Ebenda, 00:06:13–00:06:55 („So it gave us a couple options to look
at.") sowie die Bildbelege: Die Aufgabe `Add Travel Log screen with stats` liegt als
`Version 1` bis `Version 4` mit je eigenem gerendertem Preview vor; die Aufgabenliste
führt dieselbe Aufgabe mehrfach und eine Zeile `2/4 versions`.

[^openprompt]: Ebenda, Bildbeleg des Aufgabentexts: „Add a third screen to the app called
Travel Log. It contains a bunch of stats. You can make them fun and interesting. These
are just some ideas. Make sure the app is responsive on mobile. And make sure the design
is also consistent with …" Das Aussehen bleibt offen, Responsivität und
Systemkonsistenz sind gesetzt.

[^mockinput]: `Claude Code best practices`, 00:16:12–00:16:52: „You can use screenshots
to guide and debug … You can always just grab a screenshot, paste it in, or if you have
a file somewhere that's an image you can just say hey Claude, look at this mock.png and
then build the website for me." Ebenda 00:07:09–00:07:49 für die Divergenz vor dem Bau:
„Instead of just diving in and starting to work, you can use Claude Code as a thought
partner … report back with like two or three different options? Don't start working,
don't start writing any files yet." Ergänzend
`Build beautiful frontends with OpenAI Codex`, 00:04:50–00:05:31: „It allows you to add
basically exactly as much fidelity as you want … you can do like a very thin sketch and
have the model fill in the details."

[^annotation]: `Building websites with ChatGPT Sites`, 00:08:21–00:09:45: „if I want to
make very focused edits, what we'll use is annotations … this allows me to select
individual items on that site." Ebenda 00:14:30–00:15:51 für den Prüfdurchgang am
laufenden Build: ein Ziel wie „review the site for ease of use for user feedback",
abgearbeitet „visually and back-end to understand any priority findings".

[^askforn]: `Building websites with ChatGPT Sites`, 00:04:12–00:04:54: „I really want
three different prototypes to be showcased in my output. So this is important because I
want to tell the model that not just one, don't pick one of these, pick all three."

[^oneshot]: `Make Work Flow - Streamline team engagement with Codex`, 00:11:45–00:13:08:
„one-shotting, which is like trying to build a fully working prototype in a single
prompt. I generally don't encourage that. It's really hard for Codex to get something
right on the first try. And so I encourage you to work with Codex … almost treat it like
it was a developer or someone on your team that you wanted to just help them get started
on the project, and then you can give feedback." Deckt sich mit dem Anti-Muster
`Single-shot „Go build the app" prompting` aus dem Bootcamp-Foliensatz.

[^mainwork]: Ebenda, 00:09:35–00:10:19: „This is most of my workflow with front design.
It's just taking screenshots and giving them to Codex." Ebenda 00:17:57–00:18:37 zur
Eigenprüfung des Agenten am laufenden Build: „Codex is actually inspecting the site
itself … it's actually doing a visual inspection of the site."

[^concretefeedback]: Ebenda, 00:18:37–00:19:22 zur ortsgebundenen Anmerkung im Browser:
„I can annotate right in this browser … I can inspect the font, the color … and then I
can just add a comment here where I could say, make this bigger. I could add a comment
here that says, this arrow is bumping up against the side." Ebenda 00:15:13–00:15:54 zu
den Befunden am ersten Wurf: „these look really dense. I'm having a hard time scanning
through it. This kind of spacing is kind of crazy."

[^tweaks]: `Introducing Claude Design by Anthropic Labs`, 00:12–00:57. Das Video trägt
keine Sprache; belegt sind die Bildinhalte: ein `Tweaks`-Panel mit direkt verstellbaren
Parametern statt Neu-Prompt, ein `Knobs`-Panel mit gesetzten Werten für Familie, Größe,
Gewicht, Laufweite, Zeilenabstand und Radius, Umschalter `DARK | LIGHT` und
`DESKTOP | TABLET | MOBILE` bereits während des Entwurfs, sowie ein ortsgebundener
Kommentar an einem einzelnen Element. Das Werkzeug ist hier nicht installiert und wird
nicht vorausgesetzt; übernommen ist ausschließlich das Prinzip.
