---
name: alleleflux
category: population-genomics
description: A tool for fine-grained evolutionary analysis of microbial populations and communities, identifying genomic targets of natural selection
tags: [alleleflux, metagenomics, allele-frequencies, evolution, microbial-populations]
author: oxo-call-community
source_url: "https://github.com/MoellerLabPU/AlleleFlux"
---

## Concepts

- **Tool Overview**: AlleleFlux is a Python package designed for fine-grained evolutionary analysis of microbial populations and communities, enabling identification of genomic targets of natural selection in bacterial communities.
- **Core Function**: Analyzes allele frequency trajectories in metagenomic data, profiling MAG (Metagenome-Assembled Genome) populations across samples to detect parallel evolution and selection signals.
- **Input/Output**: Input: BAM/SAM alignments, MAG sequences, metagenomic reads. Output: Allele frequency tables, selection statistics, evolutionary trajectories.
- **Key Features**: Detects parallel evolution, identifies selection targets, profiles population dynamics across samples.
- **Installation**: Install via bioconda: `conda install -c bioconda alleleflux`
- **License**: GPL-3.0

## Pitfalls

- **MAG Quality**: Requires high-quality metagenome-assembled genomes for accurate analysis.
- **Coverage Depth**: Sufficient sequencing depth is required for reliable allele frequency estimation.
- **Reference Genome**: Needs appropriate reference genome for mapping.
- **Computational Resources**: Large datasets may require significant computational resources.
- **Contamination**: Contaminating sequences can affect allele frequency estimates.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available command-line options and usage instructions.

### Profile allele frequencies
**Args:** `alleleflux profile -i alignments.bam -r reference.fasta -o profiles.tsv`
**Explanation:** Profiles allele frequencies from BAM alignments against reference genome.

### Detect selection signals
**Args:** `alleleflux detect-selection -i profiles.tsv -o selection_results.tsv`
**Explanation:** Identifies genomic regions under selection based on allele frequency trajectories.

### Analyze population dynamics
**Args:** `alleleflux dynamics -i profiles.tsv -t time_points.txt -o dynamics.pdf`
**Explanation:** Analyzes temporal changes in allele frequencies across time points.

### Compare populations
**Args:** `alleleflux compare -i population1.tsv population2.tsv -o comparison.tsv`
**Explanation:** Compares allele frequency profiles between two populations.

### Generate visualization
**Args:** `alleleflux plot -i profiles.tsv -o allele_freq_plot.pdf`
**Explanation:** Generates visualization of allele frequency trajectories.

### Filter low-coverage sites
**Args:** `alleleflux filter -i profiles.tsv -c 10 -o filtered.tsv`
**Explanation:** Filters out sites with coverage below 10x.

### Merge multiple samples
**Args:** `alleleflux merge -i sample1.tsv sample2.tsv sample3.tsv -o merged.tsv`
**Explanation:** Merges allele frequency profiles from multiple samples.

### Run complete pipeline
**Args:** `alleleflux pipeline -i alignments/ -r reference.fasta -o results/`
**Explanation:** Runs the complete analysis pipeline from alignment to selection detection.
