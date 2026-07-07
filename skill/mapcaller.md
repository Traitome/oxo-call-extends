---
name: mapcaller
category: alignment
description: "MapCaller: combined short-read mapper and variant caller"
tags: [mapcaller, alignment, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hsinnan75/MapCaller"
---
## Concepts

- **Tool Overview**: mapcaller v0.9.9.41 - An efficient and versatile approach for short-read mapping and variant identification using high-throughput sequencing data.
- **Core Function**: Combines short-read mapping and variant calling into a single integrated workflow.
- **Input/Output**: Input: FASTQ reads, reference genome; Output: BAM alignment, VCF variant calls.
- **Installation**: `conda install -c bioconda mapcaller`
- **Integrated Workflow**: Performs mapping and variant calling in a single step.
- **High Throughput**: Optimized for high-throughput sequencing data analysis.

## Pitfalls

- **Read Quality**: Poor quality reads affect mapping and variant calling accuracy.
- **Reference Genome**: Must use the same reference for mapping and variant calling.
- **Memory Usage**: Large datasets require significant memory.
- **Parameter Tuning**: Incorrect parameters affect variant detection sensitivity.
- **False Positives**: May produce false positive variant calls.
- **Complex Regions**: Difficult to map regions may have reduced sensitivity.

## Examples

### Map and call variants
**Args:** `mapcaller -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o output/`
**Explanation:** Maps reads and calls variants in a single workflow.

### Single-end mode
**Args:** `mapcaller -r ref.fa -s reads.fastq -o output/`
**Explanation:** Processes single-end reads.

### With quality filter
**Args:** `mapcaller -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o output/ -q 30`
**Explanation:** Filters reads with quality < 30.

### Verbose mode
**Args:** `mapcaller -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o output/ -v`
**Explanation:** Provides detailed logging during analysis.

### Skip duplicate marking
**Args:** `mapcaller -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o output/ --no-duplicates`
**Explanation:** Skips duplicate marking step.

### Generate report
**Args:** `mapcaller -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o output/ --report`
**Explanation:** Generates analysis report.