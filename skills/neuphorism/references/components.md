# Neuphorism Component Library

Complete CSS for all core components. Copy and adapt as needed.

## Base Setup

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap');

:root {
  /* Surface */
  --neu-bg: #e6e8ed;
  --neu-bg-light: #f7f9fc;
  --neu-bg-dark: #d1d4db;
  
  /* Shadows */
  --neu-shadow-dark: #c5c8ce;
  --neu-shadow-light: #ffffff;
  
  /* Text */
  --neu-text: #4a5568;
  --neu-text-secondary: #718096;
  --neu-heading: #2d3748;
  
  /* Accents */
  --neu-accent: #667eea;
  --neu-accent-hover: #5a67d8;
  --neu-error: #e53e3e;
  --neu-success: #38a169;
  --neu-warning: #d69e2e;
  
  /* Shadows */
  --neu-extruded: 12px 12px 24px var(--neu-shadow-dark), -12px -12px 24px var(--neu-shadow-light);
  --neu-pressed: inset 6px 6px 12px var(--neu-shadow-dark), inset -6px -6px 12px var(--neu-shadow-light);
  --neu-elevated: 16px 16px 32px var(--neu-shadow-dark), -16px -16px 32px var(--neu-shadow-light);
  
  /* Radius */
  --neu-radius-sm: 8px;
  --neu-radius-md: 12px;
  --neu-radius-lg: 20px;
  
  /* Transitions */
  --neu-transition: 250ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Dark Mode */
:root[data-theme="dark"] {
  --neu-bg: #2d3748;
  --neu-bg-light: #3d4a5c;
  --neu-bg-dark: #1a202c;
  --neu-shadow-dark: #1a202c;
  --neu-shadow-light: #3d4a5c;
  --neu-text: #e2e8f0;
  --neu-text-secondary: #a0aec0;
  --neu-heading: #f7fafc;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--neu-bg);
  color: var(--neu-text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
```

## Button

```css
.neu-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--neu-heading);
  background: var(--neu-bg);
  border: none;
  border-radius: var(--neu-radius-md);
  box-shadow: var(--neu-extruded);
  cursor: pointer;
  transition: box-shadow var(--neu-transition), transform var(--neu-transition);
}

.neu-btn:hover {
  box-shadow: var(--neu-elevated);
  transform: translateY(-2px);
}

.neu-btn:active,
.neu-btn:focus {
  box-shadow: var(--neu-pressed);
  transform: translateY(0);
  outline: none;
}

.neu-btn:focus-visible {
  box-shadow: var(--neu-pressed), 0 0 0 3px rgba(102, 126, 234, 0.3);
}

/* Primary variant */
.neu-btn--primary {
  background: var(--neu-accent);
  color: #ffffff;
}

.neu-btn--primary:hover {
  background: var(--neu-accent-hover);
}

/* Icon button */
.neu-btn--icon {
  width: 48px;
  height: 48px;
  padding: 0;
  border-radius: 50%;
}
```

## Card

```css
.neu-card {
  background: var(--neu-bg);
  border-radius: var(--neu-radius-lg);
  box-shadow: var(--neu-extruded);
  padding: 32px;
  transition: box-shadow var(--neu-transition), transform var(--neu-transition);
}

.neu-card:hover {
  box-shadow: var(--neu-elevated);
  transform: translateY(-4px) scale(1.01);
}

.neu-card__title {
  font-size: 20px;
  font-weight: 500;
  color: var(--neu-heading);
  margin: 0 0 12px;
}

.neu-card__body {
  color: var(--neu-text);
}

/* Flat card (no hover effect) */
.neu-card--flat:hover {
  transform: none;
  box-shadow: var(--neu-extruded);
}
```

## Input

```css
.neu-input {
  width: 100%;
  padding: 12px 16px;
  font-family: inherit;
  font-size: 16px;
  color: var(--neu-text);
  background: var(--neu-bg);
  border: none;
  border-radius: var(--neu-radius-md);
  box-shadow: var(--neu-pressed);
  transition: box-shadow var(--neu-transition), transform var(--neu-transition);
}

.neu-input:focus {
  outline: none;
  box-shadow: var(--neu-pressed), 0 0 0 3px rgba(102, 126, 234, 0.3);
  transform: scale(1.01);
}

.neu-input::placeholder {
  color: var(--neu-text-secondary);
}

/* Textarea */
.neu-textarea {
  min-height: 120px;
  resize: vertical;
}

/* Input group with label */
.neu-field {
  margin-bottom: 24px;
}

.neu-label {
  display: block;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--neu-text-secondary);
  margin-bottom: 8px;
}
```

## Navigation

```css
.neu-nav {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px;
  background: var(--neu-bg);
  border-radius: var(--neu-radius-lg);
  box-shadow: var(--neu-extruded);
}

