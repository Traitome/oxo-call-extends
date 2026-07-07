---
name: siann
category: utility
description: siann - Strain level differentiation from FASTQ data
tags: ["siann", "utility", "strain", "fastq"]
author: oxo-call-community
source_url: "https://github.com/signaturescience/siann/wiki"
---

## Concepts

- **Tool Overview**: siann (v1.3) performs strain-level differentiation from sequencing data.
- **Core Function**: Identifies bacterial/viral strains from FASTQ reads.
- **Algorithm**: Uses k-mer matching and reference genome comparison.
- **Input/Output**: Accepts FASTQ reads and produces strain identification results.
- **Strain Analysis**: Focuses on high-resolution strain typing.
- **Applications**: Pathogen identification, microbial surveillance, and epidemiology.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Reference Database**: Requires comprehensive reference database.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Identify strains
**Args:** `siann -i reads.fastq -o results.txt`
**Explanation:** `-i` input FASTQ; `-o` output results.

### With reference database
**Args:** `siann -i reads.fastq -d ref_database/ -o results.txt`
**Explanation:** `-d` reference database directory.

### Paired-end reads
**Args:** `siann -1 reads_1.fastq -2 reads_2.fastq -o results.txt`
**Explanation:** `-1/-2` paired-end reads.

### Help command
**Args:** `siann --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `siann --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `siann -v -i reads.fastq -o results.txt`
**Explanation:** `-v` verbose output.

### With confidence threshold
**Args:** `siann -i reads.fastq -c 0.95 -o results.txt`
**Explanation:** `-c 0.95` confidence threshold.
