---
name: go-figure
category: visualization
description: GO-Figure! generates visualizations of Gene Ontology term enrichment results for exploratory data analysis.
tags: [go-figure, GO, visualization, gene-ontology, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/evogenlab/GO-Figure"
---

## Concepts

- **GO Term Visualization**: GO-Figure! creates informative visualizations of GO term enrichment results, facilitating exploratory data analysis.

- **Multiple Dataset Comparison**: Supports comparison of enrichment results across multiple datasets, highlighting common and unique GO terms.

- **Interactive Plots**: Generates interactive visualizations that allow users to explore GO term relationships and significance levels.

- **GO Hierarchy Display**: Visualizes the hierarchical relationships between enriched GO terms, showing parent-child relationships.

- **Customizable Output**: Provides options for customizing plot appearance, including colors, fonts, and layout.

- **Publication-Quality Figures**: Generates high-quality figures suitable for publication in scientific journals.

## Pitfalls

- **Input Format**: Ensure input files follow the required format. Incorrectly formatted input can cause parsing errors.

- **GO Term Overlap**: Highly similar GO terms may clutter visualizations. Consider filtering or grouping related terms.

- **Visual Complexity**: Too many GO terms can make plots difficult to interpret. Focus on the most significant terms.

- **Color Blindness**: Default color schemes may not be accessible to color-blind users. Use color-blind friendly palettes when necessary.

- **Figure Resolution**: Export figures at appropriate resolutions for your intended use. Low-resolution figures may be unsuitable for publication.

## Examples

### Basic GO term visualization
**Args:** `go-figure -i enrichment_results.txt -o go_figure.png`
**Explanation:** Generates a visualization of GO enrichment results and saves it as a PNG image.

### Compare multiple datasets
**Args:** `go-figure -i dataset1.txt dataset2.txt dataset3.txt -o comparison.png`
**Explanation:** Creates a comparative visualization of enrichment results from three datasets.

### Show GO hierarchy
**Args:** `go-figure -i results.txt --hierarchy -o hierarchy.png`
**Explanation:** Visualizes the hierarchical relationships between enriched GO terms.

### Customize colors
**Args:** `go-figure -i results.txt -c viridis -o colored.png`
**Explanation:** Uses the viridis color palette for the visualization instead of the default.

### Generate interactive HTML
**Args:** `go-figure -i results.txt --interactive -o interactive.html`
**Explanation:** Creates an interactive HTML visualization that can be explored in a web browser.

### Filter by significance
**Args:** `go-figure -i results.txt -p 0.05 -o filtered.png`
**Explanation:** Only includes GO terms with p-values below 0.05 in the visualization.

### Adjust figure size
**Args:** `go-figure -i results.txt --width 10 --height 8 -o large.png`
**Explanation:** Generates a larger figure with specified dimensions (in inches).