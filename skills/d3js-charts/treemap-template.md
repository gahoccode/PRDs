# Treemap Template

Complete, copy-paste-ready hierarchical treemap with tooltips, labels, and interactive features.

## Data Format

```typescript
interface TreeNode {
  name: string;
  value?: number;        // Leaf nodes have value
  children?: TreeNode[]; // Parent nodes have children array
}

// Example hierarchical data:
const data: TreeNode = {
  name: 'root',
  children: [
    {
      name: 'Technology',
      children: [
        { name: 'Apple', value: 3000 },
        { name: 'Microsoft', value: 2500 },
        { name: 'Google', value: 2000 },
      ],
    },
    {
      name: 'Finance',
      children: [
        { name: 'JPMorgan', value: 1500 },
        { name: 'Goldman', value: 1200 },
      ],
    },
    {
      name: 'Healthcare',
      children: [
        { name: 'Johnson & Johnson', value: 1800 },
        { name: 'Pfizer', value: 1400 },
      ],
    },
  ],
};
```

## Full Implementation

```typescript
import * as d3 from 'd3';

// === CONFIGURATION ===
interface TreemapConfig {
  width: number;
  height: number;
  padding: number;
  tile: (node: d3.HierarchyRectangularNode<TreeNode>, x0: number, y0: number, x1: number, y1: number) => void;
  cornerRadius: number;
  showLabels: boolean;
  showValues: boolean;
  formatValue: (n: number) => string;
  colorScheme: 'custom' | 'tableau10' | 'category10' | 'set1' | 'set2';
}

const defaultConfig: TreemapConfig = {
  width: 800,
  height: 600,
  padding: 1,
  tile: d3.treemapSquarify,
  cornerRadius: 2,
  showLabels: true,
  showValues: true,
  formatValue: d3.format(',d'),
  colorScheme: 'custom',
};

// === CUSTOM COLOR PALETTE ===
const CATEGORICAL_COLORS = [
  '#204F80',  // Deep blue
  '#804F1F',  // Warm brown
  '#0A2845',  // Navy
  '#426F99',  // Steel blue
  '#45280A',  // Dark brown
  '#996F42',  // Tan
  '#FF6B6B',  // Coral
  '#4ECDC4',  // Teal
  '#45B7D1',  // Sky blue
  '#96CEB4',  // Sage green
];

// === THEME COLORS ===
function getThemeColors() {
  const isDark = document.documentElement.classList.contains('dark');
  return {
    background: isDark ? '#0E1117' : '#FFFFFF',
    text: isDark ? '#FAFAFA' : '#1F1916',
    subText: isDark ? '#E5E7EB' : '#56524D',
    tooltipBg: isDark ? '#262730' : '#FFFFFF',
    tooltipBorder: isDark ? '#4B5563' : '#333333',
  };
}

// === COLOR SCHEMES ===
function getColorScheme(scheme: TreemapConfig['colorScheme']): readonly string[] {
  switch (scheme) {
    case 'custom':
      return CATEGORICAL_COLORS;
    case 'tableau10':
      return d3.schemeTableau10;
    case 'category10':
      return d3.schemeCategory10;
    case 'set1':
      return d3.schemeSet1;
    case 'set2':
      return d3.schemeSet2;
    default:
      return CATEGORICAL_COLORS;
  }
}

// === TILING ALGORITHMS ===
const tilingAlgorithms = {
  squarify: d3.treemapSquarify,       // Default, balanced aspect ratios
  binary: d3.treemapBinary,           // Horizontal/vertical alternating
  slice: d3.treemapSlice,             // Horizontal slices
  dice: d3.treemapDice,               // Vertical slices
  sliceDice: d3.treemapSliceDice,     // Alternating by depth
};

// === MAIN RENDER FUNCTION ===
export function renderTreemap(
  container: string,
  data: TreeNode,
  config: Partial<TreemapConfig> = {}
) {
  const cfg = { ...defaultConfig, ...config };
  const { width, height, padding, tile, cornerRadius, showLabels, showValues, formatValue, colorScheme } = cfg;
  const colors = getThemeColors();

  // Clear container
  const containerEl = document.querySelector(container);
  if (!containerEl) return;
  containerEl.innerHTML = '';

  // Create hierarchy and compute layout
  const root = d3.treemap<TreeNode>()
    .tile(tile)
    .size([width, height])
    .padding(padding)
    .round(true)
  (
    d3.hierarchy(data)
      .sum(d => d.value || 0)
      .sort((a, b) => (b.value || 0) - (a.value || 0))
  );

  // Color scale by top-level parent
  const topLevelNames = data.children?.map(d => d.name) || [];
  const color = d3.scaleOrdinal<string>()
    .domain(topLevelNames)
    .range(getColorScheme(colorScheme));

  // Helper: get top-level parent for coloring
  function getTopParent(d: d3.HierarchyRectangularNode<TreeNode>): d3.HierarchyRectangularNode<TreeNode> {
    let node = d;
    while (node.depth > 1 && node.parent) {
      node = node.parent;
    }
    return node;
  }

  // Create SVG
  const svg = d3.select(container)
    .append('svg')
    .attr('viewBox', [0, 0, width, height])
    .attr('width', width)
    .attr('height', height)
    .style('max-width', '100%')
    .style('height', 'auto')
    .style('font', '10px sans-serif')
    .style('background', colors.background);

  // === TOOLTIP (HTML) ===
  const tooltip = d3.select(container)
    .append('div')
    .attr('class', 'treemap-tooltip')
    .style('opacity', 0)
    .style('position', 'absolute')
    .style('background-color', colors.tooltipBg)
    .style('border', `2px solid ${colors.tooltipBorder}`)
    .style('border-radius', '5px')
    .style('padding', '10px')
    .style('font-size', '12px')
    .style('pointer-events', 'none')
    .style('z-index', '1000')
    .style('color', colors.text);

  // === LEAF GROUPS ===
  const leaf = svg.selectAll<SVGGElement, d3.HierarchyRectangularNode<TreeNode>>('g.leaf')
    .data(root.leaves())
    .join('g')
    .attr('class', 'leaf')
    .attr('transform', d => `translate(${d.x0}, ${d.y0})`);

  // === RECTANGLES ===
  leaf.append('rect')
    .attr('id', (_, i) => `leaf-rect-${i}`)
    .attr('fill', d => color(getTopParent(d).data.name))
    .attr('fill-opacity', 0.7)
    .attr('width', d => Math.max(0, d.x1 - d.x0))
    .attr('height', d => Math.max(0, d.y1 - d.y0))
    .attr('rx', cornerRadius)
    .attr('ry', cornerRadius)
    .style('cursor', 'pointer')
    .on('mouseenter', function(event, d) {
      d3.select(this).attr('fill-opacity', 1);
      
      const path = d.ancestors().reverse().map(n => n.data.name).join(' → ');
      tooltip
        .style('opacity', 1)
        .html(`
          <strong>${d.data.name}</strong><br/>
          <span style="color: ${colors.subText}">${path}</span><br/>
          Value: <strong>${formatValue(d.value || 0)}</strong>
        `);
    })
    .on('mousemove', function(event) {
      tooltip
        .style('left', `${event.pageX + 15}px`)
        .style('top', `${event.pageY - 10}px`);
    })
    .on('mouseleave', function() {
      d3.select(this).attr('fill-opacity', 0.7);
      tooltip.style('opacity', 0);
    });

  // === CLIP PATHS ===
  leaf.append('clipPath')
    .attr('id', (_, i) => `clip-${i}`)
    .append('rect')
    .attr('width', d => Math.max(0, d.x1 - d.x0))
    .attr('height', d => Math.max(0, d.y1 - d.y0));

  // === LABELS ===
  if (showLabels) {
    leaf.append('text')
      .attr('clip-path', (_, i) => `url(#clip-${i})`)
      .attr('fill', colors.text)
      .selectAll('tspan')
      .data(d => {
        const cellWidth = d.x1 - d.x0;
        const cellHeight = d.y1 - d.y0;
        
        // Skip labels for very small cells
        if (cellWidth < 30 || cellHeight < 20) return [];
        
        // Split name on camelCase, spaces, or hyphens
        const nameParts = d.data.name.split(/(?=[A-Z][a-z])|\s+|-/g).filter(Boolean);
        
        // Add value if space permits and showValues is true
        if (showValues && cellHeight > 35) {
          return [...nameParts, formatValue(d.value || 0)];
        }
        return nameParts;
      })
      .join('tspan')
      .attr('x', 4)
      .attr('y', (_, i, nodes) => {
        const isValue = i === nodes.length - 1 && showValues;
        return `${(isValue ? 0.3 : 0) + 1.1 + i * 0.9}em`;
      })
      .attr('fill-opacity', (_, i, nodes) => i === nodes.length - 1 && showValues ? 0.7 : 1)
      .style('font-size', '10px')
      .style('font-weight', (_, i) => i === 0 ? '600' : '400')
      .text(d => d);
  }

  // === SVG TITLE (for native tooltips as fallback) ===
  leaf.append('title')
    .text(d => `${d.ancestors().reverse().map(n => n.data.name).join(' → ')}\n${formatValue(d.value || 0)}`);

  // Return reference for updates
  return {
    svg: svg.node(),
    update: (newData: TreeNode) => {
      // Re-render with new data
      renderTreemap(container, newData, config);
    },
    color,
  };
}
```

## Usage Example

```typescript
// Hierarchical data
const data: TreeNode = {
  name: 'Portfolio',
  children: [
    {
      name: 'Stocks',
      children: [
        { name: 'AAPL', value: 15000 },
        { name: 'MSFT', value: 12000 },
        { name: 'GOOGL', value: 10000 },
      ],
    },
    {
      name: 'Bonds',
      children: [
        { name: 'Treasury', value: 8000 },
        { name: 'Corporate', value: 5000 },
      ],
    },
    {
      name: 'Real Estate',
      children: [
        { name: 'REITs', value: 7000 },
      ],
    },
  ],
};

