---
name: krona
category: visualization
description: Interactive Krona charts for hierarchical data visualization
tags: [krona, visualization, charts, metagenomics, taxonomy, HTML-visualization]
author: oxo-call-community
source_url: "https://github.com/marbl/Krona"
---

## Concepts

- **Hierarchical Charts**: Creates interactive hierarchical pie charts
- **Taxonomic Visualization**: Visualizes taxonomic classification data
- **HTML Output**: Generates interactive HTML visualizations
- **Multi-source Data**: Imports from various bioinformatics tools
- **Zoomable Interface**: Allows drilling down into hierarchical data
- **Self-contained HTML**: Charts are fully contained in HTML files

## Pitfalls

- **Data Format**: Requires specific input format for import
- **Large Datasets**: Very large datasets create complex visualizations
- **Browser Compatibility**: Some browsers struggle with large charts
- **Missing Values**: Missing data may cause visualization issues
- **Depth Limitations**: Very deep hierarchies become hard to navigate
- **Color Assignment**: Color assignment may not be optimal

## Examples

### Create Krona chart
**Args:** `ktImportTaxonomy -o chart.html taxonomy.txt`
**Explanation:** Creates interactive Krona chart from taxonomy file.

### From Kraken output
**Args:** `ktImportTaxonomy -o krona.html kraken_report.txt`
**Explanation:** Creates chart directly from Kraken report.

### Multiple samples
**Args:** `ktImportTaxonomy -o combined.html sample1.txt sample2.txt sample3.txt`
**Explanation:** Combines multiple samples in single chart.

### From XML
**Args:** `ktImportXML -o chart.xml taxonomy.xml`
**Explanation:** Creates chart from XML taxonomy data.

### Specify taxonomy levels
**Args:** `ktImportTaxonomy -o chart.html --level genus taxonomy.txt`
**Explanation:** Shows only genus level and above.

### Batch creation
**Args:** `ktImportTaxonomy batch -d reports/ -o charts/`
**Explanation:** Creates multiple Krona charts from directory.