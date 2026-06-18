# Principles of Figure Design

- Source PDF: `11. Principles of figure design.pdf`
- Pages/slides: 114
- Extraction style: cleaned knowledge notes by slide/page, not a raw transcript.
- Visual caveat: image-heavy examples may need the original PDF for exact graphical details.

## Deck-Level Focus

Provides practical rules for proportional ink, overlap, color, multi-panel figures, titles, tables, context, and 3D avoidance.

## Core Knowledge

- The amount of visual ink should be proportional to the represented data where appropriate.
- Overplotting hides patterns and requires techniques such as transparency, binning, or faceting.
- Color should be meaningful, restrained, and accessible to color-vision deficiencies.
- Multi-panel figures help compare related distributions or groups at scale.
- Titles, captions, labels, and data-source notes provide context and should not be treated as
    decoration.
- Avoid gratuitous 3D because it distorts perception unless the data is inherently 3D.

## How This Supports the Churn Report

- Keep churn charts 2D, use direct labels where helpful, and preserve a consistent color mapping.
- Use chart titles that state the question or insight, not only the variable name.

## Slide-by-Slide Extraction

### Slide 001: Principles of figure design

- Type: Concept / definition
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Viet-Trung Tran
  - 1

### Slide 002: A sample figure

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 2

### Slide 003: Outline

- Type: Roadmap
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The principle of proportional ink
  - Handling overlapping points
  - Common pitfalls of color use
  - Redundant coding
  - Multi-panel figures
  - Titles, captions, and tables
  - Balance the data and the context
  - Use larger axis labels
  - Avoid line drawings
  - Don’t go 3D
  - 3

### Slide 004: The principle of proportional ink

- Type: Concept / definition
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 4

### Slide 005: The principle of proportional ink

- Type: Concept / definition
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - When a shaded region is used to represent a
  - numerical value, the area of that shaded region
  - should be directly proportional to the
  - corresponding value [Bergstrom and West
  - 2016].
  - Make sure that there is no inconsistency
  - 5

### Slide 006: Visualizations along linear axes

- Type: Concept / application
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Median income in the five counties of the state of Hawaii
  - The y-axis scale starts at $50,000 instead of $0
  - The bar heights are not proportional to the values shown
  - The income differential between the county of Hawaii and the other four
  - counties appears much bigger than it actually is
  - 6

### Slide 007: Example: Median income in the five counties of the state of Hawaii

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - The y-axis scale starts at $0 and therefore the relative magnitudes of the
  - median incomes in the five counties are accurately shown.
  - Bars on a linear scale should always start at 0.
  - 7

### Slide 008: Example: Stock price of Facebook (FB) from Oct. 22, 2016, to Jan.

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - 21, 2017
  - The FB stock price collapsed around Nov. 1,
  - 2016?
  - 8

### Slide 009: Example: Stock price of Facebook (FB) from Oct. 22, 2016, to Jan.

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - 21, 2017
  - More accurately relays the magnitude of the FB
  - price drop around Nov. 1, 2016
  - 9

### Slide 010: Question

- Type: Concept / application
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Bars and shaded areas are not useful to
  - represent small changes over time or
  - differences between conditions, since we
  - always must draw the whole bar or area starting from 0?
  - 10

### Slide 011: Example: Change in median income in Hawaiian counties from 2010 to 2015

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - It is perfectly valid to use bars or shaded areas
  - to show differences between conditions, if we
  - make it explicit which differences we are showing.
  - 11

### Slide 012: Example: Decline in Facebook (FB) stock price relative to the price of Oct. 22, 2016

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 12

### Slide 013: Visualizations along logarithmic axes

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - For a logarithmic scale, data values are not
  - linearly spaced along the axis
  - 13

### Slide 014: Example: GDP in 2007 of countries in Oceania

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - Simply place a dot at the appropriate location along the scale for
  - each country’s GDP and avoid the issue of bar lengths altogether.
  - 14

### Slide 015: Handling overlapping points

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 16

### Slide 016: Scenarios

- Type: Concept / application
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - In the visualization of large or very large
  - datasets, simple x–y scatterplots do not work
  - very well because many points lie on top of
  - each other and partially or fully overlap.
  - In small datasets if data values were recorded
  - with low precision or rounded, multiple
  - observations have the same numeric values.
  - 17

### Slide 017: Partial transparency and jittering

- Type: Concept / definition
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - City fuel economy versus engine displacement, for
  - popular cars released between 1999 and 2008
  - Each point represents one car.
  - Many car models have identical values.
  - 18

