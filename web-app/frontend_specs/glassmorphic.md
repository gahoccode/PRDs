# Glassmorphic Design System Specification

## 1. Design Tokens (CSS Variables)

```css
:root {
  /* Color Gradients */
  --gradient-primary: linear-gradient(135deg, #0f766e 0%, #1e293b 100%);
  --gradient-overlay:
    radial-gradient(
      circle at 20% 50%,
      rgba(15, 118, 110, 0.4) 0%,
      transparent 50%
    ),
    radial-gradient(
      circle at 80% 80%,
      rgba(30, 41, 59, 0.3) 0%,
      transparent 50%
    );

  /* Glass Palette */
  --glass-light: rgba(255, 255, 255, 0.1);
  --glass-light-hover: rgba(255, 255, 255, 0.15);
  --glass-border: rgba(255, 255, 255, 0.2);
  --glass-highlight: rgba(255, 255, 255, 0.3);

  /* Typography */
  --font-family-sans:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue",
    Arial, sans-serif;
  --font-family-mono: "IBM Plex Mono", "Monaco", "Courier New", monospace;

  /* Text Colors */
  --text-primary: rgba(255, 255, 255, 0.95);
  --text-secondary: rgba(255, 255, 255, 0.7);
  --text-tertiary: rgba(255, 255, 255, 0.5);

  /* Effects */
  --blur-sm: blur(8px);
  --blur-md: blur(10px);
  --blur-lg: blur(16px);
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.15);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.3);
  --shadow-inset: inset 0 1px 0 rgba(255, 255, 255, 0.3);

  /* Spacing Scale (8px base) */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;

  /* Border Radius */
  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-xl: 1.5rem;

  /* Transitions */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 300ms cubic-bezier(0.4, 0, 0.2, 1);

  /* Z-Index */
  --z-backdrop: 10;
  --z-modal: 20;
  --z-tooltip: 30;
}

@media (prefers-color-scheme: light) {
  :root {
    --text-primary: rgba(0, 0, 0, 0.95);
    --text-secondary: rgba(0, 0, 0, 0.7);
    --text-tertiary: rgba(0, 0, 0, 0.5);
    --glass-light: rgba(255, 255, 255, 0.5);
    --glass-light-hover: rgba(255, 255, 255, 0.6);
  }
}
```

---

## 2. Typography Scale

```css
body {
  font-family: var(--font-family-sans);
  line-height: 1.5;
  color: var(--text-primary);
}

h1 {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

h2 {
  font-size: 2rem;
  font-weight: 600;
  line-height: 1.3;
}

h3 {
  font-size: 1.5rem;
  font-weight: 600;
  line-height: 1.4;
}

h4 {
  font-size: 1.25rem;
  font-weight: 600;
}

h5,
h6 {
  font-size: 1rem;
  font-weight: 600;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75;
}
.text-base {
  font-size: 1rem;
  line-height: 1.5;
}
.text-sm {
  font-size: 0.875rem;
  line-height: 1.5;
}
.text-xs {
  font-size: 0.75rem;
  line-height: 1.5;
}

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

.text-primary {
  color: var(--text-primary);
}
.text-secondary {
  color: var(--text-secondary);
}
.text-tertiary {
  color: var(--text-tertiary);
}
.text-shadow {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
```

---

## 3. Color Palette

### Primary Gradient

- **Start**: `#0f766e` (Teal-800)
- **End**: `#1e293b` (Slate-900)
- **Use**: Page backgrounds, accent elements, focus states

### Accent Colors (Financial Context)

| Color             | Hex       | Usage                                |
| ----------------- | --------- | ------------------------------------ |
| Positive/Growth   | `#059669` | Portfolio gains, positive change     |
| Warning/Caution   | `#d97706` | Alert states, attention needed       |
| Negative/Loss     | `#dc2626` | Portfolio losses, error states       |
| Info/Neutral      | `#0284c7` | Informational messages, neutral data |
| Premium/Secondary | `#8b5cf6` | Secondary CTAs, premium features     |

### Glass Layer

| Color     | Value                    | Usage                    |
| --------- | ------------------------ | ------------------------ |
| Base      | `rgba(255,255,255,0.1)`  | Containers, cards        |
| Hover     | `rgba(255,255,255,0.15)` | Interactive hover states |
| Border    | `rgba(255,255,255,0.2)`  | Dividers, borders        |
| Highlight | `rgba(255,255,255,0.3)`  | Inset glow, focus states |

### Text Hierarchy

