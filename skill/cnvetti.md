---
name: cnvetti
category: utility
description: CNVetti is a CNV caller from high-throughput sequencing data
tags: [cnvetti, cnv-calling, copy-number-variation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/bihealth/cnvetti"
---

## Concepts

- **Tool Overview**: CNVetti is a copy number variation (CNV) caller designed for high-throughput sequencing (HTS) data, providing accurate detection of genomic copy number changes.
- **Core Function**: Detects copy number variations from sequencing data using read depth analysis and segmentation algorithms.
- **Algorithm**: Uses read depth normalization and segmentation to identify regions with abnormal copy numbers.
- **Input**: BAM files with aligned sequencing reads.
- **Output**: CNV calls in VCF or BED format with copy number estimates.
- **Application**: Cancer genomics, population genetics, and clinical diagnostics.
- **Installation**: Install via bioconda: `conda install -c bioconda cnvetti`

## Pitfalls

- **Data Quality**: Requires high-quality sequencing data with even coverage.
- **GC Bias**: May be affected by GC content bias in sequencing data.
- **Segmentation**: Segmentation parameters may need adjustment.
- **Reference Genome**: Requires appropriate reference genome for normalization.
- **Structural Variants**: May miss complex structural variants.

## Examples

### Call CNVs from BAM
**Args:** `cnvetti -i sample.bam -o cnv_calls.vcf`
**Explanation:** Calls CNVs from aligned sequencing data.

### With reference
**Args:** `cnvetti -i sample.bam -r reference.fasta -o cnv_calls.vcf`
**Explanation:** Uses reference genome for normalization.

### Output BED format
**Args:** `cnvetti -i sample.bam -o cnv_calls.bed -f bed`
**Explanation:** Outputs CNV calls in BED format.

### Display help
**Args:** `cnvetti --help`
**Explanation:** Shows all available options and usage information.