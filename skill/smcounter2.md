---
name: smcounter2
category: variant-calling
description: smCounter2 - an accurate low-frequency variant caller for targeted sequencing data with unique molecular identifiers (UMIs)
tags: [smcounter2, variant-calling, low-frequency, umi, targeted-sequencing]
author: oxo-call-community
source_url: "https://github.com/qiaseq/qiaseq-smcounter-v2"
---

## Concepts

- **Tool Overview**: smcounter2 (v0.1.2018.08.28) - A variant caller optimized for low-frequency mutations with UMIs
- **Core Function**: Calls low-frequency variants from targeted sequencing data using UMI deduplication
- **Input/Output**: Accepts BAM files with UMI tags; outputs VCF with variant calls
- **Algorithm**: Uses UMI-based deduplication to reduce PCR duplicates and improve sensitivity
- **Installation**: `conda install -c bioconda smcounter2`
- **Key Features**: High sensitivity for low-frequency variants, UMI support, targeted sequencing optimization

## Pitfalls

- **UMI Requirements**: Requires UMI information in BAM file
- **BAM Format**: BAM must be properly formatted with UMI tags
- **Target Regions**: Performance depends on target region definition
- **Coverage Depth**: Requires sufficient coverage for low-frequency detection
- **Contamination**: Sample contamination affects variant calling accuracy
- **Reference Genome**: Must use correct reference genome

## Examples

### Display help
**Args:** `smcounter2 --help`
**Explanation:** Shows available options and usage information.

### Basic variant calling
**Args:** `smcounter2 -i input.bam -r reference.fasta -o output.vcf`
**Explanation:** Call variants from BAM file with UMI information.

### With target regions
**Args:** `smcounter2 -i input.bam -r reference.fasta -t targets.bed -o output.vcf`
**Explanation:** Restrict variant calling to target regions.

### Set minimum allele frequency
**Args:** `smcounter2 -i input.bam -r reference.fasta -o output.vcf -f 0.001`
**Explanation:** Set minimum allele frequency threshold to 0.1%.

### With custom UMI tag
**Args:** `smcounter2 -i input.bam -r reference.fasta -o output.vcf -u RX`
**Explanation:** Use custom UMI tag (default is UB).

### Generate statistics
**Args:** `smcounter2 -i input.bam -r reference.fasta -o output.vcf -s stats.txt`
**Explanation:** Generate variant calling statistics.

### Filter by quality
**Args:** `smcounter2 -i input.bam -r reference.fasta -o output.vcf -q 20`
**Explanation:** Filter variants by quality >= 20.

### Output annotated VCF
**Args:** `smcounter2 -i input.bam -r reference.fasta -o output.vcf -a`
**Explanation:** Output annotated VCF with additional metrics.