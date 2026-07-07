---
name: trf
category: analysis
description: TRF - Tandem Repeat Finder for identifying tandem repeats in DNA sequences.
tags: [trf, tandem-repeat, repeat-finder, dna-analysis, genomics]
author: oxo-call-community
source_url: "https://tandem.bu.edu/trf/trf.html"
---

## Concepts

- **Tool Overview**: TRF - Tandem Repeat Finder for identifying tandem repeats in DNA sequences.
- **Core Function**: Detects tandem repeats, microsatellites, and minisatellites in genomic sequences.
- **Input**: DNA sequences (FASTA), optional quality data.
- **Output**: Repeat annotations, repeat coordinates, consensus sequences.
- **Installation**: `conda install -c bioconda trf`
- **Use Case**: Genome annotation, repeat analysis, microsatellite identification.

## Pitfalls

- **Performance**: May be slow for very large sequences.
- **Complex Repeats**: Complex repeat structures may be missed.

## Examples

### Find repeats
**Args:** `trf sequence.fasta 2 7 7 80 10 50 500 -f -d -m`
**Explanation:** Identify tandem repeats with default parameters.

### With quality
**Args:** `trf genome.fasta 2 7 7 80 10 50 500 -f -d -m -q quality.txt`
**Explanation:** Find repeats with quality filtering.
