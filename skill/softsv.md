---
name: softsv
category: variant-analysis
description: SoftSV - Structural variant detection from paired-end sequencing data
tags: [softsv, variant-analysis, structural-variants, paired-end, sv]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/softsv"
---

## Concepts

- **Tool Overview**: softsv (v1.4.2) - A structural variant detection tool
- **Core Function**: Detects deletions, inversions, duplications, and translocations
- **Input/Output**: Accepts BAM alignments; outputs VCF with SV calls
- **Algorithm**: Analyzes paired-end read patterns for SV detection
- **Installation**: `conda install -c bioconda softsv`
- **Key Features**: SV detection, paired-end analysis, multiple SV types

## Pitfalls

- **Input Requirements**: Requires properly aligned paired-end BAM files
- **Read Depth**: Requires sufficient read depth for reliable SV calling
- **Insert Size**: Requires proper insert size estimation
- **Reference Genome**: Must use compatible reference genome
- **Memory Usage**: Large BAM files require significant memory
- **False Positives**: May produce false positives in repetitive regions

## Examples

### Display help
**Args:** `softsv --help`
**Explanation:** Shows available options and usage information.

### Basic SV calling
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf`
**Explanation:** Detect structural variants from BAM.

### With insert size
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf --insert-size 500`
**Explanation:** Set expected insert size.

### Filter by size
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf --min-size 100`
**Explanation:** Filter SVs by minimum size.

### Detect deletions only
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf --deletions`
**Explanation:** Detect only deletion variants.

### Detect inversions only
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf --inversions`
**Explanation:** Detect only inversion variants.

### With threads
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf -p 8`
**Explanation:** Use multiple threads for SV calling.

### Generate report
**Args:** `softsv -i aligned.bam -r reference.fasta -o sv_calls.vcf --report`
**Explanation:** Generate SV detection report.