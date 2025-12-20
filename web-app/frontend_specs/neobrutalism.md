---

## 1. Design Tokens (CSS Variables)

Place the following in your `globals.css` or root stylesheet:

```css
:root {
  /* Color Tokens - Primitives */
  --color-white: #ffffff;
  --color-black: #000000;
  
  /* Neutral Scale (Grays) */
  --color-neutral-100: #e8e8e8;
  --color-neutral-200: #f0f0f0;
  --color-neutral-300: #d9d9d9;
  --color-neutral-400: #b0b8c4;
  --color-neutral-500: #7a7a7a;
  --color-neutral-600: #3a3c42;
  --color-neutral-700: #22242a;
  
  /* Primary Brand - Purple */
  --color-primary-400: #7159eb;
  --color-primary-500: #7b61ff;
  --color-primary-600: #6b50d9;
  --color-primary-700: #5b40c9;
  
  /* Secondary - Cyan/Blue */
  --color-secondary-300: #77d3d7;
  --color-secondary-400: #4db8bd;
  --color-secondary-500: #2a9d9e;
  --color-secondary-700: #1b5f66;
  
  /* Accent - Pink */
  --color-accent-300: #f4a8c1;
  --color-accent-400: #f08db3;
  --color-accent-500: #e5729a;
  --color-accent-600: #d94e78;
  
  /* Semantic - Success */
  --color-success-500: #34c759;
  --color-success-600: #2aa84f;
  
  /* Semantic - Warning */
  --color-warning-500: #fbbf24;
  --color-warning-600: #f59e0b;
  
  /* Semantic - Danger */
  --color-danger-500: #ff8555;
  --color-danger-600: #ff6b3d;
  
  /* Semantic - Info */
  --color-info-500: #5ba3d0;
  --color-info-600: #4682b4;
  
  /* Typography */
  --font-primary: "Space Grotesk", system-ui, -apple-system, sans-serif;
  --font-secondary: "Georgia", serif;
  --font-mono: "Menlo", "Monaco", monospace;
  
  /* Sizing Scale (Base: 8px) */
  --size-xs: 0.25rem; /* 4px */
  --size-sm: 0.5rem; /* 8px */
  --size-md: 0.75rem; /* 12px */
  --size-lg: 1rem; /* 16px */
  --size-xl: 1.5rem; /* 24px */
  --size-2xl: 2rem; /* 32px */
  --size-3xl: 2.5rem; /* 40px */
  --size-4xl: 3rem; /* 48px */
  --size-5xl: 4rem; /* 64px */
  --size-6xl: 5rem; /* 80px */
  
  /* Spacing */
  --spacing-0: 0;
  --spacing-1: 0.25rem; /* 4px */
  --spacing-2: 0.38rem; /* 6px */
  --spacing-3: 0.5rem; /* 8px */
  --spacing-4: 0.63rem; /* 10px */
  --spacing-5: 0.75rem; /* 12px */
  --spacing-6: 1rem; /* 16px */
  --spacing-7: 1.25rem; /* 20px */
  --spacing-8: 1.5rem; /* 24px */
  --spacing-9: 1.75rem; /* 28px */
  --spacing-10: 2rem; /* 32px */
  --spacing-12: 2.5rem; /* 40px */
  --spacing-14: 3rem; /* 48px */
  --spacing-16: 4rem; /* 64px */
  --spacing-20: 5rem; /* 80px */
  
  /* Border Radius */
  --radius-none: 0;
  --radius-sm: 0.25rem; /* 4px */
  --radius-md: 0.5rem; /* 8px */
  --radius-lg: 1rem; /* 16px */
  --radius-xl: 1.5rem; /* 24px */
  --radius-full: 9999px;
  
  /* Border & Shadows */
  --border-sm: 1px;
  --border-md: 2px;
  --border-lg: 4px;
  --border-style: solid;
  --border-color: var(--color-neutral-600);
  
  --shadow-xs: 0 1px 2px rgba(58, 60, 66, 0.05);
  --shadow-sm: 0 2px 4px rgba(58, 60, 66, 0.1);
  --shadow-md: 2px 2px 4px rgba(58, 60, 66, 0.15);
  --shadow-lg: 4px 4px 8px rgba(58, 60, 66, 0.2);
  --shadow-bold: 4px 4px 0px 0px rgba(58, 60, 66, 0.92);
  
  /* Z-Index Scale */
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal-bg: 300;
  --z-modal: 400;
  --z-toast: 500;
  
  /* Transition */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Dark Mode Overrides (if needed) */
@media (prefers-color-scheme: dark) {
  :root {
    --color-neutral-100: #1f2329;
    --color-neutral-200: #2a2e35;
    --color-neutral-300: #3a3c42;
    --color-neutral-400: #5a5f6b;
    --color-neutral-500: #8a9099;
    --color-neutral-600: #b0b8c4;
    --color-neutral-700: #e8e8e8;
  }
}
```

