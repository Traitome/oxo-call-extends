---
name: rnastructure
category: alignment
description: RNAstructure is a complete package for RNA and DNA secondary structure  prediction and analysis. It includes algorithms for   secondary structure  prediction, including facility to predict base pairing probabilities. It  also can be used to predict bimolecular structures and can predict the  equilibrium binding affinity of an oligonucleotide to a structured RNA  target. This is useful for siRNA design. It can also predict secondary  structures common to two, unaligned sequences, which is much more accurate  than single sequence secondary structure prediction. Finally, RNAstructure  can take a number of different types of experiment mapping data to constrain  or restrain structure prediction. These include chemical mapping, enzymatic  mapping, NMR, and SHAPE data.
tags: ["rnastructure", "alignment"]
author: oxo-call-community
source_url: "https://rna.urmc.rochester.edu/Overview/index.html"
---

## Concepts

- **Tool Overview**: RNAstructure is a complete package for RNA and DNA secondary structure  prediction and analysis. It includes algorithms for   secondary structure  prediction, including facility to predict base pairing probabilities. It  also can be used to predict bimolecular structures and can predict the  equilibrium binding affinity of an oligonucleotide to a structured RNA  target. This is useful for siRNA design. It can also predict secondary  structures common to two, unaligned sequences, which is much more accurate  than single sequence secondary structure prediction. Finally, RNAstructure  can take a number of different types of experiment mapping data to constrain  or restrain structure prediction. These include chemical mapping, enzymatic  mapping, NMR, and SHAPE data. (version 6.6)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rnastructure`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

