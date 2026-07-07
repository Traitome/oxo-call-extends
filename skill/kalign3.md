---
name: kalign3
category: alignment
description: Kalign3 - fast and accurate multiple sequence alignment algorithm.
tags: [kalign3, alignment, MSA, sequence, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/TimoLassmann/kalign"
---

## Concepts

- **Tool Overview**: kalign3 (v3.4.0) - A fast and accurate multiple sequence alignment tool.
- **Algorithm**: Uses progressive alignment approach with profile HMMs.
- **Performance**: Optimized for speed and accuracy.
- **Sequence Types**: Supports DNA, RNA, and protein sequences.
- **Format Support**: Supports multiple input/output formats.
- **Parallel Processing**: Supports multi-threaded alignment.

## Pitfalls

- **Memory Requirements**: Large alignments require significant memory.
- **Time Complexity**: Complex alignments can take time.
- **Parameter Tuning**: Default parameters may not be optimal.
- **Format Compatibility**: Some formats may have issues.
- **Version Compatibility**: Different from kalign2 syntax.
- **Long Sequences**: Very long sequences may cause issues.

## Examples

### Basic alignment
**Args:** `kalign -i input.fasta -o aligned.fasta`
**Explanation:** Aligns sequences in FASTA format.

### DNA alignment
**Args:** `kalign -i input.fasta -o aligned.fasta -s DNA`
**Explanation:** Treats input as DNA sequences.

### Protein alignment
**Args:** `kalign -i input.fasta -o aligned.fasta -s PROTEIN`
**Explanation:** Treats input as protein sequences.

### Output in Clustal format
**Args:** `kalign -i input.fasta -o aligned.clustal -f clustal`
**Explanation:** Outputs alignment in Clustal format.

### Use multiple threads
**Args:** `kalign -i input.fasta -o aligned.fasta -t 4`
**Explanation:** Uses 4 threads for parallel alignment.

### Input from stdin
**Args:** `cat input.fasta | kalign -o aligned.fasta`
**Explanation:** Reads input from standard input.