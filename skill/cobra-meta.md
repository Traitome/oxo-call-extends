---
name: cobra-meta
category: assembly
description: COBRA is a tool to get higher quality viral genomes assembled from metagenomes
tags: [cobra-meta, viral-assembly, metagenomics, bioinformatics, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/linxingchen/cobra"
---

## Concepts

- **Tool Overview**: COBRA is a metagenomic assembly tool specifically designed for reconstructing high-quality viral genomes from metagenomic sequencing data.
- **Core Function**: Assembles viral genomes from metagenomic reads by leveraging coverage information and sequence composition.
- **Algorithm**: Uses coverage-based binning and assembly refinement to improve viral genome reconstruction.
- **Input**: Metagenomic sequencing reads in FASTQ format.
- **Output**: Assembled viral genomes in FASTA format.
- **Application**: Viral metagenomics, virus discovery, and viral community analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cobra-meta`

## Pitfalls

- **Host Contamination**: May assemble host sequences along with viral sequences.
- **Low Coverage**: Requires sufficient sequencing depth for viral genomes.
- **Complex Communities**: May struggle with highly diverse viral communities.
- **Memory Usage**: May require significant memory for large datasets.
- **Assembly Quality**: Results depend on input read quality and coverage.

## Examples

### Assemble viral genomes
**Args:** `cobra-meta -i reads.fastq -o assembly_dir/`
**Explanation:** Assembles viral genomes from metagenomic reads.

### With paired-end reads
**Args:** `cobra-meta -i reads_1.fastq -i reads_2.fastq -o assembly_dir/`
**Explanation:** Uses paired-end reads for assembly.

### With coverage threshold
**Args:** `cobra-meta -i reads.fastq -c 10 -o assembly_dir/`
**Explanation:** Sets minimum coverage threshold to 10x.

### Display help
**Args:** `cobra-meta --help`
**Explanation:** Shows all available options and usage information.