---
name: focus
category: metagenomics
description: FOCUS is an innovative and agile model to profile and report organisms present in metagenomic samples based on composition usage without sequence length dependencies.
tags: [focus, metagenomics, taxonomic profiling, composition analysis]
author: oxo-call-community
source_url: "https://edwards.sdsu.edu/FOCUS"
---

## Concepts
- **Composition-based Profiling**: Uses oligonucleotide composition rather than sequence alignment for taxonomic classification.
- **Length-independent**: Works equally well with short and long reads due to composition approach.
- **Reference Database**: Utilizes a pre-built database of genomic signatures from known organisms.
- **K-mer Frequency**: Analyzes k-mer frequency patterns to identify organism presence.
- **Hierarchical Classification**: Classifies reads at multiple taxonomic levels (species, genus, family).

## Pitfalls
- **Database Dependence**: Performance depends on the comprehensiveness of the reference database.
- **Species Misclassification**: May misclassify closely related species with similar genomic composition.
- **Low-abundance Detection**: Struggles with detecting low-abundance organisms in complex communities.
- **Computational Speed**: Slower than alignment-based methods for large datasets.
- **Memory Usage**: Loading the reference database requires significant memory.

## Examples
### Basic metagenomic profiling
**Args:** `focus -q sample.fastq -o profile.txt`
**Explanation:** Profiles a metagenomic sample and outputs taxonomic composition.

### Specify custom database
**Args:** `focus -q sample.fastq -d custom_db/ -o profile.txt`
**Explanation:** Uses a custom reference database for taxonomic profiling.

### Profile at genus level
**Args:** `focus -q sample.fastq -l genus -o profile_genus.txt`
**Explanation:** Profiles sample and reports results at the genus taxonomic level.

### Paired-end read analysis
**Args:** `focus -q sample_R1.fastq -r sample_R2.fastq -o profile.txt`
**Explanation:** Analyzes paired-end metagenomic reads for improved accuracy.

### Generate visualization
**Args:** `focus -q sample.fastq -o profile.txt --plot`
**Explanation:** Generates a bar plot visualization of the taxonomic profile.