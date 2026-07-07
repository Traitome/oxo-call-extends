---
name: mccortex
category: alignment
description: De novo genome assembly and multisample variant calling using cortex graphs.
tags: [mccortex, genome-assembly, variant-calling]
author: oxo-call-community
source_url: "https://github.com/mcveanlab/mccortex"
---

## Concepts

- **Tool Overview**: McCortex performs de novo assembly and variant calling.
- **Core Function**: Builds cortex graphs for genome analysis.
- **Graph Construction**: Constructs colored de Bruijn graphs.
- **Variant Calling**: Identifies variants across multiple samples.
- **De Novo Assembly**: Assembles genomes without reference.
- **Installation**: `conda install -c bioconda mccortex`

## Pitfalls

- **Memory Requirements**: High memory usage for large datasets.
- **Computation Time**: Slow for large genomes.
- **k-mer Selection**: k-mer choice affects assembly quality.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Graph Complexity**: Complex graphs can be hard to interpret.
- **Data Quality**: Low-quality reads affect assembly.

## Examples

### Build cortex graph
**Args:** `mccortex build -k 31 -s sample1 -1 reads_1.fq -2 reads_2.fq -o graph.ctx`
**Explanation:** Builds cortex graph from paired-end reads.

### Merge graphs
**Args:** `mccortex merge -o merged.ctx graph1.ctx graph2.ctx`
**Explanation:** Merges multiple cortex graphs.

### Call variants
**Args:** `mccortex call -r ref.fasta graph.ctx -o variants.vcf`
**Explanation:** Calls variants from cortex graph.

### View graph stats
**Args:** `mccortex stats graph.ctx`
**Explanation:** Shows graph statistics.

### Export graph
**Args:** `mccortex view graph.ctx -o graph.gfa`
**Explanation:** Exports graph in GFA format.

### Help documentation
**Args:** `mccortex --help`
**Explanation:** Displays available commands and options.
