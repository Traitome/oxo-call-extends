---
name: biotdg
category: utility
description: Bioinformatics Test Data Generator for creating realistic synthetic data
tags: [test-data, synthetic-data, bioinformatics, generation]
author: oxo-call-community
source_url: "https://github.com/biowdl/biotdg"
---

## Concepts

- **Tool Overview**: BioTDG (Bioinformatics Test Data Generator) generates realistic synthetic bioinformatics test data for testing pipelines and tools.
- **Realistic Data**: Generates biologically realistic sequences and annotations that mimic real data characteristics.
- **Configurable Parameters**: Allows control over sequence length, GC content, read depth, and other parameters.
- **Format Support**: Generates FASTA, FASTQ, VCF, BED, and other bioinformatics formats.
- **Applications**: Pipeline testing, tool validation, benchmark data generation.

## Pitfalls

- **Reference Compatibility**: Generated data may not match specific reference genomes without proper configuration.
- **Biologically Realistic**: Synthetic data may not capture all complexities of real biological data.
- **Size Limitations**: Very large synthetic datasets may require significant storage.

## Examples

### Generate synthetic FASTQ
**Args:** `biotdg generate --type fastq --reads 1000000 --length 150 -o synthetic_reads.fq`
**Explanation:** Generates one million 150bp synthetic FASTQ reads.

### Generate test VCF
**Args:** `biotdg generate --type vcf --samples 10 --variants 1000 -o test_variants.vcf`
**Explanation:** Generates a VCF file with 1000 variants across 10 samples.

### Generate targeted BED
**Args:** `biotdg generate --type bed --chroms chr1,chr2,chr3 --regions 100 -o target_regions.bed`
**Explanation:** Generates BED file with 100 target regions on specified chromosomes.