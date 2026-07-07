---
name: strmie-hd
category: variant-calling
description: Automated Huntington Disease polyQ pattern scanner.
tags: [strmie-hd, huntington-disease, polyq, str-analysis]
author: oxo-call-community
source_url: "https://mazzalab.github.io/STRmie-HD/"
---

## Concepts

- **Tool Overview**: strmie-hd (v1.0.0) is an automated tool for detecting polyQ expansions associated with Huntington Disease.
- **Core Function**: Identifies and analyzes CAG repeat expansions in the HTT gene.
- **Algorithm**: Uses pattern matching and sequence analysis to detect polyQ repeats.
- **Input/Output**: Input: Sequence data (FASTA/BAM); Output: PolyQ repeat length and classification.
- **Applications**: Huntington Disease diagnosis, genetic screening, research.
- **Installation**: `conda install -c bioconda strmie-hd` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect repeat counting accuracy.
- **Repeat Complexity**: Interrupted repeats affect counting.
- **Read Coverage**: Insufficient coverage affects accuracy.
- **Reference Bias**: Reference genome may not contain all known alleles.
- **Memory Requirements**: Large datasets require significant memory.
- **Specificity**: Designed specifically for Huntington Disease; not general purpose.

## Examples

### Display help
**Args:** `strmie-hd --help`
**Explanation:** Shows available options and usage information.

### Basic polyQ scanning
**Args:** `strmie-hd -i input.fasta -o results.txt`
**Explanation:** Scan sequence for polyQ patterns.

### With BAM input
**Args:** `strmie-hd -i reads.bam -r reference.fasta -o results.txt`
**Explanation:** Analyze BAM file for polyQ expansions.

### Verbose mode
**Args:** `strmie-hd -i input.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output VCF
**Args:** `strmie-hd -i reads.bam -r reference.fasta -o results.vcf --vcf`
**Explanation:** Output results in VCF format.

### Batch processing
**Args:** `strmie-hd -i batch/ -r reference.fasta -o results/`
**Explanation:** Process multiple samples together.

### Filter by quality
**Args:** `strmie-hd -i reads.bam -r reference.fasta -o results.txt -q 20`
**Explanation:** Filter reads by mapping quality.

### Include confidence
**Args:** `strmie-hd -i reads.bam -r reference.fasta -o results.txt --confidence`
**Explanation:** Output confidence scores for calls.

### Generate report
**Args:** `strmie-hd -i reads.bam -r reference.fasta -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
