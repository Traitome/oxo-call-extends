---
name: gat
category: utility
description: Genomic Association Tester for computing significance of overlap between genomic interval sets
tags: [gat, genomic-intervals, chip-seq, enrichment-analysis, statistical-testing]
author: oxo-call-community
source_url: "https://github.com/AndreasHeger/gat"
---

## Concepts

- **Tool Overview**: GAT (Genomic Association Tester) is a tool for computing the significance of overlap between multiple sets of genomic intervals using simulation-based statistical testing.
- **Core Function**: Tests whether genomic intervals (e.g., from ChIP-Seq experiments) overlap significantly more or less than expected with genomic annotations (e.g., promoters, introns, DNase-hypersensitive sites).
- **Statistical Method**: Implements a sampling algorithm that creates randomized versions of segments of interest within a workspace, then compares observed overlap to expected overlap to compute empirical p-values.
- **Input Format**: All inputs must be in BED format (tab-separated with chrom, start, end). Supports gzip-compressed files (.gz).
- **Three Required Inputs**:
  - **Segments of Interest (S)**: Intervals to test (e.g., ChIP-Seq peaks)
  - **Annotations (A)**: Genomic features to test against (e.g., gene promoters)
  - **Workspace (W)**: The genomic region to analyze (e.g., chromosomes or specific regions)
- **Output**: Tab-separated table with observed counts, expected counts, 95% confidence intervals, fold enrichment, log2 fold, p-value, and q-value (FDR-corrected).
- **G+C Bias Control**: Can account for isochore structure and G+C content biases in the null model.
- **Sampling**: Uses Monte Carlo simulation (typically >1000 samples) to build null distribution of expected overlaps.
- **Installation**: `conda install -c bioconda gat`

## Pitfalls

- **CRITICAL: Coordinate System**: BED files use 0-based coordinates (start inclusive, end exclusive). GAT uses 1-based coordinates internally. Mismatches between input coordinate systems will produce incorrect results.
- **CRITICAL: Subcommand Naming**: The main script is `gat-run.py` (not `gat`). Always use `gat-run.py --help` to see available options.
- **Memory Usage**: Large BED files with many intervals can require significant memory. Consider filtering or splitting large files.
- **Sample Size**: Default sampling may be insufficient for very small or very large datasets. Increase `--num-samples` for higher precision on borderline p-values.
- **Workspace Definition**: Failing to define an appropriate workspace can lead to inflated or deflated enrichment estimates. The workspace should encompass all regions where segments could reasonably fall.
- **Multiple Testing**: When testing multiple segment-annotation pairs, always use q-values (FDR correction) rather than raw p-values to control false discoveries.
- **Version Differences**: Command-line options may vary between versions. Check `gat-run.py --help` for your installed version.

## Examples

### Basic enrichment analysis
**Args:** `--segment-file=segments.bed.gz --workspace-file=workspace.bed.gz --annotation-file=annotations.bed.gz`
**Explanation:** The fundamental GAT command tests if segments (e.g., ChIP-Seq peaks) overlap significantly with annotations (e.g., promoters). The workspace defines the background region. Output shows observed/expected overlap ratios and statistical significance.

### Test multiple segment files simultaneously
**Args:** `--segment-file=chip_peaks.bed.gz,replicated_peaks.bed.gz --workspace-file=hg19_chroms.bed.gz --annotation-file=promoters.bed.gz`
**Explanation:** Use comma-separated file paths to test multiple segment sets against the same annotations in a single run. This is useful for comparing different experimental conditions or replicates.

### Increase sampling for precise p-values
**Args:** `--segment-file=peaks.bed --workspace-file=chroms.bed --annotation-file=genes.bed --num-samples=10000`
**Explanation:** Default 1000 samples may be insufficient for borderline cases. Increasing to 10000 provides more precise p-value estimates, especially important when p-values are near the significance threshold (0.05).

### Add isochores for G+C bias control
**Args:** `--segment-file=peaks.bed --workspace-file=genome.bed --annotation-file=exons.bed --isochore-file=isochores.bed`
**Explanation:** Isochores are genomic regions with similar G+C content. Adding this file accounts for G+C bias in the null model, preventing inflated enrichment estimates for G+C-rich annotations.

### Run on specific chromosome
**Args:** `--segment-file=chr1_peaks.bed --workspace-file=chr1.bed --annotation-file=chr1_genes.bed`
**Explanation:** Restricting analysis to a single chromosome is useful for testing, debugging, or when working with chromosome-specific datasets. Smaller datasets also run faster.

### Output to specific file
**Args:** `--segment-file=peaks.bed --workspace-file=genome.bed --annotation-file=annotations.bed --stdout=gat_results.tsv`
**Explanation:** By default GAT outputs to stdout. Use `--stdout` to redirect results to a specific file. The output is a tab-separated table with columns: track, annotation, observed, expected, CI95low, CI95high, stddev, fold, l2fold, pvalue, qvalue.

### Use gzip-compressed input files
**Args:** `--segment-file=chip_peaks.bed.gz --workspace-file=hg38.bed.gz --annotation-file=refseq_annotations.bed.gz`
**Explanation:** GAT automatically recognizes .gz files and decompresses them on-the-fly. This saves disk space and is recommended for large BED files.

### Change p-value method
**Args:** `--segment-file=peaks.bed --workspace-file=genome.bed --annotation-file=annots.bed --pvalue-method=binomial`
**Explanation:** Default is empirical sampling. For certain analyses, the binomial method may be appropriate. Available methods: empirical, binomial, negative-binomial, poisson.

### Multi-sample analysis with track naming
**Args:** `--segment-file=GSM123.bed,GSM456.bed --workspace-file=hg38.bed --annotation-file=dnase_hss.bed --track-names=H3K4me3,H3K27ac`
**Explanation:** Use `--track-names` to assign meaningful names to multiple input segment files. Results will use these names instead of filenames in the output table.
