---
name: brawn
category: alignment
description: Python port of MUSCLE's profile-profile mode for aligning sequences with repetitive insertions
tags: [brawn, alignment, muscle, profile-alignment]
author: oxo-call-community
source_url: "https://github.com/SJShaw/brawn"
---

## Concepts

- **Tool Overview**: BRAWN handles repetitive insertions into sequence alignments using MUSCLE's profile-profile mode.
- **Core Function**: Aligns sequences with repetitive insertions that challenge standard MSA tools.
- **Algorithm**: Python port of MUSCLE's profile-profile alignment approach.
- **Input**: FASTA sequences and existing alignment.
- **Output**: Updated alignment with new sequences inserted.
- **Installation**: Install via bioconda: `conda install -c bioconda brawn`

## Pitfalls

- **Profile Mode**: Designed for adding sequences to existing alignments.
- **Memory Usage**: Large alignments require significant memory.
- **Python Required**: Requires Python runtime environment.
- **Alignment Quality**: Depends on quality of input alignment.

## Examples

### Add sequences to alignment
**Args:** `brawn -a existing_alignment.fa -s new_sequences.fa -o updated_alignment.fa`
**Explanation:** Adds new sequences to existing alignment using profile-profile mode.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.

### Check version
**Args:** `--version`
**Explanation:** Displays installed version for reproducibility.
