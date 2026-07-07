---
name: difcover
category: qc
description: DifCover - Differential coverage analysis pipeline for genomic regions.
tags: [difcover, qc, coverage, differential, cnv]
author: oxo-call-community
source_url: "https://github.com/timnat/DifCover"
---

## Concepts

- **Tool Overview**: difcover (v3.0.1+) is a pipeline for identifying genomic regions with differential read coverage between sample pairs.
- **Core Function**: Detects coverage differences that may indicate copy number variations (CNVs) or other structural changes between samples.
- **Input/Output**: Input: BAM files with aligned reads. Output: Genomic regions with significant coverage differences, statistics.
- **Algorithm**: Uses statistical methods to compare read coverage across genomic intervals between samples.
- **Key Features**: Coverage comparison, CNV detection, statistical significance testing, visualization, batch processing.
- **Installation**: `conda install -c bioconda difcover`

## Pitfalls

- **Input Requirements**: Requires properly indexed BAM files with consistent read groups.
- **Sequencing Depth**: Requires sufficient sequencing depth for reliable coverage comparison.
- **Normalization**: Coverage differences may reflect sequencing depth variations rather than true CNVs.
- **GC Bias**: GC content differences can affect coverage normalization.
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Compare coverage between samples
**Args:** `difcover --sample1 a.bam --sample2 b.bam --output diff_regions.bed`
**Explanation:** Identifies regions with differential coverage between two samples.

### With multiple sample pairs
**Args:** `difcover --pairs pairs.tsv --output diff_regions.bed`
**Explanation:** Process multiple sample pairs from TSV file.

### Set significance threshold
**Args:** `difcover --sample1 a.bam --sample2 b.bam --output diff_regions.bed --fdr 0.01`
**Explanation:** Set FDR threshold for calling significant regions.

### Generate coverage plots
**Args:** `difcover --sample1 a.bam --sample2 b.bam --output diff_regions.bed --plot coverage.png`
**Explanation:** Generate visualization of coverage differences.

### Using interval file
**Args:** `difcover --sample1 a.bam --sample2 b.bam --intervals regions.bed --output diff_regions.bed`
**Explanation:** Restrict analysis to specific genomic intervals.