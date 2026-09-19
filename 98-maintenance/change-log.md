---
type: maintenance
status: canonical
updated: 2026-09-19
---

# Change Log

> [!important] Geltung
> Diese Datei fuehrt die letzten zwanzig Eintraege. Aeltere Eintraege stehen vollstaendig in der Git-Historie: `git log --follow 98-maintenance/change-log.md` zeigt sie mit Diff und Datum, `git log --oneline` die Entscheidungen seit dem Umbau vom 19.09.2026.
>
> Ein Change-Log-Eintrag ist keine Abschlussbedingung mehr. Das Aenderungsprotokoll des Vaults ist die Commit-Historie; die Commit-Konvention aus `AGENTS.md` verlangt eine Betreffzeile, die die kanonische Aenderung benennt, und einen Body mit der Begruendung. Ein Eintrag hier entsteht nur noch fuer Entscheidungen, deren Begruendung laenger lebt als der Diff: eine gekippte Regel, eine verworfene Alternative, eine Recherchebasis.
>
> Eintraege vor dem 2026-08-06 sind historische Herkunftsnachweise. Wo aeltere Eintraege feste Websitezahlen, Auswahlvarianten, Asset-Ausschluesse, starre Navigationsgrenzen, verpflichtend hohe Motion, Pflichtinteraktionen oder pauschale Farb-, Schrift-, Kicker-, Schatten- und Retroverbote nennen, sind sie durch die neueren kanonischen Regeln ausdruecklich ueberholt.

## 2026-09-11 — Der Render wird Arbeitsmittel: Visual Iteration Loop als kanonische Notiz

Auslöser war die Frage des Nutzers, warum Websites, die KI-Agenten mit diesem Brain als Second Brain bauen, gestalterisch noch nicht professionell wirken. Ausgewertet wurden sieben Videos und ein Foliensatz von OpenAI und Anthropic Labs; fünf davon trugen zu dieser Änderung bei.

**Diagnose:** Das Wissen im Brain ist nicht die Ursache. [[20-design/landing-page-craft.md]], [[20-design/anti-ai-slop.md]] und [[20-design/typography-layout-and-spacing.md]] sind fachlich stark und belegt. Die Lücke lag zwischen Wissen und Ausführung, an drei Stellen:

