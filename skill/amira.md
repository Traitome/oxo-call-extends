---
name: amira
category: annotation
description: Tool for detecting acquired antimicrobial resistance (AMR) genes directly from bacterial long read sequencing data
tags: [amr, antimicrobial-resistance, long-reads, nanopore, pacbio]
author: oxo-call-community
source_url: "https://github.com/Danderson123/Amira"
---

## Concepts

- **Tool Overview**: Amira detects acquired AMR genes directly from bacterial long read sequences (ONT/PacBio), bypassing the need for genome assembly.
- **Core Function**: Identifies AMR genes by mapping long reads directly to AMR databases, reducing time and avoiding assembly-related errors.
- **Input/Output**: Input: Long read FASTQ files. Output: Detected AMR genes with coverage and identity statistics.
- **Advantage**: Works directly on reads without assembly, enabling faster AMR detection and avoiding assembly artifacts.
- **Installation**: Install via bioconda: `conda install -c bioconda amira`

## Pitfalls

- **Read Quality**: Low-quality long reads may produce false positives - consider read filtering first.
- **Coverage Requirements**: Sufficient coverage of AMR genes is needed for reliable detection.
- **Database Currency**: AMR gene detection depends on database currency - update databases regularly.
- **Acquired Genes Only**: Designed for acquired AMR genes, not chromosomal point mutations conferring resistance.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for Amira.

### Detect AMR from long reads
**Args:** `detect -i reads.fastq -o amr_results/`
**Explanation:** Detects AMR genes directly from long read sequencing data.

### Specify database
**Args:** `detect -i reads.fastq -d /path/to/amr_db -o results/`
**Explanation:** Uses custom AMR gene database for detection.

### Set minimum identity threshold
**Args:** `detect -i reads.fastq --min-identity 90 -o results/`
**Explanation:** Requires ≥90% sequence identity for AMR gene matches.

### Set minimum coverage threshold
**Args:** `detect -i reads.fastq --min-coverage 80 -o results/`
**Explanation:** Requires ≥80% of AMR gene covered by reads for reporting.

### Process compressed FASTQ
**Args:** `detect -i reads.fastq.gz -o results/`
**Explanation:** Directly processes gzip-compressed FASTQ files.

### Output detailed report
**Args:** `detect -i reads.fastq -o results/ --detailed`
**Explanation:** Generates detailed report with per-read alignment information.

### Batch process samples
**Args:** `detect -i sample1.fastq -o results/s1/ && amira detect -i sample2.fastq -o results/s2/`
**Explanation:** Processes multiple samples sequentially with separate output directories.
