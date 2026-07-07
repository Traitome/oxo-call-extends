---
name: anglerfish
category: utility
description: Anglerfish - Demultiplex Illumina libraries from Oxford Nanopore sequencing data
tags: [anglerfish, demultiplex, nanopore, Illumina, barcode]
author: oxo-call-community
source_url: "https://github.com/NationalGenomicsInfrastructure/anglerfish"
---

## Concepts

- **Tool Overview**: Anglerfish is a tool designed to demultiplex Illumina libraries sequenced on Oxford Nanopore flowcells. Version 0.7.0.
- **Core Function**: Demultiplexes Illumina libraries that have been sequenced on ONT platforms, enabling QC checks on pool balancing, contamination assessment, and library insert sizes.
- **Cross-Platform Sequencing**: Bridges Illumina library preparation with Nanopore sequencing, allowing Illumina libraries to be run on ONT flowcells for QC purposes.
- **Barcode Matching**: Uses edit distance-based barcode matching to identify samples, with configurable maximum distance thresholds.
- **Input/Output**: Input: Nanopore sequencing reads (FASTQ); Output: Demultiplexed FASTQ files per sample.
- **Installation**: Available via Bioconda (`conda install -c bioconda anglerfish`) or pip (`pip install bio-anglerfish`).

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted Nanopore FASTQ files with barcode sequences.
- **Barcode Quality**: Poor quality barcodes may lead to incorrect demultiplexing.
- **Edit Distance**: Default edit distance may need adjustment based on sequencing quality.
- **Run Name**: Ensure unique run names when processing multiple sequencing runs.
- **Demultiplexing Only**: Primarily designed for demultiplexing; additional QC may require other tools.

## Examples

### Display help
**Args:** `anglerfish --help`
**Explanation:** Shows available options and usage information.

### Basic demultiplexing
**Args:** `anglerfish -i reads.fastq -b barcodes.txt -o output_dir/`
**Explanation:** Demultiplexes Nanopore reads using provided barcode file. Outputs demultiplexed FASTQ files to output directory.

### Barcode counting only
**Args:** `anglerfish -i reads.fastq -b barcodes.txt -o output_dir/ --skip_demux`
**Explanation:** Performs only barcode counting without actual demultiplexing. Useful for quick QC assessment of pool balancing.

### Custom edit distance
**Args:** `anglerfish -i reads.fastq -b barcodes.txt -o output_dir/ -m 2`
**Explanation:** Sets maximum edit distance for barcode matching to 2. Allows more mismatches for lower quality data.

### Set run name
**Args:** `anglerfish -i reads.fastq -b barcodes.txt -o output_dir/ -r my_run`
**Explanation:** Sets custom run name for output files and reports. Helpful for organizing multiple sequencing runs.

### Debug mode
**Args:** `anglerfish -i reads.fastq -b barcodes.txt -o output_dir/ -d`
**Explanation:** Enables debug mode with extra command-line output for troubleshooting demultiplexing issues.

### Version information
**Args:** `anglerfish -v`
**Explanation:** Prints the current version of Anglerfish.