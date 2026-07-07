---
name: vclust
category: bioinformatics
description: vclust - Variant clustering tool.
tags: [vclust, vcf-processing, clustering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vclust/"
---

## Concepts

- **Tool Overview**: vclust - Clusters variants based on similarity.
- **Core Function**: Groups variants into clusters.
- **Input**: VCF file.
- **Output**: Cluster assignments.
- **Installation**: Install via pip or conda
- **Use Case**: Variant clustering, population genetics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Parameters**: Requires careful parameter tuning.

## Examples

### Cluster variants
**Args:** `vclust -i input.vcf -o clusters.txt`
**Explanation:** Cluster variants.

### With options
**Args:** `vclust -i input.vcf -o clusters.txt -k 5`
**Explanation:** Use 5 clusters.
