---
name: orthoflow
category: formatting
description: OrthoFlow is a workflow for phylogenetic inference of genome-scale datasets.
tags: [orthoflow, formatting, phylogenetics, workflow]
author: oxo-call-community
source_url: "https://github.com/rbturnbull/orthoflow"
---

## Concepts

- **Tool Overview**: OrthoFlow automates phylogenetic inference workflows.
- **Core Function**: Processes genome-scale datasets for phylogenetic analysis.
- **Algorithm**: Uses Snakemake for workflow management.
- **Input Format**: Accepts FASTA files of protein-coding genes.
- **Output**: Produces phylogenetic trees and alignments.
- **Use Case**: Comparative genomics, phylogenetics, and evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Dependency Management**: Requires proper environment setup.
- **Runtime**: Workflows may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orthoflow --help`
**Explanation:** Shows available options and usage instructions.

### Initialize workflow
**Args:** `orthoflow init -o my_project`
**Explanation:** Creates a new OrthoFlow project.

### Run workflow
**Args:** `orthoflow run -c config.yaml`
**Explanation:** Executes the phylogenetic workflow.

### With configuration
**Args:** `orthoflow run -c config.yaml --cores 8`
**Explanation:** Runs with specified number of cores.

### Dry run
**Args:** `orthoflow run -c config.yaml --dry-run`
**Explanation:** Shows what would be executed.

### Verbose mode
**Args:** `orthoflow run -c config.yaml -v`
**Explanation:** Runs with verbose output.

### Resume workflow
**Args:** `orthoflow run -c config.yaml --resume`
**Explanation:** Resumes from last checkpoint.