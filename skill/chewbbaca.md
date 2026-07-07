---
name: chewbbaca
category: typing
description: Complete suite for gene-by-gene schema creation and strain identification
tags: [chewbbaca, mlst, cgmlst, wgmlst, allele-calling, strain-typing, bioinformatics]
author: oxo-call-community
source_url: "https://chewbbaca.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: chewBBACA is a comprehensive pipeline for creating and validating whole genome and core genome MultiLocus Sequence Typing (wg/cgMLST) schemas for bacterial strain identification.
- **Core Function**: Performs allele calling, schema creation, and strain typing using gene-by-gene approaches.
- **Features**: Schema creation, allele calling, quality control, and phylogenetic analysis for bacterial isolates.
- **Input**: Genome FASTA files for schema creation or allele calling.
- **Output**: Allele calls, MLST profiles, and phylogenetic trees.
- **Application**: Bacterial epidemiology, outbreak investigation, and population genetics.
- **Installation**: Install via bioconda: `conda install -c bioconda chewbbaca`

## Pitfalls

- **Schema Quality**: Schema creation requires high-quality reference genomes.
- **Genome Completeness**: Incomplete genomes may affect allele calling.
- **Computational Resources**: Large datasets may require significant compute resources.
- **Allele Database**: Requires comprehensive allele database for accurate typing.
- **Memory Usage**: May require significant memory for large analyses.

## Examples

### Create new schema
**Args:** `chewBBACA.py CreateSchema -i genomes/ -o schema/ -t 8`
**Explanation:** Creates a new cgMLST schema from genome sequences.

### Call alleles
**Args:** `chewBBACA.py AlleleCall -i genomes/ -s schema/ -o results/ -t 8`
**Explanation:** Calls alleles against existing schema.

### Quality control
**Args:** `chewBBACA.py QC -i results/ -o qc_results/`
**Explanation:** Runs quality control on allele calls.

### Display help
**Args:** `chewBBACA.py --help`
**Explanation:** Shows all available commands and options.