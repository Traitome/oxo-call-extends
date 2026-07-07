---
name: vcontact3
category: bioinformatics
description: vContact3 - Viral genome clustering tool.
tags: [vcontact3, viral-genomics, clustering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/vcontact3"
---

## Concepts

- **Tool Overview**: vContact3 - Updated viral genome clustering tool.
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
**Args:** `vcontact3 --input proteins.faa --output-dir results/`
**Explanation:** Cluster viral genomes.

### With options
**Args:** `vcontact3 --input proteins.faa --output-dir results/ --threads 8`
**Explanation:** Use 8 threads.