// Render
const treemap = renderTreemap('#chart', data, {
  width: 900,
  height: 600,
  colorScheme: 'custom',
  formatValue: d3.format('$,.0f'),
});
```

## Tiling Algorithms

```typescript
// Squarify (default) - balanced aspect ratios, best for most cases
tile: d3.treemapSquarify

// Binary - alternating horizontal/vertical splits
tile: d3.treemapBinary

// Slice - horizontal slices only
tile: d3.treemapSlice

// Dice - vertical slices only
tile: d3.treemapDice

// Slice-Dice - alternates by depth level
tile: d3.treemapSliceDice

// Resquarify - maintains order during updates (for animations)
tile: d3.treemapResquarify
```

## Animated Treemap Updates

```typescript
function animateTreemapUpdate(
  svg: d3.Selection<SVGSVGElement, unknown, null, undefined>,
  newRoot: d3.HierarchyRectangularNode<TreeNode>,
  duration: number = 750
) {
  const leaf = svg.selectAll<SVGGElement, d3.HierarchyRectangularNode<TreeNode>>('g.leaf')
    .data(newRoot.leaves(), d => d.data.name);  // Key by name

  // Update existing
  leaf.transition().duration(duration)
    .attr('transform', d => `translate(${d.x0}, ${d.y0})`);

  leaf.select('rect')
    .transition().duration(duration)
    .attr('width', d => d.x1 - d.x0)
    .attr('height', d => d.y1 - d.y0);

  // Enter new
  const entering = leaf.enter().append('g')
    .attr('class', 'leaf')
    .attr('transform', d => `translate(${d.x0}, ${d.y0})`)
    .style('opacity', 0);

  entering.append('rect')
    .attr('fill', d => color(getTopParent(d).data.name))
    .attr('width', d => d.x1 - d.x0)
    .attr('height', d => d.y1 - d.y0);

  entering.transition().duration(duration)
    .style('opacity', 1);

  // Exit old
  leaf.exit()
    .transition().duration(duration)
    .style('opacity', 0)
    .remove();
}
```

## Zoomable Treemap

```typescript
// Click to zoom into a branch
let currentRoot = root;

