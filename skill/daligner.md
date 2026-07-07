---
name: daligner
category: alignment
description: DALIGNER - Find all significant local alignments between reads
tags: [daligner, alignment, local-alignment, consensus, PacBio]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/DALIGNER/blob/master/README.md"
---

## Concepts

- **Tool Overview**: daligner (v2.0.20240118+) is a tool for finding all significant local alignments between DNA sequences, particularly designed for PacBio Sequel read datasets.
- **Core Function**: Performs fast all-vs-all local alignment to identify overlapping reads and potential consensus regions.
- **Input/Output**: Input: FASTA/FASTQ read files. Output: Alignment records, overlaps.
- **Algorithm**: Uses seed-and-extend approach with advanced filtering for sensitive detection of local alignments.
- **Key Features**: Fast performance, handles large datasets, produces sorted alignment outputs.
- **Installation**: `conda install -c bioconda daligner`

## Pitfalls

- **Input Quality**: Works best with high-quality long reads (PacBio HiFi/CLR).
- **Memory Usage**: Very large datasets may require significant memory.
- **Database Size**: Performance degrades with extremely large read sets.
- **Overlap Threshold**: Adjust overlap parameters based on read length and coverage.
- **Sort Order**: Output alignment sorting is important for downstream processing.

## Examples

### Find all local alignments
**Args:** `daligner -o outputaln inputreads.db`
**Explanation:** Find all significant local alignments between reads in the database.

### Specify k-mer length
**Args:** `daligner -k 20 -o outputaln inputreads.db`
**Explanation:** Use k-mer length of 20 for seeding alignments.

### Process multiple blocks
**Args:** `daligner -md -o outputaln inputreads.db`
**Explanation:** Process multiple blocks for improved sensitivity.
