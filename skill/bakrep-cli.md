---
name: bakrep-cli
category: utility
description: BakRep-CLI - Commandline tool for batch download of BakRep datasets
tags: [bakrep-cli, utility, data-download, bacterial-genomics, dataset-management]
author: oxo-call-community
source_url: "https://github.com/ag-computational-bio/bakrep-cli/blob/v1.1.0/README.md"
---

## Concepts

- **Tool Overview**: BakRep-CLI is a command-line tool for batch downloading bacterial genome datasets from the BakRep database. Version 1.1.0.
- **Core Function**: Facilitates batch downloading of bacterial genome assemblies and related data from BakRep repository.
- **Batch Download**: Supports downloading multiple datasets in a single operation.
- **Data Filtering**: Allows filtering datasets by species, assembly quality, and other criteria.
- **Dataset Management**: Organizes downloaded datasets into structured directory layouts.
- **Input/Output**: Accepts dataset lists or filter criteria, outputs downloaded genome files.
- **Installation**: `conda install -c bioconda bakrep-cli`.

## Pitfalls

- **Network Dependency**: Requires stable internet connection for downloading large datasets.
- **Storage Requirements**: Genome datasets can be large. Ensure sufficient disk space.
- **Version Compatibility**: Database structure may change. Update tool regularly.
- **Authentication**: Some datasets may require authentication or API keys.
- **Data Quality**: Verify downloaded data integrity after download.

## Examples

### Download specific dataset
**Args:** `bakrep-cli download --id GCF_000001405.39 --output genomes/`
**Explanation:** Downloads specific genome assembly by NCBI accession.

### Batch download by species
**Args:** `bakrep-cli download --species "Escherichia coli" --output ecoli_genomes/`
**Explanation:** Downloads all Escherichia coli genomes from BakRep.

### Filter by assembly quality
**Args:** `bakrep-cli download --species "Staphylococcus aureus" --quality complete --output saureus_complete/`
**Explanation:** Downloads only complete genome assemblies for specified species.

### Download with metadata
**Args:** `bakrep-cli download --species "Salmonella enterica" --include-metadata --output salmonella/`
**Explanation:** Downloads genomes along with associated metadata files.

### List available datasets
**Args:** `bakrep-cli list --species "Pseudomonas aeruginosa"`
**Explanation:** Lists all available datasets for specified species.

### Download multiple accessions
**Args:** `bakrep-cli download --accessions accessions.txt --output genomes/`
**Explanation:** Downloads all genomes listed in accessions.txt file.

### Check dataset status
**Args:** `bakrep-cli status --id GCF_000001405.39`
**Explanation:** Checks availability and metadata for specific dataset.

### Display help
**Args:** `bakrep-cli --help`
**Explanation:** Shows all available command-line options and usage information.