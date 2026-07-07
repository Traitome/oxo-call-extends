---
name: scrubby
category: sequence-analysis
description: scrubby - Read depletion/extraction and database cleaning using k-mer and alignment methods
tags: ["scrubby", "sequence-analysis", "k-mer", "filtering"]
author: oxo-call-community
source_url: "https://github.com/esteinig/scrubby"
---

## Concepts

- **Tool Overview**: scrubby (v0.2.1) performs read depletion/extraction and database cleaning using k-mer and alignment methods.
- **Core Function**: Filters and cleans sequencing data using k-mer matching and alignment.
- **Algorithm**: Uses k-mer frequency analysis and sequence alignment for data cleaning.
- **Input/Output**: Accepts FASTA/FASTQ files and produces cleaned sequences.
- **Data Cleaning**: Specifically designed for removing contaminant sequences.
- **Applications**: Sequence data cleaning, contaminant removal, and database curation.

## Pitfalls

- **Memory Usage**: High memory requirements for large k-mer databases.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May remove legitimate sequences.
- **False Negatives**: May miss contaminant sequences.
- **k-mer Selection**: Choosing the right k-mer size affects performance.

## Examples

### Basic depletion
**Args:** `scrubby deplete -i reads.fastq -d contaminants.fasta -o cleaned.fastq`
**Explanation:** `-i` input reads; `-d` contaminants; `-o` cleaned output.

### Extract sequences
**Args:** `scrubby extract -i reads.fastq -k kmers.txt -o extracted.fastq`
**Explanation:** Extracts sequences matching k-mers.

### K-mer counting
**Args:** `scrubby count -i reads.fastq -k 21 -o counts.txt`
**Explanation:** Counts k-mers with k=21.

### Database cleaning
**Args:** `scrubby clean -i database.fasta -d contaminants.fasta -o cleaned.fasta`
**Explanation:** Removes contaminants from database.

### Verbose logging
**Args:** `scrubby deplete -i reads.fastq -d contaminants.fasta -v -o cleaned.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `scrubby deplete -i reads.fastq -d contaminants.fasta -t 8 -o cleaned.fastq`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Quality filtering
**Args:** `scrubby deplete -i reads.fastq -d contaminants.fasta -q 20 -o cleaned.fastq`
**Explanation:** `-q 20` filters reads with quality below 20.