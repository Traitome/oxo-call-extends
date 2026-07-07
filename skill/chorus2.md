---
name: chorus2
category: design
description: Pipeline to select oligonucleotides for fluorescence in situ hybridization (Oligo-FISH)
tags: [chorus2, oligo-fish, oligonucleotides, probe-design, bioinformatics]
author: oxo-call-community
source_url: "https://chorus2.readthedocs.io/en/dev/"
---

## Concepts

- **Tool Overview**: Chorus2 is a comprehensive pipeline for designing oligonucleotide probes for fluorescence in situ hybridization (Oligo-FISH).
- **Core Function**: Selects optimal oligonucleotide sequences for specific genomic regions for FISH experiments.
- **Features**: Probe design, specificity checking, melting temperature optimization, and batch processing.
- **Input**: Genomic target regions (BED format) and reference genome sequence.
- **Output**: Selected oligonucleotide sequences with melting temperatures and specificity scores.
- **Application**: Fluorescence in situ hybridization experiments, spatial genomics, and chromosome painting.
- **Installation**: Install via bioconda: `conda install -c bioconda chorus2`

## Pitfalls

- **Target Region Size**: Probe density depends on target region size.
- **Specificity**: Requires genome reference for specificity checks.
- **Melting Temperature**: Tm optimization critical for hybridization success.
- **GC Content**: Oligos with extreme GC content may have hybridization issues.
- **Repeat Regions**: May need masking of repetitive sequences.

## Examples

### Design probes for target region
**Args:** `chorus2 design -t targets.bed -g genome.fasta -o probes.fasta`
**Explanation:** Designs oligonucleotide probes for specified target regions.

### Optimize probes
**Args:** `chorus2 optimize -i probes.fasta -o optimized.fasta`
**Explanation:** Optimizes probe sequences for better hybridization.

### Check specificity
**Args:** `chorus2 specificity -i probes.fasta -g genome.fasta -o specificity.txt`
**Explanation:** Checks probe specificity against reference genome.

### Display help
**Args:** `chorus2 --help`
**Explanation:** Shows all available commands and options.