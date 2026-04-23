---
name: chopper
category: qc
description: Filter and trim long reads (PacBio/ONT) based on quality, length, and GC content
tags: [chopper, long-reads, filtering, trimming, ont, pacbio, nanopore, qc]
author: oxo-call-community
source_url: "https://github.com/wdecoster/chopper"
---

## Concepts

- **Tool Overview**: Chopper is a Rust-based tool for filtering and trimming long reads from PacBio and Oxford Nanopore sequencing. It is the successor to NanoFilt and NanoLyse with much faster performance.
- **Core Function**: Filters reads by quality, length, and GC content, and trims reads from either end. Also supports removal of host/laboratory sequences.
- **Input/Output**: Input: FASTQ format (stdin or file). Output: Filtered/trimmed FASTQ to stdout. Supports gzip compression.
- **Quality Filtering**: Uses mean read quality scores. ONT reads typically have Phred quality scores.
- **Headcrop/Tailcrop**: Trims specified number of bases from the start (headcrop) or end (tailcrop) of reads.
- **Lambda Phage Removal**: Built-in support for filtering out lambda phage control reads using `--lcf` (lambda control filter).

## Pitfalls

- **Stdin/Stdout**: By default reads from stdin and writes to stdout. Use `--input` for file input and pipe or redirect output.
- **Quality Encoding**: Ensure quality scores are in the correct encoding (Phred+33 for most modern data).
- **Order of Operations**: Filtering is applied before trimming. A read must pass filters before trimming is applied.
- **Compressed Input**: Supports gzip-compressed FASTQ input. Use `--input` flag with .gz files.
- **No In-Place Editing**: Cannot modify files in place. Must redirect output to a new file.

## Examples

### Filter by minimum quality and length
**Args:** `--input reads.fq.gz --minqual 10 --minlength 1000`
**Explanation:** Retains only reads with mean quality >= Q10 and length >= 1000bp, suitable for downstream assembly.

### Filter by maximum length
**Args:** `--input reads.fq.gz --maxlength 50000`
**Explanation:** Removes extremely long reads (>50kb) that may cause issues in some analysis tools.

### Trim reads from both ends
**Args:** `--input reads.fq.gz --headcrop 50 --tailcrop 100`
**Explanation:** Removes 50bp from the start and 100bp from the end of each read, useful for removing adapter artifacts.

### Filter by GC content
**Args:** `--input reads.fq.gz --mingc 0.3 --maxgc 0.7`
**Explanation:** Retains reads with GC content between 30% and 70%, useful for removing AT-rich or GC-rich contaminants.

### Combine quality filtering with trimming
**Args:** `--input reads.fq.gz --minqual 7 --minlength 500 --headcrop 100`
**Explanation:** Filters reads by quality >= Q7 and length >= 500bp, then trims 100bp from the start of surviving reads.

### Remove lambda phage control reads
**Args:** `--input reads.fq.gz --lcf lambda_reference.fna`
**Explanation:** Removes reads that map to the lambda phage reference, commonly used as ONT sequencing control.

### Pipeline with gzip output
**Args:** `--input reads.fq.gz --minqual 10 --minlength 1000 | gzip > filtered.fq.gz`
**Explanation:** Filters reads and compresses output directly, saving disk space for large datasets.

### Filter with very stringent quality
**Args:** `--input reads.fq.gz --minqual 15 --minlength 5000 --maxlength 100000`
**Explanation:** Very stringent filtering for high-quality long reads, suitable for structural variant calling or haplotype phasing.
