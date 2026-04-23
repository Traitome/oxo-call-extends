---
name: mitosalt
category: utility
description: MitoSAlt is a pipeline to identify large deletions and duplications in human and mouse mitochondrial genomes from next generation whole genome/exome sequencing data. The pipeline is capable of analyzing any circular genome in principle, as long as a proper configuration file is provided.
tags: [mitosalt, utility, sequence]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/mitosalt/"
---

## Concepts

- **Tool Overview**: mitosalt v1.1.1 - This mitosalt version:  - lets us choose the destination folder of the reference genomes and indices   - `export MITOSALT_DATA=/path/to/mitosalt/genomedata` - downloads user-selected reference genomes and builds indices   - `download-mitosalt-db.sh -h [human_genome_url, blank for custom hg19 genome]`   - `download-mitosalt-db.sh -m [mouse_genome_url, blank for custom GRCm38.p6 genome]`   - `download-mitosalt-db.sh -h [human_genome_url, blank for custom hg19 genome] -m [mouse_genome_url, blank for custom GRCm38.p6 genome]` - runs the pipeline with paired-end reads   - `mitosalt.pl <config_file> <fastq file 1> <fastq file 2> <study name>` - runs the pipeline with single-end reads   - `mitosalt_se.pl <config_file> <fastq file> <study name>` - provides configuration file template in the package at `$CONDA_PREFIX/share/mitosalt-1.1.1-3/`.
- **Core Function**: MitoSAlt is a pipeline to identify large deletions and duplications in human and mouse mitochondrial genomes from next generation whole genome/exome sequencing data. The pipeline is capable of analyzing any circular genome in principle, as long as a proper configuration file is provided.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mitosalt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
