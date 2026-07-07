---
name: cured
category: metagenomics
description: Classification Using Restriction Enzyme Diagnostics
tags: [cured, metagenomics, classification, restriction-enzyme, diagnostics]
author: oxo-call-community
source_url: "https://github.com/microbialARC/CURED"
---

## Concepts

- **Tool Overview**: cured (v1.05+) is a tool for microbial classification using restriction enzyme diagnostics.
- **Core Function**: Uses restriction enzyme digestion patterns to classify microbial species from sequencing data.
- **Input/Output**: Input: FASTA sequences, metagenomic reads. Output: Taxonomic classification, abundance estimates.
- **Algorithm**: Compares restriction fragment patterns against reference database for species identification.
- **Key Features**: Rapid classification, works with incomplete genomes, provides confidence scores.
- **Installation**: `conda install -c bioconda cured`

## Pitfalls

- **Reference Database**: Requires comprehensive reference database for accurate classification.
- **Restriction Enzyme Selection**: Results depend on enzyme choice; use multiple enzymes for robustness.
- **Sequence Quality**: Low-quality sequences may produce unreliable patterns.
- **Database Updates**: Reference database must be updated for emerging pathogens.
- **Output Interpretation**: Classification results should be validated with other methods.

## Examples

### Classify sequences
**Args:** `cured -i sequences.fasta -o classifications.tsv`
**Explanation:** Classify microbial sequences using restriction enzyme patterns.

### Build custom database
**Args:** `cured build -i reference.fasta -o custom_db/`
**Explanation:** Build a custom restriction enzyme database from reference sequences.

### Analyze metagenomic reads
**Args:** `cured -i reads.fastq -d database/ -o results.tsv`
**Explanation:** Classify metagenomic reads against a pre-built database.
