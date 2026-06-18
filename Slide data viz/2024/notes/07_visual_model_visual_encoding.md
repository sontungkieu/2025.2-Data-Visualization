# Visual Model and Visual Encoding

- Source PDF: `7. Visual model & Visual Encoding.pdf`
- Pages/slides: 59
- Extraction style: cleaned knowledge notes by slide/page, not a raw transcript.
- Visual caveat: image-heavy examples may need the original PDF for exact graphical details.

## Deck-Level Focus

Explains data types, visual marks, perceptual channels, and the mapping from data attributes to images.

## Core Knowledge

- Classify variables by measurement level: nominal, ordinal, interval, and ratio.
- Choose visual marks such as points, lines, and areas according to the items or relationships
    being represented.
- Use visual channels such as position, length, size, color, shape, orientation, and value to
    encode attributes.
- Effective encodings are both expressive and easy for people to decode.
- Avoid over-encoding when one or two channels communicate the message clearly.

## How This Supports the Churn Report

- Map churn status to color hue, counts/rates to bar length or position, and ordered groups to
    ordered axes.
- Document why each churn feature uses a particular chart and encoding.

## Slide-by-Slide Extraction

### Slide 001: Visual Model & Visual Encoding

- Type: Section divider / visual-only slide
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Introduces or visually illustrates: Visual Model & Visual Encoding.

### Slide 002: Goal

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Learn how data is mapped to images

### Slide 003: The big picture

- Type: Concept / definition
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Domain goals, questions, assumptions
  - Data conceptual model data model
  - Analysis task identify, compare summarize
  - Processing algorithms data transformation
  - Image marks & channels
  - Visual encoding
  - mapping from data to image
  - [Slides from J. Heer]

### Slide 004: Topics

- Type: Roadmap
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Properties of Data
  - Properties of Images
  - Visual encoding: Mapping Data to Images

### Slide 005: Properties of data

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Properties of data.

### Slide 006: Taxonomy of datasets

- Type: Concept / definition
- Application note: Choose the visualization family from the data structure: table, time, spatial, hierarchy, or network.
- Knowledge extracted:
  - 1D (sets and sequences)
  - Temporal
  - 2D (maps) 3D
  - (shapes) nD
  - (relational)
  - Trees (hierarchies)
  - Networks (graphs) and combinations…

### Slide 007: Data types: Levels of measurement

- Type: Concept / definition
- Application note: First classify each variable by measurement level; this determines valid statistics and chart encodings.
- Knowledge extracted:
  - Stevens (1946) classified variables into four
  - levels. These are referered to as levels of
  - measurement, or levels of data.
  - N - Nominal
  - O - Ordinal
  - Q – Quantitative
  - Interval
  - Ratio

### Slide 008: Nominal level measurement

- Type: Example / critique
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Merely classifies units into non-ordered categories
  - Distinct groups with no inherent order.
  - Examples: Colors, types of animals, gender.
  - No quantitative value
  - Values represent categories, but no mathematical
  - operations are meaningful.
  - Examples
  - Male/Female
  - Eye colors
  - Car models

### Slide 009: Ordinal level measurement

- Type: Example / critique
- Application note: For ordinal data, preserve the natural order on the axis or legend.
- Knowledge extracted:
  - Classifies units into ranks or ordered categories
  - Examples
  - Ranks: 1st, 2nd, 3rd... place finishers in race
  - Ordered categories: {none = 0, low=1, medium=2, high=3}
  - Relative differences
  - Can determine that one value is greater or lesser,
  - but the intervals are not consistent.

### Slide 010: Interval level measurement

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Distances (absolute differences) are meaningful
  - any arithmetic operation, such as multiplication, is not
  - A fixed difference anywhere on the measurement scale
  - always corresponds to the same difference on the trait being measured
  - The zero state of an interval scale is not a true zero value
  - A temperature reading of 0°C does not mean there is no temperature
  - Examples
  - Temperature oF
  - A one-degree temperature (°F) difference always means the same thing
  - The absolute difference between 60°F and 61°F is the same as between 100°F and 101°F

### Slide 011: Ratio level measurement

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Both differences and ratios are meaningful
  - There is a true zero
  - A zero on a ratio scale means there is a total absence of
  - the variable you are measuring.
  - Examples
  - Length, area, and population
  - The relative difference between a 10 and a 20-year-old
  - is the same as the difference between a 40- and an 80year-old (‘twice as old’).
  - Celsius and Fahrenheit are interval scales, Kelvin is a ratio scale
  - Kelvin scale has a true zero (0 K) where nothing can be colder.
  - Zero is just another temperature value in Celsius and
  - Fahrenheit

