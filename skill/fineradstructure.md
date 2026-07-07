---
name: fineradstructure
category: population-genomics
description: "fineRADstructure is an adaptation of the fineSTRUCTURE algorithm for RAD-seq data, enabling population structure inference in non-model organisms."
tags: [fineradstructure, population-genomics, RAD-seq, population-structure, bioinformatics, genetics, haplotype]
author: oxo-call-community
source_url: "https://www.milan-malinsky.org/fineradstructure"
---

## Concepts

- **Tool Overview**: fineRADstructure is an adaptation of the fineSTRUCTURE algorithm specifically designed for RAD-seq (Restriction-site Associated DNA Sequencing) data in non-model organisms. It enables population structure inference where traditional methods fail due to unknown marker positions, lack of reference genomes, or unphased data.
- **Core Function**: Performs haplotype-based population structure analysis by constructing a co-ancestry matrix from RAD-seq data, then clustering individuals using Markov chain Monte Carlo (MCMC) methods.
- **Input/Output**: Input: RAD-seq data in various formats (Stacks output, custom RAD data). Output: Co-ancestry matrix, population clustering assignments, phylogenetic tree of populations.
- **Algorithm**: Extends the ChromoPainter/fineSTRUCTURE approach to work without known genomic positions. Uses the Li-Stephens haplotype copying model adapted for RAD loci. The pipeline includes RADpainter for matrix construction and finestructure for clustering.
- **Key Features**: Works without reference genomes or phased data, integrates with common RAD-seq pipelines (Stacks, ipyrad), supports both single and paired-end RAD data, provides high resolution for recent shared ancestry detection.
- **Installation**: `conda install -c bioconda fineradstructure` or download from http://cichlid.gurdon.cam.ac.uk/fineRADstructure.html

## Pitfalls

- **Data Quality**: RAD-seq data quality significantly affects results. Ensure high-quality reads and appropriate filtering for missing data and paralogs.
- **Sample Size**: Requires sufficient samples per population for reliable structure inference. Small sample sizes may lead to unstable MCMC convergence.
- **Data Conversion**: Different RAD-seq pipelines (Stacks, ipyrad, pyRAD) produce different output formats. Use appropriate conversion scripts (e.g., Stacks2fineRAD.py).
- **MCMC Convergence**: The MCMC algorithm requires sufficient iterations to converge. Always check convergence diagnostics before interpreting results.
- **Invariant Loci**: The pipeline automatically removes invariant loci, which is necessary for analysis but may reduce power for closely related populations.

## Examples

### Calculate co-ancestry matrix with RADpainter
**Args:** `RADpainter paint AlpinePlants.data`
**Explanation:** Calculates the co-ancestry matrix from RAD-seq data. The matrix counts RAD loci where one individual has the most similar allele to another, summarizing nearest-neighbor haplotype relationships.

### Run fineSTRUCTURE MCMC clustering
**Args:** `finestructure -x 100000 -y 100000 -z 1000 AlpinePlants_chunks.out AlpinePlants_chunks.mcmc.xml`
**Explanation:** Runs the MCMC clustering algorithm on the co-ancestry matrix. Parameters: -x burn-in, -y iterations, -z sampling interval. Adjust based on dataset size.

### Convert Stacks output to fineRADstructure format
**Args:** `python Stacks2fineRAD.py -i Tortoises_Stacks_output.tsv -n 5 -m 20`
**Explanation:** Converts Stacks population analysis output to fineRADstructure format. The -n parameter sets minimum samples per locus, -m sets minimum stacks depth.

### Extract population assignments
**Args:** `finestructure -m T AlpinePlants_chunks.mcmc.xml`
**Explanation:** Extracts the population assignments from the MCMC chain. The -m flag specifies mode (T = best assignment for each individual).

### Run finestructure GUI mode
**Args:** `finestructureGui`
**Explanation:** Launches the graphical user interface for interactive exploration of results, visualization of the co-ancestry matrix, and tree building.

### Post-process with R scripts
**Args:** `Rscript finestructure.R AlpinePlants_chunks.mcmc.xml`
**Explanation:** After clustering, use fineSTRUCTURE's R scripts to create visualization plots, assess MCMC convergence, and explore the relationship between genetic clusters and metadata.

### Interpret the co-ancestry matrix
**Args:** `Rscript plot_coancestry.R AlpinePlants_chunks.out`
**Explanation:** The co-ancestry matrix heatmap shows pairwise haplotype similarity. Darker diagonal blocks indicate populations with closer shared ancestry. Off-diagonal patterns reveal admixture and migration history.

### Data preparation best practices
**Args:** `vcftools --gzvcf input.vcf.gz --remove-indels --recode --out filtered`
**Explanation:** Remove paralogous loci, filter for missing data, and ensure consistent sample naming across your dataset before running fineRADstructure. Consider removing low-frequency alleles that may represent sequencing errors.
