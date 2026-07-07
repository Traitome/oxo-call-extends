---
name: sickle-trim
category: qc
description: sickle-trim - Windowed adaptive trimming for FASTQ files
tags: ["sickle-trim", "qc", "fastq", "trimming"]
author: oxo-call-community
source_url: "https://github.com/najoshi/sickle"
---

## Concepts

- **Tool Overview**: sickle-trim (v1.33) performs windowed adaptive trimming on FASTQ files.
- **Core Function**: Trims low-quality ends from sequencing reads.
- **Algorithm**: Uses sliding window quality-based trimming.
- **Input/Output**: Accepts FASTQ files and produces trimmed reads.
- **Quality Trimming**: Focuses on maintaining read quality.
- **Applications**: NGS preprocessing, read cleaning, and quality control.

## Pitfalls

- **Quality Format**: Requires correct quality encoding (Phred+33 or Phred+64).
- **Parameter Tuning**: Requires careful adjustment of quality thresholds.
- **Input Format**: Must be valid FASTQ format.
- **Read Length**: May produce very short reads after trimming.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Trim single-end reads
**Args:** `sickle-trim se -f reads.fastq -o trimmed.fastq -t sanger`
**Explanation:** `-f` input; `-o` output; `-t` quality type.

### Trim paired-end reads
**Args:** `sickle-trim pe -f reads_1.fastq -r reads_2.fastq -o trimmed_1.fastq -p trimmed_2.fastq -t sanger`
**Explanation:** Paired-end trimming with forward and reverse reads.

### With quality threshold
**Args:** `sickle-trim se -f reads.fastq -o trimmed.fastq -q 20 -t sanger`
**Explanation:** `-q 20` minimum quality threshold.

### Help command
**Args:** `sickle-trim --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sickle-trim --version`
**Explanation:** Shows current version.

### With minimum length
**Args:** `sickle-trim se -f reads.fastq -o trimmed.fastq -l 50 -t sanger`
**Explanation:** `-l 50` minimum output read length.

### Phred+64 encoding
**Args:** `sickle-trim se -f reads.fastq -o trimmed.fastq -t illumina`
**Explanation:** `-t illumina` uses Phred+64 encoding.
