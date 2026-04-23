---
name: jaffa
category: expression
description: JAFFA is a multi-step pipeline that takes either raw RNA-Seq reads, or pre-assembled transcripts then searches for gene fusions.  This package contains the wrappers jaffa-direct, jaffa-assembly, and jaffa-hybrid. You can pass the "refSeq" parameter in the environment variables JAFFA_REF_BASE. Otherwise, pass any paramters to the wrappers as you would to the bpipe JAFFA_{method} call in the manual.
tags: [jaffa, expression]
author: oxo-call-community
source_url: "https://github.com/Oshlack/JAFFA"
---

## Concepts

- **Tool Overview**: jaffa (v2.5) - JAFFA is a multi-step pipeline that takes either raw RNA-Seq reads, or pre-assembled transcripts then searches for gene fusions.  This package contains the wrappers jaffa-direct, jaffa-assembly, and jaffa-hybrid. You can pass the "refSeq" parameter in the environment variables JAFFA_REF_BASE. Otherwise, pass any paramters to the wrappers as you would to the bpipe JAFFA_{method} call in the manual.
- **Core Function**: Provides functionality for expression tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda jaffa`

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
