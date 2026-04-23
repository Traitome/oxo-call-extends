---
name: biobb_adapters
category: utility
description: BioBB module for using building blocks with workflow managers
tags: [workflow, bioexcel, building-blocks, pipeline]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_adapters"
---

## Concepts
- **Tool Overview**: biobb_adapters is the BioExcel Building Blocks (BioBB) module for using building blocks with several workflow managers (CWL, Nextflow, Snakemake, etc.).
- **BioBB Framework**: BioBB packages are Python building blocks that create interoperability over popular bioinformatics tools.
- **Workflow Integration**: Adapts BioBB components for use in different workflow management systems.
- **Applications**: Molecular dynamics, structural biology, and bioinformatics pipeline construction.

## Pitfalls
- **Workflow Manager Knowledge**: Requires familiarity with target workflow manager.
- **Dependency Management**: BioBB components have specific dependency requirements.

## Examples
### Generate CWL wrapper
**Args:** `biobb_adapters cwl --tool biobb_md.gromacs.mdrun --output mdrun.cwl`
**Explanation:** Generates a CWL wrapper for a BioBB GROMACS component.

### Generate Nextflow wrapper
**Args:** `biobb_adapters nextflow --tool biobb_md.gromacs.mdrun --output Mdrun.nf`
**Explanation:** Generates a Nextflow module for a BioBB component.
