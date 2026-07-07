---
name: metabinner
category: utility
description: Ensemble binning method for recovering individual genomes from complex microbial communities.
tags: [metabinner, metagenomics, binning]
author: oxo-call-community
source_url: "https://github.com/ziyewang/MetaBinner"
---

## Concepts

- **Tool Overview**: MetaBinner uses ensemble methods for metagenomic binning.
- **Core Function**: Ensemble-based genome recovery.
- **Multiple Binners**: Combines results from multiple binning tools.
- **Machine Learning**: Uses ML for improved binning.
- **MAG Quality**: Improves MAG completeness and purity.
- **Installation**: `conda install -c bioconda metabinner`

## Pitfalls

- **Dependency Issues**: Requires multiple binning tools.
- **Memory Requirements**: High memory usage.
- **Computation Time**: Slow due to multiple binners.
- **Parameter Tuning**: Complex configuration.
- **Input Requirements**: Needs multiple input types.
- **Result Integration**: Combining outputs may fail.

## Examples

### Run ensemble binning
**Args:** `metabinner -i contigs.fasta -a depth.txt -o bins/`
**Explanation:** Runs ensemble binning.

### With multiple depth files
**Args:** `metabinner -i contigs.fasta -a sample1.txt,sample2.txt -o bins/`
**Explanation:** Uses multiple samples.

### Custom binners
**Args:** `metabinner -i contigs.fasta -b metabat,maxbin -o bins/`
**Explanation:** Uses specific binners.

### High confidence bins
**Args:** `metabinner -i contigs.fasta -c 0.9 -o bins/`
**Explanation:** Filters for high confidence bins.

### Help documentation
**Args:** `metabinner --help`
**Explanation:** Displays available options.
