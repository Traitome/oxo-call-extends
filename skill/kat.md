---
name: kat
category: utility
description: K-mer Analysis Toolkit - analyse jellyfish hashes or sequence files using k-mer counts.
tags: [kat, utility, k-mer, jellyfish, sequence analysis]
author: oxo-call-community
source_url: "https://kat.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: kat (v2.4.2) - K-mer Analysis Toolkit for sequence analysis.
- **k-mer Counting**: Analyzes k-mer frequencies in sequence data.
- **Jellyfish Integration**: Works with jellyfish hash outputs.
- **Quality Control**: Provides QC metrics for sequencing data.
- **Visualization**: Generates k-mer spectrum plots.
- **Assembly Assessment**: Evaluates assembly quality using k-mers.

## Pitfalls

- **Memory Usage**: k-mer counting requires significant memory.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Hash Size**: Jellyfish hash size affects performance.
- **Input Size**: Large input files require more resources.
- **Output Size**: k-mer spectra can be large files.
- **Time Complexity**: Processing large datasets can be slow.

## Examples

### Count k-mers
**Args:** `kat count -t 8 -o kmer_counts reads.fastq`
**Explanation:** Counts k-mers in FASTQ file with 8 threads.

### Generate k-mer spectrum
**Args:** `kat hist -i kmer_counts.jf -o kmer_spectrum.png`
**Explanation:** Generates k-mer spectrum histogram.

### Compare two k-mer sets
**Args:** `kat comp -i1 sample1.jf -i2 sample2.jf -o comparison.png`
**Explanation:** Compares k-mer profiles of two samples.

### Validate assembly
**Args:** `kat validate -a assembly.fasta -r reads.fastq -o validation.txt`
**Explanation:** Validates assembly against reads.

### Generate statistics
**Args:** `kat stats -i kmer_counts.jf -o stats.txt`
**Explanation:** Generates k-mer statistics.

### Convert to matrix
**Args:** `kat matrix -i kmer_counts.jf -o matrix.txt`
**Explanation:** Outputs k-mer counts as matrix.