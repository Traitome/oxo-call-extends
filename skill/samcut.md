---
name: samcut
category: utility
description: Column extraction tool for SAM/BAM files using human-readable field names
tags: ["samcut", "SAM", "BAM", "cut", "utility"]
author: oxo-call-community
source_url: "https://github.com/gshiba/samcut"
---

## Concepts

- **Tool Overview**: samcut (v0.1.1) is a command-line tool for extracting specific columns from SAM/BAM files using human-readable field names instead of column indices.
- **Core Function**: Selects and outputs specific fields from SAM/BAM alignments, similar to the Unix `cut` command but with SAM-specific field names.
- **Algorithm**: Parses SAM format and maps human-readable field names (e.g., "qname", "flag", "rname") to their corresponding columns.
- **Input Format**: SAM/BAM files (from samtools view output or piped input).
- **Output Format**: Selected fields in tab-separated format.
- **Use Case**: Custom reporting, quick data extraction, pipeline integration.

## Pitfalls

- **Input format**: Requires properly formatted SAM input (not BAM directly).
- **Field availability**: Some optional fields may not be present in all SAM records.
- **Performance**: Processing very large files may require streaming.
- **Header lines**: May require filtering header lines separately.
- **Tag parsing**: Custom SAM tags may require specific handling.
- **Delimiter options**: Limited delimiter customization.

## Examples

### Extract specific fields
**Args:** `samtools view input.bam | samcut qname rname pos mapq`
**Explanation:** Extracts query name, reference name, position, and mapping quality.

### Output all fields
**Args:** `samtools view input.bam | samcut -a`
**Explanation:** `-a` outputs all available fields.

### Custom delimiter
**Args:** `samtools view input.bam | samcut -d "," qname pos`
**Explanation:** `-d` specifies custom delimiter (comma).

### With header
**Args:** `samtools view input.bam | samcut -H qname rname pos`
**Explanation:** `-H` includes header line with field names.

### Extract tags
**Args:** `samtools view input.bam | samcut qname tags:NM tags:MD`
**Explanation:** Extracts specific SAM tags (NM, MD).

### Count occurrences
**Args:** `samtools view input.bam | samcut flag | sort | uniq -c`
**Explanation:** Counts occurrences of each flag value.

### Filter and extract
**Args:** `samtools view input.bam | samcut qname mapq | awk '$2 >= 30'`
**Explanation:** Extracts reads with mapping quality >= 30.