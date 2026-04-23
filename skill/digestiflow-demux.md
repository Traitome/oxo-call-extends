---
name: digestiflow-demux
category: utility
description: Demultiplexing module for Digestiflow workflow.
tags: [digestiflow-demux, utility, demultiplexing, workflow]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: digestiflow-demux - Demultiplexing component of the Digestiflow workflow system.
- **Core Function**: Demultiplexes sequencing data as part of the Digestiflow processing pipeline.
- **Input/Output**: Expects raw sequencing files; outputs demultiplexed reads per sample.
- **Installation**: `conda install -c bioconda digestiflow-demux`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires raw sequencing data with sample barcodes.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `digestiflow-demux --input raw_data/ --output demux/`
**Explanation:** Demultiplexes sequencing data in Digestiflow workflow.
