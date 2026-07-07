---
name: bcl2fastq-nextseq
category: qc
description: bcl2fastq-nextseq - Convert Illumina NextSeq BCL files to FASTQ format
tags: [bcl2fastq-nextseq, qc, FASTQ, Illumina, NextSeq]
author: oxo-call-community
source_url: "https://github.com/brwnj/bcl2fastq"
---

## Concepts

- **Tool Overview**: bcl2fastq-nextseq (v1.3.0) is a specialized tool for converting Illumina NextSeq BCL (base call) files to FASTQ format, optimized for NextSeq sequencing platform outputs.
- **Core Function**: Converts raw BCL files from Illumina NextSeq sequencers to standard FASTQ format with demultiplexing.
- **NextSeq Optimization**: Optimized specifically for NextSeq platform data characteristics.
- **Base Calling**: Converts intensity data to nucleotide sequences with Phred quality scores.
- **Demultiplexing**: Separates reads by sample using index sequences.
- **Input/Output**: Accepts Illumina BCL run folders; outputs FASTQ files.
- **Installation**: `conda install -c bioconda bcl2fastq-nextseq`.

## Pitfalls

- **NextSeq Specific**: Designed specifically for NextSeq platform; may not work with other Illumina platforms.
- **Run Folder Structure**: Requires complete NextSeq run folder structure.
- **Sample Sheet**: Requires properly formatted sample sheet with index information.
- **Index Mismatches**: Index mismatches may cause sample misassignment.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic conversion
**Args:** `bcl2fastq-nextseq --runfolder-dir run_folder/ --output-dir fastq/`
**Explanation:** Converts NextSeq BCL files to FASTQ format.

### Specify sample sheet
**Args:** `bcl2fastq-nextseq --runfolder-dir run_folder/ --sample-sheet samplesheet.csv --output-dir fastq/`
**Explanation:** Uses custom sample sheet for demultiplexing.

### No lane splitting
**Args:** `bcl2fastq-nextseq --runfolder-dir run_folder/ --no-lane-splitting --output-dir fastq/`
**Explanation:** Combines reads from all lanes into single files per sample.

### With trimming
**Args:** `bcl2fastq-nextseq --runfolder-dir run_folder/ --trim-adapters --output-dir fastq/`
**Explanation:** Trims adapter sequences during conversion.

### Custom quality cutoff
**Args:** `bcl2fastq-nextseq --runfolder-dir run_folder/ --quality-cutoff 20 --output-dir fastq/`
**Explanation:** Sets minimum quality cutoff for base calling.

### Output compressed FASTQ
**Args:** `bcl2fastq-nextseq --runfolder-dir run_folder/ --gzip --output-dir fastq/`
**Explanation:** Outputs gzip-compressed FASTQ files.

### Display help
**Args:** `bcl2fastq-nextseq --help`
**Explanation:** Shows all available command-line options and usage information.