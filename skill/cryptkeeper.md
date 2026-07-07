---
name: cryptkeeper
category: expression
description: A negative design tool for predicting and visualizing undesired gene expression
tags: [cryptkeeper, expression, synthetic-biology, RBS, promoter, terminator]
author: oxo-call-community
source_url: "https://github.com/barricklab/cryptkeeper"
---

## Concepts

- **Tool Overview**: CryptKeeper (v1.0.1+) is a computational pipeline for predicting cryptic gene expression that can cause plasmid instability or protein truncations.
- **Core Function**: Predicts ribosome binding sites (RBS), promoters, and terminators to identify potentially burdensome open reading frames on plasmids.
- **Input/Output**: Input: FASTA file containing DNA sequence. Output: CSV files with predictions and interactive Bokeh visualization.
- **Key Features**: RBS strength prediction, promoter prediction, rho-dependent/rho-independent terminator prediction, translational burden scoring.
- **Visualization**: Generates interactive circular plots showing predicted elements and burden scores.
- **Installation**: `conda install -c bioconda cryptkeeper` or `pip install cryptkeeper`

## Pitfalls

- **Circular Sequences**: Use `-c` flag for circular DNA (plasmids, viruses) to handle sequence wrap-around.
- **Thread Count**: Parallel processing available with `-j` flag; useful for large sequences.
- **RBS Cutoff**: Adjust `--rbs-score-cutoff` to filter low-confidence predictions.
- **Dependencies**: Requires ViennaRNA and TransTermHP for secondary structure and terminator prediction.
- **Output Files**: Produces multiple CSV files and HTML visualization in output directory.

## Examples

### Analyze circular plasmid
**Args:** `-i plasmid.fna -o results/pSMART -j 8 -c`
**Explanation:** Analyze a circular plasmid sequence with 8 threads, output to specified directory.

### Analyze linear sequence
**Args:** `-i linear_sequence.fna -o output/prefix --name my_sequence`
**Explanation:** Analyze a linear DNA sequence with custom sample name for visualization.

### Plot only mode
**Args:** `-i sequence.fna -o results/prefix -p`
**Explanation:** Generate visualization from previously computed results (plot-only mode).

### Set RBS score cutoff
**Args:** `-i sequence.fna -o output/prefix --rbs-score-cutoff 0.5`
**Explanation:** Filter RBS predictions to only include scores >= 0.5 in output and plot.

### Custom tick frequency
**Args:** `-i plasmid.fna -o results/prefix -t 500`
**Explanation:** Set Y-axis tick frequency to 500 for better visualization of large sequences.

### Basic analysis with default settings
**Args:** `-i input.fna -o output/prefix`
**Explanation:** Run CryptKeeper with default parameters for quick analysis.

### Multi-threaded analysis
**Args:** `-i large_sequence.fna -o results/prefix -j 16 -c`
**Explanation:** Use 16 threads for faster analysis of large circular sequences.

### Output with custom name
**Args:** `-i sequence.fna -o output/prefix -n "My Virus Clone"`
**Explanation:** Assign a descriptive name to the sample for better visualization labeling.
