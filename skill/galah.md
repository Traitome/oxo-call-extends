---
name: galah
category: assembly
description: Galah aims to be a more scalable metagenome assembled genome (MAG) dereplication method.
tags: [galah, metagenome, MAG, dereplication, genome assembly]
author: oxo-call-community
source_url: "https://github.com/wwood/galah"
---

## Concepts
- **MAG Dereplication**: Dereplicates metagenome-assembled genomes.
- **Scalable Method**: Designed for large-scale MAG analysis.
- **Fast Comparison**: Fast genome comparison algorithm.
- **ANIm Support**: Uses Average Nucleotide Identity for comparison.
- **Batch Processing**: Handles large batches of MAGs.

## Pitfalls
- **Memory Usage**: High memory usage for large genome sets.
- **Identity Threshold**: Requires careful selection of identity threshold.
- **Computational Time**: Large batches can take significant time.
- **Quality Dependence**: Results depend on MAG quality.
- **Reference Database**: May need reference genomes for comparison.

## Examples
### Dereplicate MAGs
**Args:** `galah cluster -i genomes/ -o clusters.txt`
**Explanation:** Dereplicates MAGs and outputs cluster assignments.

### Set identity threshold
**Args:** `galah cluster -i genomes/ -i 0.95 -o clusters.txt`
**Explanation:** Uses 95% ANI threshold for dereplication.

### With覆盖率 filter
**Args:** `galah cluster -i genomes/ -c 90 -o clusters.txt`
**Explanation:** Filters by 90% genome coverage.

### Generate report
**Args:** `galah report -i genomes/ -o report.html`
**Explanation:** Generates dereplication report.

### Extract representatives
**Args:** `galah representatives -i genomes/ -c clusters.txt -o reps/`
**Explanation:** Extracts representative genomes from each cluster.