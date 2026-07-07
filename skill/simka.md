---
name: simka
category: metagenomics
description: Simka - Comparative metagenomics using k-mer spectra
tags: ["simka", "metagenomics", "k-mer", "comparative"]
author: oxo-call-community
source_url: "https://github.com/GATB/simka"
---

## Concepts

- **Tool Overview**: Simka (v1.5.3) performs comparative metagenomics using k-mer spectra.
- **Core Function**: Computes ecological distances between metagenomic datasets.
- **Algorithm**: Uses k-mer based comparison and ecological distance metrics.
- **Input/Output**: Accepts FASTQ files and produces distance matrices.
- **Metagenomics Analysis**: Specialized for comparing microbial communities.
- **Applications**: Microbiome analysis, metagenomics comparison, biodiversity studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Compare metagenomes
**Args:** `simka -i samples.txt -o results/`
**Explanation:** `-i` file with sample paths; `-o` output directory.

### With k-mer size
**Args:** `simka -i samples.txt -k 31 -o results/`
**Explanation:** `-k 31` k-mer size.

### Using simkaMin
**Args:** `simka -i samples.txt --min -o results/`
**Explanation:** `--min` use memory-efficient simkaMin mode.

### Help command
**Args:** `simka --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simka --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simka -v -i samples.txt -o results/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `simka -t 8 -i samples.txt -o results/`
**Explanation:** `-t 8` uses 8 threads.
