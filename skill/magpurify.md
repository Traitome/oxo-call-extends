---
name: magpurify
category: assembly
description: Identify and remove incorrectly binned contigs from metagenome-assembled genomes.
tags: [magpurify, assembly, MAGs, contamination]
author: oxo-call-community
source_url: "https://github.com/snayfach/MAGpurify"
---

## Concepts

- **Tool Overview**: magpurify v2.1.2 - A tool for identifying and removing incorrectly binned contigs from Metagenome-Assembled Genomes (MAGs) to improve genome quality.
- **Core Function**: Uses machine learning and sequence composition to detect and remove contaminating contigs from MAG bins.
- **Input/Output**: Input: MAG contigs (FASTA), optionally coverage information; Output: Purified MAGs, contamination reports.
- **Installation**: `conda install -c bioconda magpurify`
- **Machine Learning Models**: Trained models for detecting contamination based on tetranucleotide frequency and other features.
- **Multiple Methods**: Supports multiple contamination detection methods including tetra, gc, coverage, and taxonomy.

## Pitfalls

- **Training Data**: Models trained on specific datasets may not generalize.
- **Coverage Data**: Missing coverage information reduces prediction accuracy.
- **Completeness**: Over-purification may remove genuine contigs.
- **Taxonomy Database**: Outdated taxonomy databases affect classification.
- **Memory Usage**: Processing large MAG collections requires significant memory.
- **False Positives**: May incorrectly flag genuine contigs as contaminants.

## Examples

### Run all purification methods
**Args:** `magpurify clean --fasta bin.fasta --outdir purified/`
**Explanation:** Runs all contamination detection methods on a MAG.

### Specific method
**Args:** `magpurify tetra --fasta bin.fasta --outdir results/`
**Explanation:** Uses tetranucleotide frequency method only.

### With coverage information
**Args:** `magpurify clean --fasta bin.fasta --coverage coverage.txt --outdir purified/`
**Explanation:** Incorporates coverage information for better detection.

### Custom threshold
**Args:** `magpurify clean --fasta bin.fasta --outdir purified/ --threshold 0.9`
**Explanation:** Sets custom confidence threshold.

### Batch processing
**Args:** `magpurify batch --indir bins/ --outdir purified/`
**Explanation:** Processes multiple MAGs in batch.

### Generate report
**Args:** `magpurify clean --fasta bin.fasta --outdir purified/ --report`
**Explanation:** Generates HTML report of purification results.