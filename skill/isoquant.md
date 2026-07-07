---
name: isoquant
category: expression
description: Reference-based analysis of long RNA reads for gene/transcript quantification and isoform discovery.
tags: [isoquant, expression, long reads, transcriptomics, quantification]
author: oxo-call-community
source_url: "https://ablab.github.io/IsoQuant"
---

## Concepts

- **Reference-Based Analysis**: Aligns long RNA reads to a reference genome for transcript analysis.
- **Transcript Quantification**: Provides accurate gene and transcript-level expression estimates.
- **Isoform Discovery**: Identifies novel transcript isoforms not present in reference annotations.
- **Long Read Optimization**: Specifically designed for Oxford Nanopore and PacBio long-read data.
- **Splice Junction Detection**: Identifies and quantifies alternative splicing events.
- **Comprehensive Output**: Generates multiple output files for downstream analysis.

## Pitfalls

- **Reference Genome Quality**: Poorly annotated reference genomes affect quantification accuracy.
- **Read Mapping Quality**: Inaccurate read mapping leads to incorrect quantification.
- **Computational Resources**: Processing large datasets requires significant computational resources.
- **Memory Requirements**: Memory usage increases with dataset size and genome complexity.
- **Alternative Splicing Complexity**: Highly complex splicing patterns may be undercounted.
- **Parameter Tuning**: Optimal parameters may vary between datasets.

## Examples

### Basic quantification
**Args:** `isoquant --reference genome.fasta --reads reads.fastq --output results/`
**Explanation:** Performs reference-based transcript quantification from long reads.

### With annotation
**Args:** `isoquant --reference genome.fasta --annotation genes.gtf --reads reads.fastq --output results/`
**Explanation:** Uses existing gene annotation to guide quantification.

### Novel isoform discovery
**Args:** `isoquant --reference genome.fasta --reads reads.fastq --discover --output results/`
**Explanation:** Enables novel isoform discovery mode.

### Strand-specific analysis
**Args:** `isoquant --reference genome.fasta --reads reads.fastq --stranded --output results/`
**Explanation:** Performs strand-specific transcript quantification.

### Parallel processing
**Args:** `isoquant --reference genome.fasta --reads reads.fastq --threads 8 --output results/`
**Explanation:** Uses multiple threads for faster processing.

### Generate reports
**Args:** `isoquant --reference genome.fasta --reads reads.fastq --report --output results/`
**Explanation:** Generates comprehensive analysis report.