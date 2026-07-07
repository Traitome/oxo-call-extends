---
name: mauvealigner
category: alignment
description: Command-line tools for generating multiple genome alignments handling large-scale evolutionary events.
tags: [mauvealigner, genome-alignment, progressive-alignment]
author: oxo-call-community
source_url: "http://darlinglab.org/mauve/"
---

## Concepts

- **Tool Overview**: mauveAligner provides command-line tools for multiple genome alignment.
- **Core Function**: Aligns multiple genomes accounting for rearrangements and inversions.
- **Progressive Alignment**: Uses progressiveMauve algorithm for multiple sequence alignment.
- **Genome Rearrangement**: Handles large-scale evolutionary events like inversions and translocations.
- **Input/Output**: Accepts FASTA genome sequences, produces XMFA format alignments.
- **Installation**: `conda install -c bioconda mauvealigner`

## Pitfalls

- **Memory Requirements**: Aligning multiple large genomes requires significant memory.
- **Computation Time**: Can be slow for many genomes or large sequences.
- **Sequence Quality**: Low-quality sequences affect alignment accuracy.
- **Genome Order**: Input order can affect alignment results.
- **Parameter Tuning**: Requires careful parameter adjustment for optimal results.
- **Output Format**: XMFA format may require conversion for downstream tools.

## Examples

### Align two genomes
**Args:** `mauveAligner --output=alignment.xmfa ref.fasta query.fasta`
**Explanation:** Aligns two genomes and outputs in XMFA format.

### Progressive alignment
**Args:** `progressiveMauve --output=alignment.xmfa genome1.fasta genome2.fasta genome3.fasta`
**Explanation:** Creates progressive alignment of multiple genomes.

### With seed families
**Args:** `mauveAligner --output=alignment.xmfa --seed-family=seeds.txt ref.fasta query.fasta`
**Explanation:** Uses custom seed families for alignment.

### Adjust minimum LCB score
**Args:** `mauveAligner --output=alignment.xmfa --min-lcb-score=1000 ref.fasta query.fasta`
**Explanation:** Sets minimum LCB score threshold.

### Threaded alignment
**Args:** `progressiveMauve --output=alignment.xmfa --threads=8 *.fasta`
**Explanation:** Uses 8 threads for parallel computation.

### Help documentation
**Args:** `mauveAligner --help`
**Explanation:** Displays available commands and options.
