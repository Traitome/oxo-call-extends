---
name: abundancebin
category: metagenomics
description: Abundance-based tool for binning metagenomic sequences.
tags: [abundancebin, metagenomics, binning, sequences, l-tuples]
author: oxo-call-community
source_url: "https://omics.informatics.indiana.edu/AbundanceBin"
---

## Concepts

- **Tool Overview**: AbundanceBin (v1.0.1) is an abundance-based tool for binning metagenomic sequences such that reads classified in a bin belong to species of identical or very similar abundances.
- **Core Function**: Bins metagenomic sequences by abundance similarity and estimates species abundances and genome sizes.
- **Algorithm**: Uses l-tuples for sequence comparison and abundance-based clustering.
- **Scientific Paper**: Yu-Wei Wu and Yuzhen Ye. A novel abundance-based algorithm for binning metagenomic sequences using l-tuples. Lecture Notes in Computer Science, 2010, Volume 6044/2010, 535-549 (RECOMB 2010).
- **Input**: Metagenomic sequence reads (FASTA/FASTQ format)
- **Output**: Binned sequences organized by species abundance, abundance estimates, and genome size estimates
- **Installation**: `conda install -c bioconda abundancebin`
- **Platform**: Linux (x86_64, aarch64), macOS (arm64)
- **Dependencies**: libgcc (>=13), libstdcxx (>=13)

## Pitfalls

- **Version Differences**: Options may vary between versions; v1.0.1 is the latest stable release.
- **Input Format**: Requires FASTA or FASTQ formatted sequence files.
- **Abundance Sensitivity**: Designed for species with similar abundances; may not perform well with highly uneven abundance distributions.
- **Sequence Length**: Optimal for moderate-length reads; very short reads may reduce binning accuracy.
- **Memory Requirements**: Large datasets may require significant memory allocation.
- **Reference-Free**: Does not use reference databases; binning is purely based on abundance patterns.

## Examples

### Display help information
**Args:** `abundancebin -h`
**Explanation:** Shows all available command-line options including input/output parameters and algorithm settings.

### Basic binning with default parameters
**Args:** `abundancebin -i contigs.fasta -o output_bins/`
**Explanation:** Bins metagenomic contigs by abundance similarity and outputs results to the specified directory. Creates separate bins for sequences with similar abundance profiles.

### Binning with custom k-mer size
**Args:** `abundancebin -i reads.fastq -o bins/ -k 25`
**Explanation:** Uses k-mer size of 25 for sequence comparison instead of the default value. Larger k-mer sizes may improve specificity but reduce sensitivity.

### Binning with abundance threshold
**Args:** `abundancebin -i contigs.fasta -o output/ -t 0.01`
**Explanation:** Sets a minimum abundance threshold of 0.01 (1%) for including sequences in bins. Filters out low-abundance sequences that may be noise.

### Batch processing multiple files
**Args:** `abundancebin -i sample1.fasta sample2.fasta -o combined_bins/`
**Explanation:** Processes multiple input files together and creates combined bins across all samples. Useful for comparative metagenomics analysis.

### Binning with verbose output
**Args:** `abundancebin -i reads.fastq -o bins/ -v`
**Explanation:** Enables verbose mode to display detailed progress information during binning, including abundance estimates for each bin.