---
name: trimmomatic
category: qc
description: A flexible read trimming tool for Illumina NGS data.
tags: [trimmomatic, qc, trimming, adapter, fastq, illumina]
author: oxo-call-community
source_url: "https://www.plabipd.de/trimmomatic_main.html"
---

## Concepts

- **Tool Overview**: Trimmomatic (v0.40+) is a flexible read trimming tool for Illumina NGS data that performs quality trimming, adapter removal, and filtering. It supports both single-end and paired-end reads.
- **Core Function**: Trims low-quality bases, removes adapter sequences, filters short reads, and performs quality control on sequencing data.
- **Input/Output**: Input: FASTQ reads (single-end or paired-end). Output: Trimmed FASTQ reads with optional unpaired reads for paired-end data.
- **Algorithm**: Processes reads sequentially, applying trimming operations based on quality scores and adapter sequences.
- **Key Features**: Supports multiple adapter types, quality-based trimming, sliding window trimming, and various filtering options.
- **Installation**: `conda install -c bioconda trimmomatic`

## Pitfalls

- **Adapter Sequences**: Ensure correct adapter sequences are specified. Use `ILLUMINACLIP` for Illumina adapters or provide custom sequences.
- **Paired-End Data**: For paired-end reads, use `PE` mode with proper input/output file ordering.
- **Quality Format**: Trimmomatic uses Phred+33 by default. Use `-phred64` for older Illumina data.
- **Output Files**: For paired-end data, four output files are generated: paired R1, unpaired R1, paired R2, unpaired R2.
- **Memory Usage**: Processing large datasets may require increasing Java heap size with `java -Xmx16g`.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Trim paired-end reads
**Args:** `PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz ILLUMINACLIP:adapters.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
**Explanation:** Trims paired-end reads with Illumina adapter removal, leading/trailing quality trimming, sliding window quality filter, and minimum length of 36.

### Trim single-end reads
**Args:** `SE -phred33 reads.fastq.gz trimmed.fastq.gz ILLUMINACLIP:adapters.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
**Explanation:** Trims single-end reads with the same parameters as paired-end mode.

### Quality trimming only
**Args:** `PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
**Explanation:** Trims reads without adapter removal, applying only quality-based trimming.

### Custom adapter sequences
**Args:** `PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz ILLUMINACLIP:custom_adapters.fa:2:30:10 LEADING:3 TRAILING:3`
**Explanation:** Uses custom adapter sequences from custom_adapters.fa for adapter trimming.

### Strict quality filtering
**Args:** `PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz ILLUMINACLIP:adapters.fa:2:30:10 LEADING:5 TRAILING:5 SLIDINGWINDOW:6:20 MINLEN:50`
**Explanation:** Applies stricter quality thresholds (Phred 5 for leading/trailing, Phred 20 for sliding window) and minimum length of 50.

### Remove low-complexity reads
**Args:** `PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz ILLUMINACLIP:adapters.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 COMPLEXITY:0.8`
**Explanation:** Filters reads with low complexity (entropy threshold 0.8).

### Trim with maximum memory
**Args:** `java -Xmx32g -jar trimmomatic.jar PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz ILLUMINACLIP:adapters.fa:2:30:10 LEADING:3 TRAILING:3`
**Explanation:** Runs Trimmomatic with 32GB heap space for large datasets.

### Quality trimming with specific adapter file
**Args:** `PE -phred33 R1.fastq.gz R2.fastq.gz R1_paired.fastq.gz R1_unpaired.fastq.gz R2_paired.fastq.gz R2_unpaired.fastq.gz ILLUMINACLIP:/path/to/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
**Explanation:** Uses the TruSeq3-PE adapter file for Illumina TruSeq paired-end libraries.