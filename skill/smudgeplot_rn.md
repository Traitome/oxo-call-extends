---
name: smudgeplot_rn
category: genomics
description: smudgeplot_rn - Fork of smudgeplot for inference of ploidy and heterozygosity structure using whole genome sequencing data
tags: [smudgeplot_rn, genomics, ploidy, heterozygosity, sequencing]
author: oxo-call-community
source_url: "https://github.com/RNieuwenhuis/smudgeplot"
---

## Concepts

- **Tool Overview**: smudgeplot_rn (v0.2.5_RN) - A fork of smudgeplot with additional features for ploidy analysis
- **Core Function**: Inference of ploidy and heterozygosity structure from whole-genome sequencing data
- **Input/Output**: Accepts k-mer counts; outputs ploidy estimates and visualizations
- **Algorithm**: Analyzes k-mer frequency distributions to identify ploidy levels
- **Installation**: `conda install -c bioconda smudgeplot_rn`
- **Key Features**: Extended ploidy estimation, additional visualization options, bug fixes

## Pitfalls

- **k-mer Size**: Appropriate k-mer size selection is critical
- **Sequence Quality**: Low-quality reads affect k-mer counting accuracy
- **Coverage Depth**: Requires sufficient sequencing coverage
- **Genome Complexity**: Highly repetitive genomes may produce misleading results
- **Contamination**: Sample contamination affects ploidy estimation
- **Version Compatibility**: May have different options than original smudgeplot

## Examples

### Display help
**Args:** `smudgeplot_rn --help`
**Explanation:** Shows available options and usage information.

### Basic ploidy estimation
**Args:** `smudgeplot_rn analyze -k kmer_counts.hist -o results/`
**Explanation:** Analyze k-mer distribution to infer ploidy.

### Generate enhanced plot
**Args:** `smudgeplot_rn plot -i results/smudgeplot_data.txt -o ploidy_plot.png -e`
**Explanation:** Generate enhanced smudgeplot visualization.

### With coverage information
**Args:** `smudgeplot_rn analyze -k kmer_counts.hist -c coverage.txt -o results/`
**Explanation:** Incorporate coverage information into analysis.

### Specify k-mer size
**Args:** `smudgeplot_rn analyze -k kmer_counts.hist -K 21 -o results/`
**Explanation:** Specify k-mer size used for counting.

### Batch processing
**Args:** `smudgeplot_rn batch -i samples.txt -o results_dir/`
**Explanation:** Process multiple samples in batch.

### Generate report
**Args:** `smudgeplot_rn report -i results/ -o report.html`
**Explanation:** Generate comprehensive HTML report.

### Custom parameters
**Args:** `smudgeplot_rn analyze -k kmer_counts.hist -p 2,4,6 -o results/`
**Explanation:** Test specific ploidy hypotheses.