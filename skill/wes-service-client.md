---
name: wes-service-client
category: hpc
description: Implementation of the GA4GH Workflow Execution Service, a REST service for running workflows; client support only
tags: [wes-service-client, hpc]
author: oxo-call-community
source_url: "https://github.com/common-workflow-language/workflow-service"
---

## Concepts

- **Tool Overview**: wes-service-client (v2.7) - Implementation of the GA4GH Workflow Execution Service, a REST service for running workflows; client support only
- **Core Function**: Implementation of the GA4GH Workflow Execution Service, a REST service for running workflows; client support only
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda wes-service-client`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
