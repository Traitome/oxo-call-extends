---
name: tb-profiler
category: utility
description: Profiling tool for Mycobacterium tuberculosis to detect drug resistance and lineage from sequencing data
tags: [tb-profiler, utility]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/TBProfiler"
---

## Concepts

- **Tool Overview**: tb-profiler (v6.7.0) - Profiling tool for Mycobacterium tuberculosis to detect drug resistance and lineage from sequencing data
- **Core Function**: Profiling tool for Mycobacterium tuberculosis to detect drug resistance and lineage from sequencing data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tb-profiler`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tb-profiler -i <input_file> -o <output_file>`
**Explanation:** Run tb-profiler with typical input and output options.
