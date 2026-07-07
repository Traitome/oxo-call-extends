---
name: comparem2
category: assembly
description: Genomes-to-report pipeline for metagenomic analysis
tags: [comparem2, metagenomics, genomes, pipeline, bioinformatics]
author: oxo-call-community
source_url: "https://comparem2.readthedocs.io"
---

## Concepts

- **Tool Overview**: CompareM2 is a comprehensive genomes-to-report pipeline for metagenomic analysis, providing automated workflows from raw sequencing data to final reports.
- **Core Function**: Processes metagenomic sequencing data through quality control, assembly, binning, annotation, and comparative analysis to generate comprehensive reports.
- **Algorithm**: Integrates multiple bioinformatics tools into a unified pipeline with standardized workflows and reporting.
- **Input**: Raw sequencing reads (FASTQ), optional reference databases.
- **Output**: Comprehensive analysis reports, assembled contigs, genome bins, and functional annotations.
- **Application**: Metagenomic analysis, microbial community characterization, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda comparem2`

## Pitfalls

- **Computational Resources**: Full pipeline requires significant computational resources.
- **Database Requirements**: May require large reference databases for comprehensive analysis.
- **Parameter Tuning**: Default parameters may not suit all sample types.
- **Quality Control**: Poor input quality affects downstream results.
- **Pipeline Version**: Tool versions within pipeline may change between releases.

## Examples

### Run full pipeline
**Args:** `comparem2 -i reads.fastq -o results/`
**Explanation:** Runs complete genomes-to-report pipeline on sequencing data.

### With custom database
**Args:** `comparem2 -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses custom reference database for analysis.

### Specific workflow step
**Args:** `comparem2 -i reads.fastq -s assembly -o results/`
**Explanation:** Runs only assembly step of the pipeline.

### Display help
**Args:** `comparem2 --help`
**Explanation:** Shows all available options and usage information.