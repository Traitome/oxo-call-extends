---
name: gridss
category: bioinformatics
description: GRIDSS is a comprehensive suite for identifying genomic rearrangements including structural variants from sequencing data.
tags: [gridss, structural-variants, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/PapenfussLab/gridss"
---

## Concepts

- **Structural Variant Detection**: GRIDSS identifies various types of genomic rearrangements.

- **Breakpoint Identification**: Detects precise breakpoints of structural variants.

- **Multiple Evidence Integration**: Combines multiple sources of evidence for variant calling.

- **Assembly-Based Calling**: Uses de novo assembly for complex variant detection.

- **Quality Filtering**: Provides quality filtering for reliable variant calls.

- **Visualization**: Generates visualizations of detected structural variants.

## Pitfalls

- **Memory Requirements**: Processing large genomes may require significant memory.

- **Read Depth**: Low coverage regions may miss structural variants.

- **Complex Rearrangements**: Very complex rearrangements may be difficult to detect.

- **Parameter Tuning**: Adjust parameters based on sequencing technology and expected variant types.

- **Output Interpretation**: Complex structural variants may require careful interpretation.

## Examples

### Detect structural variants
**Args:** `gridss -i reads.bam -r reference.fasta -o sv_calls.vcf`
**Explanation:** Detects structural variants from aligned reads.

### Include assembly
**Args:** `gridss -i reads.bam -r reference.fasta -a -o sv_calls.vcf`
**Explanation:** Uses de novo assembly for complex variant detection.

### Specify breakend confidence
**Args:** `gridss -i reads.bam -r reference.fasta -c 30 -o sv_calls.vcf`
**Explanation:** Sets minimum confidence score for breakend calls.

### Parallel processing
**Args:** `gridss -i reads.bam -r reference.fasta -t 8 -o sv_calls.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Filter variants
**Args:** `gridss filter -i sv_calls.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters variants with quality score below 30.

### Generate statistics
**Args:** `gridss stats -i sv_calls.vcf -o stats.txt`
**Explanation:** Generates statistics about detected structural variants.

### Visualize variants
**Args:** `gridss visualize -i sv_calls.vcf -r reference.fasta -o visualization.png`
**Explanation:** Creates a visualization of detected structural variants.