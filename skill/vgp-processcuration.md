---
name: vgp-processcuration
category: bioinformatics
description: VGP ProcessCuration - Genome curation tool.
tags: [vgp-processcuration, genome-curation, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/VGP/vgp-processcuration"
---

## Concepts

- **Tool Overview**: VGP ProcessCuration - Genome assembly curation.
- **Core Function**: Curates and validates genome assemblies.
- **Input**: Assembly files.
- **Output**: Curated assembly.
- **Installation**: Install via pip or conda
- **Use Case**: Genome assembly, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Curate assembly
**Args:** `vgp-processcuration -i assembly.fasta -o curated/`
**Explanation:** Curate genome assembly.

### With options
**Args:** `vgp-processcuration -i assembly.fasta -o curated/ -t 8`
**Explanation:** Use 8 threads.
