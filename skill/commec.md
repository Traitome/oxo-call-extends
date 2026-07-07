---
name: commec
category: utility
description: Free open-source tool for DNA sequence screening
tags: [commec, dna-screening, sequence-analysis, bioinformatics, safety]
author: oxo-call-community
source_url: "https://github.com/ibbis-screening/common-mechanism/wiki"
---

## Concepts

- **Tool Overview**: commec is a free, open-source, globally available tool for DNA sequence screening, designed to identify potentially hazardous sequences in synthetic biology applications.
- **Core Function**: Screens DNA sequences against databases of concern to identify sequences that may require additional safety review.
- **Algorithm**: Uses sequence alignment and pattern matching to compare input sequences against curated databases of regulated or hazardous sequences.
- **Input**: DNA sequences in FASTA or other standard formats.
- **Output**: Screening results with matches to sequences of concern and risk assessments.
- **Application**: Synthetic biology safety screening, gene synthesis quality control, and regulatory compliance.
- **Installation**: Install via bioconda: `conda install -c bioconda commec`

## Pitfalls

- **Database Currency**: Results depend on up-to-date screening databases.
- **Threshold Settings**: Sensitivity thresholds affect false positive/negative rates.
- **Sequence Length**: Very short sequences may produce spurious matches.
- **Regulatory Compliance**: May not cover all jurisdiction-specific requirements.
- **Interpretation**: Results require expert interpretation for regulatory decisions.

## Examples

### Screen DNA sequence
**Args:** `commec -i sequence.fasta -o results.txt`
**Explanation:** Screens DNA sequence against databases of concern.

### With custom database
**Args:** `commec -i sequence.fasta -d custom_db/ -o results.txt`
**Explanation:** Uses custom screening database for analysis.

### With detailed report
**Args:** `commec -i sequence.fasta -v -o results.txt`
**Explanation:** Generates detailed verbose report with all matches.

### Display help
**Args:** `commec --help`
**Explanation:** Shows all available options and usage information.