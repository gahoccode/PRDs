# Neuphorism Tailwind Configuration

Drop-in configuration for Tailwind CSS projects.

## tailwind.config.js

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        neu: {
          bg: {
            DEFAULT: '#e6e8ed',
            light: '#f7f9fc',
            dark: '#d1d4db',
          },
          shadow: {
            dark: '#c5c8ce',
            light: '#ffffff',
          },
          text: {
            DEFAULT: '#4a5568',
            secondary: '#718096',
            heading: '#2d3748',
          },
          accent: {
            DEFAULT: '#667eea',
            hover: '#5a67d8',
          },
          error: '#e53e3e',
          success: '#38a169',
          warning: '#d69e2e',
        },
      },
      fontFamily: {
        neu: ['Inter', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        light: '300',
        regular: '400',
        medium: '500',
      },
      borderRadius: {
        'neu-sm': '8px',
        'neu-md': '12px',
        'neu-lg': '20px',
      },
      boxShadow: {
        'neu-extruded': '12px 12px 24px #c5c8ce, -12px -12px 24px #ffffff',
        'neu-pressed': 'inset 6px 6px 12px #c5c8ce, inset -6px -6px 12px #ffffff',
        'neu-elevated': '16px 16px 32px #c5c8ce, -16px -16px 32px #ffffff',
        // Dark mode variants
        'neu-extruded-dark': '12px 12px 24px #1a202c, -12px -12px 24px #3d4a5c',
        'neu-pressed-dark': 'inset 6px 6px 12px #1a202c, inset -6px -6px 12px #3d4a5c',
        'neu-elevated-dark': '16px 16px 32px #1a202c, -16px -16px 32px #3d4a5c',
      },
      spacing: {
        'neu-1': '4px',
        'neu-2': '8px',
        'neu-3': '12px',
        'neu-4': '16px',
        'neu-5': '24px',
        'neu-6': '32px',
        'neu-7': '48px',
        'neu-8': '64px',
      },
      transitionTimingFunction: {
        'neu': 'cubic-bezier(0.4, 0, 0.2, 1)',
      },
      transitionDuration: {
        'neu': '250ms',
      },
    },
  },
  plugins: [],
};
```

## Usage Examples

### Button

```html
<button class="
  px-6 py-3
  font-neu font-medium text-sm uppercase tracking-wider
  text-neu-text-heading
  bg-neu-bg
  rounded-neu-md
  shadow-neu-extruded
  hover:shadow-neu-elevated hover:-translate-y-0.5
  active:shadow-neu-pressed active:translate-y-0
  focus:outline-none focus-visible:ring-2 focus-visible:ring-neu-accent/30
  transition-all duration-neu ease-neu
">
  Button
</button>
```

### Card

```html
<div class="
  p-8
  bg-neu-bg
  rounded-neu-lg
  shadow-neu-extruded
  hover:shadow-neu-elevated hover:-translate-y-1 hover:scale-[1.01]
  transition-all duration-neu ease-neu
">
  <h3 class="text-xl font-medium text-neu-text-heading mb-3">Card Title</h3>
  <p class="text-neu-text">Card content goes here.</p>
</div>
```

### Input

```html
<input
  type="text"
  placeholder="Enter text..."
  class="
    w-full px-4 py-3
    font-neu text-base text-neu-text
    bg-neu-bg
    rounded-neu-md
    shadow-neu-pressed
    focus:outline-none focus:ring-2 focus:ring-neu-accent/30 focus:scale-[1.01]
    placeholder:text-neu-text-secondary
    transition-all duration-neu ease-neu
  "
/>
```

### Navigation

```html
<nav class="flex items-center gap-2 p-3 bg-neu-bg rounded-neu-lg shadow-neu-extruded">
  <a href="#" class="
    px-4 py-2
    text-sm font-medium
    text-neu-text-secondary
    rounded-neu-sm
    hover:text-neu-accent hover:shadow-neu-pressed
    transition-all duration-neu ease-neu
  ">
    Home
  </a>
  <a href="#" class="
    px-4 py-2
    text-sm font-medium
    text-neu-accent
    rounded-neu-sm
    shadow-neu-pressed
  ">
    Active
  </a>
</nav>
```

## Dark Mode Setup

### With Tailwind Dark Mode

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class', // or 'media'
  // ... rest of config
}
```

```html
<div class="
  bg-neu-bg dark:bg-[#2d3748]
  shadow-neu-extruded dark:shadow-neu-extruded-dark
  text-neu-text dark:text-[#e2e8f0]
">
  Content
</div>
```

### With CSS Variables (Recommended)

Add to your CSS:

```css
@layer base {
  :root {
    --neu-bg: #e6e8ed;
    --neu-shadow-dark: #c5c8ce;
    --neu-shadow-light: #ffffff;
  }
  
  .dark {
    --neu-bg: #2d3748;
    --neu-shadow-dark: #1a202c;
    --neu-shadow-light: #3d4a5c;
  }
}
```

Then use arbitrary values:

```html
<div class="bg-[var(--neu-bg)] shadow-[12px_12px_24px_var(--neu-shadow-dark),-12px_-12px_24px_var(--neu-shadow-light)]">
  Content
</div>
```
