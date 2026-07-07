---
name: absense
category: utility
description: "abSENSE: a method to interpret undetected homologs"
tags: [absense, utility, homology, blast, detection, probability]
author: oxo-call-community
source_url: "https://github.com/caraweisman/abSENSE"
---
## Concepts

- **Tool Overview**: abSENSE (v1.0.1) is a computational method that calculates the probability that a homolog of a given gene would fail to be detected by a homology search (like BLAST) in a given species, even if the homolog were present and evolving normally.
- **Core Function**: Helps interpret negative homology search results by distinguishing between true gene absence vs. statistical detection failure
- **Scientific Paper**: Weisman CM, Murray AW, Eddy SR (2020) Many, but not all, lineage-specific genes can be explained by homology detection failure. PLoS Biol 18(11): e3000862.
- **Main Script**: `Run_abSENSE.py` - performs batch analysis; `Plot_abSENSE.py` - performs single-gene analysis with visualization
- **Input**: Bitscore file (homolog bitscores across species) and distance file (evolutionary distances between focal species and others)
- **Output**: Detection failure probabilities, predicted bitscores, 99% confidence intervals
- **Installation**: `conda install -c bioconda absense`
- **Dependencies**: Python (>=3.8,<3.9), dill (>=0.3.9), matplotlib-base (>=3.0.0), scipy (1.7.3.*)
- **GUI Available**: Web interface at http://eddylab.org/abSENSE/ for simple single-gene analyses

## Pitfalls

- **Input Format**: Requires specific tab-delimited input formats for bitscore and distance files
- **Data Requirement**: At least three species with bitscore data required per gene for prediction
- **E-value Threshold**: Default E-value threshold is 0.001; adjust with `--Eval` for different stringency
- **Gene Length Assumption**: Default gene length is 400 aa; provide actual lengths with `--genelenfile` for accuracy
- **Database Size**: Default database size is 8 million aa; provide actual sizes with `--dblenfile`
- **Species Names**: Must be consistent across bitscore file, distance file, and optional files
- **Command Name**: The actual command is `python Run_abSENSE.py`, not just `absense`

## Examples

### Display help information
**Args:** `python Run_abSENSE.py --help`
**Explanation:** Shows all available command-line options including advanced parameters like `--out`, `--Eval`, `--genelenfile`, and `--dblenfile`.

### Basic batch analysis
**Args:** `python Run_abSENSE.py --distfile Fungi_Distances --scorefile Fungi_Example_Bitscores`
**Explanation:** Performs abSENSE analysis on multiple genes. Requires a distance file with evolutionary distances and a bitscore file with BLAST bitscores across species. Outputs detection failure probabilities and predicted bitscores to timestamped directory.

### Batch analysis with custom output directory
**Args:** `python Run_abSENSE.py --distfile distances.txt --scorefile bitscores.txt --out my_results`
**Explanation:** Runs analysis and saves results to `my_results/` directory instead of the default timestamped directory.

### Analysis with gene lengths and database sizes
**Args:** `python Run_abSENSE.py --distfile distances.txt --scorefile bitscores.txt --genelenfile gene_lengths.txt --dblenfile db_lengths.txt`
**Explanation:** Provides more accurate predictions by specifying actual gene lengths and database sizes rather than using defaults.

### Single-gene analysis with visualization
**Args:** `python Plot_abSENSE.py --distfile distances.txt --scorefile bitscores.txt --gene NP_116682.3`
**Explanation:** Analyzes a single gene (specified by its ID) and displays a visualization of results. Suitable for investigating individual genes of interest.

### Analysis with custom E-value threshold
**Args:** `python Run_abSENSE.py --distfile distances.txt --scorefile bitscores.txt --Eval 0.0001`
**Explanation:** Uses a more stringent E-value threshold of 0.0001 instead of the default 0.001 for determining detectability.