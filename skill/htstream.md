---
name: htstream
category: quality-control
description: HTStream is a quality control and processing pipeline for High Throughput Sequencing data using streaming architecture for efficient processing.
tags: [htstream, quality-control, sequencing, FASTQ, streaming]
author: oxo-call-community
source_url: "https://s4hts.github.io/HTStream"
---

## Concepts

- **Tool Overview**: HTStream is a streaming quality control pipeline that processes sequencing data without intermediate files.
- **Streaming Architecture**: Uses tab-delimited FASTQ format enabling pipelining between tools.
- **Modular Tools**: Includes hts_AdapterTrimmer, hts_CutTrim, hts_QWindowTrim, hts_SuperDeduper, hts_Overlapper, etc.
- **Parallel Processing**: Processes reads concurrently for improved performance.
- **Unix Philosophy**: Designed to work with standard Unix tools via piping.
- **Installation**: `conda install -c bioconda htstream`

## Pitfalls

- **Streaming Format**: Requires tab-delimited FASTQ format for streaming between modules.
- **Tool Chain Order**: Tools must be chained in correct order for proper processing.
- **Memory Management**: Large datasets require sufficient memory for buffering.
- **Quality Thresholds**: Default parameters may need adjustment for specific data.
- **Adapter Sequences**: May require custom adapter sequences for non-standard libraries.
- **Output Format**: Output is tab-delimited FASTQ, requiring conversion for downstream tools.

## Examples

### Basic quality trimming pipeline
**Args:** `hts_AdapterTrimmer -a AGATCGGAAGAGC -i input.fastq | hts_QWindowTrim -q 20 | hts_LengthFilter -m 50`
**Explanation:** Trims adapters, low-quality bases, and filters short reads in a streaming pipeline.

### Paired-end processing
**Args:** `hts_AdapterTrimmer -a AGATCGGAAGAGC -i input_R1.fastq -I input_R2.fastq | hts_SuperDeduper`
**Explanation:** Processes paired-end data with adapter trimming and duplicate removal.

### Overlapping paired reads
**Args:** `hts_Overlapper -i input_R1.fastq -I input_R2.fastq -o overlapping.fastq`
**Explanation:** Merges overlapping paired-end reads into single reads.

### PolyA tail trimming
**Args:** `hts_PolyATTrim -i input.fastq -o trimmed.fastq`
**Explanation:** Trims polyA/polyT tails from sequencing reads.

### Generate statistics
**Args:** `hts_Stats -i input.fastq -o stats.json`
**Explanation:** Computes quality statistics and outputs results in JSON format.