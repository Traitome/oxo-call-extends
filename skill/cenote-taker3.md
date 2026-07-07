---
name: cenote-taker3
category: metagenomics
description: Discover and annotate viral sequences from metagenomic data
tags: [cenote-taker3, virome, viral-discovery, annotation, metagenomics]
author: oxo-call-community
source_url: "https://github.com/mtisza1/Cenote-Taker3/blob/v3.4.4/README.md"
---

## Concepts

- **Tool Overview**: Cenote-Taker 3 is a pipeline for discovering and annotating viral sequences from metagenomic data.
- **Core Function**: Identifies viral contigs and performs comprehensive annotation of viral genomes.
- **Features**: Viral identification, gene prediction, taxonomy assignment, and functional annotation.
- **Input**: Metagenomic assembly contigs in FASTA format.
- **Output**: Annotated viral sequences with gene predictions and taxonomy.
- **Application**: Virome analysis from metagenomic sequencing data.
- **Installation**: Install via bioconda: `conda install -c bioconda cenote-taker3`

## Pitfalls

- **Contig Quality**: Requires good quality assembled contigs.
- **False Positives**: May identify non-viral sequences as viral.
- **Database Dependencies**: Relies on viral reference databases.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Run viral discovery and annotation
**Args:** `cenote-taker3 --contigs contigs.fasta --output virome_results/`
**Explanation:** Runs complete viral discovery and annotation pipeline.

### Specify custom viral database
**Args:** `cenote-taker3 --contigs contigs.fasta --db custom_virus_db --output results/`
**Explanation:** Uses custom viral database for identification.

### Run quick mode
**Args:** `cenote-taker3 --contigs contigs.fasta --quick --output results/`
**Explanation:** Runs in quick mode for faster results.

### Display help
**Args:** `cenote-taker3 --help`
**Explanation:** Shows all available options and usage information.