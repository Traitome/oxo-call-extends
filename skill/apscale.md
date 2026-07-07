---
name: apscale
category: metabarcoding
description: APSCALE - Advanced Pipeline for Simple yet Comprehensive AnaLysEs of DNA metabarcoding data
tags: [apscale, metabarcoding, bioinformatics-pipeline, biodiversity, DNA-sequencing]
author: oxo-call-community
source_url: "https://github.com/DominikBuchner/apscale"
---

## Concepts

- **Tool Overview**: APSCALE (v4.3.0) - A comprehensive DNA metabarcoding pipeline designed for processing high-throughput sequencing data for biodiversity assessment.
- **Core Function**: Handles paired-end merging, primer trimming, quality filtering, denoising, clustering, and basic data operations like replicate merging and negative control filtering.
- **Key Features**:
  - **Paired-end Merging**: Combines overlapping paired-end reads
  - **Primer Trimming**: Removes primer sequences using cutadapt
  - **Quality Filtering**: Filters low-quality reads
  - **Denoising**: Error correction and chimera removal using vsearch
  - **Clustering**: Supports swarm and threshold-based OTU clustering
  - **Replicate Merging**: Merges technical/biological replicates
  - **Negative Control Removal**: Filters reads found in negative controls
- **Integrated Tools**:
  - vsearch: PE merging, quality filtering, denoising, chimera removal
  - cutadapt: Primer trimming
  - swarm: Swarm clustering (optional)
  - LULU: OTU filtering
- **Input**: Demultiplexed gzipped FASTQ reads
- **Output**: Log files, project report, ESV/OTU tables
- **Applications**: Biodiversity assessment, ecological monitoring, microbial community profiling
- **Installation**: `conda install -c bioconda apscale` or `pip install apscale`

## Pitfalls

- **External Dependencies**: Requires vsearch and swarm to be installed and in PATH
- **Configuration File**: Requires proper configuration file setup for most operations
- **Memory Usage**: May require significant memory for large datasets
- **Threading**: Optimal thread count depends on available system resources
- **Data Protection**: Designed to run locally to comply with data protection regulations

## Examples

### Create new project
**Args:** `apscale create --name my_project --input_dir /path/to/reads/`
**Explanation:** Creates a new apscale project with raw reads directory.

### Run full pipeline
**Args:** `apscale run --config config.yaml`
**Explanation:** Runs the complete metabarcoding pipeline using configuration file.

### Add metadata via browser interface
**Args:** `apscale metadata --name my_project`
**Explanation:** Opens browser-based interface for metadata addition (v4.0+).

### Run specific module
**Args:** `apscale trim --name my_project --primers primers.fasta`
**Explanation:** Runs only the primer trimming module.

### Merge replicates
**Args:** `apscale merge_replicates --name my_project --groups groups.csv`
**Explanation:** Merges biological/technical replicates based on grouping file.

### Help documentation
**Args:** `apscale --help`
**Explanation:** Shows available commands and options.