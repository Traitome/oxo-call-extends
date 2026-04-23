---
name: biopet-scatterregions
category: utility
description: Break reference or BED files into smaller scatter regions
tags: [scatter, regions, parallel-processing]
author: oxo-call-community
source_url: "https://github.com/biopet/scatterregions"
---

## Concepts
- **Tool Overview**: ScatterRegions breaks a reference genome or BED file into smaller regions of equal size for parallel processing in pipelines.
- **Scatter Strategy**: Divides genomic regions into equal-sized chunks for distributed processing.
- **Applications**: Pipeline parallelization, distributed computing, workload balancing.

## Pitfalls
- **Region Boundaries**: Scatter regions may split genes or features at boundaries.

## Examples
### Scatter reference genome
**Args:** `java -jar ScatterRegions.jar -R reference.fa -s 1000000 -o scatter_regions.bed`
**Explanation:** Divides reference into 1Mb scatter regions.
