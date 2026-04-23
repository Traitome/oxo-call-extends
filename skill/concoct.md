---
name: concoct
category: metagenomics
description: Clustering contigs with coverage and composition for metagenomic binning
tags: [concoct, metagenomics, binning, contig, mag]
author: oxo-call-community
source_url: "https://github.com/BinPro/CONCOCT"
---

## Concepts

- **Tool Overview**: CONCOCT is a metagenomic binning tool that clusters contigs based on both sequence composition (tetranucleotide frequencies) and coverage across multiple samples.
- **Core Function**: Bins assembled contigs into genome bins (MAGs) by analyzing compositional signatures and abundance profiles across samples.
- **Input/Output**: Input: Assembled contigs (FASTA) and coverage information (BAM files or coverage table). Output: Binned contigs in FASTA format and bin assignments.
- **Coverage Profiles**: Uses differential coverage across multiple samples to distinguish between species with similar composition.
- **Gaussian Mixture Models**: Employs probabilistic clustering using Gaussian mixture models to assign contigs to bins.
- **Two-Step Process**: First generates coverage table from BAM files, then performs clustering and binning.

## Pitfalls

- **Multiple Samples Required**: Best results require multiple samples with differential coverage. Single-sample binning is less accurate.
- **Contig Length**: Short contigs (<1kb) are harder to bin accurately. Consider filtering before binning.
- **Coverage Depth**: Low-coverage contigs (<5x) may be mis-binned. Ensure sufficient sequencing depth.
- **Number of Bins**: Must estimate or specify the number of bins. Use `--clusters` to adjust.
- **Memory Usage**: Large datasets with many samples require significant memory for coverage matrix.

## Examples

### Generate coverage table from BAM files
**Args:** `concoct_coverage_table.py contigs.fasta samples/*.bam > coverage_table.tsv`
**Explanation:** Creates coverage table from multiple BAM files, required input for binning.

### Basic binning
**Args:** `concoct --contigs contigs.fasta --coverage_file coverage_table.tsv -b output_bins/`
**Explanation:** Bins contigs using coverage and composition, outputs bins to specified directory.

### Specify number of clusters
**Args:** `--contigs contigs.fasta --coverage_file coverage_table.tsv --clusters 50 -b output_bins/`
**Explanation:** Manually sets the number of bins to 50 instead of auto-estimation.

### Adjust length threshold
**Args:** `--contigs contigs.fasta --coverage_file coverage_table.tsv --length_threshold 1500 -b output_bins/`
**Explanation:** Only bins contigs >= 1500bp, excluding short contigs that are harder to bin accurately.

### Use different k-mer size
**Args:** `--contigs contigs.fasta --coverage_file coverage_table.tsv --kmer_length 5 -b output_bins/`
**Explanation:** Uses 5-mers instead of default 4-mers for composition analysis, may improve specificity.

### Extract bins to FASTA
**Args:** `extract_bins.py --bin_path output_bins/ --output_path extracted_bins/`
**Explanation:** Extracts contigs for each bin into separate FASTA files for downstream analysis.

### Run with more iterations
**Args:** `--contigs contigs.fasta --coverage_file coverage_table.tsv --iterations 500 -b output_bins/`
**Explanation:** Increases EM iterations for better convergence on difficult datasets.

### Set random seed for reproducibility
**Args:** `--contigs contigs.fasta --coverage_file coverage_table.tsv --seed 42 -b output_bins/`
**Explanation:** Sets random seed for reproducible binning results across runs.
