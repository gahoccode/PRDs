# React Charting Libraries - Stack Research

## Overview

This document provides a comprehensive comparison of popular React charting libraries for web application development. Each library offers unique strengths and integration patterns with major UI frameworks.

## Quick Reference

| Library | UI Framework | License | Chart Types | Best For |
|---------|-------------|---------|-------------|----------|
| **Mantine Charts** | Mantine | MIT | 12+ | Mantine projects, quick setup |
| **MUI X Charts** | Material UI | MIT/Commercial | 10-12+ | MUI projects, enterprise |
| **Ant Design Charts** | Ant Design | Open Source | 27+ | Diverse needs, complex data |
| **Recharts** | Framework-agnostic | MIT | 10+ | Flexibility, popularity |

---

## 1. Mantine Charts (@mantine/charts)

### Overview

- **Version**: 8.3.1 (Latest as of October 2025)
- **License**: MIT (Free and Open Source)
- **Documentation**: https://mantine.dev/charts/getting-started/
- **Technology**: React wrapper for Recharts with enhanced features

### Installation

```bash
npm install @mantine/charts recharts
```

**Important**: Must import styles in specific order:
```javascript
import '@mantine/core/styles.css';
import '@mantine/charts/styles.css';
```

### Chart Types Supported (12+)

- AreaChart, BarChart, LineChart
- CompositeChart, DonutChart, PieChart
- FunnelChart, RadarChart, ScatterChart
- BubbleChart, RadialBarChart
- Sparkline, Heatmap

### Key Features

- **Legend support** with hover highlighting
- **Gradient fills** with customizable color stops
- **Stacked and waterfall** chart variants
- **Reference areas** for highlighting regions
- **Value formatting** for axes and tooltips
- **Custom labels** and point labels
- **Interactive tooltips**
- **Dual Y-axes** support
- **SVG patterns** and color schemes
- Animations (disabled by default but configurable)

### Technical Details

- **Rendering**: SVG-based
- **Bundle Size**: ~1.53 MB uncompressed (@mantine/core: 174 kB minified + gzipped)
- **Tree-shaking**: Reduces footprint by up to 40%
- **TypeScript**: Excellent support (built with TypeScript)
- **Framework Compatibility**:
  - React 18: ✅ Full support
  - Next.js: ✅ Full support (including App Router)
  - SSR: ✅ Supported

### Pros

✅ Seamless integration with Mantine UI components
✅ Pre-built components with sensible defaults
✅ Access to underlying Recharts props for customization
✅ Excellent interactive documentation
✅ Consistent styling with Mantine design system
✅ Strong TypeScript support
✅ Modular architecture

### Cons

❌ Animations disabled by default
❌ Smaller ecosystem (only 30 npm dependents)
❌ Larger bundle size compared to minimal libraries
❌ Limited to Recharts capabilities

### Best For

- Applications already using Mantine UI
- Projects requiring quick setup with good defaults
- Dashboards needing consistent design system integration

### Maintenance Status

🟢 **Actively Maintained** - Latest version published 13 days ago (October 2025)

---

## 2. MUI X Charts

### Overview

- **Version**: v8 (Released April 2025)
- **License**: MIT (Community) / Commercial (Pro)
- **Documentation**: https://mui.com/x/react-charts/
- **Technology**: Custom animation engine with Material Design integration

### Installation

```bash
# Community (Free)
npm install @mui/x-charts

# Pro (Commercial)
npm install @mui/x-charts-pro
```

### Chart Types Supported

#### Community Version (Free)
- Line Charts, Bar Charts (including horizontal)
- Pie (Donut) Charts, Scatter Charts
- Area Charts, Heatmap, Radar Charts

#### Pro Version (Commercial)
- Funnel Charts
- Advanced features: zooming, panning, exporting

#### Roadmap
- Sparkline, Gauge, Pyramid, Sankey

### Key Features

#### Community (Free)
- Essential charts and core features
- Axes, legends, styling customizations
- Tooltips and highlights
- Responsive design
- **Server-side rendering (SSR)** support (added in v8)
- Tight integration with MUI theme
- Composition-based developer experience
- Custom animation engine (replaced React Spring in v8)
- **React 19** compatibility

#### Pro (Commercial)
- Advanced chart types
- Zooming and panning
- Chart exporting
- Commercial license

