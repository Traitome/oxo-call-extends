---
name: metacompass
category: assembly
description: "MetaCompass: Reference-guided Assembly of Metagenomes."
tags: [metacompass, assembly, metagenomics, reference-guided]
author: oxo-call-community
source_url: "https://github.com/marbl/MetaCompass"
---
## Concepts

- **Tool Overview**: MetaCompass v1.12 is a reference-guided metagenomic assembly tool that uses closely related reference genomes to guide the assembly process.
- **Core Function**: Improves metagenomic assembly by leveraging reference genome information to scaffold and orient contigs.
- **Reference-guided Assembly**: Uses reference genomes to guide the assembly of metagenomic sequences.
- **Scaffolding**: Integrates contigs into larger scaffolds using reference genome alignment.
- **Input/Output**: Accepts raw sequencing reads and reference genomes; outputs assembled scaffolds in FASTA format.
- **Hybrid Assembly**: Combines de novo assembly with reference-guided scaffolding.

## Pitfalls

- **Reference Availability**: Requires closely related reference genomes for effective assembly.
- **Reference Bias**: May introduce bias towards reference genome sequences.
- **Assembly Quality**: Depends on the quality of input reads and reference genomes.
- **Computational Resources**: Memory and CPU requirements can be significant for large datasets.
- **Reference Genome Quality**: Poor quality reference genomes can negatively impact assembly.
- **Strain Variation**: May struggle with samples containing multiple strains of the same species.

## Examples

### Run reference-guided assembly
**Args:** `metacompass -i reads.fastq -r reference.fasta -o assembly/`
**Explanation:** Performs reference-guided assembly using the provided reference genome.

### With paired-end reads
**Args:** `metacompass -i reads_1.fastq reads_2.fastq -r reference.fasta -o assembly/`
**Explanation:** Processes paired-end sequencing data with reference guidance.

### Multiple references
**Args:** `metacompass -i reads.fastq -r ref1.fasta ref2.fasta -o assembly/`
**Explanation:** Uses multiple reference genomes for assembly guidance.

### Specify k-mer size
**Args:** `metacompass -i reads.fastq -r reference.fasta -k 31 -o assembly/`
**Explanation:** Uses k-mer size of 31 for assembly.

### Output assembly graph
**Args:** `metacompass -i reads.fastq -r reference.fasta -o assembly/ --graph`
**Explanation:** Generates assembly graph visualization.