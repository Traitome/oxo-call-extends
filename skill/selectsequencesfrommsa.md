---
name: selectsequencesfrommsa
category: alignment
description: selectsequencesfrommsa - Select representative sequences from multiple sequence alignment
tags: ["selectsequencesfrommsa", "alignment", "MSA", "sequence-selection"]
author: oxo-call-community
source_url: "https://github.com/eggzilla/SelectSequencesFromMSA"
---

## Concepts

- **Tool Overview**: selectsequencesfrommsa (v1.0.5) selects representative sequences from multiple sequence alignments.
- **Core Function**: Identifies and extracts representative sequences from MSAs.
- **Algorithm**: Uses diversity-based selection to pick representative sequences.
- **Input/Output**: Accepts MSA files and produces subset alignments.
- **Diversity Sampling**: Focuses on selecting diverse representative sequences.
- **Applications**: Phylogenetics, sequence analysis, and data reduction.

## Pitfalls

- **Alignment Quality**: Results depend on input alignment quality.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large MSAs.
- **Computational Resources**: May require significant compute resources.
- **Input Format**: Requires correct alignment format.
- **Sequence Selection**: Selection criteria may not always produce desired results.

## Examples

### Select sequences
**Args:** `selectsequencesfrommsa -i alignment.fasta -n 10 -o selected.fasta`
**Explanation:** `-i` input MSA; `-n 10` select 10 sequences; `-o` output file.

### By similarity threshold
**Args:** `selectsequencesfrommsa -i alignment.fasta -s 0.9 -o selected.fasta`
**Explanation:** `-s 0.9` selects sequences with >90% similarity.

### Random selection
**Args:** `selectsequencesfrommsa -i alignment.fasta -r 10 -o selected.fasta`
**Explanation:** `-r 10` randomly selects 10 sequences.

### Verbose logging
**Args:** `selectsequencesfrommsa -i alignment.fasta -v -o selected.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `selectsequencesfrommsa --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `selectsequencesfrommsa --version`
**Explanation:** Shows current version.

### Output statistics
**Args:** `selectsequencesfrommsa -i alignment.fasta -n 10 -s -o selected.fasta`
**Explanation:** `-s` outputs selection statistics.