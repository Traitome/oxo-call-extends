---
name: imseq
category: immunology
description: Fast, PCR and sequencing error aware tool for analyzing T-cell receptor and immunoglobulin gene sequencing data
tags: [imseq, TCR, BCR, immune-repertoire]
author: oxo-call-community
source_url: "http://www.imtools.org/"
---

## Concepts

- **Tool Overview**: IMSEQ (v1.1.0) is a fast, error-aware tool for analyzing high-throughput T-cell receptor (TCR) and immunoglobulin gene sequencing data.
- **Core Function**: Processes TCR/BCR sequencing reads, handles PCR and sequencing errors, and identifies clonotypes with high accuracy.
- **Error Handling**: Incorporates error-aware algorithms to correct sequencing errors and PCR artifacts without discarding reads.
- **Input/Output**: Accepts FASTA/FASTQ files (including gzipped). Outputs clonotype counts, per-read statistics, and CDR3 sequences.
- **Reference Segments**: Requires V/D/J segment reference files for human TRA, TRB, and other receptor types.

## Pitfalls

- **Reference Segment Format**: Reference files must be in correct FASTA format with properly formatted segment names.
- **Strand Orientation**: TCR amplicons have specific orientation; use -r flag for reverse strand sequences.
- **Quality Thresholds**: Default quality filtering may be too strict; adjust -mq parameter based on data quality.
- **Barcode Handling**: PCR barcodes require special handling with -bcl and -ber parameters.
- **Memory Usage**: Large datasets may require significant memory; consider splitting input files.

## Examples

### Basic TCR sequence analysis
**Args:** `imseq -ref Homo.Sapiens.TRB.fa -o output.tsv input.fastq`
**Explanation:** Processes TCR beta chain sequencing data and outputs detailed per-read information.

### Reverse strand orientation
**Args:** `imseq -r -ref Homo.Sapiens.TRB.fa -o output.tsv input.fasta`
**Explanation:** Processes sequences on forward strand (use -r for reverse complement reads).

### Amino acid clonotype output
**Args:** `imseq -ref Homo.Sapiens.TRB.fa -j 4 -oa clonotypes.txt input.fastq.gz`
**Explanation:** Outputs amino acid-based clonotype counts using 4 parallel threads.

### Quality filtering and clustering
**Args:** `imseq -ref Homo.Sapiens.TRB.fa -mq 10 -qc -oa output.txt input.fastq`
**Explanation:** Uses quality threshold of 10 with posterior clustering to rescue low-quality reads.

### PCR barcode correction
**Args:** `imseq -ref Homo.Sapiens.TRB.fa -bcl 10 -ber 0.1 -oa output.txt input.fastq`
**Explanation:** Handles 10-base PCR barcodes with 0.1 error rate for barcode-based clustering.

### Paired-end data processing
**Args:** `imseq -ref Homo.Sapiens.TRA.fa -1 read1.fastq -2 read2.fastq -o output.tsv`
**Explanation:** Processes paired-end TCR alpha chain sequencing data.