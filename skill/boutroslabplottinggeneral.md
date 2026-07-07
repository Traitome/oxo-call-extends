---
name: boutroslabplottinggeneral
category: visualization
description: R package for general plotting functions from the Boutros Lab
tags: [boutroslab, r-package, visualization, plotting]
author: oxo-call-community
source_url: "https://labs.oicr.on.ca/boutros-lab/software/bpg"
---

## Concepts

- **Tool Overview**: BoutrosLabPlottingGeneral is an R package providing general plotting functions for bioinformatics data visualization.
- **Core Function**: Provides a suite of plotting functions for creating publication-quality graphs.
- **Features**: Custom themes, color palettes, and specialized plots for genomic data.
- **Application**: Bioinformatics data visualization, publication figure generation.
- **Installation**: Install via bioconda: `conda install -c bioconda boutroslabplottinggeneral`

## Pitfalls

- **R Package**: Requires R environment; not a command-line tool.
- **Dependencies**: May require other Boutros Lab packages for full functionality.
- **Version Compatibility**: Ensure compatibility with R version and other packages.

## Examples

### Load package and create plot
**Args:** `library(BoutrosLabPlottingGeneral); create.barplot(data)`
**Explanation:** Loads the package and creates a bar plot from data.

### Set custom theme
**Args:** `set.BoutrosLab.theme()`
**Explanation:** Applies the Boutros Lab custom plotting theme.