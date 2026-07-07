---
name: cawlign
category: alignment
description: Align consensus sequences to reference genomes
tags: [cawlign, alignment, consensus, reference-genome, fasta]
author: oxo-call-community
source_url: "https://github.com/veg/cawlign"
---

## Concepts

- **Tool Overview**: cawlign aligns consensus sequences to reference genomes, ported from bealign/BioExt.
- **Core Function**: Maps sequences from FASTA file to reference sequence and outputs aligned FASTA.
- **Algorithm**: Implements sequence alignment algorithm for consensus mapping.
- **Input**: FASTA file with consensus sequences and reference sequence.
- **Output**: Aligned sequences in FASTA format.
- **Application**: Viral sequence analysis, consensus mapping, and sequence alignment.
- **Installation**: Install via bioconda: `conda install -c bioconda cawlign`

## Pitfalls

- **FASTA Format**: Requires properly formatted FASTA input files.
- **Reference Match**: Reference sequence should match expected genome.
- **Sequence Length**: Works best with consensus sequences of moderate length.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Align consensus sequences
**Args:** `cawlign -i consensus.fasta -r reference.fasta -o aligned.fasta`
**Explanation:** Aligns consensus sequences to reference genome.

### With output SAM
**Args:** `cawlign -i consensus.fasta -r reference.fasta -s alignment.sam -o aligned.fasta`
**Explanation:** Outputs both aligned FASTA and SAM alignment file.

### Display help
**Args:** `cawlign --help`
**Explanation:** Shows all available options and usage information.