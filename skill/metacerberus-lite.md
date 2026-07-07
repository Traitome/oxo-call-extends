---
name: metacerberus-lite
category: annotation
description: "MetaCerberus with reduced dependencies: Versatile Functional Ontology Assignments for Metagenomes via Hidden Markov Model (HMM) searching with environmental focus of shotgun meta'omics data"
tags: [metacerberus-lite, annotation, metagenomics, HMM]
author: oxo-call-community
source_url: "https://github.com/raw-lab/metacerberus"
---
## Concepts

- **Tool Overview**: MetaCerberus-lite v1.4.0 is a lightweight version of MetaCerberus for functional annotation of metagenomic sequences using Hidden Markov Model (HMM) searching.
- **Core Function**: Assigns functional ontology terms to metagenomic sequences through HMM-based searches against protein databases.
- **Environmental Focus**: Specifically designed for environmental metagenomics data with optimized databases for environmental microbes.
- **Reduced Dependencies**: Stripped-down version with fewer dependencies, ideal for resource-limited environments.
- **Input/Output**: Accepts FASTA-formatted nucleotide or protein sequences; outputs functional annotations in tabular format.
- **Ontology Support**: Supports multiple functional ontologies including GO, KEGG, and COG.

## Pitfalls

- **Database Updates**: Outdated HMM databases can lead to incomplete functional annotations.
- **Sequence Quality**: Poor quality sequences may produce incorrect or incomplete annotations.
- **Memory Constraints**: Large datasets may require significant memory for HMM searches.
- **Annotation Confidence**: Low-confidence matches may require manual curation.
- **Dependency Conflicts**: Lite version may lack some features of the full MetaCerberus.
- **Taxonomic Bias**: Functional annotation databases may have inherent biases.

## Examples

### Basic functional annotation
**Args:** `metacerberus-lite -i sequences.fasta -o annotations.txt`
**Explanation:** Performs functional annotation on input sequences.

### With custom database
**Args:** `metacerberus-lite -i sequences.fasta -d custom_hmm_db/ -o annotations.txt`
**Explanation:** Uses a custom HMM database for annotation.

### Output in JSON format
**Args:** `metacerberus-lite -i sequences.fasta -o annotations.json -f json`
**Explanation:** Outputs annotations in JSON format for easy parsing.

### Filter by confidence score
**Args:** `metacerberus-lite -i sequences.fasta -o annotations.txt -c 0.8`
**Explanation:** Filters annotations to only include matches with confidence >= 0.8.

### Run with multiple threads
**Args:** `metacerberus-lite -i sequences.fasta -o annotations.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.