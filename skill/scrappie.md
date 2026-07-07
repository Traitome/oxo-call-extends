---
name: scrappie
category: sequencing
description: scrappie - Oxford Nanopore basecalling technology demonstrator
tags: ["scrappie", "sequencing", "nanopore", "basecalling"]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/scrappie"
---

## Concepts

- **Tool Overview**: scrappie (v1.4.2) is a technology demonstrator for the Oxford Nanopore Research Algorithms group.
- **Core Function**: Performs basecalling on Oxford Nanopore sequencing data.
- **Algorithm**: Uses neural networks for accurate basecalling from raw signal data.
- **Input/Output**: Accepts raw nanopore signal data and produces base-called sequences.
- **Nanopore Focus**: Specifically designed for Oxford Nanopore sequencing technology.
- **Applications**: Nanopore sequencing analysis, basecalling, and data processing.

## Pitfalls

- **Computational Resources**: Requires significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **GPU Acceleration**: Performance benefits from GPU acceleration.
- **Version Compatibility**: Different versions may have breaking changes.
- **Data Quality**: Results depend on input signal quality.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Basecall fast5 files
**Args:** `scrappie basecall -i reads.fast5 -o sequences.fasta`
**Explanation:** `-i` input FAST5; `-o` output FASTA.

### With GPU
**Args:** `scrappie basecall -i reads.fast5 -o sequences.fasta --gpu`
**Explanation:** `--gpu` enables GPU acceleration.

### Verbose logging
**Args:** `scrappie basecall -i reads.fast5 -o sequences.fasta -v`
**Explanation:** `-v` enables verbose output for debugging.

### Quality filtering
**Args:** `scrappie basecall -i reads.fast5 -o sequences.fasta -q 10`
**Explanation:** `-q 10` filters reads with quality below 10.

### Batch processing
**Args:** `scrappie batch -i fast5_dir/ -o sequences.fasta`
**Explanation:** Processes multiple FAST5 files in batch.

### Model selection
**Args:** `scrappie basecall -i reads.fast5 -o sequences.fasta -m model.rnn`
**Explanation:** `-m` specifies custom basecalling model.

### Output FASTQ
**Args:** `scrappie basecall -i reads.fast5 -o sequences.fastq --fastq`
**Explanation:** `--fastq` outputs FASTQ format with quality scores.