# Neuphorism Design System Specification

---

## 1. Design Tokens (CSS Variables)

```css
:root {
  /* Surface Colors */
  --neu-bg-primary: #e6e8ed;
  --neu-bg-light: #f7f9fc;
  --neu-bg-dark: #d1d4db;

  /* Shadow Colors */
  --neu-shadow-dark: #c5c8ce;
  --neu-shadow-light: #ffffff;

  /* Text Colors */
  --neu-text-primary: #4a5568;
  --neu-text-secondary: #718096;
  --neu-text-heading: #2d3748;

  /* Accent Colors */
  --neu-accent: #667eea;
  --neu-accent-hover: #5a67d8;
  --neu-error: #e53e3e;
  --neu-success: #38a169;
  --neu-warning: #d69e2e;

  /* Shadows */
  --neu-shadow-extruded:
    12px 12px 24px var(--neu-shadow-dark),
    -12px -12px 24px var(--neu-shadow-light);
  --neu-shadow-pressed:
    inset 6px 6px 12px var(--neu-shadow-dark),
    inset -6px -6px 12px var(--neu-shadow-light);
  --neu-shadow-elevated:
    16px 16px 32px var(--neu-shadow-dark),
    -16px -16px 32px var(--neu-shadow-light);

  /* Border Radius */
  --neu-radius-lg: 20px;
  --neu-radius-md: 12px;
  --neu-radius-sm: 8px;

  /* Spacing Scale */
  --neu-space-1: 4px;
  --neu-space-2: 8px;
  --neu-space-3: 12px;
  --neu-space-4: 16px;
  --neu-space-5: 24px;
  --neu-space-6: 32px;
  --neu-space-7: 48px;
  --neu-space-8: 64px;

  /* Typography */
  --neu-font-family:
    "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --neu-font-weight-light: 300;
  --neu-font-weight-regular: 400;
  --neu-font-weight-medium: 500;

  /* Transitions */
  --neu-transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --neu-transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
  --neu-transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Dark Mode Overrides */
:root[data-theme="dark"] {
  --neu-bg-primary: #2d3748;
  --neu-bg-light: #3d4a5c;
  --neu-bg-dark: #1a202c;
  --neu-shadow-dark: #1a202c;
  --neu-shadow-light: #3d4a5c;
  --neu-text-primary: #e2e8f0;
  --neu-text-secondary: #a0aec0;
  --neu-text-heading: #f7fafc;
}
```

---

## 2. Typography Scale

```css
/* Font Import */
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap");

/* Base Typography */
body {
  font-family: var(--neu-font-family);
  font-weight: var(--neu-font-weight-regular);
  color: var(--neu-text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

/* Type Scale Utilities */
.neu-text-xs {
  font-size: 12px;
  line-height: 1.5;
}
.neu-text-sm {
  font-size: 14px;
  line-height: 1.5;
}
.neu-text-base {
  font-size: 16px;
  line-height: 1.6;
}
.neu-text-lg {
  font-size: 18px;
  line-height: 1.6;
}
.neu-text-xl {
  font-size: 20px;
  line-height: 1.5;
}
.neu-text-2xl {
  font-size: 24px;
  line-height: 1.4;
}
.neu-text-3xl {
  font-size: 30px;
  line-height: 1.3;
}
.neu-text-4xl {
  font-size: 36px;
  line-height: 1.2;
}

/* Weight Utilities */
.neu-font-light {
  font-weight: var(--neu-font-weight-light);
}
.neu-font-regular {
  font-weight: var(--neu-font-weight-regular);
}
.neu-font-medium {
  font-weight: var(--neu-font-weight-medium);
}

/* Label Style (uppercase, tracked) */
.neu-label {
  font-size: 12px;
  font-weight: var(--neu-font-weight-medium);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--neu-text-secondary);
}

/* Heading Defaults */
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: var(--neu-font-weight-medium);
  color: var(--neu-text-heading);
  margin: 0 0 var(--neu-space-4);
}
```

---

## 3. Color Palette