| Level     | Value                    | Usage                                 |
| --------- | ------------------------ | ------------------------------------- |
| Primary   | `rgba(255,255,255,0.95)` | Headings, main content, critical data |
| Secondary | `rgba(255,255,255,0.7)`  | Body text, labels, descriptions       |
| Tertiary  | `rgba(255,255,255,0.5)`  | Hints, disabled states, timestamps    |

### Light Mode Overrides

```css
@media (prefers-color-scheme: light) {
  :root {
    --text-primary: rgba(0, 0, 0, 0.95);
    --text-secondary: rgba(0, 0, 0, 0.7);
    --text-tertiary: rgba(0, 0, 0, 0.5);
    --glass-light: rgba(255, 255, 255, 0.5);
    --glass-light-hover: rgba(255, 255, 255, 0.6);
  }
}
```

---

## 4. Spacing & Layout

```css
.space-xs {
  margin: 0.25rem;
}
.space-sm {
  margin: 0.5rem;
}
.space-md {
  margin: 1rem;
}
.space-lg {
  margin: 1.5rem;
}
.space-xl {
  margin: 2rem;
}
.space-2xl {
  margin: 3rem;
}
.space-3xl {
  margin: 4rem;
}

.px-md {
  padding-left: 1rem;
  padding-right: 1rem;
}
.py-lg {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

@media (max-width: 768px) {
  .container {
    max-width: 640px;
    padding: 0 1rem;
  }
}

.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}
.grid-3 {
  grid-template-columns: repeat(3, 1fr);
}

@media (max-width: 768px) {
  .grid-2,
  .grid-3 {
    grid-template-columns: 1fr;
  }
}

.flex {
  display: flex;
}
.flex-col {
  flex-direction: column;
}
.gap-md {
  gap: 1rem;
}
```

---

## 5. Component Quick-Wins

### Button

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: var(--glass-light);
  color: var(--text-primary);
  border: 1px solid var(--glass-border);
  box-shadow:
    0 2px 8px rgba(0, 0, 0, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
  backdrop-filter: var(--blur-md);
}

.btn-primary:hover {
  background: var(--glass-light-hover);
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.btn-secondary {
  background: transparent;
  color: var(--text-secondary);
  border: 1px solid var(--glass-border);
}

.btn-secondary:hover {
  background: var(--glass-light);
  color: var(--text-primary);
}

.btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: left 200ms;
}

.btn:hover::before {
  left: 100%;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn:disabled:hover {
  transform: none;
  background: var(--glass-light);
}
```

### Card

```css
.card {
  background: var(--glass-light);
  border: 1px solid var(--glass-border);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
  backdrop-filter: var(--blur-md);
  transition: all 200ms;
}

.card:hover {
  background: var(--glass-light-hover);
  box-shadow:
    0 16px 48px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
  transform: translateY(-4px);
}

.card-header {
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--glass-border);
}

.card-body {
  margin-bottom: 1rem;
}

.card-footer {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--glass-border);
}
```

### Navigation

```css
.nav {
  display: flex;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: var(--glass-light);
  border: 1px solid var(--glass-border);
  border-radius: 1rem;
  backdrop-filter: var(--blur-md);
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.nav-item {
  color: var(--text-secondary);
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  transition: all 200ms;
}

.nav-item:hover {
  color: var(--text-primary);
  background: var(--glass-light);
}

.nav-item.active {
  color: var(--text-primary);
  background: var(--glass-highlight);
  border: 1px solid var(--glass-border);
}
```

### Hero Section

```css
.hero {
  position: relative;
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  text-align: center;
}

.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--gradient-primary);
  background-attachment: fixed;
  z-index: -2;
}

.hero::after {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--gradient-overlay);
  z-index: -1;
}

.hero-content {
  position: relative;
  max-width: 800px;
  padding: 4rem 1.5rem;
}

.hero h1 {
  color: var(--text-primary);
  margin-bottom: 2rem;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.hero p {
  color: var(--text-secondary);
  margin-bottom: 2rem;
  font-size: 1.125rem;
}
```

### Form Input

```css
.input {
  width: 100%;
  padding: 0.5rem 1rem;
  background: var(--glass-light);
  border: 1px solid var(--glass-border);
  border-radius: 0.5rem;
  color: var(--text-primary);
  backdrop-filter: var(--blur-md);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);
  transition: all 200ms;
  font-family: inherit;
  font-size: 1rem;
}

.input::placeholder {
  color: var(--text-tertiary);
}

.input:focus {
  outline: none;
  background: var(--glass-light-hover);
  border-color: var(--glass-highlight);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    0 0 0 3px rgba(15, 118, 110, 0.2);
}

