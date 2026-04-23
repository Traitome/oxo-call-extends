---
name: dig2
category: utility
description: In silico digester of protein sequences for MS/MS fragment simulation.
tags: [dig2, utility, proteomics, digestion, msms]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: dig2 v1.0 - In silico protein sequence digester supporting various enzymes and MS/MS fragment generation.
- **Core Function**: Simulates enzymatic digestion of proteins and generates CID/ECD/ETD fragments for mass spectrometry.
- **Input/Output**: Expects protein FASTA files; outputs digested peptides and fragment ions.
- **Installation**: `conda install -c bioconda dig2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires protein sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dig2 --input proteins.fa --enzyme trypsin --output peptides.tsv`
**Explanation:** Simulates trypsin digestion of protein sequences.