1. **Der Render war nur Nachweis.** In [[70-qa/quality-gates.md]] stand „Screenshots liegen für die vorgeschriebenen Prüfbreiten vor". Nirgends stand, dass der Agent den Render ansieht, beurteilt und daraufhin korrigiert. Die einzige dokumentierte Schleife war der Impeccable-Review, der genau einmal nach der Implementierung läuft. Das ist eine Prüfung, keine Konvergenz. Ein Entwurf, der alle Regeln erfüllt, ist der erste Entwurf; die professionelle Anmutung entsteht in den Durchgängen danach.
2. **Es gab keinen Divergenzschritt.** Das [[20-design/landing-page-craft.md#Auftakt-Repertoire]] bietet zehn Kompositionen an, aber keine wurde je gebaut und angesehen. Die Wahl fand rein gedanklich statt, und ein Sprachmodell wählt dabei die wahrscheinlichste Lösung. Das ist genau die Ursache, die [[20-design/landing-page-craft.md#Professionell gegen generiert]] selbst benennt.
3. **Es gab kein visuelles Ziel.** Der Tokenvertrag wurde als Werteliste dokumentiert, nie als Bild geprüft. Eine Tabelle belegt nicht, dass `text-tertiary` auf `surface-alt` trägt.

**Kanonisch neu**

- [[20-design/visual-iteration-loop.md]] ist der neue kanonische Besitzer dafür, **durch welche Arbeit** eine gebaute Oberfläche ihre Qualität erreicht. Die Notiz führt den Loop `rendern -> ansehen -> benennen -> ändern`, den Schritt `D0 Stilkachel`, das Auftaktfeld, drei Pflichtdurchgänge, die Befundform, eine Abbruchregel und die Nachweisform.
- **`D0 Stilkachel`**: Vor der ersten Komponente werden Tokenvertrag, Type Ramp, Radius-/Rahmen-/Tiefengrammatik, Aktionszustände, gewählte Inhaltsgrundform und Signaturdetail als **eine gerenderte Seite** ausgegeben und angesehen, in Licht und Dunkel, an echtem Text. Sie ersetzt die Werteaufzählung im Design Contract, sie kommt nicht zu ihr hinzu; [[20-design/color-system.md#Tokenvertrag]] gilt erst als erfüllt, wenn er gerendert wurde.
- **Auftaktfeld**: Zwei bis drei Auftaktfassungen mit verschiedenen Kompositionen und denselben realen Inhalten werden tatsächlich gebaut und nebeneinander bei 375 und 1280 Pixel beurteilt. Die Anzahl wird ausdrücklich verlangt, sonst entscheidet das Modell die Auswahl für sich. `prototype` wechselt in [[00-start/04-plugins-and-skills.md#Prototype]] von optional auf für das Auftaktfeld verbindlich; seine Grenze auf einzelne Bauteile bleibt unverändert, ein Auftakt ist keine Website.
- **Drei Pflichtdurchgänge** `D1 Komposition`, `D2 Rhythmus und Hierarchie`, `D3 Zustand und Detail`, je Website getrennt, jeder mit benannten Stopps und schriftlicher Befundliste aus Ort, Beobachtung und Änderung. Ein Render ohne Befundliste ist kein Durchgang.
- **Rendernachweise sind ganzseitig**, nicht nur bis zur Falz. Überlauf, Kollision, abgeschnittene Popover und Fehlerzustände liegen unterhalb des sichtbaren Auftakts. Ergänzt in [[70-qa/test-matrix.md]] und [[70-qa/quality-gates.md]].
- Der Loop läuft **vor** dem KI-Detail-Review und ersetzt ihn nicht: Der Loop bringt die Fassung auf Qualität, der Review prüft sie gegen den Befundkatalog. Ein Review auf einer Fassung ohne Durchgänge verbraucht die teurere Prüfrunde für Befunde, die der Loop selbst beseitigt hätte.
- Propagiert durch `AGENTS.md`, [[00-start/01-core-rules.md]], [[00-start/00-brain-index.md]], [[00-start/02-routing-map.md]] mit zwei neuen Zeilen, [[00-start/03-update-protocol.md]], [[00-start/04-plugins-and-skills.md]], [[00-start/05-web-product-workflow.md]] mit neuem Schritt 9, [[20-design/landing-page-craft.md]], [[20-design/anti-ai-slop.md]], [[20-design/design-direction.md]], [[20-design/color-system.md]], [[70-qa/quality-gates.md]] mit drei neuen G1-Prüfpunkten, [[70-qa/test-matrix.md]], [[80-templates/project-master-spec.md]], [[80-templates/ai-build-prompt.md]] und [[98-maintenance/coverage-and-impact-map.md]].

**Konflikt und wie er entschieden wurde**

Beide Anbieter empfehlen erstanbieterlich, dem Modell ein Bild als Ziel zu geben, etwa einen Screenshot oder ein Mockup in frei wählbarem Detailgrad. Das steht in Spannung zur Regel, bei genau einer Website keine Live-Leitreferenz zu wählen. **Die Referenzregel bleibt unverändert.** Übernommen wird der Mechanismus, nicht die Quelle: Das visuelle Ziel entsteht projektintern als `D0 Stilkachel` und als gebautes Auftaktfeld. Begründung und Auslöser für eine erneute Prüfung stehen in [[98-maintenance/review-queue.md]]. Der Nutzer hat die Entscheidung ausdrücklich dem Agenten überlassen.

**Nicht geändert:** Referenzquote und Referenzmodus, Anzahl der Websites, Beweis-Hierarchie, Textbudgets, Motion-Budget, Stilprofile und Leitbenchmarks, Rechts-, Sicherheits- und Betriebsregeln. Bestehende Projektartefakte wurden nicht angefasst.

**Als Anschlussidee vorgemerkt, nicht übernommen:** Dieselbe Quelle führt eine `design.md`, die aus Screenshots eines gelungenen Zustands erzeugt und bei jeder Rückmeldung fortgeschrieben wird, damit wiederkehrende Gestaltungskritik nicht in jeder Sitzung neu entsteht. Das Brain besitzt mit dem Design Contract und der `D0 Stilkachel` bereits zwei Träger dieser Funktion; ein dritter Speicher würde die kanonische Eindeutigkeit verletzen. Ob der Design Contract künftig aus der Kachel erzeugt statt von Hand gefüllt wird, ist in [[98-maintenance/review-queue.md]] als offene Frage vermerkt.

**Bewusst nicht gelöst:** Das Design- und Frontend-Layer enthält in allen vierzehn Notizen **keinen einzigen Codeblock**. Es fehlt jede Referenzimplementierung dafür, wie Tokenvertrag, Radiusgrammatik oder Auftakt konkret als HTML und CSS aussehen. Die `D0 Stilkachel` löst das je Projekt, nicht im Brain. Als offener Punkt mit Auslöser in [[98-maintenance/review-queue.md]] eingetragen, weil ein mitgeliefertes Beispiel leicht als Pflichtaussehen gelesen wird — derselbe Fehler, den [[20-design/interface-benchmarks.md#H0 Handwerksuntergrenze]] bei B5 bereits einmal korrigieren musste.

**Quellenbasis:** `Build beautiful frontends with OpenAI Codex` (Romain Huet und Channing aus dem Codex-Forschungsteam, erstanbieterlich), `Claude Code best practices` (Anthropic), `Introducing Claude Design by Anthropic Labs` (ohne Sprache, rein visuell ausgewertet), `Building websites with ChatGPT Sites` (OpenAI Solutions Engineering) und `Slides - Virtual Builder Bootcamp Codex` vom Juni 2026. Alle Zeitmarken in den Fußnoten sind gegen die erzeugten Transkripte geprüft. Dazu `Make Work Flow - Streamline team engagement with Codex`, das den vollständigen Frontend-Ablauf eines OpenAI-Mitarbeiters zeigt und den Loop unabhängig bestätigt: „This is most of my workflow with front design. It's just taking screenshots and giving them to Codex.", die Ablehnung des One-Shot-Baus, die ortsgebundene Anmerkung im Browser und die Eigenprüfung des Agenten am laufenden Build. Nicht eingeflossen sind `How marketing teams use Codex` und `OpenAI - How our marketing team uses ChatGPT Work`: beide behandeln Kampagnen-Briefings, Mood Boards, synthetische Kundenprofile und Anzeigen-Assets, nicht die Gestaltung von Websites. Das erste liegt koreanisch vor und wurde maschinell übersetzt; sein Wortlaut ist deshalb ausdrücklich nicht zitierfähig und wurde für keine Regel herangezogen. Beide wurden vollständig transkribiert und durchgesehen, bevor sie verworfen wurden.

Transkripte, Frames und Evidenzdateien liegen außerhalb des Vaults im Ingest-Workspace und wurden nicht committet.

**Graphify neu gebaut.** Die inkrementelle Erkennung meldete genau die 19 geänderten Dateien. Der Graph umfasst jetzt **1816 Knoten, 2500 Kanten, 11 Hyperkanten und 140 Gemeinschaften**, gegenüber 1202/1990/10/79. Die Integritätsdiagnose meldet keine hängenden, fehlenden, doppelten, kollabierten oder Selbstschleifen-Kanten. Sechs neue Gemeinschaften tragen die Themen dieser Änderung: `Visual Iteration Loop`, `D0 Stilkachel`, `Auftaktfeld: Divergenz vor Konvergenz`, `Pflichtdurchgänge und Rendernachweis`, `Impeccable KI-Detail-Review` und `Feinschliff am Render`.

**Shrink-Schutz ist im ersten Anlauf angesprungen und war berechtigt.** Der erste Extraktionsdurchgang hätte den Graphen auf 1057 Knoten verkleinert. Die Prüfung nach der Graphify-Regel ergab: Die unberührten Dateien blieben vollständig (818 auf 816, reine Deduplizierung), der Verlust lag ausschließlich bei den 19 neu extrahierten Dateien (384 auf 241). Ursache war die Extraktionsgranularität dieses Laufs, nicht der Notenstand: Der vorherige Lauf hatte **jede Tabellenzeile als eigenen Knoten** geführt, etwa jede Slop-Signatur, jede Auftaktkomposition und jede Zeile der Zuständigkeitstabelle, während der erste Durchgang eine Tabelle zu einem Knoten mit vielen Kanten zusammenfasste. Für Abfragen nach dem kanonischen Besitzer einer einzelnen Regel wäre das ein Rückschritt gewesen. `graph.json` wurde deshalb aus der Sicherung wiederhergestellt und mit vorgegebenen Mindestdichten je Datei neu extrahiert; der zweite Lauf wächst auf 1816 Knoten. Der Shrink wurde nicht erzwungen.

**Zwei Artefaktbesonderheiten dieses Laufs.** Die Signaturdatei `.graphify_labels.json.sig` war mit 69 Einträgen gegenüber 140 Gemeinschaften veraltet und wurde neu erzeugt, damit ein späterer Lauf keine Bezeichnung einer inzwischen anders zusammengesetzten Gemeinschaft weiterverwendet. `GRAPH_REPORT.md` nennt in der Kopfzeile den absoluten Pfad des bauenden Rechners; er lautet jetzt `/home/andreas/Downloads/web-brain-update/web-brain` statt `/srv/Web-Design/web-brain`. Das ist erzeugter Berichtstext, keine Notizangabe, und ändert keine Pfadauflösung im Vault.

**Zur Quellenzuverlässigkeit:** Die Aussagen sind an Produktständen von Mitte 2026 belegt und teilweise werkzeugspezifisch. Übernommen wurde ausschließlich der Arbeitsvorgang, nicht die Werkzeugwahl; konkrete Werkzeuge bleiben in [[00-start/04-plugins-and-skills.md]] mit eigener Prüffrist.

## 2026-09-03 — Die Landing Page bekommt eine eigene kanonische Notiz

Auslöser war der Auftrag, den Grundaufbau von Landing Pages und die Unterscheidung zwischen professioneller und generierter Anmutung gründlich zu recherchieren und als kanonisches Wissen abzulegen, und dabei zugleich Komposition, Überschriftenanordnung und Kopfzeile für mehr gestalterische Freiheit zu öffnen.

**Diagnose:** Die Landing-Page-Regeln lagen bisher als ein Abschnitt in [[20-design/design-direction.md]] und beantworteten vor allem, was ein Auftakt nicht sein darf. Es fehlten der Aufbau der gesamten Seite, ein Entscheidungsraum für die Auftaktkomposition, eine Regel für die Anordnung der Überschriften über die Seite hinweg, eine Rolle für die Kopfzeile im Auftakt und ein prüfbarer Detailkatalog dessen, woran eine generierte Oberfläche tatsächlich erkannt wird. Ohne diesen Entscheidungsraum entsteht bei fehlender Vorgabe immer die wahrscheinlichste Lösung, und genau das ist die Ursache der generischen Anmutung.

**Kanonisch neu**

- [[20-design/landing-page-craft.md]] ist der neue kanonische Besitzer für Aufbau, Auftaktkomposition, Überschriftenanordnung, Kopfzeilenrolle, Beweisplatzierung, Handlungsdichte und die Abgrenzung zur generierten Anmutung der Startseite. Die Notiz führt drei Beurteilungszeitfenster, eine Tabelle erster Nutzerfragen und stärkster Beweisformen je Seitentyp, die sechs Auftaktrollen, ein Auftakt-Repertoire aus zehn Kompositionen, das Signaturdetail, eine Feinschliffliste und vierzehn Prüffragen.
- Zwei Rollen des Auftakts sind neu benannt und prüfpflichtig: der **Beweisanker**, der in generierten Auftakten fast immer fehlt, und der **Fortschritt**, ohne den ein sauber abschließender erster Bildschirm als vollständig gelesen wird.
- [[20-design/anti-ai-slop.md#Slop-Signaturen]] führt einen Detailkatalog aus rund sechzig konkreten Einzelmerkmalen, gegliedert nach Fläche, Typografie, Farbe, Aufbau, Bewegung, Bild und Copy. Jede Zeile ist ein Befund mit Alternative, kein Verbot; bewusster Einsatz wird im Design Contract begründet.
- [[20-design/design-direction.md#Landing Page]] behält den Anker, enthält jetzt aber die Entscheidungen des Direction Briefs und verweist für die Herleitung auf die neue Notiz. Neu dort und in [[00-start/01-core-rules.md]]: zwei bis drei verschiedene Überschriftenanordnungen je Seite, größerer Abstand über als unter einer Überschrift, Faktor 1,25 zwischen benachbarten Typostufen, ein hergeleitetes Signaturdetail je Website.
- [[30-frontend/components-and-ui-states.md#Kopfzeilen-Repertoire]] öffnet die Kopfzeile als Art-Direction-Entscheidung mit acht Formen von der durchgehenden Leiste bis zur erst ab dem zweiten Bildschirm erscheinenden Kopfzeile, mit Höhenbudget und Aktionsregel.
- [[20-design/typography-layout-and-spacing.md#Typografischer Feinschliff]] ergänzt die Handwerksschicht, die zuerst auffällt: Umbruch, Schusterjungen, optischer Randausgleich, Ziffernform, Zeichensatz, Mindestgrößen, Blocksatz.
- Propagiert durch Brain Index, Routing Map, Core Rules, `AGENTS.md`, Information Density, Derived Design Patterns, Project Master Spec, AI Build Prompt, Quality Gates und Coverage and Impact Map. Die Quality Gates enthalten elf neue G1-Prüfpunkte zur Landing Page.

**Recherchebasis:** Erste Eindrücke innerhalb von 50 Millisekunden und die Wirkung von visueller Komplexität und Prototypikalität, die Verteilung der Betrachtungszeit über die Bildschirmhöhen, die Illusion der Vollständigkeit, das Aufmerksamkeitsverhältnis aus der Conversion-Centered-Design-Systematik, der Fünf-Sekunden-Test, zwei öffentlich dokumentierte Musterkataloge generierter Oberflächen sowie Kennwerte zu Auftaktmedium und Ladezeit. Die Belege stehen als Fußnoten in den jeweiligen Notizen mit Prüfdatum 3. September 2026.

**Nicht geändert:** Beweis-Hierarchie, Textbudgets, Referenzquote, Motion-Budget, Rechts- und Betriebsregeln. Bestehende Projektartefakte wurden nicht angefasst.

**Graphify neu gebaut.** Die inkrementelle Erkennung meldete 16 geänderte Notizen. Die Semantikextraktion lief in dieser Sitzung ohne Subagenten unmittelbar im Host, weil in dieser Umgebung keine Subagenten eingesetzt werden; der Skill sieht diesen Weg ausdrücklich vor. Die 306 bereits belegten Knoten und 765 Kanten dieser 16 Dateien wurden erhalten und um die neuen Landing-Page-, Slop-Signatur-, Kopfzeilen- und Feinschliffknoten ergänzt. Der Graph umfasst jetzt **1202 Knoten, 1990 Kanten, 10 Hyperkanten und 79 Gemeinschaften**, gegenüber 1116/1879/7/79. Die Integritätsdiagnose meldet keine hängenden, fehlenden, doppelten oder kollabierten Kanten. Ein Shrink trat nicht auf. Die Gemeinschaften wurden nach der neuen Zugehörigkeit neu benannt; sechs davon tragen jetzt die Landing-Page-Themen `Landing Page Craft`, `Auftakt-Repertoire`, `Die sechs Auftaktrollen`, `Slop-Signaturen`, `Kopfzeilen-Repertoire` und `Typografischer Feinschliff`.

## 2026-08-31 — Leserecht auf den Entdeckungswurzeln der Developer-Plattform

- [[60-operations/delivery-and-local-start.md]] hält jetzt fest, dass die Entdeckung `readdir` auf den drei Wurzelordnern ausführt und der ausliefernde Dienst dort Leserecht braucht. Mit `--x` allein bleibt der Bereich „Aktuelle Projekte" für alle Projekte zugleich leer, und der Fehler sieht wie ein einzelnes fehlendes Projekt aus.
- Gefunden beim Bau der Website für die Fahrschule Kladow unter `../projekte/fahrschule-kladow/`. Die ACL auf `/srv/Web-Design/projekte` gab `web-johannstein` und `owner-hosting` nur das Durchgangsrecht.
- Der nötige `setfacl`-Aufruf steht in der Notiz. Er ist eine Entscheidung des Nutzers und wurde nicht selbst gesetzt.

### Geprüfte Auswirkungen

Betroffen ist allein der Betriebsabschnitt zur Developer-Plattform. Regeln zu Design, Copy, Recht, Sicherheit und Owner-Hosting bleiben unverändert. Das in [[60-operations/owner-hosting-and-dashboard.md]] beschriebene Verhalten registrierter Buildprofile war bereits kanonisch und ist im Owner-Hosting jetzt umgesetzt; die Notiz brauchte dafür keine Änderung.


## 2026-08-27 — Nutzwert vor Stilintensität und eine referenzgeführte Fassung

Auslöser war die gemeinsame Durchsicht von fünf lokal gerenderten Startseiten desselben Fahrschulauftrags in zwei Entwicklungsständen. Die älteren, vom Nutzer bevorzugten Fassungen wurden nicht als neue Vorlage in das Brain kopiert. Extrahiert wurden nur die übertragbaren Gründe, warum ihre Startseiten im Groben überzeugender funktionieren.

**Diagnose:** Die stärkeren Auftakte verbinden eine lesbare Angebotsaussage sofort mit einem konkreten Inhaltsanker, etwa dem tatsächlichen Gegenstand des Betriebs oder einem nützlichen Rechner, und führen anschließend sichtbar zur nächsten Nutzerfrage. Schwächere Fassungen erzeugten Unterschiedlichkeit dagegen über ein dominantes Epochenzitat, typografische Übergröße, einen nur formal vorhandenen Bildblock oder einen Auftakt ohne konkreten Gegenstand. Eine Desktop-H1 wurde dabei angeschnitten, eine weitere Komposition kollidierte mobil mit der klebenden Kopfzeile. Die bisherige Pflicht zu einer anderen Live-Leitreferenz je Website und die Formulierung, eine Landing Page solle auffällig oder extravagant sein, belohnten diese Verschiebung von Nutzwert zu Stilabstand.

**Kanonisch neu**

- [[20-design/design-direction.md#Landing Page]] setzt Angebot, konkreten Inhaltsanker, primäre Handlung, vollständige H1-Lesbarkeit und den Übergang zur nächsten Nutzerfrage vor Stilintensität. Ein Bild ist optional; wenn es eingesetzt wird, muss es in Ausschnitt, Maßstab und Raster an der Aussage teilnehmen. Schriftgröße, leerer Weißraum und Retrograd sind allein kein Konzept.
- [[10-strategy/information-density-and-mobile-clarity.md]] verlangt, dass innerhalb der zweiten mobilen Bildschirmhöhe die nächste reale Nutzerfrage oder der erste Beweis beginnt. [[20-design/typography-layout-and-spacing.md]] schützt die einzige semantische H1 vor Anschnitt, Masken, Überlagerung und Kopfzeilenkollision. [[20-design/anti-ai-slop.md]] führt die entsprechenden Befunde und Erkennungsfragen.
- Ein starkes vollflächiges Epochenzitat bleibt möglich, ist aber eine Ausnahme. Es braucht einen ausdrücklichen Nutzerwunsch oder tragenden Markenbezug. Der Wunsch, mehrere Fassungen sichtbar zu unterscheiden, genügt nicht; ohne Nachweis bleibt historische Typografie ein begrenzter Akzent in einem gegenwärtigen System.
- [[20-design/design-direction.md#Stilabstand bei mehreren Websites]] bestimmt zuerst die gemeinsame sachlich beste Nutzstruktur und erst danach mindestens fünf wirksame Gestaltungsunterschiede. Derselbe grobe Landing-Page-Aufbau darf wiederkehren. Keine Fassung wird durch einen schwächeren Auftakt, fehlenden Inhaltsanker, unlesbare Übergröße oder stärkeren Retrograd künstlich abgesetzt.
- [[90-references/reference-research-workflow.md]] ersetzt die Regel vom 23. August 2026. Eine Einzelwebsite entsteht ohne automatisch ausgewählte Live-Leitreferenz als Eigenentwurf, sofern der Nutzer keine Referenz vorgibt. Bei zwei oder mehr Websites wird genau eine Fassung von genau einer fachlich stark passenden Originalseite geprägt; alle übrigen Fassungen sind Eigenentwürfe und übernehmen die Referenz nicht quer. Nur wenn trotz dokumentierter Suche keine starke Passung existiert, bleiben ausnahmsweise alle Fassungen Eigenentwürfe.
- Die neue Referenzquote und die Landing-Page-Nutzwertprüfung wurden durch AGENTS, Core Rules, Routing Map, Web Product Workflow, Website Reference Pool, Inspiration Catalog, Derived Design Patterns, Project Master Spec, AI Build Prompt, Quality Gates, Update Protocol und Coverage and Impact Map propagiert.

**Prüfbasis:** Alle fünf lokalen Startseiten wurden in echter Chromium-Darstellung bei 1440 und 375 Pixel aufgenommen und visuell verglichen. Geprüft wurden Auftakt, H1, Kopfzeile, Bild- oder Modulrolle, erste zwei Bildschirmhöhen und der Übergang in die Folgesektionen. Die archivierten Projekte selbst wurden nicht verändert.

**Graphify neu gebaut und Shrink-Schutz geprüft.** Die erste inkrementelle Semantikextraktion lieferte für 22 neu zu lesende Notizen 379 Knoten und 155 Kanten, während ihre bisherigen Dateianteile 566 Knoten umfassten. Ursache war kein entsprechender Inhaltsabbau, sondern die zu grobe Zusammenfassung weitgehend unveränderter Langabschnitte im Website Reference Pool, Inspiration Catalog und Change Log. Die Versöhnung erhielt deshalb die weiterhin belegten Katalog-, Quellen- und Historienknoten, entfernte 39 überholte Konzeptknoten der alten Regeln `primäre Leitreferenz je Website`, `verschiedene Referenz je Website` und `Eigenentwurf nur als Fallback` und ergänzte die neuen Referenzquoten-, Nutzwert-, H1-, Bildrollen- und Mobilfortschrittsbeziehungen. Der aktuelle Graph umfasst **1114 Knoten, 1872 Kanten, 13 Hyperkanten und 81 Gemeinschaften**, gegenüber 1031/1686/5/69. Der einzige anschließende Rückgang um einen Knoten und eine Kante entfernt den geschlossenen Eintrag `Offene Wartungsschuld` aus der Review Queue; ein ungeprüfter Shrink wurde nicht erzwungen. Der neue Graph bildet den vollständigen Notizenstand ab.

## 2026-08-24 — Was überall wirkt, wird nicht überall bearbeitet

Auslöser war eine Liste von Beobachtungen am Hosting-Dashboard: Seitenränder, die beim Wechsel auf „Bearbeiten“ um 140 px nach außen sprangen; ein Vorwahlfeld, in dem „+49“ am Dreieck klebte; Rückgängig-Pfeile über einem Formular, in dem sie nichts Benennbares zurücknehmen; ein Knopf zum Zurückholen eines verworfenen Entwurfs, der als Nebensatz im leeren Zustand stand; und die Frage, warum Textänderungen nicht sofort und nicht an allen Stellen wirken.

**Diagnose:** Der Editor bot jede Stelle an, die reiner Text ist. Für einen Satz über den Betrieb ist das richtig und für die Kopfzeile falsch — was dort steht, steht auf jeder Seite, und wer den Menüpunkt „Kontakt“ antippt, ändert ihn zugleich in der Schublade, in der Fußzeile und in der Sprungmarke für Bildschirmleser, sieht aber nur die eine Stelle. Umgekehrt fehlte für die wenigen Angaben, die man beiläufig ändern können soll, jeder Weg: Die Zahl der Fahrlehrer im Team war überhaupt kein Feld. Und der Rückgängig-Stapel legte den ganzen Entwurf ab, nahm also beim Drücken auch zurück, was seither zentral geändert worden war.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Was auf keiner Website bearbeitet wird]]: Kopfzeile, Navigation und Menü, die Seitenliste der Fußzeile, `address`, Anruf- und Mailverweise, die Namen von Impressum, Datenschutz, AGB und Widerruf sowie Angaben für Suchmaschinen und Technik sind für **jede** gehostete Website gesperrt. Die Liste liegt als Code im Owner-Hosting, nicht im Vertrag: Eine neue Hosting-Subdomain soll sie nicht erst eintragen müssen. Ein Vertrag ergänzt sie über `gesperrt`, hebt aber keine Regel auf. Eine gesperrte Stelle antwortet auf einen Klick mit ihrer Begründung — eine Stelle, auf die gar nichts passiert, sieht aus wie ein Fehler und nicht wie eine Entscheidung.
- **Kopfzeilen werden nicht bearbeitet, Impressum und Datenschutz nicht umbenannt.** Das erste, weil eine Änderung dort überall zugleich wirkt und man ihren Umfang nicht sehen kann; das zweite, weil eine Seite, die nicht so heißt, für ihre Pflicht nicht auffindbar ist. Beides ist keine Vorsicht, sondern eine Entscheidung.
- **Das Logo wird nicht ersetzt.** Es steht in Kopfzeile, Menü, Fußzeile, als Favicon und im Vorschaubild — vier bis fünf Stellen, von denen der Editor eine kennt. Ein Fahrzeugbild ist der Gegenfall: ein bis zwei Stellen, ein Feld, ein Handgriff. Daraus die Faustregel in [[80-templates/owner-hosting-website-contract.md#Das Logo wird nicht ersetzt, Fahrzeugbilder schon]]: hochladen darf der Owner ein Bild, das ein bis zwei Stellen hat und keine Marke ist.
- **Der Copyright-Hinweis steht immer**, auch wenn „©“ in der Vorlage fehlt oder in der Schrift nicht darstellbar ist; dann tritt „(c)“ an seine Stelle, nicht eine Lücke. Er gehört zur Rechtszeile der Fußzeile und ist mit ihr gesperrt. Eine Fußzeile ohne ihn gilt als unvollständig, nicht als schlicht.
- [[60-operations/owner-hosting-and-dashboard.md#Der Owner ändert nichts Tiefgreifendes ohne Freigabe]]: Zentrale Angaben werden dreifach abgestuft — mit Rechtswirkung (Formular plus bestätigte Prüfung), ohne Rechtswirkung (Formular, auf Wunsch auch auf der Seite), gesperrt (nur Builder-Auftrag). Die Zuordnung ist Vertragssache und steht im Code, nicht in der Oberfläche.
- **`seite` am zentralen Feld** ([[80-templates/owner-hosting-website-contract.md#`seite` sagt, wo eine zentrale Angabe steht — und ob man sie dort anfassen darf]]): `stellen` sagt, wo der Wert auf der gebauten Seite erscheint, `form` in welcher Schreibweise, `bearbeitbar` ob er dort eingetippt werden darf, `grund` warum nicht. Damit erkennt der Editor auch Werte, die als Text nichts Besonderes sind — eine „6“ ist eine Sechs, die Zahl der Fahrlehrer im Team aber nur an ihrer Stelle.
- **Eine Änderung an einer Stelle wirkt an allen, und man sieht es dabei.** Zentrale Werte, die im Entwurf anders sind als im Release, werden im Rahmen fortgeschrieben — samt `href` bei Anruf- und Mailverweisen und `data-count` bei Kennzahlen. Ist `seite.bearbeitbar` gesetzt, erscheint an der Stelle ein Eingabefeld; gespeichert wird trotzdem zentral. Erlaubt nur für einfache Werte ohne Rechtswirkung, und die Grenze zieht der Server.
- **Der neue Typ `abende`** für wiederkehrende Termine mit einer gemeinsamen Zeit, und die Regel, dass eine **Anzahl nie ein eigenes Feld** ist: „drei Abende pro Woche“ ist die Länge der Liste und wird über `form: "anzahl"` daran gebunden. Ein zweites Feld dafür wäre genau die Stelle, an der Zahl und Liste auseinanderlaufen.
- [[60-operations/owner-hosting-and-dashboard.md#Zurücknehmen gehört zur Seite]]: Zurück, wieder vor und Vollbild stehen nur noch am Rahmen des Seiteneditors. Über einem Formular mit benannten Feldern nimmt ein Pfeil etwas zurück, das man nicht benennen kann — dort stellt man das Feld zurück. Ein Schritt merkt sich außerdem seinen Bereich und stellt nur ihn wieder her; vorher verlor er zwischenzeitliche zentrale Änderungen mit.
- [[60-operations/owner-hosting-and-dashboard.md#Verworfen heißt im Papierkorb, nicht weg]]: Ein verworfener Entwurf geht in einen Papierkorb — genau einer je Website — und steht unter „Veröffentlichen“ oben als eigener Kasten mit Zurückholen und Endgültig löschen. Vorher war er ein Pfeil, dessen Tooltip man lesen musste, um zu wissen, dass er die Rettung ist.
- [[60-operations/owner-hosting-and-dashboard.md#Eine weitere Hosting-Subdomain kostet keine Anpassung]]: DNS, nginx samt Zertifikat, ein Eintrag in `OWNER_HOSTING_DASHBOARD_HOSTS` — mehr nicht. Der Dienst trägt jeden dort genannten Namen bei jedem Start ein und entfernt Namen, die nicht mehr darin stehen; ein Dashboard unter einem abgeschalteten Namen wäre kein Rest, sondern eine offene Tür.

**Oberfläche:** Alle Dashboard-Seiten teilen sich jetzt eine Breite (1360 px, vorher 1080 auf Textseiten und 1360 im Editor) — ein Kopf, der beim Wechsel um 140 px springt, sieht aus wie zwei Programme. Das Vorwahlfeld schrumpft nicht mehr unter seinen Inhalt. Am Bild bleibt genau ein Bedienelement: der blau eingefärbte Knopf unten rechts, frühere Fassungen daneben; die zweite Leiste darüber mit demselben Knopf ist entfallen. Die Farbe der Auswahlumrandung sagt, womit man es zu tun hat: blau ändern, warngelb zentral, grau gesperrt.

## 2026-08-23 — Eine konkrete Leitreferenz je Website statt Designsammlung

Auslöser war der Wunsch, die bereits gespeicherten positiven Designbeispiele und fünf große Designsammlungen wirksamer für neue Website-Builds zu nutzen. Ein Agent soll nicht nur allgemeine Muster lesen, sondern je gebauter Website eine fachlich passende Originalseite auswählen und deren Grundstruktur, Gestaltung und zweckvolle Motion in frei gewählter Tiefe adaptieren. Bei drei Websites entstehen drei unterschiedliche Referenzentscheidungen; fehlt eine starke Passung, bleibt ein kreativer Eigenentwurf richtig.

**Kanonisch neu**

- [[90-references/website-reference-pool.md]] bündelt mehr als hundert direkt aufrufbare Originalseiten nach lokalen Dienstleistungen, Gastronomie und Hospitality, Gesundheit, Immobilien und Architektur, Mobilität und Logistik, Software und Finanzen sowie Studios und immersive Erlebnisse. Die fünf Sammlungen stehen nicht im aktiven Auswahlbestand; sie sind nur als datierte Herkunftsnachweise erhalten.
- [[90-references/reference-research-workflow.md]] ersetzt die bisherige Acht-Referenzen-/Drei-Rollen-Pflicht. Pro Website wird nach einem kurzen fachlichen Vergleich genau eine konkrete Leitreferenz gewählt. Passung wiegt stärker als Spektakel; unter ähnlich passenden Kandidaten wird die professionellere und sinnvoll animationsreichere Seite bevorzugt.
- Die Übernahmetiefe bleibt bewusst offen: `punktuell`, `teilweise` oder `prägend`, optional grob in Prozent. Dokumentiert werden Folgen für Auftakt, Raster, Dramaturgie, Typografie, Flächen, Medien und Motion sowie bewusste Abweichungen. Projektwahrheit, Brain-Regeln, reale Marke, Accessibility und Technik bleiben verbindlich.
- Mehrere Websites desselben Auftrags verwenden verschiedene Originalseiten. Galerie-, Award-, Stilbibliotheks- und Sammlungsseiten sind keine Leitreferenzen. Gibt es keine starke fachliche und gestalterische Passung, werden die geprüften Kandidaten begründet verworfen und als `Eigenentwurf` weitergearbeitet.
- Die Regel wurde in AGENTS, Core Rules, Brain Index, Routing, Web Product Workflow, Design Direction, Inspirationskatalog, Project Master Spec, AI Build Prompt, Quality Gates und Impact Map durchgezogen.

**Recherchegrenze:** Die Sammlungen und darin gelistete Websites können sich ändern. Der Pool ist ein Suchindex, kein eingefrorener Qualitätsbeweis. Vor einer konkreten Übernahme wird die Originalseite mit Desktop, Mobil, Tastatur und Reduced Motion erneut geprüft; interaktive Behauptungen benötigen ein Interaktionsprotokoll.

## 2026-08-23 — Bearbeiten am Ort der Sache: Seiteneditor, zwei Ansichten, der Entwurf als Sache

Auslöser waren drei Aufträge zum Hosting-Dashboard: die Landesvorwahl im geschlossenen Feld kürzen, gespeicherte Entwürfe wieder löschbar machen und den Inhalte-Mechanismus so umbauen, dass man ihn beim ersten Ansehen versteht — Fahrzeugbilder heraus, zentrale Angaben zentral, alles Übrige unmittelbar auf der Seite, ähnlich wie in Figma.

**Diagnose:** Das Dashboard hatte **eine** Art zu ändern und behandelte damit zwei verschiedene Dinge gleich. Eine Telefonnummer steht an sieben Stellen der Website und gehört an eine Stelle gepflegt; ein Fahrzeugbild steht an genau einer Stelle und stand im selben Formular wie die Bürozeiten — weit weg von dem Ort, an dem man es sieht. Zweitens war der Entwurf kein Gegenstand, sondern ein Hinweissatz: Er entstand mit zwei Tastendrücken, wurde erwähnt, ließ sich aber nur loswerden, indem man jedes Feld von Hand zurückstellte. Drittens zeigte ein `select` geschlossen den vollen Optionstext, weil er das von sich aus nicht anders kann.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Bearbeiten: zwei Ansichten, eine Entscheidungsregel]]: Ein Bereich, zwei Ansichten, eine Entscheidungsregel — erscheint der Wert an mehreren Stellen der Website, ist er zentral; steht er an genau einer, gehört er auf die Seite. Die Zuordnung steht als `surface` am Feld, nicht in der Oberfläche. Ein Feld erscheint in genau einer Ansicht.
- [[60-operations/owner-hosting-and-dashboard.md#Der Seiteneditor]]: Die gebaute Website im Rahmen, jede Stelle anklickbar, Leiste für Ausrichtung, Textgröße und Versatz, Bildknopf unten rechts im Bild. Was entsteht, ist eine **Darstellungsregel** neben der Website, kein Eingriff in die Quelle. Der Anker ist eine Struktur, keine Textsuche; ersetzt wird nur reiner Text und maskiert; Gestaltung ist eine aufgezählte Liste, kein CSS; angewendet wird nach dem Bau und vor den Prüfungen; eine Regel ohne Stelle wird protokolliert statt den Bau abzubrechen. Zentrale Angaben werden im Editor benannt und verlinkt, nicht überschrieben — sonst änderte sich die Nummer an einer Stelle und im Impressum nicht.
- [[60-operations/owner-hosting-and-dashboard.md#Der Entwurf ist eine Sache, kein Zustand]]: Ein Entwurf je Website, beide Teile als vollständiger Satz in getrennten Spalten, geschrieben über **eine** Funktion. Sichtbar als Karte auf drei Seiten, dort weiterbearbeitbar und **verwerfbar**. Eine Vormerkung wird dagegen nicht bearbeitet, sondern zurück in den Entwurf geholt: Sie ist ein geprüfter Stand mit einem Termin, und an ihr zu ändern verbände die Prüfung von gestern mit dem Inhalt von heute.
- Die Vertragsvorlage ([[80-templates/owner-hosting-website-contract.md]]) ergänzt das Pflichtattribut `surface` samt Checklistenpunkten. [[80-templates/owner-hosting-website-contract.md#Änderungen auf der Seite sind kein Vertragsfeld]] hält fest, dass ein einzelner Satz auf einer Seite **nicht** als Vertragsfeld nachgetragen wird — die Quelle kennt ihn nicht als Feld, und ein Feld dafür wäre eine Erfindung.
- Drei Regeln kamen erst durch den Test im echten Browser dazu, weil sie ohne ihn unsichtbar bleiben: Der **Server** liefert den Index der Textstellen mit, statt den Browser raten zu lassen — Skripte der Website schreiben Text nach dem Laden um, und ein Editor, der aus dem fertigen Dokument liest, hielte den erzeugten Text für den ursprünglichen. Die **Adressen** der Website werden für den Rahmen umgebogen, sonst zeigt er die Seite ohne Gestaltung. Und der Rahmen braucht `X-Frame-Options: SAMEORIGIN` für diese eine Antwort sowie `frame-src 'self'` in der Richtlinie des Dashboards; fehlt eines davon, bleibt er leer, ohne Fehlermeldung.
- Der Entwurf trägt den **ganzen** Stand der Darstellungsregeln. Ohne diese Regel verschwände jede früher veröffentlichte Änderung beim nächsten Bau — der Entwurf wird nach dem Veröffentlichen gelöscht, gebaut wird aus der Quelle, und die kennt sie nicht.
- Die Landesvorwahl steht in der Liste mit dem Land dahinter und im geschlossenen Feld nur als Vorwahl. Die kurze Anzeige entsteht erst im Browser: Ohne Skript bliebe „+49“ stehen, während in Wahrheit Österreich gewählt ist — der volle Text ist dann länger, aber richtig.

**Propagation und Prüfung:** Umgesetzt in `projekte/owner-hosting` (neues `packages/core/darstellung.mjs`, `apps/dashboard/editor.mjs`, Migration `006_darstellung.sql`, Worker-Anwendung nach dem Bau). Der Anker-Zerleger wurde gegen eine unabhängige zweite Implementierung über sechs gebaute Seiten geprüft — 435, 344, 312, 268, 275 und 208 Elemente, keine Abweichung. Drei Prüfebenen: der Selbsttest (59 Prüfungen: Anker, Seitenpfade, Gestaltungsgrenzen, Maskierung, Stellen mit Markup, verwaiste Regeln, Stellenindex, Adressumbiegung, Rahmenauslieferung); ein Durchlauf über zwei Veröffentlichungen und einen Rollback (16 Prüfungen, darunter „die erste Änderung überlebt die zweite Veröffentlichung“ und „Rollback stellt den Stand mit erster, ohne zweite Änderung her“); und der Editor in einem echten Browser über das Chrome DevTools Protocol (27 Prüfungen: Auswahl, Leiste, Ausrichtung, Textgröße, Verschieben per Pfeiltaste, Zurücksetzen, Bildknopf, zentrale Angabe, Seitenwechsel, keine Konsolenfehler). Genau dieser dritte Weg hat die drei oben genannten Regeln überhaupt erst sichtbar gemacht. Der Graph wurde in dieser Änderung **nicht** neu gebaut und nichts gepusht.

## 2026-08-19 — Veröffentlichungsreife je Website und zweckbezogene Designfreiheit

Auslöser war der Auftrag, vor der Veröffentlichung einer Website nicht länger verteilte Restpunkte im Projekt, in sichtbarer Copy und in externer Infrastruktur suchen zu müssen. Zusätzlich sollte die Gestaltung nicht mehr durch feste Rezepte wie eine globale Anzahl von Kopfzeilenpunkten, obligatorische Interaktion oder pauschale Stilverbote eingeengt werden. Als Gegenprobe wurden die 37 vom Nutzer genannten Rocket-Sites-Auftritte strukturell untersucht.

**Diagnose:** Der bisherige Launch-Check begann zu spät. Preview-Sperren, Dummy-Ziele, unfertige Hinweise, noch nicht produktive Formulare und externe Konten konnten während des Builds entstehen, ohne an einer gemeinsamen Stelle je Website zusammenzulaufen. Gleichzeitig setzte das Brain einzelne Muster mit Professionalität gleich. Die Referenzgruppe zeigt dagegen fokussierte Einzweckseiten, umfangreiche B2B-Informationsarchitekturen, lokale Praxen, Beratung, SaaS und Recruiting mit sehr verschiedenen Navigations-, Bild-, Typografie- und Bewegungsentscheidungen. Gemeinsam sind vor allem verständlicher Zweck, erkennbare Belege, ein konsistentes System und echte Kontaktwege.

**Kanonisch neu**

- [[60-operations/release-readiness-register.md]] verlangt ab Projektbeginn ein eigenes `release-readiness/<website-slug>.md` je Website. Jede neue provisorische Sperre, Attrappe, sichtbare Unfertig-Aussage und noch nicht produktive Integration wird in derselben Änderung eingetragen und erst mit Produktionsnachweis geschlossen. Die neue [[80-templates/release-readiness-register.md|Vorlage]] trennt P0-Blocker, Owner-Entscheidungen und spätere Verbesserungen.
- Formulare gelten erst nach einem echten Ende-zu-Ende-Test als produktiv: realer Endpunkt, tatsächlicher Betreiberweg, korrekte Absender-/Antwortadresse, SPF/DKIM/DMARC soweit vorgesehen, Fehlerpfad, Retry oder Alert und ein eindeutiger Empfangsnachweis. Eine Erfolgsmeldung im Browser beweist keine Zustellung.
- Der Produktions-Cutover behandelt nginx `auth_basic`, Passwort-/IP-Sperren, Wartungsflags, `X-Robots-Tag`, Robots-Meta, `robots.txt` mit `Disallow: /`, Canonicals, Sitemap, DNS, TLS und Redirects als zusammenhängende Entsperrung. Vorschau und Produktion behalten getrennte Sollzustände.
- Google Search Console, Site Verification und die Search Console API besitzen eigene Nachweise für Property, Konto, OAuth-Berechtigung, echten API-Abruf und Sitemap. API-Verbindung und Indexierbarkeit werden ausdrücklich nicht miteinander verwechselt.
- Sichtbare Aussagen wie „Kontaktformular funktioniert noch nicht“, Preview-Banner, Demo-/Coming-soon-Texte, Platzhalter, Dummy-Daten und leere Aktionen werden mit Route, exaktem Text oder Selector, Codequelle und Zielzustand inventarisiert, damit sie vor Veröffentlichung gezielt entfernt oder ersetzt werden können.
- [[20-design/interface-benchmarks.md#B6 Purpose-Fit Professional Web|B6 Purpose-Fit Professional Web]] übernimmt aus der Rocket-Sites-Referenzgruppe keine Schablone, sondern ein Auswahlprinzip. Kopfzeileninventar, Seitentiefe, Beweisform, Farbwelt, Typografie, Flächen, Motion und Interaktion folgen Nutzerziel, Marke und Inhalt. Es gibt keine globale Navigationshöchstzahl, keine Mindestmenge an Motion und kein obligatorisches interaktives Kernmodul.
- [[20-design/anti-ai-slop.md]], [[20-design/color-system.md]], [[20-design/typography-layout-and-spacing.md]], [[20-design/motion-and-interaction.md]], [[20-design/design-direction.md]] und die Frontend-/QA-Regeln wurden entsprechend geöffnet. Redundante Defaults bleiben prüfpflichtig, aber konkrete Farben, Zeitbezüge, Schatten, Kicker oder statische Seiten werden nicht pauschal verboten. Mehrere Websites brauchen eine eigenständige kohärente Richtung und mindestens fünf wirksame Unterschiede, nicht künstliche Abweichung auf jeder Tabellenzeile.

**Propagation und Prüfung:** Aktualisiert wurden Einstieg, Routing, Workflow, Strategie, Design, Frontend, Preview-Gate, Owner-Hosting, SEO, QA, Templates, Referenzkatalog, Impact Map, Review Queue, README und AGENTS. Die Rocket-Sites-Gruppe ist mit allen 37 URLs und Prüfgrenzen im [[90-references/inspiration-catalog.md#Rocket-Sites-Referenzgruppe — strukturell analysiert am 19. August 2026]] dokumentiert. Google-Aussagen stützen sich auf die aktuellen offiziellen Unterlagen zu Robots-Meta, erneutem Crawlen, Search-Console-Berechtigungen und Site Verification. `git diff --check`, Suche nach überholten Pflichtformulierungen, interner Link-/Ankercheck und Graphify-Diagnose gehören zum Abschluss. Der Graph wird in diesem Commit am bestehenden Ort `graphify-out/` aus dem vollständigen Notizenstand neu gebaut; Kennzahlen und Integritätsbefund stehen im mitversionierten [[graphify-out/GRAPH_REPORT.md|Graphify-Bericht]]. Projektordner außerhalb des Web-Brains wurden nicht verändert.

## 2026-08-19 — Weniger Text, Erklärzeichen statt Absätze, und fünf Zustände, die auseinanderliefen

Auslöser waren drei Aufträge: den Sicherungslauf zu Ende bringen, die Oberfläche des Dashboards von Text entlasten, und eine Einführung für den ersten Besuch. Dazu die Bitte, gezielt nach weiteren Fehlern derselben Art zu suchen.

**Diagnose:** Die Textmenge war kein Schönheitsproblem. Auf der Übersicht standen 1100 sichtbare Zeichen, davon der größte Teil Begründungen, die beim zweiten Besuch niemand mehr liest — und die trotzdem jedes Mal zwischen dem Nutzer und dem Knopf stehen. Die Suche nach weiteren Fehlern förderte fünf Stellen zutage, an denen zwei Orte dasselbe wissen mussten und auseinanderlaufen konnten.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Wie viel Text eine Oberfläche verträgt]]: Auf der Seite steht, was zu tun ist; warum es so ist, steht dahinter. Erklärzeichen ohne JavaScript, `aria-describedby` bleibt, Symbole werden gezeichnet statt als Unicode gesetzt. Eine häufige Aktion ist ein Knopf, keine Karte mit Erklärtext.
- [[60-operations/owner-hosting-and-dashboard.md#Einführung beim ersten Besuch]]: gemerkt im Browser statt an der IP — eine IP wechselt im Mobilfunk und ist im Büro für alle dieselbe. Echtes Loch statt halbdurchsichtigem Kasten, nur auf der Einstiegsseite, abbrechbar und wiederholbar.
- [[60-operations/owner-hosting-and-dashboard.md#Zustände, die auseinanderlaufen können]] fasst die fünf gefundenen Fehler zu Regeln zusammen: zuerst die wirkende Stelle schreiben, dann die anzeigende; einen Zustand nicht doppelt führen; zusammengehörige Formularfelder über einen Index verbinden statt über die Reihenfolge; Sitzungen beim Arbeiten verlängern; keinen Verweis anbieten, dessen Ziel gelöscht sein kann.
- Ergänzung zur [[60-operations/owner-hosting-and-dashboard.md#Datensicherung]]: Der regelmäßige Lauf prüft sich selbst und räumt erst danach auf; ein verpasster Lauf wird nachgeholt.
- Ergänzung zum [[60-operations/owner-hosting-and-dashboard.md#Der Zeitpunkt gehört an die Veröffentlichung]]: Gehört der Host inzwischen einer anderen Website, verfällt die Vormerkung.

**Die fünf Befunde im Einzelnen**

Der gravierendste: Eine vorgemerkte Veröffentlichung hätte nach einem Slotwechsel nachts eine fremde Website verdrängen können — der einzige Weg, auf dem dieser Dienst eine fremde Website vom Netz genommen hätte. Der folgenreichste im Alltag: Ohne JavaScript verrutschten die Bürozeiten um einen Tag, sobald ein Tag geschlossen war, und der Eigentümer hätte falsche Öffnungszeiten veröffentlicht, ohne dass etwas nach einem Fehler aussah. Dazu der Wartungsmodus in falscher Schreibreihenfolge, Sitzungen ohne gleitende Verlängerung und ein Vorschaulink auf einen längst entfernten Release.

**In der gebauten Fassung**

**Graphify vollständig neu gebaut.** Erstmals ohne Cache: alle 64 Dateien in sechs Teilen. **651 Knoten, 1430 Kanten, 46 Gemeinschaften**, gegenüber 603/940/47.

Die Kantenzahl wuchs um gut die Hälfte, weil die Querverweise zwischen den Teilen jetzt tatsächlich ankommen. Das war zuvor die Schwachstelle: Die Teile bildeten die Kennung einer verlinkten Notiz unterschiedlich — mal `70_qa_quality_gates`, mal `70_qa_quality_gates_quality_gates` —, und 192 der 1443 Kanten liefen ins Leere. Beide Schreibweisen wurden mechanisch auf den tatsächlichen Dokumentknoten zurückgeführt: 38 der 39 unbekannten Kennungen ließen sich eindeutig auflösen, eine einzelne Kante ohne Ziel wurde entfernt. **Der Graph hat jetzt null lose Kanten** (vorher 13). Für künftige Teilextraktionen ist das die Stelle, an der nachzusehen ist.

Sichtbarer Text: Übersicht von rund 1100 auf 430 Zeichen, `/inhalte` um 44 Prozent kürzer. Die Einführung läuft in fünf Schritten. `operations/systemd/owner-hosting-backup.{service,timer}` sichert täglich um 03:20 mit `Persistent=true`, behält 14 Stände und prüft jeden neuen, bevor ältere entfernt werden. Selbsttest 43 von 43, dazu fünf Durchläufe über HTTP; eine Prüfung über alle Seiten belegt, dass kein Formular verschachtelt ist und jede `aria-describedby`-Kennung auflöst.

## 2026-08-19 — Umwandler als Betriebsvoraussetzung, Vormerkung übersteht einen Neustart, Sicherung

Auslöser waren drei Rückfragen: `libwebp` wurde auf dem Server eingerichtet, damit ein Bild nur einmal hochgeladen werden muss; der Dienst sollte sich selbst neu starten lassen; und die Frage, was mit einer vorgemerkten Veröffentlichung geschieht, wenn sie auf eine Ausfallzeit oder ein Systemupdate fällt.

**Diagnose:** Die dritte Frage deckte zwei Lücken auf, die der Umsetzung vom Vortag entgangen waren. Eine ausgelöste Vormerkung galt als „ausgeführt“, sobald ein Job entstand — unabhängig davon, ob der Bau gelang. Ein Neustart mitten im Bau ließ sie damit als erledigt zurück, während die Website unverändert blieb und niemand davon erfuhr. Und ein inhaltlich fehlgeschlagener Bau war nur im Joblog sichtbar.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Eine Datei genügt, die übrigen Fassungen entstehen daraus]] ersetzt die Regel „Grenze ohne Umwandler“ vom 18. August. Ein Bildumwandler ist eine Betriebsvoraussetzung wie eine Node-Version: Ohne ihn müsste ein Owner wissen, was WebP ist. Ein verlustfreier Umweg zwischen zwei Formaten ist zulässig und dem Verzicht vorzuziehen. Vier Regeln gelten für jedes Programm, das der Dienst startet — absoluter Pfad, keine geerbte Umgebung, begrenzte Laufzeit, und das Ergebnis durchläuft dieselbe Prüfung wie ein Upload von außen. Die alte Regel bleibt als Rückfallweg gültig, wenn der Umwandler fehlt.
- Zwei Ergänzungen zu [[60-operations/owner-hosting-and-dashboard.md#Der Zeitpunkt gehört an die Veröffentlichung]]: Ein Neustart während der Ausführung öffnet die Vormerkung wieder, ein inhaltlicher Fehlschlag wird gemeldet statt wiederholt. Der Zustand wird nicht doppelt geführt, sondern am Job abgelesen.
- [[60-operations/owner-hosting-and-dashboard.md#Datensicherung]]: Eine laufende Datenbank wird nicht kopiert, sondern als stimmige Momentaufnahme herausgeschrieben. Assets gehören dazu, Releases nicht — sie sind reproduzierbar. Fremde Zugangsdaten nur auf ausdrücklichen Wunsch. Eine halb geschriebene Sicherung wird gelöscht, nicht liegengelassen. Und eine Sicherung, die nie geöffnet wurde, ist eine Vermutung: Der Prüflauf gehört dazu.

**In der gebauten Fassung**

`packages/core/bildwandler.mjs` erzeugt die fehlenden Fassungen mit `cwebp` und `dwebp`; JPEG nach PNG läuft über eine verlustfreie WebP-Zwischenstufe, weil es keinen unmittelbaren Weg gibt. Qualitätsstufe 85 trifft die von Hand erzeugten Fassungen des Pilotprojekts fast genau (66 statt 69 kB); überschreitet eine Fassung ihre Grenze, wird die Qualität gesenkt statt abgelehnt. `packages/core/backup.mjs` sichert über `VACUUM INTO`, `backup:verify` zählt nach. Selbsttest 41 von 41, dazu Durchläufe für den Neustartfall und einen echten Bildtausch bis ins Release. Der Dienst wurde neu gestartet und antwortet.

**Graphify neu gebaut.** Der Graph stand seit dem 16. August auf 541 Knoten und bildete weder die Änderung vom 17. noch die beiden vom 18. und 19. ab. Er ist jetzt aktuell: **603 Knoten, 940 Kanten, 47 Gemeinschaften**, gegenüber 541/823/29. Der Shrink-Schutz hat nicht angeschlagen; die Extraktion lief über Subagenten, weil `graphify` selbst nur einen Gemini-Schlüssel kennt und das Brain dafür nicht an einen weiteren Anbieter gegeben wird. 35 von 64 Dateien kamen aus dem Cache, 29 wurden neu gelesen.

Eine Unschärfe bleibt und wird hier festgehalten statt verschwiegen: **13 von 965 Kanten (1,3 %) verloren ihren Endpunkt**, weil zwischengespeicherte Extraktionen aus früheren Läufen auf Knotenkennungen zeigen, die der neue Lauf leicht anders benannt hat. Betroffen sind Querverweise wie „Discovery and Scope → Web Product Workflow“. Die Notizen selbst bleiben über ihre Dokumentknoten verbunden; ein vollständiger Neubau aller 64 Dateien würde es beheben und ist die Sache eines späteren Laufs. Zwölf weitere Kanten fielen zusammen, weil dasselbe Paar einmal als `cites` und einmal als `references` extrahiert wurde — unschädlich.

**Offen bleibt** ein regelmäßiger Sicherungslauf: Der Aufruf gehört in einen systemd-Timer als root, das richtet der Betreiber ein.

## 2026-08-18 — Bilder als Dateien an ihrer Stelle, Termin an der Veröffentlichung, Auskunft danach

Nachtrag desselben Tages. Aus den vorgeschlagenen Erweiterungen wurden vier ausgewählt und gebaut: Bilder tauschen, geplantes Veröffentlichen, eine Ansicht dessen, was sich geändert hat, und der Export der eigenen Inhalte. Die Zertifikatsanzeige wurde ausdrücklich zurückgestellt.

**Diagnose:** Bei allen vieren lag die eigentliche Entscheidung nicht in der Umsetzung, sondern in der Ebene. Ein Bildfeld, das einen Dateinamen entgegennimmt, gibt dem Owner Macht über jede Verlinkung im Projekt, die das Dashboard nicht kennt. Ein Termin je Feld erzeugt Zwischenstände, die niemand entworfen hat; ein Termin-Modus ist versteckter Zustand. Und ein Vergleich vor der Entscheidung beantwortet nicht die Frage, die man danach hat.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Ein Bild ist eine Datei an einer Stelle, kein Wert in der Inhaltsdatei]]: Ein Bildfeld ersetzt eine Datei an einem registrierten Pfad; der Dateiname bleibt, in die Inhaltsdatei geht nur der Alternativtext.
- [[60-operations/owner-hosting-and-dashboard.md#Was hochgeladen wird, wird gelesen, nicht geglaubt]]: Endung und gemeldeter Typ entscheiden nichts. EXIF, XMP, IPTC und Kommentare werden entfernt, das Farbprofil bleibt, gespeichert wird nur die bereinigte Fassung. Ein Handyfoto trägt regelmäßig GPS-Koordinaten; das ist der Regelfall, nicht die Ausnahme.
- [[60-operations/owner-hosting-and-dashboard.md#Assets sind unveränderlich]]: Ein neues Bild entsteht neben dem alten. Rollback und Rückkehr zu einer früheren Fassung folgen daraus, statt eigene Mechanik zu brauchen.
- [[60-operations/owner-hosting-and-dashboard.md#Eine Datei genügt, die übrigen Fassungen entstehen daraus]] (damals „Grenze ohne Umwandler“): Ohne Bildkonverter werden mehrere Formate einzeln hochgeladen. Dieselbe Datei unter zwei Namen abzulegen ist ausgeschlossen; ein PNG, das als `image/webp` angekündigt wird, ist eine Falschangabe. **Überholt am 19. August**, siehe unten.
- [[60-operations/owner-hosting-and-dashboard.md#Der Zeitpunkt gehört an die Veröffentlichung]]: nicht je Feld, nicht als Modus. Gebaut wird zum Termin, ein Probebau läuft sofort. Eine Vormerkung belegt die Warteschlange nicht, es gibt höchstens eine offene je Website, und wer zwischendurch anderes veröffentlicht, entscheidet ausdrücklich über sie. Verspätetes wird begrenzt nachgeholt, Älteres verfällt sichtbar. Datum und Uhrzeit, Zeitzone an einer Stelle.
- [[60-operations/owner-hosting-and-dashboard.md#Nach der Veröffentlichung: sagen, was jetzt anders ist]]: eigene Ansicht in ganzen Sätzen, verglichen gegen die vorherige Revision statt gegen den heutigen Stand.
- [[60-operations/owner-hosting-and-dashboard.md#Eigene Inhalte mitnehmen]]: Selbstbedienung ohne Rückfrage, ohne Passwort-Hashes, Sitzungen und fremde Zugangsdaten.
- Der Typkatalog kennt `image`; die Vorlage beschreibt ihn in [[80-templates/owner-hosting-website-contract.md#Der Typ image beschreibt Dateien, keinen Dateinamen]]. Die Mindestnachweise decken jetzt Metadatenentfernung, Uploadverlust beim Speichern, Neustartfestigkeit einer Vormerkung, verdeckende Probebauten und die Sauberkeit des Exports ab.

**In der gebauten Fassung**

Der Pilot Uferlinie v4 gibt seine vier Fahrzeugbilder frei, je zwei Dateien. Bild- und Zeitprüfung stecken in `packages/core/bilder.mjs` und `packages/core/zeit.mjs`, beide ohne Fremdcode; Metadaten werden am Containerformat entlang entfernt, ohne Pixel zu dekodieren. Ein echter Build belegt, dass PNG und WebP im Release ersetzt sind, das unberührte Bild unverändert bleibt und der Alternativtext im HTML steht. Beim Testen fielen zwei eigene Fehler auf und wurden behoben: Das Speichern des Inhaltsformulars setzte hochgeladene Bilder lautlos zurück, und ein laufender Probebau verdeckte Fehlermeldungen und offene Entscheidungen. Selbsttest 40 von 40.

**Zurückgestellt:** die Anzeige des Zertifikatsablaufs. Sie bräuchte Lesezugriff auf `/etc/letsencrypt/live/` oder einen root-Timer, der den Zustand in eine lesbare Datei schreibt — eine Einrichtungsentscheidung, keine Dashboardarbeit.

## 2026-08-18 — Eine Eingabe je Angabe, Kontaktweg vor Versandweg, Search Console ehrlich benannt

Auslöser war die Beobachtung im laufenden Dashboard, dass Telefonnummern zwei Felder brauchten — eines für die Anzeige, eines zum Anwählen — und dass der Owner die Lücken selbst setzen musste. Dazu kamen springende Seitenränder zwischen den Unterseiten, ein fehlender Kontaktweg zum Betreiber und die Frage, wie ein Search-Console-Zugang überhaupt hinterlegt werden kann.

**Diagnose:** Zwei Felder für dieselbe Angabe sind kein Komfortproblem, sondern eine Fehlerquelle mit stillem Ausgang. Wer die sichtbare Nummer ändert und die Wählform vergisst, hat eine Website, auf der der Anruf-Link zum alten Anschluss führt; beide Werte sehen für sich gültig aus, und auf der Seite ist nichts zu sehen. Beim Prüfen fiel zusätzlich auf, dass die Konsistenzprüfung des Releases bis dahin nur E-Mail-Adressen abglich und eine fest im Quelltext stehende Rufnummer deshalb nicht meldete.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Eine Angabe ist ein Feld]]: Ein Feldtyp darf mehrere registrierte Pointer schreiben und leitet sie aus einer Eingabe ab. Der Owner gibt die fachliche Angabe ein, nicht ihre Darstellungsform. Browser- und Serverformatierung sind dieselbe Implementierung, nicht zwei gleichlautende. Deutsche Rufnummern folgen DIN 5008; willkürliche Blockgrenzen innerhalb der Teilnehmernummer werden nicht erfunden.
- Der Typkatalog kennt `phone` mit `pointers` statt `pointer`; ein einfaches Textfeld `tel` ist für neue Verträge nicht mehr zulässig. Kanonisch in [[80-templates/owner-hosting-website-contract.md#Der Typ phone schreibt zwei Pointer]].
- [[60-operations/owner-hosting-and-dashboard.md#Vertragsänderungen und bereits veröffentlichte Werte]]: Gespeicherte Wertesätze werden beim Laden auf die aktuelle Vertragsfassung gehoben, nicht in der Datenbank überschrieben. Eine Revision ist ein Beleg und wird nicht nachträglich verändert. Ein Rollback über eine Formänderung hinweg ist ein eigener Testfall.
- [[60-operations/owner-hosting-and-dashboard.md#Formular vor Versandweg]]: Ein Formular darf vor der Entscheidung über den Versandweg gebaut werden, wenn die Anfrage serverseitig ankommt, ihr Zustellzustand ein eigenes Feld ist und im UI steht, und der Betreiber einen belegten Weg hat, sie zu lesen. Ein Formular, das nur eine Erfolgsmeldung zeigt, ist schlechter als keines.
- [[60-operations/owner-hosting-and-dashboard.md#Ein API-Schlüssel genügt nicht]]: Die Search Console API verlangt ein autorisiertes Konto, kein API-Schlüssel-Projekt. Verwendet wird ein Dienstkonto; seine Schlüsseldatei liegt mit Rechten `0600` neben der Datenbank statt darin, damit ein Datenbank-Backup keine fremden Zugangsdaten enthält, und wird nie zurückgezeigt.
- [[60-operations/owner-hosting-and-dashboard.md#Drei Zustände, nicht zwei]]: `aus`, `hinterlegt`, `aktiv`. Zugangsdaten hinterlegen und Daten abrufen sind verschiedene Dinge. Die Netzwerkisolierung des Dienstes wird für eine Statistik nicht aufgehoben; ein Abruf braucht einen eigenen, ausschließlich für Google freigegebenen Weg. Ohne Abruf zeigt das Dashboard Striche mit Begründung, keine Beispielzahlen.
- [[60-operations/owner-hosting-and-dashboard.md#Dashboard-Bereiche]]: Der Seitenrahmen ist auf allen Unterseiten identisch. Der Platz der Bildlaufleiste bleibt reserviert, die Kopfzeile steht in festen Spalten. Ein springender Rahmen entzieht einer Verwaltungsoberfläche das Vertrauen, bevor jemand ihn benennen kann.
- Die Konsistenzprüfung des Legacy-Adapters umfasst alle Kontaktangaben des Vertrags, nicht nur E-Mail-Adressen; Rufnummern werden ziffernreduziert verglichen. Warnungen erscheinen sichtbar im Protokoll der Fassung, nicht nur als Zeile im Joblog.

**In der gebauten Fassung**

Der Pilot Uferlinie v4 hat statt vier Telefonfeldern zwei: Land und Nummer für Festnetz und Mobil. Ein Build mit geänderter Nummer belegt, dass `betrieb.telefon.anzeige` und `betrieb.telefon.tel` gemeinsam geschrieben werden. Dabei trat die erwartete Legacy-Grenze zutage: `src/pages/contact.mjs` trägt die Rufnummer zusätzlich fest in `kontaktDescription`. Die Quelle wurde nicht angefasst; die Prüfung meldet die Stelle jetzt namentlich als Warnung. Neu sind außerdem die Dashboard-Bereiche „Kontakt“ und „Suchmaschine“ sowie die CLI-Befehle `support:list`, `support:show`, `support:status` und `integrations`.

**Propagation und Prüfung:** Owner Hosting and Dashboard, Owner Hosting Website Contract, Coverage and Impact Map und dieser Change Log wurden gemeinsam aktualisiert. Selbsttest 29 von 29, dazu ein Durchlauf über HTTP von Anmeldung bis Veröffentlichungsvergleich und ein echter Legacy-Build. Alle internen Verweise des Vaults lösen auf.

**Graphify weiterhin offen, jetzt mit benannter Ursache.** `graphify-out/` steht unverändert auf dem Stand vom 16. August 2026 mit 541 Knoten und bildet weder die Änderung vom 17. noch diese ab. Der Grund ist keine Entscheidung, sondern eine fehlende Voraussetzung: Die semantische Extraktion braucht entweder einen gesetzten `GEMINI_API_KEY` beziehungsweise `GOOGLE_API_KEY` oder Subagenten des Hosts; beides stand in dieser Sitzung nicht zur Verfügung. Der Cache deckt 35 der 64 Inhaltsdateien ab, 29 sind neu zu lesen — darunter Core Rules, Routing Map, Owner Hosting and Dashboard, Quality Gates und dieser Change Log. Vor der nächsten graphgestützten Strukturabfrage ist der Graph neu zu bauen und der Shrink-Schutz zu prüfen. Bis dahin sind Antworten aus dem Graphen zu diesen Notizen veraltet, und es ist breit zu suchen statt abzufragen.

## 2026-08-17 — Deployment-Slots, Staging-Domain und erste gebaute Fassung des Owner-Hostings

Auslöser war der Auftrag, `johannstein.de` von der Weiterleitung auf `johannstein.com` zu lösen und als Testumgebung für jeweils eine ausgewählte Website zu betreiben, mit Dashboard unter `hosting.johannstein.de` und Steuerung über eine rote Kachel auf `/dev`. Bis dahin beschrieb das Brain das Owner-Hosting nur als Zielarchitektur; ein Modell für „ein Host, wechselnde Website“ fehlte.

**Diagnose:** Ohne eigene Entität hätte die Zieladresse entweder als weiterer Katalogstatus geführt werden müssen, womit jede Website Anspruch auf sie gehabt hätte, oder als Pseudo-Tenant, womit Historien, Verträge und Zugänge verschiedener Websites vermischt worden wären. Zusätzlich fehlte eine Regel für Altprojekte, die das Hosting nicht kennen und laut Auftrag nicht geändert werden dürfen.

**Kanonisch neu**

- [[60-operations/owner-hosting-and-dashboard.md#Deployment-Slots]] führt den Deployment-Slot als getrennte Entität zwischen Host und Tenant ein: zwei Hosts, genau ein Tenant, genau ein Release, ein vorgemerkter Kandidat. Öffentlicher Release und Dashboard-Tenant wechseln atomar gemeinsam; Sitzungen sind an den Tenant gebunden und nach einem Wechsel wertlos. Ein Wechsel läuft immer in zwei Schritten.
- Passwortgeschützte Staging-Domains sind beschrieben: eigenes Basic Auth außerhalb der Repositories, `noindex` an zwei Stellen, ACME-Challenge ausgenommen. `noindex` fällt erst nach ausdrücklicher Entscheidung, unabhängig vom Passwortschutz.
- Der Legacy-Adapter ist als eng begrenzte Ausnahme für unveränderliche Altprojekte kanonisiert: isolierte Kopie, gepinnter Quellhash, kein Schreiben in die Quelle, zusätzlich erzwungen über `ProtectSystem=strict`. Fest im Quelltext hinterlegte Kontaktdaten werden als Warnung gemeldet statt durch Änderung der Quelle „behoben“.
- Websites ohne Editorvertrag bekommen ein ehrlich schreibgeschütztes Dashboard. Bearbeitbare Felder werden nie aus Text oder HTML erraten.
- [[60-operations/delivery-and-local-start.md#Test-Slot johannstein.de]] beschreibt die rote Zielfläche als einzelnes Deployment-Ziel, ausdrücklich keine vierte Lane. Eine abgelegte Archivfassung bleibt im Archiv; `catalog.json` wird nicht umgedeutet. Der Browser überträgt nur den Katalogschlüssel `group/project/variant`.
- [[60-operations/delivery-and-local-start.md#Keine Hosting-Subdomain für Unterseiten-Vorschauen]] entscheidet die offene Frage: Unterseiten-Vorschauen auf `.com` erhalten kein simuliertes Dashboard und keine nachgebildete Subdomain. Nur die im Slot aktive Fassung hat ein Dashboard.
- [[80-templates/owner-hosting-website-contract.md#Legacy-Bridge-Vertrag als Ausnahme]] dokumentiert den von außen beschriebenen Vertrag samt `legalImpact`-Pflichtbestätigung. Neue Websites verwenden weiterhin den regulären Content-Loader.
- [[70-qa/quality-gates.md]] und [[70-qa/test-matrix.md]] prüfen Slotwechsel, atomaren Doppelwechsel, Cross-Tenant-Hostbindung, Quellimmutabilität, Passwortgate, `noindex`, Rollback und die Unabhängigkeit der öffentlichen Website.

**Erste gebaute Fassung**

`/srv/Web-Design/projekte/owner-hosting/` existiert jetzt und ist nicht mehr nur Zielarchitektur. Zwei begründete Abweichungen sind in [[60-operations/owner-hosting-and-dashboard.md#Verbindliche Architekturentscheidung]] als Umsetzungsstand vermerkt: ein Dienst statt zweier getrennter Units, mit der Trennung stattdessen an zwei Sockets mit eigenen Gruppen, und SQLite über `node:sqlite` statt PostgreSQL, da auf dem Server keines installiert ist. Schema, Hostauflösung, Vertragsgrenzen und Buildisolation bleiben unverändert. Der Dienst hat keine Laufzeitabhängigkeiten außerhalb der Node-Standardbibliothek und läuft ohne Netzwerkzugang.

Pilot ist `Old-Projects/Fahrschule-Kladow_v4/versions/01-uferlinie` mit einem Legacy-Vertrag über Telefon, Mobil, E-Mail, Bürozeiten und den Schalter der Stellenanzeige. Der Quellhash ohne Buildausgaben ist `5ddc5924ea92a8fb343706efaf9cc519ebe290f2a2898146451b342a62bf0464`, der Hash des vorhandenen `dist/` `385d38a19363c1296420069105f8e64cbad85d6d3a814ad0f83cfa14af781032`; beide blieben über mehrere Builds und einen Rollback unverändert. Die im vorherigen Handoff genannten Vergleichswerte waren mit keiner reproduzierbaren Berechnung nachvollziehbar und wurden durch die hier dokumentierte ersetzt.

**Propagation und Prüfung:** Owner Hosting and Dashboard, Delivery and Local Start, Quality Gates, Test Matrix, Owner Hosting Website Contract, Coverage and Impact Map und dieser Change Log wurden gemeinsam aktualisiert.

**Graphify weiterhin vertagt:** Die Vertagung vom 17. August 2026 gilt unverändert fort. `graphify-out/` bleibt auf dem Stand von 541 Knoten und bildet auch diese Änderung nicht ab. Vor der nächsten graphgestützten Strukturabfrage muss der Graph mit einem verfügbaren LLM-Backend neu gebaut und der Shrink-Schutz geprüft werden.

## 2026-08-17 — Variationszwang, Owner Hosting und serverbasierte Developer-Plattform

Auslöser war die Durchsicht von `Old-Projects/Fahrschule-Kladow_v5`: Die drei Fassungen waren formal verschieden, wirkten aber wegen derselben Karten-, Radius-, Header-, Typografie- und Motion-Sprache wie Varianten desselben Systems. Gleichzeitig fehlten ein kanonisches Owner-Hosting-Modell und eine belastbare Einordnung der Server-Vorschauen.

**Diagnose:** B5 „Modern Neutral Craft Web“ war als websiteübergreifende Detailebene formuliert. Zusammen mit einer Unterscheidungsmatrix, die nur vier abweichende Merkmale verlangte, erzeugte das einen gemeinsamen Stilzwang. Design Contract und UI-UX-Pro-Max-Ergebnis wurden außerdem nicht dauerhaft je Website geführt. Im Betrieb waren statische Kundenseite, Owner-Dashboard, editierbare Inhalte und die drei Zustände der Developer-Plattform nicht als zusammenhängendes Modell beschrieben.

**Kanonisch neu und geändert**

- [[20-design/interface-benchmarks.md#H0 Handwerksuntergrenze]] ist die immer geltende, stilneutrale Qualitätsuntergrenze. B5 bleibt als wählbares Stilprofil erhalten; seine Radius-, Karten-, Header-, Mono- und Motion-Sprache ist kein globaler Standard mehr.
- [[20-design/design-direction.md#Stilabstand bei mehreren Websites]] verlangt jetzt paarweisen Abstand auf jeder Achse der vollständigen Unterscheidungsmatrix. Jede Website führt einen eigenen Design Contract, ein eigenes UI-UX-Pro-Max-Artefakt und bei Vorgängerfassungen ein Vererbungsregister. Motiv, Name, Signalfarbe und Kernmodul dürfen ohne begründete Entscheidung nicht wiederholt werden.
- Typografie, Radius, Rahmen, Tiefe, Komponentenrepertoire, Headerinventar, Footer, Page Chrome und Bewegung werden je Website entschieden. Mono bleibt technischen Rollen vorbehalten und wird nicht für Adressen, Fließtext oder Abschnittstitel verwendet.
- [[70-qa/quality-gates.md]] und [[70-qa/test-matrix.md]] prüfen Kontrast im tatsächlichen Komponenten- und Flächenkontext, die Geometrie aller Header-Kinder bei den Zielbreiten sowie echte Browser-Renderings. Eine fehlende Render-Möglichkeit ist ein Vorabnahme-Blocker.
- [[60-operations/owner-hosting-and-dashboard.md]] ist der kanonische Owner-Hosting-Vertrag: öffentliche statische Website hinter Nginx, getrennte Dashboard-App unter `hosting.<domain>`, ein mandantenfähiger Codebestand, `owner_editable` pro Inhaltsblock, atomare Veröffentlichungen mit Rollback, Wartungsmodus mit `503`, Datenschutz-/Vertragsgrenzen und die vier offenen Produktentscheidungen.
- Auf dem Server `217.154.218.30` sind feste Projektports und lokale Startskripte kein Übergabeweg; Zugriff und Status laufen über `johannstein.com/dev`. Außerhalb dieses Servers bleibt die Portregel bestehen.
- [[60-operations/delivery-and-local-start.md#Developer-Plattform]] definiert Archiv, aktuelle Projekte und zur Veröffentlichung vorgesehene Fassungen. `vorschau/` bleibt eine geschützte Legacy-Quelle mit Startstatus „vorgesehen“, aber keine vierte Übersicht; Login, Einzelfreigaben und `noindex` bleiben unverändert.

**Owner-Hosting am 17. August weiter präzisiert**

- Das Dashboard wird einmal als eigener Git-Bestand unter `/srv/Web-Design/projekte/owner-hosting/` gebaut. Eine zentrale Webanwendung bedient alle `hosting.<domain>`-Hosts über einen Unix-Socket; ein getrennter Worker baut und veröffentlicht. Kundenprojekte erhalten keine Dashboard-Kopie.
- Code, Secrets, PostgreSQL-Zustände, Content-Revisionen, Assets, Build-Arbeit und statische Releases haben getrennte kanonische Pfade und Dienstberechtigungen. Projekt-Basis und zentrales Owner-Overlay bilden beim Build eine aufgelöste statische Inhaltsdatei.
- [[80-templates/owner-hosting-website-contract.md]] definiert die zwei Website-Artefakte `content/<website>.json` und `owner-hosting/tenant.json`, den reservierten `_hosting`-Vertrag mit stabilen JSON-Pointern, Typen, Grenzen, Preview-Routen und Veröffentlichungspolicies sowie die Synchronisierung bei späteren Website-Updates.
- Der Website-Build liest lokal die eingecheckte Basis und im zentralen Worker `OWNER_HOSTING_CONTENT_FILE`; Preview und Release verwenden damit dieselbe aufgelöste, validierte Inhaltsquelle, ohne Browser-SDK, Dashboard-API oder Datenbankzugriff aus der Kundenseite.
- Registrieren und Aktualisieren laufen über die Zielbefehle `tenant lint`, `tenant plan`, `tenant register` und den Contract-Diff. Owner-Werte werden bei Updates erhalten, explizit migriert oder dokumentiert archiviert; ein Projektordner allein aktiviert kein Hosting.
- Zentrales Datenmodell, Host-zu-Tenant-Auflösung, automatisch generierte Formulare, Draft-/Preview-/Publish-Ablauf, isolierte Buildprofile und eine sechsstufige Baufolge vom Fundament bis zu Integrationen sind jetzt verbindlich beschrieben.
- Der beschlossene Pfad ist ausdrücklich Zielarchitektur: Owner-Hosting-Repository, Dienste, CLI, Datenbank und Tenant Registry sind noch nicht implementiert und werden erst nach den dokumentierten Mindestnachweisen als produktiv behandelt.

**Propagation und Prüfung:** Core Rules, Routing Map, Update Protocol, Workflow, Skillrouting, Design-, Komponenten-, Motion- und Typografienotizen, beide QA-Dokumente, Project Master Spec, Owner Hosting Website Contract, Templates Index, AI Build Prompt, Dateninventar, Betriebsdokumentation, Index, README, Coverage Map, Review Queue und `AGENTS.md` wurden gemeinsam aktualisiert. Widersprüchliche Altformulierungen und veraltete Anker wurden gesucht und korrigiert.

**Graphify ausdrücklich vertagt:** Der Nutzer hat am 17. August 2026 entschieden, Graphify später zu klären. `graphify-out/` bleibt deshalb in diesem Commit bewusst auf dem Vorgängerstand von 541 Knoten und bildet diese Änderung noch nicht ab. Vor der nächsten graphgestützten Strukturabfrage muss der Graph mit einem verfügbaren LLM-Backend neu gebaut und der Shrink-Schutz geprüft werden.

**Begleitende Implementierung:** Im separaten Repository `projekte/johannstein.com` wurde `/dev` in die drei Bereiche gegliedert und als Commit `e4b1ff2` nach `origin/main` gepusht. Die Zuordnung zwischen „aktuell“ und „zur Veröffentlichung vorgesehen“ wird atomar unter `.runtime/previews/catalog.json` gespeichert und ist per Drag-and-drop sowie sichtbarer Tastatur-/Button-Aktion bedienbar. Produktionsbuild, Auth-Negativtest, Archiv-Sperre, Persistenz, Drag-and-drop, Tastaturbedienung und echte Desktop-/Mobil-Renderings wurden geprüft.

**Offen:** Vor dem ersten Owner-Hosting-Rollout sind die vier Entscheidungen aus [[60-operations/owner-hosting-and-dashboard.md#Offene Produktentscheidungen]] zu Search-Console-Konto/Property, E-Mail-Anbieter, Kalender- oder Vorschlagsfluss und Zugangszustellung projektspezifisch zu treffen.

## 2026-08-16 — Prüfliste an Auslöser gebunden statt an Kalenderdaten

Auslöser war die Feststellung des Nutzers, dass die neun Zeilen der Review Queue Fälligkeitsdaten trugen, aber nirgends ein Mechanismus existierte, der sie auslöst. Weder Cronjob noch Hook noch geplante Routine waren vorhanden. Die Liste war eine Absichtserklärung, deren Termine mit der Zeit alle in die Vergangenheit gerutscht wären.

**Diagnose:** Eine Wartungsliste ohne Auslöser wird nicht abgearbeitet und entwertet mit jedem verstrichenen Datum auch die Zeilen, die wirklich zählen.

**Kanonisch neu**

- [[98-maintenance/review-queue.md]] trennt jetzt zwischen automatisch und anlassgebunden geprüften Quellen. Ein Datum allein gilt ausdrücklich nicht mehr als Auslöser.
- Sicherheits-, Auth- und Billing-Quellen laufen über eine geplante Cloud-Routine, viermal im Jahr, mit Ergebnis direkt nach `main`. Ohne Befund aktualisiert sie nur Datum und Status, damit der Lauf sichtbar ist.
- Die übrigen sieben Prüfungen hängen an einem Arbeitsschritt, der ohnehin stattfindet, etwa dem Setzen eines Grenzwerts, der Aufnahme einer Bibliothek oder dem Einbinden einer Karte. Registriert in [[98-maintenance/coverage-and-impact-map.md#Zeitabhängige Quelle wird verwendet]].

**Auf Eis:** Die Routine ist inhaltlich fertig, aber nicht angelegt. Zuerst fehlte die GitHub-Verknüpfung des Claude-Kontos, danach der Zugriff der GitHub-App auf das private Repository. Der Nutzer hat das Thema am selben Tag zurückgestellt. Die beiden automatisch geprüften Zeilen werden deshalb bis auf Weiteres nicht geprüft; das steht so in der Review Queue. Die anlassgebundenen Prüfungen sind davon nicht betroffen und wirken sofort.

**Nicht geändert**, ausdrücklich auf Entscheidung des Nutzers vom 2026-08-16: `prefers-reduced-transparency` und `prefers-contrast` bleiben ungeregelt, die Lizenzfrage bei UI UX Pro Max wird nicht vorgezogen, die eingeschränkt geprüften Referenzen werden nicht nachgearbeitet, die drei neuen Motion-Skills werden nicht in eine Kalenderzeile aufgenommen. Sie stehen stattdessen anlassgebunden in der neuen Tabelle.

## 2026-08-16 — Drei Motion-Skills installiert, Apple-Referenz aufgenommen

Auslöser war die Durchsicht des Skillsets [emilkowalski/skills](https://github.com/emilkowalski/skills) auf Wunsch des Nutzers. Von zehn Skills wurden drei installiert, einer als Referenznotiz übernommen und die übrigen begründet abgelehnt.

**Diagnose:** Das Brain forderte je Bewegung Zweck, Häufigkeit, Easing, Dauer und Unterbrechbarkeit, hatte aber keine Instanz, die das prüft, und keinen Skill, der eine Einzelbewegung mit diesen Werten baut. Für gestengeführte Bewegung, Federn und Momentum fehlte jede Regel.

**Neu installiert**, real unter `/srv/Web-Design/shared-agent-skills/`, verlinkt nach `~/.claude/skills/` und `~/.agents/skills/`, damit Claude und Codex dieselbe Fassung lesen:

- `animate` für den Bau einer Einzelbewegung.
- `review-animations` als Pflichtprüfung vor der Abnahme, verankert in [[70-qa/quality-gates.md]] `G1` und in [[20-design/motion-and-interaction.md#Nachweis und Abnahme]].
- `prototype` für Divergenz in der Entwurfsphase, ausdrücklich nur für einzelne Bauteile und nie für ganze Websites, damit die Regel aus [[00-start/05-web-product-workflow.md#Anzahl der Websites]] unberührt bleibt.

**Kanonisch neu**

- [[90-references/apple-fluid-interface.md]] als Referenz für gestengeführte und federbasierte Bewegung mit Federwerten, Geschwindigkeitsübergabe, Momentumprojektion, Rubberbanding und Materialtiefe. Der zugehörige Skill `apple-design` ist bewusst nicht installiert, sein Inhalt steht in der Notiz.
- [[20-design/motion-and-interaction.md#Gestengeführte Bewegung]] verweist von der kanonischen Motion-Notiz dorthin und behält bei Widerspruch den Vorrang.

**Abgelehnt:** `find-animation-opportunities` widerspricht dem verbindlichen Motion-Niveau, weil es Bewegung nach dem Grundsatz filtert, die meisten Kandidaten abzulehnen. `pick-ui-library` würde eine zweite Bibliotheksliste neben [[90-references/tools-and-libraries.md]] eröffnen. `ask-sonner` ist ohne React und Sonner ohne Anwendung, `animation-vocabulary` ohne Entscheidungsgewinn, `improve-animations` überschneidet sich mit `review-animations` und wird erst bei einem echten Bestandsaudit nachgezogen. `emil-design-eng` war bereits installiert und ist mit der Repo-Fassung identisch.

**Offen:** Die Signale `prefers-reduced-transparency` und `prefers-contrast` sind im Brain noch nicht kanonisch geregelt. Vermerkt in der Apple-Notiz und in [[98-maintenance/review-queue.md]].

## 2026-08-16 — Website Copy als kanonische Notiz und Stilabstand bei mehreren Websites

Auslöser war die Durchsicht der beiden Websites aus `Old-Projects/Fahrschule-Kladow_v4` durch den Nutzer. Beide Websites wurden ausdrücklich als gut bewertet. Die Kritik betraf die Texte und den Abstand zwischen den Fassungen, nicht Gestaltung oder Umfang.

**Diagnose:** Das Brain regelte Textmenge, Tonalität und Beweisführung, aber nicht die Formulierung selbst. Damit entstanden wiederkehrende Muster, die eine Seite generiert wirken lassen, obwohl jede Einzelregel eingehalten war: Meta-Sätze über die eigene Seite wie „Gerechnet mit unseren echten Preisen. Stand 8. August 2026.", Negativabgrenzungen wie „Keine Bewertungsdurchschnitte, keine Bestehensquoten.", Selbstverständlichkeiten wie „Jede Seite nennt Voraussetzungen, Umfang und Prüfung.", verblose Statementzeilen unter Überschriften und die durchgehende Dreiergliederung.

**Kanonisch neu**

- [[10-strategy/website-copy.md]] als Besitzer für Formulierung, Satzform, Interpunktion und Textmuster. Enthält Streichregeln, die erwünschten Muster einschließlich Hakenliste, eine Umformungstabelle aus der Durchsicht und Prüffragen vor der Abnahme.
- [[20-design/design-direction.md#Stilabstand bei mehreren Websites]] mit einer Unterscheidungsmatrix aus acht Merkmalen, von denen sich mindestens vier klar unterscheiden müssen. Vorlage dafür in [[80-templates/project-master-spec.md]].
- [[00-start/04-plugins-and-skills.md#Vorrang der Brain-Regeln vor Skill-Vorschlägen]] mit den bekannten Konfliktstellen, weil die eingesetzten Skills genau die verbotenen Copy-Muster vorschlagen.
- [[90-references/inspiration-catalog.md]] führt StepSafer als vom Nutzer benannten Copy-Benchmark, belegt am 16. August 2026.

**Geändert**

- Textbudget in [[10-strategy/information-density-and-mobile-clarity.md#Textbudget]]: Der erklärende Text unter einer Überschrift darf jetzt ein bis drei ganze Sätze umfassen, ein Fragment ist keine zulässige Fassung. Aufzählungen beginnen bei zwei Punkten, damit die Dreierfigur nicht mehr die kleinste erlaubte Antwort ist. Die frühere Fassung mit genau einem Satz und mindestens drei Punkten hat die kritisierten Muster begünstigt.
- [[70-qa/quality-gates.md]] `G1` prüft die Copy-Regeln und die Unterscheidungsmatrix getrennt.

**Abgrenzung:** Die Beispiele stammen aus einem abgeschlossenen Projekt und lösen dort keine Nacharbeit aus. Sie stehen im Brain als Muster für kommende Builds.

## 2026-08-09 — Preview Access Gate und Ablage für Vorschauprojekte

Auslöser war der Auftrag, künftige Projekte unter `johannstein.de` zeigen zu können, ohne dass sie öffentlich erreichbar sind, während `johannstein.com` und `bildungsbruecke-verbindet.de` unverändert öffentlich bleiben.

**Diagnose:** Das Brain kannte nur vollwertige Konten und Rollen aus [[40-backend-security/authentication-and-accounts.md]], aber kein Muster für „noch nicht öffentlich". Damit gab es für einen wiederkehrenden Fall keine kanonische Antwort, und die naheliegende Abkürzung wäre ein Client-Check gewesen, den [[40-backend-security/security-baseline.md]] ausdrücklich verbietet.

**Kanonisch neu**

- [[40-backend-security/preview-access-gate.md]] als Muster: Durchsetzung am Reverse Proxy statt in der Anwendung, Hash statt Klartext, `noindex` zusätzlich zum Gate, eigene Domain statt Unterpfad der Produktionsdomain, ACME-Ausnahme für die Zertifikatserneuerung, plus Prüfpunkte und Betriebsablauf für Codewechsel und Veröffentlichung.
- Ablagekonvention `Web-Design/vorschau/<Projektname>/` parallel zu `projekte/` für Live-Websites, mit gemeinsamer Gate-Konfiguration unter `vorschau/_gate/`. Jedes weitere Vorschauprojekt erbt das Gate und belegt einen Port nach [[60-operations/delivery-and-local-start.md]].
- Registrierung in [[00-start/02-routing-map.md]] und [[98-maintenance/coverage-and-impact-map.md]].

**Abgrenzung:** Das Gate ist eine Sichtbarkeitssperre, kein Zugriffsschutz. Ein kurzer Zugangscode hält gezielte Angreifer nicht auf, deshalb ist in der Notiz festgehalten, dass hinter dem Gate keine echten Kundendaten, Produktionsschlüssel oder Zahlungsvorgänge liegen dürfen.

## 2026-08-08 — Handwerksebene B5: Tokenvertrag, Formsprache und Bewegungswerte

Auslöser war der Befund des Nutzers, dass beauftragte Websites noch nicht wie sieben von ihm benannte Referenzseiten aussehen, ausdrücklich bezogen auf Oberfläche, Bedienung, Animation und Kastengestaltung, ausdrücklich nicht auf Rechtliches oder Belege.

**Diagnose:** Das Brain war stark im Prozess und in der Haltung, aber ohne konkrete Werte. Es forderte „definierte Tokens", „eine Radiusfamilie" und „hohe Motion-Dichte", nannte aber weder die Pflichtrollen der Tokens noch Radius-, Rahmen-, Tiefen- oder Bewegungswerte. Damit war jeder Build in genau den Details frei, die den Unterschied zwischen konzipiert und fertig ausmachen. Belegt wurde das durch Auswertung des ausgelieferten Markups und der vollständigen CSS-Bündel aller sieben Seiten am 8. August 2026.

**Kanonisch neu**

- [[20-design/interface-benchmarks.md#B5 Modern Neutral Craft Web]] als fünfter Benchmark und als Detailebene, die bei jedem Build zusätzlich zum gewählten Leitbenchmark gilt und nicht gewählt wird.
- [[20-design/color-system.md#Tokenvertrag]] mit Pflichtrollen samt belegten Referenzwerten. Die zwei bisher fehlenden Rollen `border-hover` und `accent-subtle` sind die konkrete Ursache für flach wirkende Zustände und getönte Flächen, die im eigenen Build nicht entstanden.
- [[20-design/typography-layout-and-spacing.md#Radiusskala und Rahmenbehandlung|frühere vierstufige Radiusskala]] mit vier Stufen, [[20-design/typography-layout-and-spacing.md#Tiefe und Rahmen]] mit einer Rahmenstärke und genau einer Schattenstufe, kalibrierte Type Ramp mit negativem Tracking nur auf großen Stufen, fluide Container- und Sektionswerte.
- [[30-frontend/components-and-ui-states.md#Kartenentscheidung|früheres Kartenrezept]] und [[30-frontend/components-and-ui-states.md#Option durchscheinende Kopfzeile|früheres Kopfzeilenrezept]] samt Statuspille, Tag und Chip.
- [[20-design/motion-and-interaction.md#Kalibrierte Bewegungsbeispiele|frühere Standardrezepte]] mit Kurven- und Dauersatz und zwölf benannten Rezepten von Reveal über Zeichenauftakt bis Maskenausblendung.

**Bewusste Lockerungen, vom Nutzer am 8. August 2026 ausdrücklich genehmigt**

1. Die durchscheinende Kopfzeile mit Blur und ein einziger flacher Hover-Schatten auf klickbaren Flächen sind jetzt erlaubt. Vorher schloss [[20-design/interface-benchmarks.md#B1 Soft Neutral Product Console]] Glas und Schatten pauschal aus. Bedingungen: kein Schatten im Ruhezustand, genau eine Stufe, Kontrastmessung gegen den ungünstigsten darunterliegenden Inhalt, deckender Fallback. Hairline bleibt das tragende Abgrenzungsmittel, und B1 selbst bleibt vollständig schattenfrei.
2. Der kleine Karten-Hover-Lift von einem bis zwei Pixeln ist als System-Affordanz ausdrücklich erlaubt und erwünscht. „Aggressive Card-Lifts" in [[20-design/anti-ai-slop.md]] ist auf über zwei Pixel, Maßstab über `1.02`, Rotation und Schattensprung präzisiert, und neu verboten ist der Lift auf Flächen, die nichts auslösen. Klargestellt: der Lift ersetzt keine Route-Choreografie.
3. Die Radiusvorgabe ist von einer Containerstufe auf vier feste Stufen umgestellt: `6–8px`, `10–12px`, `16–20px`, Pille.

**Nicht übernommen** aus den Referenzen: der Blau-Lila-Verlaufstext, Emojis als Sektionszeichen, Verlaufsflächen als Bildersatz sowie alles Rechtliche, alle Kennzahlen und Referenzangaben dieser sieben Seiten.

### Geprüfte Auswirkungen

Aktualisiert wurden Core Rules, `AGENTS.md`, Interface Benchmarks, Color System, Typography Layout and Spacing, Motion and Interaction, Anti AI Slop, Design Direction, Components and UI States, Derived Design Patterns, Inspiration Catalog, Quality Gates, Project Master Spec, AI Build Prompt und die Coverage and Impact Map. Sitemap, Datenflüsse, Rechtstexte, Sicherheitsregeln und Betriebsdoku änderten sich nicht. Kein Projekt unter `../Projekte/` wurde verändert; bestehende Projekte werden nur auf ausdrückliche Ansage nachgezogen.

Offen und in der [[98-maintenance/review-queue.md|Review Queue]]: Tastaturbedienung, Reduced-Motion-Verhalten und mobiles Verhalten der sieben Referenzseiten sind nicht belegt, weil die Auswertung statisch über Markup und CSS erfolgte. Vor einer Übernahme genau dieser Aspekte ist eine interaktive Prüfung nach [[90-references/reference-research-workflow.md]] nötig.

## 2026-08-07 — Web-Brain als Git-Repository mit agentengesteuerter Synchronisation

Auslöser war die Anforderung des Nutzers, das Vault geräteübergreifend zu nutzen. Das Vault liegt jetzt als privates Git-Repository unter `git@github.com:johstn8/web-brain` auf Branch `main`, Einzelnutzer. Kein Projekt unter `../Projekte/` wurde verändert.

- **Neuer kanonischer Abschnitt `AGENTS.md` → Synchronisation.** Der kanonische Stand des Brains liegt im Remote, nicht im lokalen Arbeitsverzeichnis. Vor jeder Nutzung, auch rein lesend und auch bei Verwendung für ein Web-Produkt, wird `git fetch` ausgeführt und bei Rückstand per `git pull --rebase` nachgezogen. Nach jeder abgeschlossenen Änderung folgt Commit und Push ohne Rückfrage. Grenzen sind benannt: kein Force-Push, kein Umschreiben veröffentlichter Historie, bei Konflikt keine eigenmächtige Auflösung, bei Fehlschlag von `fetch` oder `push` Meldung statt stiller Weiterarbeit.
- **Verbindliche Regel ergänzt.** Die Regelliste in `AGENTS.md` verweist auf den Synchronisationsabschnitt als kanonischen Besitzer.
- **[[00-start/03-update-protocol.md]] erweitert.** Der Ablauf beginnt mit dem Holen des Remote-Stands und endet mit Commit und Push. Notizänderung und Change-Log-Eintrag gehören in denselben Commit; ohne diesen Schritt gilt ein Update nicht als abgeschlossen.
- **Absolute Gerätepfade entfernt.** Der Graphify-Abschnitt nannte den Graphen bisher unter einem absoluten Pfad des bisherigen Rechners und hätte auf jedem weiteren Gerät ins Leere gezeigt. Der Graph wird jetzt repository-relativ als `graphify-out/graph.json` geführt, der Projektausschluss als `../Projekte/`. Pfade in Notizen werden generell relativ zur Vault-Wurzel aufgelöst.
- **Obsidian-UI-Zustand aus der Versionierung genommen.** `.obsidian/workspace.json` speichert geöffnete Fenster und Cursorpositionen des jeweiligen Geräts und hätte bei jedem Gerätewechsel unnötige Konflikte erzeugt. Die Datei ist untracked und steht zusammen mit `workspace-mobile.json` und `.obsidian/cache` in `.gitignore`. Geteilte Vault-Einstellungen wie Erscheinungsbild und Plugin-Auswahl bleiben versioniert. `TasksForAgent.md` bleibt wie vom Nutzer eingerichtet ausgeschlossen.

- **Graph-Neubau bei jeder Aktualisierung Pflicht.** `AGENTS.md` → Graphify → Pflicht zum Neubau verlangt den Neubau nicht mehr nur bei größeren Änderungen, sondern bei jeder Aktualisierung des Brains, am bestehenden Ort `graphify-out/` und im selben Commit wie die Notizänderung. Begründung: ein Graph, der den Notizenstand nicht abbildet, liefert falsche Antworten und ist schlechter als kein Graph. Der Graph bleibt ausdrücklich mitversioniert, damit ein frisch geklontes Gerät ohne Neuberechnung abfragen kann.
- **Graph neu gebaut.** Stand 2026-08-07: 334 Knoten, 564 Kanten, 18 Hyperedges, 12 Communities aus 63 Dateien. Der Vorgängerstand vom 2026-08-06 hatte 438 Knoten, aber nur 397 Kanten und keine Hyperedges. Der Rückgang der Knotenzahl stammt aus geringerer Zerfaserung der Konzeptknoten, nicht aus gelöschten Inhalten; Kantendichte und Gruppenbeziehungen sind gestiegen. Graphifys Shrink-Schutz wurde dafür bewusst übergangen, der Vorgängergraph bleibt über die Git-Historie erreichbar. Die Diagnose meldet fünf zusammengefallene Kanten, was im ungerichteten Graphen bei doppelt gerichteten Knotenpaaren erwartbar ist; keine hängenden oder fehlenden Endpunkte.
- **Gerätespezifische Graphify-Dateien aus der Versionierung genommen.** `graphify-out/.graphify_python` enthielt den absoluten Interpreterpfad des bisherigen Rechners, `graphify-out/.graphify_root` einen absoluten Vault-Pfad; beide wären auf jedem weiteren Gerät falsch gewesen. Zusätzlich ist `graphify-out/cache/` ausgeschlossen: 149 regenerierbare Dateien, die bei der neuen Regel sonst bei jedem Neubau die Historie aufblähen. Alle drei entstehen beim nächsten Lauf neu.

### Geprüfte Auswirkungen

Geprüft und synchronisiert wurden: `AGENTS.md`, [[00-start/03-update-protocol.md]], `.gitignore` und die Graph-Artefakte unter `graphify-out/`. Inhaltliche Fachnotizen sind unverändert; die Änderung betrifft ausschließlich Ablage und Arbeitsablauf.

Offen: Der Graph meldet 35 schwach verbundene Knoten und mehrere AMBIGUOUS-Kanten, unter anderem zwischen `Messplan` und [[10-strategy/information-density-and-mobile-clarity.md]]. Das ist ein Hinweis auf fehlende Querverweise zwischen Notizen, nicht auf einen Graphfehler, und gehört bei Gelegenheit in die [[98-maintenance/review-queue.md]].
