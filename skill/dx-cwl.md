---
name: dx-cwl
category: programming
description: "Import and run CWL workflows on DNAnexus"
tags: [dx-cwl, programming, CWL, DNAnexus, workflow, cloud]
author: oxo-call-community
source_url: "https://github.com/dnanexus/dx-cwl"
---

## Concepts

- **Tool Overview**: dx-cwl is a tool for importing and running Common Workflow Language (CWL) workflows on the DNAnexus platform.
- **Core Function**: Converts CWL workflows to DNAnexus native format and executes them in the cloud.
- **Input/Output**: Input: CWL workflow files, input parameters. Output: DNAnexus workflow, execution results.
- **Algorithm**: Translates CWL specifications to DNAnexus workflow language.
- **Key Features**: CWL compatibility, cloud execution, DNAnexus integration, workflow validation.
- **Installation**: `conda install -c bioconda dx-cwl`

## Pitfalls

- **DNAnexus Account**: Requires active DNAnexus account and authentication.
- **CWL Version**: May not support all CWL versions or features.
- **Resource Limits**: Cloud resources may have usage limits and costs.
- **Data Transfer**: Large input/output files may incur transfer costs.
- **Workflow Complexity**: Complex workflows may require manual adjustments.

## Examples

### Import CWL workflow
**Args:** `dx-cwl compile workflow.cwl --output workflow.dx.json`
**Explanation:** Compiles CWL workflow to DNAnexus format.

### Run workflow
**Args:** `dx-cwl run workflow.cwl --inputs inputs.json`
**Explanation:** Runs CWL workflow on DNAnexus platform.

### With project
**Args:** `dx-cwl run workflow.cwl --inputs inputs.json --project project-xxxx`
**Explanation:** Runs workflow in specific DNAnexus project.

### Validate workflow
**Args:** `dx-cwl validate workflow.cwl`
**Explanation:** Validates CWL workflow without executing.

### List available tools
**Args:** `dx-cwl list-tools`
**Explanation:** Lists available CWL tools on DNAnexus.