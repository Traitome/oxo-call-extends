---
name: demuxem
category: expression
description: DemuxEM - demultiplexing module for cell-hashing and nucleus-hashing genomics data.
tags: [demuxem, expression, demultiplexing, single-cell, cell-hashing]
author: oxo-call-community
source_url: "https://github.com/lilab-bcb/demuxEM"
---

## Concepts

- **Tool Overview**: demuxem (v0.1.8+) is the demultiplexing module of Pegasus for cell-hashing and nucleus-hashing single-cell genomics data. It assigns cells to samples using hashtag oligonucleotide (HTO) data.
- **Core Function**: Assigns cell barcodes to sample identities using HTO count data from cell-hashing experiments, enabling pooling of multiple samples in single-cell sequencing.
- **Input/Output**: Input: Gene expression matrix (h5), HTO count matrix (h5). Output: Cell-to-sample assignments, doublet detection, summary statistics.
- **Algorithm**: Uses mixture modeling and statistical inference to assign cells to samples based on HTO intensities.
- **Key Features**: Cell-hashing demultiplexing, doublet detection, robust statistical model, integrates with Pegasus workflow, visualization support.
- **Installation**: `conda install -c bioconda demuxem`

## Pitfalls

- **Input Requirements**: Requires paired gene expression and HTO count data.
- **HTO Quality**: Poor HTO signal may affect assignment accuracy.
- **Doublet Rate**: High doublet rates can complicate demultiplexing.
- **Batch Effects**: May be affected by batch effects in HTO data.
- **Reference Data**: Requires proper reference HTO sequences.

## Examples

### Demultiplex cells using HTO data
**Args:** `demuxem demux --rna rna.h5 --hto hto.h5 --output assignments.tsv`
**Explanation:** Demultiplexes cells using gene expression and HTO data.

### With doublet detection
**Args:** `demuxem demux --rna rna.h5 --hto hto.h5 --output assignments.tsv --detect-doublets`
**Explanation:** Detect and flag doublet cells during demultiplexing.

### Generate report
**Args:** `demuxem demux --rna rna.h5 --hto hto.h5 --output assignments.tsv --report report.html`
**Explanation:** Generate HTML report with demultiplexing statistics.