# DESIGN.md

## Color

Tinted neutrals plus one accent. Strategy: **Restrained**. The accent stays under 10% of any given surface.

### Global tokens (in `styles.css`)

| Role | Value | Notes |
|---|---|---|
| `--bg-color` | `#0A0A0B` | Base. Replaces pure black. |
| `--bg-elevated` | `#111113` | One step up for elevated surfaces. |
| `--text-primary` | `#EDEDED` | Off-white. Never `#fff`. |
| `--text-secondary` | `#A0A0A8` | Body copy and muted labels. |
| `--text-tertiary` | `#6E6E78` | Mono labels, captions, disabled. |
| `--card-border` | `rgba(255,255,255,0.07)` | All structural borders. |
| `--card-bg` | `rgba(255,255,255,0.025)` | Subtle elevated tint. |
| `--card-hover` | `rgba(255,255,255,0.05)` | Hover state. |
| `--accent-1` | `#E90074` | Saturated magenta. The single brand color. |
| `--accent-1-soft` | `rgba(233,0,116,0.12)` | Soft fills, hover backdrops, glow tints. |

### Where magenta appears (under 10% rule)

- Active nav state underline
- Primary CTA fill
- `.case-eyebrow` and `.case-rule__label` mono labels
- The `.dot` after the name in the hero
- `.accent-mark` highlight on the hero keyword
- Persona avatar letter color
- Inline link color

### Per-case scoped palettes

Components representing client brands use scoped CSS variables to swap context without polluting global tokens.

- **XP** (`.phone-mock`): `--mock-accent: #FFCC00` (XP yellow), screen base `#0A0A0C`.
- **XP poster** (`.case-thumb-xp`): `#FFCC00` background plus near-black foreground.
- **INFLUO poster** (`.case-thumb-influo`): `#15091F` to `#0A050F` gradient with `#FF7A59` coral accent.
- **Attar poster** (`.case-thumb-attar`): navy and violet gradient with cyan plus purple highlights, mirroring Attar's original brand.

## Typography

| Family | Use | Source |
|---|---|---|
| **Outfit** | Display, headings, eyebrows | Google Fonts. Geometric sans, anti-Inter choice. |
| **Inter Tight** | Body, paragraphs, UI text | Google Fonts. |
| **JetBrains Mono** | Numbers, labels, metadata, mono badges | Google Fonts. |

```css
--font-heading: 'Cabinet Grotesk', 'Outfit', system-ui, sans-serif;
--font-body: 'Inter Tight', 'Inter', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', ui-monospace, monospace;
```

Headings use weight 500 (never 700). Letter-spacing tightens at scale: `-0.02em` to `-0.035em`. Body line-height 1.6, max-width 60 to 65ch. Hierarchy is built from scale plus weight contrast (≥1.25 ratio between steps), not just one or the other.

## Motion

Easing: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-quart-ish). No bounce, no elastic, no linear.

Durations (in `styles.css`):

- `--transition-fast`: 0.18s. Small UI feedback.
- `--transition-medium`: 0.32s. Component-level transitions.
- `--transition-slow`: 0.6s. Layout transitions and card morphs.

Animatable properties: `transform`, `opacity`, `border-color`, `background`. Never `width`, `height`, `top`, `left`.

Scroll reveals: JS injects `--stagger-index` on grid children, CSS applies delay `calc(var(--stagger-index) * 70ms + 120ms)` when the parent enters the viewport. `prefers-reduced-motion` is respected.

## Elevation

Cards use a Liquid Glass refraction recipe:

- 1px outer border at `var(--card-border)`.
- 1px inset highlight `rgba(255,255,255,0.06)` for the top edge.
- Optional 1px tinted shadow on the bottom for depth.

No drop shadows on text or icons. No glow shadows. No outer glows on buttons.

## Layout

- Container: `max-width: 1200px; padding: 0 5%;`. Centered.
- Section spacing: 100px desktop, scales down on mobile.
- Bento grid for cases: 6-column CSS Grid. Row 1 splits 4 plus 2. Row 2 spans 6 (full) when there are 3 cards, splits 3 plus 3 when there are 4.
- Hero: `min-height: 100dvh`. Never `100vh`.
- Mobile breakpoints: 968px (collapse to single column above), 768px (hamburger menu), 600px (further compaction).

## Components

### Navbar

Top of page: full-width, transparent. On scroll past 50px it morphs into a centered 880px pill: `border-radius: 999px`, glassy bg `rgba(15,15,17,0.72)` with 20px blur and 140% saturate, 1px inset highlight. Easing matches `--transition-slow`.

### Buttons

- `.btn-primary`: magenta fill, 1px white-04 border, inset highlight. Hover lifts -1px translateY plus a lighter shade. Active resets translate. No glow shadows.
- `.btn-secondary`: transparent, 1px card-border, hover lifts background to `var(--card-hover)`.

### Cards

`.glass-card`: subtle tinted bg, 1px border, 18px radius, inset highlight. Used sparingly. Never nest cards.

### Cases

Around 30 shared classes for case study pages: `.case-eyebrow`, `.case-rule`, `.case-callout`, `.case-prose`, `.case-arrow-list`, `.case-info-strip`, `.case-feature-grid`, `.case-grid-2`, `.case-grid-3`, `.case-grid-mixed`, `.case-final`, `.case-hero`, `.bilingual-card`, `.persona-card`, `.mockup-showcase`, `.case-phases` plus `.phase`, etc. All scoped under `.case-study` parent.

### Coded mockups

`.phone-mock` is a self-contained iPhone-style mockup. CSS-only, scoped variables, swap brand by overriding `--mock-accent`. Used in case-xp hero and prototype sections.

### Case poster covers

`.case-thumb-xp`, `.case-thumb-influo`, `.case-thumb-attar`: stylized brand posters used as bento card covers. Each has its own CSS variables for brand colors. Format is consistent (top-left mono number, top-right chip, big wordmark, bottom mono labels) but palette is brand-specific.

## Iconography

- Inline SVG only. No icon font, no react-icons (this is vanilla JS).
- Stroke 1.6 to 2.0, rounded caps and joins.
- Single color (currentColor or scoped accent).
- 14 to 24px sizes.

## Don't

- `#000` or `#fff`. Always tinted.
- `border-left` or `border-right` greater than 1px as a colored accent. Use full borders, leading icons, or nothing.
- `background-clip: text` with a gradient.
- Glassmorphism as default decoration.
- Three-equal-card grids.
- Centered hero by default.
- Inline `<style>` blocks in HTML. Everything goes in `styles.css`.
- Inline `style="..."` attributes for anything reusable. Promote to a class.
- Em dashes in copy. Use commas, colons, semicolons, periods, or parentheses.
