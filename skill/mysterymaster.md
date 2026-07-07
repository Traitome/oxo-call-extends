---
name: mysterymaster
category: utility
description: MysteryMaster - Graphical Oxford Nanopore read demultiplexer
tags: [mysterymaster, utility, nanopore, demultiplexing, barcoding, graphical]
author: oxo-call-community
source_url: "https://bitbucket.org/NPC239/mysterymaster/src/main/"
---

## Concepts

- **Tool Overview**: MysteryMaster v0.0.8 is a graphical demultiplexing tool for Oxford Nanopore sequencing reads. It assigns reads to samples based on barcode information and provides visual feedback of demultiplexing results.
- **Core Function**: Reads FASTQ files from Nanopore sequencing runs with barcodes and sorts them into sample-specific output files. Features a graphical user interface for configuration and result visualization.
- **Demultiplexing Algorithm**: Uses barcode sequence matching to assign reads. Handles barcode errors within configurable thresholds and can use barcode-aware basecalling results from Guppy or MinKNOW.
- **Input Format**: Accepts FASTQ or gzipped FASTQ files from Nanopore runs. Requires a barcode manifest file defining the barcodes used in the experiment.
- **Output**: Produces sample-specific FASTQ files containing only reads assigned to each barcode. Also generates summary statistics of read counts per sample.
- **Use Case**: Nanopore barcoded sample demultiplexing, especially for multiplexed runs in clinical or research settings where multiple samples are barcoded and sequenced together.

## Pitfalls

- **Barcode Quality**: Poor barcode synthesis or ligation efficiency can lead to read assignment errors. Validate barcode quality before sequencing.
- **Barcode File Format**: Barcode definition file must be in the correct format. Mismatched formats cause all reads to fail demultiplexing.
- **GUI Dependency**: Runs with graphical interface by default. Requires X11 forwarding or GUI environment for headless servers.
- **Sequential Processing**: Large FASTQ files are processed sequentially, which can be slow. Consider splitting large files for parallel processing.
- **Adapter Contamination**: Reads with partial barcode sequences due to adapter contamination may not be assigned correctly.
- **Minimum Score Threshold**: Barcode minimum score thresholds affect assignment accuracy. Too strict loses reads, too permissive causes cross-contamination.

## Examples

### Basic demultiplexing
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir`
**Explanation:** Standard demultiplexing workflow. Reads input, assigns by barcode, and outputs sample-specific files.

### Specify barcode format
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o results/ -f standard`
**Explanation:** Uses standard barcode format. Other formats available depending on kit used.

### Set minimum barcode score
**Args:** `-i sample.fastq.gz -b barcode_manifest.tsv -o demuxed/ -s 60`
**Explanation:** Sets minimum barcode score threshold to 60 for read assignment. Higher values increase specificity.

### Run with verbose logging
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir -v`
**Explanation:** Enables detailed logging of barcode matching and read assignment decisions.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage instructions.