### Licensing Model

1. **Community**: MIT licensed, free forever
2. **Pro**: Commercial license required
   - Per-developer licensing
   - 30-day trial for non-production use
   - Annual price increase up to 7% at renewal
3. **Premium**: All Pro features + advanced Data Grid

**Pricing**: Community (Free) | Pro/Premium (Contact sales - per-developer annual licensing)

### Technical Details

- **Rendering**: SVG-based
- **Bundle Size**: Medium (heavier than minimal libraries)
- **TypeScript**: Full support with autocomplete
- **Framework Compatibility**:
  - React 16-19: ✅ Full support
  - Next.js: ✅ Compatible
  - SSR: ✅ Supported (v8+)

### Pros

✅ Tight integration with MUI ecosystem
✅ Comprehensive documentation and examples
✅ Actively maintained by MUI team
✅ Professional design out of the box
✅ Strong TypeScript support
✅ SSR support for better initial load and SEO
✅ React 19 compatibility guaranteed
✅ Advanced Pro features for enterprise needs

### Cons

❌ Advanced features require commercial license
❌ Per-developer pricing can be expensive for large teams
❌ Heavier bundle compared to minimal libraries
❌ Locked into MUI ecosystem design patterns

### Best For

- Enterprise applications requiring commercial support
- Projects already using MUI components
- Data-rich dashboards with advanced interactivity
- Applications requiring SSR/SEO optimization

### Maintenance Status

🟢 **Actively Maintained** - Major v8 release in April 2025, regular updates from MUI team

---

## 3. Ant Design Charts

### Overview

- **Version**: 2.6.5
- **License**: Open Source
- **Documentation**: https://ant-design-charts.antgroup.com/en
- **Technology**: React version of G2Plot (built by AntV team at Alibaba Group)

### Installation

```bash
npm install @ant-design/charts
```

### Chart Types Supported (27+)

#### Statistical Charts
- Area, Bar, Column, Line, Pie, Scatter, Stock, Waterfall
- BidirectionalBar, DualAxes, Funnel, Histogram, Radar
- Tiny, Box, Bullet, Venn, Treemap, Circle Packing
- Liquid, Rose, Sunburst, WordCloud, Gauge, Violin
- Sankey, RadialBar

#### Relational Diagrams
- Dendrogram, Indented Tree, MindMap
- Organization Chart, Network Graph
- Flow Direction Graph (FlowGraph)

#### Additional Capabilities
- Geographic visualization support
- Annotation shapes
- Interaction features
- Events handling
- Composite views

### Chart Categories by Purpose

- **Comparison**: Bar, BidirectionalBar, Box, Bullet, Column, Histogram, Radar, Rose
- **Distribution**: Area, Box, Heatmap, Histogram, Scatter, Sunburst
- **Trend/Time**: Area, DualAxes, Line, Stock
- **Proportion**: Pie
- **Flow/Relation**: Funnel, Sankey
- **Interval**: Area, Gauge

### Key Features

- Easy to use with TypeScript support
- Pretty & lightweight design
- Responsive layouts
- Storytelling capabilities
- Out-of-the-box high-quality charts with default configurations
- Hundreds of chart variations available
- Based on G2Plot with all G2Plot configurations inherited
- Good visual and interactive experience

### Technical Details

- **Rendering**: SVG/Canvas (G2/G6 based)
- **Bundle Size**: Split packages for on-demand importing
  - Statistical charts: `charts.min.js`
  - Graph charts: `charts_g6.min.js`
- **TypeScript**: Full support with type definitions
- **Framework Compatibility**:
  - React 16-18: ✅ Full support
  - React 19: ⚠️ Most features compatible
  - Next.js: ⚠️ Compatible (some configuration needed)

### Technology Stack

Built on AntV visualization libraries:
- **G2Plot**: Statistical charts
- **G6**: Relational/graph analysis
- **X6**: Flow diagrams
- **L7**: Geographic visualization

### Pros

✅ Comprehensive chart type coverage (27+ types)
✅ Enterprise-ready (used by Alibaba Cloud, Alipay, Tmall, Taobao, JD.com)
✅ Strong backing from AntV team
✅ Excellent for both statistical and relational data
✅ Rich feature set out of the box
✅ Good documentation with examples
✅ Free and open source
✅ TypeScript support
✅ Responsive design

