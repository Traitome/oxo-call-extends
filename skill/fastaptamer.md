---
name: fastaptamer
category: formatting
description: "A Bioinformatic Toolkit for High-Throughput Sequence Analysis of Combinatorial Selections"
tags: [fastaptamer, formatting, aptamer, SELEX, bioinformatics]
author: oxo-call-community
source_url: "https://burkelab.missouri.edu/fastaptamer.html"
---

## Concepts

- **Tool Overview**: FastAptamer is a bioinformatic toolkit for high-throughput sequence analysis of combinatorial selections, primarily used for aptamer and SELEX experiments.
- **Core Function**: Processes and analyzes sequencing data from aptamer selection experiments.
- **Input/Output**: Input: FASTQ files from sequencing. Output: Sequence counts, enrichment analysis, consensus sequences.
- **Algorithm**: Implements various algorithms for sequence counting, clustering, and enrichment analysis.
- **Key Features**: High-throughput processing, sequence counting, clustering, enrichment analysis, consensus generation, batch processing.
- **Installation**: `conda install -c bioconda fastaptamer`

## Pitfalls

- **Data Quality**: Requires high-quality sequencing data.
- **Memory Usage**: Large datasets may require significant memory.
- **Sequence Diversity**: Highly diverse libraries may affect clustering.
- **Computation Time**: Large datasets may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic processing
**Args:** `fastaptamer process -i reads.fastq -o results/`
**Explanation:** Processes aptamer sequencing data.

### Sequence counting
**Args:** `fastaptamer count -i reads.fastq -o counts.txt`
**Explanation:** Counts sequence occurrences.

### Clustering
**Args:** `fastaptamer cluster -i reads.fastq -o clusters.txt`
**Explanation:** Clusters similar sequences.

### Enrichment analysis
**Args:** `fastaptamer enrich -i round3.fastq -c round1.fastq -o enrichment.txt`
**Explanation:** Analyzes enrichment between selection rounds.

### Consensus generation
**Args:** `fastaptamer consensus -i cluster.fastq -o consensus.fasta`
**Explanation:** Generates consensus sequences.