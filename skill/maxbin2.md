---
name: maxbin2
category: assembly
description: Binning assembled metagenomic sequences using Expectation-Maximization algorithm.
tags: [maxbin2, metagenomics, binning]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/maxbin"
---

## Concepts

- **Tool Overview**: MaxBin2 bins metagenomic contigs into genome bins.
- **Core Function**: Uses Expectation-Maximization for automated binning.
- **Coverage Information**: Uses sequencing coverage for binning.
- **Taxonomic Classification**: Integrates taxonomic information.
- **Input/Output**: Accepts FASTA contigs and coverage data, produces genome bins.
- **Installation**: `conda install -c bioconda maxbin2`

## Pitfalls

- **Contig Quality**: Requires good quality assembled contigs.
- **Coverage Data**: Requires accurate coverage information.
- **Computation Time**: Can be slow for large datasets.
- **Memory Requirements**: High memory for large metagenomic datasets.
- **Bin Quality**: May produce mixed bins for complex communities.
- **Parameter Tuning**: Requires careful adjustment of EM parameters.

## Examples

### Run binning
**Args:** `run_MaxBin.pl -contig contigs.fasta -out bins/`
**Explanation:** Bins contigs into genome bins.

### With abundance file
**Args:** `run_MaxBin.pl -contig contigs.fasta -abund abundance.txt -out bins/`
**Explanation:** Uses abundance information for binning.

### Multiple samples
**Args:** `run_MaxBin.pl -contig contigs.fasta -abund sample1.txt,sample2.txt -out bins/`
**Explanation:** Uses multiple abundance files.

### Set min contig length
**Args:** `run_MaxBin.pl -contig contigs.fasta -min_contig_length 1000 -out bins/`
**Explanation:** Sets minimum contig length to 1000bp.

### Threaded processing
**Args:** `run_MaxBin.pl -contig contigs.fasta -thread 8 -out bins/`
**Explanation:** Uses 8 threads for parallel processing.

### Help documentation
**Args:** `run_MaxBin.pl -help`
**Explanation:** Displays available options.
