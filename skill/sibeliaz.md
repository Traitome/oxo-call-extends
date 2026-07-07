---
name: sibeliaz
category: alignment
description: SibeliaZ - Fast whole-genome aligner based on de Bruijn graphs
tags: ["sibeliaz", "alignment", "genome", "de-bruijn"]
author: oxo-call-community
source_url: "https://github.com/medvedevgroup/SibeliaZ"
---

## Concepts

- **Tool Overview**: SibeliaZ (v1.2.7) is a fast whole-genome aligner using de Bruijn graphs.
- **Core Function**: Aligns complete genomes efficiently.
- **Algorithm**: Uses de Bruijn graph-based approach for alignment.
- **Input/Output**: Accepts FASTA genomes and produces alignment files.
- **Genome Alignment**: Optimized for large-scale whole-genome alignment.
- **Applications**: Comparative genomics, genome assembly, and evolutionary analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Size**: Performance degrades with very large genomes.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Align genomes
**Args:** `sibeliaz -i genomes.txt -o output/`
**Explanation:** `-i` file with genome paths; `-o` output directory.

### With reference
**Args:** `sibeliaz -r reference.fasta -i genomes.txt -o output/`
**Explanation:** `-r` reference genome.

### With k-mer size
**Args:** `sibeliaz -k 31 -i genomes.txt -o output/`
**Explanation:** `-k 31` k-mer size.

### Help command
**Args:** `sibeliaz --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sibeliaz --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `sibeliaz -t 8 -i genomes.txt -o output/`
**Explanation:** `-t 8` uses 8 threads.

### Verbose mode
**Args:** `sibeliaz -v -i genomes.txt -o output/`
**Explanation:** `-v` verbose output.
