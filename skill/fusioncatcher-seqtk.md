---
name: fusioncatcher-seqtk
category: utility
description: Modified Seqtk version required for FusionCatcher.
tags: [fusioncatcher-seqtk, sequence processing, FASTQ, FusionCatcher]
author: oxo-call-community
source_url: "https://github.com/ndaniel/seqtk"
---

## Concepts
- **Seqtk Modification**: Modified version of seqtk for FusionCatcher.
- **Sequence Processing**: Processes sequencing data for fusion detection.
- **FASTQ Manipulation**: Handles FASTQ file operations.
- **Quality Filtering**: Filters reads by quality.
- **Adapter Trimming**: Trims adapter sequences from reads.

## Pitfalls
- **Specialized Use**: Designed specifically for FusionCatcher.
- **Compatibility**: May not be compatible with standard seqtk workflows.
- **Version Specific**: Requires specific version for FusionCatcher.
- **Limited Functionality**: May lack some features of standard seqtk.
- **Dependency**: Required as a dependency for FusionCatcher.

## Examples
### Convert FASTQ to FASTA
**Args:** `fusioncatcher-seqtk seq reads.fastq > reads.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Filter low-quality reads
**Args:** `fusioncatcher-seqtk trim -q 20 reads.fastq > filtered.fastq`
**Explanation:** Filters reads with quality < 20.

### Subsample reads
**Args:** `fusioncatcher-seqtk sample -s 123 reads.fastq 10000 > subsampled.fastq`
**Explanation:** Subsamples 10000 reads with seed 123.

### Trim adapters
**Args:** `fusioncatcher-seqtk trim adapters.fasta reads.fastq > trimmed.fastq`
**Explanation:** Trims adapter sequences from reads.

### Extract sequences by name
**Args:** `fusioncatcher-seqtk subseq reads.fastq names.txt > subset.fastq`
**Explanation:** Extracts reads matching names in names.txt.