---
name: ucsc-bedcoverage
category: analysis
description: UCSC bedCoverage - Tool for calculating coverage over BED regions.
tags: [ucsc-bedcoverage, ucsc, coverage-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedCoverage - A tool for calculating sequencing coverage over BED-defined regions.
- **Core Function**: Computes coverage statistics for specified genomic regions.
- **Input**: BED file, BAM file or wiggle file.
- **Output**: Coverage statistics per region.
- **Installation**: Part of UCSC utilities
- **Use Case**: Coverage analysis, sequencing depth, genomic profiling.

## Pitfalls

- **BAM Index**: Requires indexed BAM file.
- **Memory**: May require significant memory for large datasets.

## Examples

### Calculate coverage
**Args:** `bedCoverage -i regions.bed -b alignments.bam > coverage.txt`
**Explanation:** Calculate coverage over BED regions.

### With window
**Args:** `bedCoverage -i regions.bed -w 100 -b alignments.bam > coverage.txt`
**Explanation:** Calculate coverage with sliding window.
