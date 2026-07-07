---
name: cgecore
category: genomics
description: Center for Genomic Epidemiology Core Module for bacterial genomic analysis
tags: [cgecore, genomic-epidemiology, bacteria, typing, bioinformatics]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/cge_core_module"
---

## Concepts

- **Tool Overview**: CGE Core is the central module for the Center for Genomic Epidemiology tools, providing common utilities for bacterial genomic analysis.
- **Core Function**: Provides shared functionality for sequence typing, annotation, and analysis in genomic epidemiology.
- **Features**: Sequence processing, database management, typing methods, and result visualization.
- **Input**: Bacterial genome sequences in FASTA format.
- **Output**: Typing results, annotation data, and analysis reports.
- **Application**: Bacterial identification, antimicrobial resistance detection, and genomic epidemiology.
- **Installation**: Install via bioconda: `conda install -c bioconda cgecore`

## Pitfalls

- **Database Updates**: Requires regular database updates for accurate typing.
- **Sequence Quality**: Poor quality sequences may affect typing accuracy.
- **Reference Databases**: Must use appropriate reference databases.
- **Computational Resources**: Large datasets may require significant memory.

## Examples

### Initialize CGE analysis
**Args:** `cgecore init --db-path databases/`
**Explanation:** Initializes CGE core with database path.

### Run MLST typing
**Args:** `cgecore mlst --input genome.fasta --output results/`
**Explanation:** Performs MLST typing on bacterial genome.

### Check database status
**Args:** `cgecore db-status`
**Explanation:** Checks status of reference databases.

### Display help
**Args:** `cgecore --help`
**Explanation:** Shows all available options and usage information.