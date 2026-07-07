---
name: dnmtools
category: epigenomics
description: DNMtools - Tools for DNA methylation analysis from bisulfite sequencing data.
tags: [dnmtools, epigenomics, methylation, bisulfite, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/smithlabcode/dnmtools"
---

## Concepts

- **Tool Overview**: DNMtools is a suite of command-line tools for analyzing DNA methylation data from bisulfite sequencing experiments.
- **Core Function**: Provides utilities for processing bisulfite reads, calling methylation states, and analyzing methylation patterns across genomes.
- **Input/Output**: Input: Bisulfite sequencing reads (FASTQ), reference genome (FASTA). Output: Methylation calls (BED/WIG), coverage statistics, differential methylation reports.
- **Algorithm**: Uses Bayesian inference and statistical modeling to distinguish true methylation from sequencing errors.
- **Key Features**: Methylation calling, differential methylation analysis, quality filtering, strand-specific analysis, integration with genome browsers.
- **Installation**: `conda install -c bioconda dnmtools`

## Pitfalls

- **Input Requirements**: Requires properly aligned bisulfite sequencing data; unaligned reads will fail.
- **Strand Bias**: Bisulfite conversion can introduce strand-specific biases that affect methylation calling.
- **Coverage Depth**: Low coverage regions may produce unreliable methylation estimates.
- **Reference Genome**: Must use the same reference genome used for alignment; mismatched references cause errors.
- **Conversion Efficiency**: Incomplete bisulfite conversion can lead to false methylation calls.
- **CpG Islands**: Methylation patterns differ significantly in CpG islands vs non-CpG regions.

## Examples

### Count methylation levels
**Args:** `dnmtools methcounts --input aligned.bam --ref ref.fa --output methylation.bed`
**Explanation:** Counts methylation at each CpG site from aligned bisulfite sequencing data.

### Generate methylation track
**Args:** `dnmtools methcounts --input aligned.bam --ref ref.fa --output methylation.wig --wig`
**Explanation:** Generates a WIG format track for visualization in genome browsers.

### Differential methylation analysis
**Args:** `dnmtools diff --group1 group1.bed --group2 group2.bed --output diff_results.txt`
**Explanation:** Compares methylation levels between two sample groups to identify differentially methylated regions.

### Filter by coverage
**Args:** `dnmtools methcounts --input aligned.bam --ref ref.fa --output filtered.bed --min-cov 10`
**Explanation:** Only includes CpG sites with at least 10x coverage for reliable methylation calls.

### Strand-specific analysis
**Args:** `dnmtools methcounts --input aligned.bam --ref ref.fa --output strand_specific.bed --strand`
**Explanation:** Reports methylation separately for Watson and Crick strands.

### Merge replicates
**Args:** `dnmtools merge --input rep1.bed rep2.bed rep3.bed --output merged.bed`
**Explanation:** Combines methylation data from multiple biological replicates.