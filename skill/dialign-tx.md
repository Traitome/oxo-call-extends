---
name: dialign-tx
category: alignment
description: DIALIGN-TX - Segment-based multiple sequence alignment tool.
tags: [dialign-tx, alignment, multiple-sequence, segment-based]
author: oxo-call-community
source_url: "https://dialign.gobics.de"
---

## Concepts

- **Tool Overview**: dialign-tx (v1.0.2+) is a segment-based multiple sequence alignment tool using greedy and progressive approaches for improved accuracy.
- **Core Function**: Aligns sequences based on segment-to-segment comparisons rather than single residue alignment, capturing conserved regions more effectively.
- **Input/Output**: Input: FASTA sequences. Output: Multiple sequence alignment in various formats.
- **Algorithm**: Combines greedy segment extension with progressive alignment strategies for robust multiple sequence alignment.
- **Key Features**: Segment-based approach, greedy and progressive strategies, improved handling of distantly related sequences, multiple output formats.
- **Installation**: `conda install -c bioconda dialign-tx`

## Pitfalls

- **Input Requirements**: Requires sequences in FASTA format.
- **Sequence Diversity**: May struggle with very divergent sequences.
- **Memory Usage**: May require significant memory for large datasets.
- **Computational Time**: Progressive alignment can be computationally intensive.
- **Output Format**: Default format may require conversion for some downstream tools.

## Examples

### Basic segment-based alignment
**Args:** `dialign-tx -fa input.fa -out aligned.fa`
**Explanation:** Performs segment-based multiple sequence alignment.

### Use greedy mode only
**Args:** `dialign-tx -fa input.fa -out aligned.fa -greedy`
**Explanation:** Use greedy alignment strategy for faster results.

### Output in FASTA format
**Args:** `dialign-tx -fa input.fa -out aligned.fa -f fasta`
**Explanation:** Output alignment in FASTA format.

### Set segment length threshold
**Args:** `dialign-tx -fa input.fa -out aligned.fa -minlen 20`
**Explanation:** Set minimum segment length for alignment.

### Generate alignment statistics
**Args:** `dialign-tx -fa input.fa -out aligned.fa -stats stats.txt`
**Explanation:** Generate alignment quality statistics.