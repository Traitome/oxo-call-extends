---
name: trawler
category: analysis
description: TRAWLER - Tool for analyzing tandem repeats and low-complexity regions.
tags: [trawler, tandem-repeat, low-complexity, sequence-analysis, genomics]
author: oxo-call-community
source_url: "https://github.com/compbio/trawler"
---

## Concepts

- **Tool Overview**: TRAWLER - A tool for identifying and analyzing tandem repeats and low-complexity regions in sequences.
- **Core Function**: Detects tandem repeats, microsatellites, and low-complexity regions in genomic sequences.
- **Input**: Sequence files (FASTA), optional quality data.
- **Output**: Repeat annotations, complexity metrics, statistical analysis.
- **Installation**: `pip install trawler` or `conda install -c bioconda trawler`
- **Use Case**: Repeat analysis, genome annotation, evolutionary studies.

## Pitfalls

- **Complex Repeats**: Complex repeat structures may be difficult to resolve.
- **Performance**: May be slow for very long sequences.

## Examples

### Find repeats
**Args:** `trawler -i sequence.fasta -o repeats/`
**Explanation:** Identify tandem repeats and low-complexity regions.

### With quality filter
**Args:** `trawler -i genome.fasta -q 20 -o filtered_repeats/`
**Explanation:** Filter repeats by quality threshold.
