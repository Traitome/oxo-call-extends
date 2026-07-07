---
name: safesim
category: variant_calling
description: SafeSeqS variant simulator for targeted sequencing data
tags: ["safesim", "variant-calling", "simulation", "NGS", "SafeSeqS"]
author: oxo-call-community
source_url: "https://github.com/genetronhealth/safesim"
---

## Concepts

- **Tool Overview**: SafeSim (v0.1.6) is a variant simulator specifically designed for SafeSeqS targeted sequencing technology, enabling simulation of low-frequency somatic variants in sequencing data.
- **Core Function**: Simulates targeted sequencing reads with known variants at specified allele frequencies, supporting SafeSeqS duplex sequencing methodology.
- **Algorithm**: Generates synthetic reads incorporating user-defined variants, mimicking real sequencing errors, and maintaining molecular barcode integrity.
- **Input Format**: Reference genome (FASTA), target regions (BED), variant list (VCF or CSV), sequencing parameters.
- **Output Format**: Simulated FASTQ files, ground truth VCF with known variants, sequencing statistics.
- **Use Case**: Validation of variant calling pipelines, performance benchmarking, sensitivity testing, method development.

## Pitfalls

- **Reference genome**: Must use the same reference genome as the target pipeline.
- **Barcode complexity**: Incorrect barcode configuration affects duplex validation.
- **Error model**: Simulation may not perfectly replicate real sequencing errors.
- **Variant representation**: Complex variants (indels, CNVs) may require special handling.
- **Performance**: High-depth simulations require significant computational resources.
- **Memory usage**: Large target regions require substantial memory for read generation.

## Examples

### Basic variant simulation
**Args:** `safesim -r reference.fasta -t targets.bed -v variants.vcf -o output_prefix`
**Explanation:** `-r` reference genome; `-t` target regions; `-v` variants to simulate; `-o` output prefix.

### Specify allele frequency
**Args:** `safesim -r ref.fasta -t targets.bed -v variants.vcf -o output -f 0.01`
**Explanation:** `-f` allele frequency for simulated variants (default: 0.01).

### Generate duplex reads
**Args:** `safesim -r ref.fasta -t targets.bed -v variants.vcf -o output --duplex`
**Explanation:** `--duplex` enables SafeSeqS duplex sequencing simulation.

### Set coverage depth
**Args:** `safesim -r ref.fasta -t targets.bed -v variants.vcf -o output -d 1000`
**Explanation:** `-d` target sequencing depth (default: 500).

### Include sequencing errors
**Args:** `safesim -r ref.fasta -t targets.bed -v variants.vcf -o output --error-rate 0.001`
**Explanation:** `--error-rate` sets base error rate (default: 0.001).

### Single-end mode
**Args:** `safesim -r ref.fasta -t targets.bed -v variants.vcf -o output --single-end`
**Explanation:** Generates single-end reads instead of paired-end.

### Quality score configuration
**Args:** `safesim -r ref.fasta -t targets.bed -v variants.vcf -o output --quality-offset 33`
**Explanation:** `--quality-offset` sets Phred quality score offset.