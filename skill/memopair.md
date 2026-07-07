---
name: memopair
category: epigenomics
description: Identifies methylated motif pairs in genomic sequences.
tags: [memopair, epigenomics, methylation]
author: oxo-call-community
source_url: "https://github.com/SorenHeidelbach/memopair"
---

## Concepts

- **Tool Overview**: MemoPair identifies pairs of methylated motifs.
- **Core Function**: Detects correlated methylated motif pairs.
- **Methylation Analysis**: Analyzes DNA methylation patterns.
- **Motif Correlation**: Identifies co-occurring motifs.
- **Genomic Context**: Considers spatial relationships.
- **Installation**: `conda install -c bioconda memopair`

## Pitfalls

- **Data Requirements**: Requires methylation data.
- **Computation Time**: Slow for large genomes.
- **Memory Requirements**: High memory usage.
- **False Positives**: May detect spurious correlations.
- **Threshold Tuning**: Requires careful parameter adjustment.
- **Motif Database**: Depends on motif definitions.

## Examples

### Identify methylated pairs
**Args:** `memopair -i methylation.bed -o pairs.txt`
**Explanation:** Identifies methylated motif pairs.

### With custom motifs
**Args:** `memopair -i methylation.bed -m motifs.txt -o pairs.txt`
**Explanation:** Uses custom motif definitions.

### Verbose mode
**Args:** `memopair -i methylation.bed -v -o pairs.txt`
**Explanation:** Shows detailed processing information.

### Filter by distance
**Args:** `memopair -i methylation.bed -d 1000 -o pairs.txt`
**Explanation:** Sets maximum distance between pairs.

### Help documentation
**Args:** `memopair --help`
**Explanation:** Displays available options.
