---
name: flowcraft
category: hpc
description: "Flowcraft is a Nextflow pipeline assembler for genomics that allows modular pipeline construction and execution."
tags: [flowcraft, hpc, nextflow, pipeline, genomics, bioinformatics, workflow]
author: oxo-call-community
source_url: "https://github.com/assemblerflow/flowcraft"
---

## Concepts
- **Tool Overview**: Flowcraft is a modular pipeline framework built on Nextflow that enables construction and execution of bioinformatics workflows for genomics analysis.
- **Core Function**: Assembles modular pipeline components into complete workflows for genomic data processing and analysis.
- **Input/Output**: Input: Sequencing data (FASTQ), configuration files. Output: Analysis results, reports, processed data.
- **Modular Architecture**: Components (modules) can be combined in various ways to create custom pipelines.
- **Nextflow Integration**: Leverages Nextflow's parallel execution and reproducibility features.
- **Pipeline Templates**: Provides pre-built pipelines for common genomics tasks like assembly, variant calling, and RNA-Seq.
- **Installation**: `conda install -c bioconda flowcraft` or clone from GitHub. Requires Nextflow and Python 3.x.

## Pitfalls
- **Nextflow Version**: Requires compatible Nextflow version. Check compatibility before installation.
- **Module Compatibility**: Modules must be compatible with each other. Incompatible modules cause pipeline failures.
- **Configuration Complexity**: Complex pipelines require careful configuration. Validate config files before running.
- **Resource Requirements**: Pipeline components may have specific resource requirements. Adjust accordingly.
- **Dependency Conflicts**: Conda environment conflicts can cause pipeline failures. Use isolated environments.
- **Error Handling**: Pipeline errors require careful debugging. Use Nextflow's logging for troubleshooting.

## Examples
### Create new pipeline project
**Args:** `flowcraft init my_pipeline`
**Explanation:** Creates a new pipeline project directory with basic structure.

### Run pre-built pipeline
**Args:** `flowcraft run assembly --input reads.fastq --output results/`
**Explanation:** Runs pre-built assembly pipeline on input reads.

### Add module to pipeline
**Args:** `flowcraft add spades_assembler`
**Explanation:** Adds SPAdes assembler module to current pipeline.

### Configure pipeline
**Args:** `flowcraft config --set 'params.reads="*.fastq"'`
**Explanation:** Sets configuration parameters for the pipeline.

### Test pipeline
**Args:** `flowcraft test --profile test`
**Explanation:** Runs pipeline with test data to verify functionality.
