---
name: dascrubber
category: alignment
description: DASCRUBBER - alignment-based scrubbing pipeline for long reads
tags: [dascrubber, alignment, long-reads, polishing, error-correction]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/DASCRUBBER"
---

## Concepts

- **Tool Overview**: dascrubber (v0.0.1a2+) is an alignment-based scrubbing pipeline for long-read sequencing data.
- **Core Function**: Identifies and removes artifacts, contaminants, and low-quality regions from long reads.
- **Input/Output**: Input: Long-read sequences (FASTA/FASTQ). Output: Cleaned reads, quality reports.
- **Algorithm**: Uses self-alignment and reference alignment to identify and remove problematic regions.
- **Key Features**: Handles PacBio/ONT reads, removes chimeras, improves read quality.
- **Installation**: `conda install -c bioconda dascrubber`

## Pitfalls

- **Read Length**: Works best with long reads (PacBio/ONT).
- **Memory Usage**: May require significant memory for large datasets.
- **Reference Quality**: Reference-based scrubbing requires good quality references.
- **Chimera Detection**: May miss complex chimeric reads.
- **Over-scrubbing**: Aggressive parameters may remove valid sequences.

## Examples

### Scrub long reads
**Args:** `dascrubber -i reads.fastq -o cleaned_reads.fastq`
**Explanation:** Run alignment-based scrubbing on long reads.

### Use reference for scrubbing
**Args:** `dascrubber -i reads.fastq -r reference.fasta -o cleaned.fastq`
**Explanation:** Use reference-guided scrubbing for improved accuracy.

### Generate quality report
**Args:** `dascrubber -i reads.fastq -o cleaned.fastq --report`
**Explanation:** Generate quality report with scrubbing statistics.
