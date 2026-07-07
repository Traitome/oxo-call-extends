---
name: seqbuster
category: rna-analysis
description: seqbuster - miRNA and isomiR annotation from sequencing data
tags: ["seqbuster", "rna-analysis", "miRNA", "isomiR"]
author: oxo-call-community
source_url: "https://github.com/lpantano/seqbuster"
---

## Concepts

- **Tool Overview**: seqbuster (v3.5) performs miRNA and isomiR annotation from sequencing data.
- **Core Function**: Identifies and annotates miRNAs and isomiRs from small RNA sequencing.
- **Algorithm**: Uses sequence alignment and pattern matching for miRNA identification.
- **Input/Output**: Accepts FASTQ/BAM files and produces annotation results.
- **miRNA Analysis**: Focuses on microRNA and isomiR detection and annotation.
- **Applications**: Small RNA sequencing analysis, miRNA profiling, and isomiR characterization.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Database**: Requires up-to-date miRNA reference database.
- **Input Quality**: Results depend on sequencing data quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Annotate miRNAs
**Args:** `seqbuster -i reads.fastq -d mirbase -o annotations.txt`
**Explanation:** `-i` input FASTQ; `-d mirbase` uses miRBase database; `-o` output file.

### From BAM
**Args:** `seqbuster -i alignments.bam -d mirbase -o annotations.txt`
**Explanation:** `-i` input BAM file.

### Verbose logging
**Args:** `seqbuster -i reads.fastq -v -o annotations.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `seqbuster -i reads.fastq -t 8 -o annotations.txt`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `seqbuster --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqbuster --version`
**Explanation:** Shows current version.

### IsomiR analysis
**Args:** `seqbuster -i reads.fastq --isomir -o isomirs.txt`
**Explanation:** `--isomir` enables isomiR analysis.