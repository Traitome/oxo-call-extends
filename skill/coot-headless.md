---
name: coot-headless
category: programming
description: Coot Headless API - Software for macromolecular model building.
tags: [coot-headless, programming]
author: oxo-call-community
source_url: "https://www.mrc-lmb.cam.ac.uk/lucrezia/libcootapi-documentation/index.html"
---

## Concepts

- **Tool Overview**: coot-headless (v1.2) - Coot Headless API - Software for macromolecular model building.
- **Core Function**: Coot is a macromolecular model building, model completion and validation application. This package provides the headless APIs (Chapi python bindings and libcootapi C++ library) without GUI dependencie...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda coot-headless`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `--input input_file --output output_file`
**Explanation:** Process input and generate output
