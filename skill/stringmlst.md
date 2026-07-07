---
name: stringmlst
category: typing
description: Fast k-mer based tool for multi locus sequence typing (MLST) directly from genome sequencing reads.
tags: [stringmlst, mlst, typing, k-mer]
author: oxo-call-community
source_url: "https://github.com/jordanlab/stringMLST"
---

## Concepts

- **Tool Overview**: stringmlst (v0.6.3) is a fast k-mer based tool for multi locus sequence typing (MLST) directly from sequencing reads.
- **Core Function**: Performs MLST typing using k-mer analysis without assembly.
- **Algorithm**: Uses k-mer matching to identify sequence types from raw reads.
- **Input/Output**: Input: Sequencing reads (FASTQ); Output: MLST type assignments.
- **Applications**: Bacterial typing, epidemiological studies, pathogen identification.
- **Installation**: `conda install -c bioconda stringmlst` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect typing accuracy.
- **Coverage**: Insufficient coverage affects type calling.
- **Database Quality**: Outdated MLST databases affect results.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Species Specific**: Requires species-specific MLST database.

## Examples

### Display help
**Args:** `stringmlst --help`
**Explanation:** Shows available options and usage information.

### Basic MLST typing
**Args:** `stringmlst -i reads.fastq -o results.txt`
**Explanation:** Perform MLST typing from sequencing reads.

### With custom database
**Args:** `stringmlst -i reads.fastq -d mlst_db/ -o results.txt`
**Explanation:** Use custom MLST database.

### Verbose mode
**Args:** `stringmlst -i reads.fastq -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output alleles
**Args:** `stringmlst -i reads.fastq -o results.txt --alleles`
**Explanation:** Output individual allele calls.

### Batch processing
**Args:** `stringmlst -i batch/ -o results/`
**Explanation:** Process multiple sequencing samples together.

### Filter by quality
**Args:** `stringmlst -i reads.fastq -o results.txt -q 20`
**Explanation:** Filter reads by quality score.

### Include novel alleles
**Args:** `stringmlst -i reads.fastq -o results.txt --novel`
**Explanation:** Report novel alleles.

### Generate report
**Args:** `stringmlst -i reads.fastq -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
