---
name: tr-trimmer
category: utility
description: TR-Trimmer - Tool for trimming terminal repeats from sequences.
tags: [tr-trimmer, repeat-trimming, sequence-processing, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/compbio/tr-trimmer"
---

## Concepts

- **Tool Overview**: TR-Trimmer - A tool for trimming terminal repeats from DNA sequences.
- **Core Function**: Identifies and removes terminal repeats from sequence ends.
- **Input**: Sequence files (FASTA), optional repeat motifs.
- **Output**: Trimmed sequences, trimming statistics.
- **Installation**: `pip install tr-trimmer` or `conda install -c bioconda tr-trimmer`
- **Use Case**: Sequence cleaning, repeat removal, data preprocessing.

## Pitfalls

- **Repeat Detection**: May miss complex repeat patterns.
- **Over-trimming**: May trim legitimate sequence.

## Examples

### Trim terminal repeats
**Args:** `tr-trimmer -i sequences.fasta -o trimmed.fasta`
**Explanation:** Trim terminal repeats from sequences.

### With custom motif
**Args:** `tr-trimmer -i reads.fastq -m TTAGGG -o clean.fastq`
**Explanation:** Trim specific repeat motif from sequence ends.
