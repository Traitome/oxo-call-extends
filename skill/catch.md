---
name: catch
category: utility
description: Design compact and comprehensive capture probe sets for targeted sequencing
tags: [catch, capture, probe-design, targeted-sequencing]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/catch"
---

## Concepts

- **Tool Overview**: CATCH designs capture probe sets for targeted enrichment sequencing.
- **Core Function**: Creates probe sets that cover diverse sequence variants efficiently.
- **Algorithm**: Optimizes probe placement to maximize coverage of genetic diversity.
- **Input**: Reference sequences or multiple sequence alignments.
- **Output**: Probe sequences and coordinates for synthesis.
- **Application**: Viral panel design, pathogen detection, and targeted sequencing.
- **Installation**: Install via bioconda: `conda install -c bioconda catch`

## Pitfalls

- **Sequence Diversity**: Input sequences should represent target diversity.
- **Probe Length**: Adjust probe length based on capture chemistry.
- **Coverage**: More probes increase cost but improve coverage.
- **Specificity**: Check for cross-reactivity with non-target sequences.

## Examples

### Design probes for sequences
**Args:** `catch design -i sequences.fa -o probes.fa`
**Explanation:** Designs capture probes covering input sequence diversity.

### Set probe length
**Args:** `catch design -i sequences.fa -l 120 -o probes.fa`
**Explanation:** Designs 120bp capture probes.

### Set coverage target
**Args:** `catch design -i sequences.fa --coverage 2 -o probes.fa`
**Explanation:** Designs probes with 2x tiling coverage.

### Display help
**Args:** `catch --help`
**Explanation:** Shows all available options and usage information.
