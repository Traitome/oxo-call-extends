---
name: express
category: expression
description: "eXpress is a streaming DNA/RNA sequence quantification tool."
tags: [express, expression, RNA-seq, quantification, gene-expression]
author: oxo-call-community
source_url: "http://bio.math.berkeley.edu/eXpress/"
---

## Concepts

- **Tool Overview**: eXpress is a streaming DNA/RNA sequence quantification tool that efficiently estimates transcript abundances from sequencing data.
- **Core Function**: Quantifies gene and transcript expression levels from RNA-seq data using a streaming algorithm.
- **Input/Output**: Input: Aligned reads (BAM/SAM), reference transcripts (FASTA). Output: Expression estimates (FPKM/RPKM), abundance files.
- **Algorithm**: Uses an expectation-maximization algorithm for transcript quantification with streaming processing.
- **Key Features**: Streaming processing, efficient memory usage, support for paired-end reads, multi-mapping reads handling, expression normalization.
- **Installation**: `conda install -c bioconda express`

## Pitfalls

- **Alignment Quality**: Results depend on high-quality aligned reads.
- **Reference Transcripts**: Requires comprehensive transcript annotation.
- **Multi-mapping Reads**: May assign reads ambiguously to multiple transcripts.
- **Memory Management**: Large datasets may require tuning memory parameters.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic expression quantification
**Args:** `express transcripts.fasta alignments.bam -o results/`
**Explanation:** Quantifies transcript expression from aligned reads.

### With paired-end reads
**Args:** `express transcripts.fasta alignments.bam --paired-end -o results/`
**Explanation:** Processes paired-end sequencing data.

### FPKM output
**Args:** `express transcripts.fasta alignments.bam --fpkm -o results/`
**Explanation:** Outputs expression in FPKM units.

### With custom normalization
**Args:** `express transcripts.fasta alignments.bam --normalize -o results/`
**Explanation:** Applies normalization to expression values.

### Batch processing
**Args:** `express transcripts.fasta alignments/ -o results/ --batch`
**Explanation:** Processes multiple alignment files in batch mode.