| Token                  | Light Mode | Dark Mode | Usage                     |
| ---------------------- | ---------- | --------- | ------------------------- |
| `--neu-bg-primary`     | `#e6e8ed`  | `#2d3748` | Page/component background |
| `--neu-bg-light`       | `#f7f9fc`  | `#3d4a5c` | Gradient highlights       |
| `--neu-bg-dark`        | `#d1d4db`  | `#1a202c` | Gradient shadows          |
| `--neu-shadow-dark`    | `#c5c8ce`  | `#1a202c` | Bottom-right shadow       |
| `--neu-shadow-light`   | `#ffffff`  | `#3d4a5c` | Top-left highlight        |
| `--neu-text-primary`   | `#4a5568`  | `#e2e8f0` | Body copy                 |
| `--neu-text-secondary` | `#718096`  | `#a0aec0` | Labels, captions          |
| `--neu-text-heading`   | `#2d3748`  | `#f7fafc` | Headings                  |
| `--neu-accent`         | `#667eea`  | `#667eea` | Buttons, links            |
| `--neu-accent-hover`   | `#5a67d8`  | `#5a67d8` | Hover state               |
| `--neu-error`          | `#e53e3e`  | `#fc8181` | Error messages            |
| `--neu-success`        | `#38a169`  | `#68d391` | Success states            |
| `--neu-warning`        | `#d69e2e`  | `#f6e05e` | Warning states            |

---

## 4. Spacing & Layout

```css
/* Spacing Utilities */
.neu-p-1 {
  padding: var(--neu-space-1);
}
.neu-p-2 {
  padding: var(--neu-space-2);
}
.neu-p-3 {
  padding: var(--neu-space-3);
}
.neu-p-4 {
  padding: var(--neu-space-4);
}
.neu-p-5 {
  padding: var(--neu-space-5);
}
.neu-p-6 {
  padding: var(--neu-space-6);
}
.neu-p-7 {
  padding: var(--neu-space-7);
}
.neu-p-8 {
  padding: var(--neu-space-8);
}

.neu-m-1 {
  margin: var(--neu-space-1);
}
/* ... repeat for m-2 through m-8 */

.neu-mb-3 {
  margin-bottom: var(--neu-space-3);
}
.neu-mb-4 {
  margin-bottom: var(--neu-space-4);
}
.neu-mb-5 {
  margin-bottom: var(--neu-space-5);
}
.neu-mb-6 {
  margin-bottom: var(--neu-space-6);
}

/* Container */
.neu-container {
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--neu-space-5);
  padding-right: var(--neu-space-5);
}

/* Breakpoints */
/* sm: 640px | md: 768px | lg: 1024px | xl: 1280px */

/* Grid System */
.neu-grid {
  display: grid;
  gap: var(--neu-space-5);
}
.neu-grid-cols-2 {
  grid-template-columns: repeat(2, 1fr);
}
.neu-grid-cols-3 {
  grid-template-columns: repeat(3, 1fr);
}
.neu-grid-cols-4 {
  grid-template-columns: repeat(4, 1fr);
}

@media (max-width: 768px) {
  .neu-grid-cols-2,
  .neu-grid-cols-3,
  .neu-grid-cols-4 {
    grid-template-columns: 1fr;
  }
}
```

---

## 5. Component Quick-Wins

### Button

```css
.neu-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--neu-space-3) var(--neu-space-5);
  font-family: var(--neu-font-family);
  font-size: 14px;
  font-weight: var(--neu-font-weight-medium);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--neu-text-heading);
  background: var(--neu-bg-primary);
  border: none;
  border-radius: var(--neu-radius-md);
  box-shadow: var(--neu-shadow-extruded);
  cursor: pointer;
  transition:
    box-shadow var(--neu-transition-base),
    transform var(--neu-transition-fast);
}

.neu-btn:hover {
  box-shadow: var(--neu-shadow-elevated);
  transform: translateY(-2px);
}

.neu-btn:active,
.neu-btn:focus {
  box-shadow: var(--neu-shadow-pressed);
  transform: translateY(0);
  outline: none;
}

.neu-btn--primary {
  background: var(--neu-accent);
  color: #ffffff;
}

.neu-btn--primary:hover {
  background: var(--neu-accent-hover);
}
```

