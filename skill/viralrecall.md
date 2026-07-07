---
name: viralrecall
category: bioinformatics
description: ViralRecall - Viral sequence recall tool.
tags: [viralrecall, viral-genomics, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/viralrecall/"
---

## Concepts

- **Tool Overview**: ViralRecall - Identifies known viral sequences.
- **Core Function**: Recalls known viral sequences from sequencing data.
- **Input**: FASTQ or FASTA files.
- **Output**: Identified viral sequences.
- **Installation**: Install via pip or conda
- **Use Case**: Virus detection, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Database**: Requires viral sequence database.

## Examples

### Recall sequences
**Args:** `viralrecall -i reads.fastq -o viral.fasta`
**Explanation:** Recall viral sequences.

### With options
**Args:** `viralrecall -i reads.fastq -o viral.fasta -d viral_db`
**Explanation:** Use custom database.
