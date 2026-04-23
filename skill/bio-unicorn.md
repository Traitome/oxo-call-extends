---
name: bio-unicorn
category: qc
description: Compute statistics on short read alignments
tags: [alignment, statistics, quality-control, bam]
author: oxo-call-community
source_url: "https://github.com/GeoGenetics/unicorn"
---

## Concepts
- **Tool Overview**: unicorn computes statistics on short read alignments in BAM format. It provides comprehensive alignment quality metrics.
- **Alignment Metrics**: Reports mapping quality distribution, coverage statistics, insert size, and other alignment properties.
- **Applications**: Quality control of sequencing data, alignment validation, downstream analysis preparation.

## Pitfalls
- **BAM Input**: Requires indexed BAM file as input.
- **Reference Dependency**: Some statistics require reference genome information.

## Examples
### Compute alignment statistics
**Args:** `unicorn -i aligned.bam -o stats.tsv`
**Explanation:** Computes comprehensive alignment statistics from BAM file.

### Generate coverage report
**Args:** `unicorn -i aligned.bam --coverage --output coverage.tsv`
**Explanation:** Reports coverage depth distribution across the genome.
