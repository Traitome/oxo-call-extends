---
name: sgcocaller
category: variant-calling
description: sgcocaller - Single-cell gamete crossover calling
tags: ["sgcocaller", "variant-calling", "single-cell", "crossover"]
author: oxo-call-community
source_url: "https://gitlab.svi.edu.au/biocellgen-public/sgcocaller"
---

## Concepts

- **Tool Overview**: sgcocaller (v0.3.9) performs personalized haplotype construction and crossover calling in single-cell DNA sequenced gamete cells.
- **Core Function**: Identifies crossover events in gamete cells using single-cell sequencing data.
- **Algorithm**: Uses haplotype phasing and variant calling for crossover detection.
- **Input/Output**: Accepts BAM files and produces crossover calls.
- **Single-Cell Analysis**: Focuses on gamete cell crossover detection.
- **Applications**: Meiotic recombination research, genetics, and reproductive biology.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Call crossovers
**Args:** `sgcocaller -i input.bam -r reference.fasta -o output.vcf`
**Explanation:** `-i` input BAM; `-r` reference; `-o` output VCF.

### With phasing
**Args:** `sgcocaller -i input.bam -r reference.fasta -p phased.vcf -o output.vcf`
**Explanation:** `-p` phased VCF for haplotype information.

### Verbose logging
**Args:** `sgcocaller -v -i input.bam -r reference.fasta -o output.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sgcocaller --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sgcocaller --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `sgcocaller -t 8 -i input.bam -r reference.fasta -o output.vcf`
**Explanation:** `-t 8` uses 8 threads.