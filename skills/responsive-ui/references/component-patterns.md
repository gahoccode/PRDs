# Responsive Component Patterns

Production-ready patterns for common UI components across all viewport sizes.

## Navigation Components

### Hamburger Menu (≤600px) → Full Nav (>600px)

See `accessible-nav.md` for complete implementation.

### Mega Menu → Accordion

```css
.mega-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--bg);
  padding: var(--space-lg);
}

.nav-item:hover .mega-menu,
.nav-item:focus-within .mega-menu {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-md);
}

@media (max-width: 768px) {
  .mega-menu {
    position: static;
    display: none;
    grid-template-columns: 1fr;
  }
  
  .nav-item[data-expanded="true"] .mega-menu {
    display: block;
  }
}
```

### Off-Canvas Drawer

```css
.drawer {
  position: fixed;
  top: 0;
  left: 0;
  width: min(320px, 85vw);
  height: 100%;
  background: var(--bg);
  transform: translateX(-100%);
  transition: transform 0.3s ease;
  z-index: 200;
  overflow-y: auto;
}

.drawer[data-open="true"] {
  transform: translateX(0);
}

.drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s;
}

.drawer[data-open="true"] ~ .drawer-overlay {
  opacity: 1;
  visibility: visible;
}
```

### Sticky Header

```css
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--bg);
  transition: box-shadow 0.2s;
}

.header[data-scrolled="true"] {
  box-shadow: var(--shadow-md);
}
```

```js
window.addEventListener('scroll', () => {
  document.querySelector('.header')
    ?.toggleAttribute('data-scrolled', window.scrollY > 10);
}, { passive: true });
```

## Form Components

### Text Field / Input

```css
.input {
  width: 100%;
  padding: var(--space-sm) var(--space-md);
  font-size: var(--fs-base);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  min-height: 44px; /* Touch target */
}

.input:focus {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}
```

### Dropdown / Select

```css
.select {
  width: 100%;
  padding: var(--space-sm) var(--space-md);
  padding-right: 2.5rem;
  font-size: var(--fs-base);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--bg) url("data:image/svg+xml,...") no-repeat right 0.75rem center;
  background-size: 1rem;
  appearance: none;
  min-height: 44px;
  cursor: pointer;
}

/* Custom dropdown on desktop only */
@media (min-width: 768px) {
  .select-custom { display: block; }
  .select-native { display: none; }
}

@media (max-width: 767px) {
  .select-custom { display: none; }
  .select-native { display: block; }
}
```

### Switch / Toggle

```css
.switch {
  position: relative;
  width: 52px;
  height: 32px;
  min-width: 44px; /* Touch target */
  min-height: 44px;
  padding: 6px 0;
}

.switch-track {
  width: 52px;
  height: 32px;
  background: var(--border);
  border-radius: 16px;
  transition: background 0.2s;
}

.switch-thumb {
  position: absolute;
  top: 8px;
  left: 2px;
  width: 28px;
  height: 28px;
  background: white;
  border-radius: 50%;
  transition: transform 0.2s;
  box-shadow: var(--shadow-sm);
}

.switch[aria-checked="true"] .switch-track {
  background: var(--primary);
}

.switch[aria-checked="true"] .switch-thumb {
  transform: translateX(20px);
}
```

### Date Picker

```css
/* Use native on mobile for better UX */
.date-input[type="date"] {
  width: 100%;
  padding: var(--space-sm);
  font-size: var(--fs-base);
  min-height: 44px;
}

@media (min-width: 768px) {
  .date-input-custom { display: block; }
  .date-input[type="date"] { display: none; }
}

@media (max-width: 767px) {
  .date-input-custom { display: none; }
  .date-input[type="date"] { display: block; }
}
```

### Slider / Range

```css
.range {
  width: 100%;
  height: 44px; /* Touch target */
  -webkit-appearance: none;
  background: transparent;
}

.range::-webkit-slider-track {
  height: 8px;
  background: var(--border);
  border-radius: 4px;
}

.range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  background: var(--primary);
  border-radius: 50%;
  cursor: pointer;
  margin-top: -8px;
}

/* Firefox */
.range::-moz-range-thumb {
  width: 24px;
  height: 24px;
  background: var(--primary);
  border-radius: 50%;
  border: none;
  cursor: pointer;
}
```