### Slide 018: Example: City fuel economy versus engine displacement

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Points have been made partially transparent
  - Points that lie on top of other points can now be identified by their darker shade
  - 19

### Slide 019: Example: City fuel economy versus engine displacement

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - By adding a small amount of jitter to each point,
  - we can increase the visibility of the overplotted
  - points without substantially distorting the message of the plot.
  - 20

### Slide 020: Adding too much jitter

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - The visualization does not accurately reflect the underlying dataset
  - 21

### Slide 021: Example: Departure delay in minutes versus flight departure time

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - When the number of individual points gets very
  - large, partial transparency (with or without
  - jittering) will not be sufficient
  - Areas with high point density will appear as uniform blobs of dark color,
  - Areas with low point density are barely visible
  - 22

### Slide 022: 2D histogram

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Instead of plotting individual points, we bin the data in two dimensions
  - Subdivide the entire x–y plane into small rectangles,
  - count how many observations fall into each one,
  - and then color the rectangles by those counts.
  - 23

### Slide 023: Example: Head length versus body mass for 123 blue jays

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Estimate the point density across the plot area.
  - The lines indicate regions of similar point density.
  - The point density increases toward the center of the plot.
  - 24

### Slide 024: Example: Head length versus body mass for 123 blue jays

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - The areas enclosed by the contour lines are shaded with increasingly darker shades of gray.
  - This shading creates a stronger visual impression of increasing point
  - density toward the center of the point cloud.
  - 25

### Slide 025: Example: Head length versus body mass for 123 blue jays

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Indicate the birds’ sex by color when drawing contour lines.
  - 26

### Slide 026: Example: Price of diamonds versus their carat value

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 27

### Slide 027: Example: Price of diamonds versus their carat value

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Individual points are replaced by contour lines
  - 28

### Slide 028: Example: Price of diamonds versus their carat value

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Draw the contour lines for each cut quality in its own plot panel.
  - 29

### Slide 029: Common pitfalls of color use

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - 30

### Slide 030: Encoding too much or irrelevant information

- Type: Concept / application
- Application note: For nominal data, use categorical encodings such as bar positions or color hue; do not treat category codes as quantities.
- Knowledge extracted:
  - Population growth versus
  - population size for all 50 US
  - states and the District of
  - Columbia.
  - Qualitative color scales
  - work best when there are three to five different
  - categories that need to be colored
  - 31

### Slide 031: Example: Population growth from 2000 to 2010 versus population size in 2000

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Use color only to indicate the geographic region of each state
  - Identify individual states by direct labeling.
  - 32

### Slide 032: Example: Population growth in the US from 2000 to 2010

- Type: Example / critique
- Application note: Use color intentionally and choose palettes that remain readable for color-vision deficiencies.
- Knowledge extracted:
  - Coloring for the sake of coloring, without having a clear purpose for the colors
  - 33

### Slide 033: Using nonmonotonic color scales to encode data values

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Sequential color scales that can represent data values
  - The colors need to clearly indicate which data values are larger
  - or smaller than which other ones, and the differences between
  - colors need to visualize the corresponding differences between data values.
  - The rainbow color scale is highly nonmonotonic
  - Tends to obscure data features and/or highlight arbitrary aspects of the data.
  - The colors are overly saturated.
  - 34

### Slide 034: Example: Percentage of people identifying as white in Texas counties

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 35

### Slide 035: Not designing for Color-Vision deficiency

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Some of the readers may have some form of colorvision deficiency (CVD i.e., are colorblind)
  - Red–green color-vision deficiency.
  - Blue and green (blue–yellow color-vision deficiency).
  - Sequential scales will generally not cause any problems for people with CVD
  - It presents a continuous gradient from dark to light colors.
  - 36

### Slide 036: Diverging color scales

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - A red–green contrast becomes indistinguishable under red–green CVD
  - (deuteranomaly or protanomaly)
  - A blue–green contrast becomes indistinguishable under blue–yellow CVD
  - (tritanomaly).
  - 37

### Slide 037: Diverging color scales

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The ColorBrewer PiYG (pink to yellow-green) scale looks like a red–green
  - contrast to people with regular color vision but works for people with all
  - forms of color-vision deficiency.
  - 38

### Slide 038: Qualitative color scales

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Different colors need to be distinguishable from each
  - other under all forms of CVD.
  - Qualitative color palette for all color-vision deficiencies.
  - Colorblind-friendly color scale [Okabe and Ito 2008].
  - 39