### Cons

❌ Bundle size can be large if not using on-demand imports
❌ Learning curve for advanced features
❌ Some Next.js configuration challenges reported
❌ Documentation primarily focused on G2Plot API

### Best For

- Enterprise dashboards
- Complex data visualization (statistical + relational)
- Geographic visualizations
- Projects using Ant Design UI
- Applications requiring diverse chart types

### Maintenance Status

🟢 **Actively Maintained** - Latest version published 14-21 days ago (October 2025), ~2.1k GitHub stars

---

## 4. Recharts

### Overview

- **Version**: 3.2.1
- **License**: MIT (Free and Open Source)
- **Documentation**: https://recharts.org/
- **Technology**: "Redefined chart library built with React and D3"
- **Popularity**: Most popular React charting library

### Installation

```bash
npm install recharts
```

### Chart Types Supported (10+)

- Line Charts, Bar Charts, Area Charts
- Pie Charts, Scatter Charts, Radar Charts
- Composed Charts, Treemap, Sankey, Funnel
- Radial Bar Charts

### Key Features

- Simply deploy with React components
- Native SVG support
- Lightweight with minimal D3 dependencies
- Declarative components
- Responsive design via `ResponsiveContainer`
- Smooth animations (customizable)
- Beautiful charts out of the box
- Highly customizable through props
- Excellent tooltip system
- Support for reference lines/areas
- Brushes for zooming
- Custom shapes and labels

### Technical Details

- **Rendering**: SVG-based
- **Bundle Size**: 139 kB (Minified + Gzipped)
- **Dependencies**: 11 (modular D3 submodules only)
- **TypeScript**: Support available but some typing issues reported
- **Framework Compatibility**:
  - React 16-18: ✅ Full support
  - Next.js: ⚠️ Compatible (ResponsiveContainer has SSR limitations)
  - Mobile: ✅ Good support

### Performance

- Suitable for small to medium datasets
- SVG-based, not optimal for 10,000+ data points
- Below 1,000 points: excellent performance
- Smooth animations
- Mobile-friendly

### Accessibility

⚠️ Work in progress toward WCAG 2.2 AA compliance
- Tooltip areas are live regions for screen readers
- Keyboard navigation partially implemented (inconsistent across chart types)
- AreaChart supports focus and arrow key navigation
- Some chart types (FunnelChart, vertical layouts) lack keyboard support

### Community & Popularity

- **GitHub Stars**: 24,800-26,041 ⭐
- **npm Downloads**: 7.9M-10M weekly 📦
- **Dependents**: 781K+ repositories
- Strong community support
- Excellent documentation
- Active maintainers

### Pros

✅ Consistently praised for simplicity and ease of use
✅ Clean SVG rendering
✅ Strong community support (largest among React chart libraries)
✅ Most popular choice (millions of weekly downloads)
✅ Framework-agnostic (works with any React setup)
✅ Free and open source
✅ Good documentation
✅ Modular and composable
✅ Declarative, React-friendly approach
✅ Less code needed for basic charts
✅ Responsive out of the box

### Cons

❌ TypeScript typing issues (inherited from D3)
❌ Not optimal for very large datasets (10,000+ points)
❌ Accessibility not fully WCAG compliant yet
❌ ResponsiveContainer doesn't work well with SSR
❌ Less opinionated about design (requires more styling decisions)
❌ Animations can be inconsistent across chart types

### Best For

- Dashboards with small to medium datasets
- Projects needing maximum flexibility
- Applications not committed to a specific UI framework
- Line, bar, pie, area charts with standard requirements
- Projects prioritizing community support and documentation

### Maintenance Status

🟢 **Actively Maintained** - Latest version published 1 month ago (September 2025), millions of weekly downloads

---

## Performance Comparison: SVG vs Canvas

### SVG-based (Recharts, Mantine, MUI X Community)
- **Best for**: <1,000 data points
- **Advantages**: CSS styling, DOM manipulation, smooth animations, easy interactivity
- **Limitations**: Performance degrades with large datasets

### Canvas-based (Ant Design's G2 option)
- **Best for**: 10,000+ data points
- **Advantages**: 10x faster rendering, uses less memory
- **Limitations**: Harder to style, less interactive by default

