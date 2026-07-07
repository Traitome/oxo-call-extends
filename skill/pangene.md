---
name: pangene
category: utility
description: Pangene constructs a pangenome gene graph from multiple sequence alignments.
tags: [pangene, utility, pangenome, gene-graph]
author: oxo-call-community
source_url: "https://github.com/lh3/pangene"
---

## Concepts

- **Tool Overview**: Pangene builds pangenome gene graphs from alignments.
- **Core Function**: Constructs gene-level pangenome graphs.
- **Algorithm**: Uses graph construction from multiple sequence alignments.
- **Input Format**: Accepts multiple sequence alignments in FASTA format.
- **Output**: Produces pangenome graph in GFA format.
- **Use Case**: Pangenome analysis, gene family analysis, and comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Results depend on input alignment quality.
- **Graph Complexity**: Complex graphs may be difficult to interpret.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pangene --help`
**Explanation:** Shows available options and usage instructions.

### Build gene graph
**Args:** `pangene -i alignments.fasta -o pangenome.gfa`
**Explanation:** Constructs pangenome gene graph.

### With annotations
**Args:** `pangene -i alignments.fasta -g genes.gff -o pangenome.gfa`
**Explanation:** Incorporates gene annotations.

### Verbose mode
**Args:** `pangene -v -i alignments.fasta -o pangenome.gfa`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pangene -t 8 -i alignments.fasta -o pangenome.gfa`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pangene -i alignments.fasta -o pangenome.gfa --gfa2`
**Explanation:** Outputs in GFA2 format.

### Minimum length
**Args:** `pangene -m 100 -i alignments.fasta -o pangenome.gfa`
**Explanation:** Filters by minimum gene length.