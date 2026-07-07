---
name: cenmap
category: genome-annotation
description: Centromere mapping and annotation pipeline for T2T human and primate genome assemblies
tags: [cenmap, centromere, mapping, annotation, snakemake, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/logsdon-lab/CenMAP/blob/v1.2.0/README.md"
---

## Concepts

- **Tool Overview**: CenMAP is a Snakemake pipeline for centromere mapping and annotation in T2T genome assemblies.
- **Core Function**: Identifies and annotates centromeric regions using satellite repeat analysis.
- **Algorithm**: Uses satellite repeat detection and sequence alignment for centromere identification.
- **Input**: Complete genome assembly in FASTA format.
- **Output**: Centromere annotations in GFF/bed format and analysis reports.
- **Application**: Centromere annotation in complete genome assemblies.
- **Installation**: Install via bioconda: `conda install -c bioconda cenmap`

## Pitfalls

- **Assembly Quality**: Requires high-quality T2T genome assemblies.
- **Satellite Repeats**: May have difficulty with highly repetitive regions.
- **Reference Dependencies**: Requires appropriate reference data for centromere detection.
- **Computational Resources**: Large genomes may require significant compute.

## Examples

### Run centromere annotation pipeline
**Args:** `cenmap run --genome genome.fasta --output results/`
**Explanation:** Runs complete centromere mapping pipeline.

### Generate configuration file
**Args:** `cenmap config --output config.yaml`
**Explanation:** Generates template configuration file.

### Run with custom config
**Args:** `cenmap run --config config.yaml`
**Explanation:** Runs pipeline with custom configuration.

### Display help
**Args:** `cenmap --help`
**Explanation:** Shows all available commands and options.