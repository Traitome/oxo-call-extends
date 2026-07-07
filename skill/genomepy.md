---
name: genomepy
category: genome-management
description: genomepy - Install and use genomes & gene annotations the easy way!
tags: [genomepy, genome-management, annotations, bioinformatics]
author: oxo-call-community
source_url: "https://vanheeringen-lab.github.io/genomepy"
---

## Concepts
- **Genome Installation**: Simplifies genome download and installation.
- **Annotation Management**: Manages gene annotations.
- **Data Integration**: Integrates genome data from multiple sources.
- **Genome Indexing**: Creates indexes for various tools.
- **Workflow Integration**: Integrates with bioinformatics workflows.

## Pitfalls
- **Network Dependency**: Requires network for genome downloads.
- **Storage Requirements**: Large genomes require significant storage.
- **Version Compatibility**: Requires compatible tool versions.
- **Data Integrity**: Requires data validation after download.
- **Configuration Complexity**: May require complex configuration.

## Examples
### Install genome
**Args:** `genomepy install hg38 -d ./genomes/`
**Explanation:** Installs hg38 genome to specified directory.

### List available genomes
**Args:** `genomepy search -k human`
**Explanation:** Searches for human genomes.

### Create index
**Args:** `genomepy index -g genome.fasta -b bowtie2`
**Explanation:** Creates Bowtie2 index for genome.

### Download annotations
**Args:** `genomepy install hg38 --annotation -d ./genomes/`
**Explanation:** Downloads genome with annotations.

### Batch installation
**Args:** `genomepy install -l genomes.txt -d ./genomes/`
**Explanation:** Installs multiple genomes from list.