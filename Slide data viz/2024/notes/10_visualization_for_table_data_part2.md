# Visualization for Table Data, Part 2

- Source PDF: `10. Visualization for table data_p2.pdf`
- Pages/slides: 58
- Extraction style: cleaned knowledge notes by slide/page, not a raw transcript.
- Visual caveat: image-heavy examples may need the original PDF for exact graphical details.

## Deck-Level Focus

Continues table-data visualization with proportions, nested proportions, relationships, trends, and uncertainty.

## Core Knowledge

- Proportion charts show part-to-whole relationships; interpretation depends on baseline and
    denominator.
- Side-by-side and stacked bars have different comparison strengths and weaknesses.
- Scatterplots and scatterplot matrices reveal relationships between quantitative variables.
- Trend lines, smoothing, and confidence bands should communicate uncertainty honestly.

## How This Supports the Churn Report

- Clarify that churn-rate bars are within-group rates and do not sum to 100 percent across groups.
- If model scores or trends are shown later, include uncertainty or explain the limits of
    interpretation.

## Slide-by-Slide Extraction

### Slide 001: Slide 1

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: Slide 1.

### Slide 002: Visualization for table, multi-dimensional data

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 2

### Slide 003: Outline

- Type: Roadmap
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Previous lesson
  - Coordinate systems and axes
  - Color scales
  - Visualizing amounts
  - Visualizing distributions
  - Visualizing many distributions at once
  - Today lesson
  - Visualizing proportions
  - Visualizing nested proportions
  - Visualizing associations
  - Visualizing trends
  - Visualizing uncertainty
  - Additional minor points omitted in this note: 1. Reopen the PDF for full slide text.

### Slide 004: Visualizing proportions

- Type: Concept / application
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 4

### Slide 005: Scenarios

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Show how some group, entity, or amount
  - breaks down into individual pieces that each
  - represent a proportion of the whole.
  - Examples:
  - The proportions of men and women in a group of people.
  - The percentages of people voting for different
  - political parties in an election.
  - The market shares of companies.
  - 5

### Slide 006: Example: Party composition of the eighth German Bundestag, 1976–1980

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Visualized as a pie chart
  - Breaks a circle into slices such that the area of each
  - slice is proportional to the fraction of the total it represents.
  - 6

### Slide 007: A case where pie charts fail

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Market share of five hypothetical companies,
  - A–E, for the years 2015–2017
  - A comparison of relative market share within years is nearly impossible.
  - Changes in market share across years are difficult to see.
  - 7

### Slide 008: Stacked bars

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - The trends of a growing market share for company A and a
  - shrinking market share for company E are clearly visible.
  - The relative market shares of the five companies within each year
  - are still hard to compare
  - 8

### Slide 009: Side-by-side bars

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Market share of five hypothetical companies
  - for the years 2015–2017, visualized as side-byside bars.
  - 9

### Slide 010: Pros and cons of common approaches to visualizing proportions

- Type: Concept / application
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 10

### Slide 011: A case for Stacked Bars

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - The problem of shifting internal bars disappears
  - if there are only two bars in each stack.
  - Example: Change in the gender composition of
  - the Rwandan parliament over time, 1997 to
  - 2016.
  - 11

### Slide 012: A case for Stacked Densities

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Stacked densities can be thought of many infinitely small stacked
  - bars arranged side-by-side
  - Visualize how proportions change in response to a continuous variable
  - Example: Health status by age
  - 12

### Slide 013: Visualizing proportions separately as parts of the total

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Side-by-side bars have the problem that they
  - don’t visualize the size of the individual parts relative to the whole
  - Stacked bars have the problem that the
  - different bars cannot be compared easily
  - because they have different baselines
  - 13

### Slide 014: Example: Health status by age, shown as proportion of the total number of people

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - The colored areas show the density estimates
  - of the ages of people with the respective health status
  - The gray areas show the overall age distribution
  - 14

### Slide 015: Example: Marital status by age

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 15

