---
name: fasta-splitter
category: formatting
description: "Divides a large FASTA file into a set of smaller, approximately equally sized files"
tags: [fasta-splitter, formatting, FASTA, file-splitting, bioinformatics]
author: oxo-call-community
source_url: "http://kirill-kryukov.com/study/tools/fasta-splitter/"
---

## Concepts

- **Tool Overview**: fasta-splitter is a tool for dividing large FASTA files into smaller, approximately equally sized files.
- **Core Function**: Splits large FASTA files into manageable chunks for easier processing.
- **Input/Output**: Input: Large FASTA file. Output: Multiple smaller FASTA files.
- **Algorithm**: Distributes sequences across output files to achieve roughly equal file sizes.
- **Key Features**: File splitting, size balancing, sequence preservation, multiple output modes, batch processing.
- **Installation**: `conda install -c bioconda fasta-splitter`

## Pitfalls

- **Sequence Integrity**: May split multi-part sequences incorrectly.
- **Memory Usage**: Very large files may require significant memory.
- **Output Size**: Approximate size distribution may vary.
- **Format Compatibility**: Requires standard FASTA format.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic splitting
**Args:** `fasta-splitter --n-parts 10 input.fasta`
**Explanation:** Splits FASTA into 10 parts.

### Split by size
**Args:** `fasta-splitter --max-size 100M input.fasta`
**Explanation:** Splits FASTA into 100MB chunks.

### Output directory
**Args:** `fasta-splitter --n-parts 5 input.fasta --out-dir split_files/`
**Explanation:** Outputs to specified directory.

### Split by sequences
**Args:** `fasta-splitter --n-sequences 1000 input.fasta`
**Explanation:** Splits into files with 1000 sequences each.

### Gzip output
**Args:** `fasta-splitter --n-parts 10 input.fasta --compress`
**Explanation:** Compresses output files.