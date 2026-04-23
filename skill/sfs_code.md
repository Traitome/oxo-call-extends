---
name: sfs_code
category: population-genomics
description: This article introduces a new forward population genetic simulation program that can efficiently generate samples from populations with complex demographic histories under various models of natural selection. The program (SFS_CODE) is highly flexible, allowing the user to simulate realistic genomic regions with several loci evolving according to a variety of mutation models (from simple to context-dependent), and allows for insertions and deletions. Each locus can be annotated as either coding or non-coding, sex-linked or autosomal, selected or neutral, and have an arbitrary linkage structure (from completely linked to independent). © The Author 2008. Published by Oxford University Press. All rights reserved.
tags: [sfs_code, population-genomics, sam]
author: oxo-call-community
source_url: "http://sfscode.sourceforge.net/SFS_CODE/index/index.html"
---

## Concepts

- **Tool Overview**: sfs_code (v20150910) - This article introduces a new forward population genetic simulation program that can efficiently generate samples from populations with complex demographic histories under various models of natural selection. The program (SFS_CODE) is highly flexible, allowing the user to simulate realistic genomic regions with several loci evolving according to a variety of mutation models (from simple to context-dependent), and allows for insertions and deletions. Each locus can be annotated as either coding or non-coding, sex-linked or autosomal, selected or neutral, and have an arbitrary linkage structure (from completely linked to independent). © The Author 2008. Published by Oxford University Press. All rights reserved.
- **Core Function**: This article introduces a new forward population genetic simulation program that can efficiently generate samples from populations with complex demographic histories under various models of natural selection. The program (SFS_CODE) is highly flexible, allowing the user to simulate realistic genomic regions with several loci evolving according to a variety of mutation models (from simple to context-dependent), and allows for insertions and deletions. Each locus can be annotated as either coding or non-coding, sex-linked or autosomal, selected or neutral, and have an arbitrary linkage structure (from completely linked to independent). © The Author 2008. Published by Oxford University Press. All rights reserved.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sfs_code`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sfs_code -i <input.vcf> -o <output_dir>`
**Explanation:** Run sfs_code with typical input and output options.
