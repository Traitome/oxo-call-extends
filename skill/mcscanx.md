---
name: mcscanx
category: utility
description: Multiple Collinearity Scan toolkit for analyzing synteny and collinearity across genomes.
tags: [mcscanx, synteny, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/wyp1125/MCScanX"
---

## Concepts

- **Tool Overview**: MCScanX analyzes collinearity and synteny between genomes.
- **Core Function**: Identifies syntenic blocks and collinear regions.
- **Synteny Detection**: Finds conserved gene order across species.
- **Collinearity Analysis**: Analyzes linear gene arrangements.
- **Duplication Detection**: Identifies segmental and tandem duplications.
- **Installation**: `conda install -c bioconda mcscanx`

## Pitfalls

- **Genome Quality**: Requires well-annotated genomes.
- **Gene Annotation**: Depends on accurate gene annotations.
- **Memory Requirements**: High memory for large genomes.
- **Computation Time**: Slow for multiple large genomes.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **Output Interpretation**: Results require biological interpretation.

## Examples

### Run MCScanX
**Args:** `MCScanX input`
**Explanation:** Runs collinearity analysis on input files.

### With multiple species
**Args:** `MCScanX multi_species_input`
**Explanation:** Analyzes collinearity across multiple species.

### Visualize results
**Args:** `draw_linear_plot -i input.collinearity -o plot.png`
**Explanation:** Generates linear visualization.

### Duplication analysis
**Args:** `MCScanX -d input`
**Explanation:** Focuses on duplication detection.

### Help documentation
**Args:** `MCScanX -h`
**Explanation:** Displays available options.
