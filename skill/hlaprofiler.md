---
name: hlaprofiler
category: immunology
description: HLAProfiler uses k-mer profiles to predict HLA types from paired-end RNA-seq data.
tags: [hlaprofiler, HLA, RNA-seq, k-mer, typing]
author: oxo-call-community
source_url: "https://github.com/ExpressionAnalysis/HLAProfiler"
---

## Concepts

- **k-mer Based Typing**: HLAProfiler uses k-mer content from RNA-seq reads to predict HLA types with >99% accuracy.
- **Kraken Classification**: Utilizes a modified Kraken taxonomic classifier to assign reads to HLA genes.
- **Profile Comparison**: Compares observed k-mer profiles against reference profiles to identify HLA alleles.
- **Paired-end Support**: Currently only supports paired-end RNA-seq data.
- **Reference Database**: Requires a pre-built database of HLA k-mer profiles for typing.

## Pitfalls

- **Database Creation**: Building a custom database is time-intensive due to thousands of HLA alleles.
- **Reference Requirements**: Requires specific reference files (HLA fasta, transcript fasta/gtf, exclusion bed).
- **Memory Usage**: k-mer counting can be memory-intensive for large RNA-seq datasets.
- **RNA-seq Only**: Designed specifically for RNA-seq data; not suitable for DNA sequencing.
- **Read Assignment**: Reads that cannot be assigned to a single HLA gene are excluded from analysis.

## Examples

### Build HLAProfiler database
**Args:** `perl HLAProfiler.pl build -t transcript.fasta -g transcript.gtf -e exclusion.bed -r hla_reference.fasta -cwd hla_cwd.txt -o ./db -db hla_db -kp /path/to/kraken -c 8`
**Explanation:** Builds a k-mer reference database for HLA typing using 8 threads.

### Run HLA typing on RNA-seq data
**Args:** `perl HLAProfiler.pl predict -fastq1 sample_R1.fastq.gz -fastq2 sample_R2.fastq.gz -db ./db/hla_db -o ./results -c 8`
**Explanation:** Performs HLA typing on paired-end RNA-seq data using the pre-built database.

### Download pre-built database
**Args:** `wget https://github.com/ExpressionAnalysis/HLAProfiler/releases/download/v1.0.0-db_only/HLAProfiler_db.tar.gz && tar -xvzf HLAProfiler_db.tar.gz`
**Explanation:** Downloads and extracts a pre-built HLA k-mer database.

### Generate typing report
**Args:** `perl HLAProfiler.pl predict -fastq1 R1.fastq.gz -fastq2 R2.fastq.gz -db ./db/hla_db -o ./results -report detailed`
**Explanation:** Runs HLA typing and generates a detailed report with confidence scores.

### Batch processing
**Args:** `perl HLAProfiler.pl batch -samples samples.txt -db ./db/hla_db -o ./batch_results -c 12`
**Explanation:** Processes multiple RNA-seq samples in batch mode using 12 threads.