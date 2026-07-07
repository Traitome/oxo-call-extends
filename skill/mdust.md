---
name: mdust
category: utility
description: Dust masking tool for masking low-complexity regions in nucleotide sequences.
tags: [mdust, sequence-masking, low-complexity]
author: oxo-call-community
source_url: "https://compbio.dfci.harvard.edu/tgi"
---

## Concepts

- **Tool Overview**: mdust masks low-complexity regions in sequences.
- **Core Function**: Identifies and masks low-complexity DNA regions.
- **Dust Algorithm**: Uses the Dust algorithm for masking.
- **Repeat Masking**: Masks repetitive and low-complexity sequences.
- **Input/Output**: Accepts FASTA sequences, produces masked sequences.
- **Installation**: `conda install -c bioconda mdust`

## Pitfalls

- **Masking Sensitivity**: Parameters affect masking stringency.
- **Sequence Quality**: Low-quality sequences affect results.
- **Memory Requirements**: Large sequences require memory.
- **Output Format**: May need format conversion for downstream tools.
- **Over-masking**: May mask biologically relevant regions.
- **Parameter Tuning**: Requires careful threshold adjustment.

## Examples

### Mask low-complexity regions
**Args:** `mdust input.fasta > masked.fasta`
**Explanation:** Masks low-complexity regions in FASTA file.

### With custom window
**Args:** `mdust -w 64 input.fasta > masked.fasta`
**Explanation:** Sets window size to 64.

### Threshold adjustment
**Args:** `mdust -t 20 input.fasta > masked.fasta`
**Explanation:** Sets masking threshold.

### Lowercase masking
**Args:** `mdust -l input.fasta > masked.fasta`
**Explanation:** Converts masked regions to lowercase.

### Help documentation
**Args:** `mdust -h`
**Explanation:** Displays available options.
