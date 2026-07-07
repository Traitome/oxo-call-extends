---
name: sidr
category: metagenomics
description: SIDR - Sequence Identification using Decision Trees
tags: ["sidr", "metagenomics", "classification", "machine-learning"]
author: oxo-call-community
source_url: "https://github.com/damurdock/SIDR"
---

## Concepts

- **Tool Overview**: SIDR (v0.0.2a2) classifies DNA reads using machine learning models.
- **Core Function**: Identifies organisms from metagenomic sequencing data.
- **Algorithm**: Uses decision tree-based classification for taxonomic assignment.
- **Input/Output**: Accepts FASTQ reads and produces taxonomic classification.
- **Metagenomics Analysis**: Specialized for metagenomic read classification.
- **Applications**: Microbial community analysis, environmental sequencing, and pathogen detection.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Model Training**: Requires training on reference datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Database Requirements**: Requires comprehensive reference database.
- **Version Compatibility**: Early development stage, API may change.
- **Documentation**: Limited documentation available.

## Examples

### Classify reads
**Args:** `sidr -i reads.fastq -d database/ -o results.txt`
**Explanation:** `-i` input FASTQ; `-d` database directory; `-o` output results.

### With confidence threshold
**Args:** `sidr -i reads.fastq -d database/ -c 0.9 -o results.txt`
**Explanation:** `-c 0.9` confidence threshold.

### Batch processing
**Args:** `sidr -b batch.txt -d database/ -o results/`
**Explanation:** `-b` batch file with multiple FASTQ files.

### Help command
**Args:** `sidr --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sidr --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sidr -v -i reads.fastq -d database/ -o results.txt`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sidr -t 8 -i reads.fastq -d database/ -o results.txt`
**Explanation:** `-t 8` uses 8 threads.
