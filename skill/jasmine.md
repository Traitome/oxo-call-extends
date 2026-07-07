---
name: jasmine
category: expression
description: Java pipeline for isomiR characterization in miRNA-Seq data.
tags: [jasmine, expression, miRNA, isomiR, sequencing]
author: oxo-call-community
source_url: "https://bitbucket.org/bipous/jasmine/src/master"
---

## Concepts

- **Tool Overview**: jasmine (v1.1) - A Java-based pipeline for analyzing and characterizing isomiRs from miRNA-Seq data.
- **IsomiR Detection**: Identifies variant forms of miRNAs including 5' and 3' trimming variants.
- **miRNA Mapping**: Maps sequencing reads to known miRNA precursors and mature miRNAs.
- **Expression Quantification**: Quantifies expression levels of different isomiR variants.
- **IsomiR Classification**: Classifies isomiRs by type (trimming, editing, additions).
- **Differential Expression**: Compares isomiR expression between samples.

## Pitfalls

- **Ambiguous Mapping**: Reads may map to multiple miRNA loci.
- **Low Expression**: Lowly expressed isomiRs may be missed.
- **Reference Database**: Results depend on the completeness of miRNA reference databases.
- **Adapter Contamination**: Adapter sequences must be properly removed.
- **PCR Bias**: PCR amplification can introduce bias in isomiR representation.
- **Multi-mapping Reads**: Reads mapping to multiple locations require careful handling.

## Examples

### Run isomiR analysis
**Args:** `jasmine -i input.fastq -o results/ -r mirbase.fa`
**Explanation:** Analyzes miRNA-Seq data and identifies isomiRs.

### Specify adapter sequence
**Args:** `jasmine -i input.fastq -o results/ -r mirbase.fa -a AGATCGGAAGAGCACACGTCT`
**Explanation:** Specifies custom adapter sequence for trimming.

### Quantify expression
**Args:** `jasmine -i input.fastq -o results/ -r mirbase.fa --quantify`
**Explanation:** Performs isomiR expression quantification.

### Differential expression
**Args:** `jasmine -i sample1.fastq sample2.fastq -o results/ -r mirbase.fa --compare`
**Explanation:** Compares isomiR expression between two samples.

### Filter by quality
**Args:** `jasmine -i input.fastq -o results/ -r mirbase.fa -q 20`
**Explanation:** Filters reads by minimum Phred quality score of 20.

### Output detailed report
**Args:** `jasmine -i input.fastq -o results/ -r mirbase.fa --detailed-report`
**Explanation:** Generates comprehensive isomiR characterization report.