---
name: wgdi
category: bioinformatics
description: WGDI - Whole-genome duplication inference.
tags: [wgdi, comparative-genomics, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/SunPengChuan/wgdi"
---

## Concepts

- **Tool Overview**: WGDI - Whole-genome duplication inference tool.
- **Core Function**: Identifies whole-genome duplication events.
- **Input**: Genome sequences.
- **Output**: Duplication analysis.
- **Installation**: Install via pip
- **Use Case**: Comparative genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Analyze WGD
**Args:** `wgdi -i config.yaml`
**Explanation:** Run WGD analysis.

### With options
**Args:** `wgdi -i config.yaml -t 8`
**Explanation:** Use 8 threads.
