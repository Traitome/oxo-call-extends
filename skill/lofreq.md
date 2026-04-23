---
name: lofreq
category: variant-calling
description: A fast and sensitive variant-caller for inferring SNVs and indels from next-generation sequencing data.
tags: [lofreq, variant-calling]
author: oxo-call-community
source_url: "https://csb5.github.io/lofreq"
---

## Concepts

- **Tool Overview**: lofreq v2.1.5 - A fast and sensitive variant-caller for inferring SNVs and indels from next-generation sequencing data..
- **Core Function**: A fast and sensitive variant-caller for inferring SNVs and indels from next-generation sequencing data.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda lofreq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Call variants
**Args:** `lofreq call-parallel --pp-threads 4 -f reference.fa -o variants.vcf input.bam`
**Explanation:** Calls low-frequency variants from BAM file.

