---
name: seqverify
category: genome-editing
description: seqverify - Analyze whole genome sequencing data for gene-editing verification
tags: ["seqverify", "genome-editing", "CRISPR", "verification"]
author: oxo-call-community
source_url: "https://github.com/mpiersonsmela/SeqVerify"
---

## Concepts

- **Tool Overview**: seqverify (v1.3.0) analyzes whole genome sequencing data for gene-editing verification.
- **Core Function**: Validates CRISPR/Cas9 gene-editing outcomes using sequencing data.
- **Algorithm**: Uses alignment and variant calling to detect editing events.
- **Input/Output**: Accepts FASTQ/BAM files and produces editing verification reports.
- **Gene Editing**: Focuses on CRISPR editing outcome analysis.
- **Applications**: Genome editing validation, CRISPR screening, and gene therapy.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Verify editing
**Args:** `seqverify -i reads.fastq -g guide.fa -o results/`
**Explanation:** `-i` input reads; `-g` guide RNA; `-o` output directory.

### From BAM
**Args:** `seqverify -b alignments.bam -g guide.fa -o results/`
**Explanation:** `-b` input BAM file.

### Verbose logging
**Args:** `seqverify -v -i reads.fastq -g guide.fa -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqverify --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqverify --version`
**Explanation:** Shows current version.

### Target region
**Args:** `seqverify -i reads.fastq -g guide.fa -r chr1:1000-2000 -o results/`
**Explanation:** `-r` target region for analysis.

### Paired-end
**Args:** `seqverify -1 reads_1.fastq -2 reads_2.fastq -g guide.fa -o results/`
**Explanation:** `-1/-2` paired-end reads.