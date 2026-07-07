---
name: mbg
category: assembly
description: Minimizer-based sparse de Bruijn graph constructor for sequence assembly.
tags: [mbg, de-bruijn-graph, sequence-assembly]
author: oxo-call-community
source_url: "https://github.com/maickrau/MBG"
---

## Concepts

- **Tool Overview**: MBG constructs sparse de Bruijn graphs using minimizers.
- **Core Function**: Builds efficient de Bruijn graphs for assembly.
- **Minimizer Sampling**: Uses minimizers to reduce graph size.
- **Sparse Graph**: Constructs memory-efficient sparse graphs.
- **Input/Output**: Accepts FASTA sequences, produces graph structures.
- **Installation**: `conda install -c bioconda mbg`

## Pitfalls

- **k-mer Selection**: k-mer size significantly affects results.
- **Memory Requirements**: Still requires significant memory for large datasets.
- **Parameter Tuning**: Minimizer parameters require careful adjustment.
- **Sequence Quality**: Low-quality sequences affect graph quality.
- **Output Format**: Graph format may need conversion for downstream tools.
- **Complexity**: Graph construction can be computationally intensive.

## Examples

### Build de Bruijn graph
**Args:** `mbg -i reads.fastq -o graph.gfa`
**Explanation:** Constructs de Bruijn graph from reads.

### Set k-mer size
**Args:** `mbg -i reads.fastq -k 31 -o graph.gfa`
**Explanation:** Uses k-mer size of 31.

### With minimizer window
**Args:** `mbg -i reads.fastq -w 100 -o graph.gfa`
**Explanation:** Sets minimizer window size to 100.

### Verbose output
**Args:** `mbg -i reads.fastq -v -o graph.gfa`
**Explanation:** Shows detailed progress information.

### Help documentation
**Args:** `mbg --help`
**Explanation:** Displays available commands and options.
