---
name: optimir
category: alignment
description: OptimiR integrates genetic variations in miRNA alignment for improved accuracy.
tags: [optimir, alignment, mirna, genetics]
author: oxo-call-community
source_url: "https://github.com/FlorianThibord/OptimiR"
---

## Concepts

- **Tool Overview**: OptimiR aligns small RNA reads considering genetic variations.
- **Core Function**: Aligns miRNA reads with variant-aware mapping.
- **Algorithm**: Uses seed-based alignment with variant integration.
- **Input Format**: Accepts FASTQ reads and VCF variant files.
- **Output**: Produces aligned reads and variant-aware mappings.
- **Use Case**: miRNA-seq analysis, variant-aware alignment, and small RNA research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Alignment can be computationally intensive.
- **Variant Data**: Requires VCF file for variant-aware mapping.
- **Read Quality**: Results depend on input read quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `optimir --help`
**Explanation:** Shows available options and usage instructions.

### Align reads
**Args:** `optimir -i reads.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Aligns miRNA reads to reference.

### With variants
**Args:** `optimir -i reads.fastq -r reference.fasta -v variants.vcf -o aligned.bam`
**Explanation:** Uses VCF for variant-aware alignment.

### Output format
**Args:** `optimir -i reads.fastq -r reference.fasta -o aligned.sam --sam`
**Explanation:** Outputs in SAM format.

### Verbose mode
**Args:** `optimir -i reads.fastq -r reference.fasta -v -o aligned.bam`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `optimir batch -d fastqs/ -r reference.fasta -o results/`
**Explanation:** Processes multiple FASTQ files.

### Quality filtering
**Args:** `optimir -i reads.fastq -r reference.fasta -q 20 -o aligned.bam`
**Explanation:** Filters reads by quality score.