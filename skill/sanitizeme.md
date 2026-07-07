---
name: sanitizeme
category: utility
description: GUI and CLI tool for removing host DNA from NGS data.
tags: ["sanitizeme", "utility", "host-removal", "ngs", "contamination"]
author: oxo-call-community
source_url: "https://github.com/jiangweiyao/SanitizeMe"
---

## Concepts
- **Tool Overview**: SanitizeMe (v1.1) is a GUI and CLI tool designed to remove host DNA contamination from next-generation sequencing data.
- **Core Function**: Identifies and removes reads originating from host organisms, improving data quality for downstream analysis.
- **Algorithm**: Uses sequence alignment against host reference genome to identify and filter contaminating reads.
- **Input Format**: FASTQ files (single-end or paired-end), host reference genome.
- **Output Format**: Cleaned FASTQ files with host reads removed.
- **Use Case**: Metagenomics analysis, removing human DNA from microbial samples, improving sequence assembly quality.

## Pitfalls
- **Reference Genome**: Requires appropriate host reference genome for accurate filtering.
- **Sensitivity/Specificity Tradeoff**: Adjusting parameters affects false positive/negative rates.
- **Memory Usage**: Aligning to large genomes requires significant memory.
- **Paired-End Handling**: Requires both read files for paired-end data.
- **Speed**: Alignment-based filtering can be computationally intensive.
- **False Positives**: May remove non-host reads with sequence similarity to host.

## Examples
### Basic host removal
**Args:** `sanitizeme -i reads.fastq -r host_genome.fasta -o clean.fastq`
**Explanation:** `-i` input FASTQ; `-r` host reference; `-o` output cleaned FASTQ.

### Paired-end data
**Args:** `sanitizeme -1 reads_1.fastq -2 reads_2.fastq -r host.fasta -o clean_`
**Explanation:** `-1/-2` paired-end reads; output prefix for paired output files.

### Adjust sensitivity
**Args:** `sanitizeme -i reads.fastq -r host.fasta -s 0.9 -o clean.fastq`
**Explanation:** `-s` sets similarity threshold (0.9 = 90% identity).

### Keep unmapped reads
**Args:** `sanitizeme -i reads.fastq -r host.fasta -k -o clean.fastq`
**Explanation:** `-k` keeps reads that fail to map to host genome.

### Multiple hosts
**Args:** `sanitizeme -i reads.fastq -r host1.fasta host2.fasta -o clean.fastq`
**Explanation:** Filters against multiple host reference genomes.

### Verbose mode
**Args:** `sanitizeme -i reads.fastq -r host.fasta -v -o clean.fastq`
**Explanation:** `-v` enables verbose output for monitoring progress.

### GUI mode
**Args:** `sanitizeme --gui`
**Explanation:** Launches graphical user interface for interactive operation.