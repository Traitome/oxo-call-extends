---
name: lodei
category: rna
description: LODEI - Analyze differentially edited A-to-I regions in RNA-seq samples
tags: [lodei, rna, rna-editing, A-to-I, differential-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rna-editing1/lodei"
---

## Concepts

- **RNA Editing**: Analysis of RNA editing events
- **A-to-I Editing**: Adenosine-to-inosine editing analysis
- **Differential Analysis**: Differential editing analysis between samples
- **RNA-seq Data**: RNA sequencing data analysis
- **Statistical Testing**: Statistical testing for differential editing
- **Visualization**: Visualization of editing patterns

## Pitfalls

- **Read Quality**: Poor quality reads affect detection
- **Mapping Quality**: Requires accurate read mapping
- **Sample Size**: Requires sufficient sample size
- **Multiple Testing**: Requires proper multiple testing correction
- **Computational Time**: May be slow for large datasets
- **False Positives**: May produce false positive calls

## Examples

### Analyze editing
**Args:** `lodei -i sample1.bam sample2.bam -o editing_results.txt`
**Explanation:** Analyzes differentially edited regions between samples.

### Reference genome
**Args:** `lodei -i sample1.bam sample2.bam -r reference.fasta -o results.txt`
**Explanation:** Uses reference genome for analysis.

### Threads
**Args:** `lodei -i sample1.bam sample2.bam -o results.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `lodei -i sample1.bam sample2.bam -o results.json -f json`
**Explanation:** Outputs results in JSON format.

### Filter by coverage
**Args:** `lodei -i sample1.bam sample2.bam -o results.txt -c 10`
**Explanation:** Filters by minimum coverage.

### Generate plots
**Args:** `lodei -i sample1.bam sample2.bam -o results/ -p`
**Explanation:** Generates visualization plots.