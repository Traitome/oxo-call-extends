---
name: ispcr
category: utility
description: In silico PCR tool for designing and testing PCR primers against reference sequences.
tags: [ispcr, utility, PCR, primer design]
author: oxo-call-community
source_url: "https://users.soe.ucsc.edu/~kent/"
---

## Concepts

- **In Silico PCR**: Simulates PCR amplification in silico using primer sequences.
- **Primer Testing**: Tests primer pairs against reference sequences to predict amplification products.
- **Amplicon Prediction**: Predicts the size and sequence of PCR products.
- **Specificity Analysis**: Evaluates primer specificity against reference genomes.
- **Multiplex PCR**: Supports analysis of multiple primer pairs simultaneously.
- **Output Formats**: Generates output in various bioinformatics formats.

## Pitfalls

- **Primer Design**: Poor primer design leads to incorrect amplification predictions.
- **Reference Genome Quality**: Incomplete reference genomes affect prediction accuracy.
- **Amplicon Size Limits**: Very long amplicons may not be accurately predicted.
- **Sequence Similarity**: Highly similar sequences can produce false positives.
- **Parameter Sensitivity**: Results may be sensitive to alignment parameters.
- **Ambiguous Results**: Multiple potential binding sites can complicate interpretation.

## Examples

### Basic in silico PCR
**Args:** `ispcr -i genome.fasta -p primers.txt -o results.txt`
**Explanation:** Performs in silico PCR using primers against a reference genome.

### Single primer pair
**Args:** `ispcr -i genome.fasta -f "ATGCTGAA" -r "TTACGCTA" -o amplicon.txt`
**Explanation:** Tests a single primer pair against the reference genome.

### Multiple primer pairs
**Args:** `ispcr -i genome.fasta -p primers.txt -m -o multiplex_results.txt`
**Explanation:** Analyzes multiple primer pairs in multiplex mode.

### With specificity check
**Args:** `ispcr -i genome.fasta -p primers.txt -s -o results.txt`
**Explanation:** Performs specificity analysis for primer pairs.

### Output FASTA
**Args:** `ispcr -i genome.fasta -p primers.txt -fasta -o amplicons.fasta`
**Explanation:** Outputs predicted amplicon sequences in FASTA format.

### Quality filtering
**Args:** `ispcr -i genome.fasta -p primers.txt -q 30 -o filtered_results.txt`
**Explanation:** Filters results based on primer quality score.