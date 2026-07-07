---
name: cenplot
category: visualization
description: Centromere plotting library for visualizing centromere annotations
tags: [cenplot, centromere, visualization, plotting, genomics]
author: oxo-call-community
source_url: "https://github.com/logsdon-lab/CenPlot"
---

## Concepts

- **Tool Overview**: CenPlot is a Python library for visualizing centromere annotations and related genomic features.
- **Core Function**: Generates visualizations of centromeric regions in genome assemblies.
- **Features**: Centromere annotation plotting, sequence feature visualization, and comparative analysis.
- **Input**: Centromere annotations (GFF/BED) and genome sequence data.
- **Output**: Publication-quality plots and figures.
- **Application**: Visualizing centromere structure in genome assemblies.
- **Installation**: Install via bioconda: `conda install -c bioconda cenplot`

## Pitfalls

- **Annotation Format**: Requires properly formatted centromere annotations.
- **Genome Coordinates**: Ensure coordinate systems match between annotations and sequences.
- **Plot Customization**: May require Python scripting for full customization.
- **Large Regions**: Very large centromeres may need simplified visualization.

## Examples

### Basic centromere plot
**Args:** `python -c "import cenplot; cenplot.plot_centromere('annotations.gff', 'genome.fasta')"`
**Explanation:** Creates basic centromere visualization.

### Plot with custom colors
**Args:** `python -c "cenplot.plot_centromere('annotations.gff', colors={'satellite': 'red', 'gap': 'gray'})"`
**Explanation:** Uses custom color scheme for different features.

### Comparative plot
**Args:** `python -c "cenplot.compare_centromeres('species1.gff', 'species2.gff')"`
**Explanation:** Compares centromere structures between species.

### Display help
**Args:** `python -c "help(cenplot)"`
**Explanation:** Shows available functions and documentation.