---
name: shiba2sashimi
category: utility
description: shiba2sashimi - Sashimi plot generation from Shiba output
tags: ["shiba2sashimi", "utility", "visualization", "sashimi-plot"]
author: oxo-call-community
source_url: "https://github.com/Sika-Zheng-Lab/shiba2sashimi"
---

## Concepts

- **Tool Overview**: shiba2sashimi (v0.1.7) creates sashimi plots from Shiba output.
- **Core Function**: Generates visualizations of alternative splicing events.
- **Algorithm**: Processes splicing data and generates publication-quality plots.
- **Input/Output**: Accepts Shiba output and produces sashimi plots.
- **Visualization**: Focuses on RNA splicing visualization.
- **Applications**: RNA-seq analysis, alternative splicing studies, and publication figures.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Format**: Requires correct Shiba output format.
- **Parameter Tuning**: Requires careful adjustment for optimal visualization.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **Dependency**: Requires Shiba output as input.

## Examples

### Generate sashimi plot
**Args:** `shiba2sashimi -i shiba_output.txt -o plot.pdf`
**Explanation:** `-i` input Shiba output; `-o` output plot.

### With gene name
**Args:** `shiba2sashimi -i shiba_output.txt -g MY_GENE -o plot.pdf`
**Explanation:** `-g` gene name to plot.

### Verbose logging
**Args:** `shiba2sashimi -v -i shiba_output.txt -o plot.pdf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shiba2sashimi --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shiba2sashimi --version`
**Explanation:** Shows current version.

### High resolution
**Args:** `shiba2sashimi -i shiba_output.txt -o plot.pdf -r 300`
**Explanation:** `-r 300` sets 300 DPI resolution.

### Custom colors
**Args:** `shiba2sashimi -i shiba_output.txt -o plot.pdf -c colors.txt`
**Explanation:** `-c` custom color configuration.