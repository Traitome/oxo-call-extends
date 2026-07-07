---
name: dicey
category: utility
description: dicey - In-silico PCR and variant-aware primer design tool.
tags: [dicey, utility, pcr, primer-design, in-silico]
author: oxo-call-community
source_url: "https://github.com/gear-genomics/dicey"
---

## Concepts

- **Tool Overview**: dicey (v0.3.4+) is a tool for in-silico PCR simulation and variant-aware primer design. It helps design primers that account for known genetic variants.
- **Core Function**: Simulates PCR reactions in silico on reference genomes and designs primers that avoid or target specific variants.
- **Input/Output**: Input: Reference genome (FASTA), primer sequences or variant data (VCF). Output: In-silico PCR products, primer designs, specificity reports.
- **Algorithm**: Uses sequence alignment to simulate primer binding and PCR amplification, considering variant alleles.
- **Key Features**: In-silico PCR simulation, variant-aware primer design, specificity checking, batch processing, multiple output formats.
- **Installation**: `conda install -c bioconda dicey`

## Pitfalls

- **Reference Indexing**: Requires indexed reference genome for efficient lookup.
- **Primer Quality**: Poor primer design may produce non-specific amplification.
- **Variant Data**: Variant-aware features require VCF input with proper formatting.
- **Memory Usage**: May require significant memory for large genomes.
- **PCR Assumptions**: Simulation makes assumptions about PCR efficiency and specificity.

## Examples

### Simulate in-silico PCR
**Args:** `pcr --ref ref.fa --primers primers.tsv --output pcr_products.bed`
**Explanation:** Simulates in-silico PCR on reference genome using primers from TSV file.

### Design variant-aware primers
**Args:** `design --ref ref.fa --variants variants.vcf --output primers.tsv`
**Explanation:** Designs primers that account for known variants in the target region.

### Check primer specificity
**Args:** `pcr --ref ref.fa --primers primers.tsv --output pcr_products.bed --check-specificity`
**Explanation:** Check for potential off-target amplification sites.

### Batch primer testing
**Args:** `pcr --ref ref.fa --primers primers.tsv --output pcr_products.bed --batch`
**Explanation:** Process multiple primer pairs in batch mode.

### Generate report
**Args:** `pcr --ref ref.fa --primers primers.tsv --output pcr_products.bed --report report.html`
**Explanation:** Generate comprehensive HTML report of PCR results.