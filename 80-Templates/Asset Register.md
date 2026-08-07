---
type: template
status: canonical
updated: 2026-08-05
---

# Asset Register

Ein Block pro Asset:

- ID/Datei:
- Typ und Einsatzorte:
- Quelle, Autor, Download-Datum:
- sichtbare Lizenzname, Version, direkte Lizenz-URL oder Hinweis, soweit vorhanden:
- beobachtete Nutzungs-/Attributionsangabe, soweit sichtbar:
- tatsächliche Übernahme: `used | adapted | copied` und Bearbeitungsschritte:
- Bildrolle nach [[20-Design/Imagery and AI Editing#Bildrollen]]: `Leitbild | Beweisbild | Objektbild | Kontextbild | Struktur`:
- durchgeführte Bearbeitung, einzeln benannt, etwa `hochskaliert 2x`, `freigestellt`, `Perspektive korrigiert`, `Hintergrund ersetzt`, `Farbe angeglichen`, `Fremdmarke retuschiert`:
- bei KI-Erzeugung: Modell, Prompt, Erzeugungsdatum und ob `ai-placeholder`:
- bei `ai-placeholder`: Einsatzort, Seitenverhältnis, Dateipfad und Hinweis für die spätere Ersetzung:
- Serienzugehörigkeit und geprüfte Konsistenz zu den übrigen Bildern der Website:
- Remote oder self-hosted; Datenschutzfolge:
- Optimierte Varianten und Fallback:
- Nutzer/Owner, nicht blockierender Status und Review-/Entscheidungsdatum:
- Quelleneintrag und Prüfhinweis in `SOURCE-RIGHTS-REVIEW.md`:

Erlaubte Status: `used`, `adapted`, `copied`, `ai-generated`, `ai-placeholder`, `owner-review-pending`, `owner-reviewed`, `removed-by-user`. `ai-placeholder` bedeutet: Das Bild ist auf der Website vollwertig im Einsatz und wird dort nicht gekennzeichnet; der Nutzer kann es später gegen ein reales Bild tauschen. Jeder Status beschreibt nur den tatsächlichen Einsatz oder die spätere Einschätzung. Er darf keine Website, kein Asset, keine Animation, kein Deployment und keine Veröffentlichung durch die KI sperren oder ersetzen.
