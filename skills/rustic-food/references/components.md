# Rustic Food Components

Complete CSS patterns for common food website components.

## Table of Contents
1. [Navigation](#navigation)
2. [Hero Sections](#hero-sections)
3. [Cards](#cards)
4. [Buttons](#buttons)
5. [Forms](#forms)
6. [Menu/Pricing](#menu-pricing)
7. [Testimonials](#testimonials)
8. [Footer](#footer)

---

## Navigation

```css
.rf-nav {
  background: var(--rf-cream);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(61, 43, 31, 0.05);
}

.rf-nav-logo {
  font-family: var(--rf-font-accent);
  font-size: 1.75rem;
  color: var(--rf-terracotta);
}

.rf-nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.rf-nav-link {
  font-family: var(--rf-font-body);
  color: var(--rf-espresso);
  text-decoration: none;
  font-weight: 500;
  position: relative;
}

.rf-nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--rf-terracotta);
  transition: width 300ms ease;
}

.rf-nav-link:hover::after {
  width: 100%;
}

/* Scrolled state */
.rf-nav.scrolled {
  background: rgba(253, 246, 227, 0.95);
  backdrop-filter: blur(10px);
}
```

---

## Hero Sections

### Full-Bleed Image Hero

```css
.rf-hero {
  position: relative;
  height: 80vh;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.rf-hero-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.rf-hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(61, 43, 31, 0.3) 0%,
    rgba(61, 43, 31, 0.5) 100%
  );
}

.rf-hero-content {
  position: relative;
  text-align: center;
  color: white;
  max-width: 700px;
  padding: 2rem;
}

.rf-hero-tagline {
  font-family: var(--rf-font-accent);
  font-size: 1.25rem;
  color: var(--rf-honey);
  margin-bottom: 1rem;
}

.rf-hero-title {
  font-family: var(--rf-font-heading);
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  text-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
}

.rf-hero-subtitle {
  font-family: var(--rf-font-body);
  font-size: 1.125rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}
```

### Split Hero (Image + Content)

```css
.rf-hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 600px;
}

.rf-hero-split-image {
  position: relative;
  overflow: hidden;
}

.rf-hero-split-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.rf-hero-split-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem;
  background: var(--rf-cream);
}

@media (max-width: 768px) {
  .rf-hero-split {
    grid-template-columns: 1fr;
  }
}
```

---

## Cards

### Recipe Card

```css
.rf-recipe-card {
  background: var(--rf-warm-white);
  border-radius: var(--rf-radius-lg);
  overflow: hidden;
  box-shadow: var(--rf-shadow-sm);
  transition: transform 300ms ease, box-shadow 300ms ease;
}

.rf-recipe-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--rf-shadow-lg);
}

.rf-recipe-card-image {
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
}

.rf-recipe-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 500ms ease;
}

.rf-recipe-card:hover .rf-recipe-card-image img {
  transform: scale(1.05);
}

.rf-recipe-card-time {
  position: absolute;
  bottom: 12px;
  left: 12px;
  background: rgba(255, 255, 255, 0.95);
  padding: 0.5rem 0.75rem;
  border-radius: var(--rf-radius-sm);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--rf-espresso);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.rf-recipe-card-body {
  padding: 1.5rem;
}

.rf-recipe-card-category {
  font-family: var(--rf-font-body);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--rf-sage);
  font-weight: 600;
}

.rf-recipe-card-title {
  font-family: var(--rf-font-heading);
  font-size: 1.25rem;
  color: var(--rf-espresso);
  margin: 0.5rem 0;
  line-height: 1.3;
}

.rf-recipe-card-description {
  font-family: var(--rf-font-body);
  font-size: 0.9375rem;
  color: var(--rf-charcoal);
  line-height: 1.6;
}

.rf-recipe-card-tags {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
  flex-wrap: wrap;
}

.rf-tag {
  background: var(--rf-cream);
  color: var(--rf-olive);
  font-size: 0.75rem;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-weight: 500;
}
```

### Menu Item Card

```css
.rf-menu-item {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem;
  background: var(--rf-warm-white);
  border-radius: var(--rf-radius-md);
  transition: background 200ms ease;
}

.rf-menu-item:hover {
  background: var(--rf-cream);
}

.rf-menu-item-image {
  width: 100px;
  height: 100px;
  border-radius: var(--rf-radius-md);
  object-fit: cover;
  flex-shrink: 0;
}

.rf-menu-item-content {
  flex: 1;
}

.rf-menu-item-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}

.rf-menu-item-name {
  font-family: var(--rf-font-heading);
  font-size: 1.125rem;
  color: var(--rf-espresso);
}

.rf-menu-item-price {
  font-family: var(--rf-font-heading);
  font-size: 1.125rem;
  color: var(--rf-terracotta);
  font-weight: 600;
}

.rf-menu-item-description {
  font-family: var(--rf-font-body);
  font-size: 0.9375rem;
  color: var(--rf-charcoal);
  margin-top: 0.5rem;
  line-height: 1.5;
}

.rf-menu-item-dietary {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.rf-dietary-icon {
  width: 20px;
  height: 20px;
  background: var(--rf-sage);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.625rem;
  font-weight: 700;
}
```

---

## Buttons

```css
/* Primary Button */
.rf-btn {
  font-family: var(--rf-font-body);
  font-size: 1rem;
  font-weight: 600;
  padding: 0.875rem 2rem;
  border-radius: var(--rf-radius-md);
  border: none;
  cursor: pointer;
  transition: all 200ms ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.rf-btn-primary {
  background: var(--rf-terracotta);
  color: white;
}

.rf-btn-primary:hover {
  background: var(--rf-paprika);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(199, 91, 57, 0.3);
}

/* Secondary Button */
.rf-btn-secondary {
  background: transparent;
  color: var(--rf-terracotta);
  border: 2px solid var(--rf-terracotta);
}

.rf-btn-secondary:hover {
  background: var(--rf-terracotta);
  color: white;
}

/* Ghost Button */
.rf-btn-ghost {
  background: transparent;
  color: var(--rf-espresso);
}

.rf-btn-ghost:hover {
  background: var(--rf-linen);
}

/* Sage Accent Button */
.rf-btn-sage {
  background: var(--rf-sage);
  color: white;
}

.rf-btn-sage:hover {
  background: var(--rf-olive);
}
```

---

## Forms

```css
.rf-form-group {
  margin-bottom: 1.5rem;
}

.rf-label {
  display: block;
  font-family: var(--rf-font-body);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--rf-espresso);
  margin-bottom: 0.5rem;
}

.rf-input {
  width: 100%;
  padding: 0.875rem 1rem;
  font-family: var(--rf-font-body);
  font-size: 1rem;
  color: var(--rf-espresso);
  background: var(--rf-warm-white);
  border: 2px solid var(--rf-linen);
  border-radius: var(--rf-radius-sm);
  transition: border-color 200ms ease, box-shadow 200ms ease;
}

.rf-input:focus {
  outline: none;
  border-color: var(--rf-terracotta);
  box-shadow: 0 0 0 3px rgba(199, 91, 57, 0.15);
}

.rf-input::placeholder {
  color: #A0A0A0;
}

.rf-textarea {
  min-height: 120px;
  resize: vertical;
}

/* Newsletter inline form */
.rf-newsletter {
  display: flex;
  gap: 0.75rem;
  max-width: 500px;
}

.rf-newsletter .rf-input {
  flex: 1;
}
```

---

## Menu/Pricing

```css
.rf-menu-section {
  margin-bottom: 3rem;
}

.rf-menu-section-title {
  font-family: var(--rf-font-heading);
  font-size: 1.5rem;
  color: var(--rf-espresso);
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.rf-menu-section-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--rf-linen);
}

.rf-menu-section-description {
  font-family: var(--rf-font-accent);
  font-size: 1rem;
  color: var(--rf-charcoal);
  margin-bottom: 1.5rem;
}

/* Price with dots */
.rf-price-line {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
}

.rf-price-name {
  font-family: var(--rf-font-body);
  font-weight: 500;
}

.rf-price-dots {
  flex: 1;
  border-bottom: 2px dotted var(--rf-linen);
  margin: 0 0.5rem;
}

.rf-price-value {
  font-family: var(--rf-font-heading);
  font-weight: 600;
  color: var(--rf-terracotta);
}
```

---

## Testimonials

```css
.rf-testimonial {
  background: var(--rf-warm-white);
  padding: 2rem;
  border-radius: var(--rf-radius-lg);
  position: relative;
}

.rf-testimonial::before {
  content: '"';
  font-family: var(--rf-font-heading);
  font-size: 4rem;
  color: var(--rf-terracotta);
  opacity: 0.2;
  position: absolute;
  top: 0.5rem;
  left: 1rem;
  line-height: 1;
}

.rf-testimonial-text {
  font-family: var(--rf-font-body);
  font-size: 1.125rem;
  color: var(--rf-charcoal);
  line-height: 1.7;
  font-style: italic;
  margin-bottom: 1.5rem;
}

.rf-testimonial-author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.rf-testimonial-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.rf-testimonial-name {
  font-family: var(--rf-font-heading);
  font-size: 1rem;
  color: var(--rf-espresso);
}

.rf-testimonial-role {
  font-family: var(--rf-font-body);
  font-size: 0.875rem;
  color: var(--rf-charcoal);
}

/* Star rating */
.rf-stars {
  color: var(--rf-honey);
  font-size: 1rem;
  letter-spacing: 2px;
}
```

---

## Footer

```css
.rf-footer {
  background: var(--rf-espresso);
  color: var(--rf-cream);
  padding: 4rem 2rem 2rem;
}

.rf-footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.rf-footer-brand {
  font-family: var(--rf-font-accent);
  font-size: 2rem;
  color: var(--rf-honey);
  margin-bottom: 1rem;
}

.rf-footer-tagline {
  font-family: var(--rf-font-body);
  font-size: 1rem;
  opacity: 0.8;
  line-height: 1.6;
}

.rf-footer-title {
  font-family: var(--rf-font-heading);
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: var(--rf-cream);
}

.rf-footer-links {
  list-style: none;
  padding: 0;
}

.rf-footer-links li {
  margin-bottom: 0.75rem;
}

.rf-footer-links a {
  font-family: var(--rf-font-body);
  color: var(--rf-cream);
  opacity: 0.7;
  text-decoration: none;
  transition: opacity 200ms ease;
}

.rf-footer-links a:hover {
  opacity: 1;
}

.rf-footer-bottom {
  border-top: 1px solid rgba(253, 246, 227, 0.1);
  margin-top: 3rem;
  padding-top: 2rem;
  text-align: center;
  font-size: 0.875rem;
  opacity: 0.6;
}

@media (max-width: 768px) {
  .rf-footer-grid {
    grid-template-columns: 1fr 1fr;
  }
}
```
