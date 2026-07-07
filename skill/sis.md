---
name: sis
category: assembly
description: SiS - Scaffolding small genomes using MUMmer
tags: ["sis", "assembly", "scaffolding", "mummer"]
author: oxo-call-community
source_url: "http://marte.ic.unicamp.br:8747/"
---

## Concepts

- **Tool Overview**: SiS (v0.1.2) scaffolds small genomes using MUMmer alignments.
- **Core Function**: Orders and orients contigs into scaffolds.
- **Algorithm**: Uses MUMmer for alignment and scaffolding.
- **Input/Output**: Accepts contigs and reference, produces scaffolds.
- **Genome Scaffolding**: Specialized for small genome assembly.
- **Applications**: Genome assembly, contig scaffolding, sequence finishing.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Dependency Issues**: Requires MUMmer installation.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on contig quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Scaffold contigs
**Args:** `sis -c contigs.fasta -r reference.fasta -o scaffolds.fasta`
**Explanation:** `-c` contigs; `-r` reference; `-o` output scaffolds.

### With gap size
**Args:** `sis -c contigs.fasta -r reference.fasta -g 500 -o scaffolds.fasta`
**Explanation:** `-g 500` gap size between contigs.

### With alignment parameters
**Args:** `sis -c contigs.fasta -r reference.fasta -m 90 -o scaffolds.fasta`
**Explanation:** `-m 90` minimum alignment identity.

### Help command
**Args:** `sis --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sis --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sis -v -c contigs.fasta -r reference.fasta -o scaffolds.fasta`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sis -t 8 -c contigs.fasta -r reference.fasta -o scaffolds.fasta`
**Explanation:** `-t 8` uses 8 threads.