.input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### Alert/Badge

```css
.alert {
  padding: 1rem;
  border-radius: 0.5rem;
  border-left: 4px solid;
  background: var(--glass-light);
  backdrop-filter: var(--blur-md);
  margin-bottom: 1rem;
}

.alert-success {
  border-left-color: #059669;
  color: #d1fae5;
}

.alert-warning {
  border-left-color: #d97706;
  color: #fef3c7;
}

.alert-error {
  border-left-color: #dc2626;
  color: #fee2e2;
}

.alert-info {
  border-left-color: #0284c7;
  color: #e0f2fe;
}
```

---

## 6. Tailwind Config Snippet

```javascript
export default {
  extend: {
    colors: {
      glass: {
        light: "rgba(255, 255, 255, 0.1)",
        lighter: "rgba(255, 255, 255, 0.15)",
        border: "rgba(255, 255, 255, 0.2)",
        highlight: "rgba(255, 255, 255, 0.3)",
      },
      text: {
        primary: "rgba(255, 255, 255, 0.95)",
        secondary: "rgba(255, 255, 255, 0.7)",
        tertiary: "rgba(255, 255, 255, 0.5)",
      },
      semantic: {
        success: "#059669",
        warning: "#d97706",
        error: "#dc2626",
        info: "#0284c7",
        premium: "#8b5cf6",
      },
    },
    backgroundImage: {
      "gradient-primary": "linear-gradient(135deg, #0f766e 0%, #1e293b 100%)",
      "gradient-overlay": `radial-gradient(circle at 20% 50%, rgba(15, 118, 110, 0.4) 0%, transparent 50%),
                           radial-gradient(circle at 80% 80%, rgba(30, 41, 59, 0.3) 0%, transparent 50%)`,
    },
    backdropBlur: {
      xs: "8px",
      sm: "10px",
      md: "16px",
    },
    boxShadow: {
      glass:
        "0 2px 8px rgba(0, 0, 0, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.3)",
      "glass-md":
        "0 8px 24px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.3)",
      "glass-lg":
        "0 16px 48px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.3)",
    },
    spacing: {
      xs: "0.25rem",
      sm: "0.5rem",
      md: "1rem",
      lg: "1.5rem",
      xl: "2rem",
      "2xl": "3rem",
      "3xl": "4rem",
    },
  },
};
```

---

## 7. Figma Variables JSON

```json
{
  "collections": [
    {
      "id": "slate-colors",
      "name": "Colors",
      "variables": [
        {
          "id": "gradient-teal",
          "name": "Gradient/Primary/Teal",
          "type": "COLOR",
          "value": { "r": 0.059, "g": 0.463, "b": 0.431, "a": 1 },
          "notes": "#0f766e - Teal-800"
        },
        {
          "id": "gradient-slate",
          "name": "Gradient/Primary/Slate",
          "type": "COLOR",
          "value": { "r": 0.118, "g": 0.165, "b": 0.224, "a": 1 },
          "notes": "#1e293b - Slate-900"
        },
        {
          "id": "glass-light",
          "name": "Glass/Light",
          "type": "COLOR",
          "value": { "r": 1, "g": 1, "b": 1, "a": 0.1 }
        },
        {
          "id": "glass-border",
          "name": "Glass/Border",
          "type": "COLOR",
          "value": { "r": 1, "g": 1, "b": 1, "a": 0.2 }
        },
        {
          "id": "text-primary",
          "name": "Text/Primary",
          "type": "COLOR",
          "value": { "r": 1, "g": 1, "b": 1, "a": 0.95 }
        },
        {
          "id": "text-secondary",
          "name": "Text/Secondary",
          "type": "COLOR",
          "value": { "r": 1, "g": 1, "b": 1, "a": 0.7 }
        },
        {
          "id": "semantic-success",
          "name": "Semantic/Success",
          "type": "COLOR",
          "value": { "r": 0.016, "g": 0.588, "b": 0.412, "a": 1 },
          "notes": "#059669"
        },
        {
          "id": "semantic-warning",
          "name": "Semantic/Warning",
          "type": "COLOR",
          "value": { "r": 0.855, "g": 0.467, "b": 0.024, "a": 1 },
          "notes": "#d97706"
        },
        {
          "id": "semantic-error",
          "name": "Semantic/Error",
          "type": "COLOR",
          "value": { "r": 0.863, "g": 0.149, "b": 0.149, "a": 1 },
          "notes": "#dc2626"
        },
        {
          "id": "semantic-info",
          "name": "Semantic/Info",
          "type": "COLOR",
          "value": { "r": 0.008, "g": 0.522, "b": 0.78, "a": 1 },
          "notes": "#0284c7"
        },
        {
          "id": "semantic-premium",
          "name": "Semantic/Premium",
          "type": "COLOR",
          "value": { "r": 0.545, "g": 0.361, "b": 0.961, "a": 1 },
          "notes": "#8b5cf6"
        }
      ]
    },
    {
      "id": "slate-spacing",
      "name": "Spacing",
      "variables": [
        { "id": "space-xs", "name": "Space/XS", "type": "FLOAT", "value": 4 },
        { "id": "space-sm", "name": "Space/SM", "type": "FLOAT", "value": 8 },
        { "id": "space-md", "name": "Space/MD", "type": "FLOAT", "value": 16 },
        { "id": "space-lg", "name": "Space/LG", "type": "FLOAT", "value": 24 },
        { "id": "space-xl", "name": "Space/XL", "type": "FLOAT", "value": 32 },
        {
          "id": "space-2xl",
          "name": "Space/2XL",
          "type": "FLOAT",
          "value": 48
        },
        { "id": "space-3xl", "name": "Space/3XL", "type": "FLOAT", "value": 64 }
      ]
    }
  ]
}
```

