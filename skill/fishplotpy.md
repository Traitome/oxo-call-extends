---
name: fishplotpy
category: visualization
description: "Fishplotpy is a Python implementation for visualizing clonal evolution dynamics in cancer genomics using fish plots, showing tumor subclones and their relationships over time."
tags: [fishplotpy, visualization, cancer, clonal-evolution, genomics, tumor, clone, bioinformatics, fishplot]
author: oxo-call-community
source_url: "https://github.com/Sayitobar/fishplotpy"
---

## Concepts
- **Tool Overview**: fishplotpy is a Python translation of the R package fishplot by Chris Miller et al. It provides functionality for calculating plot layout for clonal evolution and supports multiple plot shapes (polygon, spline, bezier) with customizable appearance and annotations.
- **Core Function**: Generates publication-ready fish plots that visualize tumor clonal evolution dynamics. Each fish-shaped polygon represents a clonal population, with width indicating relative abundance and position showing temporal relationships.
- **Input Format**: Requires a timepoints dataframe and a parents dataframe. Timepoints: (Id, Timepoint, Population) specifying clone size at each time. Parents: (ParentId, ChildId) defining clonal ancestry relationships.
- **Plot Shapes**: Supports multiple interpolation methods - polygon (linear), spline (smooth curves), and bezier (customizable curves) for different visual styles.
- **Clone Relationships**: Handles branching evolution where clones diverge from ancestors. Supports multiple root clones and extinct clones (populations that shrink to zero).
- **Installation**: `conda install -c bioconda fishplotpy` or `pip install fishplotpy`. Requires Python >=3.9, matplotlib, numpy, pandas, scipy.

## Pitfalls
- **Python 2 Compatibility**: fishplotpy requires Python 3.9+. Do not attempt to use with Python 2.x installations.
- **Population Table Completeness**: All clone IDs must appear in both timepoints and parents dataframes. Missing IDs cause rendering errors.
- **Extinct Clone Handling**: Clones that go extinct (population = 0) must have explicit zero entries at final timepoint to be displayed correctly.
- **Timepoint Ordering**: Timepoints must be logically ordered. Incorrect ordering produces malformed layouts.
- **Parent Chain Validation**: Circular parent relationships are not validated and produce undefined behavior. Ensure directed acyclic graph structure.
- **Figure Size Adjustment**: Default figure sizes may need adjustment for plots with many timepoints or clones. Use figsize parameter to adjust.

## Examples
### Basic fish plot from timepoints and parents
**Args:** `fishplotpy --timepoints timepoints.csv --parents parents.csv --output evolution.png`
**Explanation:** Creates a basic fish plot from CSV files defining clone sizes over time and parent-child relationships. Each clone is rendered as a colored fish shape.

### Python API basic usage
**Args:** `python -c "from fishplotpy import FishPlot; fp = FishPlot(timepoints, parents); fp.save('output.png')"`
**Explanation:** Uses fishplotpy as a Python library. Import FishPlot class, pass pandas DataFrames for timepoints and parents, then save or display the plot.

### Custom timepoint labels
**Args:** `fishplotpy --timepoints timepoints.csv --parents parents.csv --labels "Diagnosis,Primary,Metastasis" --output timeline.png`
**Explanation:** Provides custom labels for timepoints. Useful for clinical data showing disease stages or treatment timepoints.

### Adjust figure dimensions
**Args:** `fishplotpy --timepoints timepoints.csv --parents parents.csv --figsize 12 8 --output wide.png`
**Explanation:** Sets figure width and height in inches. Adjust when plot has many clones or timepoints to improve readability.

### Color scheme customization
**Args:** `fishplotpy --timepoints timepoints.csv --parents parents.csv --colors "#FF0000,#00FF00,#0000FF" --output colored.png`
**Explanation:** Specifies colors for each clone as hex values. Use publication-appropriate color schemes or to highlight specific clones.

### Using spline interpolation
**Args:** `fishplotpy --timepoints timepoints.csv --parents parents.csv --shape spline --output smooth.png`
**Explanation:** Uses spline interpolation for smooth fish shape boundaries instead of straight polygon edges. Produces more polished figures for presentations.

### Extract clone statistics
**Args:** `python -c "from fishplotpy import FishPlot; fp = FishPlot(timepoints, parents); print(fp.get_statistics())"`
**Explanation:** Programmatic access to clone statistics including final frequencies, time of extinction, and branching points. Useful for downstream analysis.

### Export to vector format
**Args:** `fishplotpy --timepoints timepoints.csv --parents parents.csv --format svg --output figure.svg`
**Explanation:** Exports plot in vector SVG format for unlimited scalability in publications. Set format to 'png' for raster output at specific DPI.
