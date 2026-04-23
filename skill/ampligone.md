---
name: ampligone
category: qc
description: Accurately find and remove primer sequences from NGS reads in amplicon sequencing experiments
tags: [primer-removal, amplicon, ngs, fastq, trimming]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/AmpliGone"
---

## Concepts

- **Tool Overview**: AmpliGone accurately finds and removes primer sequences from NGS reads in amplicon sequencing experiments. Unlike other primer-removal tools, it uses alignment-based detection for precise primer identification. Version 2.0.2.
- **Alignment-Based Detection**: Uses alignment rather than simple sequence matching to find primers, handling mismatches and partial primer matches more accurately.
- **Amplicon-Specific**: Designed specifically for amplicon sequencing where primers are known and need removal before downstream analysis.
- **Input Requirements**: FASTQ files (gzipped supported) and primer sequences in FASTA format.
- **Primer Orientation**: Automatically detects primer orientation (forward/reverse) and handles both orientations correctly.
- **Preserves Read Structure**: Removes only primer portions while maintaining read quality scores and format integrity.
- **Speed**: Efficient processing suitable for large amplicon sequencing datasets.

## Pitfalls

- **Primer Specificity**: Primers must match the actual primers used in sequencing. Mismatched primers lead to failed detection.
- **Degenerate Bases**: Primers with degenerate bases (IUPAC codes) are supported but may require careful specification.
- **Paired-End Handling**: For paired-end data, process each file separately or ensure correct pairing after trimming.
- **Minimum Read Length**: After primer removal, very short reads may need additional filtering (e.g., with seqkit or prinseq).
- **Primer File Format**: Primer sequences must be in valid FASTA format with proper headers.

## Examples

### Basic primer removal
**Args:** `ampligone -i input.fastq.gz -p primers.fasta -o output.fastq.gz`
**Explanation:** Removes primer sequences from input FASTQ using primer definitions from FASTA file. Outputs trimmed reads in gzipped FASTQ format.

### Process paired-end reads
**Args:** `ampligone -i R1.fastq.gz -p primers.fasta -o R1_trimmed.fastq.gz; ampligone -i R2.fastq.gz -p primers.fasta -o R2_trimmed.fastq.gz`
**Explanation:** Processes paired-end reads by running AmpliGone separately on each file. Ensure primers FASTA contains both forward and reverse primers.

### Specify output format
**Args:** `ampligone -i input.fastq -p primers.fasta -o trimmed.fastq --output-format fastq`
**Explanation:** Explicitly specifies output format as FASTQ. Also supports FASTA output if quality scores not needed.

### Verbose output for debugging
**Args:** `ampligone -i input.fastq.gz -p primers.fasta -o output.fastq.gz --verbose`
**Explanation:** Enables verbose output showing primer detection details. Useful for verifying correct primer identification and troubleshooting.

### Multiple primer pairs
**Args:** `ampligone -i input.fastq.gz -p all_primers.fasta -o output.fastq.gz`
**Explanation:** Uses FASTA file containing multiple primer pairs. AmpliGone will detect and remove any matching primer from the set. Useful for multi-amplicon panels.

### Keep untrimmed reads
**Args:** `ampligone -i input.fastq.gz -p primers.fasta -o trimmed.fastq.gz --keep-untrimmed`
**Explanation:** Retains reads where no primer was found (untrimmed) in output. Useful when some reads may not contain primers due to chimeras or contamination.
