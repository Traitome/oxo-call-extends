---
name: fastq-and-furious
category: formatting
description: "Fast handling of FASTQ files"
tags: [fastq-and-furious, formatting, FASTQ, sequencing-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lgautier/fastq-and-furious"
---

## Concepts

- **Tool Overview**: fastq-and-furious is a fast library for handling FASTQ files, designed for efficient parsing and manipulation.
- **Core Function**: Provides efficient FASTQ file parsing and manipulation capabilities.
- **Input/Output**: Input: FASTQ files. Output: Parsed sequences, quality scores, processed data.
- **Algorithm**: Implements efficient parsing algorithms for FASTQ format.
- **Key Features**: Fast parsing, memory efficient, support for large files, multiple programming languages, batch processing.
- **Installation**: `conda install -c bioconda fastq-and-furious`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Sequence Quality**: Poor quality sequences may affect results.
- **Processing Time**: Very large files may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic parsing
**Args:** `fastq-and-furious parse -i reads.fastq -o parsed.txt`
**Explanation:** Parses FASTQ file and outputs sequence data.

### Quality filtering
**Args:** `fastq-and-furious filter -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** Filters reads by quality score.

### Convert to FASTA
**Args:** `fastq-and-furious convert -i reads.fastq -o sequences.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Statistics
**Args:** `fastq-and-furious stats -i reads.fastq -o stats.txt`
**Explanation:** Generates sequence statistics.

### Batch processing
**Args:** `fastq-and-furious batch -i fastq_files/ -o results/`
**Explanation:** Processes multiple files in batch mode.