---
name: get_pangenes
category: pan-genomics
description: get_pangenes - A versatile software package for calling pangenes from whole genome alignments.
tags: [get_pangenes, pan-genomics, pangenes, genome-alignment]
author: oxo-call-community
source_url: "https://github.com/Ensembl/plant-scripts/tree/master/pangenes"
---

## Concepts
- **Pangene Calling**: Calls pangenes from genome alignments.
- **Pan-genome Analysis**: Analyzes pan-genome content.
- **Gene Family**: Identifies gene families across species.
- **Synteny Analysis**: Analyzes syntenic relationships.
- **Comparative Genomics**: Compares multiple genomes.

## Pitfalls
- **Alignment Quality**: Requires high-quality genome alignments.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Computational Resources**: Large datasets require resources.
- **Memory Usage**: May require significant memory.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Call pangenes
**Args:** `get_pangenes -i alignment.maf -g genes.gff -o pangenes.txt`
**Explanation:** Calls pangenes from MAF alignment.

### With options
**Args:** `get_pangenes -i alignment.maf -g genes.gff -t 0.8 -o pangenes.txt`
**Explanation:** Uses 80% identity threshold.

### Batch processing
**Args:** `get_pangenes -l alignments.txt -g genes.gff -o ./results/`
**Explanation:** Processes multiple alignments.

### Generate report
**Args:** `get_pangenes -i alignment.maf -g genes.gff -r -o report.html`
**Explanation:** Generates pangene analysis report.

### Visualize results
**Args:** `get_pangenes -i alignment.maf -g genes.gff -v -o visualization.png`
**Explanation:** Visualizes pangene relationships.