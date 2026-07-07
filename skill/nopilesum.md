---
name: nopilesum
category: variant-calling
description: nopilesum is a fast alternative to GATK4's GetPileupSummaries for pileup summary generation.
tags: [nopilesum, variant-calling, gatk, pileup]
author: oxo-call-community
source_url: "https://github.com/blachlylab/nopilesum"
---

## Concepts

- **Tool Overview**: nopilesum provides fast pileup summary generation as an alternative to GATK4.
- **Core Function**: Generates pileup summaries from BAM files for variant calling.
- **Algorithm**: Implements efficient pileup parsing for rapid summary generation.
- **Input Format**: Accepts BAM files and VCF intervals.
- **Output**: Produces pileup summary tables.
- **Use Case**: Variant calling, genotype quality assessment, and population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Compatibility**: Requires matching reference genome.
- **Memory Usage**: Large BAM files require memory.
- **Coordinate System**: Uses 0-based or 1-based coordinates.
- **Output Format**: Different from GATK4 output.
- **Validation**: Results should be validated against GATK4.

## Examples

### Display help
**Args:** `nopilesum --help`
**Explanation:** Shows available options and usage instructions.

### Generate pileup summary
**Args:** `nopilesum -i input.bam -o output.txt -R reference.fasta`
**Explanation:** Generates pileup summary from BAM file.

### With intervals
**Args:** `nopilesum -i input.bam -o output.txt -R reference.fasta -L intervals.bed`
**Explanation:** Processes specific genomic intervals.

### VCF intervals
**Args:** `nopilesum -i input.bam -o output.txt -R reference.fasta -V variants.vcf`
**Explanation:** Uses VCF file for intervals.

### Threads
**Args:** `nopilesum -i input.bam -o output.txt -R reference.fasta -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum mapping quality
**Args:** `nopilesum -i input.bam -o output.txt -R reference.fasta -q 30`
**Explanation:** Sets minimum mapping quality threshold.

### Verbose mode
**Args:** `nopilesum -i input.bam -o output.txt -R reference.fasta -v`
**Explanation:** Runs with verbose output.