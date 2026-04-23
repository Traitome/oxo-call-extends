---
name: bam2fasta
category: utility
description: bam2fasta - CLI tool to convert BAM to FASTA format
tags: [bam-conversion, fasta, format-conversion, sequence-extraction]
author: oxo-call-community
source_url: "https://github.com/czbiohub/bam2fasta"
---

## Concepts

- **Tool Overview**: bam2fasta converts BAM alignment files to FASTA format, extracting sequences from aligned reads.

- **Sequence Extraction**: Extracts read sequences from BAM files, optionally applying quality filters.

- **Format Conversion**: Simple conversion from alignment format to sequence format for downstream analysis.

## Pitfalls

- **Alignment Information Lost**: Converting to FASTA loses alignment information. Use appropriate downstream tools.

- **Duplicate Reads**: Does not automatically deduplicate. May include PCR duplicates.

- **Quality Filtering**: Consider filtering low-quality reads before conversion.

## Examples

### Basic conversion
**Args:** `bam2fasta -b alignments.bam -o sequences.fasta`
**Explanation:** Converts all reads in BAM to FASTA format.

### Filter by quality
**Args:** `bam2fasta -b alignments.bam -q 20 -o filtered.fasta`
**Explanation:** Extracts only reads with mapping quality ≥20.

### Extract specific region
**Args:** `bam2fasta -b alignments.bam -r chr1:1000-2000 -o region.fasta`
**Explanation:** Extracts sequences aligned to specified genomic region.
