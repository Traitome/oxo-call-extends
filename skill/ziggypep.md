---
name: ziggypep
category: protein-analysis
description: Identify signal peptides in protein sequences
tags: [ziggypep, signal-peptide, protein-analysis]
author: oxo-call-community
source_url: "https://github.com/tseemann/ziggypep"
---

## Concepts

- **Tool Overview**: Ziggypep is a free, open-source tool to identify signal peptides in protein sequences
- **Detection Method**: Uses a simplistic method achieving ~72% sensitivity and ~93% specificity
- **Input**: Protein FASTA files, supports gzip/bzip2 compression
- **Output**: Tab-separated format with sequence name, signal peptide length, and signal peptide sequence
- **Installation**: `conda install -c bioconda -c conda-forge ziggypep`
- **Free License**: GPLv3 license, no academic license required

## Pitfalls

- **Prediction Accuracy**: Simpler method may miss some signal peptides compared to SignalP
- **No Probability Scores**: Does not provide confidence scores for predictions
- **No Organism-specific Models**: Unlike SignalP, does not differentiate eukaryotes/prokaryotes
- **Output Format**: Tab-separated without header; use `-s` flag to filter positive results only

## Examples

### Basic prediction
**Args:** `ziggypep proteins.fasta`
**Explanation:** Scan FASTA file for signal peptides, output all results including negatives.

### Only show positive results
**Args:** `ziggypep -s proteins.fasta`
**Explanation:** Use -s flag to output only sequences with detected signal peptides.

### Process compressed files
**Args:** `ziggypep proteins.fasta.gz`
**Explanation:** Directly process gzip-compressed FASTA files without decompression.

### Process multiple files
**Args:** `ziggypep file1.faa file2.faa.gz file3.faa.bz2`
**Explanation:** Process multiple FASTA files in a single command, supporting different compression formats.

### Quiet mode
**Args:** `ziggypep -q proteins.fasta > results.tsv`
**Explanation:** Use -q flag for quiet mode, suppressing progress output during processing.