.neu-nav__link {
  padding: 8px 16px;
  font-size: 14px;
  font-weight: 500;
  color: var(--neu-text-secondary);
  text-decoration: none;
  border-radius: var(--neu-radius-sm);
  transition: all var(--neu-transition);
}

.neu-nav__link:hover,
.neu-nav__link--active {
  color: var(--neu-accent);
  box-shadow: var(--neu-pressed);
}
```

## Hero Section

```css
.neu-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  padding: 64px;
  background: linear-gradient(145deg, var(--neu-bg-light), var(--neu-bg), var(--neu-bg-dark));
  border-radius: var(--neu-radius-lg);
  box-shadow: var(--neu-extruded);
  text-align: center;
}

.neu-hero__title {
  font-size: 36px;
  font-weight: 500;
  color: var(--neu-heading);
  margin: 0 0 16px;
}

.neu-hero__subtitle {
  font-size: 18px;
  color: var(--neu-text-secondary);
  max-width: 600px;
  margin: 0 0 32px;
}
```

## Toggle / Switch

```css
.neu-toggle {
  position: relative;
  width: 56px;
  height: 28px;
  background: var(--neu-bg);
  border-radius: 14px;
  box-shadow: var(--neu-pressed);
  cursor: pointer;
  transition: background var(--neu-transition);
}

.neu-toggle::after {
  content: '';
  position: absolute;
  top: 4px;
  left: 4px;
  width: 20px;
  height: 20px;
  background: var(--neu-bg);
  border-radius: 50%;
  box-shadow: var(--neu-extruded);
  transition: transform var(--neu-transition);
}

.neu-toggle--active {
  background: var(--neu-accent);
}

.neu-toggle--active::after {
  transform: translateX(28px);
}
```

## Slider / Range

```css
.neu-slider {
  width: 100%;
  height: 8px;
  background: var(--neu-bg);
  border-radius: 4px;
  box-shadow: var(--neu-pressed);
  -webkit-appearance: none;
}

.neu-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  background: var(--neu-bg);
  border-radius: 50%;
  box-shadow: var(--neu-extruded);
  cursor: pointer;
  transition: box-shadow var(--neu-transition);
}

.neu-slider::-webkit-slider-thumb:hover {
  box-shadow: var(--neu-elevated);
}
```

## Progress Bar

```css
.neu-progress {
  width: 100%;
  height: 12px;
  background: var(--neu-bg);
  border-radius: 6px;
  box-shadow: var(--neu-pressed);
  overflow: hidden;
}

.neu-progress__fill {
  height: 100%;
  background: var(--neu-accent);
  border-radius: 6px;
  transition: width var(--neu-transition);
}
```

## Badge / Chip

```css
.neu-badge {
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  font-size: 12px;
  font-weight: 500;
  color: var(--neu-text);
  background: var(--neu-bg);
  border-radius: var(--neu-radius-sm);
  box-shadow: var(--neu-extruded);
}

.neu-badge--success { color: var(--neu-success); }
.neu-badge--error { color: var(--neu-error); }
.neu-badge--warning { color: var(--neu-warning); }
```

## Container / Layout

```css
.neu-container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.neu-grid {
  display: grid;
  gap: 24px;
}

.neu-grid--2 { grid-template-columns: repeat(2, 1fr); }
.neu-grid--3 { grid-template-columns: repeat(3, 1fr); }
.neu-grid--4 { grid-template-columns: repeat(4, 1fr); }

@media (max-width: 768px) {
  .neu-grid--2,
  .neu-grid--3,
  .neu-grid--4 {
    grid-template-columns: 1fr;
  }
}
```

## Divider

```css
.neu-divider {
  height: 2px;
  background: var(--neu-bg);
  border: none;
  border-radius: 1px;
  box-shadow: var(--neu-pressed);
  margin: 24px 0;
}
```
