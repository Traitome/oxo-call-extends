---
name: msisensor
category: variant-calling
description: MSIsensor is a C++ program to detect replication slippage variants at microsatellite regions, and differentiate them as somatic or germline.
tags: [msisensor, variant-calling]
author: oxo-call-community
source_url: "https://github.com/ding-lab/msisensor"
---

## Concepts

- **Tool Overview**: msisensor v0.5 - MSIsensor is a C++ program to detect replication slippage variants at microsatellite regions, and differentiate them as somatic or germline..
- **Core Function**: MSIsensor is a C++ program to detect replication slippage variants at microsatellite regions, and differentiate them as somatic or germline.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda msisensor`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Detect MSI
**Args:** `msisensor scan -d reference.fa -b normal.bam -t tumor.bam -o output`
**Explanation:** Detects microsatellite instability from paired tumor-normal BAMs.

