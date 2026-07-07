---
name: dnp-diprofile
category: utility
description: DNPattern tools - Dinucleotide frequency profile analysis for DNA sequences.
tags: [dnp-diprofile, utility, dinucleotide, frequency-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/erinijapranckeviciene/dnpatterntools"
---

## Concepts

- **Tool Overview**: dnp-diprofile computes dinucleotide frequency profiles for DNA sequences.
- **Core Function**: Calculates the frequency of all 16 dinucleotide combinations across sequences.
- **Input/Output**: Input: FASTA DNA sequences. Output: Dinucleotide frequency tables and statistics.
- **Algorithm**: Counts dinucleotide occurrences and computes relative frequencies.
- **Key Features**: Dinucleotide counting, frequency normalization, strand-specific analysis, comparative profiling.
- **Installation**: `conda install -c bioconda dnp-diprofile`

## Pitfalls

- **Input Requirements**: Requires DNA sequences; RNA sequences are not supported.
- **Sequence Length**: Short sequences may produce unreliable frequency estimates.
- **Ambiguous Bases**: Ns and ambiguous characters are typically ignored.
- **Normalization**: Different normalization methods can affect results.
- **Output Size**: Detailed output for many sequences can be large.
- **Comparative Analysis**: Requires similar sequence lengths for meaningful comparison.

## Examples

### Compute dinucleotide profile
**Args:** `dnp-diprofile --input sequences.fa --output profile.tsv`
**Explanation:** Calculates dinucleotide frequency profile for input sequences.

### Strand-specific analysis
**Args:** `dnp-diprofile --input sequences.fa --output profile.tsv --strand-specific`
**Explanation:** Reports frequencies separately for forward and reverse strands.

### Normalized output
**Args:** `dnp-diprofile --input sequences.fa --output profile.tsv --normalize`
**Explanation:** Normalizes frequencies to sum to 1.0.

### Compare profiles
**Args:** `dnp-diprofile --compare seq1.fa seq2.fa --output comparison.tsv`
**Explanation:** Compares dinucleotide profiles between two sequences.

### With sliding window
**Args:** `dnp-diprofile --input sequences.fa --output profile.tsv --window 500`
**Explanation:** Computes profiles in sliding windows of 500bp.

### Batch processing
**Args:** `dnp-diprofile --input-dir fasta_files/ --output-dir profiles/`
**Explanation:** Processes multiple FASTA files and generates individual profiles.