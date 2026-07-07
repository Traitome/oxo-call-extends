---
name: dupsifter
category: utility
description: "A tool for PCR duplicate marking of WGBS (and WGS) data."
tags: [dupsifter, utility, PCR-duplicates, WGBS, WGS, methylation]
author: oxo-call-community
source_url: "https://github.com/huishenlab/dupsifter"
---

## Concepts

- **Tool Overview**: Dupsifter is a tool for marking PCR duplicates in whole-genome bisulfite sequencing (WGBS) and whole-genome sequencing (WGS) data.
- **Core Function**: Identifies and marks PCR duplicates while preserving methylation information for WGBS data.
- **Input/Output**: Input: Aligned reads (BAM). Output: BAM with duplicate markings.
- **Algorithm**: Uses alignment coordinates and methylation patterns to identify PCR duplicates.
- **Key Features**: Methylation-aware duplicate marking, WGBS/WGS support, UMI handling, parallel processing.
- **Installation**: `conda install -c bioconda dupsifter`

## Pitfalls

- **Library Complexity**: Low complexity libraries produce many duplicates.
- **UMI Barcodes**: UMI errors can affect duplicate identification.
- **Methylation Patterns**: Methylation patterns must be preserved during duplicate marking.
- **Paired-End Data**: Proper handling of paired-end reads is critical.
- **Memory Usage**: Large BAM files may require significant memory.

## Examples

### Basic duplicate marking for WGBS
**Args:** `--input aligned.bam --output marked.bam --mode WGBS`
**Explanation:** Marks PCR duplicates in WGBS data preserving methylation info.

### WGS mode
**Args:** `--input aligned.bam --output marked.bam --mode WGS`
**Explanation:** Marks PCR duplicates in WGS data.

### With UMI handling
**Args:** `--input aligned.bam --output marked.bam --mode WGBS --umi`
**Explanation:** Uses UMI information for more accurate duplicate marking.

### Remove duplicates
**Args:** `--input aligned.bam --output marked.bam --mode WGBS --remove`
**Explanation:** Removes duplicate reads instead of just marking them.

### Generate metrics
**Args:** `--input aligned.bam --output marked.bam --mode WGBS --metrics metrics.txt`
**Explanation:** Generates duplicate metrics report.