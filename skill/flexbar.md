---
name: flexbar
category: qc
description: "Flexbar is a flexible tool for barcode and adapter removal from high-throughput sequencing reads."
tags: [flexbar, qc, sequencing, adapter-trimming, barcode, bioinformatics, ngs]
author: oxo-call-community
source_url: "https://github.com/seqan/flexbar"
---

## Concepts
- **Tool Overview**: Flexbar is a fast and flexible tool for preprocessing high-throughput sequencing data. It handles adapter trimming, barcode demultiplexing, quality filtering, and sequence clipping.
- **Core Function**: Removes adapter sequences, barcodes, and low-quality regions from sequencing reads while maintaining high performance and flexibility.
- **Input/Output**: Input: FASTQ files (single-end or paired-end). Output: Cleaned FASTQ files, optional statistics report.
- **Adapter Detection**: Supports automatic adapter detection and trimming using known adapter sequences or de novo detection.
- **Barcode Handling**: Demultiplexes barcoded libraries with support for single, dual, and combinatorial barcodes.
- **Quality Trimming**: Implements Phred-based quality trimming with configurable quality thresholds and window sizes.
- **Installation**: `conda install -c bioconda flexbar` or compile from source. Requires SeqAn library.

## Pitfalls
- **Adapter Sequence Requirements**: Requires known adapter sequences for optimal trimming. Unknown adapters may not be removed.
- **Barcode Mismatches**: Allows limited mismatches but excessive errors cause misassignment. Use high-quality barcodes.
- **Quality Score Encoding**: Ensure correct Phred encoding (Phred+33 or Phred+64). Wrong encoding produces incorrect trimming.
- **Overlapping Reads**: Paired-end reads with extensive overlap may have issues. Use merge tools for overlapping fragments.
- **Memory Usage**: Large datasets require sufficient memory. Use streaming mode for memory-efficient processing.
- **Barcode Order**: Dual barcodes must be in correct order (i5/i7). Incorrect ordering causes demultiplexing errors.

## Examples
### Basic adapter trimming
**Args:** `flexbar -r reads.fastq -a adapters.fasta -t trimmed`
**Explanation:** Trims adapter sequences from single-end reads using provided adapter file.

### Paired-end trimming
**Args:** `flexbar -r reads_R1.fastq -p reads_R2.fastq -a adapters.fasta -t trimmed`
**Explanation:** Trims adapters from paired-end reads and maintains read pairing.

### Barcode demultiplexing
**Args:** `flexbar -r reads.fastq -b barcodes.fasta -t demultiplexed --barcode-error-rate 0.1`
**Explanation:** Demultiplexes barcoded reads allowing 10% barcode mismatch rate.

### Quality and adapter trimming
**Args:** `flexbar -r reads.fastq -a adapters.fasta -t trimmed -q 20 -w 5`
**Explanation:** Trims adapters and applies quality trimming with Q20 threshold and 5-base window.

### With statistics output
**Args:** `flexbar -r reads.fastq -a adapters.fasta -t trimmed --stats`
**Explanation:** Generates statistics report including trimming rates and quality metrics.
