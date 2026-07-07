---
name: moabs
category: epigenomics
description: Methylation analysis on Bisulfite-Sequencing reads.
tags: [moabs, epigenomics, methylation]
author: oxo-call-community
source_url: "https://github.com/sunnyisgalaxy/moabs"
---

## Concepts

- **Tool Overview**: MOABS v1.3.9.6 analyzes methylation from bisulfite sequencing.
- **Core Function**: Calls DNA methylation from bisulfite-treated reads.
- **Bisulfite Sequencing**: Handles BS-seq, RRBS, and WGBS data.
- **Methylation Calling**: Identifies CpG, CHG, and CHH methylation.
- **Input/Output**: Accepts aligned reads; outputs methylation calls.
- **Epigenomics**: Supports DNA methylation analysis workflows.

## Pitfalls

- **Bisulfite Specific**: Designed for bisulfite sequencing data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on bisulfite conversion efficiency.
- **Reference Genome**: Requires appropriate reference genome.
- **Computational Resources**: Large-scale analysis requires significant resources.

## Examples

### Call methylation
**Args:** `moabs -i alignments.bam -g genome.fasta -o methylation.txt`
**Explanation:** Calls methylation from aligned bisulfite reads.

### With quality filtering
**Args:** `moabs -i alignments.bam -g genome.fasta -q -o methylation.txt`
**Explanation:** Applies quality filtering before calling.

### Output in BED format
**Args:** `moabs -i alignments.bam -g genome.fasta -f bed -o methylation.bed`
**Explanation:** Outputs methylation calls in BED format.

### With strand-specific data
**Args:** `moabs -i alignments.bam -g genome.fasta -s -o methylation.txt`
**Explanation:** Handles strand-specific bisulfite data.

### Batch processing
**Args:** `moabs -i bam/ -g genome.fasta -o results/`
**Explanation:** Processes multiple BAM files.