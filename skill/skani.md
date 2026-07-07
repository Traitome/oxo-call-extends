---
name: skani
category: sequence-analysis
description: skani - Fast ANI calculation tool
tags: ["skani", "sequence-analysis", "ani", "comparative"]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/skani"
---

## Concepts

- **Tool Overview**: skani (v0.3.1) calculates Average Nucleotide Identity (ANI) between genomes.
- **Core Function**: Computes ANI for metagenome-assembled genomes and contigs.
- **Algorithm**: Uses minimizer-based approach for fast comparison.
- **Input/Output**: Accepts FASTA sequences and produces ANI values.
- **ANI Calculation**: Specialized for fast and robust ANI estimation.
- **Applications**: Genome comparison, taxonomy, metagenomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Calculate ANI
**Args:** `skani genome1.fasta genome2.fasta`
**Explanation:** Compute ANI between two genomes.

### Batch mode
**Args:** `skani -d genomes/ -o ani_matrix.txt`
**Explanation:** `-d` directory with genomes; `-o` output matrix.

### With output format
**Args:** `skani -o tsv genome1.fasta genome2.fasta`
**Explanation:** Output in TSV format.

### Help command
**Args:** `skani --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `skani --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `skani -v genome1.fasta genome2.fasta`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `skani -t 8 genome1.fasta genome2.fasta`
**Explanation:** `-t 8` uses 8 threads.
