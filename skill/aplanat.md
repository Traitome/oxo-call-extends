---
name: aplanat
category: visualization
description: Bokeh plotting API with bioinformatics-focused extras for creating interactive visualizations
tags: [aplanat, bokeh, visualization, plotting, bioinformatics, interactive]
author: oxo-call-community
source_url: "https://github.com/epi2me-labs/aplanat"
---

## Concepts

- **Tool Overview**: aplanat (v0.6.15) - A Python library providing wrappers around the Bokeh library to simplify plotting of common bioinformatics visualizations, with focus on Jupyter notebook environments.
- **Core Function**: Simplifies creation of interactive plots for bioinformatics data analysis with minimal boilerplate code.
- **Key Features**:
  - Wrapper functions for common plot types (histograms, scatter plots, line charts, heatmaps)
  - Built-in support for bioinformatics data visualization
  - Interactive features (panning, zooming, tooltips, data highlighting)
  - Inline display in JupyterLab notebooks
  - Export to standalone HTML documents
  - Support for large datasets with high-performance rendering
- **Applications**: 
  - Sequencing data visualization
  - Genome analysis plots
  - Variant calling results
  - Epigenomics data visualization
  - Interactive data exploration in notebooks
- **Installation**: `conda install -c epi2melabs aplanat` or `pip install aplanat`

## Pitfalls

- **Bokeh Dependency**: Requires Bokeh library; version compatibility should be checked
- **Jupyter Environment**: Best suited for JupyterLab notebooks; may have limited functionality in other environments
- **Interactive Features**: Some features require JavaScript-enabled environment
- **Learning Curve**: Requires understanding of Bokeh for advanced customization
- **Performance**: Very large datasets may require downsampling for smooth interactivity

## Examples

### Create a histogram
**Args:** `aplanat.plot.histogram(data, title="Coverage Distribution", x_axis_label="Coverage", y_axis_label="Count")`
**Explanation:** Creates an interactive histogram with the specified data and labels.

### Create a scatter plot
**Args:** `aplanat.plot.scatter(x_data, y_data, color="blue", title="Read Length vs Quality")`
**Explanation:** Generates an interactive scatter plot with customizable color and title.

### Generate a heatmap
**Args:** `aplanat.plot.heatmap(matrix_data, x_labels, y_labels, title="Variant Density")`
**Explanation:** Creates an interactive heatmap with labeled axes.

### Create a line plot
**Args:** `aplanat.plot.line(x_data, y_data, line_width=2, color="red", title="Depth Profile")`
**Explanation:** Generates an interactive line plot with specified styling.

### Combine multiple plots
**Args:** `aplanat.layout.grid([plot1, plot2, plot3, plot4], ncols=2)`
**Explanation:** Arranges multiple plots in a grid layout with 2 columns.