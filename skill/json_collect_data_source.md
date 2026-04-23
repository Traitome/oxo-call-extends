---
name: json_collect_data_source
category: utility
description: This tool is able to receive multiple datasets (optionally with their metadata) in a single query. As an extension of the galaxy-json-data-source tool (https://github.com/mdshw5/galaxy-json-data-source), it allows to handle archives (gz, bz2, tar, and zip) organizing their content in a collection.
tags: [json_collect_data_source, utility, JSON]
author: oxo-call-community
source_url: "https://github.com/fabio-cumbo/galaxy-json-collect-data-source"
---

## Concepts

- **Tool Overview**: json_collect_data_source (v1.0.1) - This tool is able to receive multiple datasets (optionally with their metadata) in a single query. As an extension of the galaxy-json-data-source tool (https://github.com/mdshw5/galaxy-json-data-source), it allows to handle archives (gz, bz2, tar, and zip) organizing their content in a collection.
- **Core Function**: Provides functionality for utility tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda json_collect_data_source`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
