---
name: biolite-tools
category: workflow
description: C++ tools for biolite framework providing high-performance bioinformatics utilities
tags: [workflow, provenance, diagnostics, c++, performance]
author: oxo-call-community
source_url: "https://bitbucket.org/caseywdunn/biolite"
---

## Concepts

- **Tool Overview**: biolite-tools provides C++ implementations of high-performance bioinformatics tools for the BioLite framework, designed for Next-Generation Sequencing (NGS) data processing.
- **Performance**: C++ implementation for high-speed processing of large NGS datasets.
- **Complementary Tools**: Works alongside the biolite Python framework, providing low-level utilities.
- **UNIX Design Pattern**: Follows standard UNIX "pipe and filter" design pattern for composability.
- **Optional Dependency**: Required only for pipelines that call C++ tools through wrappers.

## Pitfalls

- **Dependency**: Requires biolite Python package for full functionality.
- **Version Compatibility**: Should match biolite Python package version.
- **Specialized Use**: Primarily designed for use within BioLite pipelines.

## Examples

### Install biolite-tools
**Args:** `conda install -c bioconda biolite-tools`
**Explanation:** Installs the C++ tools for biolite.

### Filter Illumina reads
**Args:** `bl-filter-illumina -i reads.fq -o filtered.fq --quality 20`
**Explanation:** Filters low-quality Illumina sequencing reads.

### ExaML bootstraps
**Args:** `bl-examl-bootstraps -t tree.nwk -a alignment.phylip -o bootstraps/`
**Explanation:** Automates ExaML bootstrap runs for phylogenetic analysis.

### SRA export
**Args:** `bl-sra-export -i samples.txt -o sra_data/`
**Explanation:** Exports SRA data with support for 454 sequencing data.