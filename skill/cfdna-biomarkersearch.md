---
name: cfdna-biomarkersearch
category: alignment
description: Pipeline to identify candidate cfDNA biomarker sequences from WGS data
tags: [cfdna-biomarkersearch, alignment, FASTA, FASTQ, SAM]
author: oxo-call-community
source_url: "https://github.com/avo-hcemm/cfDNA-biomarkers-pipeline/blob/master/README.md"
---

## Concepts

- **Tool Overview**: cfdna-biomarkersearch (v0.1.3) - Pipeline to identify candidate cfDNA biomarker sequences from WGS data
- **Core Function**: cfDNA-BiomarkerDiscovery is a pipeline designed to identify candidate biomarker sequences from cell-free DNA (cfDNA) derived from blood samples. The pipeline takes as input: •	An archive of FASTQ file...
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda cfdna-biomarkersearch`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