function zoom(event: MouseEvent, d: d3.HierarchyRectangularNode<TreeNode>) {
  // Re-layout from clicked node as root
  const newRoot = d3.treemap<TreeNode>()
    .tile(d3.treemapSquarify)
    .size([width, height])
    .padding(1)
  (
    d3.hierarchy(d.data)
      .sum(n => n.value || 0)
      .sort((a, b) => (b.value || 0) - (a.value || 0))
  );

  currentRoot = newRoot;
  animateTreemapUpdate(svg, newRoot);
}

// Add breadcrumb for navigation back
function addBreadcrumb(path: TreeNode[]) {
  const breadcrumb = svg.append('g')
    .attr('class', 'breadcrumb')
    .attr('transform', 'translate(10, -20)');

  breadcrumb.selectAll('text')
    .data(path)
    .join('text')
    .attr('x', (_, i) => i * 100)
    .text(d => d.name)
    .style('cursor', 'pointer')
    .on('click', (_, d) => zoom(null, findNode(root, d.name)));
}
```

## Key Patterns

| Feature | Implementation |
|---------|----------------|
| Layout | `d3.treemap().tile().size().padding()` |
| Hierarchy | `d3.hierarchy(data).sum().sort()` |
| Color by parent | Walk up tree with `while (node.depth > 1)` |
| Clip text | `<clipPath>` + `clip-path` attribute |
| Multi-line labels | `tspan` elements with calculated `y` |
| Value formatting | `d3.format(',d')` or custom |

## Flat Data to Hierarchy

```typescript
// Convert flat data with path strings to hierarchy
interface FlatItem {
  path: string;  // e.g., "Technology/Software/Microsoft"
  value: number;
}

function buildHierarchy(flatData: FlatItem[]): TreeNode {
  const root: TreeNode = { name: 'root', children: [] };

  flatData.forEach(item => {
    const parts = item.path.split('/');
    let current = root;

    parts.forEach((part, i) => {
      if (!current.children) current.children = [];
      
      let child = current.children.find(c => c.name === part);
      if (!child) {
        child = { name: part };
        current.children.push(child);
      }

      if (i === parts.length - 1) {
        child.value = item.value;
      }
      current = child;
    });
  });

  return root;
}
```

## Accessibility

```typescript
// ARIA labels for screen readers
leaf.append('rect')
  .attr('role', 'img')
  .attr('aria-label', d => 
    `${d.data.name}: ${formatValue(d.value || 0)}. ` +
    `Part of ${getTopParent(d).data.name}.`
  );

// Keyboard navigation
leaf
  .attr('tabindex', 0)
  .on('keydown', (event, d) => {
    if (event.key === 'Enter' || event.key === ' ') {
      zoom(event, d);
    }
  });
```
