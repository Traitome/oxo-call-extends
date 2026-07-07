---
name: neffy-cli
category: formatting
description: NEFFy CLI is a tool for calculating effective number of codons (NEFF) and converting multiple sequence alignment (MSA) files.
tags: [neffy-cli, formatting, neff, msa, bioinformatics]
author: oxo-call-community
source_url: "https://maryam-haghani.github.io/NEFFy"
---

## Concepts

- **Tool Overview**: NEFFy CLI calculates the effective number of codons (NEFF) and processes multiple sequence alignments.
- **Core Function**: Computes NEFF values and converts between MSA formats.
- **Algorithm**: Implements codon usage bias calculations and MSA format conversion.
- **Input Format**: Accepts FASTA, Clustal, and other MSA formats.
- **Output**: Produces NEFF statistics and converted MSA files.
- **Use Case**: Codon usage analysis, evolutionary biology, sequence alignment processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Alignment Quality**: Results depend on input alignment quality.
- **Format Compatibility**: May not support all MSA formats.
- **Large Alignments**: Processing very large alignments requires memory.
- **Codon Table**: Requires appropriate codon table selection.
- **Ambiguous Codons**: May struggle with ambiguous codon positions.

## Examples

### Display help
**Args:** `neffy-cli --help`
**Explanation:** Shows available options and usage instructions.

### Calculate NEFF
**Args:** `neffy-cli neff -i alignment.fasta -o neff_results.tsv`
**Explanation:** Calculates NEFF values from alignment.

### Convert MSA format
**Args:** `neffy-cli convert -i input.clustal -o output.fasta -f fasta`
**Explanation:** Converts MSA to FASTA format.

### Multiple files
**Args:** `neffy-cli neff -i alignments/ -o results/`
**Explanation:** Processes multiple alignment files.

### Codon table
**Args:** `neffy-cli neff -i alignment.fasta -c 11 -o results.tsv`
**Explanation:** Uses codon table 11 (bacterial).

### Detailed output
**Args:** `neffy-cli neff -i alignment.fasta -v -o detailed_results.tsv`
**Explanation:** Produces verbose output with additional statistics.