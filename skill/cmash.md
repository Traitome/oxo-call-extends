---
name: cmash
category: assembly
description: Fast and accurate set similarity estimation via containment min hash for genomic datasets
tags: [cmash, minhash, similarity-estimation, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dkoslicki/CMash"
---

## Concepts

- **Tool Overview**: CMash is a tool for fast and accurate set similarity estimation using containment min hash, specifically designed for genomic datasets.
- **Core Function**: Estimates similarity between genomic sequences using probabilistic data structures for efficient comparison.
- **Algorithm**: Uses containment min hash to quickly estimate the similarity between sets of k-mers from genomic sequences.
- **Input**: FASTA/FASTQ sequence files or precomputed sketches.
- **Output**: Similarity estimates between sequences.
- **Application**: Metagenomics, sequence comparison, and genomic dataset analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cmash`

## Pitfalls

- **k-mer Size**: Requires appropriate k-mer size selection for specific datasets.
- **Sketch Size**: Larger sketches improve accuracy but increase memory usage.
- **Sequence Quality**: Poor quality sequences may affect similarity estimation.
- **Memory Usage**: May require significant memory for large datasets.
- **Computational Time**: Sketch generation can be time-consuming for large genomes.

## Examples

### Compute similarity
**Args:** `cmash -i genome1.fasta genome2.fasta -o similarity.txt`
**Explanation:** Estimates similarity between two genomic sequences.

### Generate sketch
**Args:** `cmash sketch -i genome.fasta -o genome.sketch`
**Explanation:** Generates min hash sketch from genomic sequence.

### Compare with sketch
**Args:** `cmash compare -i genome.fasta -s reference.sketch -o results.txt`
**Explanation:** Compares sequence against precomputed sketch.

### Display help
**Args:** `cmash --help`
**Explanation:** Shows all available options and usage information.