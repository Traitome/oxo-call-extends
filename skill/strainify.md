---
name: strainify
category: metagenomics
description: Strain-level abundance analysis tool for short-read metagenomics.
tags: [strainify, metagenomics, strain-profiling, abundance-estimation]
author: oxo-call-community
source_url: "https://github.com/treangenlab/Strainify"
---

## Concepts

- **Tool Overview**: strainify (v1.2.0) is a tool for strain-level abundance analysis from short-read metagenomic data.
- **Core Function**: Estimates strain-level abundances using SNP-based profiling and coverage analysis.
- **Algorithm**: Uses unique marker SNPs and read mapping to quantify strain abundances.
- **Input/Output**: Input: Metagenomic reads (FASTQ), reference database; Output: Strain abundance estimates.
- **Applications**: Microbial community analysis, strain tracking, metagenomic profiling.
- **Installation**: `conda install -c bioconda strainify` or download from GitHub.

## Pitfalls

- **Reference Quality**: Incomplete or incorrect reference databases affect estimation.
- **Strain Similarity**: Very similar strains are hard to distinguish.
- **Read Coverage**: Low coverage affects abundance estimation accuracy.
- **Mapping Quality**: Poor mapping produces incorrect estimates.
- **Reference Bias**: Reference database selection affects results.
- **Memory Requirements**: Large databases require significant memory.

## Examples

### Display help
**Args:** `strainify --help`
**Explanation:** Shows available options and usage information.

### Basic abundance analysis
**Args:** `strainify -i reads.fastq -d database/ -o results.txt`
**Explanation:** Estimate strain abundances from metagenomic reads.

### With multiple samples
**Args:** `strainify -i sample1.fastq sample2.fastq -d database/ -o results/`
**Explanation:** Process multiple samples together.

### Verbose mode
**Args:** `strainify -i reads.fastq -d database/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strainify -i reads.fastq -d database/ -o results.txt --plot`
**Explanation:** Generate visualization of strain abundances.

### Custom thresholds
**Args:** `strainify -i reads.fastq -d database/ -o results.txt -c 0.01`
**Explanation:** Minimum abundance threshold of 0.01.

### Build database
**Args:** `strainify build -i references/ -o database/`
**Explanation:** Build reference database from genome sequences.

### Filter by coverage
**Args:** `strainify -i reads.fastq -d database/ -o results.txt -m 5`
**Explanation:** Minimum coverage threshold of 5x.

### Generate report
**Args:** `strainify -i reads.fastq -d database/ -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