### Autocomplete / Typeahead

```css
.autocomplete {
  position: relative;
}

.autocomplete-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  max-height: 240px;
  overflow-y: auto;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-md);
  z-index: 50;
}

.autocomplete-item {
  padding: var(--space-sm) var(--space-md);
  min-height: 44px;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.autocomplete-item:hover,
.autocomplete-item[data-highlighted="true"] {
  background: var(--surface);
}
```

## Feedback Components

### Modal / Dialog

```css
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-md);
  z-index: 300;
}

.modal {
  background: var(--bg);
  border-radius: var(--radius-lg);
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
}

/* Full-screen on mobile */
@media (max-width: 480px) {
  .modal-overlay {
    padding: 0;
    align-items: stretch;
  }
  
  .modal {
    max-width: none;
    max-height: none;
    border-radius: 0;
    height: 100%;
  }
}
```

### Toast / Snackbar

```css
.toast-container {
  position: fixed;
  bottom: var(--space-md);
  left: 50%;
  transform: translateX(-50%);
  z-index: 400;
  width: min(90vw, 400px);
}

.toast {
  background: var(--text);
  color: var(--bg);
  padding: var(--space-sm) var(--space-md);
  border-radius: var(--radius-sm);
  margin-top: var(--space-xs);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-sm);
  animation: toast-in 0.3s ease;
}

@keyframes toast-in {
  from { transform: translateY(100%); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* Stack vertically, adjust position on mobile */
@media (max-width: 480px) {
  .toast-container {
    bottom: 0;
    left: 0;
    right: 0;
    transform: none;
    width: 100%;
  }
  
  .toast {
    border-radius: 0;
  }
}
```

### Tooltip

```css
.tooltip-trigger {
  position: relative;
}

.tooltip {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  padding: var(--space-xs) var(--space-sm);
  background: var(--text);
  color: var(--bg);
  font-size: var(--fs-sm);
  border-radius: var(--radius-sm);
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s;
  pointer-events: none;
  z-index: 50;
}

/* Hover on desktop */
@media (hover: hover) {
  .tooltip-trigger:hover .tooltip,
  .tooltip-trigger:focus .tooltip {
    opacity: 1;
    visibility: visible;
  }
}

/* Tap-to-show on touch */
@media (hover: none) {
  .tooltip-trigger[data-tooltip-visible="true"] .tooltip {
    opacity: 1;
    visibility: visible;
  }
}
```

```js
// Touch device tooltip handling
if ('ontouchstart' in window) {
  document.querySelectorAll('.tooltip-trigger').forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const isVisible = el.dataset.tooltipVisible === 'true';
      document.querySelectorAll('.tooltip-trigger')
        .forEach(t => t.dataset.tooltipVisible = 'false');
      el.dataset.tooltipVisible = String(!isVisible);
    });
  });
}
```

## Content Components

### Card

```css
.card {
  background: var(--bg);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

.card-image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  width: 100%;
}

.card-content {
  padding: var(--space-md);
}

/* Card grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
  gap: var(--space-md);
}
```

### Carousel / Slider

```css
.carousel {
  position: relative;
  overflow: hidden;
}

.carousel-track {
  display: flex;
  transition: transform 0.3s ease;
}

.carousel-slide {
  flex: 0 0 100%;
  min-width: 0;
}

/* Multiple slides on larger screens */
@media (min-width: 600px) {
  .carousel-slide { flex: 0 0 50%; }
}

@media (min-width: 900px) {
  .carousel-slide { flex: 0 0 33.333%; }
}

.carousel-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  background: var(--bg);
  border: none;
  border-radius: 50%;
  box-shadow: var(--shadow-md);
  cursor: pointer;
  z-index: 10;
}

.carousel-prev { left: var(--space-sm); }
.carousel-next { right: var(--space-sm); }

/* Hide arrows on touch, rely on swipe */
@media (hover: none) {
  .carousel-nav { display: none; }
}

.carousel-dots {
  display: flex;
  justify-content: center;
  gap: var(--space-xs);
  margin-top: var(--space-sm);
}

.carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--border);
  border: none;
  cursor: pointer;
  padding: 0;
}

.carousel-dot[data-active="true"] {
  background: var(--primary);
}
```

