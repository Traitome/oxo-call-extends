---
name: telometer
category: analysis
description: Telometer - Telomere Length Measurement tool from sequencing data.
tags: [telometer, telomere, telomere-length, ngs, qpcr-comparison, genomics]
author: oxo-call-community
source_url: "https://github.com/genome-tools/telometer"
---

## Concepts

- **Tool Overview**: Telometer - A tool for estimating telomere length from next-generation sequencing data.
- **Core Function**: Calculates telomere length estimates based on telomeric repeat abundance in sequencing data, providing an alternative to qPCR-based methods.
- **Input**: Whole genome sequencing reads (FASTQ) or telomere-enriched sequencing data.
- **Output**: Telomere length estimates in kilobases, quality metrics.
- **Installation**: `pip install telometer` or `conda install -c bioconda telometer`
- **Use Case**: Population studies of telomere length variation, cancer diagnostics, aging research.

## Pitfalls

- **Sequencing Bias**: GC-rich telomere sequences may be underrepresented in some library preparations.
- **Genome Coverage**: Requires sufficient whole-genome coverage for reliable estimates.

## Examples

### Estimate telomere length
**Args:** `telometer -i wgs_reads.fastq.gz -o telomere_length.txt`
**Explanation:** Estimate telomere length from WGS reads.

### Paired-end analysis
**Args:** `telometer -1 R1.fastq.gz -2 R2.fastq.gz -o results/`
**Explanation:** Use paired-end data for improved telomere length estimation.
