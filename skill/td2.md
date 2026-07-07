---
name: td2
category: analysis
description: TD2 - Tandem Duplicate Detector for identifying and analyzing tandem duplications in genomic sequences.
tags: [td2, tandem-duplication, genomics, structural-variation, copy-number, duplication]
author: oxo-call-community
source_url: "https://github.com/GenomeDynamics/td2"
---

## Concepts

- **Tool Overview**: TD2 (Tandem Duplication Detector) - A tool for detecting and analyzing tandem duplications in genomic sequences.
- **Core Function**: Identifies tandem duplicate regions in DNA sequences by analyzing sequence similarity patterns and genomic context.
- **Input**: Genomic sequences in FASTA format, optionally with annotation files.
- **Output**: Reports of tandem duplication events with coordinates, lengths, and sequence similarity scores.
- **Installation**: `pip install td2` or `conda install -c bioconda td2`
- **Use Case**: Studying genomic rearrangements, evolutionary duplications, and copy number variations.

## Pitfalls

- **Reference Quality**: Detection accuracy depends on quality of input reference genome.
- **Parameters**: May require adjustment of similarity and distance thresholds for different organisms.
- **Tandem Specific**: Only detects tandem duplications - other duplication types may be missed.

## Examples

### Detect tandem duplications
**Args:** `td2 -i genome.fasta -o duplications.txt`
**Explanation:** Scan genome for tandem duplications and output results.

### With minimum length filter
**Args:** `td2 -i genome.fasta -o results.txt -l 1000`
**Explanation:** Only report duplications longer than 1000 bp.

### Verbose output
**Args:** `td2 -i genome.fasta --verbose -o output.txt`
**Explanation:** Enable detailed logging of detection process.
