---
name: ebolaseq
category: population-genomics
description: "Tool for downloading and analyzing Ebola virus sequences."
tags: [ebolaseq, population-genomics, Ebola, virus-sequences, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/ebolaseq"
---

## Concepts

- **Tool Overview**: Ebolaseq is a command-line tool for downloading, processing, and analyzing Ebola virus sequences from public databases.
- **Core Function**: Automates the workflow from sequence retrieval to phylogenetic tree construction for Ebola virus analysis.
- **Input/Output**: Input: Accession numbers or search terms. Output: FASTA sequences, alignments, phylogenetic trees.
- **Algorithm**: Retrieves sequences from NCBI GenBank, performs multiple sequence alignment, and constructs phylogenetic trees.
- **Key Features**: Automated sequence downloading, quality filtering, multiple sequence alignment, phylogenetic analysis, visualization support.
- **Installation**: `pip install ebolaseq`

## Pitfalls

- **Internet Access**: Requires internet access to download sequences from NCBI.
- **Database Availability**: Dependent on NCBI database availability.
- **Sequence Quality**: Some downloaded sequences may have low quality.
- **Phylogenetic Model**: Default parameters may need adjustment for specific analyses.
- **Memory Usage**: Large sequence datasets require significant RAM.

## Examples

### Download Ebola sequences
**Args:** `ebolaseq download --output ebola_sequences.fasta`
**Explanation:** Downloads Ebola virus sequences from NCBI GenBank.

### Download with filters
**Args:** `ebolaseq download --output ebola_sequences.fasta --min-length 10000`
**Explanation:** Downloads sequences with minimum length of 10000 bp.

### Align sequences
**Args:** `ebolaseq align --input ebola_sequences.fasta --output aligned.fasta`
**Explanation:** Performs multiple sequence alignment.

### Build phylogenetic tree
**Args:** `ebolaseq tree --input aligned.fasta --output tree.nwk`
**Explanation:** Constructs phylogenetic tree from aligned sequences.

### Complete workflow
**Args:** `ebolaseq pipeline --output results/`
**Explanation:** Runs complete analysis pipeline from download to tree construction.