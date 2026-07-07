---
name: strainscan
category: metagenomics
description: Efficient and accurate strain-level microbiome composition analysis tool based on reference genomes and k-mers.
tags: [strainscan, metagenomics, strain-profiling, k-mer-analysis]
author: oxo-call-community
source_url: "https://github.com/liaoherui/StrainScan"
---

## Concepts

- **Tool Overview**: strainscan (v1.0.14) is an efficient tool for strain-level microbiome composition analysis using k-mer based profiling.
- **Core Function**: Identifies and quantifies strains in metagenomic samples using reference genomes and k-mer matching.
- **Algorithm**: Uses k-mer frequency analysis and probabilistic modeling for strain identification.
- **Input/Output**: Input: Metagenomic reads (FASTQ), reference database; Output: Strain composition and abundances.
- **Applications**: Microbiome analysis, strain tracking, pathogen detection.
- **Installation**: `conda install -c bioconda strainscan` or download from GitHub.

## Pitfalls

- **Reference Coverage**: Incomplete reference databases miss strains.
- **k-mer Selection**: Incorrect k-mer size affects accuracy.
- **Strain Similarity**: Very similar strains are hard to distinguish.
- **Read Coverage**: Low coverage affects detection sensitivity.
- **Memory Requirements**: Large k-mer databases require significant memory.
- **Computational Time**: Processing large datasets can be slow.

## Examples

### Display help
**Args:** `strainscan --help`
**Explanation:** Shows available options and usage information.

### Basic strain analysis
**Args:** `strainscan -i reads.fastq -d database/ -o results.txt`
**Explanation:** Analyze strain composition from metagenomic reads.

### With paired-end reads
**Args:** `strainscan -1 read1.fastq -2 read2.fastq -d database/ -o results.txt`
**Explanation:** Analyze paired-end metagenomic reads.

### Verbose mode
**Args:** `strainscan -i reads.fastq -d database/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strainscan -i reads.fastq -d database/ -o results.txt --plot`
**Explanation:** Generate visualization of strain composition.

### Custom k-mer size
**Args:** `strainscan -i reads.fastq -d database/ -o results.txt -k 27`
**Explanation:** Use k-mer size of 27 for analysis.

### Batch processing
**Args:** `strainscan -i batch/ -d database/ -o results/`
**Explanation:** Process multiple metagenomic samples together.

### Build database
**Args:** `strainscan build -i references/ -o database/`
**Explanation:** Build k-mer database from reference genomes.

### Generate report
**Args:** `strainscan -i reads.fastq -d database/ -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
