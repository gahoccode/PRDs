# Accessible Hamburger Navigation Pattern

Complete implementation for keyboard and screen reader accessible mobile navigation.

## HTML Structure

```html
<header class="header">
  <div class="header-inner">
    <a href="/" class="logo" aria-label="Home">
      <svg><!-- Logo SVG --></svg>
    </a>
    
    <button 
      class="nav-toggle" 
      aria-expanded="false" 
      aria-controls="nav-menu"
      aria-label="Open menu"
    >
      <span class="hamburger" aria-hidden="true"></span>
    </button>
    
    <nav id="nav-menu" class="nav" aria-label="Main navigation">
      <ul class="nav-list" role="list">
        <li><a href="#features">Features</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
```

## CSS

```css
/* Header layout */
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--bg, #fff);
}

.header-inner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-sm, 0.75rem);
  padding: var(--space-sm, 0.75rem) var(--space-md, 1rem);
  max-width: var(--content-width, 1200px);
  margin: 0 auto;
}

/* Logo */
.logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}

/* Navigation toggle button */
.nav-toggle {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  z-index: 101;
}

/* Hamburger icon */
.hamburger,
.hamburger::before,
.hamburger::after {
  display: block;
  width: 24px;
  height: 2px;
  background: currentColor;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.hamburger {
  position: relative;
}

.hamburger::before,
.hamburger::after {
  content: '';
  position: absolute;
  left: 0;
}

.hamburger::before { top: -8px; }
.hamburger::after { bottom: -8px; }

/* Hamburger to X animation */
.nav-toggle[aria-expanded="true"] .hamburger {
  background: transparent;
}

.nav-toggle[aria-expanded="true"] .hamburger::before {
  transform: translateY(8px) rotate(45deg);
}

.nav-toggle[aria-expanded="true"] .hamburger::after {
  transform: translateY(-8px) rotate(-45deg);
}

/* Navigation list */
.nav-list {
  display: flex;
  gap: var(--space-md, 1rem);
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-list a {
  display: block;
  padding: var(--space-xs, 0.5rem) var(--space-sm, 0.75rem);
  text-decoration: none;
  color: inherit;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.nav-list a:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.nav-list a:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

/* Mobile styles */
@media (max-width: 600px) {
  .nav-toggle {
    display: flex;
  }
  
  .nav {
    position: fixed;
    inset: 0;
    background: var(--bg, #fff);
    display: flex;
    align-items: center;
    justify-content: center;
    transform: translateX(100%);
    visibility: hidden;
    transition: transform 0.3s ease, visibility 0.3s ease;
  }
  
  .nav[data-visible="true"] {
    transform: translateX(0);
    visibility: visible;
  }
  
  .nav-list {
    flex-direction: column;
    align-items: center;
    gap: var(--space-lg, 1.5rem);
  }
  
  .nav-list a {
    font-size: var(--fs-lg, 1.25rem);
    padding: var(--space-sm, 0.75rem) var(--space-lg, 1.5rem);
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .hamburger,
  .hamburger::before,
  .hamburger::after,
  .nav,
  .nav-list a {
    transition: none;
  }
}
```

## JavaScript

```javascript
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  const navLinks = nav?.querySelectorAll('a');
  
  if (!toggle || !nav) return;
  
  // Toggle menu
  function toggleMenu(open) {
    const isOpen = open ?? toggle.getAttribute('aria-expanded') !== 'true';
    
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
    nav.setAttribute('data-visible', String(isOpen));
    
    // Prevent body scroll when menu is open
    document.body.style.overflow = isOpen ? 'hidden' : '';
    
    // Focus first link when opening
    if (isOpen && navLinks?.length) {
      navLinks[0].focus();
    }
  }
  
  // Toggle on button click
  toggle.addEventListener('click', () => toggleMenu());
  
  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      toggleMenu(false);
      toggle.focus();
    }
  });
  
  // Close when clicking a link
  navLinks?.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 600) {
        toggleMenu(false);
      }
    });
  });
  
  // Close on resize to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth > 600 && toggle.getAttribute('aria-expanded') === 'true') {
      toggleMenu(false);
    }
  });
  
  // Focus trap within nav when open
  nav.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab' || toggle.getAttribute('aria-expanded') !== 'true') return;
    
    const focusable = [toggle, ...navLinks];
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });
});
```

## Accessibility Requirements Met

1. **Keyboard accessible**: Tab, Enter, Space, Escape all work correctly
2. **Screen reader friendly**: aria-expanded, aria-controls, aria-label
3. **Focus management**: First link focused on open, toggle focused on close
4. **Focus trap**: Tab cycling within open menu
5. **Reduced motion**: Respects prefers-reduced-motion
6. **Touch targets**: 44×44px minimum
7. **Visual indicators**: Focus-visible styling
