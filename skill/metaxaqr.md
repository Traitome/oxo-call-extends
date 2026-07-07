---
name: metaxaqr
category: metagenomics
description: Improved Identification and Taxonomic Classification of Small and Large Subunit rRNA in Metagenomic Data.
tags: [metaxaqr, metagenomics, rRNA]
author: oxo-call-community
source_url: "http://microbiology.se/software/metaxaQR/"
---

## Concepts

- **Tool Overview**: MetaXA-QR v3.0rc2 is a tool for improved identification and taxonomic classification of small and large subunit rRNA, optimized for quick reference (QR) analysis.
- **Core Function**: Rapidly identifies and classifies rRNA sequences in metagenomic datasets.
- **rRNA Identification**: Detects small subunit (SSU) and large subunit (LSU) rRNA sequences.
- **Taxonomic Classification**: Classifies rRNA sequences into taxonomic groups.
- **Input/Output**: Accepts sequencing reads or contigs; outputs rRNA annotations and classifications.
- **High-Speed Analysis**: Optimized for rapid analysis of large metagenomic datasets.

## Pitfalls

- **Database Completeness**: Classification accuracy depends on reference database completeness.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Sequence Quality**: Detection accuracy depends on input sequence quality.
- **False Positives**: May detect false positive rRNA sequences.

## Examples

### Rapid rRNA identification
**Args:** `metaxaqr -i reads.fastq -o rRNA_results.txt`
**Explanation:** Rapidly identifies and classifies rRNA sequences.

### With custom database
**Args:** `metaxaqr -i reads.fastq -d custom_db/ -o rRNA_results.txt`
**Explanation:** Uses custom rRNA database for identification.

### Paired-end analysis
**Args:** `metaxaqr -i reads_1.fastq -r reads_2.fastq -o rRNA_results.txt`
**Explanation:** Processes paired-end sequencing data.

### Detailed output
**Args:** `metaxaqr -i reads.fastq -o rRNA_results.txt -v`
**Explanation:** Generates detailed rRNA identification report.

### Batch processing
**Args:** `metaxaqr -i fastq/ -o rRNA_results/`
**Explanation:** Processes multiple samples in batch mode.