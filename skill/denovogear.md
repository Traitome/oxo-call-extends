---
name: denovogear
category: variant-calling
description: Tool for detecting de novo mutations from parent-offspring trios.
tags: [denovogear, variant-calling, de-novo, mutation, trio]
author: oxo-call-community
source_url: "https://github.com/denovogear/denovogear"
---

## Concepts

- **Tool Overview**: denovogear v1.1.1 - Tool for calling de novo mutations from parent-offspring trio sequencing data.
- **Core Function**: Detects new mutations present in offspring but absent in both parents using a probabilistic model.
- **Input/Output**: Expects BAM/VCF files from trio members; outputs de novo variant calls.
- **Installation**: `conda install -c bioconda denovogear`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly aligned BAM files for all three trio members.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `denovogear dnm --ped trio.ped --mom mom.bam --dad dad.bam --child child.bam --ref ref.fa --output denovo.vcf`
**Explanation:** Detects de novo mutations from trio sequencing data.
