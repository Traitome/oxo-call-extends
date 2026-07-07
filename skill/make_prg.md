---
name: make_prg
category: alignment
description: A tool to create and update PRGs from a set of Multiple Sequence Alignments.
tags: [make_prg, alignment, PRG, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/iqbal-lab-org/make_prg"
---

## Concepts

- **Tool Overview**: make_prg v0.5.0 - A tool for creating and updating Population Reference Graphs (PRGs) from multiple sequence alignments.
- **Core Function**: Builds PRGs that represent genetic variation across populations.
- **Input/Output**: Input: Multiple sequence alignments (FASTA/Clustal); Output: PRG files in various formats.
- **Installation**: `conda install -c bioconda make_prg`
- **Population Reference Graphs**: PRGs represent genetic variation by encoding all observed alleles in a graph structure.
- **Graph-based Representation**: Enables efficient mapping of reads to complex genetic variation.

## Pitfalls

- **Alignment Quality**: Poor quality alignments produce inaccurate PRGs.
- **Sequence Diversity**: High diversity may increase graph complexity.
- **Memory Usage**: Large alignments require significant memory.
- **Output Format**: Different downstream tools require different PRG formats.
- **Parameter Tuning**: Incorrect parameters affect graph structure.
- **Phasing Information**: Missing phasing information limits variant representation.

## Examples

### Build PRG from alignment
**Args:** `make_prg build -i alignment.fasta -o prg.gfa`
**Explanation:** Creates PRG from multiple sequence alignment.

### Update existing PRG
**Args:** `make_prg update -i new_alignment.fasta -p existing_prg.gfa -o updated_prg.gfa`
**Explanation:** Updates PRG with new sequences.

### Output in VG format
**Args:** `make_prg build -i alignment.fasta -o prg.vg -f vg`
**Explanation:** Outputs PRG in VG format.

### With quality filtering
**Args:** `make_prg build -i alignment.fasta -o prg.gfa -q 20`
**Explanation:** Filters low-quality positions.

### Verbose mode
**Args:** `make_prg build -i alignment.fasta -o prg.gfa -v`
**Explanation:** Provides detailed logging during PRG construction.

### Generate statistics
**Args:** `make_prg stats -p prg.gfa -o stats.txt`
**Explanation:** Generates statistics about the PRG.