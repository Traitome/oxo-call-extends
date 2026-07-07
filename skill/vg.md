---
name: vg
category: bioinformatics
description: vg - Variation graph toolkit.
tags: [vg, variation-graph, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vgteam/vg"
---

## Concepts

- **Tool Overview**: vg - Tools for building and using variation graphs.
- **Core Function**: Constructs and queries variation graphs.
- **Input**: FASTA, VCF files.
- **Output**: Graph representations.
- **Installation**: Install via conda or source
- **Use Case**: Graph-based genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large graphs.
- **Complexity**: May have steep learning curve.

## Examples

### Build graph
**Args:** `vg construct -r ref.fasta -v variants.vcf -o graph.vg`
**Explanation:** Build variation graph.

### With options
**Args:** `vg construct -r ref.fasta -v variants.vcf -o graph.vg -t 8`
**Explanation:** Use 8 threads.
