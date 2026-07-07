---
name: ont-modkit
category: formatting
description: ont-modkit provides tools for working with modified bases in Oxford Nanopore sequencing data.
tags: [ont-modkit, formatting, modified-bases, nanopore]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/modkit"
---

## Concepts

- **Tool Overview**: ont-modkit processes modified base calls from nanopore data.
- **Core Function**: Analyzes and manipulates modified base information.
- **Algorithm**: Uses base modification calling algorithms.
- **Input Format**: Accepts BAM/CRAM files with modification tags.
- **Output**: Produces modification statistics and visualizations.
- **Use Case**: Epigenomics, DNA modification analysis, and methylation studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Modification Detection**: Depends on basecaller accuracy.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **False Positives**: May report false modifications.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `modkit --help`
**Explanation:** Shows available options and usage instructions.

### Call modifications
**Args:** `modkit call -i reads.bam -r reference.fasta -o modifications.bed`
**Explanation:** Calls modified bases from aligned reads.

### Summary statistics
**Args:** `modkit summary -i modifications.bed -o stats.txt`
**Explanation:** Generates modification statistics.

### Visualization
**Args:** `modkit plot -i modifications.bed -o plot.png`
**Explanation:** Creates modification visualization.

### Filter modifications
**Args:** `modkit filter -i modifications.bed -q 0.9 -o filtered.bed`
**Explanation:** Filters modifications by confidence.

### Convert format
**Args:** `modkit convert -i modifications.bed -o modifications.vcf`
**Explanation:** Converts to VCF format.

### Verbose mode
**Args:** `modkit call -i reads.bam -r reference.fasta -v -o modifications.bed`
**Explanation:** Runs with verbose output.