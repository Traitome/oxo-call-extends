---
name: czlab_perl_lib
category: formatting
description: mCross Perl script
tags: [czlab_perl_lib, formatting]
author: oxo-call-community
source_url: "https://github.com/huijfeng/czlab_perl_lib"
---

## Concepts

- **Tool Overview**: czlab_perl_lib (v1.0.1) - mCross Perl script
- **Core Function**: czlab_per_lib is the core CLI and perl library used in mCross, which is a bioinformatic tool to identify RNA-protein cross-link sites. See details of the methods in Feng et al. (2019), Modeling the in...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda czlab_perl_lib`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.gff -o output.gtf`
**Explanation:** Convert between file formats
