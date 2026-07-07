---
name: assemblerflow
category: assembly
description: Assemblerflow - Modular Nextflow pipeline framework for genomics assembly
tags: [assemblerflow, assembly, nextflow, pipeline, modular, genomics]
author: oxo-call-community
source_url: "http://assemblerflow.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: Assemblerflow is a modular Nextflow pipeline framework for building and executing customizable genomics assembly workflows. Version 1.1.0.post3.
- **Core Function**: Provides a flexible framework for constructing genomics pipelines by selecting and combining pre-built modules.
- **Nextflow Integration**: Built on Nextflow for scalable, reproducible workflow execution across different compute environments.
- **Modular Design**: Components are organized as independent modules (read QC, assembly, polishing, annotation) that can be combined.
- **Customizable**: Users can pick specific modules to build tailored pipelines for different assembly needs.
- **Scalable**: Supports execution on local machines, clusters, and cloud environments through Nextflow's abstraction.
- **Input/Output**: Accepts sequencing reads (FASTQ), outputs assembled genomes with optional annotations.
- **Installation**: `conda install -c bioconda assemblerflow` or install from GitHub.

## Pitfalls

- **Nextflow Dependency**: Requires Nextflow to be installed and properly configured.
- **Module Compatibility**: Not all module combinations may work together. Check compatibility matrix.
- **Configuration**: Requires proper configuration file for module selection and parameters.
- **Resource Allocation**: Pipeline may require significant computational resources depending on modules selected.
- **Module Versions**: Individual modules may have version-specific requirements.
- **Data Format**: Input data must conform to expected formats for each module.

## Examples

### Display help
**Args:** `assemblerflow --help`
**Explanation:** Shows all available command-line options and module information.

### List available modules
**Args:** `assemblerflow modules list`
**Explanation:** Lists all available pipeline modules with descriptions.

### Run basic assembly pipeline
**Args:** `assemblerflow run --input reads.fastq --output results/ --modules qc,spades,quast`
**Explanation:** Runs pipeline with QC, SPAdes assembly, and QUAST quality assessment modules.

### Custom pipeline configuration
**Args:** `assemblerflow run --config config.yaml --output results/`
**Explanation:** Uses custom configuration file to define module selection and parameters.

### Add polishing step
**Args:** `assemblerflow run --input reads.fastq --output results/ --modules qc,spades,pilon,quast`
**Explanation:** Adds Pilon polishing step after assembly for improved accuracy.

### Specify module parameters
**Args:** `assemblerflow run --input reads.fastq --output results/ --modules spades --params spades:k=21,33,55`
**Explanation:** Passes specific parameters to SPAdes module (k-mer sizes).

### Run on cluster
**Args:** `assemblerflow run --input reads.fastq --output results/ --profile cluster --modules spades`
**Explanation:** Executes pipeline on cluster using configured cluster profile.

### Dry run mode
**Args:** `assemblerflow run --input reads.fastq --output results/ --modules spades --dry-run`
**Explanation:** Performs dry run to validate pipeline without actual execution.

### Generate pipeline diagram
**Args:** `assemblerflow visualize --modules qc,spades,quast --output pipeline.png`
**Explanation:** Generates visual diagram of pipeline workflow for documentation.