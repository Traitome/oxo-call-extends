---
name: ggcat
category: graph-analysis
description: ggcat - Compacted and colored de Bruijn graph construction and querying.
tags: [ggcat, graph-analysis, de-bruijn-graph, k-mer]
author: oxo-call-community
source_url: "https://github.com/algbio/ggcat/blob/v2.0.0/README.md"
---

## Concepts
- **de Bruijn Graphs**: Constructs compacted de Bruijn graphs.
- **Colored Graphs**: Uses colored graph representation.
- **k-mer Analysis**: Analyzes k-mer content.
- **Graph Querying**: Queries graph for sequences.
- **Efficient Storage**: Uses compacted representation.

## Pitfalls
- **Graph Construction**: Requires significant computation.
- **Memory Usage**: Large datasets require memory.
- **K-mer Selection**: K-mer size affects results.
- **Query Complexity**: Complex queries may be slow.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Build graph
**Args:** `ggcat build -i reads.fastq -o graph.ggcat`
**Explanation:** Builds de Bruijn graph.

### Query graph
**Args:** `ggcat query -i graph.ggcat -s sequence -o matches.txt`
**Explanation:** Queries graph for sequences.

### With k-mer size
**Args:** `ggcat build -i reads.fastq -k 31 -o graph.ggcat`
**Explanation:** Uses specified k-mer size.

### Export graph
**Args:** `ggcat export -i graph.ggcat -o graph.gfa`
**Explanation:** Exports graph to GFA format.

### Batch processing
**Args:** `ggcat build -l samples.txt -o ./graphs/`
**Explanation:** Builds graphs for multiple samples.