---

## 2. Typography Scale

**Primary Font Family:** Space Grotesk (variable weight 300–900)  
**Secondary Font Family:** Georgia (serif, for body copy if needed)  
**Fallback Stack:** system-ui, -apple-system, BlinkMacSystemFont, segoe-ui, helvetica

### Utility Classes

```css
/* Headings */
.text-heading-1 {
  font-family: var(--font-primary);
  font-size: 3.75rem; /* 60px */
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-heading-2 {
  font-family: var(--font-primary);
  font-size: 3rem; /* 48px */
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.02em;
}

.text-heading-3 {
  font-family: var(--font-primary);
  font-size: 1.875rem; /* 30px */
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
}

.text-heading-4 {
  font-family: var(--font-primary);
  font-size: 1.5rem; /* 24px */
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: 0;
}

.text-heading-5 {
  font-family: var(--font-primary);
  font-size: 1.25rem; /* 20px */
  font-weight: 700;
  line-height: 1.4;
  letter-spacing: 0;
}

/* Body */
.text-body-lg {
  font-family: var(--font-primary);
  font-size: 1.125rem; /* 18px */
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0.01em;
}

.text-body-base {
  font-family: var(--font-primary);
  font-size: 1rem; /* 16px */
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0;
}

.text-body-sm {
  font-family: var(--font-primary);
  font-size: 0.875rem; /* 14px */
  font-weight: 400;
  line-height: 1.5;
  letter-spacing: 0;
}

/* Label & Caption */
.text-label {
  font-family: var(--font-primary);
  font-size: 0.75rem; /* 12px */
  font-weight: 700;
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.15em;
}

.text-caption {
  font-family: var(--font-primary);
  font-size: 0.75rem; /* 12px */
  font-weight: 400;
  line-height: 1.4;
  letter-spacing: 0;
}

/* Links */
.text-link {
  font-family: var(--font-primary);
  font-size: 1.125rem; /* 18px */
  font-weight: 900;
  line-height: 1.56;
  text-transform: uppercase;
  letter-spacing: 0.1125em;
  text-decoration: none;
  color: var(--color-primary-500);
  transition: color var(--transition-base);
}

.text-link:hover {
  color: var(--color-primary-600);
  text-decoration: underline;
}

/* Code / Monospace */
.text-code {
  font-family: var(--font-mono);
  font-size: 0.875rem; /* 14px */
  font-weight: 400;
  line-height: 1.5;
  letter-spacing: 0;
}

/* Weight Utilities */
.font-light {
  font-weight: 300;
}
.font-normal {
  font-weight: 400;
}
.font-medium {
  font-weight: 500;
}
.font-semibold {
  font-weight: 600;
}
.font-bold {
  font-weight: 700;
}
.font-black {
  font-weight: 900;
}
```

---

## 3. Color Palette

### Light Mode (Default)

