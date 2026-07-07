---
name: fastq-pair
category: formatting
description: "fastq-pair: efficient synchronization of paired-end fastq files"
tags: [fastq-pair, formatting, paired-end, synchronization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/linsalrob/fastq-pair"
---

## Concepts

- **Tool Overview**: fastq-pair is a tool for efficiently synchronizing paired-end FASTQ files, ensuring reads are properly matched.
- **Core Function**: Synchronizes paired-end reads by matching read identifiers between two FASTQ files.
- **Input/Output**: Input: Two paired-end FASTQ files. Output: Synchronized paired-end FASTQ files.
- **Algorithm**: Uses read identifier matching to synchronize paired reads.
- **Key Features**: Efficient synchronization, paired-end support, progress tracking, error handling, batch processing.
- **Installation**: `conda install -c bioconda fastq-pair`

## Pitfalls

- **Read Order**: Requires reads to be in same order or matching identifiers.
- **Memory Usage**: Large files may require significant memory.
- **Identifier Format**: Requires consistent read identifier format.
- **Missing Reads**: Missing reads may cause synchronization failures.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic synchronization
**Args:** `fastq-pair -1 reads_1.fastq -2 reads_2.fastq -o synchronized_`
**Explanation:** Synchronizes paired-end FASTQ files.

### With output prefix
**Args:** `fastq-pair -1 reads_1.fastq -2 reads_2.fastq -p output_`
**Explanation:** Sets custom output prefix.

### Skip unmatched
**Args:** `fastq-pair -1 reads_1.fastq -2 reads_2.fastq -o synchronized_ --skip-unmatched`
**Explanation:** Skips unmatched reads instead of failing.

### Verbose mode
**Args:** `fastq-pair -1 reads_1.fastq -2 reads_2.fastq -o synchronized_ -v`
**Explanation:** Shows detailed progress information.

### Batch processing
**Args:** `fastq-pair -i input_dir/ -o output_dir/`
**Explanation:** Processes multiple paired-end file pairs.