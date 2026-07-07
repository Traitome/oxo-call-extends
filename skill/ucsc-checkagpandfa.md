---
name: ucsc-checkagpandfa
category: utility
description: UCSC checkAgpAndFa - Tool for checking AGP and FASTA files.
tags: [ucsc-checkagpandfa, ucsc, quality-control, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC checkAgpAndFa - A tool for validating AGP and FASTA file consistency.
- **Core Function**: Checks consistency between AGP and FASTA files.
- **Input**: AGP file, FASTA file.
- **Output**: Validation report.
- **Installation**: Part of UCSC utilities
- **Use Case**: Quality control, genome assembly validation.

## Pitfalls

- **File Format**: Requires proper AGP format.
- **Sequence Names**: Requires matching sequence names.

## Examples

### Check AGP and FASTA
**Args:** `checkAgpAndFa assembly.agp assembly.fa`
**Explanation:** Validate AGP and FASTA consistency.

### With verbose output
**Args:** `checkAgpAndFa -verbose assembly.agp assembly.fa`
**Explanation:** Check with detailed output.
