# Map Visualization

- Source PDF: `15. Map visualization.pdf`
- Pages/slides: 33
- Extraction style: cleaned knowledge notes by slide/page, not a raw transcript.
- Visual caveat: image-heavy examples may need the original PDF for exact graphical details.

## Deck-Level Focus

Introduces map-based visualization, spatial data, geocoding, projection, and map encodings.

## Core Knowledge

- Map visualization is appropriate when location is part of the analytical question.
- Spatial encoding depends on projection, geographic granularity, and geocoding quality.
- Choropleth maps encode area-level values but can mislead when population denominators differ.
- Point maps and symbol maps require attention to overlap and scale.

## How This Supports the Churn Report

- This deck is mostly out of scope unless the churn dataset is enriched with geographic features.
- If geography is added, normalize churn metrics by customer counts before mapping.

## Slide-by-Slide Extraction

### Slide 001: Slide 1

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Slide 1.

### Slide 002: Map data visualization

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 2

### Slide 003: Map data

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Map is a special form of spatial data
  - Visualization goals
  - Finding locations
  - Finding the paths
  - Finding attributes
  - Comparison
  - 3

### Slide 004: Projection

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Earth is spherical
  - Presentation medium: computer screen, paper
  - 4

### Slide 005: Mercator projection

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Geradus Mercater, 1569
  - Project the globe on a tube
  - Relatively accurate for the part near the equator
  - Distortion for regions far from the equator
  - 5

### Slide 006: Example: Mercator projection of the world

- Type: Example / critique
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 6

### Slide 007: Example: Interrupted Goode homolosine projection of the world

- Type: Example / critique
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 7

### Slide 008: Azimuthal projection

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - A map projection in which a globe, as of the
  - Earth, is assumed to rest on a flat surface onto
  - which its features are projected
  - 8

### Slide 009: Winkel Tripel projection

- Type: Concept / application
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - a modified azimuthal map projection
  - minimizing three kinds of distortion: area, direction, and distance
  - 9

### Slide 010: Lambert conformal conic projection

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - The projection seats a cone over the sphere of
  - the Earth and projects the surface conformally onto the cone
  - 10

### Slide 011: D3

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - https://github.com/d3/d3-geo-projection/
  - 11

### Slide 012: Map libs

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 12

### Slide 013: Display information on a map

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 13

### Slide 014: Choropleth maps (bản đồ vùng)

- Type: Concept / application
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Areas on the map are colored or drawn to
  - represent information of interest in the area
  - 14

### Slide 015: Example: Median income in every US county, shown as a choropleth map

- Type: Example / critique
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 15

### Slide 016: Example: Median income in every US state, shown as a choropleth map

- Type: Example / critique
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - 16

### Slide 017: Example: Median income in every US state, shown as a cartogram

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 17

### Slide 018: Cartogram

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Map attribute values to regions of the map
  - Areas of the map can be transformed according
  - to the value to emphasize the meaning of the value
  - Map of Germany, regions distorted by population
  - 18

### Slide 019: Cartogram

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 19

### Slide 020: Cartogram

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 20

### Slide 021: Cartogram

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 21

### Slide 022: Cartogram

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 22

### Slide 023: Cartogram

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 23

### Slide 024: Example: Median income in every US state, shown as a cartogram heatmap

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 24

### Slide 025: Contour map (bản đồ đường đẳng mức)

- Type: Concept / application
- Application note: Use layout and highlighting to guide attention before the user reads details.
- Knowledge extracted:
  - Show the degree of similarity in the values of
  - locations on the map through isometric lines
  - 25

### Slide 026: Contour map

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Halley's 1701 map showing isogonic lines of equal magnetic declination in the
  - Atlantic Ocean.
  - 26

### Slide 027: Contour map

- Type: Concept / application
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Halley map of the trade winds (1686)
  - 27

### Slide 028: Example: a Contour Density Map from Choropleth Map

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - https://observablehq.com/@efrymire/griddingmap-files
  - 28

### Slide 029: Flow map (bản đồ luồng)

- Type: Example / critique
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - Combination of map and flow graph to
  - represent the flow of objects from one location
  - to another on the map (eg. Migration, exchange of goods, ...)
  - 29

### Slide 030: Minard 1869: Napoleon’s march

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 30

### Slide 031: Beck’s London tube diagram

- Type: Concept / definition
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - London Underground [Beck 33]
  - Geographic version of map
  - Principle: Straighten lines to emphasize stop sequence
  - 31

### Slide 032: https://observablehq.com/@uwdata/cartograp hic-visualization

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 32

### Slide 033: 33

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: 33.
