---
name: telogator2
category: visualization
description: Telogator2 - Telomere Characterization and Visualization Tool for genomic analysis.
tags: [telogator2, telomere, visualization, genomics, chromosome-ends, telomere-length]
author: oxo-call-community
source_url: "https://github.com/genome-tools/telogator2"
---

## Concepts

- **Tool Overview**: Telogator 2 - An upgraded tool for telomere characterization, visualization, and comparative analysis.
- **Core Function**: Provides comprehensive telomere analysis including length estimation, repeat composition, and comparative visualization across samples or species.
- **Input**: Genomic sequences, BAM alignments, or telomere repeat datasets.
- **Output**: Visualization reports (HTML/PDF), telomere length estimates, and comparative tables.
- **Installation**: `pip install telogator2` or `conda install -c bioconda telogator2`
- **Use Case**: Comparative telomere biology, cancer research, population studies of telomere variation.

## Pitfalls

- **Reference Quality**: Telomere regions are highly repetitive - assembly quality affects analysis.
- **Mixed Repeat Types**: Multiple telomere repeat types may complicate length estimation.

## Examples

### Generate telomere report
**Args:** `telogator2 -i sample_genome.fasta -o telomere_report/`
**Explanation:** Generate comprehensive telomere analysis and visualization.

### Compare samples
**Args:** `telogator2 -i sample1.fasta sample2.fasta -o comparison/ --compare`
**Explanation:** Compare telomere characteristics between two samples.
