---
name: metaprob
category: expression
description: assembly-assisted tool for un-supervised metagenomic binning
tags: [metaprob, expression, metagenomic-binning]
author: oxo-call-community
source_url: "https://bitbucket.org/samu661/metaprob/"
---

## Concepts

- **Tool Overview**: MetaProb v2 is an assembly-assisted tool for unsupervised metagenomic binning using probabilistic sequence signatures.
- **Core Function**: Bins metagenomic reads into taxonomic or functional groups without prior reference sequences.
- **Probabilistic Binning**: Uses l-mer frequencies converted into probabilistic sequence signatures for accurate binning.
- **Assembly-Assisted**: Leverages assembly information to improve binning accuracy.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs binned sequences with probabilistic assignments.
- **Multi-read Support**: Effective for both short-read (Illumina) and long-read (PacBio/ONT) sequencing data.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Binning complex metagenomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Binning accuracy depends on input read quality.
- **Abundance Bias**: May struggle with samples containing organisms at very different abundance levels.

## Examples

### Bin metagenomic reads
**Args:** `metaprob -i reads.fastq -o bins/`
**Explanation:** Performs unsupervised binning of metagenomic reads.

### With assembly guidance
**Args:** `metaprob -i reads.fastq -a assembly.fasta -o bins/`
**Explanation:** Uses assembly information to guide binning.

### Long-read binning
**Args:** `metaprob -i long_reads.fastq -o bins/ -l`
**Explanation:** Optimizes binning for long-read sequencing data.

### Adjust sensitivity
**Args:** `metaprob -i reads.fastq -o bins/ -s 0.9`
**Explanation:** Sets binning sensitivity to 0.9.

### Batch processing
**Args:** `metaprob -i fastq/ -o results/`
**Explanation:** Processes multiple FASTQ files in batch mode.