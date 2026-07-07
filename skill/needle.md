---
name: needle
category: expression
description: Needle is a fast and space-efficient pre-filter for quantifying very large collections of nucleotide sequences.
tags: [needle, expression, quantification, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/seqan/needle"
---

## Concepts

- **Tool Overview**: Needle is a pre-filter tool for efficiently quantifying large collections of nucleotide sequences.
- **Core Function**: Rapidly approximates sequence quantification for very large datasets.
- **Algorithm**: Uses advanced indexing and filtering techniques for fast sequence matching.
- **Input Format**: Accepts FASTQ reads and reference sequences in FASTA format.
- **Output**: Produces quantification estimates and mapping statistics.
- **Use Case**: RNA-seq quantification, metagenomics analysis, and large-scale sequence comparison.

## Pitfalls

- **Approximate Results**: Provides approximate quantification, not exact counts.
- **Memory Usage**: Large datasets require significant memory.
- **Version Differences**: Options may vary between versions.
- **Reference Requirements**: Requires indexed reference sequences.
- **Accuracy Trade-off**: Speed improvements may sacrifice some accuracy.
- **Format Compatibility**: May not support all sequence formats.

## Examples

### Display help
**Args:** `needle --help`
**Explanation:** Shows available options and usage instructions.

### Basic quantification
**Args:** `needle quantify -i reads.fastq -r reference.fasta -o counts.tsv`
**Explanation:** Quantifies reads against reference sequences.

### Build index
**Args:** `needle index -r reference.fasta -o index/`
**Explanation:** Builds index for reference sequences.

### Quantify with index
**Args:** `needle quantify -i reads.fastq --index index/ -o counts.tsv`
**Explanation:** Uses pre-built index for faster quantification.

### Paired-end reads
**Args:** `needle quantify -1 reads_R1.fastq -2 reads_R2.fastq -r ref.fasta -o counts.tsv`
**Explanation:** Quantifies paired-end reads.

### Gzipped input
**Args:** `needle quantify -i reads.fastq.gz -r ref.fasta -o counts.tsv`
**Explanation:** Processes gzipped FASTQ file.

### Threshold filtering
**Args:** `needle quantify -i reads.fastq -r ref.fasta -t 0.9 -o counts.tsv`
**Explanation:** Sets minimum similarity threshold to 0.9.