---
name: seqprep
category: utility
description: seqprep - Strip adaptors and merge paired reads with overlap
tags: ["seqprep", "utility", "trimming", "paired-end"]
author: oxo-call-community
source_url: "https://github.com/jstjohn/SeqPrep/blob/v1.3.2/README.md"
---

## Concepts

- **Tool Overview**: seqprep (v1.3.2) strips adaptors and merges paired reads with overlap.
- **Core Function**: Processes paired-end reads by removing adapters and merging overlapping reads.
- **Algorithm**: Implements adapter trimming and overlap-based read merging.
- **Input/Output**: Accepts paired FASTQ files and produces trimmed/merged reads.
- **Read Processing**: Focuses on preprocessing paired-end sequencing data.
- **Applications**: NGS data preprocessing, adapter removal, and read merging.

## Pitfalls

- **Memory Usage**: High memory requirements for large FASTQ files.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Merge reads
**Args:** `SeqPrep -f reads_1.fastq -r reads_2.fastq -1 merged_1.fastq -2 merged_2.fastq -s merged.fastq`
**Explanation:** `-f/-r` input reads; `-1/-2` paired outputs; `-s` merged output.

### With adapter
**Args:** `SeqPrep -f reads_1.fastq -r reads_2.fastq -A AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -o merged.fastq`
**Explanation:** `-A` specifies adapter sequence.

### Quality trimming
**Args:** `SeqPrep -f reads_1.fastq -r reads_2.fastq -q 20 -o merged.fastq`
**Explanation:** `-q 20` quality threshold for trimming.

### Verbose logging
**Args:** `SeqPrep -f reads_1.fastq -r reads_2.fastq -v -o merged.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `SeqPrep --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `SeqPrep --version`
**Explanation:** Shows current version.

### Overlap threshold
**Args:** `SeqPrep -f reads_1.fastq -r reads_2.fastq -m 10 -o merged.fastq`
**Explanation:** `-m 10` minimum overlap length.