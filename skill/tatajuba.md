---
name: tatajuba
category: metagenomics
description: Identification and classification of homopolymeric tracts from reads.
tags: [tatajuba, homopolymeric-tracts, metagenomics, sequencing]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/tatajuba"
---

## Concepts

- **Tool Overview**: tatajuba (v1.0.4) identifies homopolymeric tracts in sequences.
- **Core Function**: Detects and classifies homopolymer sequences.
- **Algorithm**: Pattern recognition for homopolymer identification.
- **Input/Output**: Input: FASTQ reads; Output: Homopolymer classifications.
- **Applications**: Metagenomics, sequence analysis, microbial typing.
- **Installation**: `conda install -c bioconda tatajuba` or download from GitHub.

## Pitfalls

- **Read Quality**: Poor quality affects homopolymer detection.
- **Read Length**: Short reads may not contain complete tracts.
- **Sequencing Errors**: Homopolymer length estimation errors.
- **Threshold Settings**: Incorrect thresholds affect detection.
- **Memory Usage**: Large datasets require significant memory.
- **Performance**: Processing large files can be slow.

## Examples

### Display help
**Args:** `tatajuba --help`
**Explanation:** Shows available options and usage information.

### Basic homopolymer detection
**Args:** `tatajuba -i reads.fastq -o homopolymers.txt`
**Explanation:** Detect homopolymeric tracts from reads.

### With database
**Args:** `tatajuba -i reads.fastq -d database/ -o homopolymers.txt`
**Explanation:** Use reference database for classification.

### Verbose mode
**Args:** `tatajuba -i reads.fastq -o homopolymers.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tatajuba -i reads.fastq -o homopolymers.txt --stats`
**Explanation:** Generate statistics about detection.

### Batch processing
**Args:** `for f in fastq/*.fastq; do tatajuba -i $f -o results/${f%.fastq}_hp.txt; done`
**Explanation:** Process multiple FASTQ files.

### Filter by length
**Args:** `tatajuba -i reads.fastq -o homopolymers.txt -l 10`
**Explanation:** Minimum homopolymer length of 10.

### Generate report
**Args:** `tatajuba -i reads.fastq -o homopolymers.txt --report`
**Explanation:** Generate comprehensive detection report.

### Export to CSV
**Args:** `tatajuba -i reads.fastq -o homopolymers.csv -f csv`
**Explanation:** Export results in CSV format.