### Slide 016: Example: Marital status by age, shown as proportion of

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - the total number of people
  - The colored areas show the density estimates of the
  - ages of people with the respective marital status.
  - The gray areas show the overall age distribution.
  - Still, this representation doesn’t make it easy to
  - determine relative proportions at any given point in time.
  - 16

### Slide 017: Example: Marital status by age, shown as proportion of

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - the total number of people
  - Show relative proportions instead of absolute counts along the y axis
  - 17

### Slide 018: Visualizing nested proportions

- Type: Concept / application
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 18

### Slide 019: Scenarios

- Type: Example / critique
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Break down a dataset by multiple categorical variables at once.
  - Example
  - Visualize both the fraction of bridges made from
  - steel, iron, or wood and the fraction that are crafts or modern.
  - 19

### Slide 020: Example: Breakdown of bridges in Pittsburgh

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - By construction material (steel, wood, iron) and
  - by date of construction (crafts, before 1870,
  - and modern, after 1940).
  - The percentages add up to more than 100%.
  - 20

### Slide 021: Example: Breakdown of bridges in Pittsburgh as a bar plot

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Does not clearly indicate the overlap among different groups
  - 21

### Slide 022: Mosaic plots

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - The widths of each rectangle are proportional to the number of bridges
  - constructed in that era.
  - The heights are proportional to the number of bridges constructed from that material.
  - Numbers represent the counts of bridges within each category.
  - A critical condition for a mosaic plot: every categorical variable shown
  - must cover all the observations in the dataset.
  - 22

### Slide 023: Tree map

- Type: Concept / application
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Take an enclosing rectangle and subdivide it
  - into smaller rectangles whose areas represent the proportions.
  - Recursively nest rectangles inside each other.
  - 23

### Slide 024: Example: States in the US visualized as a treemap

- Type: Example / critique
- Application note: Use graph visualization only when the dataset has explicit relationships between entities.
- Knowledge extracted:
  - 24

### Slide 025: Nested pies

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Breakdown of bridges in Pittsburgh by construction material (steel,
  - wood, iron; inner circle) and by era of construction (crafts,
  - emerging, mature, modern; outer circle).
  - Numbers represent the counts of bridges within each category
  - 25

### Slide 026: Example: Breakdown of bridges in Pittsburgh by construction

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - material and by era of construction
  - 26

### Slide 027: Parallel sets

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Show how the total dataset breaks down by each individual categorical variable.
  - Then draw shaded bands that show how the subgroups relate to each other.
  - 27

### Slide 028: Example: Breakdown of bridges in Pittsburgh by construction

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - material, length, era of construction, and the river they span
  - The coloring of the bands highlights the river
  - spanned by the different bridges.
  - 28

### Slide 029: Example: Breakdown of bridges in Pittsburgh by construction

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - material, length, era of construction, and the river they span
  - The modified order results in a figure that is
  - easier to read and less busy.
  - 29

### Slide 030: Visualizing associations

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Among two or more Quantitative Variables
  - 30

### Slide 031: Scenarios

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Many datasets contain two or more quantitative variables.
  - We may be interested in how these variables relate to each other.
  - Example:
  - A dataset of quantitative measurements of different
  - animals, such as the animals’ height, weight, length,
  - and daily energy demands.
  - 31

### Slide 032: Scatterplots

- Type: Concept / application
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Head length (measured from the tip of the bill to the back of the
  - head, in mm) versus body mass (in grams), for 123 blue jays.
  - Each dot corresponds to one bird.
  - There is a moderate tendency for heavier birds to have longer heads.
  - 32

### Slide 033: Example: Head length versus body mass

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The birds’ sex is indicated by color.
  - 33

### Slide 034: Bubble chart

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The birds’ sex is indicated by color.
  - The birds’ skull size by symbol size.
  - 34

### Slide 035: All-against-all scatterplot matrix

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - 35

### Slide 036: Correlation coefficient

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Examples of correlations of different magnitude
  - and direction, with associated.
  - correlation coefficient r
  - 36

### Slide 037: Correlograms

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Visualizations of correlation coefficients
  - 37

### Slide 038: Example: Correlations in mineral content for forensic glass samples

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The magnitude of each correlation is also
  - encoded in the size of the colored circles.
  - 38

