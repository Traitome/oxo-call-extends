---
name: adapterremoval
category: qc
description: The AdapterRemoval v2 tool for merging and clipping reads.
tags: [adapterremoval, qc, adapter-trimming, read-merging, ancient-dna]
author: oxo-call-community
source_url: "https://github.com/MikkelSchubert/adapterremoval"
---

## Concepts

- **Tool Overview**: Tool for adapter trimming, quality filtering, and read merging of high-throughput sequencing data. Version 2.3.4.
- **Core Function**: Removes adapter sequences, trims low-quality bases, and merges overlapping paired-end reads into consensus sequences.
- **Input/Output**: Input is FASTQ reads (single or paired-end); output is trimmed/merged FASTQ files and statistics.
- **Installation**: Install via bioconda: `conda install -c bioconda adapterremoval`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **Ancient DNA**: Widely used in ancient DNA (aDNA) studies where reads are short and overlapping.
- **Read Merging**: Merges overlapping paired-end reads into single consensus sequences with quality scores.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Adapter Specification**: Must specify correct adapter sequences. Incorrect adapters lead to untrimmed adapters in output.
- **Quality Threshold**: Default quality threshold may be too permissive or stringent for your data. Adjust based on quality distribution.
- **Merge Only Overlapping**: Read merging only works for overlapping pairs. Non-overlapping pairs are output separately.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic adapter trimming
**Args:** `--file1 reads_R1.fastq --file2 reads_R2.fastq --output1 trimmed_R1.fastq --output2 trimmed_R2.fastq`
**Explanation:** Trims adapter sequences from paired-end reads and outputs trimmed files.

### Trim and merge overlapping reads
**Args:** `--file1 R1.fq --file2 R2.fq --collapse --output1 trimmed_R1.fq --output2 trimmed_R2.fq --outputcollapsed merged.fq`
**Explanation:** Trims adapters and merges overlapping paired-end reads. Merged reads are written to the collapsed output file.

### Trim with quality filtering
**Args:** `--file1 R1.fq --file2 R2.fq --minquality 20 --minlength 30 --trimns --collapse`
**Explanation:** Trims adapters, filters reads with minimum quality 20 and minimum length 30, removes ambiguous bases (N), and merges overlapping pairs.

### Ancient DNA processing
**Args:** `--file1 R1.fq --file2 R2.fq --collapse --minlength 25 --trim5p --adapter1 AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC --adapter2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTA`
**Explanation:** Full ancient DNA processing: merge overlapping pairs, trim 5' bases (damaged), and specify custom adapter sequences.

### Output detailed statistics
**Args:** `--file1 R1.fq --file2 R2.fq --collapse --settings output.settings`
**Explanation:** Writes detailed trimming and merging statistics to a settings file for quality assessment.