### Slide 039: Colored elements become difficult to distinguish at small sizes

- Type: Concept / application
- Application note: Use color intentionally and choose palettes that remain readable for color-vision deficiencies.
- Knowledge extracted:
  - This problem becomes exacerbated in the CVD simulations.
  - 40

### Slide 040: Redundant coding

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Use color to enhance the visual appearance of the figure without relying
  - entirely on color to convey key information.
  - 41

### Slide 041: Example: Sepal width versus sepal length for three different

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - The virginica points in green and the versicolor
  - points in blue are difficult to distinguish from each other.
  - 42

### Slide 042: Color-vision deficiency simulation

- Type: Concept / application
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - 43

### Slide 043: Example: Sepal width versus sepal length for three different Iris species

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - Swap the colors used for Iris setosa and Iris versicolor, so that the blue is
  - no longer directly next to the green.
  - Use three different symbol shapes, so that the points all look different.
  - 44

### Slide 044: Example: Color-vision deficiency simulation

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - 45

### Slide 045: Example: Stock price over time for four major tech companies

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 46

### Slide 046: Example: Stock price over time for four major tech companies

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 47

### Slide 047: Designing figures without legends

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Whenever possible, design your figures so they don’t need a separate legend.
  - In direct labeling, we incorporate appropriate text labels or other visual
  - elements that serve as guideposts to the rest of the figure.
  - 48

### Slide 048: Example: Sepal width versus sepal length for three different

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - 49

### Slide 049: Example: Density estimates of the sepal lengths of three different

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Iris species
  - Each density estimate is directly labeled with
  - the respective species name.
  - 50

### Slide 050: Density plots into the margins of a scatterplot

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 51

### Slide 051: Example: Temperatures in Lincoln, NE, in 2016

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - Integrate the color legend into the x axis
  - 52

### Slide 052: Multi-panel figures

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 53

### Slide 053: Scenarios

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - When datasets become large and complex, they
  - often contain much more information than can
  - reasonably be shown in a single figure panel.
  - It can be helpful to create multi-panel figures.
  - Compound figures
  - Separate figure panels assembled in an arbitrary
  - arrangement (which may or may not be grid-based).
  - Show entirely different visualizations, or possibly
  - even different datasets.
  - 54

### Slide 054: Small multiples

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Plots consisting of multiple panels arranged in a regular grid.
  - Each panel shows a different subset of the data, but all panels use the same type of
    visualization.
  - Sometimes referred to as “faceting”.
  - Example
  - Breakdown of passengers on the
  - Titanic by gender, survival, and class in which they traveled
  - (1st, 2nd, or 3rd).
  - 55

### Slide 055: Example: Average movie rankings versus number of votes

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - It is important that each panel uses the same axis ranges and scaling
  - 56

### Slide 056: Example: Trends in bachelor’s degrees conferred by US institutions of higher learning

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - 57

### Slide 057: Example: Trends in bachelor’s degrees conferred by US institutions of higher learning

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - 58

### Slide 058: Compound figures

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Combine several independent panels into a figure that conveys one overarching point.
  - Individual panels of the compound figure are labeled alphabetically
  - Example
  - Trends in bachelor’s degrees conferred by US institutions of higher learning
  - 59

### Slide 059: Example: Trends in bachelor’s degrees conferred by US institutions of higher learning

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Poor labeling
  - The panel labels are too large and thick, they are in
  - the wrong font, and they are placed in an awkward location
  - 60

### Slide 060: Example: Physiology and body composition of male and female athletes

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - (a) shows the number of men and women in the dataset.
  - (b) shows the counts of red and white blood cells for men and women.
  - (c) shows the body fat percentages of men and women, broken down by sport.
  - 61

### Slide 061: Example: Physiology and body composition of male and female athletes

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 62

### Slide 062: Example: Physiology and body composition of male and female athletes

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 63

### Slide 063: Titles, captions, and tables

- Type: Concept / application
- Application note: Use titles, captions, and annotations to state the analytical question and guide interpretation.
- Knowledge extracted:
  - Data is placed into context by accompanying titles,
  - captions, and other annotations
  - 64

### Slide 064: Figure titles and captions

- Type: Concept / application
- Application note: Use titles, captions, and annotations to state the analytical question and guide interpretation.
- Knowledge extracted:
  - The job of the title is to accurately convey to the reader
  - what the figure is about, what point it makes.
  - Figure 22-1. Corruption and human development: the most developed countries experience the
    corruption.
  - Original
  - figure concept: [The Economist online 2011]. Data sources:
  - TRƯỜNG CÔNGleast
  - NGHỆ THÔNG
  - TIN VÀ TRUYỀN
  - THÔNG
  - Transparency International & UN Human Development Report.
  - 65

