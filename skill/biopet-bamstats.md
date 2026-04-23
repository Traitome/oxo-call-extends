---
name: biopet-bamstats
category: qc
description: Generate statistics from BAM files
tags: [bam, statistics, quality-control, alignment]
author: oxo-call-community
source_url: "https://github.com/biopet/bamstats"
---

## Concepts
- **Tool Overview**: BamStats generates comprehensive statistics from BAM files including clipping stats, flag stats, insert size, and mapping quality.
- **Output Format**: JSON output organized by sample → library → readgroup hierarchy.
- **Statistics**: Clipping rates, flag distributions, insert size distributions, mapping quality distributions.
- **Applications**: BAM quality control, alignment validation, sequencing quality assessment.

## Pitfalls
- **Readgroup Requirements**: BAM files must have readgroups annotated with sample (SM) and library (LB) tags.
- **Large Files**: Processing large BAM files can be time-consuming.

## Examples
### Generate BAM statistics
**Args:** `java -jar BamStats.jar -I input.bam -o stats.json`
**Explanation:** Generates comprehensive statistics from BAM file.

### Output TSV format
**Args:** `java -jar BamStats.jar -I input.bam -o stats.json --tsvOutput`
**Explanation:** Outputs statistics in both JSON and TSV formats.
