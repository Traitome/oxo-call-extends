---
name: igfinder
category: expression
description: A tool to extract Igh and Igl/Igk gene sequences from assembled transcripts
tags: [igfinder, immunoglobulin, gene extraction, BCR]
author: oxo-call-community
source_url: "https://tx.bioreg.kyushu-u.ac.jp/igfinder"
---

## Concepts

- **Tool Overview**: igfinder is a specialized tool designed to extract immunoglobulin heavy (IgH) and light (IgL/IgK) chain gene sequences from assembled transcriptome data
- **Core Function**: Identifies and extracts V(D)J gene segments from assembled transcripts, enabling analysis of antibody repertoire diversity
- **Input/Output**: Accepts assembled transcript sequences in FASTA format; outputs extracted Ig gene sequences with annotations
- **Installation**: `conda install -c bioconda igfinder`
- **Dependencies**: Requires biopython and numpy libraries

## Pitfalls

- **Version Compatibility**: igfinder v1.0 requires Python 2.7.x, which may conflict with modern Python environments
- **Input Quality**: Poorly assembled transcripts can lead to incomplete or incorrect gene extraction
- **Reference Database**: Accuracy depends on the quality and completeness of the germline gene reference database
- **Chimeric Sequences**: May misinterpret chimeric transcripts as legitimate Ig gene sequences
- **Memory Usage**: Processing large transcriptome datasets may require significant memory resources

## Examples

### Extract Ig gene sequences from transcripts
**Args:** `igfinder -i assembled_transcripts.fasta -o ig_sequences.fasta`
**Explanation:** Processes assembled transcript sequences and extracts immunoglobulin gene segments.

### Extract only Ig heavy chain sequences
**Args:** `igfinder -i transcripts.fasta -o igh_sequences.fasta --chain heavy`
**Explanation:** Filters output to include only heavy chain (IgH) gene sequences.

### Extract only Ig light chain sequences
**Args:** `igfinder -i transcripts.fasta -o igl_sequences.fasta --chain light`
**Explanation:** Filters output to include only light chain (IgL/IgK) gene sequences.

### Include verbose output
**Args:** `igfinder -i transcripts.fasta -o ig_sequences.fasta -v`
**Explanation:** Provides detailed processing information and statistics during extraction.

### Use custom germline database
**Args:** `igfinder -i transcripts.fasta -o ig_sequences.fasta -d custom_germline.fasta`
**Explanation:** Uses a user-provided germline gene database for improved matching accuracy.
