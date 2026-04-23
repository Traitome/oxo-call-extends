---
name: binlorry
category: qc
description: BinLorry - Flexible tool for binning and filtering sequencing reads
tags: [read-binning, read-filtering, quality-control]
author: oxo-call-community
source_url: "https://github.com/rambaut/binlorry"
---

## Concepts
- **Tool Overview**: BinLorry is a flexible tool for binning and filtering sequencing reads based on various criteria including quality, length, and barcode.
- **Read Binning**: Separates reads into bins based on user-defined criteria.
- **Filtering**: Filters reads by quality scores, read length, or other properties.
- **Applications**: Preprocessing for downstream analysis, barcode demultiplexing, quality-based read separation.

## Pitfalls
- **Filter Criteria**: Choice of filtering thresholds affects downstream analysis sensitivity.
- **Read Loss**: Aggressive filtering may remove valid reads.

## Examples
### Filter reads by quality
**Args:** `binlorry --input reads.fq --min-quality 20 --output filtered.fq`
**Explanation:** Filters reads with minimum average quality score of 20.

### Bin reads by length
**Args:** `binlorry --input reads.fq --bin-lengths 100,200,500 --output-dir binned/`
**Explanation:** Separates reads into bins based on length thresholds.
