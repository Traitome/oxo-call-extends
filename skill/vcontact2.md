---
name: vcontact2
category: bioinformatics
description: vContact2 - Viral genome clustering tool.
tags: [vcontact2, viral-genomics, clustering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/vcontact2"
---

## Concepts

- **Tool Overview**: vContact2 - Identifies viral genome clusters.
- **Core Function**: Clusters viral genomes based on protein similarity.
- **Input**: Protein sequences or genome annotations.
- **Output**: Cluster network.
- **Installation**: Install via conda
- **Use Case**: Viral genomics, metagenomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Computation**: May be slow for large datasets.

## Examples

### Cluster viral genomes
**Args:** `vcontact2 --raw-proteins proteins.faa --output-dir results/`
**Explanation:** Cluster viral genomes.

### With options
**Args:** `vcontact2 --raw-proteins proteins.faa --output-dir results/ --cpu 8`
**Explanation:** Use 8 CPUs.
