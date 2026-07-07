---
name: spoa
category: alignment
description: SPOA - SIMD partial order alignment for sequences
tags: [spoa, alignment, partial-order, simd, multiple-alignment]
author: oxo-call-community
source_url: "https://github.com/rvaser/spoa/blob/4.1.5/README.md"
---

## Concepts

- **Tool Overview**: spoa (v4.1.5) - A partial order alignment tool
- **Core Function**: Performs SIMD-accelerated partial order alignment of sequences
- **Input/Output**: Accepts sequences; outputs partial order alignments
- **Algorithm**: SIMD partial order alignment algorithm
- **Installation**: `conda install -c bioconda spoa`
- **Key Features**: Partial order alignment, SIMD acceleration, multiple alignment

## Pitfalls

- **Input Requirements**: Requires properly formatted sequences
- **Sequence Quality**: Sequence quality affects alignment accuracy
- **SIMD Support**: SIMD support affects performance
- **Memory Usage**: Large sequence sets require significant memory
- **Output Format**: Output format depends on configuration
- **Alignment Accuracy**: Accuracy depends on sequence quality

## Examples

### Display help
**Args:** `spoa --help`
**Explanation:** Shows available options and usage information.

### Basic partial order alignment
**Args:** `spoa -i sequences.fasta -o alignment.fasta`
**Explanation:** Perform partial order alignment of sequences.

### With alignment mode
**Args:** `spoa -i sequences.fasta -o alignment.fasta --mode local`
**Explanation:** Set alignment mode (local/global).

### With gap penalties
**Args:** `spoa -i sequences.fasta -o alignment.fasta --gap-open 5 --gap-extend 2`
**Explanation:** Set gap penalties for alignment.

### Multiple sequences
**Args:** `spoa -i seq1.fasta seq2.fasta seq3.fasta -o alignment.fasta`
**Explanation:** Align multiple sequence files.

### Output detailed results
**Args:** `spoa -i sequences.fasta -o alignment.fasta --detailed`
**Explanation:** Output detailed alignment information.

### Output consensus
**Args:** `spoa -i sequences.fasta -o alignment.fasta --consensus`
**Explanation:** Output consensus sequence.

### Output statistics
**Args:** `spoa -i sequences.fasta -o alignment.fasta --stats`
**Explanation:** Output alignment statistics.

### Generate report
**Args:** `spoa -i sequences.fasta -o alignment.fasta --report`
**Explanation:** Generate alignment report.

### With threads
**Args:** `spoa -i sequences.fasta -o alignment.fasta -p 8`
**Explanation:** Use multiple threads for alignment.