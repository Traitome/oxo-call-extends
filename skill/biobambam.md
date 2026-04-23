---
name: biobambam
category: utility
description: Tools for early stage alignment file processing
tags: [bam, sam, alignment-processing, sorting, markdup]
author: oxo-call-community
source_url: "https://gitlab.com/german.tischler/biobambam2"
---

## Concepts
- **Tool Overview**: biobambam2 is a suite of tools for early-stage alignment file processing. It provides high-performance alternatives to common BAM/SAM operations.
- **Key Tools**: `bamsort` (sort BAM), `bammarkduplicates` (mark duplicates), `bamcollate2` (collate paired reads), `bamsormadup` (sort and mark duplicates in one pass), `bamtofastq` (BAM to FASTQ).
- **Performance**: Optimized for speed and memory efficiency, often faster than Picard/samtools equivalents.
- **Streaming**: Supports streaming for pipeline integration.

## Pitfalls
- **Parameter Differences**: Parameters differ from samtools/Picard equivalents; check documentation.
- **Output Format**: Some tools produce slightly different output formats.

## Examples
### Sort and mark duplicates in one pass
**Args:** `bamsormadup input.bam --output-markdup=dedup.bam --output-markdupoob=metrics.txt`
**Explanation:** Sorts and marks duplicates in a single efficient pass.

### Sort BAM file
**Args:** `bamsort input.bam --output=sorted.bam`
**Explanation:** Sorts BAM file by coordinate.

### Convert BAM to FASTQ
**Args:** `bamtofastq input.bam --outputF=/dev/stdout --outputF2=/dev/stderr`
**Explanation:** Converts BAM to paired FASTQ files.

### Collate paired reads
**Args:** `bamcollate2 input.bam --output=collated.bam`
**Explanation:** Reorders BAM so paired reads are adjacent.
