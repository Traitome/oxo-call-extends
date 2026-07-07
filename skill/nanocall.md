---
name: nanocall
category: utility
description: NanoCall - Oxford Nanopore basecaller for raw signal to sequence conversion
tags: [nanocall, utility, nanopore, basecalling, signal, fast5]
author: oxo-call-community
source_url: "https://github.com/mateidavid/nanocall"
---

## Concepts

- **Tool Overview**: NanoCall v0.7.4 is an open-source basecaller for Oxford Nanopore sequencing data. It converts raw electrical signal from Nanopore sequencers into nucleotide sequences (FASTQ).
- **Core Function**: Translates raw signal data from FAST5 files into base-called reads using Hidden Markov Models or neural network-based approaches.
- **Algorithm**: Uses a combination of signal processing and statistical modeling to identify nucleotide transitions from the raw current signal. Can use either HMM or deep learning models.
- **Input Format**: Requires FAST5 files containing raw signal data from Oxford Nanopore sequencing runs. Supports both single and multi-read FAST5 formats.
- **Output**: Produces FASTQ files containing base-called sequences with quality scores. Can also output signal-level data for downstream analysis.
- **Use Case**: Basecalling Nanopore sequencing data, especially for custom or research purposes where open-source tools are preferred.

## Pitfalls

- **FAST5 Format**: Requires proper FAST5 file format. Mixed old/new formats may cause issues. Use ont-fast5-api for format conversion if needed.
- **GPU Acceleration**: Neural network models may require GPU for reasonable performance. CPU-only mode is significantly slower.
- **Model Selection**: Different basecalling models have different accuracy/speed trade-offs. Choose appropriately based on your needs.
- **Signal Drift**: Over long sequencing runs, signal characteristics may change. Regular model updates may be needed.
- **Quality Scores**: Basecall quality scores may not be perfectly calibrated. Validate with known reference sequences.
- **Deprecated**: Note that many Nanopore users now use Guppy (ONT's official basecaller) instead of NanoCall.

## Examples

### Basic basecalling
**Args:** `-i fast5_dir -o output.fastq`
**Explanation:** Standard NanoCall workflow. Basecalls all FAST5 files in the input directory.

### Use GPU acceleration
**Args:** `-i fast5_dir -o output.fastq --gpu`
**Explanation:** Uses GPU for accelerated basecalling with neural network models.

### Select model
**Args:** `-i fast5_dir -o output.fastq -m r941_min_high_g360`
**Explanation:** Specifies a specific basecalling model (R9.4.1, high accuracy).

### Output signal data
**Args:** `-i fast5_dir -o output.fastq --signal_out signal.tsv`
**Explanation:** Outputs raw signal data alongside base-called sequences.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.