---

## 8. QA Checklist

### Visual Regression Tests

- [ ] Teal/Slate gradient background renders consistently on Chrome, Safari, Firefox, Edge
- [ ] Backdrop-filter blur applies without performance degradation
- [ ] Button hover states trigger smooth elevation and shimmer animations
- [ ] Card hover transform (translateY) works without flicker
- [ ] Form inputs maintain focus glow without border collapse
- [ ] Text shadows render on all heading levels without pixelation
- [ ] Navigation active state styling applies correctly
- [ ] Hero section background-attachment: fixed works on mobile
- [ ] Semantic color alerts (success, warning, error, info) display correctly
- [ ] Premium accent color (#8b5cf6) passes contrast on glass backgrounds

### WCAG Contrast Ratios

- [ ] Primary text `rgba(255,255,255,0.95)` on glass backgrounds meets **4.5:1 (AA standard)**
  - Test at: https://webaim.org/resources/contrastchecker/
  - Teal/Slate gradient should provide sufficient base contrast
- [ ] Secondary text `rgba(255,255,255,0.7)` for body copy meets **3:1 (AA for large text)**
- [ ] Tertiary text `rgba(255,255,255,0.5)` restricted to disabled/hints only
- [ ] All semantic colors (success, warning, error, info) have sufficient contrast
- [ ] Button focus indicators visible on both light & dark backgrounds
- [ ] Error states use red icon + text (not red color alone)
- [ ] Success states use green icon + text (not green color alone)

### 3 Critical Accessibility Gotchas

1. **Backdrop-Filter Performance on Mobile**: Blur causes jank on low-end devices. Add:

   ```css
   @media (prefers-reduced-motion: reduce) {
     * {
       backdrop-filter: none !important;
     }
   }
   ```

2. **Teal/Slate on Light Mode**: When light mode activates, gradient may become too dark. Test light mode extensively. Consider creating alternate light gradient:

   ```css
   @media (prefers-color-scheme: light) {
     .hero::before {
       background: linear-gradient(135deg, #14b8a6 0%, #475569 100%);
     }
   }
   ```

3. **Focus Ring Visibility in Glass**: Frosted backgrounds obscure focus outlines. Use high-contrast box-shadow:
   ```css
   .input:focus {
     box-shadow:
       inset 0 1px 0 rgba(255, 255, 255, 0.3),
       0 0 0 3px rgba(15, 118, 110, 0.3);
     outline: 2px solid #0f766e;
     outline-offset: 2px;
   }
   ```

Additional checks:

- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Screen reader announces button roles and states
- [ ] Color blindness: test semantic colors with simulator
- [ ] Zoom to 200%: layout doesn't break, text readable
- [ ] Touch targets >= 44x44px on mobile

---

## 9. Next Steps

1. **Create project**

   ```bash
   pnpm create vite@latest my-glass-app -- --template react
   cd my-glass-app && pnpm install
   ```

2. **Install Tailwind**

   ```bash
   pnpm install -D tailwindcss postcss autoprefixer
   pnpm exec tailwindcss init -p
   ```

3. **Add token CSS**
   - Create `src/styles/tokens.css`
   - Copy `:root` block from Section 1
   - Import in `src/main.jsx`: `import './styles/tokens.css'`

4. **Configure Tailwind**
   - Replace `tailwind.config.js` with Section 6 config
   - Update template paths:

   ```js
   content: ["./index.html", "./src/**/*.{js,jsx}"];
   ```

5. **Create components directory**

   ```bash
   mkdir src/components
   ```

   - Add files: `Button.jsx`, `Card.jsx`, `Nav.jsx`, `Hero.jsx`, `Input.jsx`, `Alert.jsx`
   - Copy CSS from Section 5

6. **Set up Figma (optional)**
   - Open Figma → Assets panel → Variables
   - Click **+** to create new collection
   - Use manual entry or JSON import from Section 7
   - Link components to variables for design-to-dev sync

7. **Build hero section**

   ```jsx
   export default function Hero() {
     return (
       <section className="hero">
         <div className="hero-content">
           <h1>Portfolio Analytics</h1>
           <p>Professional insights. Modern interface.</p>
           <button className="btn btn-primary">Get Started</button>
         </div>
       </section>
     );
   }
   ```

8. **Test across browsers**
   - Chrome/Edge: Full glassmorphic effects
   - Safari: Verify `-webkit-backdrop-filter` fallback
   - Firefox: Confirm backdrop-filter enabled
   - Mobile (iOS/Android): Test blur performance, touch targets

9. **Run accessibility audit**

   ```bash
   pnpm install -D axe-core
   # Or use Lighthouse in DevTools (Ctrl+Shift+I → Lighthouse)
   ```

10. **Deploy and monitor**
    - Build: `pnpm run build`
    - Deploy to Vercel/Netlify
    - Monitor Web Vitals (CLS, LCP with backdrop-filter)
    - Gather user feedback

---

## 10. Risk Log

### Ambiguities in Original Spec

| Risk                                   | Severity | Mitigation                                              |
| -------------------------------------- | -------- | ------------------------------------------------------- |
| Light mode appearance undefined        | High     | Added light mode CSS overrides; test extensively        |
| Financial data chart rendering unclear | High     | Recommend white background for charts, glass frame only |
| Responsive breakpoints not specified   | Medium   | Use: 640px (sm), 768px (md), 1024px (lg), 1280px (xl)   |
| Animation timing/easing undefined      | Medium   | Applied Material Design standard easing                 |
| Accessibility standards not mentioned  | High     | Assumed WCAG 2.1 AA; added contrast thresholds          |
| Semantic color usage rules missing     | Medium   | Added in Section 3; restrict each color to its context  |

### Implementation Risks

| Risk                                                   | Impact     | Mitigation                                                 |
| ------------------------------------------------------ | ---------- | ---------------------------------------------------------- |
| Backdrop-filter unsupported in IE11, old Android       | Low-Medium | Fallback: `background: rgba(255,255,255,0.1)` no blur      |
| Teal/Slate too dark on light backgrounds               | High       | Test light mode extensively; create light gradient variant |
| Semi-transparent text may fail contrast on light mode  | High       | Pre-test with WebAIM; adjust opacity values                |
| Fixed gradient background impacts scroll perf          | Medium     | Profile with DevTools; use `scroll` on mobile if needed    |
| Semantic colors need icons (color blind accessibility) | Medium     | Never rely on color alone; pair with icons/text            |

### Missing from Spec

- **Animation library preference** (Framer Motion, vanilla CSS?) — Used vanilla CSS
- **Data table styling** — Apply glass containers to table rows; use striped pattern
- **Modal/dialog backdrop** — Not specified; recommend `backdrop: blur(4px)` overlay
- **Pagination component** — Not included; base on button styles
- **Breadcrumb styling** — Use `text-secondary` for inactive, `text-primary` for current
- **Badge/label components** — Not specified; create from button with smaller padding
- **Tooltip styling** — Not included; use semi-transparent glass with `pointer-events: none`
- **Responsive typography** — Recommend `clamp()` for fluid sizing
- **Icon system** — Undefined; consider Heroicons or Radix Icons
- **Loading state animations** — Not specified; add spinner component

### Recommendations

1. **Request design mockups** for critical flows (login, dashboard, portfolio view) before dev starts
2. **Test light mode immediately** with slate/teal gradient — may need adjustment
3. **Profile on real low-end device** (iPhone SE, Pixel 4a) for blur performance
4. **Document semantic color rules** (when/where to use each accent color)
5. **Create visual regression baseline** with screenshots (light + dark mode)
6. **Test financial data readability** — ensure charts/tables remain clear with glass overlay
7. **Plan icon system** early (affects button sizing, form inputs)
