---
name: medusa
category: assembly
description: Graph-based draft genome scaffolder using multiple reference genomes.
tags: [medusa, genome-scaffolding, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/combogenomics/medusa"
---

## Concepts

- **Tool Overview**: Medusa scaffolds draft genomes using multiple references.
- **Core Function**: Graph-based scaffolding using reference genomes.
- **Multiple References**: Integrates information from multiple reference genomes.
- **Graph Construction**: Builds synteny graph for scaffolding.
- **Contig Ordering**: Orders and orients contigs based on references.
- **Installation**: `conda install -c bioconda medusa`

## Pitfalls

- **Reference Quality**: Requires high-quality reference genomes.
- **Memory Requirements**: High memory for large datasets.
- **Computation Time**: Slow for complex genomes.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Synteny Assumptions**: Relies on conserved synteny.
- **Output Quality**: Depends on input contig quality.

## Examples

### Scaffold genome
**Args:** `medusa -f contigs.fasta -r ref1.fasta ref2.fasta -o scaffold.fasta`
**Explanation:** Scaffolds contigs using multiple references.

### With distance constraints
**Args:** `medusa -f contigs.fasta -r ref.fasta -d 1000 -o scaffold.fasta`
**Explanation:** Sets maximum gap distance between contigs.

### Verbose output
**Args:** `medusa -f contigs.fasta -r ref.fasta -v -o scaffold.fasta`
**Explanation:** Shows detailed scaffolding progress.

### Output AGP file
**Args:** `medusa -f contigs.fasta -r ref.fasta -a scaffold.agp -o scaffold.fasta`
**Explanation:** Generates AGP format scaffold file.

### Help documentation
**Args:** `medusa --help`
**Explanation:** Displays available options.