### Slide 039: Visualizing trends

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - 39

### Slide 040: Two fundamental approaches to determining a trend

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Smoothing the data by some method, such as a moving average
  - Or fitting a curve with a defined functional form and
  - then draw the fitted curve.
  - 40

### Slide 041: Smoothing

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Daily closing values of the Dow Jones Industrial
  - Average for the year 2009, shown together
  - with their 20-day, 50-day, and 100-day moving averages.
  - (a) The moving averages are plotted at the ends of
  - the moving time windows.
  - (b) The moving averages are plotted in the centers
  - of the moving time windows.
  - 41

### Slide 042: 42

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: 42.

### Slide 043: Moving average limitations

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Results in a smoothed curve that is shorter than the original curve
  - Parts are missing at either the beginning or the end or both.
  - Even with a large averaging window, a moving
  - average is not necessarily that smooth. It may
  - exhibit small bumps and wiggles even though larger-scale smoothing.
  - 43

### Slide 044: Locally estimated scatterplot smoothing (LOESS)

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Fits low-degree polynomials to subsets of the data.
  - 44

### Slide 045: Example: Fuel-tank capacity versus price of 93 cars

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - released for the 1993 model year
  - 45

### Slide 046: Spline models

- Type: Concept / definition
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - LOESS requires fitting of many separate regression models
  - Spline models
  - A faster alternative to LOESS
  - A spline is a piecewise polynomial function
  - Fit a spline with k segments, we need to specify k +
  - 1 knots.
  - 46

### Slide 047: Example: Different smoothing models

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Display widely different behaviors, near the boundaries of the data.
  - (a) LOESS smoother, as in
  - Figure 14-4.
  - (b) Cubic regression splines with 5 knots.
  - (c) Thin-plate regression spline with 3 knots.
  - (d) Gaussian process spline with
  - 6 knots.
  - 47

### Slide 048: Visualizing uncertainty

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - 52

### Slide 049: Scenarios

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - One of the most challenging aspects of data
  - visualization is the visualization of uncertainty.
  - Nearly every dataset has some uncertainty.
  - Whether and how we choose to represent this
  - uncertainty can make a major difference in how
  - accurately our audience perceives the meaning of the data.
  - Common approaches
  - Error bars
  - Confidence bands
  - 53

### Slide 050: Examples of uncertainty

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - In the context of future events, the eventual outcome is uncertain
  - An event in the past can also be uncertain
  - A red car parked across the street at 8 a.m. but not
  - at 4 p.m., then we can conclude the car left at some
  - point during the 8-hour window, but we don’t know exactly when.
  - Mathematically, we deal with uncertainty by
  - employing the concept of probability.
  - 54

### Slide 051: Visualizing probability as frequency

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 55

### Slide 052: Probability distribution

- Type: Concept / definition
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Confidence levels are expressed as a percentage and
  - indicate how frequently that percentage of the target
  - population would give an answer that lies within the confidence interval.
  - 56

### Slide 053: Example: Mean chocolate flavor ratings and

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - associated confidence intervals
  - 57

### Slide 054: Visualizing the uncertainty of curve fits

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Show the uncertainty in a trend line with a confidence band
  - Range of different fit lines that would be compatible with the data
  - Example: Head length versus body mass for male blue jays
  - 58

### Slide 055: Example: Head length versus body mass for male blue jays

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - The straight blue lines now represent equally
  - likely alternative fits randomly drawn from the posterior distribution
  - 59

### Slide 056: Graded confidence band

- Type: Concept / definition
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Shows several confidence levels at once
  - Enhances the sense of uncertainty in the reader.
  - Forces the reader to confront the possibility that
  - the data might support different alternative trend lines.
  - 60

### Slide 057: Confidence bands for nonlinear curve fits

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - The confidence band represents a family of
  - curves that are all quite a bit wigglier than the
  - overall best fit shown in part (a).
  - 61

### Slide 058: 62

- Type: Section divider / visual-only slide
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - Introduces or visually illustrates: 62.