### Slide 065: The title, subtitle, and data source statements have been

- Type: Concept / application
- Application note: Use titles, captions, and annotations to state the analytical question and guide interpretation.
- Knowledge extracted:
  - incorporated into the figure
  - 66

### Slide 066: Example: Head length versus body mass for 123 blue jays

- Type: Example / critique
- Application note: Prefer position and length for accurate comparison; avoid area or angle when exact comparison is important.
- Knowledge extracted:
  - 67

### Slide 067: Example: Stock price over time for four major tech companies

- Type: Example / critique
- Application note: Use titles, captions, and annotations to state the analytical question and guide interpretation.
- Knowledge extracted:
  - Axis or legend titles can be omitted, namely
  - when the labels themselves are fully explanatory.
  - 68

### Slide 068: Example: Stock price over time for four major tech companies

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Figure 100: Stock price over time for four major tech companies. The
  - stock price for each company has been normalized to equal 100 in June
  - 2012
  - 69

### Slide 069: Example: Stock price over time for four major tech companies

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 70

### Slide 070: Examples of poorly and appropriately formatted tables

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 71

### Slide 071: Tables

- Type: Concept / application
- Application note: Use titles, captions, and annotations to state the analytical question and guide interpretation.
- Knowledge extracted:
  - Key rules for table layouts
  - 1. Do not use vertical lines.
  - 2. Do not use horizontal lines between data rows.
  - (Horizontal lines as a separator between the title row
  - and the first data row or as a frame for the entire table are fine.)
  - 3. Text columns should be left aligned.
  - 4. Number columns should be right aligned and should
  - use the same number of decimal digits throughout.
  - 5. Columns containing single characters should be centered.
  - 6. The header fields should be aligned with their data; i.e.,
  - the heading for a text column will be left aligned and
  - the heading for a number column will be right aligned.
  - Additional minor points omitted in this note: 1. Reopen the PDF for full slide text.

### Slide 072: Balance the data and the context

- Type: Concept / application
- Application note: Use titles, captions, and annotations to state the analytical question and guide interpretation.
- Knowledge extracted:
  - 73

### Slide 073: Scenarios

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - The graphical elements in any visualization can
  - be broadly subdivided into elements that
  - represent data and elements that do not.
  - Example
  - Points in a scatterplot, the bars in a histogram or bar
  - plot, or the shaded areas in a heatmap.
  - Plot axes, axis ticks and labels, axis titles, legends, and plot annotations.
  - 74

### Slide 074: Providing the appropriate amount of context

- Type: Concept / application
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - “Data–ink ratio” is defined as the “proportion of
  - a graphic’s ink devoted to the non-redundant
  - display of data information.” (Edward Tufte)
  - Maximize the data–ink ratio, within reason.
  - 75

### Slide 075: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 76

### Slide 076: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 77

### Slide 077: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 78

### Slide 078: Example: Survival of passengers on the Titanic, broken down by gender and class

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 79

### Slide 079: Example: Survival of passengers on the Titanic, broken down by gender and class

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 80

### Slide 080: Background grids

- Type: Concept / application
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Grid lines in the background of a plot can help
  - the reader discern specific data values and
  - compare values in one part of a plot to values in another part.
  - Grid lines can add visual noise, when they are
  - prominent or densely spaced.
  - 81

### Slide 081: Example: Stock price over time for four major tech companies

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 82

### Slide 082: Example: Indexed stock price over time for four major tech companies

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 83

### Slide 083: Example: Indexed stock price over time for four major tech companies

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 84

### Slide 084: Example: Percent increase in stock price from June 2012 to June

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 2017
  - 85

### Slide 085: Example: Percent increase in stock price from June 2012 to June

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - 2017
  - 86

### Slide 086: Paired data

- Type: Example / critique
- Application note: Use scatter/trend views for relationships and show uncertainty when a fitted line or prediction is presented.
- Knowledge extracted:
  - Where the relevant comparison is the x = y line,
  - such as in scatterplots of paired data.
  - Draw a diagonal line rather than a grid.
  - Example
  - Gene expression levels in a mutant bacteriophage
  - T7 relative to wild type.
  - 87

### Slide 087: Example: Gene expression levels in a mutant bacteriophage T7 relative to wild type

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 88