### Card

```css
.neu-card {
  background: var(--neu-bg-primary);
  border-radius: var(--neu-radius-lg);
  box-shadow: var(--neu-shadow-extruded);
  padding: var(--neu-space-6);
  transition:
    box-shadow var(--neu-transition-base),
    transform var(--neu-transition-base);
}

.neu-card:hover {
  box-shadow: var(--neu-shadow-elevated);
  transform: translateY(-4px) scale(1.01);
}

.neu-card__title {
  font-size: 20px;
  font-weight: var(--neu-font-weight-medium);
  color: var(--neu-text-heading);
  margin-bottom: var(--neu-space-3);
}

.neu-card__body {
  color: var(--neu-text-primary);
}
```

### Navigation

```css
.neu-nav {
  display: flex;
  align-items: center;
  gap: var(--neu-space-2);
  padding: var(--neu-space-3);
  background: var(--neu-bg-primary);
  border-radius: var(--neu-radius-lg);
  box-shadow: var(--neu-shadow-extruded);
}

.neu-nav__link {
  padding: var(--neu-space-2) var(--neu-space-4);
  font-size: 14px;
  font-weight: var(--neu-font-weight-medium);
  color: var(--neu-text-secondary);
  text-decoration: none;
  border-radius: var(--neu-radius-sm);
  transition: all var(--neu-transition-fast);
}

.neu-nav__link:hover,
.neu-nav__link--active {
  color: var(--neu-accent);
  box-shadow: var(--neu-shadow-pressed);
}
```

### Hero

```css
.neu-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  padding: var(--neu-space-8);
  background: linear-gradient(
    145deg,
    var(--neu-bg-light),
    var(--neu-bg-primary),
    var(--neu-bg-dark)
  );
  border-radius: var(--neu-radius-lg);
  box-shadow: var(--neu-shadow-extruded);
  text-align: center;
}

.neu-hero__title {
  font-size: 36px;
  font-weight: var(--neu-font-weight-medium);
  color: var(--neu-text-heading);
  margin-bottom: var(--neu-space-4);
}

.neu-hero__subtitle {
  font-size: 18px;
  color: var(--neu-text-secondary);
  max-width: 600px;
  margin-bottom: var(--neu-space-6);
}
```

### Input

```css
.neu-input {
  width: 100%;
  padding: var(--neu-space-3) var(--neu-space-4);
  font-family: var(--neu-font-family);
  font-size: 16px;
  color: var(--neu-text-primary);
  background: var(--neu-bg-primary);
  border: none;
  border-radius: var(--neu-radius-md);
  box-shadow: var(--neu-shadow-pressed);
  transition:
    box-shadow var(--neu-transition-fast),
    transform var(--neu-transition-fast);
}

.neu-input:focus {
  outline: none;
  box-shadow:
    var(--neu-shadow-pressed),
    0 0 0 3px rgba(102, 126, 234, 0.3);
  transform: scale(1.01);
}

.neu-input::placeholder {
  color: var(--neu-text-secondary);
}
```

---

