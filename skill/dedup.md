---
name: dedup
category: utility
description: DeDup - read deduplication tool for paired-end read merging in ancient DNA experiments.
tags: [dedup, utility, deduplication, ancient-dna, paired-end]
author: oxo-call-community
source_url: "https://github.com/apeltzer/dedup"
---

## Concepts

- **Tool Overview**: dedup (v0.12.9+) is a tool for read deduplication in paired-end read merging, specifically designed for ancient DNA experiments where duplicates are common due to library preparation.
- **Core Function**: Identifies and removes duplicate reads from paired-end sequencing data, improving mapping quality and reducing false positives in downstream analysis.
- **Input/Output**: Input: Paired-end FASTQ reads, optionally aligned BAM. Output: Deduplicated FASTQ/BAM files, deduplication statistics.
- **Algorithm**: Uses read identifiers, sequences, and quality scores to identify duplicate reads, with special handling for ancient DNA damage patterns.
- **Key Features**: Ancient DNA optimized, paired-end support, multiple deduplication criteria, statistics reporting, BAM/FASTQ support.
- **Installation**: `conda install -c bioconda dedup`

## Pitfalls

- **Duplicate Detection**: Stringent criteria may remove true biological duplicates.
- **Ancient DNA Specific**: Optimized for aDNA; may not be optimal for modern DNA.
- **Read Length**: Short reads may affect deduplication accuracy.
- **Quality Threshold**: Quality-based deduplication requires appropriate thresholds.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Deduplicate FASTQ reads
**Args:** `dedup -1 R1.fastq -2 R2.fastq -o deduplicated/`
**Explanation:** Deduplicate paired-end FASTQ reads.

### Deduplicate aligned BAM
**Args:** `dedup -i aligned.bam -o deduplicated.bam`
**Explanation:** Deduplicate reads in aligned BAM file.

### With quality filtering
**Args:** `dedup -1 R1.fastq -2 R2.fastq -o deduplicated/ -q 20`
**Explanation:** Apply quality threshold of 20 for deduplication.