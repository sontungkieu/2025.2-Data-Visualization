# Visualization for Table Data, Part 1

- Source PDF: `10. Visualization for table data.pdf`
- Pages/slides: 71
- Extraction style: cleaned knowledge notes by slide/page, not a raw transcript.
- Visual caveat: image-heavy examples may need the original PDF for exact graphical details.

## Deck-Level Focus

Introduces coordinate systems, axes, amounts, grouped/stacked bars, heatmaps, distributions, and multi-distribution charts.

## Core Knowledge

- Cartesian position is the default for comparing quantitative values.
- Bar charts work well for amounts; ordering should follow meaning or aid comparison.
- Stacked bars are suitable only when parts form a meaningful whole.
- Histograms, density plots, box plots, and ridgelines reveal distributional structure.
- Heatmaps can summarize broad patterns but depend heavily on color scale design.

## How This Supports the Churn Report

- Use grouped bars for churn/non-churn counts and separate churn-rate bars for risk.
- Use histograms or bins for continuous features before grouping them into report-friendly
    segments.

## Slide-by-Slide Extraction

### Slide 001: Slide 1

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Slide 1.

### Slide 002: Visualization for table, multi-dimentional data

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 2

### Slide 003: Last lectures

- Type: Concept / definition
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Visual model and visual encoding
  - Graphical perception (visual decoding)
  - Today lecture
  - Visualization for table, multi-dimentional data
  - 4

### Slide 004: Outline

- Type: Roadmap
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Coordinate systems and axes
  - Color scales
  - Visualizing amounts
  - Visualizing distributions
  - Visualizing many distributions at once
  - Next lesson
  - Visualizing proportions
  - Visualizing associations
  - Visualizing trends
  - Visualizing uncertainty
  - 5

### Slide 005: Coordinate systems and axes

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 6

### Slide 006: Cartesian Coordinates

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - 2D Cartesian coordinate system
  - Each location is uniquely specified by an x and a y value.
  - The x and y axes run orthogonally to each other
  - Data values are placed in an even spacing along both axes
  - 7

### Slide 007: Example: Daily temperature for Houston

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - The same figure in different aspect ratios.
  - All three parts are valid visualizations of the temperature data.
  - 8

### Slide 008: Example: Daily temperature for Houston

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - If the x and y axes are measured in the same
  - units, then the grid spacings for the two axes should be equal.
  - 9

### Slide 009: Example: Population numbers of Texas counties relative to their median value

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - By displaying a ratio on a linear scale, we have overemphasized
  - ratios > 1 and have obscured ratios < 1.
  - Generally, ratios should not be displayed on a linear scale.
  - 10

### Slide 010: Nonlinear axes

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - In a Cartesian coordinate system, the position scales is linear.
  - In a nonlinear scale, even spacing in the visualization
  - corresponds to uneven spacing in data units.
  - 11

### Slide 011: Example: Population numbers of Texas counties relative to their median value

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - The dashed line indicates a ratio of 1, corresponding to a county with
  - median population number. The most populous counties have
  - approximately 100 times more inhabitants than the median county, and
  - the least populous counties have approximately 100 times fewer
  - inhabitants than the median county.
  - 12

### Slide 012: Square-root scales

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 13

### Slide 013: Example: Areas of northeastern US states

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - The square-root scale is the natural scale for
  - data that comes in squares
  - (a) Areas shown on a linear scale. (b) Areas shown on a square-root scale
  - 14

### Slide 014: Coordinate systems with curved axes

- Type: Concept / application
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - In the polar coordinate system, we specify positions via
  - an angle and a radial distance from the origin.
  - The angle axis is circular
  - Useful for data of a periodic nature, such that data
  - values at one end of the scale can be logically joined to
  - data values at the other end.
  - 15

### Slide 015: Example: Daily temperature normals for four selected locations in the US

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 16

### Slide 016: Color scales

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - 17

### Slide 017: Use cases

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Three fundamental use cases for color in data visualizations
  - Distinguish groups of data from each other
  - Represent data values
  - Highlight
  - 18

