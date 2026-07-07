---
name: bam2fastx
category: formatting
description: bam2fastx - Convert and demultiplex PacBio BAM files to FASTA/FASTQ format
tags: [bam2fastx, formatting, FASTA, FASTQ, BAM, PacBio, demultiplexing]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/bam2fastx"
---

## Concepts

- **Tool Overview**: bam2fastx is a PacBio tool for converting BAM files to FASTA or FASTQ format, with support for demultiplexing barcoded sequencing data. Version 3.0.0.
- **Core Function**: Converts PacBio BAM alignments to FASTA/FASTQ and demultiplexes barcoded reads.
- **Format Conversion**: Converts BAM format to gzipped FASTA or FASTQ files.
- **Demultiplexing**: Separates barcoded sequencing reads into individual files.
- **PacBio Specific**: Optimized for PacBio sequencing data including HiFi and CLR reads.
- **Input/Output**: Accepts PacBio BAM files, outputs gzipped FASTA/FASTQ files.
- **Installation**: `conda install -c bioconda bam2fastx`.

## Pitfalls

- **PacBio Only**: Designed specifically for PacBio BAM files. Not for Illumina or Nanopore data.
- **Barcode Compatibility**: Requires proper barcode information in BAM header.
- **Output Size**: Output files can be large. Ensure sufficient disk space.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Convert BAM to FASTQ
**Args:** `bam2fastq -i input.bam -o output.fastq.gz`
**Explanation:** Converts PacBio BAM to gzipped FASTQ format.

### Convert BAM to FASTA
**Args:** `bam2fasta -i input.bam -o output.fasta.gz`
**Explanation:** Converts PacBio BAM to gzipped FASTA format.

### Demultiplex barcoded reads
**Args:** `bam2fastq -i input.bam -o demultiplexed/ --split-barcode`
**Explanation:** Demultiplexes barcoded reads into separate FASTQ files.

### Preserve quality scores
**Args:** `bam2fastq -i input.bam -o output.fastq.gz --use-quality`
**Explanation:** Includes quality scores in output FASTQ.

### Filter by read type
**Args:** `bam2fastq -i input.bam -o hifi.fastq.gz --hifi-only`
**Explanation:** Extracts only HiFi reads from mixed dataset.

### Output uncompressed
**Args:** `bam2fastq -i input.bam -o output.fastq --no-gzip`
**Explanation:** Outputs uncompressed FASTQ file.

### Display help
**Args:** `bam2fastx --help`
**Explanation:** Shows all available command-line options and usage information.