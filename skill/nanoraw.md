---
name: nanoraw
category: epigenomics
description: NanoRaw - Raw signal analysis for Oxford Nanopore sequencing data
tags: [nanoraw, epigenomics, nanopore, signal, analysis, modification]
author: oxo-call-community
source_url: "https://github.com/marcus1487/nanoraw"
---

## Concepts

- **Tool Overview**: NanoRaw v0.5 is a tool for analyzing raw signal data from Oxford Nanopore sequencing. It focuses on detecting DNA modifications and performing signal-level analysis.
- **Core Function**: Analyzes raw electrical signal to detect base modifications, perform signal normalization, and generate training data for machine learning models.
- **Algorithm**: Uses signal processing techniques to extract features from raw signal data. Can train models for modification detection.
- **Input Format**: Requires FAST5 files containing raw signal data and aligned BAM files for genomic coordinates.
- **Output**: Produces modification calls, signal-level alignments, and training data for machine learning.
- **Use Case**: Epigenomics research, detecting DNA modifications, generating training data for modification detection models, and signal-level analysis.

## Pitfalls

- **FAST5 Requirements**: Requires access to raw FAST5 files. Basecalled-only data won't work for signal-level analysis.
- **Deprecated**: Note that NanoRaw is no longer actively maintained. Consider using Nanopolish or newer tools for modification detection.
- **Model Training**: Training custom models requires significant computational resources and labeled data.
- **Alignment Quality**: Results depend heavily on alignment quality. Use long-read optimized aligners.
- **Signal Drift**: Signal characteristics may vary across sequencing runs. Consider normalization.
- **Documentation**: Limited documentation available. Refer to source code for detailed usage.

## Examples

### Basic signal analysis
**Args:** `-f fast5_dir -b aligned.bam -r reference.fasta -o output_dir`
**Explanation:** Analyzes Nanopore raw signal data and detects modifications.

### Train modification model
**Args:** `-f fast5_dir -b aligned.bam -r ref.fa -o model/ --train`
**Explanation:** Trains a machine learning model for modification detection.

### Signal normalization
**Args:** `-f fast5_dir -b aligned.bam -r ref.fa -o normalized/ --normalize`
**Explanation:** Normalizes signal data across reads for consistent analysis.

### Generate training data
**Args:** `-f fast5_dir -b aligned.bam -r ref.fa -o training_data/ --generate`
**Explanation:** Generates training data for machine learning models.

### Display help
**Args:** `nanoraw --help`
**Explanation:** Shows all available options for signal analysis.
