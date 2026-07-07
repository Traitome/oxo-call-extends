---
name: motifscan
category: utility
description: A package for motif discovery and motif enrichment analysis.
tags: [motifscan, utility, motif]
author: oxo-call-community
source_url: "http://bioinfo.sibs.ac.cn/shaolab/motifscan/index.php"
---

## Concepts

- **Tool Overview**: motifscan v1.3.0 discovers and analyzes sequence motifs.
- **Core Function**: Identifies motifs and performs enrichment analysis.
- **Motif Discovery**: Finds de novo motifs in sequences.
- **Enrichment Analysis**: Tests for motif enrichment in target regions.
- **Database Integration**: Works with motif databases.
- **Input/Output**: Accepts FASTA sequences; outputs motifs and enrichment results.

## Pitfalls

- **Memory Requirements**: Memory usage depends on sequence size.
- **Parameter Tuning**: May require parameter adjustment for motif discovery.
- **Data Quality**: Results depend on sequence quality.
- **False Positives**: May produce false positive motifs.
- **Computational Resources**: Large datasets may require significant resources.
- **Multiple Testing**: Requires careful correction for multiple comparisons.

## Examples

### Discover motifs
**Args:** `motifscan discover -i sequences.fasta -o motifs.txt`
**Explanation:** Discovers de novo motifs in sequences.

### Enrichment analysis
**Args:** `motifscan enrich -i target.fasta -b background.fasta -m motifs.txt -o enrichment.txt`
**Explanation:** Performs motif enrichment analysis.

### Scan sequences
**Args:** `motifscan scan -i sequences.fasta -m motifs.txt -o matches.txt`
**Explanation:** Scans sequences for motif occurrences.

### With custom parameters
**Args:** `motifscan discover -i sequences.fasta -p params.yaml -o motifs.txt`
**Explanation:** Uses custom discovery parameters.

### Batch processing
**Args:** `motifscan enrich -i targets/ -b background.fasta -m motifs.txt -o results/`
**Explanation:** Processes multiple target files.