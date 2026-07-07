---
name: somatic-sniper
category: variant-calling
description: SomaticSniper - Tool for calling somatic single nucleotide variants
tags: [somatic-sniper, variant-calling, somatic, snv, mutations]
author: oxo-call-community
source_url: "https://github.com/genome/somatic-sniper/"
---

## Concepts

- **Tool Overview**: somatic-sniper (v1.0.5.0) - A somatic SNV caller
- **Core Function**: Detects somatic single nucleotide variants from tumor-normal pairs
- **Input/Output**: Accepts BAM files; outputs VCF with somatic SNVs
- **Algorithm**: Bayesian approach for somatic variant detection
- **Installation**: `conda install -c bioconda somatic-sniper`
- **Key Features**: Somatic SNV calling, tumor-normal pairs, Bayesian model

## Pitfalls

- **Input Requirements**: Requires tumor and normal BAM files
- **Reference Genome**: Requires reference genome for alignment
- **Coverage**: Requires sufficient coverage for reliable calling
- **Quality Scores**: Quality scores affect variant detection
- **Memory Usage**: Large BAM files require significant memory
- **False Positives**: May produce false positives in low coverage regions

## Examples

### Display help
**Args:** `bam-somaticsniper --help`
**Explanation:** Shows available options and usage information.

### Basic somatic calling
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf`
**Explanation:** Call somatic SNVs from tumor-normal pair.

### With quality threshold
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf -q 20`
**Explanation:** Set quality threshold for calling.

### With prior probability
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf -p 0.00001`
**Explanation:** Set prior probability for somatic mutation.

### Output somatic score
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf -s`
**Explanation:** Output somatic score in VCF.

### Filter by coverage
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf -c 10`
**Explanation:** Filter variants by minimum coverage.

### Generate report
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --report`
**Explanation:** Generate somatic calling report.

### With threads
**Args:** `bam-somaticsniper -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf -p 8`
**Explanation:** Use multiple threads for calling.