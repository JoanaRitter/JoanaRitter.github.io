# PRODUCT.md

## Register

**brand**. This is a personal portfolio site. The design IS the product.

## Users

Primary audiences, in priority order:

1. **Hiring managers and design leads** at Brazilian and international tech companies (fintechs, AI/ML startups, design-engineering shops). They skim 4 to 8 portfolios per session and decide in 30 to 60 seconds whether to read any case study.
2. **Product Managers and engineers** evaluating Joana for cross-functional collaboration. They care about the depth of UX rationale, not pretty pictures. They want to see the visible thinking behind decisions.
3. **Conference and podcast organizers, journalists** following Joana's work in AI product design.

All audiences are bilingual-aware (PT-BR plus EN). Most browse on desktop, with secondary mobile checks.

## Product purpose

A senior portfolio that demonstrates Joana Ritter as a Senior Product Designer at the intersection of AI, complex products, and Interface Engineering. The site itself must be the proof, not screenshots. Living interface evidence: coded prototypes, refined typography, considered motion.

Goals, in order:

1. Convince a senior reader within 8 seconds that this is a credible Senior Product Designer.
2. Make case studies easy to scan but rewarding to read end-to-end.
3. Show range (AI products, fintech, mobile, creator marketing) without diluting focus.

## Brand

Visual register: editorial-tech, closer to Linear and Vercel docs than to Webflow templates. Dark-first with a single bold accent (magenta). Typography does the heavy lifting. Decoration is restrained.

Voice: first-person, calm, confident. Jargon only when it adds precision. Bilingual (PT-BR primary, EN mirror) with the same content density on both sides. Avoids buzzwords ("seamless", "elevate", "unleash", "next-gen").

## Tone

Quiet authority, not loud claims. Show the work, not the badges. Numbers when honest, prose when more honest.

## Anti-references

What this portfolio explicitly is NOT:

- **Generic agency-creative aesthetic.** No huge full-bleed video, no parallax illustrations, no scroll-jacking, no vapor wave gradients.
- **AI-purple SaaS look.** No Inter, no neon purple gradients, no glassmorphism everywhere, no hero metric template.
- **Behance template feel.** No 3-equal-column case grid, no screenshot-only case studies with no rationale.
- **Cyan and purple AI tropes** (the LILA-BAN territory).

References that DO match the spirit:

- Linear product pages (precision typography, restrained motion).
- Vercel blog (editorial rhythm, monospace for metadata).
- Rauno's portfolio at rauno.me (component-level craft as the showcase).
- Emil Kowalski at emilkowal.ski (micro-interaction philosophy).

## Strategic principles

1. **Coded over rendered.** Where possible, mockups are real HTML and CSS components, not PNG screenshots. The portfolio itself is the work.
2. **One brand per surface.** Portfolio chrome stays magenta and zinc. Case-specific surfaces (XP poster, Attar poster) use their own brand palettes scoped locally. Never blend.
3. **Bilingual parity.** Every PT page has an EN twin. Same content density, same depth.
4. **No AI slop.** Match-and-refuse on the absolute bans: no gradient text, no side-stripe borders, no glassmorphism reflexes, no hero-metric template, no pure black, no pure white.
5. **Mobile gets the same care.** No degraded mobile copy. Use `100dvh`, single-column collapse, no horizontal scroll.

## Constraints

- Static HTML, CSS, and vanilla JS. No build step, no framework. Hosted on GitHub Pages.
- Single shared `styles.css` across all surfaces. Page-specific overrides via scoped class modifiers, never inline styles or per-page `<style>` blocks.
- 16 HTML files (8 PT, 8 EN). Any pattern change must be replicable across the matrix.
- PT-BR primary, EN secondary, with identical visual structure.
