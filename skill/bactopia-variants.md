---
name: bactopia-variants
category: variant-calling
description: Bactopia Variants - SNP and InDel analysis component for Bactopia pipeline
tags: [bactopia-variants, variant-calling, snp, indel, bacterial-genomics]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: Bactopia Variants is the variant calling component of the Bactopia pipeline, designed for SNP and InDel detection in bacterial genomes. Version 1.0.4.
- **Core Function**: Performs variant calling (SNPs and InDels) from aligned sequencing reads against a reference genome.
- **SNP Detection**: Identifies single nucleotide polymorphisms between samples and reference.
- **InDel Detection**: Detects insertions and deletions of varying sizes.
- **GATK Integration**: Uses GATK tools for variant calling with bacterial-specific optimizations.
- **Variant Filtering**: Includes quality-based filtering to reduce false positives.
- **Annotation**: Optional variant annotation with functional impact prediction.
- **Input/Output**: Accepts BAM alignments and reference FASTA, outputs VCF files.
- **Installation**: `conda install -c bioconda bactopia-variants`.

## Pitfalls

- **Version Compatibility**: Must match Bactopia pipeline version for proper integration.
- **Reference Genome**: Requires high-quality reference genome for accurate variant calling.
- **Alignment Quality**: Poor quality alignments lead to false variant calls.
- **Variant Quality**: Low-quality variants should be filtered or manually reviewed.
- **Indel Calling**: InDel detection can be sensitive to alignment parameters.
- **Memory Usage**: Variant calling requires significant memory for large datasets.

## Examples

### Basic variant calling
**Args:** `bactopia-variants --input alignments.bam --reference reference.fasta --output variants.vcf`
**Explanation:** Calls variants from aligned reads against reference genome.

### With variant filtering
**Args:** `bactopia-variants --input alignments.bam --reference reference.fasta --filter --output filtered.vcf`
**Explanation:** Applies quality filtering to variant calls.

### Multiple samples
**Args:** `bactopia-variants --input sample1.bam sample2.bam --reference reference.fasta --output variants.vcf`
**Explanation:** Calls variants from multiple aligned BAM files.

### Variant annotation
**Args:** `bactopia-variants --input alignments.bam --reference reference.fasta --annotate --output annotated.vcf`
**Explanation:** Calls and annotates variants with functional information.

### Custom quality thresholds
**Args:** `bactopia-variants --input alignments.bam --reference reference.fasta --min-quality 30 --output variants.vcf`
**Explanation:** Sets minimum quality threshold for variant calls.

### Generate VCF index
**Args:** `bactopia-variants --input alignments.bam --reference reference.fasta --index --output variants.vcf`
**Explanation:** Creates indexed VCF file for efficient access.

### Specify ploidy
**Args:** `bactopia-variants --input alignments.bam --reference reference.fasta --ploidy 1 --output variants.vcf`
**Explanation:** Sets ploidy level (1 for haploid bacteria).

### Display help
**Args:** `bactopia-variants --help`
**Explanation:** Shows all available command-line options and usage information.