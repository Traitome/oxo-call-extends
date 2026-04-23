---
name: blockbuster
category: annotation
description: Detect blocks of overlapping reads using a gaussian-distribution approach
tags: [blockbuster, peak-calling, annotation, rna-seq]
author: oxo-call-community
source_url: "http://hoffmann.bioinf.uni-leipzig.de/LIFE/blockbuster.html"
---

## Concepts

- **Tool Overview**: Blockbuster detects blocks of overlapping reads for transcript identification.
- **Core Function**: Clusters overlapping reads into transcriptional blocks using Gaussian modeling.
- **Input**: BED file with read coordinates.
- **Output**: Block coordinates and read count statistics.
- **Application**: Transcript discovery and expression analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda blockbuster`

## Pitfalls

- **Input Format**: Requires BED format input; ensure correct coordinate system.
- **Block Definition**: Parameters affect block detection sensitivity.
- **Coverage**: Low coverage regions may have incomplete block detection.
- **Strand Specificity**: Consider strand information for accurate block calling.

## Examples

### Detect read blocks
**Args:** `blockbuster -i reads.bed -o blocks.tsv`
**Explanation:** Identifies overlapping read blocks from BED file.

### Set minimum reads per block
**Args:** `blockbuster -i reads.bed -m 5 -o blocks.tsv`
**Explanation:** Requires minimum 5 reads per detected block.

### Adjust Gaussian parameters
**Args:** `blockbuster -i reads.bed -s 50 -o blocks.tsv`
**Explanation:** Sets standard deviation parameter for Gaussian clustering.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
