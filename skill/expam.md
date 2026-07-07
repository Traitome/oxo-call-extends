---
name: expam
category: metagenomics
description: "Metagenomic profiling using a reference phylogeny"
tags: [expam, metagenomics, phylogeny, taxonomic-profiling, reference-based]
author: oxo-call-community
source_url: "https://expam.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: ExPAM is a metagenomic profiling tool that uses a reference phylogeny for accurate taxonomic classification.
- **Core Function**: Assigns metagenomic reads to taxa using phylogenetic information and reference databases.
- **Input/Output**: Input: Sequencing reads (FASTQ), reference phylogeny. Output: Taxonomic profiles, abundance estimates.
- **Algorithm**: Uses phylogenetic placement and evolutionary distances for taxonomic assignment.
- **Key Features**: Phylogeny-aware profiling, high accuracy, support for complex communities, batch processing.
- **Installation**: `conda install -c bioconda expam`

## Pitfalls

- **Reference Quality**: Requires high-quality reference phylogeny and databases.
- **Computation Time**: Phylogenetic placement can be computationally intensive.
- **Memory Usage**: Large reference databases require significant RAM.
- **Evolutionary Divergence**: Highly divergent sequences may be misclassified.
- **Database Updates**: Reference databases require regular updates.

## Examples

### Basic metagenomic profiling
**Args:** `--reads sample.fastq --output profile.txt`
**Explanation:** Profiles metagenomic reads using default reference database.

### With custom database
**Args:** `--reads sample.fastq --output profile.txt --db custom_db`
**Explanation:** Uses custom reference database for profiling.

### Phylogenetic placement
**Args:** `--reads sample.fastq --output profile.txt --phylogeny tree.nwk`
**Explanation:** Uses custom phylogenetic tree for placement.

### Batch processing
**Args:** `--reads-dir samples/ --output results/ --batch`
**Explanation:** Processes multiple samples in batch mode.

### Generate report
**Args:** `--reads sample.fastq --output profile.txt --report report.html`
**Explanation:** Generates HTML report with profiling results.