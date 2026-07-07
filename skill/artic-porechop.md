---
name: artic-porechop
category: qc
description: Artic-Porechop - Adapter removal and demultiplexing of Oxford Nanopore reads
tags: [artic-porechop, qc, nanopore, adapter-removal, demultiplexing]
author: oxo-call-community
source_url: "https://github.com/artic-network/Porechop"
---

## Concepts

- **Tool Overview**: Artic-Porechop is a fork of Porechop for adapter removal and demultiplexing of Oxford Nanopore reads, specifically optimized for ARTIC pipeline. Version 0.3.2pre.
- **Core Function**: Identifies and removes adapter sequences from nanopore reads and demultiplexes barcoded samples.
- **Adapter Detection**: Uses alignment-based approach to identify adapter sequences at read ends.
- **Demultiplexing**: Separates barcoded reads into individual sample files based on barcode sequences.
- **ARTIC Optimization**: Tuned for ARTIC primer schemes and barcoding strategies used in viral sequencing.
- **Nanopore Specific**: Designed for long-read characteristics of Oxford Nanopore sequencing.
- **Input/Output**: Accepts FASTQ files and outputs trimmed/demultiplexed FASTQ files.
- **Installation**: `conda install -c bioconda artic-porechop` or install from GitHub.

## Pitfalls

- **Barcode Detection**: Barcode detection accuracy depends on barcode quality and read length. Poor quality barcodes cause misassignment.
- **Adapter Variants**: Some adapter variants may not be recognized. Custom adapter sequences may be needed.
- **Read Length**: Very short reads may not contain complete barcode sequences.
- **Overlap Handling**: Overlapping amplicons may cause adapter detection issues in ARTIC workflows.
- **Memory Usage**: Large FASTQ files require significant memory for processing.

## Examples

### Display help
**Args:** `artic-porechop --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic adapter trimming
**Args:** `artic-porechop -i input.fastq -o trimmed.fastq`
**Explanation:** Removes adapter sequences from nanopore reads. Outputs trimmed reads.

### Demultiplex barcoded reads
**Args:** `artic-porechop -i barcoded.fastq -b output_dir/ --barcode_kits EXP-NBD104`
**Explanation:** Demultiplexes barcoded reads using EXP-NBD104 barcode kit. Outputs separate files for each barcode.

### Specify adapter sequences
**Args:** `artic-porechop -i input.fastq -o trimmed.fastq --adapter_file adapters.fasta`
**Explanation:** Uses custom adapter sequences from FASTA file for detection and removal.

### Set barcode threshold
**Args:** `artic-porechop -i barcoded.fastq -b output_dir/ --barcode_threshold 0.7`
**Explanation:** Sets barcode detection threshold to 0.7. Higher threshold reduces false assignments.

### Disable demultiplexing
**Args:** `artic-porechop -i input.fastq -o trimmed.fastq --no_demultiplex`
**Explanation:** Performs adapter trimming only without demultiplexing. Useful for non-barcoded samples.

### Report adapter statistics
**Args:** `artic-porechop -i input.fastq -o trimmed.fastq --report adapter_report.txt`
**Explanation:** Generates report of adapter detection statistics including adapter types and positions.

### Multi-threaded processing
**Args:** `artic-porechop -i input.fastq -o trimmed.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing to speed up adapter removal.