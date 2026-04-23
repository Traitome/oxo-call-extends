---
name: afterqc
category: qc
description: Automatic filtering, trimming, error removing and quality control for FASTQ data
tags: [qc, fastq, trimming, filtering, quality-control, error-correction]
author: oxo-call-community
source_url: "https://github.com/OpenGene/AfterQC"
---

## Concepts

- **Tool Overview**: AfterQC automatically filters, trims, and corrects errors in FASTQ files, generating quality control reports and separating good/bad reads.
- **Core Function**: Performs automatic quality assessment, adapter trimming, error correction in overlapping paired-end reads, and separates high-quality from low-quality reads.
- **Input/Output**: Input: FASTQ files (single or paired-end). Output: Three folders - good/ (high-quality reads), bad/ (filtered reads), QC/ (HTML reports).
- **Automatic Detection**: Automatically detects trimming positions, adapter sequences, and quality thresholds without manual configuration.
- **Installation**: Install via bioconda: `conda install -c bioconda afterqc`

## Pitfalls

- **Python Performance**: Running with PyPy instead of CPython can provide 3x speedup for large datasets.
- **Successor Tool**: Author recommends fastp (C++ implementation) for better performance with multi-threading support.
- **Automatic Mode**: Default settings work automatically but may not be optimal for all sequencing platforms - adjust parameters as needed.
- **Gzip Handling**: Input gzip compression is auto-detected; use `-z` to force gzip output for uncompressed inputs.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available command line options and their default values.

### Process entire folder automatically
**Args:** `-d /path/to/fastq_folder`
**Explanation:** Automatically processes all FASTQ files in the folder, creating good/, bad/, and QC/ subdirectories.

### Process paired-end files
**Args:** `-1 R1.fastq.gz -2 R2.fastq.gz`
**Explanation:** Processes paired-end FASTQ files, performing overlap-based error correction.

### Process single-end file
**Args:** `-1 single.fastq`
**Explanation:** Processes a single FASTQ file without paired-end error correction features.

### Quality control only (no filtering)
**Args:** `-1 R1.fastq -2 R2.fastq --qc_only`
**Explanation:** Generates QC reports without filtering or trimming, useful for initial data assessment.

### Custom quality thresholds
**Args:** `-1 R1.fastq -2 R2.fastq -q 25 -u 5 -n 3`
**Explanation:** Uses Q25 quality threshold, allows max 5 unqualified bases, and max 3 N bases per read.

### Custom trimming parameters
**Args:** `-1 R1.fastq -2 R2.fastq -f 5 -t 3 -s 50`
**Explanation:** Trims 5 bases from front, 3 from tail, requires minimum 50bp after trimming.

### Enable polyG trimming for NovaSeq
**Args:** `-1 R1.fastq -2 R2.fastq -p 20 -a 3`
**Explanation:** Filters polyG sequences ≥20bp with up to 3 mismatches allowed, important for NovaSeq data.

### Output with gzip compression
**Args:** `-1 R1.fastq -2 R2.fastq -z --compression 6`
**Explanation:** Forces gzip output with compression level 6 for storage efficiency.
