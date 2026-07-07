---
name: oases
category: expression
description: Oases is a de novo transcriptome assembler for short-read RNA sequencing data.
tags: [oases, expression, transcriptome-assembly, rna-seq]
author: oxo-call-community
source_url: "https://github.com/dzerbino/oases"
---

## Concepts

- **Tool Overview**: Oases assembles transcriptomes de novo from short-read RNA-seq data.
- **Core Function**: Reconstructs full-length transcripts from sequencing reads.
- **Algorithm**: Uses de Bruijn graph approach for assembly.
- **Input Format**: Accepts FASTQ sequencing reads.
- **Output**: Produces assembled transcript sequences in FASTA format.
- **Use Case**: Transcriptome assembly, gene discovery, and RNA-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require significant memory.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Computational Cost**: Assembly can be computationally intensive.
- **Contig Quality**: Assembly quality varies with input data.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `oases --help`
**Explanation:** Shows available options and usage instructions.

### Assemble transcriptome
**Args:** `oases -o output/ -reads reads.fastq`
**Explanation:** Runs de novo transcriptome assembly.

### With k-mer size
**Args:** `oases -o output/ -reads reads.fastq -k 21`
**Explanation:** Sets k-mer size to 21.

### Paired-end reads
**Args:** `oases -o output/ -paired -reads reads_1.fastq -reads2 reads_2.fastq`
**Explanation:** Processes paired-end reads.

### Multiple k-mer sizes
**Args:** `oases -o output/ -reads reads.fastq -k 21,25,29`
**Explanation:** Uses multiple k-mer sizes.

### Strand-specific
**Args:** `oases -o output/ -reads reads.fastq --strand-specific`
**Explanation:** Handles strand-specific sequencing data.

### Verbose mode
**Args:** `oases -o output/ -reads reads.fastq -v`
**Explanation:** Runs with verbose output.