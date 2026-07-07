---
name: nanoplotter
category: qc
description: NanoPlotter - Plotting functions for Oxford Nanopore sequencing data
tags: [nanoplotter, qc, nanopore, plotting, visualization, library]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanoplotter"
---

## Concepts

- **Tool Overview**: NanoPlotter v1.10.0 is a Python library providing plotting utilities for Oxford Nanopore sequencing data visualization. It is used internally by NanoPack tools.
- **Core Function**: Provides reusable plotting functions for generating quality control plots, including read length distributions, quality score histograms, and mapping statistics.
- **Algorithm**: Uses matplotlib and seaborn for generating publication-quality visualizations. Supports multiple plot types and customization options.
- **Input Format**: Accepts pandas DataFrames or numpy arrays containing sequencing statistics. Designed as a library module.
- **Output**: Produces matplotlib figures and axes objects that can be further customized or saved to file.
- **Use Case**: Used as a dependency by other NanoPack tools (NanoPlot, NanoComp) and can be imported into custom Python scripts for custom visualization.

## Pitfalls

- **Library Only**: Primarily designed as a Python library, not a standalone command-line tool.
- **Version Compatibility**: Ensure compatibility with dependent tools. API changes may affect downstream tools.
- **Matplotlib Versions**: Plotting behavior may vary with different matplotlib versions.
- **Memory Usage**: Generating many plots simultaneously may require careful memory management.
- **Customization**: Requires Python knowledge for advanced customization. Basic users should use NanoPlot directly.
- **Documentation**: Limited standalone documentation. Refer to source code for detailed usage.

## Examples

### Import and use in Python
**Args:** `from nanoplotter import plot_length_distribution`
**Explanation:** Import plotting function from NanoPlotter.

### Generate length distribution plot
**Args:** `fig, ax = plot_length_distribution(lengths, title="Read Lengths")`
**Explanation:** Creates a read length distribution plot.

### Save plot to file
**Args:** `fig.savefig("length_dist.png", dpi=300)`
**Explanation:** Saves generated plot to PNG file.

### Customize plot appearance
**Args:** `fig, ax = plot_quality_distribution(qualities, color="blue", bins=50)`
**Explanation:** Creates quality distribution plot with custom color and bins.

### Display help
**Args:** `python -c "import nanoplotter; help(nanoplotter)"`
**Explanation:** Shows available plotting functions and their documentation.