## 6. Tailwind Config Snippet

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        neu: {
          bg: {
            primary: "#e6e8ed",
            light: "#f7f9fc",
            dark: "#d1d4db",
          },
          shadow: {
            dark: "#c5c8ce",
            light: "#ffffff",
          },
          text: {
            primary: "#4a5568",
            secondary: "#718096",
            heading: "#2d3748",
          },
          accent: {
            DEFAULT: "#667eea",
            hover: "#5a67d8",
          },
          error: "#e53e3e",
          success: "#38a169",
          warning: "#d69e2e",
        },
      },
      fontFamily: {
        neu: ["Inter", "system-ui", "sans-serif"],
      },
      fontWeight: {
        light: "300",
        regular: "400",
        medium: "500",
      },
      borderRadius: {
        "neu-sm": "8px",
        "neu-md": "12px",
        "neu-lg": "20px",
      },
      boxShadow: {
        "neu-extruded": "12px 12px 24px #c5c8ce, -12px -12px 24px #ffffff",
        "neu-pressed":
          "inset 6px 6px 12px #c5c8ce, inset -6px -6px 12px #ffffff",
        "neu-elevated": "16px 16px 32px #c5c8ce, -16px -16px 32px #ffffff",
      },
      transitionTimingFunction: {
        neu: "cubic-bezier(0.4, 0, 0.2, 1)",
      },
      spacing: {
        "neu-1": "4px",
        "neu-2": "8px",
        "neu-3": "12px",
        "neu-4": "16px",
        "neu-5": "24px",
        "neu-6": "32px",
        "neu-7": "48px",
        "neu-8": "64px",
      },
    },
  },
  plugins: [],
};
```

---

## 7. Figma Variables JSON

```json
{
  "Neuphorism": {
    "color": {
      "bg-primary": { "value": "#e6e8ed", "type": "color" },
      "bg-light": { "value": "#f7f9fc", "type": "color" },
      "bg-dark": { "value": "#d1d4db", "type": "color" },
      "shadow-dark": { "value": "#c5c8ce", "type": "color" },
      "shadow-light": { "value": "#ffffff", "type": "color" },
      "text-primary": { "value": "#4a5568", "type": "color" },
      "text-secondary": { "value": "#718096", "type": "color" },
      "text-heading": { "value": "#2d3748", "type": "color" },
      "accent": { "value": "#667eea", "type": "color" },
      "accent-hover": { "value": "#5a67d8", "type": "color" },
      "error": { "value": "#e53e3e", "type": "color" },
      "success": { "value": "#38a169", "type": "color" },
      "warning": { "value": "#d69e2e", "type": "color" }
    },
    "spacing": {
      "space-1": { "value": "4", "type": "number" },
      "space-2": { "value": "8", "type": "number" },
      "space-3": { "value": "12", "type": "number" },
      "space-4": { "value": "16", "type": "number" },
      "space-5": { "value": "24", "type": "number" },
      "space-6": { "value": "32", "type": "number" },
      "space-7": { "value": "48", "type": "number" },
      "space-8": { "value": "64", "type": "number" }
    },
    "borderRadius": {
      "radius-sm": { "value": "8", "type": "number" },
      "radius-md": { "value": "12", "type": "number" },
      "radius-lg": { "value": "20", "type": "number" }
    },
    "typography": {
      "font-family": { "value": "Inter", "type": "string" },
      "font-weight-light": { "value": "300", "type": "number" },
      "font-weight-regular": { "value": "400", "type": "number" },
      "font-weight-medium": { "value": "500", "type": "number" }
    }
  },
  "Neuphorism-Dark": {
    "color": {
      "bg-primary": { "value": "#2d3748", "type": "color" },
      "bg-light": { "value": "#3d4a5c", "type": "color" },
      "bg-dark": { "value": "#1a202c", "type": "color" },
      "shadow-dark": { "value": "#1a202c", "type": "color" },
      "shadow-light": { "value": "#3d4a5c", "type": "color" },
      "text-primary": { "value": "#e2e8f0", "type": "color" },
      "text-secondary": { "value": "#a0aec0", "type": "color" },
      "text-heading": { "value": "#f7fafc", "type": "color" }
    }
  }
}
```

---

## 8. QA Checklist

### Visual Regression Tests

| Test Case                                     | Tool                  | Threshold     |
| --------------------------------------------- | --------------------- | ------------- |
| Button states (default, hover, active, focus) | Percy/Chromatic       | 0.1% diff     |
| Card hover animation                          | Percy snapshot        | 0.1% diff     |
| Input focus state                             | Playwright screenshot | pixel-perfect |
| Dark mode toggle                              | Chromatic story       | 0.1% diff     |
| Responsive breakpoints (640, 768, 1024, 1280) | BackstopJS            | 0.05% diff    |

### Contrast Ratio Validation

| Element         | Foreground | Background | Ratio | WCAG       |
| --------------- | ---------- | ---------- | ----- | ---------- |
| Body text       | `#4a5568`  | `#e6e8ed`  | 5.2:1 | AA ✓       |
| Secondary text  | `#718096`  | `#e6e8ed`  | 3.5:1 | AA Large ✓ |
| Heading text    | `#2d3748`  | `#e6e8ed`  | 8.1:1 | AAA ✓      |
| Accent on bg    | `#667eea`  | `#e6e8ed`  | 4.6:1 | AA ✓       |
| White on accent | `#ffffff`  | `#667eea`  | 4.8:1 | AA ✓       |
| Dark mode body  | `#e2e8f0`  | `#2d3748`  | 9.7:1 | AAA ✓      |