### Accordion

```css
.accordion-item {
  border-bottom: 1px solid var(--border);
}

.accordion-trigger {
  width: 100%;
  padding: var(--space-md);
  background: transparent;
  border: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: var(--fs-base);
  text-align: left;
  cursor: pointer;
  min-height: 44px;
}

.accordion-icon {
  transition: transform 0.2s;
}

.accordion-trigger[aria-expanded="true"] .accordion-icon {
  transform: rotate(180deg);
}

.accordion-panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.3s ease;
}

.accordion-trigger[aria-expanded="true"] + .accordion-panel {
  grid-template-rows: 1fr;
}

.accordion-content {
  overflow: hidden;
  padding: 0 var(--space-md);
}

.accordion-trigger[aria-expanded="true"] + .accordion-panel .accordion-content {
  padding-bottom: var(--space-md);
}
```

### Tabs

```css
.tabs {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-xs);
  border-bottom: 1px solid var(--border);
}

.tab {
  padding: var(--space-sm) var(--space-md);
  background: transparent;
  border: none;
  font-size: var(--fs-base);
  cursor: pointer;
  position: relative;
  min-height: 44px;
}

.tab[aria-selected="true"]::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--primary);
}

.tab-panel {
  display: none;
  padding: var(--space-md) 0;
}

.tab-panel[data-active="true"] {
  display: block;
}

/* Scrollable tabs on mobile */
@media (max-width: 480px) {
  .tabs {
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  
  .tabs::-webkit-scrollbar { display: none; }
  
  .tab { white-space: nowrap; }
}
```

### Masonry Layout

```css
/* CSS columns approach */
.masonry {
  columns: 1;
  column-gap: var(--space-md);
}

.masonry-item {
  break-inside: avoid;
  margin-bottom: var(--space-md);
}

@media (min-width: 500px) {
  .masonry { columns: 2; }
}

@media (min-width: 800px) {
  .masonry { columns: 3; }
}

@media (min-width: 1200px) {
  .masonry { columns: 4; }
}
```

## Progress Components

### Stepper

```css
.stepper {
  display: flex;
  justify-content: space-between;
  position: relative;
}

.stepper::before {
  content: '';
  position: absolute;
  top: 20px;
  left: 40px;
  right: 40px;
  height: 2px;
  background: var(--border);
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 1;
}

.step-indicator {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--bg);
  border: 2px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}

.step[data-status="complete"] .step-indicator {
  background: var(--primary);
  border-color: var(--primary);
  color: white;
}

.step[data-status="current"] .step-indicator {
  border-color: var(--primary);
  color: var(--primary);
}

.step-label {
  margin-top: var(--space-xs);
  font-size: var(--fs-sm);
  text-align: center;
}

/* Vertical stepper on mobile */
@media (max-width: 480px) {
  .stepper {
    flex-direction: column;
    gap: var(--space-md);
  }
  
  .stepper::before {
    top: 20px;
    bottom: 20px;
    left: 19px;
    right: auto;
    width: 2px;
    height: auto;
  }
  
  .step {
    flex-direction: row;
    gap: var(--space-sm);
  }
  
  .step-label {
    margin-top: 0;
    text-align: left;
  }
}
```

### Skeleton Loader

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--border) 25%,
    var(--surface) 50%,
    var(--border) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.5s infinite;
  border-radius: var(--radius-sm);
}

.skeleton-text {
  height: 1em;
  margin-bottom: 0.5em;
}

.skeleton-text:last-child {
  width: 70%;
}

.skeleton-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
}

.skeleton-image {
  aspect-ratio: 16 / 9;
}

@keyframes skeleton-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

