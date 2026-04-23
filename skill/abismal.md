---
name: abismal
category: alignment
description: abismal is a fast and memory-efficient mapper for short bisulfite sequencing reads.
tags: [abismal, alignment, bisulfite, methylation, wgbs]
author: oxo-call-community
source_url: "https://github.com/smithlabcode/abismal"
---

## Concepts

- **Tool Overview**: A fast, memory-efficient mapper for whole genome bisulfite sequencing (WGBS) reads. Version 3.3.0.
- **Core Function**: Maps bisulfite-converted reads to a reference genome while accounting for C→T (and G→A) conversions from bisulfite treatment.
- **Input/Output**: Input is FASTQ reads and reference genome (FASTA or pre-built index); output is SAM/BAM format alignments.
- **Installation**: Install via bioconda: `conda install -c bioconda abismal`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **Two Subcommands**: `abismal idx` (build index) and `abismal map` (align reads)
- **Indexing Recommended**: Pre-building an index with `abismal idx` significantly speeds up mapping compared to using raw FASTA.
- **Multi-threading**: Supports up to 128 threads with `-t` flag for parallel processing.
- **PBAT Support**: Supports Post-Bisulfite Adaptor Tagging (PBAT) library protocols with `-P` and `-R` flags.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Index vs Genome**: Must use either `-i` (index) OR `-g` (genome FASTA), not both. Index is faster.
- **Bisulfite Conversion**: Assumes standard bisulfite conversion (C→T on forward strand, G→A on reverse). Use `-A` or `-P` for alternative protocols.
- **Output is SAM**: Default output is SAM (text). Use `-B` flag for BAM output or pipe through samtools.
- **Maximum Edit Distance**: Default `-m 0.1` allows 10% mismatches relative to read length. Adjust for lower-quality data.
- **Paired-End Insert Size**: Default `-l 32 -L 3000` sets concordant fragment size range. Adjust for your library prep.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available subcommands (idx, map) and their options.

### Build a genome index (recommended first step)
**Args:** `idx reference.fa reference.idx`
**Explanation:** Creates an index file from the reference genome. This significantly speeds up subsequent mapping runs.

### Map single-end reads using genome FASTA
**Args:** `map -g reference.fa -o aligned.sam reads.fq`
**Explanation:** Maps single-end bisulfite reads directly using the FASTA genome. Slower than using an index but simpler for one-off runs.

### Map paired-end reads using pre-built index
**Args:** `map -i reference.idx -o aligned.sam -t 8 reads_R1.fq reads_R2.fq`
**Explanation:** Maps paired-end reads using 8 threads with a pre-built index. Fastest method for repeated mapping against the same reference.

### Output BAM format with statistics
**Args:** `map -i ref.idx -B -s stats.yaml -o aligned.bam -t 12 reads_1.fq reads_2.fq`
**Explanation:** Outputs BAM format directly, saves mapping statistics to YAML file, and uses 12 threads for faster processing.

### Map PBAT library reads
**Args:** `map -i ref.idx -P -o aligned.sam reads_1.fq reads_2.fq`
**Explanation:** Maps PBAT (Post-Bisulfite Adaptor Tagging) library reads where conversion direction is reversed compared to standard WGBS.

### Map with relaxed edit distance
**Args:** `map -i ref.idx -m 0.15 -o aligned.sam reads.fq`
**Explanation:** Allows up to 15% mismatches (default is 10%). Useful for lower-quality bisulfite sequencing data.

### Filter for concordant pairs only
**Args:** `awk '$1 ~ /^@/ || $7 == "="' aligned.sam > concordant.sam`
**Explanation:** Extracts only concordantly paired reads from the SAM output using awk. Flag 0x100 indicates ambiguous mappings.