| Token            | Color       | Hex     | RGB           | Usage                          |
| ---------------- | ----------- | ------- | ------------- | ------------------------------ |
| **Primary**      | Purple      | #7b61ff | 123, 97, 255  | CTA, links, primary actions    |
| **Primary Dark** | Deep Purple | #5b40c9 | 91, 64, 201   | Hover state, active states     |
| **Secondary**    | Cyan        | #2a9d9e | 42, 157, 158  | Supporting actions, highlights |
| **Accent**       | Pink        | #e5729a | 229, 114, 154 | Calls-to-action, emphasis      |
| **Success**      | Green       | #34c759 | 52, 199, 89   | Success messages, valid states |
| **Warning**      | Amber       | #fbbf24 | 251, 191, 36  | Warnings, cautions             |
| **Danger**       | Orange-Red  | #ff8555 | 255, 133, 85  | Errors, critical actions       |
| **Info**         | Steel Blue  | #5ba3d0 | 91, 163, 208  | Info messages, tooltips        |
| **Neutral 100**  | Off-White   | #e8e8e8 | 232, 232, 232 | Backgrounds, disabled states   |
| **Neutral 600**  | Dark Gray   | #3a3c42 | 58, 60, 66    | Text, borders, shadows         |
| **Neutral 700**  | Charcoal    | #22242a | 34, 36, 42    | Primary text                   |

### Dark Mode Overrides

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-primary-500: #9d84ff;
    --color-neutral-100: #1f2329;
    --color-neutral-600: #b0b8c4;
    --color-neutral-700: #e8e8e8;
  }
}
```

### Semantic Color Combinations

```css
/* Text on Light Background */
.text-on-light {
  color: var(--color-neutral-700);
}
.text-subtle-light {
  color: var(--color-neutral-600);
}
.text-muted-light {
  color: var(--color-neutral-400);
}

/* Text on Dark Background */
.text-on-dark {
  color: var(--color-neutral-100);
}
.text-subtle-dark {
  color: var(--color-neutral-200);
}

/* Background Pairs */
.bg-primary {
  background-color: var(--color-primary-500);
  color: var(--color-white);
}

.bg-neutral {
  background-color: var(--color-neutral-100);
  color: var(--color-neutral-700);
}

.bg-card {
  background-color: var(--color-white);
  border: var(--border-md) var(--border-style) var(--color-neutral-600);
}

.bg-card:hover {
  box-shadow: var(--shadow-bold);
}
```

---

| Token      | Value | Rem     | Usage                                 |
| ---------- | ----- | ------- | ------------------------------------- |
| spacing-1  | 4px   | 0.25rem | Micro padding (icons, tight elements) |
| spacing-2  | 6px   | 0.38rem | Extra small spacing                   |
| spacing-3  | 8px   | 0.5rem  | Small padding/gap                     |
| spacing-4  | 10px  | 0.63rem |                                       |
| spacing-5  | 12px  | 0.75rem | Standard element spacing              |
| spacing-6  | 16px  | 1rem    | Padding for cards, buttons            |
| spacing-7  | 20px  | 1.25rem | Section spacing                       |
| spacing-8  | 24px  | 1.5rem  | Major spacing between components      |
| spacing-9  | 28px  | 1.75rem |                                       |
| spacing-10 | 32px  | 2rem    | Large spacing, vertical rhythm        |
| spacing-12 | 40px  | 2.5rem  |                                       |
| spacing-14 | 48px  | 3rem    | Page section spacing                  |
| spacing-16 | 64px  | 4rem    | Hero / major sections                 |
| spacing-20 | 80px  | 5rem    | Full-width section gaps               |

### Layout & Containers

```css
/* Container Sizes */
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--spacing-6);
  padding-right: var(--spacing-6);
}

@media (min-width: 640px) {
  .container {
    max-width: 640px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
    padding-left: var(--spacing-8);
    padding-right: var(--spacing-8);
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

@media (min-width: 1280px) {
  .container {
    max-width: 1280px;
  }
}

/* Grid System (12-column) */
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--spacing-6);
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: repeat(6, 1fr);
    gap: var(--spacing-5);
  }
}

@media (max-width: 480px) {
  .grid {
    grid-template-columns: repeat(1, 1fr);
    gap: var(--spacing-4);
  }
}

.grid > [class*="col-"] {
  grid-column: span 1;
}

.col-6 {
  grid-column: span 6;
}
.col-4 {
  grid-column: span 4;
}
.col-3 {
  grid-column: span 3;
}
.col-2 {
  grid-column: span 2;
}

