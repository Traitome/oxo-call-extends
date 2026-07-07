---
name: tinscan
category: analysis
description: TINscan - Tandem repeat Identification and analysis tool for Nanopore sequencing.
tags: [tinscan, tandem-repeat, nanopore, long-read, repeat-analysis]
author: oxo-call-community
source_url: "https://github.com/genome-tools/tinscan"
---

## Concepts

- **Tool Overview**: TINscan - A tool for identifying and analyzing tandem repeats specifically optimized for Oxford Nanopore sequencing data.
- **Core Function**: Detects tandem repeats in long reads and provides detailed analysis including repeat unit, copy number, and sequence variation.
- **Input**: Nanopore sequencing reads (FASTQ).
- **Output**: Tandem repeat annotations, repeat statistics, variant calls.
- **Installation**: `pip install tinscan` or `conda install -c bioconda tinscan`
- **Use Case**: Repeat expansion disorders, genome assembly, structural variation analysis.

## Pitfalls

- **Nanopore Only**: Optimized for Nanopore data - may not work well with other platforms.
- **Basecalling Quality**: Results depend on basecalling accuracy.

## Examples

### Scan for repeats
**Args:** `tinscan -i nanopore_reads.fastq.gz -o repeat_results/`
**Explanation:** Identify tandem repeats in Nanopore reads.

### Detailed analysis
**Args:** `tinscan -i reads.fastq -o results/ --detailed`
**Explanation:** Generate detailed analysis report of tandem repeats.
