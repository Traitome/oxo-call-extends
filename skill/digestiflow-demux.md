---
name: digestiflow-demux
category: utility
description: digestiflow-demux - Demultiplexing module for Digestiflow workflow.
tags: [digestiflow-demux, utility, demultiplexing, workflow]
author: oxo-call-community
source_url: "https://github.com/bihealth/digestiflow-demux"
---

## Concepts

- **Tool Overview**: digestiflow-demux is the demultiplexing component of the Digestiflow workflow system for sequencing data.
- **Core Function**: Demultiplexes raw sequencing data into individual sample files as part of the Digestiflow processing pipeline.
- **Input/Output**: Input: Raw sequencing files (FASTQ), sample sheet with barcode information. Output: Demultiplexed FASTQ files per sample.
- **Algorithm**: Uses sample barcodes to assign reads to specific samples, supporting various barcode configurations.
- **Key Features**: Illumina demultiplexing, barcode matching, quality filtering, sample sheet parsing, batch processing.
- **Installation**: `conda install -c bioconda digestiflow-demux`

## Pitfalls

- **Barcode Quality**: Requires high-quality barcodes for accurate demultiplexing.
- **Sample Sheet**: Sample sheet must be properly formatted with barcode information.
- **Input Requirements**: Requires raw sequencing data with intact barcodes.
- **Mismatch Tolerance**: Barcode mismatches can lead to incorrect sample assignment.
- **Output Volume**: Large number of samples can produce many output files.

## Examples

### Demultiplex sequencing data
**Args:** `digestiflow-demux --input raw_data/ --output demux/`
**Explanation:** Demultiplexes sequencing data in Digestiflow workflow.

### With sample sheet
**Args:** `digestiflow-demux --input raw_data/ --output demux/ --samplesheet samples.csv`
**Explanation:** Use sample sheet for barcode-to-sample mapping.

### Allow barcode mismatches
**Args:** `digestiflow-demux --input raw_data/ --output demux/ --mismatches 1`
**Explanation:** Allow 1 barcode mismatch during demultiplexing.

### Quality filtering
**Args:** `digestiflow-demux --input raw_data/ --output demux/ --quality-threshold 20`
**Explanation:** Apply quality threshold for barcode trimming.

### Generate report
**Args:** `digestiflow-demux --input raw_data/ --output demux/ --report demux_report.html`
**Explanation:** Generate demultiplexing statistics report.