---
name: itol-config
category: visualization
description: Tool to create iTOL (Interactive Tree of Life) configuration files for tree annotations.
tags: [itol-config, visualization, phylogenetics, tree annotation]
author: oxo-call-community
source_url: "https://jodyphelan.github.io/itol-config/"
---

## Concepts

- **Configuration Generation**: Creates iTOL configuration files for tree annotations.
- **Annotation Types**: Supports multiple annotation types (color strips, heatmaps, labels).
- **Color Schemes**: Provides predefined color schemes for annotations.
- **Batch Processing**: Generates multiple configuration files from input data.
- **Template Support**: Uses templates for consistent annotation formatting.
- **Output Formats**: Generates iTOL-compatible configuration files.

## Pitfalls

- **Input Format**: Requires specific input data format for annotations.
- **Configuration Complexity**: Complex annotations require careful configuration.
- **Color Selection**: Poor color choices can affect visualization readability.
- **File Compatibility**: Configuration files must match iTOL format exactly.
- **Tree Structure**: Annotations must match tree node labels exactly.
- **Documentation**: Requires understanding of iTOL annotation syntax.

## Examples

### Generate color strip config
**Args:** `itol-config colorstrip --input metadata.csv --output colorstrip.txt`
**Explanation:** Generates color strip annotation configuration from metadata.

### Generate heatmap config
**Args:** `itol-config heatmap --input expression.csv --output heatmap.txt`
**Explanation:** Creates heatmap annotation configuration for expression data.

### With custom colors
**Args:** `itol-config colorstrip --input metadata.csv --colors custom_colors.txt --output colorstrip.txt`
**Explanation:** Uses custom color scheme for annotations.

### Batch processing
**Args:** `itol-config batch --input-dir data/ --output-dir configs/`
**Explanation:** Processes multiple input files and generates configuration files.

### Preview configuration
**Args:** `itol-config preview --input config.txt --output preview.png`
**Explanation:** Generates preview of annotation configuration.

### Validate configuration
**Args:** `itol-config validate --input config.txt`
**Explanation:** Validates configuration file syntax and format.