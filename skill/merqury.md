---
name: merqury
category: assembly
description: Evaluate genome assembly quality using k-mer spectrum analysis.
tags: [merqury, assembly-validation, k-mer-analysis]
author: oxo-call-community
source_url: "https://github.com/marbl/merqury"
---

## Concepts

- **Tool Overview**: Merqury evaluates genome assemblies using k-mer analysis.
- **Core Function**: Assembly quality assessment without reference.
- **k-mer Spectrum**: Uses k-mer frequencies for evaluation.
- **Quality Metrics**: Computes QV and completeness metrics.
- **Reference-free**: Works without reference genome.
- **Installation**: `conda install -c bioconda merqury`

## Pitfalls

- **Memory Requirements**: High memory for large k-mer databases.
- **Computation Time**: Slow for large datasets.
- **k-mer Selection**: k-mer size affects results.
- **Illumina Data**: Requires Illumina sequencing data.
- **Parameter Tuning**: Requires careful configuration.
- **Output Interpretation**: Complex results require expertise.

## Examples

### Evaluate assembly
**Args:** `merqury.sh assembly.fasta kmer_db.meryl prefix`
**Explanation:** Evaluates assembly quality.

### Build k-mer database
**Args:** `meryl count k=21 output kmer_db.meryl reads.fastq`
**Explanation:** Builds k-mer database from reads.

### Compute QV
**Args:** `merqury qv assembly.fasta kmer_db.meryl -o qv.txt`
**Explanation:** Computes quality value.

### Plot k-mer spectrum
**Args:** `merqury plot kmer_db.meryl -o spectrum.pdf`
**Explanation:** Generates k-mer spectrum plot.

### Help documentation
**Args:** `merqury.sh --help`
**Explanation:** Displays available options.
