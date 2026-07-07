---
name: biolite
category: workflow
description: Lightweight bioinformatics framework with automated tracking of diagnostics and provenance
tags: [workflow, provenance, diagnostics, ngs, pipeline]
author: oxo-call-community
source_url: "https://bitbucket.org/caseywdunn/biolite"
---

## Concepts

- **Tool Overview**: BioLite is a Python/C++ framework for implementing bioinformatics pipelines for Next-Generation Sequencing (NGS) data, with automated tracking of diagnostics and provenance.
- **Provenance Tracking**: Automatically tracks the origin and history of all analysis products for reproducibility.
- **Diagnostics Collection**: Automates collection and reporting of summary statistics and plots at intermediate pipeline stages.
- **HTML Reports**: Generates comprehensive HTML reports with diagnostics accessible across multiple pipeline stages.
- **Lightweight Design**: Minimal resource overhead, maximum performance, portability across systems.

## Pitfalls

- **Documentation**: May require consulting the original publication for detailed usage.
- **C++ Tools**: Some advanced functionality requires separate biolite-tools package.
- **Version Compatibility**: Scripts are prefixed with 'bl-' since version 0.4.0.

## Examples

### Install biolite
**Args:** `conda install -c bioconda biolite`
**Explanation:** Installs the biolite Python framework.

### Install C++ tools
**Args:** `conda install -c bioconda biolite-tools`
**Explanation:** Installs the optional C++ tools for biolite.

### Run diagnostics
**Args:** `bl-diagnostics --help`
**Explanation:** Shows available diagnostics commands.

### Create pipeline
**Args:** `from biolite.pipeline import Pipeline; p = Pipeline(); p.add_stage('quality_filter')`
**Explanation:** Creates a new bioinformatics pipeline with quality filtering stage.