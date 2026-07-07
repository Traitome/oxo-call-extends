---
name: strobemap
category: alignment
description: Efficient string matching using strobemers for sequence alignment.
tags: [strobemap, strobemers, sequence-matching, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ksahlin/strobemers"
---

## Concepts

- **Tool Overview**: strobemap (v0.0.2) is a tool for efficient string matching using strobemers.
- **Core Function**: Performs fast sequence matching using strobemer-based indexing.
- **Algorithm**: Uses strobemers (dynamic-length seeds) for efficient sequence comparison.
- **Input/Output**: Input: Sequence files (FASTA/FASTQ); Output: Matching results with positions.
- **Applications**: Sequence alignment, read mapping, sequence comparison.
- **Installation**: `conda install -c bioconda strobemap` or download from GitHub.

## Pitfalls

- **Read Length**: Optimal for specific sequence lengths.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect matching accuracy.
- **Index Building**: Requires index building before matching.
- **Sequence Quality**: Low-quality sequences affect matching accuracy.

## Examples

### Display help
**Args:** `strobemap --help`
**Explanation:** Shows available options and usage information.

### Basic sequence matching
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt`
**Explanation:** Match query sequences against database.

### With custom k-mer size
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt -k 15`
**Explanation:** Use k-mer size of 15 for strobemers.

### Verbose mode
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output alignment
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt --align`
**Explanation:** Output alignments for matched sequences.

### Batch processing
**Args:** `strobemap -i queries/ -d database.fasta -o results/`
**Explanation:** Process multiple query files together.

### Filter by quality
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt -q 20`
**Explanation:** Filter matches by quality score.

### Include statistics
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt --stats`
**Explanation:** Generate statistics about matches.

### Generate report
**Args:** `strobemap -i query.fasta -d database.fasta -o matches.txt --report`
**Explanation:** Generate comprehensive HTML report.
