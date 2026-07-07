---
name: scalpel
category: variant-calling
description: Scalpel - sensitive detection of insertions and deletions (INDELs)
tags: ["scalpel", "variant-calling", "INDELs", "short-variants"]
author: oxo-call-community
source_url: "https://scalpel.sourceforge.net"
---

## Concepts

- **Tool Overview**: Scalpel (v0.5.4) is a sensitive variant caller specifically designed for detecting insertions and deletions (INDELs) from next-generation sequencing data.
- **Core Function**: Identifies small to medium-sized INDELs with high sensitivity and specificity.
- **Algorithm**: Uses local assembly and re-alignment to detect INDELs with high accuracy.
- **Input/Output**: Accepts BAM files and reference genome, produces VCF with INDEL calls.
- **Sensitivity**: Designed to detect both common and rare INDEL variants.
- **Applications**: Variant discovery, population genetics, and clinical genomics.

## Pitfalls

- **INDEL Specific**: Focuses on INDELs, may not detect SNPs effectively.
- **Read Depth**: Requires sufficient sequencing depth for reliable detection.
- **Reference Genome**: Results depend on reference genome quality.
- **Computational Resources**: High memory and CPU requirements.
- **Parameter Tuning**: Requires careful adjustment for optimal performance.
- **False Positives**: May report false INDELs in repetitive regions.

## Examples

### Basic INDEL calling
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta -o results/`
**Explanation:** `-b` input BAM; `-r` reference; `-o` output directory.

### With quality filtering
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta -q 20 -o results/`
**Explanation:** `-q 20` filters variants with quality below 20.

### Targeted analysis
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta -t targets.bed -o results/`
**Explanation:** `-t` BED file with target regions.

### Paired-end mode
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta --paired-end -o results/`
**Explanation:** `--paired-end` optimizes for paired-end data.

### Output VCF only
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta --vcf-only -o variants.vcf`
**Explanation:** `--vcf-only` outputs only VCF file.

### Verbose logging
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta -v -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Statistics report
**Args:** `scalpel-discovery -b alignments.bam -r reference.fasta --stats -o results/`
**Explanation:** `--stats` generates comprehensive statistics report.