---
name: clearcnv
category: variant-calling
description: CNV calling package for copy number variation detection
tags: [clearcnv, cnv, copy-number, variant-calling, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bihealth/clear-cnv"
---

## Concepts

- **Tool Overview**: clearCNV is a comprehensive CNV (Copy Number Variation) calling package for detecting copy number changes from sequencing data.
- **Core Function**: Identifies copy number variations from aligned sequencing reads or array data.
- **Algorithm**: Uses statistical methods to detect copy number changes based on read depth and other signals.
- **Input**: Aligned BAM files, VCF files, or array data.
- **Output**: CNV calls with genomic coordinates and copy number estimates.
- **Application**: Copy number variation analysis, cancer genomics, and genetic disease research.
- **Installation**: Install via bioconda: `conda install -c bioconda clearcnv`

## Pitfalls

- **Data Quality**: Requires high-quality sequencing data for accurate CNV calling.
- **Coverage Uniformity**: Depends on uniform sequencing coverage.
- **Reference Genome**: Must match the reference used for alignment.
- **Segmentation Parameters**: May require parameter adjustment for optimal results.
- **False Positives**: May detect false CNVs from technical artifacts.

## Examples

### Call CNVs from BAM
**Args:** `clearcnv -i alignments.bam -r reference.fasta -o cnv_calls.vcf`
**Explanation:** Calls copy number variations from aligned BAM file.

### With segmentation
**Args:** `clearcnv -i alignments.bam -r reference.fasta --segment -o cnv_calls.vcf`
**Explanation:** Performs segmentation-based CNV calling.

### From multiple samples
**Args:** `clearcnv -i sample1.bam,sample2.bam -r reference.fasta -o cnv_calls.vcf`
**Explanation:** Calls CNVs from multiple samples simultaneously.

### Display help
**Args:** `clearcnv --help`
**Explanation:** Shows all available options and usage information.