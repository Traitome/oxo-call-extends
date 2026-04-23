---
name: cap3
category: assembly
description: DNA sequence assembly program for Sanger and short reads
tags: [cap3, assembly, sanger, est]
author: oxo-call-community
source_url: "http://seq.cs.iastate.edu/"
---

## Concepts

- **Tool Overview**: CAP3 is a DNA sequence assembly program for Sanger sequencing and short reads.
- **Core Function**: Assembles overlapping sequence reads into contigs.
- **Algorithm**: Uses base quality values for accurate assembly.
- **Input**: FASTA files with quality scores (.qual files).
- **Output**: Contigs and singletons in FASTA format.
- **Application**: EST assembly, Sanger read assembly, and small genome assembly.
- **Installation**: Install via bioconda: `conda install -c bioconda cap3`

## Pitfalls

- **Quality Files**: Requires .qual quality files alongside FASTA.
- **Read Length**: Designed for Sanger-length reads; not optimal for NGS short reads.
- **Overlap Parameters**: Adjust overlap parameters based on data quality.
- **Output Naming**: Output files use input prefix by default.

## Examples

### Assemble sequences
**Args:** `cap3 reads.fa -o assembly.fa`
**Explanation:** Assembles reads into contigs with default parameters.

### Set overlap parameters
**Args:** `cap3 reads.fa -o assembly.fa -p 90 -s 200`
**Explanation:** Uses 90% identity overlap cutoff and 200bp minimum overlap.

### Specify quality file
**Args:** `cap3 reads.fa reads.qual -o assembly.fa`
**Explanation:** Uses quality scores from .qual file for assembly.

### Display help
**Args:** `cap3`
**Explanation:** Shows usage information by running without arguments.
