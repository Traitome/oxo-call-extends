---
name: tagdust2
category: sequencing
description: Tool to extract high confidence reads from sequencing data.
tags: [tagdust2, sequencing, quality-control, reads]
author: oxo-call-community
source_url: "https://github.com/aradar46/tagdust"
---

## Concepts

- **Tool Overview**: tagdust2 (v2.33.1) extracts high confidence reads from sequencing data.
- **Core Function**: Filters and extracts high-quality sequencing reads.
- **Algorithm**: Uses quality-based filtering for read extraction.
- **Input/Output**: Input: FASTQ/BAM files; Output: Filtered reads.
- **Applications**: Read quality control, preprocessing, data cleaning.
- **Installation**: `conda install -c bioconda tagdust2` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large sequencing files require significant memory.
- **Quality Threshold**: Incorrect thresholds affect results.
- **Input Format**: Supports limited input formats.
- **Adapter Trimming**: May not handle all adapter types.
- **Paired-end Data**: Requires proper handling of paired reads.
- **Performance**: Processing large files can be slow.

## Examples

### Display help
**Args:** `tagdust2 --help`
**Explanation:** Shows available options and usage information.

### Basic filtering
**Args:** `tagdust2 -i input.fastq -o filtered.fastq`
**Explanation:** Extract high confidence reads from FASTQ.

### With quality threshold
**Args:** `tagdust2 -i input.fastq -o filtered.fastq -q 20`
**Explanation:** Filter reads with minimum quality score of 20.

### Verbose mode
**Args:** `tagdust2 -i input.fastq -o filtered.fastq -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tagdust2 -i input.fastq -o filtered.fastq --stats`
**Explanation:** Generate statistics about filtering.

### Batch processing
**Args:** `for f in fastq/*.fastq; do tagdust2 -i $f -o filtered/${f%.fastq}_filtered.fastq; done`
**Explanation:** Process multiple FASTQ files.

### Paired-end data
**Args:** `tagdust2 -i reads_1.fastq -j reads_2.fastq -o filtered_1.fastq -p filtered_2.fastq`
**Explanation:** Process paired-end reads.

### Include adapter trimming
**Args:** `tagdust2 -i input.fastq -o filtered.fastq -a adapters.fa`
**Explanation:** Trim adapters during filtering.

### Generate report
**Args:** `tagdust2 -i input.fastq -o filtered.fastq --report`
**Explanation:** Generate comprehensive filtering report.