---

## Detailed Feature Comparison

| Feature | Mantine Charts | MUI X Charts | Ant Design Charts | Recharts |
|---------|---------------|--------------|-------------------|----------|
| **License** | MIT | MIT / Commercial | Open Source | MIT |
| **Latest Version** | 8.3.1 | v8 | 2.6.5 | 3.2.1 |
| **Chart Types** | 12+ | 10+ (Free), 12+ (Pro) | 27+ | 10+ |
| **Technology** | React + Recharts | React + Custom | React + G2/G6 | React + D3 |
| **Rendering** | SVG | SVG | SVG/Canvas | SVG |
| **Bundle Size** | ~1.53 MB (174kB gzip) | Medium | Split packages | 139 kB gzip |
| **TypeScript** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Mixed |
| **React 18** | ✅ | ✅ | ✅ | ✅ |
| **React 19** | ✅ | ✅ | ⚠️ | ✅ |
| **Next.js** | ✅ | ✅ | ⚠️ | ⚠️ |
| **SSR Support** | ✅ | ✅ (v8+) | ✅ | ⚠️ Limited |
| **GitHub Stars** | ~25K (Mantine) | ~4K (MUI X) | ~2.1K | 24.8K-26K |
| **npm Downloads** | Low | Medium | Medium | 7.9M-10M weekly |
| **Accessibility** | Via Recharts | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Standard | ⚠️ WIP |
| **Animations** | Disabled by default | ✅ Custom engine | ✅ | ✅ Customizable |
| **Pricing** | Free | Free / Paid Pro | Free | Free |
| **Documentation** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## Recommendations by Use Case

### By UI Framework
- **Already using Mantine UI** → **Mantine Charts**
- **Already using Material UI** → **MUI X Charts**
- **Already using Ant Design** → **Ant Design Charts**
- **Framework-agnostic** → **Recharts**

### By Project Type
- **Enterprise with complex data needs** → **Ant Design Charts** or **MUI X Pro**
- **Startup/MVP requiring fast setup** → **Mantine Charts** or **Recharts**
- **Maximum flexibility/popularity** → **Recharts**
- **Large datasets (10,000+ points)** → **Ant Design Charts** (Canvas mode)

### By Technical Requirements
- **Best accessibility** → **MUI X Charts**
- **Best TypeScript experience** → **Mantine Charts** or **MUI X Charts**
- **Best documentation** → **Recharts** or **Mantine Charts**
- **Best free option with most features** → **Recharts** or **Ant Design Charts**
- **SSR/SEO critical** → **MUI X Charts v8** or **Mantine Charts**
- **Next.js App Router** → **Mantine Charts** or **MUI X Charts**

### By Team Size
- **Small teams (<5 developers)** → **Recharts** or **Mantine Charts**
- **Medium teams (5-20 developers)** → Any option based on UI framework
- **Large teams (20+ developers)** → Consider MUI X Pro licensing costs vs open-source alternatives

---

## Integration Notes

### Mantine + Recharts
Mantine includes a first-party package, `@mantine/charts`, introduced in version 8.0 and fully supporting Recharts v2 and v3. This provides the best of both worlds: Recharts' proven charting engine with Mantine's design system integration.

### MUI X Charts
MUI has its own charting library built in with MUI X Charts, offering both free (MIT) and commercial (Pro) versions. The v8 release added critical SSR support and React 19 compatibility.

### Ant Design Charts
AntDesign has Ant Design Charts built on top of the powerful AntV visualization ecosystem (G2, G6, X6, L7), providing the most comprehensive chart type coverage (27+) of all options reviewed.

---

## Conclusion

Each library excels in different scenarios:

- **Choose Mantine Charts** for seamless Mantine UI integration with minimal setup
- **Choose MUI X Charts** for Material Design projects requiring enterprise support
- **Choose Ant Design Charts** for maximum chart variety and complex visualizations
- **Choose Recharts** for maximum community support, flexibility, and framework independence

All four libraries are production-ready and actively maintained as of October 2025. The best choice depends on your existing tech stack, specific chart requirements, team size, and budget constraints.

---

*Last Updated: October 16, 2025*
*Research Sources: Official documentation, npm registry, GitHub repositories, community reviews*
