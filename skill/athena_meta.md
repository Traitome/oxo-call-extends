---
name: athena_meta
category: assembly
description: Athena - Read cloud assembler for metagenomes using linked-read technology
tags: [metagenomics, assembly, linked-reads, 10x-genomics]
author: oxo-call-community
source_url: "https://github.com/abishara/athena_meta"
---

## Concepts

- **Tool Overview**: Athena is a metagenome assembler designed for linked-read sequencing data (10x Genomics). It leverages barcode information to improve assembly of complex microbial communities.

- **Linked-Read Advantage**: Uses barcode information from linked-reads to associate reads from the same DNA molecule, enabling better resolution of repetitive regions and strain separation.

- **Cloud Assembly**: Implements cloudSPAdes-style assembly by solving the shortest cloud superstring problem for metagenomic samples.

- **Metagenome Focus**: Specifically designed for microbial community samples where multiple genomes are present simultaneously.

## Pitfalls

- **Linked-Read Requirement**: Requires linked-read sequencing data (10x Genomics). Cannot be used with standard Illumina paired-end data.

- **Barcode Quality**: Assembly quality depends on barcode diversity and accuracy. Poor barcode performance reduces assembly improvement.

- **Computational Resources**: Metagenome assembly is computationally intensive, requiring significant memory and CPU resources.

- **Complex Communities**: Very diverse communities with many low-abundance organisms may have incomplete assemblies.

## Examples

### Basic assembly run
**Args:** `athena-meta --config config.json`
**Explanation:** Runs Athena assembly using parameters specified in JSON configuration file. Runs until all steps complete.

### Local execution
**Args:** `athena-meta --config config.json --local`
**Explanation:** Runs assembly locally on current machine instead of distributed computing environment.

### Specify output directory
**Args:** `athena-meta --config config.json --output results/`
**Explanation:** Saves assembly results to specified output directory instead of default location.

### Container deployment
**Args:** `docker run -v /data:/data biocontainers/athena_meta:1.3--0 athena-meta --config /data/config.json`
**Explanation:** Runs Athena in Docker container for reproducible environment and easy deployment.
