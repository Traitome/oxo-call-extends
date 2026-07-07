---
name: dialign2
category: alignment
description: DIALIGN2 - Multiple sequence alignment with external information support.
tags: [dialign2, alignment, multiple-sequence, external-information]
author: oxo-call-community
source_url: "http://dialign.gobics.de"
---

## Concepts

- **Tool Overview**: dialign2 (v2.2.1+) is a multiple sequence alignment program that can incorporate external information for improved alignment quality.
- **Core Function**: Creates multiple sequence alignments using a segment-based approach, allowing integration of external constraints like structural or functional information.
- **Input/Output**: Input: FASTA sequences, optional external constraint files. Output: Multiple sequence alignment in various formats.
- **Algorithm**: Uses segment-to-segment comparison approach with dynamic programming for optimal alignment.
- **Key Features**: External constraint support, segment-based alignment, multiple output formats, progressive alignment strategy.
- **Installation**: `conda install -c bioconda dialign2`

## Pitfalls

- **Input Requirements**: Requires sequences in FASTA format with proper headers.
- **Sequence Length**: May struggle with very long sequences or large datasets.
- **Memory Usage**: May require significant memory for large alignments.
- **External Format**: External constraint files must follow specific format requirements.
- **Computational Time**: Alignment of many sequences can be time-consuming.

## Examples

### Basic multiple sequence alignment
**Args:** `dialign2 -fa input.fa -out aligned.fa`
**Explanation:** Performs multiple sequence alignment using default parameters.

### With external constraints
**Args:** `dialign2 -fa input.fa -con constraints.txt -out aligned.fa`
**Explanation:** Incorporate external constraint information into alignment.

### Output in Clustal format
**Args:** `dialign2 -fa input.fa -out aligned.aln -f clustal`
**Explanation:** Output alignment in Clustal format for downstream tools.

### Use progressive mode
**Args:** `dialign2 -fa input.fa -out aligned.fa -prog`
**Explanation:** Use progressive alignment strategy for improved accuracy.

### Set gap opening penalty
**Args:** `dialign2 -fa input.fa -out aligned.fa -gapopen 10`
**Explanation:** Adjust gap opening penalty to control alignment sensitivity.