---
name: cesar
category: sequence-analysis
description: CESAR 2.0 - Realign coding exons or genes to DNA sequences using Hidden Markov Model
tags: [cesar, sequence-alignment, hmm, exons, genes, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/hillerlab/CESAR2.0"
---

## Concepts

- **Tool Overview**: CESAR 2.0 is a method to realign coding exons or genes to DNA sequences using a Hidden Markov Model (HMM).
- **Core Function**: Aligns coding sequences to target DNA sequences while maintaining reading frame and splice sites.
- **Algorithm**: Uses HMM with states for exons, introns, splice sites, and unaligned regions.
- **Input**: Coding sequence (CDS) in FASTA format and target DNA sequence.
- **Output**: Realigned coding regions with accurate exon boundaries.
- **Application**: Comparative genomics, gene structure prediction, and exon alignment.
- **Installation**: Install via bioconda: `conda install -c bioconda cesar`

## Pitfalls

- **Reading Frame**: Input sequences must be in the correct reading frame.
- **Splice Sites**: Requires canonical splice site patterns.
- **Sequence Quality**: Poor quality sequences may affect alignment accuracy.
- **Memory Usage**: Large alignments may require significant memory.

## Examples

### Align coding sequence to target
**Args:** `cesar --query cds.fasta --target genome.fasta --output aligned.gff`
**Explanation:** Aligns coding sequence to target genome using HMM.

### Realign with custom parameters
**Args:** `cesar --query gene.fasta --target target.fa --output result.gff --min-exon 20`
**Explanation:** Sets minimum exon length to 20 nucleotides.

### Batch processing
**Args:** `cesar --query-dir cds_dir/ --target genome.fasta --output-dir results/`
**Explanation:** Processes multiple CDS files in batch mode.

### Display help
**Args:** `cesar --help`
**Explanation:** Shows all available options and usage information.