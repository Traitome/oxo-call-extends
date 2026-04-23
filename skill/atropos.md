---
name: atropos
category: qc
description: Atropos - High-sensitivity and high-specificity NGS read trimming tool for adapter and quality trimming
tags: [adapter-trimming, quality-trimming, ngs, read-processing, cutadapt-alternative]
author: oxo-call-community
source_url: "https://github.com/jdidion/atropos"
---

## Concepts

- **Tool Overview**: Atropos is a command-line tool for trimming adapter sequences and low-quality bases from high-throughput sequencing reads. It provides high sensitivity and specificity while maintaining leading-edge speed through multi-threading and optimized algorithms.

- **Adapter Types**: Supports multiple adapter types including 3' adapters (-a), 5' adapters (-g), anchored adapters, linked adapters, and any-position adapters (-b). For paired-end reads, use uppercase options (-A, -G, -B) for the second read.

- **Alignment Algorithms**: Offers two alignment modes - the traditional adapter alignment (semi-global alignment) and the insert alignment algorithm (optimized for paired-end reads, aligns read pairs first then detects adapters).

- **Quality Trimming**: Supports quality score-based trimming using Phred scores. Can trim from both 5' and 3' ends independently using comma-separated thresholds (e.g., -q 15,10).

- **Multi-threading**: Utilizes multiple CPU cores for parallel processing using the -T option, significantly improving performance on large datasets.

- **File Format Support**: Automatically detects and handles FASTA, FASTQ, and SAM/BAM formats, including gzip, bzip2, and xz compression.

- **Demultiplexing**: Supports barcode-based demultiplexing with named adapter sequences and wildcard matching for flexible barcode patterns.

## Pitfalls

- **Adapter Detection Order**: By default, Atropos processes operations in order: fixed trimming → quality trimming → adapter trimming. Use --op-order to customize this sequence if needed.

- **Insert Alignment Requirements**: The insert alignment algorithm (--aligner insert) requires paired-end reads and works best when adapters are present in both reads.

- **Minimum Overlap**: The -O option sets minimum adapter overlap length. Too small values may cause false positives, while too large values may miss short adapter fragments.

- **Error Rate Sensitivity**: Default error rate is 10% (-e 0.1). For high-quality data, consider lowering this; for degraded samples, may need to increase it.

- **Read Length Filtering**: After trimming, reads may become very short. Use -m to set minimum length to avoid downstream analysis issues.

- **Paired-End Consistency**: When trimming paired-end reads, both reads in a pair are processed together. If one read is discarded, the pair may be broken unless using appropriate filtering options.

## Examples

### Basic 3' adapter trimming for single-end reads
**Args:** `atropos -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -o trimmed.fastq.gz -se input.fastq.gz`
**Explanation:** Trims Illumina TruSeq adapter from 3' end of single-end reads. Input and output are gzip compressed.

### Paired-end adapter trimming with insert alignment
**Args:** `atropos --aligner insert -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -o trimmed_R1.fq.gz -p trimmed_R2.fq.gz -pe1 reads_R1.fq.gz -pe2 reads_R2.fq.gz`
**Explanation:** Uses insert alignment algorithm for more accurate paired-end adapter detection. Both forward and reverse adapters specified.

### Quality trimming with adapter removal
**Args:** `atropos -q 20,15 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -m 30 -o trimmed.fastq -se input.fastq`
**Explanation:** Trims low-quality bases (Q<20 from 5' end, Q<15 from 3' end), removes adapters, and discards reads shorter than 30bp.

### Multi-threaded processing with detailed reporting
**Args:** `atropos -T 8 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC --report-file report.txt --report-formats txt -o trimmed.fastq.gz -se input.fastq.gz`
**Explanation:** Uses 8 threads for faster processing and generates detailed text report with trimming statistics.

### Demultiplexing with multiple adapters
**Args:** `atropos -a one=TATA -a two=GCGC -a three=ATAT -o trimmed-{name}.fastq.gz -se input.fastq.gz`
**Explanation:** Demultiplexes reads based on different adapter sequences. Output files named with adapter names (trimmed-one.fastq.gz, etc.).

### Fixed-length trimming from both ends
**Args:** `atropos -u 5 -u -10 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -o trimmed.fastq -se input.fastq`
**Explanation:** Removes first 5 bases from 5' end and last 10 bases from 3' end, then performs adapter trimming.

### NextSeq polyG trimming
**Args:** `atropos --nextseq-trim 20 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -o trimmed.fastq.gz -se input.fastq.gz`
**Explanation:** Trims polyG tails from NextSeq/NovaSeq data (quality score threshold 20) in addition to adapter trimming.

### Adapter detection mode
**Args:** `atropos detect -pe1 reads_R1.fq -pe2 reads_R2.fq`
**Explanation:** Detects adapter sequences present in paired-end reads without performing trimming. Useful for identifying unknown adapters.

### Using adapter file
**Args:** `atropos -a file:adapters.fasta -o trimmed.fastq -se input.fastq`
**Explanation:** Loads adapter sequences from a FASTA file, allowing multiple adapter sequences to be trimmed in one pass.

### Wildcard adapter matching
**Args:** `atropos -a ACGTAANNNNTTAGC -o trimmed.fastq -se input.fastq`
**Explanation:** Uses N wildcards to match any base at specific positions, useful for adapters with variable barcode regions.
