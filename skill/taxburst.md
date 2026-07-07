---
name: taxburst
category: visualization
description: Creates sunburst plots for taxonomic data.
tags: [taxburst, visualization, taxonomy, sunburst]
author: oxo-call-community
source_url: "https://github.com/taxburst/taxburst"
---

## Concepts

- **Tool Overview**: taxburst (v0.3.2) creates sunburst visualizations.
- **Core Function**: Generates interactive sunburst charts from taxonomy.
- **Algorithm**: Hierarchical taxonomy visualization.
- **Input/Output**: Input: Taxonomy profiles; Output: HTML/SVG plots.
- **Applications**: Taxonomic visualization, metagenomics presentation.
- **Installation**: `conda install -c bioconda taxburst` or npm install.

## Pitfalls

- **Data Format**: Requires specific input format.
- **Large Datasets**: Too many taxa clutter visualization.
- **Browser Compatibility**: Interactive features need modern browser.
- **Color Scheme**: Colors may not distinguish all taxa.
- **Performance**: Large datasets slow rendering.
- **Export Formats**: Limited export options.

## Examples

### Display help
**Args:** `taxburst --help`
**Explanation:** Shows available options and usage information.

### Basic visualization
**Args:** `taxburst -i taxonomy.txt -o sunburst.html`
**Explanation:** Create sunburst plot from taxonomy.

### With taxonomy levels
**Args:** `taxburst -i taxonomy.txt -o sunburst.html -l 5`
**Explanation:** Show 5 taxonomy levels.

### Verbose mode
**Args:** `taxburst -i taxonomy.txt -o sunburst.html -v`
**Explanation:** Run with detailed logging.

### Output statistics
**Args:** `taxburst -i taxonomy.txt -o sunburst.html --stats`
**Explanation:** Generate statistics about plot.

### Batch processing
**Args:** `for f in taxonomy/*.txt; do taxburst -i $f -o plots/${f%.txt}.html; done`
**Explanation:** Create multiple plots.

### Custom colors
**Args:** `taxburst -i taxonomy.txt -o sunburst.html -c mycolors.json`
**Explanation:** Use custom color scheme.

### Generate SVG
**Args:** `taxburst -i taxonomy.txt -o sunburst.svg`
**Explanation:** Export as SVG format.

### Interactive mode
**Args:** `taxburst -i taxonomy.txt -o sunburst.html --interactive`
**Explanation:** Enable interactive features.
