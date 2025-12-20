# Design Tokens Reference

Complete CSS variables, Tailwind configuration, and utility classes for the design system.

## CSS Variables

```css
:root {
  /* Colors - Primary (Purple) */
  --color-primary-400: #7159eb;
  --color-primary-500: #7b61ff;
  --color-primary-600: #6b50d9;
  --color-primary-700: #5b40c9;

  /* Colors - Secondary (Cyan) */
  --color-secondary-300: #77d3d7;
  --color-secondary-400: #4db8bd;
  --color-secondary-500: #2a9d9e;
  --color-secondary-700: #1b5f66;

  /* Colors - Accent (Pink) */
  --color-accent-300: #f4a8c1;
  --color-accent-400: #f08db3;
  --color-accent-500: #e5729a;
  --color-accent-600: #d94e78;

  /* Colors - Semantic */
  --color-success-500: #34c759;
  --color-success-600: #2aa84f;
  --color-warning-500: #fbbf24;
  --color-warning-600: #f59e0b;
  --color-danger-500: #ff8555;
  --color-danger-600: #ff6b3d;
  --color-info-500: #5ba3d0;
  --color-info-600: #4682b4;

  /* Colors - Neutral */
  --color-white: #ffffff;
  --color-black: #000000;
  --color-neutral-100: #e8e8e8;
  --color-neutral-200: #f0f0f0;
  --color-neutral-300: #d9d9d9;
  --color-neutral-400: #b0b8c4;
  --color-neutral-500: #7a7a7a;
  --color-neutral-600: #3a3c42;
  --color-neutral-700: #22242a;

  /* Typography */
  --font-primary: 'Space Grotesk', system-ui, -apple-system, sans-serif;
  --font-secondary: 'Georgia', serif;
  --font-mono: 'Menlo', 'Monaco', monospace;

  /* Spacing */
  --spacing-1: 0.25rem;  /* 4px */
  --spacing-2: 0.375rem; /* 6px */
  --spacing-3: 0.5rem;   /* 8px */
  --spacing-4: 0.625rem; /* 10px */
  --spacing-5: 0.75rem;  /* 12px */
  --spacing-6: 1rem;     /* 16px */
  --spacing-7: 1.25rem;  /* 20px */
  --spacing-8: 1.5rem;   /* 24px */
  --spacing-9: 1.75rem;  /* 28px */
  --spacing-10: 2rem;    /* 32px */
  --spacing-12: 2.5rem;  /* 40px */
  --spacing-14: 3rem;    /* 48px */
  --spacing-16: 4rem;    /* 64px */
  --spacing-20: 5rem;    /* 80px */

  /* Border Radius */
  --radius-none: 0;
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-xl: 1.5rem;
  --radius-full: 9999px;

  /* Borders */
  --border-sm: 1px;
  --border-md: 2px;
  --border-lg: 4px;
  --border-color: var(--color-neutral-600);

  /* Shadows */
  --shadow-xs: 0 1px 2px rgba(58, 60, 66, 0.05);
  --shadow-sm: 0 2px 4px rgba(58, 60, 66, 0.1);
  --shadow-md: 2px 2px 4px rgba(58, 60, 66, 0.15);
  --shadow-lg: 4px 4px 8px rgba(58, 60, 66, 0.2);
  --shadow-bold: 4px 4px 0px 0px rgba(58, 60, 66, 0.92);

  /* Z-Index */
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal-bg: 300;
  --z-modal: 400;
  --z-toast: 500;

  /* Transitions */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Typography Classes

```css
.text-heading-1 {
  font-family: var(--font-primary);
  font-size: 3.75rem;
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-heading-2 {
  font-family: var(--font-primary);
  font-size: 3rem;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.02em;
}

.text-heading-3 {
  font-family: var(--font-primary);
  font-size: 1.875rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
}

.text-heading-4 {
  font-family: var(--font-primary);
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.3;
}

.text-heading-5 {
  font-family: var(--font-primary);
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.4;
}

.text-body-lg {
  font-family: var(--font-primary);
  font-size: 1.125rem;
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0.01em;
}

.text-body-base {
  font-family: var(--font-primary);
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.6;
}

.text-body-sm {
  font-family: var(--font-primary);
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
}

.text-label {
  font-family: var(--font-primary);
  font-size: 0.75rem;
  font-weight: 700;
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.15em;
}

.text-caption {
  font-family: var(--font-primary);
  font-size: 0.75rem;
  font-weight: 400;
  line-height: 1.4;
}
```

## Tailwind Config

```javascript
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          400: '#7159eb',
          500: '#7b61ff',
          600: '#6b50d9',
          700: '#5b40c9',
        },
        secondary: {
          300: '#77d3d7',
          400: '#4db8bd',
          500: '#2a9d9e',
          700: '#1b5f66',
        },
        accent: {
          300: '#f4a8c1',
          400: '#f08db3',
          500: '#e5729a',
          600: '#d94e78',
        },
        success: { 500: '#34c759', 600: '#2aa84f' },
        warning: { 500: '#fbbf24', 600: '#f59e0b' },
        danger: { 500: '#ff8555', 600: '#ff6b3d' },
        info: { 500: '#5ba3d0', 600: '#4682b4' },
        neutral: {
          100: '#e8e8e8',
          200: '#f0f0f0',
          300: '#d9d9d9',
          400: '#b0b8c4',
          500: '#7a7a7a',
          600: '#3a3c42',
          700: '#22242a',
        },
      },
      fontFamily: {
        primary: ['Space Grotesk', 'system-ui', '-apple-system', 'sans-serif'],
        secondary: ['Georgia', 'serif'],
        mono: ['Menlo', 'Monaco', 'monospace'],
      },
      fontSize: {
        'heading-1': ['3.75rem', { lineHeight: '1.1', fontWeight: '900' }],
        'heading-2': ['3rem', { lineHeight: '1', fontWeight: '700' }],
        'heading-3': ['1.875rem', { lineHeight: '1.2', fontWeight: '700' }],
        'heading-4': ['1.5rem', { lineHeight: '1.3', fontWeight: '700' }],
        'heading-5': ['1.25rem', { lineHeight: '1.4', fontWeight: '700' }],
        'body-lg': ['1.125rem', { lineHeight: '1.6', fontWeight: '400' }],
        'body-base': ['1rem', { lineHeight: '1.6', fontWeight: '400' }],
        'body-sm': ['0.875rem', { lineHeight: '1.5', fontWeight: '400' }],
        'label': ['0.75rem', { lineHeight: '1.4', fontWeight: '700' }],
      },
      boxShadow: {
        xs: '0 1px 2px rgba(58, 60, 66, 0.05)',
        sm: '0 2px 4px rgba(58, 60, 66, 0.1)',
        md: '2px 2px 4px rgba(58, 60, 66, 0.15)',
        lg: '4px 4px 8px rgba(58, 60, 66, 0.2)',
        bold: '4px 4px 0px 0px rgba(58, 60, 66, 0.92)',
      },
      borderRadius: {
        none: '0',
        sm: '0.25rem',
        md: '0.5rem',
        lg: '1rem',
        xl: '1.5rem',
      },
      borderWidth: {
        sm: '1px',
        md: '2px',
        lg: '4px',
      },
    },
  },
}
```

## Dark Mode Overrides

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-primary-500: #9d84ff;
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

## Accessibility Notes

| Text | Background | Contrast | Status |
|------|-----------|----------|--------|
| Neutral 700 | White | 11.2:1 | ✅ Pass |
| Neutral 600 | Neutral 100 | 5.1:1 | ✅ Pass |
| Primary 500 | White | 4.2:1 | ⚠️ Large text only |
| Primary 700 | White | 7.1:1 | ✅ Pass |

**Rule**: Use Primary 700 (#5b40c9) for body text on white backgrounds.
