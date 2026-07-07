---
name: shigatyper
category: utility
description: shigatyper - Shigella typing from WGS Illumina sequencing
tags: ["shigatyper", "utility", "serotyping", "Shigella"]
author: oxo-call-community
source_url: "https://github.com/CFSAN-Biostatistics/shigatyper"
---

## Concepts

- **Tool Overview**: shigatyper (v2.0.5) types Shigella spp. from WGS Illumina sequencing data.
- **Core Function**: Identifies Shigella serotypes from genomic sequences.
- **Algorithm**: Uses sequence comparison against known serotype markers.
- **Input/Output**: Accepts FASTQ/FASTA files and produces serotype predictions.
- **Serotyping**: Focuses on Shigella species identification.
- **Applications**: Clinical microbiology, epidemiology, and pathogen surveillance.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Quality**: Results depend on sequencing data quality.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **Database Updates**: Requires up-to-date serotype database.

## Examples

### Type Shigella
**Args:** `shigatyper -i reads.fastq -o results.txt`
**Explanation:** `-i` input reads; `-o` output results.

### From assembly
**Args:** `shigatyper -i assembly.fasta -t fasta -o results.txt`
**Explanation:** `-t fasta` specifies FASTA input type.

### Verbose logging
**Args:** `shigatyper -v -i reads.fastq -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shigatyper --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shigatyper --version`
**Explanation:** Shows current version.

### Paired-end
**Args:** `shigatyper -1 reads_1.fastq -2 reads_2.fastq -o results.txt`
**Explanation:** `-1/-2` paired-end reads.

### Force mode
**Args:** `shigatyper -i reads.fastq -o results.txt -f`
**Explanation:** `-f` force overwrite output.