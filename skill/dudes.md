---
name: dudes
category: metagenomics
description: "DUDes: a top-down taxonomic profiler for metagenomics and metaproteomics"
tags: [dudes, metagenomics, taxonomic-profiling, metagenomics, metaproteomics]
author: oxo-call-community
source_url: "https://github.com/pirovc/dudes"
---

## Concepts

- **Tool Overview**: DUDes is a top-down taxonomic profiler for metagenomics and metaproteomics data.
- **Core Function**: Assigns taxonomic labels to reads or peptides using a hierarchical classification approach.
- **Input/Output**: Input: Sequencing reads or peptides (FASTA/FASTQ), reference database. Output: Taxonomic profiles, abundance estimates.
- **Algorithm**: Uses a top-down approach with LCA (Lowest Common Ancestor) assignment for robust taxonomic classification.
- **Key Features**: Handles ambiguous alignments, supports multiple databases, strain-level resolution, protein and DNA input.
- **Installation**: `conda install -c bioconda dudes`

## Pitfalls

- **Database Size**: Large reference databases require significant memory.
- **Alignment Quality**: Taxonomic assignment depends on alignment quality.
- **Strain Resolution**: Some closely related strains may be difficult to distinguish.
- **Horizontal Transfer**: Horizontal gene transfer can affect taxonomic assignments.
- **Coverage Bias**: Uneven sequencing coverage affects abundance estimates.

## Examples

### Basic taxonomic profiling
**Args:** `--input reads.fastq --db reference.db --output profile.txt`
**Explanation:** Performs taxonomic profiling of metagenomic reads.

### With multiple databases
**Args:** `--input reads.fastq --db db1 db2 --output profile.txt`
**Explanation:** Uses multiple reference databases for profiling.

### Strain-level analysis
**Args:** `--input reads.fastq --db reference.db --output profile.txt --strain-level`
**Explanation:** Enables strain-level taxonomic resolution.

### Metaproteomics mode
**Args:** `--input peptides.fasta --db protein.db --output profile.txt --protein`
**Explanation:** Profiles taxonomic composition from metaproteomics data.

### Generate report
**Args:** `--input reads.fastq --db reference.db --output profile.txt --report report.html`
**Explanation:** Generates HTML report with taxonomic profile visualization.