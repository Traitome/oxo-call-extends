---
name: kseqpp
category: formatting
description: C++11 kseq re-implementation with modern API and resource management
tags: [kseqpp, formatting, FASTA, FASTQ, parser, C++, sequencing]
author: oxo-call-community
source_url: "https://github.com/cartoonist/kseqpp"
---

## Concepts

- **Kseq Re-implementation**: Modern C++11 re-implementation of Heng Li's kseq
- **FASTA/FASTQ Parsing**: Efficient parsing of sequence files
- **Generic Stream Buffer**: Based on generic stream buffer implementation
- **Modern API**: Provides updated API for sequence file handling
- **Resource Management**: Improved memory and resource management
- **Cross-platform**: Works on multiple platforms and compilers

## Pitfalls

- **Library Integration**: Requires proper library integration
- **Build Requirements**: Needs C++11 compatible compiler
- **API Changes**: Different API from original kseq
- **Error Handling**: New error handling mechanisms
- **Buffer Size**: Default buffer sizes may need adjustment
- **Compilation Flags**: May need specific compilation flags

## Examples

### Parse FASTQ file
**Args:** `kseqpp parse -i sequences.fastq -o parsed.txt`
**Explanation:** Parses FASTQ file and outputs sequence data.

### Process FASTA
**Args:** `kseqpp parse -i genome.fasta -o sequences.txt`
**Explanation:** Parses FASTA genome file.

### Specify format
**Args:** `kseqpp parse -i reads.fastq --format fastq -o output.txt`
**Explanation:** Explicitly specifies input format.

### Batch processing
**Args:** `kseqpp batch -d sequences/ -o results/`
**Explanation:** Processes multiple sequence files.

### Export statistics
**Args:** `kseqpp stats -i sequences.fastq -o statistics.txt`
**Explanation:** Generates sequence statistics.

### Quality filtering
**Args:** `kseqpp filter -i reads.fastq --min-qual 20 -o filtered.fastq`
**Explanation:** Filters reads by quality score.