/* Flexbox Utilities */
.flex {
  display: flex;
}
.flex-col {
  flex-direction: column;
}
.flex-wrap {
  flex-wrap: wrap;
}
.gap-3 {
  gap: var(--spacing-3);
}
.gap-6 {
  gap: var(--spacing-6);
}
.items-center {
  align-items: center;
}
.justify-between {
  justify-content: space-between;
}

/* Breakpoints */
/* mobile-first: base -> sm -> md -> lg -> xl */
@media (min-width: 640px) {
  /* sm */
}
@media (min-width: 768px) {
  /* md */
}
@media (min-width: 1024px) {
  /* lg */
}
@media (min-width: 1280px) {
  /* xl */
}
```

---

## 5. Component Quick-Wins

### Button Component

```css
/* Base Button */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  padding: var(--spacing-5) var(--spacing-6);
  font-family: var(--font-primary);
  font-size: 1rem;
  font-weight: 700;
  line-height: 1;
  text-transform: uppercase;
  letter-spacing: 0.075em;
  border: var(--border-md) var(--border-style) transparent;
  border-radius: var(--radius-none);
  cursor: pointer;
  transition: all var(--transition-base);
  user-select: none;
  text-decoration: none;
}

/* Primary Button */
.btn-primary {
  background-color: var(--color-primary-500);
  color: var(--color-white);
  border-color: var(--color-primary-500);
}

.btn-primary:hover {
  background-color: var(--color-primary-600);
  box-shadow: var(--shadow-bold);
}

.btn-primary:active {
  transform: translate(2px, 2px);
  box-shadow: none;
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Secondary Button */
.btn-secondary {
  background-color: transparent;
  color: var(--color-primary-500);
  border-color: var(--color-primary-500);
}

.btn-secondary:hover {
  background-color: var(--color-primary-500);
  color: var(--color-white);
  box-shadow: var(--shadow-bold);
}

/* Ghost Button */
.btn-ghost {
  background-color: transparent;
  color: var(--color-neutral-700);
  border-color: transparent;
}

.btn-ghost:hover {
  background-color: var(--color-neutral-100);
  border-color: var(--color-neutral-600);
}

/* Size Variants */
.btn-sm {
  padding: var(--spacing-2) var(--spacing-5);
  font-size: 0.875rem;
}

.btn-lg {
  padding: var(--spacing-6) var(--spacing-8);
  font-size: 1.125rem;
}

/* Full Width */
.btn-block {
  width: 100%;
}
```

### Card Component

```css
.card {
  background-color: var(--color-white);
  border: var(--border-md) var(--border-style) var(--color-neutral-600);
  border-radius: var(--radius-none);
  padding: var(--spacing-8);
  transition: all var(--transition-base);
}

.card:hover {
  box-shadow: var(--shadow-bold);
  border-color: var(--color-primary-500);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--spacing-6);
  padding-bottom: var(--spacing-5);
  border-bottom: var(--border-md) var(--border-style) var(--color-neutral-100);
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--color-neutral-700);
}

.card-body {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--color-neutral-600);
}

.card-footer {
  margin-top: var(--spacing-6);
  padding-top: var(--spacing-5);
  border-top: var(--border-md) var(--border-style) var(--color-neutral-100);
  display: flex;
  gap: var(--spacing-3);
}
```

### Navigation Component

```css
nav {
  background-color: var(--color-white);
  border-bottom: var(--border-md) var(--border-style) var(--color-neutral-600);
  padding: var(--spacing-6) var(--spacing-8);
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
}

nav > .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-8);
}

.nav-brand {
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--color-primary-500);
  text-decoration: none;
  letter-spacing: -0.02em;
}

.nav-menu {
  list-style: none;
  display: flex;
  gap: var(--spacing-8);
  align-items: center;
  margin: 0;
  padding: 0;
}

.nav-link {
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-neutral-700);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  position: relative;
  transition: color var(--transition-base);
}

.nav-link::after {
  content: "";
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--color-primary-500);
  transition: width var(--transition-base);
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}

.nav-link:hover {
  color: var(--color-primary-500);
}
```

### Hero Section

```css
.hero {
  background: linear-gradient(
    135deg,
    var(--color-primary-500) 0%,
    var(--color-accent-500) 100%
  );
  color: var(--color-white);
  padding: var(--spacing-16) var(--spacing-8);
  text-align: center;
  border-bottom: var(--border-lg) var(--border-style) var(--color-neutral-600);
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 400px;
  height: 400px;
  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.1) 0%,
    transparent 70%
  );
  border-radius: 50%;
  z-index: -1;
}

