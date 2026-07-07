---
name: codoff
category: assembly
description: Measure the irregularity of codon usage for a genomic region relative to the full genome
tags: [codoff, codon-usage, genome-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/Kalan-Lab/codoff/blob/v1.2.3/README.md"
---

## Concepts

- **Tool Overview**: codoff is a tool for measuring the irregularity of codon usage in specific genomic regions (such as biosynthetic gene clusters, phage regions, etc.) relative to the entire genome.
- **Core Function**: Quantifies deviations in codon usage patterns between a specific genomic region and the whole genome background.
- **Algorithm**: Uses statistical methods to compare codon usage frequencies between target region and reference genome.
- **Input**: Genome sequence in FASTA format with optional region coordinates.
- **Output**: Codon usage irregularity scores and statistical metrics.
- **Application**: Detecting horizontally transferred genes, identifying genomic islands, and analyzing biosynthetic gene clusters.
- **Installation**: Install via bioconda: `conda install -c bioconda codoff`

## Pitfalls

- **Region Size**: Small regions may produce unreliable statistics.
- **Genome Quality**: Requires complete, high-quality genome sequence.
- **Codon Table**: Must use correct codon table for the organism.
- **GC Content**: Differences in GC content can affect codon usage patterns.
- **Statistical Significance**: Results should be interpreted with statistical caution.

## Examples

### Analyze codon usage irregularity
**Args:** `codoff -g genome.fasta -r region.bed -o results.txt`
**Explanation:** Measures codon usage irregularity for specified genomic region.

### With custom window size
**Args:** `codoff -g genome.fasta -r region.bed -w 1000 -o results.txt`
**Explanation:** Uses 1000bp sliding window for analysis.

### Compare multiple regions
**Args:** `codoff -g genome.fasta -r regions.bed -o results.txt`
**Explanation:** Analyzes multiple genomic regions from BED file.

### Display help
**Args:** `codoff --help`
**Explanation:** Shows all available options and usage information.