---
name: metagenome-atlas
category: alignment
description: ATLAS - Three commands to start analysing your metagenome data
tags: [metagenome-atlas, alignment, sequence, alignment]
author: oxo-call-community
source_url: "https://github.com/metagenome-atlas"
---

## Concepts

- **Tool Overview**: metagenome-atlas v19.0.1 - Atlas is a easy to use metagenomic pipeline   Three commands to start analysing your metagenome data: ```     mamba install -c bioconda -c conda-forge metagenome-atlas     atlas init --db-dir databases path/to/fastq/files     atlas run ``` All databases and dependencies are installed on the fly in the directory `db-dir`. You want to run these three commands on the example_data on the GitHub repo. If you have more time, then we recommend you configure atlas according to your needs.   - check the `samples.tsv`   - edit the `config.yaml`   - run atlas on any cluster system For more details see documentation..
- **Core Function**: ATLAS - Three commands to start analysing your metagenome data
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metagenome-atlas`

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
