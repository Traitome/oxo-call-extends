---
name: manta
category: variant-calling
description: Structural variant and indel caller for mapped sequencing data
tags: [manta, variant-calling]
author: oxo-call-community
source_url: "https://github.com/Illumina/manta"
---

## Concepts

- **Tool Overview**: manta v1.6.0 - Structural variant and indel caller for mapped sequencing data.
- **Core Function**: Structural variant and indel caller for mapped sequencing data
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda manta`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Call SVs
**Args:** `configManta.py --bam input.bam --referenceFasta ref.fa --runDir manta_run`
**Explanation:** Configures Manta SV calling workflow.

