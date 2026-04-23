---
name: fastp
category: qc
description: An ultra-fast all-in-one FASTQ preprocessor for quality control, adapter trimming, quality filtering, and per-read quality pruning.
tags: [fastp, qc, trimming, adapter, fastq, paired-end, umi]
author: oxo-call-community
source_url: "https://github.com/OpenGene/fastp"
---

## Concepts

- **Tool Overview**: fastp is an all-in-one FASTQ preprocessor that performs quality control, adapter trimming, quality filtering, and per-read quality pruning in a single pass. It is 2-4× faster than Trimmomatic and produces HTML + JSON QC reports. Version 0.23.4.
- **Single vs Paired-End**: For single-end use `-i input.fq.gz -o output.fq.gz`. For paired-end use `-i R1.fq.gz -I R2.fq.gz -o R1_out.fq.gz -O R2_out.fq.gz`. Paired-end mode automatically handles read synchronization.
- **Automatic Adapter Detection**: fastp detects adapters automatically from the data using overlap analysis (for paired-end) or known Illumina adapter sequences. Override with `--adapter_sequence` and `--adapter_sequence_r2`.
- **Quality Reports**: Always generates `fastp.html` (interactive HTML report) and `fastp.json` (machine-readable) by default. Redirect with `-h report.html -j report.json`. Use with MultiQC for multi-sample summaries.
- **UMI Support**: fastp natively supports UMI (Unique Molecular Identifier) extraction and deduplication with `--umi --umi_loc` options. Supports read1/read2/index1/index2 UMI locations.
- **Deduplication**: Built-in exact-match deduplication with `--dedup` (no sorting required). This deduplicates based on read sequence, not coordinates — useful before alignment or for amplicon data.
- **Thread Control**: Use `-w N` to set worker threads (default 3). Setting `-w 16` is usually optimal for modern servers; increasing beyond 16 rarely helps due to I/O bottlenecks.
- **Installation**: `conda install -c bioconda fastp`

## Pitfalls

- **CRITICAL - Paired-End Flags**: For paired-end data, use `-i`/`-o` for R1 and `-I`/`-O` for R2 (uppercase for R2). Mixing them up will process only one file or crash.
- **Output Files Not Created by Default**: Without `-o`/`-O`, processed reads are written to stdout. Always specify output files for paired-end to prevent interleaved output.
- **Adapter Detection Quality**: For very short inserts (<30 bp), automatic adapter detection may fail. Specify adapters explicitly with `--adapter_sequence AGATCGGAAGAGC` (Illumina TruSeq).
- **--disable_adapter_trimming vs Filtering**: `--disable_adapter_trimming` only stops adapter removal; quality filtering still applies. Use `--disable_quality_filtering` separately to turn off quality-based filtering.
- **Low Complexity Filtering**: fastp can filter low-complexity reads with `--low_complexity_filter`. Default is disabled. Enable for metagenomics to remove repetitive/homopolymer reads.

## Examples

### Quality trim paired-end reads (most common usage)
**Args:** `-i sample_R1.fastq.gz -I sample_R2.fastq.gz -o trimmed_R1.fastq.gz -O trimmed_R2.fastq.gz -h sample_fastp.html -j sample_fastp.json -w 8`
**Explanation:** Processes paired-end FASTQ with 8 threads. Automatically detects and trims adapters, applies quality/length filtering, and generates both HTML and JSON QC reports. This is the standard production command.

### Single-end quality trimming
**Args:** `-i sample.fastq.gz -o trimmed.fastq.gz -h qc_report.html -j qc_stats.json`
**Explanation:** Single-end mode. Automatic adapter detection and quality filtering. HTML report for visual inspection, JSON for programmatic parsing (e.g., MultiQC integration).

### Trim with explicit adapter sequences
**Args:** `-i R1.fastq.gz -I R2.fastq.gz -o R1_trim.fastq.gz -O R2_trim.fastq.gz --adapter_sequence AGATCGGAAGAGCACACGTCTGAACTCCAGTCA --adapter_sequence_r2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT`
**Explanation:** Explicitly specify TruSeq Read1 and Read2 adapters. Use when automatic detection is unreliable (short inserts, specific library preparation kits).

### Strict quality filtering for variant calling
**Args:** `-i R1.fastq.gz -I R2.fastq.gz -o R1_strict.fastq.gz -O R2_strict.fastq.gz -q 30 -l 50 --correction -w 8`
**Explanation:** `-q 30` raises minimum quality threshold from default 15 to 30; `-l 50` requires minimum 50 bp after trimming; `--correction` enables correction of mismatched bases in overlapping paired-end regions. Reduces false variant calls.

### UMI-based deduplication
**Args:** `-i R1.fastq.gz -I R2.fastq.gz -o R1_umi.fastq.gz -O R2_umi.fastq.gz --umi --umi_loc read1 --umi_len 12 -w 8`
**Explanation:** Extracts 12-bp UMI from the start of read1, appends to read name, and deduplicates based on UMI+sequence. `--umi_loc` can be read1, read2, index1, index2, or per_index.

### Generate QC report without filtering (assessment only)
**Args:** `-i R1.fastq.gz -I R2.fastq.gz --disable_adapter_trimming --disable_quality_filtering --disable_length_filtering -o /dev/null -O /dev/null -h raw_qc.html -j raw_qc.json`
**Explanation:** Disables all modifications to assess raw data quality only. Output to `/dev/null` discards processed reads while still generating QC reports. Useful for initial data assessment.

### Split output into multiple files for parallel downstream processing
**Args:** `-i R1.fastq.gz -I R2.fastq.gz -o R1_trim.fastq.gz -O R2_trim.fastq.gz --split_by_lines 40000000`
**Explanation:** Splits output into chunks of 40M lines each (10M reads per file). Useful for distributing downstream alignment across multiple parallel jobs.