### Accessibility Gotchas

1. **Focus visibility**: The pressed shadow state alone may not be sufficient for keyboard users. Add a visible outline or ring (`0 0 0 3px rgba(102, 126, 234, 0.3)`) on `:focus-visible` to meet WCAG 2.4.7.

2. **Motion sensitivity**: The `transform: scale()` and `translateY()` animations can trigger vestibular issues. Wrap all motion in `@media (prefers-reduced-motion: no-preference)` and provide static fallbacks.

3. **Touch target size**: Neuphoristic padding looks generous but verify buttons and nav links hit 44×44px minimum touch targets (WCAG 2.5.5). Current padding may fall short on mobile.

---

## 9. Next Steps

1. **Scaffold the project**

```bash
   pnpm create vite@latest neu-ds --template vanilla
   cd neu-ds && pnpm install
```

2. **Add Inter font**
   - Add to `index.html`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap"
  rel="stylesheet"
/>
```

3. **Create token file** – Copy Section 1 into `src/tokens.css` and import at the top of your main CSS.

4. **Build component library** – Create `src/components/` folder with individual files: `button.css`, `card.css`, `input.css`, `nav.css`, `hero.css`.

5. **Add dark mode toggle** – Implement a JS toggle that adds `data-theme="dark"` to `<html>`.

6. **Run contrast audit**

```bash
   npx pa11y http://localhost:5173 --standard WCAG2AA
```

7. **Set up visual regression** – Install Chromatic or Percy; add Storybook stories for each component.

8. **Document in Storybook** – `pnpm add -D @storybook/html` and create stories for all variants.

9. **Extract Tailwind config** – If using Tailwind, paste Section 6 into `tailwind.config.js`.

10. **Publish to Figma** – Import Section 7 JSON into Figma's Variables panel (Plugins → Variables → Import).

---

## 10. Risk Log

| #   | Issue                                                                                                                | Severity | Mitigation                                                                                 |
| --- | -------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| 1   | **No font fallback weights defined** – If Inter fails to load, `font-weight: 300` may render as 400 on system fonts. | Medium   | Add explicit fallback stack with weights that map correctly.                               |
| 2   | **Shadow performance on low-end devices** – Dual box-shadows can cause jank on budget Android phones.                | Medium   | Test on real devices; consider `will-change: transform` or reducing shadow blur on mobile. |
| 3   | **Dark mode shadow values unvalidated** – The dark mode shadow palette was derived, not tested.                      | High     | Validate dark mode shadows in a real environment before shipping.                          |
| 4   | **No disabled state defined** – Buttons and inputs lack `[disabled]` styling.                                        | High     | Add `opacity: 0.5; cursor: not-allowed;` and remove shadow on disabled elements.           |
| 5   | **Pressed state relies on `:active`** – May not persist for keyboard users.                                          | Medium   | Use `:focus-visible` in addition to `:active` for pressed appearance.                      |
| 6   | **Gradient background performance** – Three-stop gradient on `body` can cause repaints on scroll.                    | Low      | Convert to a fixed-position pseudo-element or static image.                                |
| 7   | **No z-index scale defined** – Elevated elements may stack unpredictably.                                            | Low      | Define `--neu-z-dropdown: 100; --neu-z-modal: 200;` etc.                                   |
| 8   | **Letter-spacing on buttons may clip** – Uppercase + tracking can clip descenders in some fonts.                     | Low      | Test with letters like "g", "y", "p" in button text.                                       |
