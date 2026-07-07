---
name: deepbinner
category: qc
description: Deepbinner - signal-level demultiplexer for Oxford Nanopore reads.
tags: [deepbinner, qc, nanopore, demultiplexing, signal-level]
author: oxo-call-community
source_url: "https://github.com/rrwick/Deepbinner"
---

## Concepts

- **Tool Overview**: deepbinner (v0.2.0+) is a deep learning-based tool for demultiplexing Oxford Nanopore sequencing reads at the signal level. It classifies raw signal data to assign reads to specific barcodes.
- **Core Function**: Demultiplexes Nanopore reads by analyzing raw signal data, enabling accurate assignment of reads to barcodes before base calling.
- **Input/Output**: Input: Raw signal files (FAST5), base-called reads (FASTQ). Output: Demultiplexed reads by barcode, summary statistics.
- **Algorithm**: Uses deep neural networks to classify raw signal patterns corresponding to different barcode sequences.
- **Key Features**: Signal-level classification, supports multiple barcode kits, high accuracy, early demultiplexing before base calling.
- **Installation**: `conda install -c bioconda deepbinner`

## Pitfalls

- **Signal Quality**: Requires good quality raw signal data.
- **Barcode Variation**: May not handle non-standard barcodes.
- **Computational Resources**: Requires GPU for optimal performance.
- **Base Calling**: May conflict with base calling software.
- **Training Data**: Performance depends on training barcode diversity.

## Examples

### Demultiplex reads
**Args:** `deepbinner demux -i fast5/ -o demultiplexed/`
**Explanation:** Demultiplex Nanopore reads from FAST5 files.

### With base-called reads
**Args:** `deepbinner demux -i reads.fastq -b barcodes.fasta -o demultiplexed/`
**Explanation:** Demultiplex using base-called reads and barcode sequences.

### Train custom model
**Args:** `deepbinner train -i training_data/ -o custom_model/`
**Explanation:** Train custom demultiplexing model.