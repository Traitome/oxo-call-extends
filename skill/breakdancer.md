---
name: breakdancer
category: variant-calling
description: Structural variant detection from paired-end read mapping
tags: [breakdancer, sv, structural-variant, indel, deletion]
author: oxo-call-community
source_url: "https://github.com/genome/breakdancer"
---

## Concepts

- **Tool Overview**: BreakDancer detects structural variants (SVs) from paired-end sequencing data.
- **Core Function**: Identifies insertions, deletions, inversions, and translocations from discordant read pairs.
- **Input Requirement**: Sorted BAM file from paired-end alignment.
- **Output Format**: Tab-delimited file with SV coordinates, types, and supporting read counts.
- **Sensitivity**: Detects SVs from 100bp to several megabases in size.
- **Installation**: Install via bioconda: `conda install -c bioconda breakdancer`

## Pitfalls

- **Paired-End Only**: Requires proper paired-end sequencing data; single-end not supported.
- **Insert Size**: Accurate insert size estimation is critical for SV detection.
- **False Positives**: High false positive rate in repetitive regions; manual curation recommended.
- **BAM Sorting**: Input BAM must be sorted by read name, not coordinate.
- **Memory Usage**: Large BAM files require significant memory for processing.

## Examples

### Generate config file
**Args:** `bam2cfg.pl aligned.bam > config.txt`
**Explanation:** Creates configuration file with insert size statistics from BAM.

### Detect all SV types
**Args:** `breakdancer-max config.txt > svs.txt`
**Explanation:** Detects all structural variant types from paired-end data.

### Detect deletions only
**Args:** `breakdancer-max -t DEL config.txt > deletions.txt`
**Explanation:** Reports only deletion events from the BAM file.

### Detect insertions only
**Args:** `breakdancer-max -t INS config.txt > insertions.txt`
**Explanation:** Reports only insertion events from the paired-end data.

### Minimum supporting reads
**Args:** `breakdancer-max -r 5 config.txt > svs.txt`
**Explanation:** Requires minimum 5 supporting reads for SV call.

### Output in VCF format
**Args:** `breakdancer-max -o 1 config.txt > svs.vcf`
**Explanation:** Outputs structural variants in VCF format for downstream analysis.
