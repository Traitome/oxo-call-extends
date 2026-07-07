---
name: cdskit
category: sequence-analysis
description: Toolkit for processing protein-coding sequences (CDS)
tags: [cdskit, cds, protein-coding, sequence-analysis, codon]
author: oxo-call-community
source_url: "https://github.com/kfuku52/cdskit"
---

## Concepts

- **Tool Overview**: cdskit is a Python toolkit for processing protein-coding sequences (CDS).
- **Core Function**: Handles DNA sequences using codon-based operations and sequence analysis.
- **Features**: Codon manipulation, sequence extraction, translation, and validation.
- **Input**: FASTA files with CDS sequences.
- **Output**: Processed sequences, translations, and analysis reports.
- **Application**: Genomics analysis, gene prediction validation, and codon usage studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cdskit`

## Pitfalls

- **CDS Format**: Requires valid protein-coding sequences in correct reading frame.
- **Frame Validation**: Sequences must be in-frame and divisible by 3.
- **Stop Codons**: Internal stop codons may cause issues in translation.
- **FASTA Format**: Requires properly formatted FASTA input files.

## Examples

### Extract CDS from FASTA
**Args:** `cdskit extract -i genes.fa -o cds.fa`
**Explanation:** Extracts CDS regions from gene sequences.

### Translate CDS to protein
**Args:** `cdskit translate -i cds.fa -o proteins.fa`
**Explanation:** Translates CDS sequences to protein sequences.

### Check codon usage
**Args:** `cdskit codon_usage -i cds.fa -o codon_usage.tsv`
**Explanation:** Calculates codon usage statistics for CDS sequences.

### Display help
**Args:** `cdskit --help`
**Explanation:** Shows all available options and usage information.