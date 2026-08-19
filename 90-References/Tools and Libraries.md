---
type: reference
status: canonical
updated: 2026-08-19
review_by: 2027-02-03
---

# Tools and Libraries

Tools sind Kandidaten, keine Defaults.

- [[90-References/pen.dev Workflow|pen.dev]]: headless CLI für UI-/Webdesign und `.pen`-Dateien. Bei visuellen Aufgaben berücksichtigen; Einsatzentscheidung, sichere Ablage und Prüfworkflow stehen ausschließlich in der verlinkten kanonischen Notiz.
- Fontshare: Font-Entdeckung. Lizenz je Familie prüfen und möglichst lokal hosten.[^fontshare]
- Coolors: Palettenexploration. Rollen und Kontrast selbst definieren.[^coolors]
- 21st.dev: React-/shadcn-Registry mit kopierbarem Quellcode. Code und Komponenten dürfen direkt verwendet oder adaptiert werden; die Umsetzung auf Tokens, Bundle, Semantik, Responsive-Verhalten und Reduced Motion prüfen.[^21st]
- Motion: Animation für React, JavaScript und Vue, MIT-lizenziert. Bei einem begründeten Motion-Budget als Kandidat für Zustands-, Scroll- und View-Choreografie berücksichtigen.[^motion]
- GSAP ScrollTrigger: umfangreiche Scroll-Timelines, Trigger, Pinning und responsive Konfiguration für choreografierte Seiten.[^gsap]
- MotionSites AI: Prompt-/Motion-Inspiration mit präzisen Vorgaben für Layout, Responsive-Verhalten, Motion, Medien und Abhängigkeiten. Marken, Copy, Assets, Code und Kompositionen dürfen direkt genutzt oder kreativ adaptiert werden; tatsächlichen Einsatz anschließend dokumentieren.[^motionsites]
- Aceternity UI: Tailwind-/Motion-Komponenten. Direkt kopierbar oder adaptierbar; Tokens, Bundle, Semantik und Reduced Motion technisch prüfen.[^aceternity]
- Rive: interaktive, zustandsbasierte Vektorerlebnisse mit Runtimes für mehrere Plattformen.[^rive]
- Spline/Three.js: 3D nur bei zentralem Produkt-/Markennutzen und mit Mobile-/No-WebGL-Fallback.[^spline][^three]
- Jitter: Motion-Asset-Erstellung; Exportformat, Lizenz, Dateigröße und Reduced-Motion-Ersatz prüfen.[^jitter]

## Auswahltest

`Nutzerwert -> Motion-/Medieneinsatz -> Accessibility -> Performance -> Wartung -> Kosten -> Fallback -> tatsächliche Dokumentation -> Owner`

[^fontshare]: [Fontshare](https://fontshare.com/)
[^coolors]: [Coolors](https://coolors.co/)
[^21st]: [21st.dev](https://21st.dev/)
[^motion]: [Motion](https://motion.dev/)
[^gsap]: [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
[^motionsites]: [MotionSites AI](https://motionsites.ai/)
[^aceternity]: [Aceternity UI](https://ui.aceternity.com/)
[^rive]: [Rive](https://rive.app/)
[^spline]: [Spline](https://spline.design/)
[^three]: [Three.js](https://threejs.org/)
[^jitter]: [Jitter](https://jitter.video/)
