---
name: gqlib
category: bioinformatics
description: gqlib is a gene quantification library for analyzing gene expression levels from sequencing data.
tags: [gqlib, gene-quantification, RNA-seq, expression, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cschu/gqlib"
---

## Concepts

- **Gene Quantification**: gqlib calculates gene expression levels from RNA-seq and other sequencing data.

- **Multiple Input Formats**: Supports various input formats including BAM, SAM, and FASTQ.

- **Expression Metrics**: Calculates different expression metrics including raw counts, RPKM, FPKM, and TPM.

- **Strand-Specific Analysis**: Handles strand-specific RNA-seq data for accurate quantification.

- **Splicing Awareness**: Accounts for alternative splicing events when quantifying gene expression.

- **Quality Control**: Provides metrics for assessing quantification quality and reproducibility.

## Pitfalls

- **Alignment Quality**: Results depend heavily on alignment quality. Use high-quality alignments.

- **Annotation Version**: Ensure annotation files match the reference genome used for alignment.

- **Read Length**: Short reads may affect quantification accuracy. Consider read length when interpreting results.

- **Multimapping Reads**: Multimapping reads can affect quantification. Use appropriate strategies for handling them.

- **Memory Usage**: Processing large datasets may require significant memory. Consider downsampling when necessary.

## Examples

### Basic gene quantification
**Args:** `gqlib quantify -i alignments.bam -a annotations.gtf -o expression.txt`
**Explanation:** Quantifies gene expression from aligned reads using gene annotations.

### Calculate TPM
**Args:** `gqlib quantify -i alignments.bam -a annotations.gtf -m TPM -o tpm.txt`
**Explanation:** Calculates expression in Transcripts Per Million (TPM) units.

### Strand-specific analysis
**Args:** `gqlib quantify -i alignments.bam -a annotations.gtf -s forward -o expression.txt`
**Explanation:** Performs strand-specific quantification for forward-stranded libraries.

### Filter low-expression genes
**Args:** `gqlib filter -i expression.txt -c 1 -o filtered.txt`
**Explanation:** Filters out genes with fewer than 1 count across all samples.

### Batch processing
**Args:** `gqlib batch -d samples/ -a annotations.gtf -o results/`
**Explanation:** Processes multiple BAM files in a directory.

### Generate QC report
**Args:** `gqlib qc -i alignments.bam -a annotations.gtf -o qc_report.txt`
**Explanation:** Generates a quality control report for the quantification.

### Visualize expression distribution
**Args:** `gqlib plot -i expression.txt -o distribution.png`
**Explanation:** Creates a visualization of expression level distribution.