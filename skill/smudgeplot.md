---
name: smudgeplot
category: genomics
description: smudgeplot - Inference of ploidy and heterozygosity structure using whole genome sequencing data
tags: [smudgeplot, genomics, ploidy, heterozygosity, sequencing]
author: oxo-call-community
source_url: "https://github.com/KamilSJaron/smudgeplot"
---

## Concepts

- **Tool Overview**: smudgeplot (v0.5.3) - A tool for inferring ploidy and heterozygosity structure from WGS data
- **Core Function**: Uses k-mer frequencies to estimate ploidy level and heterozygosity
- **Input/Output**: Accepts k-mer counts; outputs ploidy estimates and visualizations
- **Algorithm**: Analyzes k-mer frequency distributions to identify peaks corresponding to different ploidy levels
- **Installation**: `conda install -c bioconda smudgeplot`
- **Key Features**: Ploidy estimation, heterozygosity analysis, visualization tools

## Pitfalls

- **k-mer Size**: Appropriate k-mer size selection is critical
- **Sequence Quality**: Low-quality reads affect k-mer counting accuracy
- **Coverage Depth**: Requires sufficient sequencing coverage
- **Genome Complexity**: Highly repetitive genomes may produce misleading results
- **Contamination**: Sample contamination affects ploidy estimation
- **Memory Usage**: Large k-mer databases require significant memory

## Examples

### Display help
**Args:** `smudgeplot --help`
**Explanation:** Shows available options and usage information.

### Basic ploidy estimation
**Args:** `smudgeplot analyze -k kmer_counts.hist -o results/`
**Explanation:** Analyze k-mer distribution to infer ploidy.

### Generate plot
**Args:** `smudgeplot plot -i results/smudgeplot_data.txt -o ploidy_plot.png`
**Explanation:** Generate smudgeplot visualization.

### With coverage information
**Args:** `smudgeplot analyze -k kmer_counts.hist -c coverage.txt -o results/`
**Explanation:** Incorporate coverage information into analysis.

### Specify k-mer size
**Args:** `smudgeplot analyze -k kmer_counts.hist -K 21 -o results/`
**Explanation:** Specify k-mer size used for counting.

### Batch processing
**Args:** `smudgeplot batch -i samples.txt -o results_dir/`
**Explanation:** Process multiple samples in batch.

### Generate report
**Args:** `smudgeplot report -i results/ -o report.html`
**Explanation:** Generate comprehensive HTML report.

### Custom parameters
**Args:** `smudgeplot analyze -k kmer_counts.hist -p 2,4,6 -o results/`
**Explanation:** Test specific ploidy hypotheses.