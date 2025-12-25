# Testing Checklist for Responsive UI

Run through this checklist on real hardware and Chrome DevTools to verify responsive implementation.

## Chrome DevTools Testing

### Viewport Testing

1. Open DevTools → Toggle Device Toolbar (Ctrl/Cmd+Shift+M)
2. Test these breakpoints:
   - [ ] 280px (Galaxy Fold inner screen)
   - [ ] 320px (iPhone SE)
   - [ ] 375px (iPhone 12/13/14)
   - [ ] 390px (iPhone 14 Pro)
   - [ ] 428px (iPhone 14 Plus)
   - [ ] 768px (iPad portrait)
   - [ ] 1024px (iPad landscape / small laptop)
   - [ ] 1280px (Standard laptop)
   - [ ] 1440px (Large laptop / small desktop)
   - [ ] 1920px (Full HD)
   - [ ] 2560px (QHD / Ultra-wide)

### At Each Breakpoint Verify

- [ ] No horizontal scrollbar appears
- [ ] All text is readable (not truncated/overlapping)
- [ ] Touch targets are ≥44×44px on mobile
- [ ] Navigation is accessible and functional
- [ ] Images scale appropriately
- [ ] Spacing feels balanced

## Navigation Testing

### Hamburger Menu (≤600px)

- [ ] Hamburger icon visible
- [ ] Click/tap opens menu
- [ ] Menu animates smoothly
- [ ] All links accessible
- [ ] Clicking outside closes menu
- [ ] Escape key closes menu

### Desktop Nav (>600px)

- [ ] Full navigation visible
- [ ] Hamburger icon hidden
- [ ] Links have hover states
- [ ] Active state visible

## Keyboard Testing

- [ ] Tab moves focus in logical order
- [ ] Focus visible on all interactive elements
- [ ] Enter/Space activates buttons and links
- [ ] Skip link present and functional (optional)
- [ ] Modal/menu traps focus when open

## Screen Reader Testing

Use VoiceOver (Mac), NVDA (Windows), or TalkBack (Android):

- [ ] Page structure announced correctly
- [ ] Landmarks identified (header, main, footer)
- [ ] Images have meaningful alt text
- [ ] Links and buttons have accessible names
- [ ] Navigation state announced (expanded/collapsed)

## Lighthouse Audit

Run in Chrome DevTools → Lighthouse tab:

### Performance (Target: ≥95)

- [ ] First Contentful Paint < 1.8s
- [ ] Largest Contentful Paint < 2.5s
- [ ] Cumulative Layout Shift < 0.1
- [ ] Images properly sized
- [ ] Lazy loading working

### Accessibility (Target: ≥95)

- [ ] Color contrast passes WCAG AA
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] ARIA attributes valid
- [ ] Heading hierarchy correct

### Best Practices (Target: ≥90)

- [ ] HTTPS used
- [ ] No console errors
- [ ] Images have aspect ratio

### SEO (Target: ≥90)

- [ ] Meta viewport set
- [ ] Document has title
- [ ] Links have descriptive text

## Real Device Testing

Test on actual hardware when possible:

### iOS Safari

- [ ] Layout correct
- [ ] Touch interactions work
- [ ] Bottom bar doesn't overlap content
- [ ] 100vh issue handled (use 100dvh or JS)

### Android Chrome

- [ ] Layout correct
- [ ] Touch interactions work
- [ ] Address bar resize handled

### Desktop Browsers

- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

## Network Conditions

Test in DevTools → Network → Throttling:

- [ ] Fast 3G: Page usable within 5s
- [ ] Slow 3G: Core content loads first
- [ ] Offline: Shows fallback (if PWA)

## Component-Specific Testing

### Navigation Components

#### Hamburger Menu
- [ ] Icon visible at ≤600px
- [ ] Menu opens/closes on tap/click
- [ ] aria-expanded toggles correctly
- [ ] Focus trapped when open
- [ ] Escape closes menu
- [ ] Links work and close menu

#### Mega Menu
- [ ] Opens on hover (desktop)
- [ ] Collapses to accordion (mobile)
- [ ] Keyboard navigable
- [ ] Closes on outside click

#### Off-Canvas Drawer
- [ ] Slides in smoothly
- [ ] Overlay visible behind
- [ ] Body scroll locked when open
- [ ] Close button accessible

#### Sticky Header
- [ ] Sticks on scroll
- [ ] Shadow appears when scrolled
- [ ] Doesn't overlap content
- [ ] Works with safe-area-inset (iOS)

### Form Components

#### Text Input / Textarea
- [ ] Min-height 44px (touch target)
- [ ] Focus ring visible
- [ ] Label associated correctly
- [ ] Error states visible

#### Dropdown / Select
- [ ] Native select on mobile
- [ ] Custom dropdown on desktop (if used)
- [ ] Touch target ≥44px
- [ ] All options reachable

