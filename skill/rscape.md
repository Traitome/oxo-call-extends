---
name: rscape
category: rna-analysis
description: R-scape (RNA Structural Covariation Above Phylogenetic Expectation) is a tool for detecting conserved RNA secondary structure by measuring pairwise covariations in multiple sequence alignments.
tags: ["rscape", "rna-structure", "covariation", "multiple-sequence-alignment", "stockholm-format", "rna-analysis"]
author: oxo-call-community
source_url: "http://eddylab.org/R-scape/"
---

## Concepts

- **Tool Overview**: R-scape (v2.6.6, Eddy-Rivas Lab) is a tool for detecting conserved RNA secondary structure by measuring pairwise covariations in multiple sequence alignments. It provides a statistical test that accounts for phylogenetic relationships and base composition biases, distinguishing true structural covariation from spurious correlations.
- **Core Function**: Takes a Stockholm-format RNA alignment (optionally with a consensus structure) and identifies significantly covarying base pairs. It performs two independent covariation tests when a structure is provided: one on proposed base pairs and one on all other pairs.
- **Algorithm**: Uses a G-test statistic (default) or other metrics (MI, MIr, MIg, CHI, OMES, RaF, RAFS) to measure covariation. The null hypothesis accounts for phylogenetic relationships using a tree-based model. Reports E-values for each tested pair and estimates statistical power.
- **Input Format**: Stockholm-format alignment file (`.sto`) containing one or more RNA sequences with optional consensus secondary structure annotation. Only the first alignment in multi-alignment files is analyzed.
- **Output Format**: TSV/JSON with significantly covarying pairs (E-value < 0.05 by default), substitution counts, and power estimates. Visualization outputs include structure plots with covarying pairs highlighted.
- **Use Case**: Validating predicted RNA structures, identifying structural RNAs in genomic data, quality assessment of RNA alignments, and distinguishing functional ncRNAs from non-structured transcripts.

## Pitfalls

- **Requires high-quality alignments**: Poorly aligned sequences produce false positives/negatives. Use tools like Infernal or LocARNA for reliable alignments before running R-scape.
- **Minimum sequence diversity required**: Too few sequences or insufficient evolutionary distance reduces statistical power. Aim for ≥15 sequences with meaningful divergence.
- **Default E-value threshold of 0.05 is stringent**: May miss weak but real signals. Adjust with `-e` option for exploratory analysis, but validate findings independently.
- **Pseudoknot handling is limited**: While R-scape accepts pseudoknotted structures, its statistical model assumes nested structures. Covariation in pseudoknots may be underestimated.
- **Requires external tools for visualization**: The web server provides visualization; command-line output requires additional scripts (CaCoFold integration available).
- **Memory intensive for large alignments**: Alignments with >100 sequences or >1000 columns may require substantial memory. Consider subsetting or using the web server.

## Examples

### Analyze an alignment for conserved structure
**Args:** `rscape -i alignment.sto -o results`
**Explanation:** `-i` specifies input Stockholm file; `-o` sets output directory. Runs in "evaluate region" mode, testing all possible pairs equally. Outputs include covarying_pairs.tsv and structure plots.

### Evaluate a proposed structure
**Args:** `rscape -i alignment.sto -s proposed.structure -o results`
**Explanation:** `-s` provides a consensus structure in dot-bracket format. R-scape performs separate tests on proposed base pairs vs. background pairs. Use when validating a known structure.

### Predict a new structure from covariation
**Args:** `rscape -i alignment.sto --predict -o results`
**Explanation:** `--predict` enables structure prediction mode. R-scape identifies covarying pairs and uses CaCoFold to generate a consensus structure compatible with significant covariations.

### Run with alternative statistic
**Args:** `rscape -i alignment.sto --stat MI -o results`
**Explanation:** `--stat MI` uses mutual information instead of the default G-test. Other options: MIr, MIg, CHI, OMES, RaF, RAFS. MI is more sensitive but less specific.

### Adjust E-value threshold
**Args:** `rscape -i alignment.sto -e 0.1 -o results`
**Explanation:** `-e 0.1` relaxes the significance threshold to 10% false discovery rate. Use for exploratory analysis when looking for weaker signals.

### Generate power analysis
**Args:** `rscape -i alignment.sto --power -o results`
**Explanation:** `--power` calculates the statistical power to detect covarying pairs given the alignment's sequence diversity. Useful for assessing alignment quality before downstream analysis.