---
name: centrifuge-core
category: metagenomics
description: Core classifier for metagenomic sequence classification
tags: [centrifuge-core, centrifuge, metagenomics, sequence-classification, taxonomy]
author: oxo-call-community
source_url: "https://genome.cshlp.org/content/26/12/1721"
---

## Concepts

- **Tool Overview**: centrifuge-core is the core classification component of Centrifuge for metagenomic sequence analysis.
- **Core Function**: Classifies DNA sequences against a reference database for taxonomic identification.
- **Algorithm**: Uses an efficient indexing scheme for fast sequence classification.
- **Input**: FASTA/FASTQ sequence files.
- **Output**: Taxonomic classifications with confidence scores.
- **Application**: Rapid taxonomic profiling of metagenomic samples.
- **Installation**: Install via bioconda: `conda install -c bioconda centrifuge-core`

## Pitfalls

- **Database Requirement**: Requires pre-built Centrifuge index database.
- **Memory Usage**: Large databases may require significant memory.
- **Index Compatibility**: Database index must match tool version.
- **Classification Accuracy**: Depends on database completeness.

## Examples

### Build index from reference sequences
**Args:** `centrifuge-build -p 8 reference.fasta index_name`
**Explanation:** Builds Centrifuge index from reference sequences.

### Classify sequences
**Args:** `centrifuge -x index_name -1 reads_1.fastq -2 reads_2.fastq -o output.tsv`
**Explanation:** Classifies paired-end reads against reference index.

### Single-end classification
**Args:** `centrifuge -x index_name -U reads.fastq -o output.tsv`
**Explanation:** Classifies single-end reads.

### Display help
**Args:** `centrifuge --help`
**Explanation:** Shows all available options and usage information.