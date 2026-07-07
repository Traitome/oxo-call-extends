---
name: cnvpytor
category: programming
description: Python extension of CNVnator for copy number variation analysis
tags: [cnvpytor, cnv-calling, python, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://abyzovlab.github.io/CNVpytor"
---

## Concepts

- **Tool Overview**: CNVpytor is a Python extension of CNVnator, providing a more flexible and accessible interface for copy number variation detection from sequencing data.
- **Core Function**: Detects copy number variations using read depth analysis with histogram-based segmentation, similar to CNVnator but with Python-based interface.
- **Algorithm**: Uses read depth histogram analysis and mean-shift segmentation for CNV detection.
- **Input**: BAM files with aligned sequencing reads.
- **Output**: CNV calls with copy number estimates and statistical metrics.
- **Application**: Genomics research, population genetics, and copy number variation analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cnvpytor`

## Pitfalls

- **Reference Genome**: Requires matching reference genome for alignment.
- **Bin Size**: Bin size selection affects detection sensitivity.
- **Memory Usage**: May require significant memory for large datasets.
- **Data Quality**: Requires high-quality sequencing data.
- **Python Dependencies**: May require specific Python version and dependencies.

## Examples

### Initialize CNVpytor
**Args:** `cnvpytor -root sample.root -unique sample.bam`
**Explanation:** Extracts read depth from BAM file into root format.

### Generate histogram
**Args:** `cnvpytor -root sample.root -his 100 -d reference.fasta`
**Explanation:** Generates read depth histogram with 100bp bin size.

### Call CNVs
**Args:** `cnvpytor -root sample.root -call 100 > cnv_calls.txt`
**Explanation:** Calls CNVs from segmented data.

### Display help
**Args:** `cnvpytor --help`
**Explanation:** Shows all available options and usage information.