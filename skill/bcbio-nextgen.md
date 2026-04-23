---
name: bcbio-nextgen
category: variant-calling
description: bcbio-nextgen - Validated, scalable pipeline for variant calling, RNA-seq, and small RNA analysis
tags: [pipeline, variant-calling, rna-seq, small-rna, automated-analysis]
author: oxo-call-community
source_url: "https://github.com/bcbio/bcbio-nextgen"
---

## Concepts

- **Tool Overview**: bcbio-nextgen provides validated, scalable, community-developed pipelines for variant calling, RNA-seq, and small RNA analysis.

- **Automated Pipelines**: Fully automated workflows from raw reads to final analysis with best practices.

- **Multiple Analyses**: Supports germline and somatic variant calling, RNA-seq, small RNA-seq, and more.

- **Scalability**: Runs on local machines, clusters, and cloud platforms.

- **Community Developed**: Continuously updated with community contributions and validation.

- **Container Support**: Uses Docker/Singularity containers for reproducibility.

## Pitfalls

- **Installation**: Complex installation with many dependencies. Use automated installer.

- **Configuration**: Requires proper YAML configuration. Use bcbio_setup_genome.py for setup.

- **Resource Requirements**: Full pipelines require substantial CPU and memory.

- **Template System**: Uses template system for configuration. Understand template structure.

## Examples

### Run pipeline
**Args:** `bcbio_nextgen.py config.yaml workdir/`
**Explanation:** Runs bcbio pipeline with specified configuration.

### Setup genome reference
**Args:** `bcbio_setup_genome.py -f genome.fasta -g gff.gff3 -i config.yaml`
**Explanation:** Creates genome reference configuration for pipeline.

### Upgrade installation
**Args:** `bcbio_nextgen.py upgrade --tooldir=/path/to/tools`
**Explanation:** Upgrades bcbio installation and tools.

### Generate configuration
**Args:** `bcbio_nextgen.py -w template config.yaml sample1.bam sample2.bam`
**Explanation:** Generates configuration from template and input files.

### Validate installation
**Args:** `bcbio_nextgen.py validate --config config.yaml`
**Explanation:** Validates bcbio installation and configuration.

### Run with specific cores
**Args:** `bcbio_nextgen.py config.yaml workdir/ -n 16`
**Explanation:** Uses 16 cores for parallel processing.
