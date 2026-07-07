---
name: asqcan
category: assembly
description: ASQcan - Combined pipeline for bacterial genome assembly, quality control and annotation
tags: [asqcan, assembly, bacterial-genomics, quality-control, annotation, pipeline]
author: oxo-call-community
source_url: "https://github.com/bogemad/asqcan"
---

## Concepts

- **Tool Overview**: ASQcan is an integrated pipeline for bacterial genome analysis combining assembly, quality control, and annotation into a single workflow. Version 0.4.
- **Core Function**: Automates the complete bacterial genome analysis workflow from raw reads to annotated genome.
- **Assembly**: Uses SPAdes or other assemblers for de novo genome assembly.
- **Quality Control**: Assesses assembly quality using multiple metrics (N50, completeness, contamination).
- **Annotation**: Performs gene prediction and functional annotation using Prokka or similar tools.
- **Pipeline Integration**: Combines multiple tools into cohesive workflow with automatic file handling.
- **Bacterial Focus**: Optimized specifically for bacterial genomes. May not work well for eukaryotes.
- **Input/Output**: Accepts raw sequencing reads (FASTQ), outputs assembled and annotated genome.
- **Installation**: `conda install -c bioconda asqcan` or install from GitHub.

## Pitfalls

- **Bacterial Specific**: Designed for bacterial genomes only. Not suitable for eukaryotic assemblies.
- **Read Quality**: Requires high-quality sequencing reads. Poor quality reads produce poor assemblies.
- **Assembly Parameters**: Default parameters may not work for all datasets. May need tuning.
- **Resource Requirements**: Assembly step requires significant memory for large bacterial genomes.
- **Annotation Databases**: Requires up-to-date annotation databases. Outdated databases produce poor annotations.
- **Complete Genomes**: Works best with near-complete genomes. Highly fragmented assemblies may cause issues.

## Examples

### Display help
**Args:** `asqcan --help`
**Explanation:** Shows all available command-line options and usage information.

### Run complete pipeline
**Args:** `asqcan --input reads_1.fastq reads_2.fastq --output results/ --species "E. coli"`
**Explanation:** Runs complete pipeline from raw reads to annotation. Specifies species for better annotation.

### Skip annotation step
**Args:** `asqcan --input reads_1.fastq reads_2.fastq --output results/ --skip-annotation`
**Explanation:** Runs assembly and QC only, skips annotation step. Useful for quick assembly assessment.

### Specify assembler
**Args:** `asqcan --input reads_1.fastq reads_2.fastq --output results/ --assembler spades`
**Explanation:** Uses SPAdes assembler instead of default. Other options may include flye, shovill.

### Set coverage cutoff
**Args:** `asqcan --input reads_1.fastq reads_2.fastq --output results/ --min-coverage 20`
**Explanation:** Sets minimum coverage threshold of 20x. Filters out low-coverage regions.

### Multi-threaded processing
**Args:** `asqcan --input reads_1.fastq reads_2.fastq --output results/ -t 16`
**Explanation:** Uses 16 threads for parallel processing. Speeds up assembly and annotation.

### Generate QC report
**Args:** `asqcan --input reads_1.fastq reads_2.fastq --output results/ --qc-report qc.html`
**Explanation:** Generates HTML quality control report with assembly metrics and visualization.

### Use existing assembly
**Args:** `asqcan --assembly contigs.fasta --output results/ --skip-assembly`
**Explanation:** Uses pre-assembled contigs, runs only QC and annotation steps.

### Batch processing
**Args:** `asqcan --input-dir raw_reads/ --output-dir results/ --batch`
**Explanation:** Processes multiple samples in batch mode. Automatically detects paired-end read files.