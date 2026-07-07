---
name: tiddit
category: analysis
description: TIDDIT - Structural variant detection tool for DNA sequencing data.
tags: [tiddit, structural-variant, sv-detection, duplication, deletion, inversion]
author: oxo-call-community
source_url: "https://github.com/SciLifeLab/TIDDIT"
---

## Concepts

- **Tool Overview**: TIDDIT - A tool for detecting structural variants (SV) including deletions, duplications, inversions, and insertions from DNA sequencing data.
- **Core Function**: Uses read-depth, split-read, and discordant read-pair analysis to identify and characterize structural variants.
- **Input**: BAM alignments from whole genome or exome sequencing.
- **Output**: VCF file with called structural variants and annotations.
- **Installation**: `conda install -c bioconda tiddit`
- **Use Case**: Cancer genomics, genetic disease research, population SV studies.

## Pitfalls

- **Read Length**: Longer reads improve SV detection sensitivity.
- **Genome Mappability**: Repetitive regions may cause false positives or missed SVs.

## Examples

### Detect structural variants
**Args:** `tiddit --bam sample.bam --out-prefix sample_sv`
**Explanation:** Detect structural variants from BAM file.

### With custom parameters
**Args:** `tiddit --bam reads.bam --out output --min-size 50 --max-size 1000000`
**Explanation:** Set minimum and maximum SV size thresholds.
