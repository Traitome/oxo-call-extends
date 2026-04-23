---
name: atol-genome-launcher
category: assembly
description: AToL Genome Launcher - Launch genome assemblies and annotations from ingested metadata
tags: [genome-engine, pipeline-launcher, assembly, annotation]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-genome-launcher"
---

## Concepts

- **Tool Overview**: Launches genome assembly and annotation pipelines based on metadata ingested by atol-bpa-datamapper in AToL Genome Engine.

- **Pipeline Selection**: Automatically selects appropriate assembly and annotation pipelines based on data type and quality.

- **Parameter Configuration**: Configures pipeline parameters based on metadata (read type, genome size, coverage).

- **Workflow Management**: Integrates with workflow managers for reproducible pipeline execution.

## Pitfalls

- **Resource Requirements**: Assembly pipelines require significant CPU and memory. Ensure adequate resources.

- **Parameter Tuning**: Default parameters may not be optimal for all organisms. Review and adjust as needed.

- **Dependency Installation**: Requires all pipeline dependencies installed. Use containers for reproducibility.

## Examples

### Launch assembly pipeline
**Args:** `atol-genome-launcher --metadata mapped_data.tsv --pipeline assembly --output assembly_results/`
**Explanation:** Launches genome assembly pipeline using mapped metadata.

### Launch annotation pipeline
**Args:** `atol-genome-launcher --metadata mapped_data.tsv --pipeline annotation --genome assembly.fasta --output annotation_results/`
**Explanation:** Launches annotation pipeline on completed assembly.

### Specify custom parameters
**Args:** `atol-genome-launcher --metadata mapped_data.tsv --pipeline assembly --params genome_size=5m,threads=16 --output results/`
**Explanation:** Launches assembly with custom parameters for genome size and thread count.

### Dry run
**Args:** `atol-genome-launcher --metadata mapped_data.tsv --pipeline assembly --dry-run`
**Explanation:** Shows what would be executed without actually running the pipeline.
