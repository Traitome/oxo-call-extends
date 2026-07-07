---
name: vartracker
category: bioinformatics
description: VarTracker - Variant tracking tool.
tags: [vartracker, variant-tracking, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vartracker/"
---

## Concepts

- **Tool Overview**: VarTracker - A tool for tracking variant frequencies over time.
- **Core Function**: Tracks variant frequencies across samples or time points.
- **Input**: Multiple VCF files.
- **Output**: Frequency tracking results.
- **Installation**: Install via pip or conda
- **Use Case**: Variant monitoring, population genetics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Time**: May be slow for many samples.

## Examples

### Track variants
**Args:** `vartracker -i samples/ -o tracking.txt`
**Explanation:** Track variants across samples.

### With options
**Args:** `vartracker -i samples/ -o tracking.txt -t 8`
**Explanation:** Use 8 threads.
