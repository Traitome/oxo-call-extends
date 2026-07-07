---
name: usearch
category: bioinformatics
description: USEARCH - High-performance sequence analysis tool.
tags: [usearch, sequence-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://www.drive5.com/usearch/"
---

## Concepts

- **Tool Overview**: USEARCH - A high-performance sequence analysis tool.
- **Core Function**: Provides various sequence analysis operations.
- **Input**: Sequence files (FASTA/FASTQ).
- **Output**: Analysis results.
- **Installation**: Download from official site
- **Use Case**: Sequence clustering, OTU picking, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Licensing**: Commercial license required for some features.

## Examples

### Cluster sequences
**Args:** `usearch -cluster_fast input.fasta -id 0.97 -centroids clusters.fasta`
**Explanation:** Cluster sequences at 97% identity.

### OTU picking
**Args:** `usearch -unoise3 input.fastq -zotus zotus.fasta`
**Explanation:** Run UNOISE3 for OTU picking.
