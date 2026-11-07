# Befund: INIZIO Solar

Quelle: https://sixth-powder-95605714.figma.site/ · gemessen 2026-11-07 vom Nutzer in seinem Chrome über die Chrome-Erweiterung · Werte in `messung.json`.
Kennzeichnung: **[M]** gemessen, **[A]** abgeleitet oder geschätzt.

## Gemessen

- [M] Figma Make, React, Tailwind v4. Root 14 px; alle rem-Werte und Breakpoints ×14.
- [M] Inhalt hat sich seit August geändert: Der Auftakt heißt „Powering the Future with Sustainable Tech“.
- [M] Space Grotesk 700/600 für H1/H2, Outfit 500/600 für H3, Navigation und Knöpfe, Inter für Text.
- [M] Signalfarbe #39ec2a, Grund #0a0a0a und #1a1a1a, Grau #888; Abschnitte wechseln hell und dunkel.
- [M] Auftakt: Vollbildfoto mit Abdunklung `matte-black/70`, Inhalt zentriert, zwei Knöpfe 57 px hoch.
- [M] Hover, alle 300 ms `cubic-bezier(.4,0,.2,1)`: Leistungskachel `scale` 1,05 mit Eckkreis 1,5 und Deckkraft .2 → .1; Nav-Unterstrich `scale-x` 0 → 1; Pfeil 3,5 px; Service-Zeile Kachel 10 → 20 %, Titel Signalfarbe; Wert-Kachel gefüllt und 1,1; Footer-Link 3,5 px; Social-Kachel 1,1.
- [M] Kein Reveal, kein Parallax, keine Scrollanimation; nur die Navigation klebt. Das Mobilmenü öffnet ohne Animation.
- [M] Glow-Klassen und `hover:neon-green` stehen im CSS, wirken aber nicht.

## Geschätzt

- [A] Stimmenkarte `hover:shadow-lg` und `scale-105`, nur aus den Klassen gelesen.
- [A] Farbe des Eckkreises in der Vorlage: schwarz auf gefüllter, Signalfarbe auf grauer Kachel.

## Übertragen in `web-kit/vorlagen/signal/`

Der Nutzer hat die Seite insgesamt „stark“ genannt, deshalb eine Vorlage nach [[90-references/inspiration-eingang.md#Verarbeiten]]: Vollbild-Leitbild mit 70 % Abdunklung, eine Signalfarbe auf fast schwarzem Grund, Wechsel hell und dunkel, abwechselnd gefüllte Leistungskacheln mit Hover, Ablaufliste mit Icon-Kachel-Hover, Unterstrich-Hover der Navigation, drei Schriften mit fester Rolle. Am 2026-11-07 nachgemessen: Hover und Scrollverhalten stimmen.

## Nicht übertragen

Overline-Kicker, Badge-Pille über der H1, animierter Verlauf in Überschriften, zweites Wort der H2 in Signalfarbe, Kennzahlen ohne Beleg (10+, 5000+, 50 MW, 500+, 98 %, 99,9 %, 25yr), Kundenstimmen, Glas-Kennzahlenkarte, Deko-Kreise, Scroll-Indikator mit Dauer-Bounce, Verlauf auf Fotos. Grautext auf Weiß ist dunkler gesetzt (Kontrast AA). Fotos und Logo bleiben beim Original; das About-Foto zeigt ein Dashboard statt Solar.

## Schwächen des Originals

Mobil ist der Auftakt höher als der Bildschirm, die Badge rutscht unter die Navigation.

## Screenshots

Das ZIP `figma-messung-screenshots-2026-11-07.zip` lag beim Ablegen nicht auf dem Server. Wenn es nachgeliefert wird, gehören die Bilder als WebP in `screenshots/`.
