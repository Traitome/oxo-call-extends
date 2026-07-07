---
name: megatron
category: utility
description: MEGATRON - MEGA TRajectories of clONes for analyzing cancer evolution.
tags: [megatron, cancer-genomics, clonal-evolution]
author: oxo-call-community
source_url: "https://github.com/pinellolab/MEGATRON"
---

## Concepts

- **Tool Overview**: MEGATRON analyzes clonal trajectories in cancer.
- **Core Function**: Models clonal evolution from sequencing data.
- **Clonal Tracking**: Tracks clonal populations over time.
- **Phylogenetic Reconstruction**: Builds clonal phylogenies.
- **Copy Number Analysis**: Integrates copy number data.
- **Installation**: `conda install -c bioconda megatron`

## Pitfalls

- **Data Requirements**: Requires multiple time-point samples.
- **Computation Time**: Slow for complex datasets.
- **Memory Requirements**: High memory usage.
- **Parameter Tuning**: Requires careful optimization.
- **Clonal Complexity**: May struggle with highly heterogeneous tumors.
- **Result Interpretation**: Complex output requires expertise.

## Examples

### Analyze clonal trajectories
**Args:** `megatron -i variants.vcf -o trajectories/`
**Explanation:** Analyzes clonal trajectories from variants.

### With copy number
**Args:** `megatron -i variants.vcf -c cnv.txt -o trajectories/`
**Explanation:** Integrates copy number data.

### Plot results
**Args:** `megatron-plot -i trajectories/ -o plot.pdf`
**Explanation:** Visualizes clonal trajectories.

### Verbose mode
**Args:** `megatron -i variants.vcf -v -o trajectories/`
**Explanation:** Shows detailed progress.

### Help documentation
**Args:** `megatron --help`
**Explanation:** Displays available options.
