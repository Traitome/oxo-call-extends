---
name: twopaco
category: assembly
description: TwoPaCo - Tool for constructing de Bruijn graphs from sequencing data.
tags: [twopaco, de-bruijn-graph, genome-assembly, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/medvedevgroup/TwoPaCo"
---

## Concepts

- **Tool Overview**: TwoPaCo - A tool for efficiently constructing de Bruijn graphs from sequencing reads.
- **Core Function**: Builds de Bruijn graphs for genome assembly and sequence analysis.
- **Input**: Sequencing reads (FASTQ), k-mer size.
- **Output**: De Bruijn graph, assembly graphs, k-mer statistics.
- **Installation**: `conda install -c bioconda twopaco`
- **Use Case**: Genome assembly, sequence analysis, k-mer counting.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **k-mer Selection**: Requires appropriate k-mer size selection.

## Examples

### Build de Bruijn graph
**Args:** `twopaco -k 31 -i reads.fastq -o graph`
**Explanation:** Build de Bruijn graph with k-mer size 31.

### With multiple files
**Args:** `twopaco -k 25 -i reads_1.fastq -i reads_2.fastq -o graph`
**Explanation:** Build graph from multiple read files.