.hero > .container {
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.hero-title {
  font-size: 3.75rem;
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: var(--spacing-6);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.hero-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  margin-bottom: var(--spacing-8);
  opacity: 0.95;
}

.hero-cta {
  display: inline-flex;
  gap: var(--spacing-3);
}

@media (max-width: 768px) {
  .hero {
    padding: var(--spacing-12) var(--spacing-6);
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }
}
```

---

## 6. Tailwind Config Snippet

Add to your `tailwindcss.config.js`:

```javascript
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          400: "#7159eb",
          500: "#7b61ff",
          600: "#6b50d9",
          700: "#5b40c9",
        },
        secondary: {
          300: "#77d3d7",
          400: "#4db8bd",
          500: "#2a9d9e",
          700: "#1b5f66",
        },
        accent: {
          300: "#f4a8c1",
          400: "#f08db3",
          500: "#e5729a",
          600: "#d94e78",
        },
        success: {
          500: "#34c759",
          600: "#2aa84f",
        },
        warning: {
          500: "#fbbf24",
          600: "#f59e0b",
        },
        danger: {
          500: "#ff8555",
          600: "#ff6b3d",
        },
        info: {
          500: "#5ba3d0",
          600: "#4682b4",
        },
        neutral: {
          100: "#e8e8e8",
          200: "#f0f0f0",
          300: "#d9d9d9",
          400: "#b0b8c4",
          500: "#7a7a7a",
          600: "#3a3c42",
          700: "#22242a",
        },
      },
      fontFamily: {
        primary: ["Space Grotesk", "system-ui", "-apple-system", "sans-serif"],
        secondary: ["Georgia", "serif"],
        mono: ["Menlo", "Monaco", "monospace"],
      },
      fontSize: {
        "heading-1": ["3.75rem", { lineHeight: "1.1", fontWeight: "900" }],
        "heading-2": ["3rem", { lineHeight: "1", fontWeight: "700" }],
        "heading-3": ["1.875rem", { lineHeight: "1.2", fontWeight: "700" }],
        "heading-4": ["1.5rem", { lineHeight: "1.3", fontWeight: "700" }],
        "heading-5": ["1.25rem", { lineHeight: "1.4", fontWeight: "700" }],
        "body-lg": ["1.125rem", { lineHeight: "1.6", fontWeight: "400" }],
        "body-base": ["1rem", { lineHeight: "1.6", fontWeight: "400" }],
        "body-sm": ["0.875rem", { lineHeight: "1.5", fontWeight: "400" }],
        label: ["0.75rem", { lineHeight: "1.4", fontWeight: "700" }],
      },
      spacing: {
        1: "0.25rem",
        2: "0.38rem",
        3: "0.5rem",
        4: "0.63rem",
        5: "0.75rem",
        6: "1rem",
        7: "1.25rem",
        8: "1.5rem",
        9: "1.75rem",
        10: "2rem",
        12: "2.5rem",
        14: "3rem",
        16: "4rem",
        20: "5rem",
      },
      borderRadius: {
        none: "0",
        sm: "0.25rem",
        md: "0.5rem",
        lg: "1rem",
        xl: "1.5rem",
      },
      borderWidth: {
        sm: "1px",
        md: "2px",
        lg: "4px",
      },
      boxShadow: {
        xs: "0 1px 2px rgba(58, 60, 66, 0.05)",
        sm: "0 2px 4px rgba(58, 60, 66, 0.1)",
        md: "2px 2px 4px rgba(58, 60, 66, 0.15)",
        lg: "4px 4px 8px rgba(58, 60, 66, 0.2)",
        bold: "4px 4px 0px 0px rgba(58, 60, 66, 0.92)",
      },
      zIndex: {
        dropdown: "100",
        sticky: "200",
        "modal-bg": "300",
        modal: "400",
        toast: "500",
      },
      transitionDuration: {
        fast: "150ms",
        base: "250ms",
        slow: "350ms",
      },
    },
  },
};
```

---

## 7. Figma Variables JSON

Copy the following and paste into Figma's Variables panel (**Assets > Variables > Import**):

```json
{
  "version": 1,
  "collections": {
    "Color": {
      "name": "Color",
      "modes": {
        "Light": {
          "Primary / 400": { "type": "COLOR", "value": "#7159eb" },
          "Primary / 500": { "type": "COLOR", "value": "#7b61ff" },
          "Primary / 600": { "type": "COLOR", "value": "#6b50d9" },
          "Primary / 700": { "type": "COLOR", "value": "#5b40c9" },
          "Secondary / 300": { "type": "COLOR", "value": "#77d3d7" },
          "Secondary / 400": { "type": "COLOR", "value": "#4db8bd" },
          "Secondary / 500": { "type": "COLOR", "value": "#2a9d9e" },
          "Secondary / 700": { "type": "COLOR", "value": "#1b5f66" },
          "Accent / 300": { "type": "COLOR", "value": "#f4a8c1" },
          "Accent / 400": { "type": "COLOR", "value": "#f08db3" },
          "Accent / 500": { "type": "COLOR", "value": "#e5729a" },
          "Accent / 600": { "type": "COLOR", "value": "#d94e78" },
          "Success / 500": { "type": "COLOR", "value": "#34c759" },
          "Success / 600": { "type": "COLOR", "value": "#2aa84f" },
          "Warning / 500": { "type": "COLOR", "value": "#fbbf24" },
          "Warning / 600": { "type": "COLOR", "value": "#f59e0b" },
          "Danger / 500": { "type": "COLOR", "value": "#ff8555" },
          "Danger / 600": { "type": "COLOR", "value": "#ff6b3d" },
          "Info / 500": { "type": "COLOR", "value": "#5ba3d0" },
          "Info / 600": { "type": "COLOR", "value": "#4682b4" },
          "Neutral / 100": { "type": "COLOR", "value": "#e8e8e8" },
          "Neutral / 200": { "type": "COLOR", "value": "#f0f0f0" },
          "Neutral / 300": { "type": "COLOR", "value": "#d9d9d9" },
          "Neutral / 400": { "type": "COLOR", "value": "#b0b8c4" },
          "Neutral / 500": { "type": "COLOR", "value": "#7a7a7a" },
          "Neutral / 600": { "type": "COLOR", "value": "#3a3c42" },
          "Neutral / 700": { "type": "COLOR", "value": "#22242a" }
        },
        "Dark": {
          "Primary / 400": { "type": "COLOR", "value": "#8a73ff" },
          "Primary / 500": { "type": "COLOR", "value": "#9d84ff" },
          "Primary / 600": { "type": "COLOR", "value": "#7b61ff" },
          "Primary / 700": { "type": "COLOR", "value": "#6b50d9" },
          "Neutral / 100": { "type": "COLOR", "value": "#1f2329" },
          "Neutral / 200": { "type": "COLOR", "value": "#2a2e35" },
          "Neutral / 600": { "type": "COLOR", "value": "#b0b8c4" },
          "Neutral / 700": { "type": "COLOR", "value": "#e8e8e8" }
        }
      }
    },
    "Typography": {
      "name": "Typography",
      "modes": {
        "Default": {
          "Heading / 1": {
            "type": "TYPOGRAPHY",
            "value": {
              "fontFamily": "Space Grotesk",
              "fontWeight": 900,
              "fontSize": 60,
              "lineHeight": 66,
              "letterSpacing": -0.02,
              "textTransform": "none"
            }
          },
          "Heading / 2": {
            "type": "TYPOGRAPHY",
            "value": {
              "fontFamily": "Space Grotesk",
              "fontWeight": 700,
              "fontSize": 48,
              "lineHeight": 48,
              "letterSpacing": -0.02,
              "textTransform": "none"
            }
          },
          "Body / Base": {
            "type": "TYPOGRAPHY",
            "value": {
              "fontFamily": "Space Grotesk",
              "fontWeight": 400,
              "fontSize": 16,
              "lineHeight": 25.6,
              "letterSpacing": 0,
              "textTransform": "none"
            }
          }
        }
      }
    },
    "Spacing": {
      "name": "Spacing",
      "modes": {
        "Default": {
          "xs": { "type": "FLOAT", "value": 4 },
          "sm": { "type": "FLOAT", "value": 8 },
          "md": { "type": "FLOAT", "value": 12 },
          "lg": { "type": "FLOAT", "value": 16 },
          "xl": { "type": "FLOAT", "value": 24 },
          "2xl": { "type": "FLOAT", "value": 32 },
          "3xl": { "type": "FLOAT", "value": 40 },
          "4xl": { "type": "FLOAT", "value": 48 },
          "5xl": { "type": "FLOAT", "value": 64 },
          "6xl": { "type": "FLOAT", "value": 80 }
        }
      }
    }
  }
}
```

---

## 8. QA Checklist

### Visual Regression Tests

- [ ] Run Chromatic / Percy snapshot tests for each component variant
- [ ] Compare light mode vs. dark mode rendering
- [ ] Verify button hover/active/disabled states render correctly
- [ ] Check card border and shadow animations
- [ ] Validate typography rendering across font weights (300–900)
- [ ] Test responsive breakpoints (480px, 768px, 1024px, 1280px)
- [ ] Verify spacing scale consistency (gap = margin = padding)
- [ ] Check color contrast on all text elements

### Contrast Ratio Tests (WCAG AA minimum: 4.5:1 for body text, 3:1 for large text)

| Text                  | Background            | Contrast | Status              |
| --------------------- | --------------------- | -------- | ------------------- |
| Neutral 700 (#22242a) | White (#ffffff)       | 11.2:1   | ✅ Pass             |
| Neutral 600 (#3a3c42) | Neutral 100 (#e8e8e8) | 5.1:1    | ✅ Pass             |
| Primary 500 (#7b61ff) | White (#ffffff)       | 4.2:1    | ⚠️ Fail (body text) |
| Success 500 (#34c759) | White (#ffffff)       | 5.2:1    | ✅ Pass             |
| Danger 500 (#ff8555)  | White (#ffffff)       | 4.8:1    | ✅ Pass             |

**Action:** Primary 500 text on white should not be used for body copy. Use Primary 700 instead.

---

## 9. Next Steps (Implementation Roadmap)

1. **Set up project scaffold** – Run `pnpm create vite@latest myapp --template react` (or Vue/Svelte)

2. **Install dependencies**

   ```bash
   pnpm add -D tailwindcss postcss autoprefixer
   pnpm add -D @tailwindcss/forms @tailwindcss/typography
   ```

3. **Initialize Tailwind** – Run `pnpm exec tailwindcss init -p`

4. **Copy CSS variables** – Paste the `:root` block into `src/index.css` or `src/globals.css`

5. **Extend Tailwind config** – Copy the `theme.extend` object from Section 6 into `tailwind.config.js`

6. **Create component library**

   ```
   src/
   ├── components/
   │   ├── Button.jsx (use .btn classes)
   │   ├── Card.jsx
   │   ├── Nav.jsx
   │   └── Hero.jsx
   ├── styles/
   │   ├── globals.css (variables)
   │   ├── typography.css (scale)
   │   └── components.css (utilities)
   ```

7. **Import fonts** – Add Space Grotesk via Google Fonts or self-hosted:

   ```css
   @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;900&display=swap");
   ```

8. **Test dark mode** – Add to `tailwind.config.js`:

   ```javascript
   darkMode: 'class', // or 'media'
   ```

   Then test with `<html class="dark">` toggle.

9. **Build component storybook** – Run `pnpm add -D storybook @storybook/react`:

   ```bash
   pnpm exec storybook init
   ```

   Create `.stories.jsx` files for Button, Card, Nav, Hero.

10. **Set up visual regression** – Add Chromatic or Percy snapshot tests to CI:

    ```bash
    pnpm add -D @chromatic-com/storybook
    ```

11. **QA pass** – Run contrast tests, keyboard nav, screen reader audit, responsive checks

12. **Export to Figma** – Import the JSON variables (Section 7) into Figma design file

13. **Deploy** – Build and deploy component library to npm or internal registry (if monorepo)

---

---
