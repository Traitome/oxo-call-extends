---
name: interval-binning
category: metagenomics
description: A Python implementation of the interval binning scheme for metagenomic data analysis
tags: [interval-binning, metagenomics, binning, MAGs]
author: oxo-call-community
source_url: "https://github.com/martijnvermaat/binning"
---

## Concepts

- **Tool Overview**: interval-binning is a Python library for metagenomic binning using interval-based approaches
- **Core Function**: Groups metagenomic contigs into bins (MAGs - Metagenome-Assembled Genomes) based on sequence composition and coverage
- **Binning Strategy**: Uses coverage information and tetranucleotide frequency to cluster contigs
- **Input Requirements**: Requires assembled contigs and coverage depth information
- **Installation**: `conda install -c bioconda interval-binning`

## Pitfalls

- **Contig Length**: Short contigs can reduce binning accuracy; recommend minimum 1500bp
- **Coverage Bias**: Uneven coverage across samples can affect binning quality
- **Strain Variation**: Closely related strains may be binned together
- **Memory Usage**: Large datasets require significant memory
- **Preprocessing**: Requires proper read mapping and depth calculation beforehand

## Examples

### Basic binning
**Args:** `interval-binning --contigs assembly.fasta --depth depth.txt --output bins/`
**Explanation:** Performs binning on assembled contigs using coverage depth information.

### With minimum contig length
**Args:** `interval-binning --contigs assembly.fasta --depth depth.txt --output bins/ --min-length 2000`
**Explanation:** Filters out contigs shorter than 2000bp before binning.

### Specify number of bins
**Args:** `interval-binning --contigs assembly.fasta --depth depth.txt --output bins/ --num-bins 20`
**Explanation:** Attempts to create approximately 20 bins from the assembly.

### Multiple sample coverage
**Args:** `interval-binning --contigs assembly.fasta --depth sample1_depth.txt sample2_depth.txt --output bins/`
**Explanation:** Uses coverage information from multiple samples for improved binning.

### Generate bin statistics
**Args:** `interval-binning --contigs assembly.fasta --depth depth.txt --output bins/ --stats`
**Explanation:** Outputs statistics about each bin including completeness estimates.

### Verbose output
**Args:** `interval-binning --contigs assembly.fasta --depth depth.txt --output bins/ --verbose`
**Explanation:** Provides detailed logging of the binning process.