---
name: clame
category: alignment
description: Binning software for metagenomic reads using FM-index and graph-based clustering
tags: [clame, metagenomics, binning, fm-index, clustering]
author: oxo-call-community
source_url: "https://github.com/andvides/CLAME"
---

## Concepts

- **Tool Overview**: CLAME is a binning software for metagenomic reads, using FM-index search algorithm for sequence alignment and strongly connected component strategy for binning.
- **Core Function**: Groups metagenomic reads into bins based on sequence similarity and DNA composition.
- **Algorithm**: Uses FM-index for efficient sequence alignment and graph-based clustering for binning.
- **Input**: Metagenomic sequencing reads (FASTQ).
- **Output**: Binned sequences grouped by similarity.
- **Application**: Metagenomic data analysis, taxonomic profiling, and genome reconstruction.
- **Installation**: Install via bioconda: `conda install -c bioconda clame`

## Pitfalls

- **Memory Usage**: May require significant memory for large datasets.
- **Data Quality**: Depends on sequencing data quality.
- **Computational Resources**: May require significant compute resources.
- **Reference Database**: Performance depends on reference database quality.
- **Parameter Tuning**: May require parameter adjustment for optimal results.

## Examples

### Run metagenomic binning
**Args:** `clame -i reads.fastq -o bins/`
**Explanation:** Bins metagenomic reads into groups based on sequence similarity.

### With reference database
**Args:** `clame -i reads.fastq -d reference_db -o bins/`
**Explanation:** Uses reference database for improved binning accuracy.

### Specify k-mer size
**Args:** `clame -i reads.fastq -k 21 -o bins/`
**Explanation:** Uses specific k-mer size for sequence comparison.

### Display help
**Args:** `clame --help`
**Explanation:** Shows all available options and usage information.