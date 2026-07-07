---
name: skc
category: sequence-analysis
description: skc - Shared k-mer content analysis
tags: ["skc", "sequence-analysis", "k-mer", "comparative"]
author: oxo-call-community
source_url: "https://github.com/mbhall88/skc"
---

## Concepts

- **Tool Overview**: skc (v0.1.0) analyzes shared k-mer content between genomes.
- **Core Function**: Calculates shared k-mer statistics between sequences.
- **Algorithm**: Uses k-mer counting for sequence comparison.
- **Input/Output**: Accepts FASTA sequences and produces k-mer statistics.
- **K-mer Analysis**: Specialized for shared k-mer content analysis.
- **Applications**: Genome comparison, sequence similarity, phylogenetics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Compare genomes
**Args:** `skc -a genome1.fasta -b genome2.fasta -o shared_kmers.txt`
**Explanation:** `-a` and `-b` input genomes; `-o` output file.

### With k-mer size
**Args:** `skc -a genome1.fasta -b genome2.fasta -k 31 -o shared_kmers.txt`
**Explanation:** `-k 31` k-mer size.

### Count only
**Args:** `skc -a genome1.fasta -b genome2.fasta -c`
**Explanation:** `-c` only count shared k-mers.

### Help command
**Args:** `skc --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `skc --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `skc -v -a genome1.fasta -b genome2.fasta -o shared_kmers.txt`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `skc -t 8 -a genome1.fasta -b genome2.fasta -o shared_kmers.txt`
**Explanation:** `-t 8` uses 8 threads.