### Slide 012: Significance of Levels of Measurement

- Type: Example / critique
- Application note: First classify each variable by measurement level; this determines valid statistics and chart encodings.
- Knowledge extracted:
  - Guiding data analysis and visualization choices
  - Determines statistical analyses
  - Tailor statistical methods based on the level of measurement.
  - Example: Nominal data requires different analyses than ratio data.
  - Informs visualization choices
  - Select visualizations aligned with the nature of your data.
  - Example: Use bar charts for ordinal data, histograms for interval data.
  - Aids in data interpretation
  - Understanding measurement level guides meaningful conclusions.
  - Example: Recognize ratio data for accurate calculations and interpretations.

### Slide 013: Properties of images

- Type: Concept / definition
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Image Models

### Slide 014: Visual language is a sign system

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Images perceived as a set of signs
  - Sender encodes information in signs
  - Receiver decodes information from signs
  - Semiology of Graphics, 1967
  - Jacques Bertin
  - Cartographer
  - [1918-2010]

### Slide 015: Image models

- Type: Concept / definition
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Visual Marks (Đối tượng biểu diễn)
  - Basic graphical elements in an image
  - Represent information (items or links)
  - Perceptual Channels (Biến thị giác)
  - Control the appearance of marks
  - Change appearance based on attribute value
  - Encode information
  - Channel = Visual Variables
  - Points
  - Position
  - Size
  - Value
  - Additional minor points omitted in this note: 6. Reopen the PDF for full slide text.

### Slide 016: Visual marks to represent items

- Type: Section divider / visual-only slide
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Introduces or visually illustrates: Visual marks to represent items.

### Slide 017: Visual marks to represent links

- Type: Section divider / visual-only slide
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Introduces or visually illustrates: Visual marks to represent links.

### Slide 018: Visual marks to represent links (2)

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Nested containment

### Slide 019: Perceptual channels

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Control the appearance of marks
  - Encode information

### Slide 020: Perceptual channels: Position

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Can encode quantitative variables (Q)
  - 1. A, B, C are distinguishable
  - 2. B is between A and C.
  - 3. BC is twice as long as AB.
  - "Resemblance, order and proportional are the three signfields in graphics.” — Bertin

### Slide 021: Perceptual channels: Position

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The most used perceptual channel
  - Suitable for most data types

### Slide 022: Perceptual channels: Size

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Length, area, volume
  - Good for 1D, 2D
  - Easy to compare

### Slide 023: Encoding Information in Color and Value

- Type: Concept / application
- Application note: For ordinal data, preserve the natural order on the axis or legend.
- Knowledge extracted:
  - Value (lightness) is perceived as ordered
  - Encode ordinal variables (O)
  - [better]
  - Encode continuous variables (Q)
  - Hue is normally perceived as unordered
  - Encode nominal variables (N)

### Slide 024: Perceptual channels: Color

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Should limit the number of colors
  - Not good

### Slide 025: Perceptual channels: Shape

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Encode nominal variables (N)
  - No ordered

### Slide 026: Encoding information in perceptual channels

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Quantitative/Ordered
  - Nominal

### Slide 027: Using marks and channels

- Type: Section divider / visual-only slide
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Introduces or visually illustrates: Using marks and channels.

### Slide 028: Example: Deconstructions

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Example: Deconstructions.

### Slide 029: William Playfair, 1786

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: William Playfair, 1786.

### Slide 030: William Playfair, 1786

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Color:
  - Imports/exports (N)
  - Y-axis:
  - Currency (Q)
  - X-axis:
  - Year (Q)

### Slide 031: Wattenberg’s Map of the Market

- Type: Section divider / visual-only slide
- Application note: Use maps only when location is analytically meaningful and metrics are normalized by relevant denominators.
- Knowledge extracted:
  - Introduces or visually illustrates: Wattenberg’s Map of the Market.

### Slide 032: Wattenberg’s Map of the Market

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Rectangle
  - Area: market cap
  - (Q)
  - Rectangle
  - Position: market sector (N), market cap
  - (Q)
  - Color Hue: loss vs. gain (N)
  - Color Value:
  - magnitude of loss or gain (Q)

### Slide 033: Minard 1869: Napoleon’s March

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Minard 1869: Napoleon’s March.

### Slide 034: Minard 1869: Napoleon’s March

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Minard 1869: Napoleon’s March.

### Slide 035: Minard 1869: Napoleon’s March

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Y-axis: latitude (Q)
  - Width: army size (Q)
  - Color: march / return
  - X-axis: longitude (Q)

### Slide 036: Minard 1869: Napoleon’s March

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Y-axis: temperature (Q)
  - X-axis:
  - longitude (Q) / time (O)

