---
name: rsa
category: utility
description: RSA (Resampling Statistical Analysis) / R-scape helper — utilities for statistical analysis of structural RNA alignments; commonly used as a lightweight wrapper around R-scape for automated covariation analysis pipelines.
tags: ["rsa", "r-scape", "rna-structure", "covariation", "statistical-analysis", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/EddyRivasLab/R-scape"
---

## Concepts

- **Tool Overview**: RSA (v2.0.x, Eddy-Rivas Lab) is a lightweight command-line wrapper around R-scape (RNA Significant Covariation Above Phylogenetic Expectation) that automates the statistical analysis of structural RNA alignments. It runs R-scape over a directory of Stockholm alignments and aggregates the results into a single summary table.
- **Core Function**: Takes a directory of Stockholm-formatted RNA alignments and runs R-scape on each alignment (or a single alignment as input). It then aggregates the per-alignment covariation statistics (number of base pairs tested, number of significant pairs, E-value distribution) into a TSV/JSON summary. Designed for batch processing of Rfam seed alignments or custom alignment collections.
- **Algorithm**: (1) Iterate over the input alignments; (2) invoke R-scape on each; (3) parse the R-scape output (covariation table, power table); (4) aggregate the per-alignment statistics; (5) write a summary TSV. The covariation statistic is the G-test (default) or several others (MI, MIr, MIg, CHI, OMES, RaF, RAFS).
- **Input Format**: (1) A single Stockholm alignment file (`.sto`), or (2) a directory of Stockholm alignment files. R-scape is required and must be in `PATH` (or supplied via `--rscape-path`).
- **Output Format**: A TSV with one row per alignment: `alignment_name, num_pairs_tested, num_significant_pairs, best_evalue, power`. An optional JSON output includes the full per-base-pair covariation table. A plot (PDF/PNG) of the E-value distribution is also produced.
- **Use Case**: Batch processing of Rfam seed alignments to identify families with significant covariation (canonical use case), running R-scape over a custom alignment collection in a covariation-analysis pipeline, generating a summary report for a benchmarking study of covariation statistics, and integrating R-scape into a Snakemake/Nextflow pipeline.

## Pitfalls

- **CRITICAL — R-scape must be installed and in `PATH`**: RSA is a thin wrapper; without R-scape, it fails immediately. Install via `conda install -c bioconda r-scape` or build from source (http://eddylab.org/R-scape/).
- **CRITICAL — The input MUST be in extended Stockholm format (with `#=GC RF` annotation)**: A plain Stockholm alignment without the consensus secondary structure annotation produces a degenerate R-scape run (no base pairs to test). For alignments without a structure, use `cmalign` from Infernal first.
- **R-scape is slow on large alignments**: An alignment of 1000 sequences × 500 columns takes ~10 minutes. RSA does not parallelize by default; use `--threads` to run multiple R-scape instances in parallel.
- **The E-value threshold is 0.05 by default**: This is the R-scape-recommended threshold. A stricter threshold (e.g., 0.001) reduces the number of significant pairs but increases the false-negative rate. A looser threshold (e.g., 0.1) increases the false-positive rate.
- **RSA does NOT generate plots for individual alignments**: The default output is a summary table. For per-alignment plots, run R-scape directly (`R-scape alignment.sto`) and inspect the output PDF.
- **The summary table does NOT include the alignment length**: A small alignment (50 columns) and a large alignment (5000 columns) are not directly comparable. Normalize by `num_significant_pairs / num_pairs_tested` for a fair comparison.

## Examples

### Basic RSA run on a directory
**Args:** `rsa --input-dir alignments/ --out summary.tsv`
**Explanation:** `--input-dir` is a directory of Stockholm files; `--out` is the output TSV. RSA runs R-scape on each alignment and writes one row per alignment to the summary TSV.

### Single alignment
**Args:** `rsa --alignment my_alignment.sto --out single.tsv`
**Explanation:** `--alignment` is a single Stockholm file. Equivalent to running R-scape and aggregating, but with a more concise output.

### Specify the E-value threshold
**Args:** `rsa --input-dir alignments/ --evalue 0.001 --out summary_strict.tsv`
**Explanation:** `--evalue` sets the R-scape E-value threshold (default 0.05). Stricter threshold for high-confidence covariation.

### Use the MI covariation statistic
**Args:** `rsa --input-dir alignments/ --statistic MI --out summary_MI.tsv`
**Explanation:** `--statistic` selects the covariation statistic (G-test by default; alternatives: MI, MIr, MIg, CHI, OMES, RaF, RAFS). The choice affects the per-alignment statistics but the output schema is the same.

### Run with multiple threads
**Args:** `rsa --input-dir alignments/ --threads 8 --out summary.tsv`
**Explanation:** `--threads` runs multiple R-scape instances in parallel. Recommended for >10 alignments.

### Output JSON
**Args:** `rsa --input-dir alignments/ --format json --out summary.json`
**Explanation:** `--format json` writes a JSON with the full per-base-pair covariation tables. Useful for programmatic access (e.g., parsing in Python).

### Generate a summary plot
**Args:** `rsa --input-dir alignments/ --plot summary_plot.png --out summary.tsv`
**Explanation:** `--plot` writes a PNG of the E-value distribution across all alignments. Useful for figure generation in publications.
