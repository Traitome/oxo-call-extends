---
name: starseqr
category: variant-calling
description: RNA Fusion Detection and Quantification.
tags: [starseqr, rna-seq, fusion-detection, cancer]
author: oxo-call-community
source_url: "https://github.com/ExpressionAnalysis/STAR-SEQR"
---

## Concepts

- **Tool Overview**: starseqr (v0.6.7) is a comprehensive tool for detecting and quantifying gene fusions from RNA-seq data.
- **Core Function**: Identifies fusion transcripts and provides expression quantification for both fusion partners.
- **Algorithm**: Uses STAR alignment combined with custom filtering to detect chimeric reads and quantify fusion expression.
- **Input/Output**: Input: FASTQ reads or BAM file; Output: Fusion calls with supporting read counts and confidence scores.
- **Quantification**: Provides both junction read counts and spanning fragment counts for accurate expression estimation.
- **Installation**: `conda install -c bioconda starseqr` or download from GitHub.

## Pitfalls

- **Alignment Quality**: Poor alignment affects fusion detection accuracy.
- **Read Coverage**: Low coverage at fusion breakpoints may miss true fusions.
- **False Positives**: Transcriptional artifacts can produce false positive calls.
- **Memory Requirements**: Large datasets require significant memory for processing.
- **Version Compatibility**: Requires specific STAR version for optimal performance.
- **Filtering Parameters**: Incorrect thresholds affect sensitivity/specificity.

## Examples

### Display help
**Args:** `starseqr --help`
**Explanation:** Shows available options and usage information.

### Basic fusion detection
**Args:** `starseqr -1 read1.fastq -2 read2.fastq -o results/ -g genome.fasta -a annotation.gtf`
**Explanation:** Detect and quantify fusions from paired-end RNA-seq reads.

### With pre-aligned BAM
**Args:** `starseqr -b aligned.bam -o results/ -g genome.fasta -a annotation.gtf`
**Explanation:** Process pre-aligned BAM file for fusion detection.

### Quantification only
**Args:** `starseqr -b aligned.bam -o results/ -g genome.fasta -a annotation.gtf --quant-only`
**Explanation:** Perform only quantification without fusion calling.

### Custom filters
**Args:** `starseqr -1 read1.fastq -2 read2.fastq -o results/ -g genome.fasta -a annotation.gtf -c 0.8`
**Explanation:** Set minimum confidence threshold to 0.8.

### Verbose mode
**Args:** `starseqr -1 read1.fastq -2 read2.fastq -o results/ -g genome.fasta -a annotation.gtf -v`
**Explanation:** Run with detailed logging for debugging.

### Output VCF
**Args:** `starseqr -1 read1.fastq -2 read2.fastq -o results/ -g genome.fasta -a annotation.gtf --vcf`
**Explanation:** Output fusion calls in VCF format.

### Batch processing
**Args:** `starseqr --batch samples.txt -o results/ -g genome.fasta -a annotation.gtf`
**Explanation:** Process multiple samples from batch file.

### Generate report
**Args:** `starseqr -1 read1.fastq -2 read2.fastq -o results/ -g genome.fasta -a annotation.gtf --report`
**Explanation:** Generate HTML report with fusion analysis results.
