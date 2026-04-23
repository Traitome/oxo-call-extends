---
name: bgreat
category: alignment
description: BGREAT2 - Read mapping tool for aligning reads on a de Bruijn graph
tags: [read-mapping, de-bruijn-graph, ngs, alignment]
author: oxo-call-community
source_url: "https://github.com/Malfoy/BGREAT2"
---

## Concepts
- **Tool Overview**: BGREAT2 is a read mapping tool that aligns NGS sequencing reads onto a de Bruijn graph rather than a linear reference. This approach can capture structural variations and novel sequences not present in the reference.
- **De Bruijn Graph Mapping**: Instead of mapping to a linear reference genome, BGREAT2 maps reads to a de Bruijn graph constructed from reads or assemblies.
- **Applications**: Useful for mapping reads from heterogeneous samples, metagenomics, and detecting structural variants.
- **Integration**: Can be used as a preprocessing step for tools like Bcool (short read corrector).

## Pitfalls
- **Graph Construction**: Requires a pre-built de Bruijn graph. Graph quality affects mapping accuracy.
- **Memory Usage**: De Bruijn graphs for large genomes require significant memory.
- **Output Format**: Output format differs from standard SAM/BAM and may require conversion.

## Examples
### Map reads to de Bruijn graph
**Args:** `bgreat2 -g graph.gfa -r reads.fq -o mappings.paf`
**Explanation:** Maps reads to a de Bruijn graph in GFA format.

### Map with specific k-mer size
**Args:** `bgreat2 -g graph.gfa -r reads.fq -k 31 -o mappings.paf`
**Explanation:** Maps reads using k-mer size 31 for graph traversal.
