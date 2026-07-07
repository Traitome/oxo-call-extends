---
name: shmlast
category: utility
description: shmlast - Conditional reciprocal best hits with LAST
tags: ["shmlast", "utility", "sequence-comparison", "LAST"]
author: oxo-call-community
source_url: "https://github.com/camillescott/shmlast"
---

## Concepts

- **Tool Overview**: shmlast (v1.6) finds conditional reciprocal best hits using LAST.
- **Core Function**: Identifies orthologous sequences between genomes.
- **Algorithm**: Uses LAST aligner for reciprocal best hit detection.
- **Input/Output**: Accepts sequence files and produces orthology predictions.
- **Orthology Detection**: Focuses on identifying homologous sequences.
- **Applications**: Comparative genomics, phylogenomics, and sequence analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Find reciprocal best hits
**Args:** `shmlast -q query.fasta -d database.fasta -o results.txt`
**Explanation:** `-q` query sequences; `-d` database; `-o` output results.

### With options
**Args:** `shmlast -q query.fasta -d database.fasta -e 1e-5 -o results.txt`
**Explanation:** `-e 1e-5` e-value threshold.

### Verbose logging
**Args:** `shmlast -v -q query.fasta -d database.fasta -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shmlast --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shmlast --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shmlast -t 8 -q query.fasta -d database.fasta -o results.txt`
**Explanation:** `-t 8` uses 8 threads.

### Output format
**Args:** `shmlast -q query.fasta -d database.fasta -f tab -o results.txt`
**Explanation:** `-f tab` tab-separated output format.