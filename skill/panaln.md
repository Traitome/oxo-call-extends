---
name: panaln
category: alignment
description: Panaln provides pangenome indexing for efficient read alignment.
tags: [panaln, alignment, pangenome, read-mapping]
author: oxo-call-community
source_url: "https://github.com/Lilu-guo/Panaln"
---

## Concepts

- **Tool Overview**: Panaln indexes pangenomes for fast read alignment.
- **Core Function**: Creates pangenome index and aligns reads.
- **Algorithm**: Uses pangenome-aware indexing strategy.
- **Input Format**: Accepts pangenome FASTA and sequencing reads.
- **Output**: Produces aligned reads in SAM/BAM format.
- **Use Case**: Pangenome analysis, population genomics, and variant calling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large pangenomes require memory.
- **Index Size**: Index files can be large.
- **Computational Cost**: Indexing can be time-consuming.
- **Reference Quality**: Results depend on pangenome quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `panaln --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `panaln index -i pangenome.fasta -o index/`
**Explanation:** Creates pangenome index.

### Align reads
**Args:** `panaln align -x index/ -i reads.fastq -o alignments.sam`
**Explanation:** Aligns reads to pangenome.

### Output BAM
**Args:** `panaln align -x index/ -i reads.fastq -o alignments.bam --bam`
**Explanation:** Outputs in BAM format.

### Verbose mode
**Args:** `panaln align -v -x index/ -i reads.fastq -o alignments.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `panaln align -t 16 -x index/ -i reads.fastq -o alignments.sam`
**Explanation:** Uses 16 threads for parallel processing.

### Paired-end reads
**Args:** `panaln align -x index/ -1 reads_1.fastq -2 reads_2.fastq -o alignments.sam`
**Explanation:** Aligns paired-end reads.