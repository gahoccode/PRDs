# Rustic Food - Tailwind CSS Configuration

Drop-in Tailwind config for the Rustic Food design system.

## tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue,svelte}",
  ],
  theme: {
    extend: {
      colors: {
        cream: '#FDF6E3',
        'warm-white': '#FFFBF5',
        terracotta: {
          DEFAULT: '#C75B39',
          dark: '#A63D2E', // paprika
        },
        sage: '#7A9E7E',
        olive: '#6B7B3C',
        espresso: '#3D2B1F',
        charcoal: '#4A4A4A',
        honey: '#D4A84B',
        linen: '#E8E0D5',
      },
      fontFamily: {
        heading: ['Playfair Display', 'Georgia', 'serif'],
        body: ['Source Sans 3', 'system-ui', 'sans-serif'],
        accent: ['Dancing Script', 'cursive'],
      },
      fontSize: {
        'hero': ['3.5rem', { lineHeight: '1.1' }],
        'hero-lg': ['4rem', { lineHeight: '1.05' }],
      },
      boxShadow: {
        'rf-sm': '0 2px 8px rgba(61, 43, 31, 0.08)',
        'rf-md': '0 4px 16px rgba(61, 43, 31, 0.1)',
        'rf-lg': '0 8px 32px rgba(61, 43, 31, 0.12)',
        'rf-hover': '0 12px 40px rgba(61, 43, 31, 0.15)',
      },
      borderRadius: {
        'rf-sm': '4px',
        'rf-md': '8px',
        'rf-lg': '16px',
        'organic': '40% 60% 55% 45% / 55% 45% 60% 40%',
      },
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
        '30': '7.5rem',
      },
      backgroundImage: {
        'grain': "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E\")",
      },
    },
  },
  plugins: [],
}
```

## Usage Examples

### Basic Page Structure

```html
<body class="bg-cream font-body text-charcoal">
  <nav class="bg-cream/95 backdrop-blur-sm sticky top-0 z-50 shadow-rf-sm">
    <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
      <a href="/" class="font-accent text-2xl text-terracotta">Rustic Kitchen</a>
      <ul class="flex gap-8">
        <li><a href="#" class="font-body font-medium text-espresso hover:text-terracotta transition-colors">Menu</a></li>
        <li><a href="#" class="font-body font-medium text-espresso hover:text-terracotta transition-colors">About</a></li>
        <li><a href="#" class="font-body font-medium text-espresso hover:text-terracotta transition-colors">Contact</a></li>
      </ul>
    </div>
  </nav>
</body>
```

### Hero Section

```html
<section class="relative h-[80vh] min-h-[500px] flex items-center justify-center">
  <img src="hero.jpg" alt="" class="absolute inset-0 w-full h-full object-cover">
  <div class="absolute inset-0 bg-gradient-to-b from-espresso/30 to-espresso/50"></div>
  <div class="relative text-center text-white max-w-2xl px-6">
    <span class="font-accent text-lg text-honey">Farm to Table</span>
    <h1 class="font-heading text-hero lg:text-hero-lg font-bold mt-2 mb-6">
      Fresh. Local. Delicious.
    </h1>
    <p class="text-lg opacity-90 mb-8">
      Experience the finest seasonal ingredients prepared with love
    </p>
    <button class="bg-terracotta text-white font-semibold px-8 py-4 rounded-rf-md hover:bg-terracotta-dark transition-all hover:-translate-y-0.5 hover:shadow-rf-lg">
      View Our Menu
    </button>
  </div>
</section>
```

### Recipe Card

```html
<article class="bg-warm-white rounded-rf-lg shadow-rf-sm overflow-hidden group hover:-translate-y-1 hover:shadow-rf-lg transition-all duration-300">
  <div class="relative aspect-[4/3] overflow-hidden">
    <img src="recipe.jpg" alt="Pasta Primavera" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
    <span class="absolute bottom-3 left-3 bg-white/95 px-3 py-1.5 rounded-rf-sm text-sm font-medium text-espresso flex items-center gap-2">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
      30 min
    </span>
  </div>
  <div class="p-6">
    <span class="text-xs uppercase tracking-wider text-sage font-semibold">Pasta</span>
    <h3 class="font-heading text-xl text-espresso mt-1 mb-2">Pasta Primavera</h3>
    <p class="text-charcoal text-[15px] leading-relaxed">
      Fresh seasonal vegetables tossed with al dente pasta in a light garlic sauce
    </p>
    <div class="flex gap-2 mt-4">
      <span class="bg-cream text-olive text-xs px-3 py-1 rounded-full font-medium">Vegetarian</span>
      <span class="bg-cream text-olive text-xs px-3 py-1 rounded-full font-medium">Quick</span>
    </div>
  </div>
</article>
```

### Buttons

```html
<!-- Primary -->
<button class="bg-terracotta text-white font-semibold px-6 py-3 rounded-rf-md hover:bg-terracotta-dark transition-all hover:-translate-y-0.5 hover:shadow-rf-md">
  Order Now
</button>

<!-- Secondary -->
<button class="border-2 border-terracotta text-terracotta font-semibold px-6 py-3 rounded-rf-md hover:bg-terracotta hover:text-white transition-all">
  Learn More
</button>

<!-- Sage accent -->
<button class="bg-sage text-white font-semibold px-6 py-3 rounded-rf-md hover:bg-olive transition-colors">
  Subscribe
</button>
```

### Form Input

```html
<div class="space-y-1.5">
  <label class="block text-sm font-semibold text-espresso">Email Address</label>
  <input 
    type="email" 
    placeholder="your@email.com"
    class="w-full px-4 py-3 bg-warm-white border-2 border-linen rounded-rf-sm text-espresso placeholder:text-gray-400 focus:outline-none focus:border-terracotta focus:ring-2 focus:ring-terracotta/15 transition-all"
  >
</div>
```

### Newsletter Inline Form

```html
<div class="flex gap-3 max-w-md">
  <input 
    type="email" 
    placeholder="Enter your email"
    class="flex-1 px-4 py-3 bg-warm-white border-2 border-linen rounded-rf-sm focus:outline-none focus:border-terracotta transition-colors"
  >
  <button class="bg-terracotta text-white font-semibold px-6 rounded-rf-md hover:bg-terracotta-dark transition-colors">
    Subscribe
  </button>
</div>
```

## Google Fonts Import

Add to your HTML `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Playfair+Display:wght@400;500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
```

Or in CSS:

```css
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Playfair+Display:wght@400;500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap');
```