### Slide 037: Bertin’s Levels of Organization

- Type: Concept / definition
- Application note: For ordinal data, preserve the natural order on the axis or legend.
- Knowledge extracted:
  - Position
  - N
  - O
  - Q
  - Nominal
  - Size
  - N
  - O
  - Q
  - Ordinal
  - Value
  - N
  - Additional minor points omitted in this note: 11. Reopen the PDF for full slide text.

### Slide 038: Mackinlay’s Ranking

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Expanded Bertin’s variables and conjectured
  - eﬀectiveness of encodings by data type.
  - [Mackinlay 86]
  - Jock D. Mackinlay
  - Vice President
  - Tableau Software

### Slide 039: Example: Encoding Data

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Example: Encoding Data.

### Slide 040: Example: Coﬀee Sales

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Sales ﬁgures for a ﬁctional coﬀee chain
  - Sales
  - Proﬁt
  - Marketing
  - Q-Ratio
  - Product Type N {Coﬀee, Espresso, Herbal Tea,
  - Tea}
  - Market
  - N {Central, East, South, West}

### Slide 041: Encode “Proﬁt” (Q)

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Y-Position
  - Encode “Sales” (Q)
  - X-Position

### Slide 042: Encode “Product Type” (N)

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Hue (Color)

### Slide 043: Encode “Market” (N)

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Shape

### Slide 044: Encode “Marketing” (Q)

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Size

### Slide 045: Avoid over-encoding

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Use trellis plots (small multiples/facets) that
  - subdivide space to enable comparison across multiple plots.

### Slide 046: Visual encoding

- Type: Section divider / visual-only slide
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Introduces or visually illustrates: Visual encoding.

### Slide 047: Choosing visual encodings

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Assume k visual channels and n data attributes.
  - We would like to pick the “best” encoding
  - among a combinatorial set of possibilities of size nk

### Slide 048: Choosing visual encodings

- Type: Concept / definition
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Assume k visual encodings and n data
  - attributes. We would like to pick the “best”
  - encoding among a combinatorial set of
  - possibilities of size nk
  - Principle of Consistency
  - The properties of the image (visual variables) should
  - match the properties of the data.
  - Principle of Importance Ordering
  - Encode the most important information in the most effective way.

### Slide 049: Design Criteria [Mackinlay 86]

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Expressiveness
  - Eﬀectiveness

### Slide 050: Design Criteria [Mackinlay 86]

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Expressiveness
  - A set of facts is expressible in a visualization if it
  - expresses all the facts and only the facts in the data.
  - Tell the truth and nothing but the truth
  - (don’t lie, and don’t lie by omission)

### Slide 051: Dot plot

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Dot plot.

### Slide 052: Can not express the facts

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - The relationship among multiple data attributes may not be
  - expressed in a single horizontal dot plot.
  - Single horizontal dot plot

### Slide 053: Can not express the facts

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - The relationship among multiple data attributes may not be
  - expressed in a single horizontal dot plot.
  - Single horizontal dot plot
  - Categories in different positions

### Slide 054: Expresses facts not in the data

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - A length is interpreted
  - as a quantitative value.

### Slide 055: Design Criteria [Mackinlay 86]

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Expressiveness
  - A set of facts is expressible in a visualization if it
  - expresses all the facts and only the facts in the data.
  - Tell the truth and nothing but the truth
  - (don’t lie, and don’t lie by omission)
  - Eﬀectiveness
  - A visualization is more eﬀective than another one if
  - the information conveyed is more readily perceived.
  - Use encodings that people decode better
  - (where better = faster and/or more accurate)

### Slide 056: Mackinlay’s Design Algorithm

- Type: Concept / definition
- Application note: For ordinal data, preserve the natural order on the axis or legend.
- Knowledge extracted:
  - APT - “A Presentation Tool”, 1986
  - User formally specifies data model and type
  - Input: ordered list of data variables to show
  - APT searches over design space
  - Test expressiveness of each visual encoding
  - Generate encodings that pass test
  - Rank by perceptual effectiveness criteria
  - Output the “most effective” visualization

### Slide 057: APT

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Automatically generate a chart for input variables:
  - Price
  - Mileage
  - Repair
  - Weight

### Slide 058: Tableau

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Tableau.

### Slide 059: Take away: Visual Encoding Design

- Type: Summary
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Use expressive and effective encodings
  - Avoid over-encoding
  - Reduce the problem space
  - Use interaction to generate relevant views
  - Rarely does a single visualization answer all
  - questions. Instead, the ability to generate
  - appropriate visualizations quickly is critical!
