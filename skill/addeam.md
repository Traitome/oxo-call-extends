---
name: addeam
category: epigenomics
description: Fast and scalable tool for estimating and clustering reference-level damage profiles in ancient DNA
tags: [ancient-dna, damage, clustering, gmm, authentication]
author: oxo-call-community
source_url: "https://github.com/LouisPwr/AdDeam"
---

## Concepts

- **Tool Overview**: AdDeam estimates and clusters DNA damage profiles at reference level, enabling authentication of ancient DNA and detection of UDG treatment levels.
- **Core Function**: Generates damage profiles from BAM files and clusters them using Gaussian Mixture Models (GMMs) to differentiate between damaged and undamaged samples.
- **Input/Output**: Input: BAM files with MD tags. Output: Damage profile files (*.prof), clustering reports, and visualization plots.
- **Two-Step Workflow**: First generate profiles with `addeam-bam2prof.py`, then cluster with `addeam-cluster.py`.
- **Installation**: Install via bioconda: `conda install -c bioconda addeam`

## Pitfalls

- **MD Tags Required**: BAM files must have MD tags - add them with `samtools calmd -b input.bam reference.fasta > output.bam` before running.
- **Two Modes**: Meta mode (per-reference) for metagenomics; Classic mode (per-BAM) for single sample analysis.
- **Clustering K Values**: Default tests k=2,3,4 clusters - adjust if you expect different numbers of damage levels.
- **Read Depth**: Low-coverage references may be excluded from analysis due to insufficient data.

## Examples

### Display help for profile generation
**Args:** `addeam-bam2prof.py --help`
**Explanation:** Shows options for generating damage profiles from BAM files.

### Generate damage profiles in Classic mode
**Args:** `addeam-bam2prof.py -classic -o profiles/classic bam_list.txt`
**Explanation:** Generates one damage profile per BAM file for single-sample ancient DNA analysis.

### Generate damage profiles in Meta mode
**Args:** `addeam-bam2prof.py -meta -o profiles/meta bam_list.txt`
**Explanation:** Generates separate profiles per reference sequence, suitable for metagenomics data.

### Cluster damage profiles
**Args:** `addeam-cluster.py -i profiles/meta -o clusters/meta`
**Explanation:** Clusters damage profiles using GMM, generating reports and visualizations.

### Add MD tags to BAM file
**Args:** `samtools calmd -b input.bam reference.fasta > output.bam`
**Explanation:** Prerequisite step to add MD tags required by AdDeam for damage pattern detection.

### Cluster with custom K values
**Args:** `addeam-cluster.py -i profiles/ -o clusters/ --k-values 2,3,4,5`
**Explanation:** Tests additional cluster numbers to find optimal grouping of damage profiles.

### Specify custom bam2prof binary
**Args:** `addeam-bam2prof.py -classic --bam2profpath /path/to/bam2prof -o profiles/ bam_list.txt`
**Explanation:** Uses custom path for the compiled bam2prof binary if not in default location.
