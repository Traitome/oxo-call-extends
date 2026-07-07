---
name: consensusfixer
category: alignment
description: Compute consensus sequences with ambiguous bases from NGS alignments
tags: [consensusfixer, consensus, ngs, alignment, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/ConsensusFixer"
---

## Concepts

- **Tool Overview**: ConsensusFixer computes consensus sequences with wobbles (ambiguous bases) and in-frame insertions from next-generation sequencing read alignments.
- **Core Function**: Generates consensus sequences that preserve ambiguity information from aligned reads, useful for representing population diversity.
- **Algorithm**: Analyzes alignment columns to determine base frequencies and assigns IUPAC ambiguity codes for mixed positions.
- **Input**: Aligned sequencing reads in BAM/SAM format.
- **Output**: Consensus sequence in FASTA format with IUPAC ambiguity codes.
- **Application**: Viral quasispecies analysis, population genomics, and consensus sequence generation.
- **Installation**: Install via bioconda: `conda install -c bioconda consensusfixer`

## Pitfalls

- **Coverage Requirements**: Requires sufficient coverage for accurate consensus calling.
- **Ambiguity Threshold**: Threshold settings affect ambiguity code assignment.
- **Frame Awareness**: In-frame insertion detection requires coding sequence context.
- **Alignment Quality**: Poor alignments produce incorrect consensus sequences.
- **Strand Bias**: May not account for strand-specific biases.

## Examples

### Generate consensus sequence
**Args:** `consensusfixer -i alignment.bam -o consensus.fasta`
**Explanation:** Generates consensus sequence with ambiguity codes from alignment.

### With minimum coverage
**Args:** `consensusfixer -i alignment.bam -c 10 -o consensus.fasta`
**Explanation:** Requires minimum coverage of 10x for consensus calling.

### With ambiguity threshold
**Args:** `consensusfixer -i alignment.bam -t 0.2 -o consensus.fasta`
**Explanation:** Sets 20% threshold for assigning ambiguity codes.

### Display help
**Args:** `consensusfixer --help`
**Explanation:** Shows all available options and usage information.