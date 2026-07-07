---
name: ddrage
category: formatting
description: Simulator for ddRADseq datasets that generates realistic reads with ground truth.
tags: [ddrage, formatting, ddRADseq, simulation, RAD-seq]
author: oxo-call-community
source_url: "https://bitbucket.org/genomeinformatics/rage"
---

## Concepts

- **Tool Overview**: ddrage (v1.8.1+) is a simulator for double digest RAD-seq (ddRADseq) datasets. It generates realistic FASTQ reads along with ground truth information for benchmarking and validation of RAD-seq analysis pipelines.
- **Core Function**: Simulates ddRADseq sequencing reads from a reference genome, including realistic error profiles, size selection, and digestion patterns, with known ground truth for validation.
- **Input/Output**: Input: Reference genome (FASTA), digestion enzymes, simulation parameters. Output: Simulated FASTQ reads, ground truth YAML file, loci information.
- **Algorithm**: Simulates restriction enzyme digestion, size selection, read generation with error models, and sampling to create realistic ddRADseq data.
- **Key Features**: Realistic error modeling, multiple enzyme support, size selection simulation, ground truth generation, population simulation.
- **Installation**: `conda install -c bioconda ddrage`

## Pitfalls

- **Enzyme Specification**: Requires correct restriction enzyme recognition sequences.
- **Size Selection**: Size selection parameters must match experimental protocol.
- **Error Model**: Error model may not match all sequencing platforms.
- **Computational Requirements**: Large genomes require significant memory.
- **Population Simulation**: Population-level simulations require additional parameters.

## Examples

### Basic ddRADseq simulation
**Args:** `ddrage -r reference.fasta -e1 EcoRI -e2 MspI -o simulated/`
**Explanation:** Simulate ddRADseq reads using EcoRI and MspI enzymes.

### Specify size selection range
**Args:** `ddrage -r reference.fasta -e1 EcoRI -e2 MspI --min-size 300 --max-size 500 -o simulated/`
**Explanation:** Simulate with size selection between 300-500 bp.

### Simulate with coverage
**Args:** `ddrage -r reference.fasta -e1 EcoRI -e2 MspI --coverage 20x -o simulated/`
**Explanation:** Simulate ddRADseq data with 20x coverage.