---
name: suppa
category: rnaseq
description: A tool to study splicing across multiple conditions at high speed and accuracy.
tags: [suppa, splicing, rnaseq, alternative-splicing]
author: oxo-call-community
source_url: "https://github.com/comprna/SUPPA"
---

## Concepts

- **Tool Overview**: suppa (v2.4) analyzes alternative splicing events from RNA-seq data.
- **Core Function**: Identifies and quantifies alternative splicing events.
- **Algorithm**: Uses junction counts and transcript annotations for splicing analysis.
- **Input/Output**: Input: RNA-seq alignments, annotations; Output: Splicing events and statistics.
- **Applications**: RNA-seq analysis, alternative splicing, gene expression regulation.
- **Installation**: `conda install -c bioconda suppa` or download from GitHub.

## Pitfalls

- **Annotation Quality**: Poor annotations affect results.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Analysis of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect detection.
- **Read Coverage**: Low coverage affects quantification accuracy.
- **Transcript Isoforms**: Complex transcript structures may be missed.

## Examples

### Display help
**Args:** `suppa.py --help`
**Explanation:** Shows available options and usage information.

### Basic splicing analysis
**Args:** `suppa.py events -i junctions.bed -a annotations.gtf -o events.txt`
**Explanation:** Identify alternative splicing events.

### Quantification
**Args:** `suppa.py quantify -i events.txt -a annotations.gtf -o quant.txt`
**Explanation:** Quantify splicing events.

### Verbose mode
**Args:** `suppa.py events -i junctions.bed -a annotations.gtf -o events.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Differential splicing
**Args:** `suppa.py diffSplice -i quant1.txt quant2.txt -o diff.txt`
**Explanation:** Find differentially spliced events.

### Batch processing
**Args:** `suppa.py events -i junctions/ -a annotations.gtf -o results/`
**Explanation:** Process multiple junction files together.

### Filter by coverage
**Args:** `suppa.py events -i junctions.bed -a annotations.gtf -o events.txt -c 10`
**Explanation:** Minimum coverage threshold of 10.

### Include novel events
**Args:** `suppa.py events -i junctions.bed -a annotations.gtf -o events.txt --novel`
**Explanation:** Detect novel splicing events.

### Generate report
**Args:** `suppa.py events -i junctions.bed -a annotations.gtf -o events.txt --report`
**Explanation:** Generate comprehensive HTML report.
