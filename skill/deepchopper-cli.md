---
name: deepchopper-cli
category: metagenomics
description: DeepChopper CLI - chimera artifact detection in Nanopore Direct RNA sequencing.
tags: [deepchopper-cli, metagenomics, chimera-detection, nanopore, RNA-seq]
author: oxo-call-community
source_url: "https://github.com/ylab-hi/DeepChopper"
---

## Concepts

- **Tool Overview**: deepchopper-cli (v1.2.9+) is a CLI tool for the DeepChopper genomic language model, designed to detect chimera artifacts in Nanopore Direct RNA sequencing data.
- **Core Function**: Identifies and removes chimeric sequences from Nanopore RNA sequencing data using deep learning.
- **Input/Output**: Input: FASTQ reads from Nanopore Direct RNA sequencing. Output: Cleaned reads, chimera predictions, summary report.
- **Algorithm**: Uses transformer-based genomic language model to detect artificial chimeric sequences.
- **Key Features**: Chimera detection, genomic language model, supports Direct RNA sequencing, high accuracy, batch processing.
- **Installation**: `conda install -c bioconda deepchopper-cli`

## Pitfalls

- **RNA-specific**: Optimized for RNA sequencing; may not work well for DNA.
- **Computational Resources**: Requires GPU for optimal performance.
- **Model Version**: Different models may give different results.
- **Read Length**: May struggle with very short reads.
- **Training Data**: Performance depends on training dataset.

## Examples

### Detect chimeras
**Args:** `deepchopper detect -i reads.fastq -o clean_reads.fastq`
**Explanation:** Detect and filter chimeric sequences from reads.

### With probability threshold
**Args:** `deepchopper detect -i reads.fastq -o clean_reads.fastq -t 0.9`
**Explanation:** Set 90% probability threshold for chimera detection.

### Generate report
**Args:** `deepchopper detect -i reads.fastq -o clean_reads.fastq --report`
**Explanation:** Generate detailed report of chimera detection.