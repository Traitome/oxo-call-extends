---
name: bcl2fastq
category: qc
description: bcl2fastq - Convert Illumina BCL files to FASTQ format
tags: [bcl-conversion, illumina, fastq, demultiplexing]
author: oxo-call-community
source_url: "https://support.illumina.com/sequencing/sequencing_software/bcl2fastq-conversion-software.html"
---

## Concepts

- **Tool Overview**: bcl2fastq converts Illumina BCL (base call) files to FASTQ format, performing base calling and demultiplexing.

- **Base Calling**: Converts raw intensity data to nucleotide sequences with quality scores.

- **Demultiplexing**: Separates reads by sample using index sequences.

- **Quality Scoring**: Assigns Phred quality scores to each base.

## Pitfalls

- **Sample Sheet**: Requires correct sample sheet with index information.

- **Run Folder**: Needs complete Illumina run folder structure.

- **Index Mismatches**: Index mismatches may cause sample misassignment.

## Examples

### Basic conversion
**Args:** `bcl2fastq --runfolder-dir run_folder/ --output-dir fastq/`
**Explanation:** Converts BCL files to FASTQ with automatic demultiplexing.

### Specify sample sheet
**Args:** `bcl2fastq --runfolder-dir run_folder/ --sample-sheet samplesheet.csv --output-dir fastq/`
**Explanation:** Uses custom sample sheet for demultiplexing.

### No lane splitting
**Args:** `bcl2fastq --runfolder-dir run_folder/ --no-lane-splitting --output-dir fastq/`
**Explanation:** Combines reads from all lanes into single files per sample.
