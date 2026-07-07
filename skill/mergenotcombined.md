---
name: mergenotcombined
category: utility
description: Merge forward and reverse reads from separate FASTQ files.
tags: [mergenotcombined, fastq, sequence-manipulation]
author: oxo-call-community
source_url: "https://github.com/andvides/mergeNotCombined.git"
---

## Concepts

- **Tool Overview**: mergentotcombined merges paired-end reads from separate files.
- **Core Function**: Combines forward and reverse read files.
- **FASTQ Format**: Works with standard FASTQ format.
- **Paired-end Support**: Handles paired-end sequencing data.
- **File Matching**: Matches reads by sequence identifiers.
- **Installation**: `conda install -c bioconda mergenotcombined`

## Pitfalls

- **Read Order**: Requires matching read order in files.
- **File Format**: Must be valid FASTQ format.
- **Identifier Matching**: Depends on consistent identifiers.
- **Memory Requirements**: High memory for large files.
- **Output Size**: Combined output can be large.
- **Read Pairing**: Unpaired reads may cause issues.

## Examples

### Merge paired reads
**Args:** `mergenotcombined -1 R1.fastq -2 R2.fastq -o merged.fastq`
**Explanation:** Merges forward and reverse reads.

### Gzipped input
**Args:** `mergenotcombined -1 R1.fastq.gz -2 R2.fastq.gz -o merged.fastq`
**Explanation:** Handles gzipped input files.

### Paired output
**Args:** `mergenotcombined -1 R1.fastq -2 R2.fastq --paired -o merged/`
**Explanation:** Outputs paired reads separately.

### Verbose mode
**Args:** `mergenotcombined -1 R1.fastq -2 R2.fastq -v -o merged.fastq`
**Explanation:** Shows detailed processing progress.

### Help documentation
**Args:** `mergenotcombined --help`
**Explanation:** Displays available options.