@media (prefers-reduced-motion: reduce) {
  .skeleton { animation: none; }
}
```

### Spinner / Loader

```css
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid var(--border);
  border-top-color: var(--primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.spinner-lg {
  width: 48px;
  height: 48px;
  border-width: 4px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .spinner { animation: none; }
}
```

## Action Components

### Floating Action Button (FAB)

```css
.fab {
  position: fixed;
  bottom: var(--space-lg);
  right: var(--space-lg);
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  border: none;
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 100;
  transition: transform 0.2s, box-shadow 0.2s;
}

.fab:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.fab:active {
  transform: scale(0.95);
}

/* Adjust for mobile bottom nav */
@media (max-width: 600px) {
  .fab {
    bottom: calc(var(--space-lg) + 60px); /* Above bottom nav */
  }
}
```

### Ghost Button

```css
.btn-ghost {
  padding: var(--space-sm) var(--space-md);
  background: transparent;
  border: 2px solid currentColor;
  color: var(--text);
  font-size: var(--fs-base);
  border-radius: var(--radius-sm);
  cursor: pointer;
  min-height: 44px;
  transition: background 0.2s, color 0.2s;
}

.btn-ghost:hover {
  background: var(--text);
  color: var(--bg);
}
```

### Chips / Pills / Tags

```css
.chip {
  display: inline-flex;
  align-items: center;
  gap: var(--space-xs);
  padding: var(--space-xs) var(--space-sm);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 9999px;
  font-size: var(--fs-sm);
}

.chip-remove {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.chip-remove:hover {
  background: rgba(0, 0, 0, 0.1);
}

/* Scrollable chip list on mobile */
.chip-list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-xs);
}

@media (max-width: 480px) {
  .chip-list-scroll {
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    padding-bottom: var(--space-xs);
  }
  
  .chip-list-scroll .chip {
    flex-shrink: 0;
  }
}
```

### Breadcrumbs

```css
.breadcrumbs {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-xs);
  font-size: var(--fs-sm);
}

.breadcrumb-item {
  display: flex;
  align-items: center;
  gap: var(--space-xs);
}

.breadcrumb-item:not(:last-child)::after {
  content: '/';
  color: var(--text-muted);
}

.breadcrumb-link {
  color: var(--text-muted);
  min-height: 44px;
  display: flex;
  align-items: center;
}

.breadcrumb-link:hover {
  color: var(--text);
}

.breadcrumb-current {
  color: var(--text);
  font-weight: 500;
}

/* Truncate middle items on mobile */
@media (max-width: 480px) {
  .breadcrumbs[data-truncate="true"] .breadcrumb-item:not(:first-child):not(:last-child) {
    display: none;
  }
  
  .breadcrumbs[data-truncate="true"]::before {
    content: '...';
    color: var(--text-muted);
  }
}
```

## Visual Effects

### Skeleton Screen (Page-level)

```css
.page-skeleton {
  padding: var(--space-md);
}

.page-skeleton .skeleton-header {
  height: 60px;
  margin-bottom: var(--space-lg);
}

.page-skeleton .skeleton-hero {
  height: 300px;
  margin-bottom: var(--space-lg);
}

.page-skeleton .skeleton-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
  gap: var(--space-md);
}
```

### Lazy Loading Images

```html
<img
  src="placeholder.jpg"
  data-src="actual-image.jpg"
  data-srcset="image-400.jpg 400w, image-800.jpg 800w"
  alt="Description"
  loading="lazy"
  class="lazy-image"
>
```

```css
.lazy-image {
  opacity: 0;
  transition: opacity 0.3s;
}

.lazy-image[data-loaded="true"] {
  opacity: 1;
}
```

```js
// Native lazy loading with fallback
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img[data-src]').forEach(img => {
    img.src = img.dataset.src;
    if (img.dataset.srcset) img.srcset = img.dataset.srcset;
  });
} else {
  // Fallback: Intersection Observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        if (img.dataset.srcset) img.srcset = img.dataset.srcset;
        img.dataset.loaded = 'true';
        observer.unobserve(img);
      }
    });
  });
  
  document.querySelectorAll('img[data-src]').forEach(img => observer.observe(img));
}
```

### Infinite Scroll

```js
const sentinel = document.querySelector('.scroll-sentinel');
const container = document.querySelector('.content-container');

const observer = new IntersectionObserver(async (entries) => {
  if (entries[0].isIntersecting) {
    // Load more content
    const newContent = await fetchMoreContent();
    container.insertAdjacentHTML('beforeend', newContent);
  }
}, { rootMargin: '200px' });

observer.observe(sentinel);
```

```html
<div class="content-container">
  <!-- Content items -->
</div>
<div class="scroll-sentinel" aria-hidden="true"></div>
```
