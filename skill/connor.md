---
name: connor
category: formatting
description: Deduplicate BAM files based on custom inline barcoding
tags: [connor, bam, deduplication, barcoding, ngs]
author: oxo-call-community
source_url: "https://github.com/umich-brcf-bioinf/Connor"
---

## Concepts

- **Tool Overview**: Connor is a command-line tool for deduplicating BAM files based on custom inline barcoding, removing PCR duplicates while preserving unique molecular identifiers (UMIs).
- **Core Function**: Identifies and removes PCR duplicates from aligned sequencing data using UMI information embedded in reads.
- **Algorithm**: Groups reads by alignment position and UMI sequence, retaining only unique molecules.
- **Input**: Aligned sequencing reads in BAM format with UMI information.
- **Output**: Deduplicated BAM file with PCR duplicates removed.
- **Application**: NGS data processing, UMI-based sequencing, and variant calling preparation.
- **Installation**: Install via bioconda: `conda install -c bioconda connor`

## Pitfalls

- **UMI Quality**: Low-quality UMI bases may cause incorrect deduplication.
- **Alignment Required**: Must be aligned before deduplication.
- **UMI Position**: Must correctly specify UMI location in reads.
- **Duplicate Definition**: May be overly aggressive in duplicate calling.
- **Paired-end**: Requires proper handling of paired-end reads.

## Examples

### Deduplicate BAM file
**Args:** `connor -i input.bam -o deduplicated.bam`
**Explanation:** Removes PCR duplicates from BAM file using default UMI settings.

### With custom UMI position
**Args:** `connor -i input.bam -u 1-8 -o deduplicated.bam`
**Explanation:** Specifies UMI at positions 1-8 of reads.

### With UMI error correction
**Args:** `connor -i input.bam -e 1 -o deduplicated.bam`
**Explanation:** Allows 1 mismatch in UMI for error correction.

### Display help
**Args:** `connor --help`
**Explanation:** Shows all available options and usage information.