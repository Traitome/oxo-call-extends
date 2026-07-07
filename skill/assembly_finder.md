---
name: assembly_finder
category: assembly
description: Assembly Finder - Snakemake-powered pipeline to download genomes from NCBI
tags: [assembly_finder, assembly, ncbi, genome-download, snakemake]
author: oxo-call-community
source_url: "https://metagenlab.github.io/assembly_finder"
---

## Concepts

- **Tool Overview**: Assembly Finder is a Snakemake-powered command-line pipeline for downloading genome assemblies from NCBI Datasets. Version 0.9.0.
- **Core Function**: Automates genome assembly retrieval from NCBI using NCBI Datasets API with configurable filters.
- **Snakemake Integration**: Built on Snakemake for reproducible, scalable workflow execution.
- **NCBI Datasets**: Uses NCBI Datasets API for reliable genome data retrieval.
- **Filtering Options**: Supports filtering by organism, assembly level, completeness, and other criteria.
- **Batch Download**: Enables downloading multiple genomes in parallel.
- **Input/Output**: Accepts organism names or NCBI accessions, outputs FASTA genome files with metadata.
- **Installation**: `conda install -c bioconda assembly_finder` or install from GitHub.

## Pitfalls

- **Network Dependency**: Requires internet connection for NCBI API access.
- **API Rate Limits**: NCBI API has rate limits. May need to throttle requests.
- **Organism Names**: Requires accurate organism names. Ambiguous names may return incorrect results.
- **Assembly Availability**: Not all organisms have complete genome assemblies available.
- **Data Size**: Downloading multiple large genomes requires significant storage space.
- **Snakemake Requirements**: Requires Snakemake to be installed and properly configured.

## Examples

### Display help
**Args:** `assembly_finder --help`
**Explanation:** Shows all available command-line options and usage information.

### Download single organism genome
**Args:** `assembly_finder --organism "Escherichia coli" --output genomes/`
**Explanation:** Downloads E. coli genome assembly to specified output directory.

### Download multiple organisms
**Args:** `assembly_finder --organism "Escherichia coli" "Salmonella enterica" --output genomes/`
**Explanation:** Downloads genomes for multiple organisms in parallel.

### Filter by assembly level
**Args:** `assembly_finder --organism "Homo sapiens" --assembly-level complete --output genomes/`
**Explanation:** Downloads only complete genome assemblies for human.

### Download by accession
**Args:** `assembly_finder --accession GCF_000005845.2 --output genomes/`
**Explanation:** Downloads specific genome assembly by NCBI accession number.

### Set output format
**Args:** `assembly_finder --organism "Escherichia coli" --output genomes/ --format fasta,gbff`
**Explanation:** Downloads genome in both FASTA and GenBank flat file formats.

### Include annotation
**Args:** `assembly_finder --organism "Escherichia coli" --output genomes/ --include-annotation`
**Explanation:** Downloads genome sequence along with annotation data.

### Dry run mode
**Args:** `assembly_finder --organism "Escherichia coli" --output genomes/ --dry-run`
**Explanation:** Shows what would be downloaded without actually downloading.

### Custom configuration
**Args:** `assembly_finder --config config.yaml --output genomes/`
**Explanation:** Uses custom YAML configuration file for advanced options.

### Parallel downloads
**Args:** `assembly_finder --organism "Escherichia coli" "Salmonella enterica" --output genomes/ --threads 4`
**Explanation:** Uses 4 threads for parallel downloading of multiple genomes.