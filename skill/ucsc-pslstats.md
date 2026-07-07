---
name: ucsc-pslstats
category: utility
description: UCSC pslStats - Tool for generating PSL statistics.
tags: [ucsc-pslstats, ucsc, psl, statistics, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslStats - A tool for generating PSL alignment statistics.
- **Core Function**: Computes statistical metrics from PSL alignments.
- **Input**: PSL file.
- **Output**: Statistics report.
- **Installation**: Part of UCSC utilities
- **Use Case**: Quality control, alignment analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Generate PSL statistics
**Args:** `pslStats input.psl > stats.txt`
**Explanation:** Generate alignment statistics.

### With options
**Args:** `pslStats -verbose input.psl > stats.txt`
**Explanation:** Detailed statistics report.
