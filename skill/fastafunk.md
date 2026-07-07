---
name: fastafunk
category: utility
description: "Miscellaneous fasta manipulation tools"
tags: [fastafunk, utility, FASTA, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cov-ert/fastafunk"
---

## Concepts

- **Tool Overview**: fastafunk is a collection of miscellaneous FASTA manipulation tools for sequence processing and analysis.
- **Core Function**: Provides various utilities for manipulating FASTA files including filtering, splitting, merging, and reformatting.
- **Input/Output**: Input: FASTA files. Output: Modified FASTA files, sequence statistics.
- **Algorithm**: Implements efficient sequence parsing and manipulation operations.
- **Key Features**: FASTA filtering, sequence extraction, file splitting, merging, reformatting, batch processing.
- **Installation**: `conda install -c bioconda fastafunk`

## Pitfalls

- **Memory Usage**: Large FASTA files may require significant memory.
- **Format Compatibility**: Requires standard FASTA format.
- **Sequence Quality**: Poor quality sequences may affect results.
- **Duplicate Sequences**: May need manual handling of duplicate entries.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Filter sequences by length
**Args:** `fastafunk filter -i input.fasta -o filtered.fasta --min-length 100`
**Explanation:** Filters sequences by minimum length.

### Extract sequences by ID
**Args:** `fastafunk extract -i input.fasta -o extracted.fasta --ids ids.txt`
**Explanation:** Extracts specific sequences by ID.

### Split FASTA file
**Args:** `fastafunk split -i input.fasta -o output_dir/ --chunks 10`
**Explanation:** Splits FASTA file into multiple chunks.

### Merge FASTA files
**Args:** `fastafunk merge -i files/ -o merged.fasta`
**Explanation:** Merges multiple FASTA files.

### Sequence statistics
**Args:** `fastafunk stats -i input.fasta -o stats.txt`
**Explanation:** Generates sequence statistics.