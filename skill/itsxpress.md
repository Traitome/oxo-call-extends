---
name: itsxpress
category: qc
description: Rapidly trims the Internally Transcribed Spacer (ITS) region from FASTQ files.
tags: [itsxpress, qc, FASTQ, ITS, trimming]
author: oxo-call-community
source_url: "http://github.com/usda-ars-gbru/itsxpress"
---

## Concepts

- **ITS Trimming**: Rapidly trims ITS regions from raw FASTQ sequencing data.
- **Quality Control**: Removes low-quality bases from ITS sequences.
- **Paired-End Support**: Optimized for paired-end sequencing data.
- **Taxonomic Filtering**: Supports filtering by taxonomic group.
- **Multiple Regions**: Handles ITS1, ITS2, and full ITS regions.
- **Fast Processing**: Optimized for speed with large sequencing datasets.

## Pitfalls

- **Read Quality**: Poor quality reads affect trimming accuracy.
- **Adapter Contamination**: Adapter sequences should be removed first.
- **Read Length**: Short reads may not contain complete ITS regions.
- **Paired-End Synchronization**: Requires properly paired reads.
- **Memory Requirements**: Processing large datasets requires significant memory.
- **Parameter Tuning**: Optimal parameters may vary between datasets.

## Examples

### Basic ITS trimming
**Args:** `itsxpress --input R1.fastq R2.fastq --output trimmed/`
**Explanation:** Trims ITS regions from paired-end FASTQ files.

### Specify ITS region
**Args:** `itsxpress --input R1.fastq R2.fastq --region ITS2 --output trimmed/`
**Explanation:** Trims only the ITS2 region from reads.

### Taxonomic filtering
**Args:** `itsxpress --input R1.fastq R2.fastq --taxa Fungi --output trimmed/`
**Explanation:** Filters and trims fungal ITS sequences.

### Quality filtering
**Args:** `itsxpress --input R1.fastq R2.fastq --min-quality 20 --output trimmed/`
**Explanation:** Applies quality filtering during trimming.

### Single-end mode
**Args:** `itsxpress --single-end --input reads.fastq --output trimmed.fastq`
**Explanation:** Processes single-end sequencing data.

### Batch processing
**Args:** `itsxpress --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple samples in batch mode.