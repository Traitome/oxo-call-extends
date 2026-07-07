---
name: sharkmer
category: expression
description: sharkmer - Kmer counter and de Bruijn graph assembler
tags: ["sharkmer", "expression", "k-mer", "assembly"]
author: oxo-call-community
source_url: "https://github.com/caseywdunn/sharkmer"
---

## Concepts

- **Tool Overview**: sharkmer (v3.1.0) is a k-mer counter and seeded de Bruijn graph assembler.
- **Core Function**: Counts k-mers and performs in silico PCR and genome size estimation.
- **Algorithm**: Uses de Bruijn graph approach for sequence assembly.
- **Input/Output**: Accepts FASTA/Q sequences and produces k-mer counts or assemblies.
- **K-mer Analysis**: Focuses on k-mer counting and sequence assembly.
- **Applications**: Genome size estimation, in silico PCR, and sequence analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **Performance**: May be slow for extremely large files.

## Examples

### Count k-mers
**Args:** `sharkmer count -i input.fasta -o kmer_counts.txt`
**Explanation:** `-i` input sequences; `-o` output k-mer counts.

### Assembly mode
**Args:** `sharkmer assemble -i input.fasta -o contigs.fasta`
**Explanation:** Assembles sequences using de Bruijn graph.

### With k-mer size
**Args:** `sharkmer count -i input.fasta -k 31 -o kmer_counts.txt`
**Explanation:** `-k 31` k-mer size.

### Verbose logging
**Args:** `sharkmer -v count -i input.fasta -o kmer_counts.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sharkmer --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sharkmer --version`
**Explanation:** Shows current version.

### Genome size estimate
**Args:** `sharkmer estimate -i input.fasta -o estimate.txt`
**Explanation:** Estimates genome size from k-mer distribution.