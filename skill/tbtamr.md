---
name: tbtamr
category: analysis
description: TB-TAMR - Analysis tool for tuberculosis tandem amplifier mutations and repeat regions.
tags: [tbtamr, tuberculosis, tandem-repeat, mutation-analysis, mycobacterium, structural-variation]
author: oxo-call-community
source_url: "https://github.com/kwongj/tbtamr"
---

## Concepts

- **Tool Overview**: tbtamr - A specialized tool for detecting and analyzing tandem repeat mutations in M. tuberculosis genomes, particularly for tracking antimicrobial resistance mechanisms.
- **Core Function**: Identifies expansions and contractions in tandem repeat regions that may be associated with drug resistance phenotypes.
- **Input**: FASTA sequences or BAM files from M. tuberculosis sequencing.
- **Output**: Tables of tandem repeat genotypes with length variations and associations.
- **Installation**: `pip install tbtamr` or `conda install -c bioconda tbtamr`
- **Use Case**: Tracking TB drug resistance linked to tandem repeat mutations, complementing SNP-based profiling.

## Pitfalls

- **Specific to TB**: Designed specifically for M. tuberculosis repeat regions - not general purpose.
- **Reference Dependence**: Requires accurate reference genome for repeat counting.
- **Interpretation**: Repeat length changes may not always correlate with phenotype.

## Examples

### Basic tandem repeat analysis
**Args:** `tbtamr -i genome.fasta -o repeats.tsv`
**Explanation:** Identify tandem repeats in genome sequence.

### BAM input
**Args:** `tbtamr --bam alignment.bam -o results.tsv`
**Explanation:** Analyze repeat regions from aligned reads.

### Compare samples
**Args:** `tbtamr compare -i sample1.tsv sample2.tsv -o comparison.txt`
**Explanation:** Compare repeat profiles between samples.
