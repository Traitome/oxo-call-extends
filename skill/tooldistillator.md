---
name: tooldistillator
category: utility
description: ToolDistillator - Tool for distilling and simplifying bioinformatics workflows.
tags: [tooldistillator, workflow, simplification, bioinformatics, pipeline]
author: oxo-call-community
source_url: "https://github.com/compbio/tooldistillator"
---

## Concepts

- **Tool Overview**: ToolDistillator - A tool for simplifying and optimizing complex bioinformatics workflows.
- **Core Function**: Analyzes workflow dependencies and suggests optimizations to reduce complexity.
- **Input**: Workflow definition files, pipeline configuration.
- **Output**: Simplified workflow, optimization suggestions, performance metrics.
- **Installation**: `pip install tooldistillator` or `conda install -c bioconda tooldistillator`
- **Use Case**: Workflow optimization, pipeline simplification, performance improvement.

## Pitfalls

- **Workflow Complexity**: Very complex workflows may be difficult to distill.
- **Completeness**: Optimization suggestions may not cover all edge cases.

## Examples

### Distill workflow
**Args:** `tooldistillator -w workflow.cwl -o distilled_workflow/`
**Explanation:** Analyze and simplify a CWL workflow.

### Optimize pipeline
**Args:** `tooldistillator optimize -i pipeline.wdl -o optimized/`
**Explanation:** Optimize a WDL pipeline for performance.
