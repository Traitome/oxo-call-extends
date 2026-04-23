---
name: biopet
category: utility
description: Bio Pipeline Execution Toolkit for LUMC sequencing analysis
tags: [pipeline, workflow, sequencing-analysis]
author: oxo-call-community
source_url: "https://github.com/biopet/biopet"
---

## Concepts
- **Tool Overview**: Biopet (Bio Pipeline Execution Toolkit) is the main pipeline development framework of the LUMC Sequencing Analysis Support Core team. It provides ready-to-use pipelines for common sequencing analyses.
- **Pipeline Framework**: Built on top of GATK Queue for workflow management and execution.
- **Included Pipelines**: Mapping, variant calling, RNA-seq, ChIP-seq, and other common NGS workflows.
- **Applications**: Production sequencing analysis, pipeline development, reproducible research.

## Pitfalls
- **Java Dependency**: Requires Java runtime environment.
- **Configuration**: Pipelines require proper configuration files.

## Examples
### Run mapping pipeline
**Args:** `biopet mapping -config config.json -output output_dir/`
**Explanation:** Runs the Biopet mapping pipeline with specified configuration.
