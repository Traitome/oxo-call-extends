---
name: apt-probeset-summarize
category: microarray
description: apt-probeset-summarize - Affymetrix Power Tools program for analyzing expression arrays including 3' IVT and exon arrays
tags: [apt-probeset-summarize, affymetrix, microarray, expression-analysis, power-tools]
author: oxo-call-community
source_url: "https://downloads.thermofisher.com"
---

## Concepts

- **Tool Overview**: apt-probeset-summarize (v2.10.0) - A program from the Affymetrix Power Tools (APT) package for analyzing microarray expression data.
- **Core Function**: Processes Affymetrix microarray data including 3' IVT arrays and exon arrays, performing background correction, normalization, and signal summarization.
- **Key Features**:
  - **Background Correction**: Supports MAS5 and RMA methods
  - **Normalization**: Linear scaling, quantile normalization, sketch normalization
  - **Summarization**: PLIER, RMA, and MAS5 methods
  - **Probe Masking**: Supports masking out specific probes using --kill-list option
  - **Multiple Array Types**: Works with 3' IVT arrays and exon arrays
- **Input**: CEL files (raw intensity data), library files (CDF/PGF/CLF/BGP)
- **Output**: Expression signal files in various formats
- **Applications**: 
  - Gene expression profiling
  - Exon-level expression analysis
  - Alternative splicing studies
- **Installation**: `conda install -c bioconda apt-probeset-summarize`

## Pitfalls

- **Library Files**: Requires appropriate library files (CDF, PGF, CLF, BGP) for the specific array type
- **CEL File Requirements**: Raw CEL files must be properly formatted
- **Memory Usage**: May require significant memory for large datasets
- **Probe Masking**: In older versions (<=1.8.0), masking probes in multiple probesets may cause errors
- **Array Specificity**: Different arrays require different library files

## Examples

### RMA sketch normalization
**Args:** `apt-probeset-summarize -a rma-sketch -p HuEx-1_0-st-v2.r2.pgf -c HuEx-1_0-st-v2.r2.clf -b HuEx-1_0-st-v2.r2.antigenomic.bgp -o results *.CEL`
**Explanation:** Process exon arrays using RMA sketch algorithm.

### MAS5 summarization
**Args:** `apt-probeset-summarize -a mas5 -c HumanExon1_0stv2.cdf -o mas5_results --cel-files cel_list.txt`
**Explanation:** Process arrays using MAS5 algorithm with CDF file.

### With probe masking
**Args:** `apt-probeset-summarize -a rma-sketch -p genome.pgf -c genome.clf -b background.bgp -o results --kill-list probe_mask.txt *.CEL`
**Explanation:** Mask specific probes during analysis using a kill list file.

### PLIER summarization
**Args:** `apt-probeset-summarize -a plier -c array.cdf -o plier_results sample1.CEL sample2.CEL`
**Explanation:** Use PLIER algorithm for expression summarization.

### Help documentation
**Args:** `apt-probeset-summarize --help`
**Explanation:** Shows available options and parameters.