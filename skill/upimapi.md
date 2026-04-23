---
name: upimapi
category: alignment
description: UniProt Id Mapping through API
tags: [upimapi, alignment]
author: oxo-call-community
source_url: "https://github.com/iquasere/UPIMAPI/blob/master/README.md"
---

## Concepts

- **Tool Overview**: upimapi (v1.13.3) - UPIMAPI takes as input either a list of UniProt IDs or a blast file from annotation using UniProt database as reference and uses UniProt's API to retrieve information relative to those IDs. It is essentially a command line implementation of UniProt's ID mapping web service available at https://www.uniprot.org/uploadlists/, allowing for retrieval of information from thousands of IDs in one go, while still relying on the web service.
- **Core Function**: UniProt Id Mapping through API
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda upimapi`

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
