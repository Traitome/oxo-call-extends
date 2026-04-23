---
name: bamrescue
category: utility
description: Bamrescue - Check BAM files for corruption and repair by skipping corrupted blocks
tags: [bam-repair, corruption-detection, data-recovery, bgzf]
author: oxo-call-community
source_url: "https://github.com/Arkanosis/bamrescue"
---

## Concepts

- **Tool Overview**: Bamrescue inspects BAM files for corruption and repairs them by skipping corrupted BGZF blocks, rescuing as much valid data as possible.

- **BGZF Structure**: Leverages the BGZF structure (concatenated gzip blocks) to identify and skip corrupted sections using CRC32 checksums.

- **Data Recovery**: Recovers valid data from partially corrupted BAM files that would otherwise be unreadable.

- **Integrity Checking**: Verifies BAM file integrity using built-in checksums.

## Pitfalls

- **Data Loss**: Corrupted blocks are skipped, resulting in data loss. Not all reads may be recovered.

- **Index Invalidation**: Repaired BAM files require reindexing. Old indexes are invalid.

- **Downstream Verification**: Verify downstream analysis results carefully after rescue, as some data is missing.

## Examples

### Check BAM integrity
**Args:** `bamrescue check alignments.bam`
**Explanation:** Checks BAM file for corruption without modifying it.

### Repair corrupted BAM
**Args:** `bamrescue repair alignments.bam -o repaired.bam`
**Explanation:** Repairs BAM file by skipping corrupted blocks, outputs repaired file.

### Verbose output
**Args:** `bamrescue check alignments.bam --verbose`
**Explanation:** Provides detailed information about corrupted blocks found.

### Estimate recoverable data
**Args:** `bamrescue check alignments.bam --estimate`
**Explanation:** Estimates percentage of data that can be recovered from corrupted file.
