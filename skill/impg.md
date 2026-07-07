---
name: impg
category: pangenomics
description: Implicit pangenome graphs construction and manipulation toolkit
tags: [impg, pangenome, graph-genomics, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/pangenome/impg"
---

## Concepts

- **Tool Overview**: impg (v0.3.3) is a toolkit for constructing and manipulating implicit pangenome graphs, representing genetic variation across multiple genomes efficiently.
- **Core Function**: Builds compressed pangenome graphs that implicitly represent all sequences, enabling efficient querying and analysis of population-scale genomic data.
- **Input/Output**: Accepts FASTA sequences, VCF files, and multiple sequence alignments. Outputs graph structures in various pangenome formats.
- **Graph Representation**: Uses implicit graph representation to minimize memory usage while maintaining full sequence information.
- **Scalability**: Designed to handle large pangenome datasets with thousands of genomes efficiently.

## Pitfalls

- **Memory Management**: Large pangenome datasets may require careful memory management; consider using graph partitioning.
- **Format Compatibility**: Ensure input files are in compatible formats (FASTA, VCF, or MSA).
- **Reference Selection**: Choice of reference genome can impact graph construction and downstream analysis.
- **Variant Representation**: Complex structural variants may require specialized handling during graph construction.
- **Computational Resources**: Graph construction for large datasets can be computationally intensive.

## Examples

### Build pangenome graph from FASTA files
**Args:** `impg build -i genomes/*.fasta -o pangenome.impg`
**Explanation:** Constructs an implicit pangenome graph from multiple FASTA files.

### Build graph from VCF and reference
**Args:** `impg build -r reference.fasta -v variants.vcf -o pangenome.impg`
**Explanation:** Builds pangenome graph using a reference genome and variant calls.

### Query sequence in pangenome
**Args:** `impg query -g pangenome.impg -q query_sequence.fasta -o matches.tsv`
**Explanation:** Queries a sequence against the pangenome graph and returns matches.

### Extract subgraph
**Args:** `impg extract -g pangenome.impg -r chr1:1-100000 -o region.impg`
**Explanation:** Extracts a specific genomic region from the pangenome graph.

### Convert to GFA format
**Args:** `impg convert -g pangenome.impg -f gfa -o pangenome.gfa`
**Explanation:** Converts implicit graph to GFA (Graphical Fragment Assembly) format for visualization.

### Statistics and validation
**Args:** `impg stats -g pangenome.impg -o statistics.json`
**Explanation:** Generates comprehensive statistics about the pangenome graph structure.