---
name: notramp
category: alignment
description: NoTrAmp provides super-fast normalization and trimming for amplicon sequencing data (long and short reads).
tags: [notramp, alignment, trimming, normalization, amplicon]
author: oxo-call-community
source_url: "https://github.com/simakro/NoTrAmp.git"
---

## Concepts

- **Tool Overview**: NoTrAmp performs fast trimming and read-depth normalization of amplicon reads.
- **Core Function**: Caps coverage of each amplicon and trims to appropriate length.
- **Algorithm**: Implements efficient trimming and normalization in single clipping step.
- **Input Format**: Accepts FASTQ reads from Illumina, ONT, or PacBio platforms.
- **Output**: Produces trimmed and normalized FASTQ files.
- **Use Case**: Amplicon sequencing, targeted sequencing, and multiplexed amplicon panels.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Length**: Short reads may require adjusting minimum alignment length.
- **Barcode Removal**: Requires proper barcode/adapter sequences.
- **Memory Usage**: Large datasets require memory.
- **Amplicon Size**: Optimized for specific amplicon sizes.
- **Validation**: Results should be validated for trimming accuracy.

## Examples

### Display help
**Args:** `notramp --help`
**Explanation:** Shows available options and usage instructions.

### Basic trimming
**Args:** `notramp -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims amplicon reads to appropriate length.

### With normalization
**Args:** `notramp -i reads.fastq -o trimmed.fastq -c 1000`
**Explanation:** Caps coverage at 1000 reads per amplicon.

### Long reads mode
**Args:** `notramp -i reads.fastq -o trimmed.fastq --long-reads`
**Explanation:** Optimizes for long reads (ONT/PacBio).

### Set minimum length
**Args:** `notramp -i reads.fastq -o trimmed.fastq --set_min_len 50`
**Explanation:** Sets minimum alignment length to 50.

### Remove barcodes
**Args:** `notramp -i reads.fastq -o trimmed.fastq -b barcodes.fasta`
**Explanation:** Removes barcode sequences from reads.

### Threads
**Args:** `notramp -i reads.fastq -o trimmed.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `notramp -i reads.fastq -o trimmed.fastq -v`
**Explanation:** Runs with verbose output.