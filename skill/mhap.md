---
name: mhap
category: alignment
description: "MHAP: MinHash Alignment Protocol. A tool for finding overlaps of long-read sequences (such as PacBio or Nanopore) in bioinformatics."
tags: [mhap, alignment, long-read]
author: oxo-call-community
source_url: "https://github.com/marbl/MHAP"
---
## Concepts

- **Tool Overview**: MHAP v2.1.3 is the MinHash Alignment Protocol for finding overlaps between long-read sequences.
- **Core Function**: Finds overlaps between long sequencing reads using MinHash algorithm.
- **MinHash Algorithm**: Uses MinHash for efficient similarity estimation.
- **Long-read Support**: Optimized for PacBio and Oxford Nanopore reads.
- **Input/Output**: Accepts long-read sequences; outputs overlap information.
- **Assembly Support**: Used in de novo assembly pipelines.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal overlap detection.
- **Data Quality**: Overlap detection accuracy depends on read quality.
- **Runtime**: Analysis of large read sets can be time-consuming.
- **Read Length**: Performance may vary with different read lengths.

## Examples

### Find overlaps
**Args:** `mhap -i reads.fastq -o overlaps.txt`
**Explanation:** Finds overlaps between long-read sequences.

### With custom k-mer size
**Args:** `mhap -i reads.fastq -o overlaps.txt -k 21`
**Explanation:** Uses k-mer size of 21 for MinHash.

### Paired-end mode
**Args:** `mhap -i reads_1.fastq -r reads_2.fastq -o overlaps.txt`
**Explanation:** Processes paired-end long reads.

### Generate assembly hints
**Args:** `mhap -i reads.fastq -o overlaps.txt -a`
**Explanation:** Generates hints for assembly.

### Batch processing
**Args:** `mhap -i fastq/ -o overlaps/`
**Explanation:** Processes multiple read files in batch mode.