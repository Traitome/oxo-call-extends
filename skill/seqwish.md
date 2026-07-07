---
name: seqwish
category: alignment
description: seqwish - Alignment to variation graph inducer
tags: ["seqwish", "alignment", "variation-graph", "pangenome"]
author: oxo-call-community
source_url: "https://github.com/ekg/seqwish"
---

## Concepts

- **Tool Overview**: seqwish (v0.7.11) converts alignments to variation graphs.
- **Core Function**: Builds variation graphs from sequence alignments.
- **Algorithm**: Uses alignment information to construct graph representations.
- **Input/Output**: Accepts alignments and produces variation graphs.
- **Variation Graphs**: Focuses on pangenome graph construction.
- **Applications**: Pangenomics, population genomics, and variant analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on alignment quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Build graph
**Args:** `seqwish -i alignments.paf -s sequences.fasta -o graph.gfa`
**Explanation:** `-i` PAF alignments; `-s` sequences; `-o` output graph.

### Index graph
**Args:** `seqwish index -g graph.gfa`
**Explanation:** Creates index for graph.

### Compress graph
**Args:** `seqwish compress -g graph.gfa -o graph.cgfa`
**Explanation:** Compresses graph file.

### Verbose logging
**Args:** `seqwish -v -i alignments.paf -s sequences.fasta -o graph.gfa`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqwish --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqwish --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `seqwish -t 8 -i alignments.paf -s sequences.fasta -o graph.gfa`
**Explanation:** `-t 8` uses 8 threads.