### Slide 018: Color as a tool to distinguish

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - A qualitative color scale:
  - A finite set of specific colors that are chosen to look clearly distinct
  - from each other while also being equivalent to each other
  - Distinguish discrete items or groups that do not have an intrinsic
  - order, such as different countries on a map or different
  - manufacturers of a certain product.
  - 19

### Slide 019: Example: Population growth in the US from 2000 to 2010

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 20

### Slide 020: Color to represent data values

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - A sequential color scale:
  - Represent quantitative data values, such as income, temperature, or speed
  - Clearly indicate which values are larger or smaller than which
  - other ones, and how distant two specific values are from each other
  - 21

### Slide 021: Example: Median annual income in Texas counties

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 22

### Slide 022: Diverging color scales

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Visualize the deviation of data values in one of
  - two directions relative to a neutral midpoint.
  - Two sequential scales stitched together at a common midpoint color.
  - 23

### Slide 023: Example: Percentage of people identifying as white in

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Texas counties
  - 24

### Slide 024: Color as a tool to highlight

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Specific categories or
  - values in the dataset that carry key information
  - about the story we want to tell.
  - Color these figure
  - elements in a color or set
  - of colors that vividly stand
  - out against the rest of the figure.
  - 25

### Slide 025: Example

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Track athletes are among the shortest and
  - leanest of male professional athletes
  - participating in popular sports.
  - 26

### Slide 026: Visualizing amounts

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - 27

### Slide 027: Scenario

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Visualize the magnitude of some set of numbers
  - a set of categories (e.g., brands of cars, cities, or
  - sports) and a quantitative value for each category.
  - 28

### Slide 028: Example: Highest-grossing movies for the weekend of

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - December 22–24, 2017
  - 29

### Slide 029: A bar plot with rotated axis tick labels

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - 30

### Slide 030: Horizontal bar plot

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - 31

### Slide 031: Example: Highest-grossing movies for the weekend of

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - December 22–24, 2017
  - This arrangement of bars is arbitrary, doesn’t serve a meaningful
  - purpose, and makes the resulting figure much less intuitive.
  - 32

### Slide 032: Example: 2016 median US annual household income versus age group

- Type: Example / critique
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Only rearrange bars when there is no natural
  - ordering to the categories the bars represent.
  - 33

### Slide 033: Example: 2016 median US annual household income versus age group

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - While this order of bars looks visually appealing,
  - the order of the age groups is now confusing
  - 34

### Slide 034: Grouped and Stacked Bars

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Frequently, we are interested in > two
  - categorical variables at the same time.
  - Grouped bar plot (groups of bars side-by-side)
  - 35

### Slide 035: Example: 2016 median US annual household income

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - versus age group and race
  - 36

### Slide 036: Show the data as four separate regular bar plots. This choice has the

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - advantage that we don’t need to encode either categorical variable by bar color
  - 37

### Slide 037: Stack bars on top of each other

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Useful when the sum of the amounts
  - represented by the individual stacked bars is a meaningful amount.
  - Numbers of female and male passengers on the
  - Titanic traveling in 1st, 2nd, and 3rd class
  - 38

### Slide 038: Bar chart: Baseline

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - 42

### Slide 039: Dot Plots

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Example: Life expectancies of countries in the
  - Americas, for the year 2007
  - 43

### Slide 040: Example: Life expectancies of countries in the Americas, for the year 2007

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 44

### Slide 041: Pay attention to the ordering of the data values

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 45

### Slide 042: Heatmap: map data values onto colors

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Harder to determine the exact data values shown.
  - Excellent job of highlighting broader trends.
  - 46

### Slide 043: Visualizing distributions

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Histograms and Density Plots
  - 47

### Slide 044: Visualizing a single distribution

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - To understand how a particular variable is
  - distributed in a dataset.
  - 48

### Slide 045: Example: Histogram of the ages of Titanic passengers

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 49

### Slide 046: Histograms depend on the chosen bin width

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 50

