---
name: shorah
category: assembly
description: shorah - Viral haplotype assembly from NGS data
tags: ["shorah", "assembly", "viral", "haplotype"]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/shorah"
---

## Concepts

- **Tool Overview**: shorah (v1.99.2) infers viral haplotypes from NGS data.
- **Core Function**: Assembles short reads into haplotypes for viral populations.
- **Algorithm**: Uses probabilistic methods for haplotype reconstruction.
- **Input/Output**: Accepts FASTQ reads and produces haplotype sequences.
- **Viral Analysis**: Focuses on viral population diversity analysis.
- **Applications**: Viral evolution, quasispecies analysis, and virology research.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Assemble haplotypes
**Args:** `shorah -i reads.fastq -r reference.fasta -o output/`
**Explanation:** `-i` input reads; `-r` reference; `-o` output directory.

### Paired-end
**Args:** `shorah -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o output/`
**Explanation:** `-1/-2` paired-end reads.

### Verbose logging
**Args:** `shorah -v -i reads.fastq -r reference.fasta -o output/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shorah --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shorah --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shorah -t 8 -i reads.fastq -r reference.fasta -o output/`
**Explanation:** `-t 8` uses 8 threads.

### With quality filter
**Args:** `shorah -i reads.fastq -r reference.fasta -q 20 -o output/`
**Explanation:** `-q 20` minimum quality threshold.