#### Switch / Toggle
- [ ] Touch target ≥44px
- [ ] Visual state clear
- [ ] aria-checked updates
- [ ] Works with keyboard (Space)

#### Date Picker
- [ ] Native picker on mobile
- [ ] Custom picker on desktop (if used)
- [ ] All dates selectable
- [ ] Keyboard navigable

#### Slider / Range
- [ ] Thumb grabbable on touch
- [ ] Value updates smoothly
- [ ] Min/max respected
- [ ] Accessible labels

#### Autocomplete
- [ ] Suggestions appear on type
- [ ] Arrow keys navigate options
- [ ] Enter selects option
- [ ] Escape closes dropdown
- [ ] Touch-friendly option height

### Feedback Components

#### Modal / Dialog
- [ ] Full-screen on mobile (≤480px)
- [ ] Centered overlay on desktop
- [ ] Focus trapped inside
- [ ] Escape closes modal
- [ ] Background scroll locked
- [ ] Close button accessible

#### Toast / Snackbar
- [ ] Appears at bottom
- [ ] Full-width on mobile
- [ ] Auto-dismisses (or has close)
- [ ] Multiple toasts stack
- [ ] Doesn't block content

#### Tooltip
- [ ] Shows on hover (desktop)
- [ ] Shows on tap (mobile)
- [ ] Positioned correctly
- [ ] Doesn't overflow viewport
- [ ] Hides on scroll/outside tap

### Content Components

#### Card
- [ ] Content scales with container
- [ ] Image aspect ratio maintained
- [ ] Touch targets ≥44px for links/buttons
- [ ] Grid reflows correctly

#### Carousel / Slider
- [ ] Swipe works on touch
- [ ] Arrows visible on desktop
- [ ] Dots/indicators accessible
- [ ] Correct slide count per viewport
- [ ] No layout shift on load

#### Accordion
- [ ] Headers expand/collapse on click
- [ ] aria-expanded updates
- [ ] Animation smooth
- [ ] Keyboard accessible (Enter/Space)
- [ ] Only one open (if single-select)

#### Tabs
- [ ] Scrollable on mobile if needed
- [ ] Active tab visible
- [ ] Panel content shows correctly
- [ ] Arrow keys navigate tabs
- [ ] Focus management correct

#### Masonry Layout
- [ ] Columns adjust per viewport
- [ ] No orphaned items
- [ ] Images load without layout shift

### Progress Components

#### Stepper
- [ ] Horizontal on desktop
- [ ] Vertical on mobile (if designed)
- [ ] Current step highlighted
- [ ] Completed steps indicated
- [ ] Labels readable

#### Skeleton Loader
- [ ] Matches content layout
- [ ] Animation smooth
- [ ] Respects prefers-reduced-motion
- [ ] Replaces with content correctly

#### Spinner
- [ ] Visible and centered
- [ ] Size appropriate
- [ ] Respects prefers-reduced-motion

### Action Components

#### FAB (Floating Action Button)
- [ ] Fixed position maintained
- [ ] Doesn't overlap bottom nav
- [ ] Touch target ≥56px
- [ ] Accessible label present

#### Ghost Button
- [ ] Touch target ≥44px
- [ ] Hover state visible
- [ ] Focus ring visible
- [ ] Contrast sufficient

#### Chips / Pills
- [ ] Scrollable container on mobile
- [ ] Remove button accessible
- [ ] Touch targets adequate
- [ ] Selected state visible

#### Breadcrumbs
- [ ] Truncates correctly on mobile
- [ ] All links work
- [ ] Current page indicated
- [ ] Separator visible

### Visual Effects

#### Lazy Loading
- [ ] Placeholder visible before load
- [ ] Image fades in smoothly
- [ ] No layout shift
- [ ] Works without JS (fallback)

#### Infinite Scroll
- [ ] New content loads on scroll
- [ ] Loading indicator visible
- [ ] Focus management correct
- [ ] "End of content" message (if applicable)

#### Skeleton Screen
- [ ] Layout matches final content
- [ ] Animation smooth
- [ ] Disappears on content load

## Common Issues to Watch

1. **Horizontal scroll** — Usually caused by:
   - Fixed-width elements
   - `width: 100vw` (includes scrollbar)
   - Padding/margin on body/html
   - Overflow on absolute positioned elements

2. **Text overflow** — Check for:
   - Long words without `overflow-wrap: break-word`
   - Fixed heights on containers
   - `white-space: nowrap` without handling

3. **Image issues** — Verify:
   - `max-width: 100%` applied
   - Height not fixed
   - srcset serving correct sizes

4. **Touch target size** — Ensure:
   - Buttons/links ≥44×44px
   - Adequate spacing between targets
