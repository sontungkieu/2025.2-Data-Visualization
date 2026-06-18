# Visualization for Graphs

- Source PDF: `14. Visualization for graphs.pdf`
- Pages/slides: 28
- Extraction style: cleaned knowledge notes by slide/page, not a raw transcript.
- Visual caveat: image-heavy examples may need the original PDF for exact graphical details.

## Deck-Level Focus

Introduces graph data, node-link and matrix representations, and layout choices for relationships.

## Core Knowledge

- Graph visualization is for data with entities and explicit relationships or edges.
- Node-link diagrams emphasize paths and structure but can become cluttered.
- Matrix representations scale better for dense graphs but can be less intuitive.
- Layout choice communicates assumptions about hierarchy, force, or adjacency.

## How This Supports the Churn Report

- This deck is mostly out of scope for the churn dataset unless relationship data is added.
- State non-applicability in the report rather than forcing an irrelevant graph visualization.

## Slide-by-Slide Extraction

### Slide 001: Slide 1

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Slide 1.

### Slide 002: Graph data visualization

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - 2

### Slide 003: What is graph data

- Type: Concept / definition
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Data representing relationships between entities
  - Entities are represented by nodes (vertices or points)
  - Relationships are represented by edges (lines or arcs)
  - The graph G(V,E) includes the set of vertices V and the set of edges E
  - 4

### Slide 004: Properties of Graph Data

- Type: Concept / definition
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Sparsity
  - Not all nodes are connected by edges
  - Number of edges is often much less than the number of
  - possible connections between nodes
  - Directionality
  - Directed edges: Show a one-way relationship between
  - nodes (e.g., following on Twitter)
  - Undirected edges: Show a two-way relationship
  - between nodes (e.g., friendship on Facebook)
  - Weights
  - Weights represent the strength or importance of the
  - relationship between nodes
  - Additional minor points omitted in this note: 2. Reopen the PDF for full slide text.

### Slide 005: Basic concepts

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - An independent set, stable set, coclique or anticlique is a set of
  - vertices in a graph, no two of which are adjacent.
  - Clique is a subset of vertices of an undirected graph such that
  - every two distinct vertices in the clique are adjacent.
  - A graph is said to be connected if every pair of vertices in the graph is connected.
  - A tree is an undirected graph in which any two vertices are
  - connected by exactly one path, or equivalently a connected acyclic undirected graph.

### Slide 006: Basic concepts

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - An articulation point (or cut vertex) (Điểm khớp) is defined as a
  - vertex which, when removed along with associated edges, makes the graph disconnected
  - A biconnected graph (đồ thị nối đôi) is a connected and
  - "nonseparable" graph, meaning that if any one vertex were to be
  - removed, the graph will remain connected.
  - A biconnected graph has no articulation vertices.
  - A bipartite graph (or bigraph) (đồ thị hai phần) is a graph whose
  - vertices can be divided into two disjoint and independent sets U
  - and V such that every edge connects a vertex in U to one in V

### Slide 007: Basic concepts

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Degree (bậc) of a vectex
  - deg(n) is the number of edges that are incident to the vertex
  - Graph diameter (đường kính)
  - diam(G) is the greatest distance (shortest parh)
  - between any pair of vertices

### Slide 008: Graph visualization

- Type: Section divider / visual-only slide
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Introduces or visually illustrates: Graph visualization.

### Slide 009: Explicit graph visualization (node-link)

- Type: Section divider / visual-only slide
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Introduces or visually illustrates: Explicit graph visualization (node-link).

### Slide 010: Criteria for node-link representation

- Type: Concept / application
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Minimizing the intersection edges
  - Minimize the distance between the vertices
  - Minimize drawing area
  - Edges of similar length
  - Maximum angle between different edges
  - Symmetry (graphs with the same structure must look the same)

### Slide 011: Force-directed graph

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - The forces are applied to the nodes, pulling them closer together
  - or pushing them further apart.
  - This is repeated iteratively until the system comes to a mechanical equilibrium state
  - https://observablehq.com/@d3/force-directed-graph

### Slide 012: Multi-level technique

- Type: Concept / definition
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Reduce the magnitude of a graph by merging
  - vertices together, compute a partition on this
  - reduced graph, and finally project this partition on the original graph.

### Slide 013: Sampling

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Large graphs can overwhelm visualization tools and viewers.
  - Sampling allows us to explore a manageable subset of the data.
  - Different sampling techniques highlight various aspects of the graph.
  - Key sampling techniques
  - Random Sampling
  - Degree-Based Sampling
  - Ego-Network Sampling
  - Community Sampling

### Slide 014: Collapse/Expand

- Type: Concept / application
- Application note: Choose the visualization family from the data structure: table, time, spatial, hierarchy, or network.
- Knowledge extracted:
  - Particularly useful for hierarchical graphs, where subtrees can be collapsed or expanded as
    needed.
  - Clarity: Reduces visual clutter, making it easier to focus
  - on specific areas of interest.
  - Scalability: Handles large datasets efficiently by
  - allowing parts of the graph to be hidden.
  - http://bl.ocks.org/mbostock/1062288

### Slide 015: Fixed arrangement for graphs

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Circos Layout
  - Compact Visualization: Efficiently uses space to show large, complex datasets.
  - Pattern Recognition: Facilitates the identification of clusters,
  - patterns, and relationships.
  - Aesthetic Appeal: Attractive and engaging, enhancing the visual storytelling of data.

### Slide 016: Fixed arrangement for graphs

- Type: Section divider / visual-only slide
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Introduces or visually illustrates: Fixed arrangement for graphs.

### Slide 017: Fixed arrangement for graphs

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Edge bundling
  - https://observablehq.com/@d3/hierarchical-edge-bundling

### Slide 018: Tree layout

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - https://observablehq.com/@d3/tree

### Slide 019: Tree layout

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - http://bl.ocks.org/mbostock/4339083

### Slide 020: Adjacency matrix

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Adjacency matrix.

### Slide 021: Adjacency matrix

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Adjacency matrix.

### Slide 022: Adjacency matrix

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Advantage
  - Can represent most graphs (except hypergraphs)
  - Focus on edges instead of vertices
  - No need to care about layout
  - Disadvantage
  - Difficult to detect relationships such as paths, cycles, etc.

### Slide 023: Hybrid layout

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Hybrid layout.

### Slide 024: Implicit presentation

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - A treemap chart is a visualization that displays hierarchical data
  - using nested rectangles.
  - Structure
  - The entire chart area represents the root of the hierarchy.
  - Each rectangle (or cell) represents a branch or leaf node.
  - Rectangles are sized and ordered by a quantitative variable.
  - Colors can be used to represent different categories or to encode additional data
    dimensions.
  - http://www.nytimes.com/packages/html/ne
  - wsgraphics/2011/0119-budget/

### Slide 025: 27

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: 27.

### Slide 026: Implicit presentation

- Type: Concept / definition
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - A sunburst chart is a radial visualization that represents
  - hierarchical data using concentric circles.
  - Structure
  - The center circle represents the root of the hierarchy.
  - Each subsequent ring represents a level in the hierarchy.
  - Slices are divided into segments representing subcategories.
  - Interactive Exploration: Often allows users to zoom in on segments for detailed views.
  - https://observablehq.com/@d3/sunburst
  - https://observablehq.com/@d3/zoomable-sunburst

### Slide 027: https://observablehq.com/@3cd7d5ec89dc7f6

- Type: Concept / application
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - 8/graph-visualization-introduction
  - 29

### Slide 028: 30

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: 30.
