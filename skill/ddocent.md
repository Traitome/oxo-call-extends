---
name: ddocent
category: variant-calling
description: Interactive bash wrapper for RAD-seq data processing including QC, assembly, mapping, and SNP calling.
tags: [ddocent, variant-calling, RAD-seq, SNP, population-genetics]
author: oxo-call-community
source_url: "https://www.ddocent.com/UserGuide/"
---

## Concepts

- **Tool Overview**: ddocent (v2.9.8+) is a pipeline for processing RAD-seq (Restriction-site Associated DNA sequencing) data. It provides an interactive wrapper for quality control, de novo assembly, read mapping, and variant calling.
- **Core Function**: Processes RAD-seq data from raw reads through variant calling, including quality filtering, assembly of reference sequences, alignment, and SNP/indel detection.
- **Input/Output**: Input: Demultiplexed FASTQ reads from RAD-seq. Output: VCF files with variants, assembled reference, alignment files.
- **Algorithm**: Integrates multiple tools (FastQC, Trimmomatic, Rainbow, BWA, FreeBayes, VCFtools) into a streamlined pipeline with sensible defaults for RAD data.
- **Key Features**: Interactive configuration, automatic parameter optimization, handles paired-end RAD data, population genetics filtering, produces analysis-ready VCFs.
- **Installation**: `conda install -c bioconda ddocent`

## Pitfalls

- **Interactive Mode**: Requires user input during pipeline execution.
- **Memory Requirements**: Large datasets may require significant memory.
- **Parameter Selection**: Default parameters may not be optimal for all organisms.
- **Reference Quality**: De novo assembly quality affects downstream variant calling.
- **Population Structure**: Filtering parameters should consider population structure.

## Examples

### Run full pipeline
**Args:** `dDocent`
**Explanation:** Launch interactive dDocent pipeline for RAD-seq processing.

### Specify input directory
**Args:** `dDocent -i raw_reads/ -o output/`
**Explanation:** Run pipeline with specified input and output directories.

### Use custom parameters
**Args:** `dDocent --trim-left 5 --trim-right 5 --min-coverage 5`
**Explanation:** Run with custom trimming and coverage parameters.