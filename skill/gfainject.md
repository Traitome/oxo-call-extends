---
name: gfainject
category: graph-alignment
description: gfainject - Inject alignment into pangenome graphs.
tags: [gfainject, graph-alignment, pangenome, GFA]
author: oxo-call-community
source_url: "https://github.com/AndreaGuarracino/gfainject"
---

## Concepts
- **Graph Alignment**: Aligns sequences to pangenome graphs.
- **Pangenome Graphs**: Works with pangenome graph structures.
- **Alignment Injection**: Injects alignment information into graphs.
- **Variant Representation**: Represents variants in graph format.
- **Graph Modification**: Modifies graphs with alignment data.

## Pitfalls
- **Graph Complexity**: Complex graphs may affect performance.
- **Alignment Quality**: Depends on input alignment quality.
- **Memory Usage**: Large graphs require significant memory.
- **Format Compatibility**: Requires correct GFA format.
- **Result Validation**: Results should be validated.

## Examples
### Inject alignment
**Args:** `gfainject -i graph.gfa -a alignment.sam -o injected.gfa`
**Explanation:** Injects SAM alignment into pangenome graph.

### With BAM input
**Args:** `gfainject -i graph.gfa -b alignment.bam -o injected.gfa`
**Explanation:** Injects BAM alignment into graph.

### Batch processing
**Args:** `gfainject -i graph.gfa -l alignments.txt -o ./results/`
**Explanation:** Processes multiple alignment files.

### Generate report
**Args:** `gfainject -i graph.gfa -a alignment.sam -r -o report.html`
**Explanation:** Generates injection report.

### Validate output
**Args:** `gfainject -i graph.gfa -a alignment.sam -v -o injected.gfa`
**Explanation:** Validates output graph.