### Slide 047: Density plots

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Attempt to visualize the underlying probability
  - distribution of the data by drawing an
  - appropriate continuous curve
  - Estimated from the data
  - The most used method is called kernel density estimation
  - 51

### Slide 048: Example: Kernel density estimate of the age distribution

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - of passengers on the Titanic
  - 52

### Slide 049: Kernel density estimates depend on the chosen kernel and bandwidth

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 53

### Slide 050: Kernel density estimates can extend the tails of

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - the distribution into areas where no data exists,
  - and no data is even possible.
  - 54

### Slide 051: Visualizing multiple distributions at the same time

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Histogram of the ages of Titanic passengers stratified by gender
  - The heights of the bars representing female
  - passengers cannot easily be compared to each other
  - 55

### Slide 052: Example: Age distributions of male and female Titanic passengers

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Having all bars start at zero and making the
  - bars partially transparent
  - There is no clear visual indication that all blue bars start at a count of 0
  - 56

### Slide 053: Overlapping density plots

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Continuous density lines help the eye keep the distributions separate
  - 57

### Slide 054: Example: Age distributions of male and female

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Show the age distributions separately, each as a
  - proportion of the overall age distribution
  - 58

### Slide 055: Separate histograms, rotated by 90 degrees

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - The age distributions of male and female Titanic
  - passengers visualized as an age pyramid
  - 59

### Slide 056: Density plots for multiple distributions

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Work well if the distributions are somewhat distinct and contiguous
  - Example: Density estimates of the butterfat
  - percentage in the milk of four cattle breeds
  - 60

### Slide 057: Visualizing many distributions at once

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 61

### Slide 058: Scenarios

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Visualize multiple distributions at the same time.
  - For example, visualize how temperature varies
  - across different months while also showing the
  - distribution of observed temperatures within each month.
  - 62

### Slide 059: Visualizing distributions along the vertical axis

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Show their mean or median as points,
  - Show some indication of the variation around
  - the mean or median shown by error bars.
  - 63

### Slide 060: Problems of the approach

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Loss a lot of information about the data
  - Is not immediately obvious what the points represent
  - Is not obvious what the error bars represent
  - 64

### Slide 061: Boxplot

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Invented by the statistician John Tukey in
  - 1970s
  - 65

### Slide 062: Example: Mean daily temperatures in Lincoln, NE, visualized as boxplots

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 66

### Slide 063: Violin plots

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Only the y values of the points are visualized in the violin plot.
  - The width of the violin at a given y value represents the point
  - density at that y value.
  - Technically, a violin plot is a density estimate rotated by 90
  - degrees and then mirrored.
  - 67

### Slide 064: Example: Mean daily temperatures in Lincoln, NE,

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - visualized as violin plots
  - 68

### Slide 065: Strip charts

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Displays numerical data along a single strip.
  - A good alternative to boxplots when the sample
  - sizes are small so that you can see the individual data points.
  - 69

### Slide 066: Example: Mean daily temperatures in Lincoln, NE,

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - visualized as strip charts
  - Spread out the points somewhat along the x
  - axis, by adding some random noise in the x dimension (jittering)
  - 70

### Slide 067: Example: Mean daily temperatures in Lincoln, NE,

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - visualized as sina plots
  - A combination of individual points and violins.
  - 71

### Slide 068: Visualizing distributions along the horizontal axis

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Ridgeline plots
  - These plots look like mountain ridgelines.
  - Standard ridgeline plot uses density estimates.
  - The purpose of the plot is not to show specific density values but
  - instead to allow for easy comparison of density shapes and relative heights across groups.
  - 72

### Slide 069: Example: Evolution of movie lengths over time

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Ridgeline plots scale to very large numbers of distributions
  - 73

### Slide 070: Example: Voting patterns in the US House of

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Representatives
  - Ridgeline plot is used to compare two trends over time.
  - Voting patterns have become increasingly polarized.
  - 74

### Slide 071: 109

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: 109.
