---
name: biobb_wf_mutations
category: utility
description: Lysozyme + Mutations workflow using BioBB
tags: [bioexcel, workflow, mutations, tutorial]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_md"
---

## Concepts
- **Tool Overview**: biobb_wf_mutations is a demonstration workflow for lysozyme with mutations, built using BioBB and based on the official GROMACS tutorial.
- **Workflow**: Structure preparation → topology generation → energy minimization → equilibration → production MD → analysis.
- **Educational Purpose**: Demonstrates BioBB workflow capabilities for MD simulations with mutations.

## Pitfalls
- **Tutorial Nature**: This is a demonstration workflow, not a general-purpose tool.

## Examples
### Run mutation workflow
**Args:** `biobb_wf_mutations.run --mutation A:ALA:VAL:50 --output results/`
**Explanation:** Runs the lysozyme mutation workflow.
