---
name: beast-pype
category: programming
description: beast-pype - BEAST 2 pipelines for phylodynamics analysis
tags: [beast-pype, programming, BEAST2, phylodynamics, pipeline]
author: oxo-call-community
source_url: "https://github.com/m-d-grunnill/BEAST_pype"
---

## Concepts

- **Tool Overview**: beast-pype (v0.3.1) is a package of BEAST 2 pipelines for phylodynamics analysis, providing automated workflows for Bayesian evolutionary inference.
- **Core Function**: Provides pre-configured pipelines for common phylodynamic analyses using BEAST 2.
- **Phylodynamics**: Integrates phylogenetic and epidemiological analysis for disease dynamics.
- **Pipeline Automation**: Automates multi-step BEAST 2 analyses including XML generation, running, and result processing.
- **Snakemake Integration**: Uses Snakemake for workflow management and parallel execution.
- **Input/Output**: Accepts sequence alignments and metadata; outputs BEAST2 XML and analysis results.
- **Installation**: `conda install -c bioconda beast-pype`.

## Pitfalls

- **BEAST2 Dependencies**: Requires BEAST 2 and related packages to be installed.
- **Phylodynamic Models**: Requires careful selection of demographic and clock models.
- **Computational Resources**: Phylodynamic analyses can be computationally intensive.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Run basic phylodynamic pipeline
**Args:** `beast-pype run --input alignment.fasta --output results/`
**Explanation:** Runs complete phylodynamic analysis pipeline.

### Generate BEAST2 XML
**Args:** `beast-pype xml --input alignment.fasta --output analysis.xml`
**Explanation:** Generates BEAST2 XML configuration file.

### Run with custom model
**Args:** `beast-pype run --input alignment.fasta --model skyline --output results/`
**Explanation:** Uses skyline demographic model for analysis.

### Specify chain length
**Args:** `beast-pype run --input alignment.fasta --chain-length 10000000 --output results/`
**Explanation:** Sets MCMC chain length to 10 million iterations.

### Run convergence check
**Args:** `beast-pype check --input results/`
**Explanation:** Checks MCMC convergence using Tracer.

### Generate report
**Args:** `beast-pype report --input results/ --output report.html`
**Explanation:** Generates HTML report of analysis results.

### Display help
**Args:** `beast-pype --help`
**Explanation:** Shows all available command-line options and usage information.