### Slide 088: Example: Gene expression levels in a mutant bacteriophage T7 relative to wild type

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 89

### Slide 089: Use larger axis labels

- Type: Concept / application
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 90

### Slide 090: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 91

### Slide 091: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 92

### Slide 092: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 93

### Slide 093: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 94

### Slide 094: Example: Percent body fat versus height in professional male

- Type: Example / critique
- Application note: Always state the denominator of a percentage or rate to avoid misreading part-to-whole relationships.
- Knowledge extracted:
  - Australian athletes
  - 95

### Slide 095: Avoid line drawings

- Type: Concept / application
- Application note: Use color intentionally and choose palettes that remain readable for color-vision deficiencies.
- Knowledge extracted:
  - Whenever possible, visualize your data with solid, colored shapes
  - rather than with lines that outline those shapes.
  - 96

### Slide 096: Example: Histogram of the ages of Titanic passengers, drawn with empty bars

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 97

### Slide 097: Example: Histogram of the ages of Titanic passengers

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - 98

### Slide 098: Example: Density estimates of the sepal lengths of three different

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Iris species
  - 99

### Slide 099: Example: Density estimates of the sepal lengths of three different

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Iris species
  - 100

### Slide 100: Example: Density estimates of the sepal lengths of three different

- Type: Example / critique
- Application note: For quantitative data, use numeric axes, distributions, bins, or summary statistics instead of arbitrary categories.
- Knowledge extracted:
  - Iris species
  - 101

### Slide 101: Example: City fuel economy versus engine displacement

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 102

### Slide 102: Example: City fuel economy versus engine displacement

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 103

### Slide 103: Don’t go 3D

- Type: Concept / application
- Application note: Avoid 3D unless the data itself has a necessary 3D spatial structure.
- Knowledge extracted:
  - Almost always inappropriately used.
  - 104

### Slide 104: Avoid gratuitous 3D

- Type: Concept / application
- Application note: Avoid 3D unless the data itself has a necessary 3D spatial structure.
- Knowledge extracted:
  - The third dimension does not convey any actual data.
  - 3D is used simply to decorate and adorn the plot.
  - 105

### Slide 105: Example: The same 3D pie chart shown from four different angles

- Type: Example / critique
- Application note: Avoid 3D unless the data itself has a necessary 3D spatial structure.
- Knowledge extracted:
  - 106

### Slide 106: Example: Numbers of female and male passengers on

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - the Titanic traveling in 1st, 2nd, and 3rd class
  - 107

### Slide 107: Avoid 3D position scales

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - The use of the third
  - dimension serves an actual purpose.
  - Nevertheless, the resulting
  - plots are frequently difficult to interpret.
  - Example: Fuel efficiency versus displacement and power for 32 cars
  - 108

### Slide 108: Example: Fuel efficiency versus displacement (a) and power (b)

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 109

### Slide 109: Example: Power versus displacement for 32 cars, with fuel

- Type: Example / critique
- Application note: When documenting a chart, explicitly state the mark and visual channel used for each variable.
- Knowledge extracted:
  - efficiency represented by dot size
  - 110

### Slide 110: Example: Mortality rates in Virginia in 1940, visualized as a 3D bar plot

- Type: Example / critique
- Application note: Use bar charts for comparing amounts or rates; stacked bars only when the parts share a meaningful denominator.
- Knowledge extracted:
  - 111

### Slide 111: Example: Mortality rates in Virginia in 1940, visualized as a small multiples plot

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 112

### Slide 112: Appropriate use of 3D visualizations

- Type: Concept / application
- Application note: Avoid 3D unless the data itself has a necessary 3D spatial structure.
- Knowledge extracted:
  - The visualization is interactive and can be rotated by the viewer.
  - If the visualization isn’t interactive, showing it
  - slowly rotating, will allow the viewer to discern
  - where in 3D space different graphical elements reside.
  - Use 3D visualizations when we want to show
  - actual 3D objects and/or data mapped onto them.
  - 113

### Slide 113: Example: Relief of the Island of Corsica in the

- Type: Example / critique
- Application note: Use this as supporting theory when explaining why a chart or layout choice is appropriate.
- Knowledge extracted:
  - Mediterranean Sea
  - 114

### Slide 114: Example: Patterns of evolutionary variation in a protein

- Type: Example / critique
- Application note: This slide is mostly visual or transitional; inspect the original PDF if this example is used in the final report.
- Knowledge extracted:
  - 115
