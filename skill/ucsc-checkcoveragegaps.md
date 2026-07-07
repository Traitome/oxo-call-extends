---
name: ucsc-checkcoveragegaps
category: utility
description: UCSC checkCoverageGaps - Tool for checking coverage gaps.
tags: [ucsc-checkcoveragegaps, ucsc, quality-control, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC checkCoverageGaps - A tool for identifying coverage gaps in sequencing data.
- **Core Function**: Detects regions with insufficient sequencing coverage.
- **Input**: BED file, coverage data.
- **Output**: Gap regions in BED format.
- **Installation**: Part of UCSC utilities
- **Use Case**: Quality control, coverage analysis, genome assembly.

## Pitfalls

- **Coverage Threshold**: Requires appropriate threshold setting.
- **Memory**: May require significant memory for large datasets.

## Examples

### Check coverage gaps
**Args:** `checkCoverageGaps -i coverage.bw -threshold=10 > gaps.bed`
**Explanation:** Identify regions with coverage below threshold.

### With regions
**Args:** `checkCoverageGaps -i coverage.bw -regions=targets.bed > gaps.bed`
**Explanation:** Check gaps in specified regions.
