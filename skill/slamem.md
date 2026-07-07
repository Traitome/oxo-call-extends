---
name: slamem
category: alignment
description: slaMEM - efficient retrieval of maximal exact matches using a sampled LCP array for sequence alignment
tags: [slamem, alignment, MEM, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/fjdf/slaMEM"
---

## Concepts

- **Tool Overview**: slamem (v0.8.5) - A tool for efficient retrieval of maximal exact matches (MEMs) using a sampled LCP array
- **Core Function**: Identifies maximal exact matches between sequences for use in sequence alignment and comparison
- **Input/Output**: Accepts FASTA sequence files; outputs MEM coordinates and statistics
- **Algorithm**: Implements a sampled LCP array approach optimized for backward search with FM-Index
- **Installation**: `conda install -c bioconda slamem` or compile from source
- **Key Features**: Memory-efficient, competitive performance with state-of-the-art approaches

## Pitfalls

- **Input Format**: Requires properly formatted FASTA files
- **Memory Requirements**: Large sequences may require significant memory for index construction
- **Algorithm Selection**: Default parameters may need adjustment for specific use cases
- **Output Interpretation**: MEM results require downstream processing for alignment
- **Reference Index**: Must build index before performing searches
- **k-mer Size**: Default k-mer size may not be optimal for all datasets

## Examples

### Display help
**Args:** `slamem --help`
**Explanation:** Shows available options and usage information.

### Build index
**Args:** `slamem index -i reference.fasta -o index_prefix`
**Explanation:** Build MEM index from reference sequence.

### Find MEMs
**Args:** `slamem mem -i index_prefix -q query.fasta -o matches.txt`
**Explanation:** Find maximal exact matches between query and reference.

### With minimum length
**Args:** `slamem mem -i index_prefix -q query.fasta -l 50 -o matches.txt`
**Explanation:** Find MEMs with minimum length of 50 bp.

### Batch processing
**Args:** `slamem batch -i index_prefix -d queries/ -o results/`
**Explanation:** Process multiple query sequences in batch.

### Generate statistics
**Args:** `slamem stats -i matches.txt -o stats.txt`
**Explanation:** Generate statistics from MEM matches.

### Compare sequences
**Args:** `slamem compare -a seq1.fasta -b seq2.fasta -o comparison.txt`
**Explanation:** Compare two sequences and find MEMs.