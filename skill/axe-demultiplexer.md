---
name: axe-demultiplexer
category: qc
description: Axe - Rapid competitive read demultiplexer using trie-based algorithm
tags: [demultiplexing, barcodes, index-splitting, trie-algorithm]
author: oxo-call-community
source_url: "https://github.com/kdm9/axe"
---

## Concepts

- **Tool Overview**: Axe is a rapid competitive read demultiplexer that uses a trie-based algorithm for accurate index matching, even in the presence of sequencing errors.

- **Competitive Matching**: Selects the optimal index present in a read by comparing all possible matches competitively, reducing misassignment.

- **Trie Algorithm**: Uses a trie data structure for efficient index lookup, enabling fast processing of large datasets.

- **Combinatorial Indexing**: Supports combinatorial (dual-index) demultiplexing where forward and reverse indices are combined.

- **Error Tolerance**: Handles sequencing errors in index reads by allowing mismatches while maintaining accuracy.

## Pitfalls

- **Index Uniqueness**: Indices must be sufficiently different from each other. Similar indices increase misassignment rates.

- **Index Length**: Very short indices may have insufficient complexity for unique assignment.

- **Combinatorial Mode**: In combinatorial mode, ensure all index combinations are expected and accounted for.

- **Quality Trimming**: Poor quality index reads may be demultiplexed incorrectly. Consider quality filtering first.

## Examples

### Basic demultiplexing
**Args:** `axe-demultiplexer -b barcodes.tsv -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -o output/`
**Explanation:** Demultiplexes paired-end reads using barcode definitions from TSV file.

### Combinatorial demultiplexing
**Args:** `axe-demultiplexer -b barcodes.tsv -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz --combinatorial -o output/`
**Explanation:** Uses combinatorial dual-index demultiplexing for samples with paired indices.

### Single-end demultiplexing
**Args:** `axe-demultiplexer -b barcodes.tsv -0 reads.fastq.gz -o output/`
**Explanation:** Demultiplexes single-end reads using -0 flag for unpaired input.

### Allow mismatches
**Args:** `axe-demultiplexer -b barcodes.tsv -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz --max-error-rate 0.15 -o output/`
**Explanation:** Allows up to 15% error rate in index matching for more permissive demultiplexing.

### Output unassigned reads
**Args:** `axe-demultiplexer -b barcodes.tsv -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz --unassigned -o output/`
**Explanation:** Saves reads that could not be assigned to any barcode to separate files.
