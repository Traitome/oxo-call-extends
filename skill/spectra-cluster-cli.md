---
name: spectra-cluster-cli
category: hpc
description: This is a stand-alone implementation of the new updated PRIDE Cluster algorithm. It is based on the spectra-cluster API and uses a highly similar logic as the Hadoop implementation spectra-cluster-hadoop used to build the PRIDE Cluster resource.
tags: [spectra-cluster-cli, hpc]
author: oxo-call-community
source_url: "https://github.com/spectra-cluster/spectra-cluster-cli"
---

## Concepts

- **Tool Overview**: spectra-cluster-cli (v1.1.2) - This is a stand-alone implementation of the new updated PRIDE Cluster algorithm. It is based on the spectra-cluster API and uses a highly similar logic as the Hadoop implementation spectra-cluster-hadoop used to build the PRIDE Cluster resource.
- **Core Function**: This is a stand-alone implementation of the new updated PRIDE Cluster algorithm. It is based on the spectra-cluster API and uses a highly similar logic as the Hadoop implementation spectra-cluster-hadoop used to build the PRIDE Cluster resource.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spectra-cluster-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spectra-cluster-cli -i <input_file> -o <output_file>`
**Explanation:** Run spectra-cluster-cli with typical input and output options.
