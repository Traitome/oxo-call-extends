---
name: datma
category: assembly
description: DATMA - Distributed Automatic Metagenomic Assembly and Annotation framework
tags: [datma, assembly, metagenomics, distributed-computing, annotation]
author: oxo-call-community
source_url: "https://github.com/andvides/DATMA"
---

## Concepts

- **Tool Overview**: datma (v2.0+) is a distributed automatic metagenomic assembly and annotation framework.
- **Core Function**: Performs metagenomic assembly and annotation using distributed computing resources.
- **Input/Output**: Input: Metagenomic sequencing reads. Output: Assembled contigs, annotations.
- **Algorithm**: Integrates multiple assembly tools with distributed processing for scalability.
- **Key Features**: Distributed processing, automated pipeline, integrated annotation.
- **Installation**: `conda install -c bioconda datma`

## Pitfalls

- **Cluster Requirements**: Requires distributed computing environment.
- **Resource Management**: Proper cluster configuration required for optimal performance.
- **Input Quality**: Results depend on input sequencing data quality.
- **Memory Requirements**: Large datasets may require significant memory across nodes.
- **Network Performance**: Distributed processing depends on network speed.

## Examples

### Run metagenomic assembly
**Args:** `datma assemble -i reads.fastq -o assembly/ -n 8`
**Explanation:** Run distributed metagenomic assembly with 8 nodes.

### Run annotation
**Args:** `datma annotate -i contigs.fasta -o annotations/`
**Explanation:** Annotate assembled contigs with functional annotations.

### Complete pipeline
**Args:** `datma pipeline -i reads.fastq -o results/ --nodes 16`
**Explanation:** Run complete assembly and annotation pipeline with 16 nodes.
