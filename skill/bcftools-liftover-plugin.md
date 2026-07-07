---
name: bcftools-liftover-plugin
category: formatting
description: bcftools-liftover-plugin - Liftover VCF coordinates between genome assemblies
tags: [bcftools-liftover-plugin, formatting, VCF, liftover, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/samtools/bcftools"
---

## Concepts

- **Tool Overview**: bcftools-liftover-plugin (v1.22) is a bcftools plugin that converts (lifts over) variant coordinates from one genome assembly to another (e.g., hg19 to hg38).
- **Core Function**: Liftovers VCF variant coordinates between different genome assemblies using chain files.
- **Coordinate Conversion**: Converts genomic positions between reference genome versions.
- **Chain File Support**: Uses UCSC-style chain files for coordinate mapping.
- **bcftools Integration**: Works as a plugin for the bcftools suite.
- **Input/Output**: Accepts VCF files and chain files; outputs liftovered VCF files.
- **Installation**: `conda install -c bioconda bcftools-liftover-plugin`.

## Pitfalls

- **bcftools Dependency**: Requires bcftools to be installed and configured.
- **Chain File Quality**: Liftover accuracy depends on chain file quality.
- **Ambiguous Mapping**: Some positions may map ambiguously; check for failures.
- **Post-liftover Validation**: Always validate liftovered coordinates against target reference.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic liftover
**Args:** `bcftools +liftover input.vcf -c hg19ToHg38.over.chain.gz -o output.vcf`
**Explanation:** Lifts over VCF coordinates from hg19 to hg38.

### With reference genome
**Args:** `bcftools +liftover input.vcf -c chain.chain.gz -r target_reference.fasta -o output.vcf`
**Explanation:** Uses target reference for additional validation.

### Output unmapped variants
**Args:** `bcftools +liftover input.vcf -c chain.chain.gz -o output.vcf -u unmapped.vcf`
**Explanation:** Outputs unmapped variants to separate file.

### Skip failed variants
**Args:** `bcftools +liftover input.vcf -c chain.chain.gz -o output.vcf --skip-failed`
**Explanation:** Skips variants that fail liftover instead of reporting errors.

### Compressed output
**Args:** `bcftools +liftover input.vcf -c chain.chain.gz -o output.vcf.gz`
**Explanation:** Outputs compressed VCF file.

### Liftover with stats
**Args:** `bcftools +liftover input.vcf -c chain.chain.gz -o output.vcf --stats liftover_stats.txt`
**Explanation:** Generates statistics about liftover success rates.

### Display help
**Args:** `bcftools +liftover --help`
**Explanation:** Shows all available command-line options and usage information.