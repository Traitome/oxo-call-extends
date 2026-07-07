---
name: kmc
category: utility
description: Tools for efficient k-mer counting and filtering of reads based on k-mer content.
tags: [kmc, utility, k-mer, counting, genomics]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/kmc"
---

## Concepts

- **K-mer Counting**: Counts k-mers in DNA sequences with high efficiency
- **Memory Efficiency**: Uses disk-based approach for large datasets
- **Read Filtering**: Filters reads based on k-mer abundance
- **Multiple Databases**: Supports multiple k-mer databases for comparison
- **Set Operations**: Performs union, intersection, and difference of k-mer sets
- **Fast Algorithm**: Optimized for speed with multi-threading

## Pitfalls

- **Memory Management**: Requires careful memory allocation for large genomes
- **K-mer Size Selection**: Larger k-mers increase specificity but require more memory
- **Disk Space**: Intermediate files can consume significant disk space
- **Duplicate Reads**: KMC may count duplicate reads multiple times
- **Complexity**: Complex genomes produce many unique k-mers
- **Database Size**: Large k-mer sets require substantial storage

## Examples

### Count k-mers from FASTQ
**Args:** `kmc -k21 -ci1 -fm input.fastq output_kmcdb tmp_dir`
**Explanation:** Counts 21-mers from FASTQ, keeping k-mers with count >= 1.

### Count from multiple files
**Args:** `kmc -k31 input1.fastq input2.fastq output_db tmp_dir`
**Explanation:** Counts 31-mers from multiple input files.

### Filter k-mers by abundance
**Args:** `kmc -k25 -ci3 -cx5 input.fastq output_db tmp_dir`
**Explanation:** Counts k-mers with count between 3 and 5.

### K-mer database operations
**Args:** `kmc_tools complex output1.kmc + output2.kmc combined.kmc`
**Explanation:** Performs union of two k-mer databases.

### Intersect k-mer databases
**Args:** `kmc_tools simple db1.kmc intersect db2.kmc result.kmc`
**Explanation:** Finds common k-mers between two databases.

### Transform to histogram
**Args:** `kmc_tools transform output.kmc histogram hist.txt`
**Explanation:** Generates k-mer abundance histogram.