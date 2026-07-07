---
name: megadepth
category: alignment
description: Efficient coverage extraction from BAM and BigWig files for sequencing data analysis.
tags: [megadepth, coverage-analysis, sequencing]
author: oxo-call-community
source_url: "https://github.com/ChristopherWilks/megadepth"
---

## Concepts

- **Tool Overview**: Megadepth extracts coverage information from sequencing files.
- **Core Function**: Efficiently computes coverage from BAM/BigWig files.
- **Coverage Calculation**: Computes read coverage across regions.
- **BigWig Support**: Directly reads and writes BigWig files.
- **Region Summary**: Provides coverage summaries over intervals.
- **Installation**: `conda install -c bioconda megadepth`

## Pitfalls

- **File Size**: Large BAM files require memory.
- **Index Requirements**: BAM files must be indexed.
- **Computation Time**: Slow for very large datasets.
- **Output Size**: Coverage files can be large.
- **Parameter Tuning**: Requires careful bin size selection.
- **Format Compatibility**: Limited to BAM and BigWig formats.

## Examples

### Compute coverage
**Args:** `megadepth aligned.bam -o coverage.bw`
**Explanation:** Computes coverage and outputs BigWig.

### Region coverage
**Args:** `megadepth aligned.bam --regions regions.bed -o coverage.txt`
**Explanation:** Gets coverage for specific regions.

### TSV output
**Args:** `megadepth aligned.bam --tsv -o coverage.tsv`
**Explanation:** Outputs coverage in TSV format.

### Whole genome coverage
**Args:** `megadepth aligned.bam --whole-genome -o wg_coverage.bw`
**Explanation:** Computes whole-genome coverage.

### Help documentation
**Args:** `megadepth --help`
**Explanation:** Displays available options.
