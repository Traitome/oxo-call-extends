---
name: shasta
category: assembly
description: shasta - De novo assembly from Oxford Nanopore reads
tags: ["shasta", "assembly", "de-novo", "Nanopore"]
author: oxo-call-community
source_url: "https://paoloshasta.github.io/shasta/"
---

## Concepts

- **Tool Overview**: shasta (v0.14.0) performs de novo assembly from Oxford Nanopore reads.
- **Core Function**: Assembles long-read sequencing data into contigs.
- **Algorithm**: Uses hierarchical assembly approach optimized for long reads.
- **Input/Output**: Accepts FASTQ reads and produces assembled contigs.
- **Long-Read Assembly**: Focuses on Oxford Nanopore data assembly.
- **Applications**: Genome assembly, metagenomics, and long-read sequencing analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Assemble reads
**Args:** `shasta --input reads.fastq --output assembly/`
**Explanation:** `--input` input reads; `--output` output directory.

### With threads
**Args:** `shasta --input reads.fastq --output assembly/ --threads 8`
**Explanation:** `--threads 8` uses 8 threads.

### Preset mode
**Args:** `shasta --input reads.fastq --output assembly/ --preset nanopore`
**Explanation:** `--preset nanopore` uses Nanopore-optimized settings.

### Verbose logging
**Args:** `shasta --input reads.fastq --output assembly/ --verbose`
**Explanation:** `--verbose` enables verbose output.

### Help command
**Args:** `shasta --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shasta --version`
**Explanation:** Shows current version.

### Assembly graph
**Args:** `shasta --input reads.fastq --output assembly/ --writeGfa1`
**Explanation:** `--writeGfa1` outputs assembly graph in GFA format.