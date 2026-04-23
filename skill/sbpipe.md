---
name: sbpipe
category: formatting
description: SBpipe is a collection of pipelines for systems modelling of biological networks. It allows mathematical modellers to automatically repeat the tasks of model simulation and parameter estimation, and extract robustness information from these repeat sequences in a solid and consistent manner, facilitating model development and analysis. SBpipe can run models implemented in COPASI, Python or coded in any other programming language using Python as a wrapper module. Pipelines can run on multicore computers, Sun Grid Engine (SGE), Load Sharing Facility (LSF) clusters, or via Snakemake.
tags: ["sbpipe", "formatting"]
author: oxo-call-community
source_url: "http://sbpipe.readthedocs.io"
---

## Concepts

- **Tool Overview**: SBpipe is a collection of pipelines for systems modelling of biological networks. It allows mathematical modellers to automatically repeat the tasks of model simulation and parameter estimation, and extract robustness information from these repeat sequences in a solid and consistent manner, facilitating model development and analysis. SBpipe can run models implemented in COPASI, Python or coded in any other programming language using Python as a wrapper module. Pipelines can run on multicore computers, Sun Grid Engine (SGE), Load Sharing Facility (LSF) clusters, or via Snakemake. (version 4.21.0)
- **Core Function**: Processes bioinformatics data related to formatting
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sbpipe`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Convert format
**Args:** `-i input.file -o output.file`
**Explanation:** Converts between file formats.

