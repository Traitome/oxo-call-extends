---
name: cwl2wdl
category: formatting
description: Converter from Common Workflow Language (CWL) to Workflow Definition Language (WDL)
tags: [cwl2wdl, formatting, CWL, WDL, workflow-conversion]
author: oxo-call-community
source_url: "https://github.com/adamstruck/cwl2wdl"
---

## Concepts

- **Tool Overview**: cwl2wdl (v0.1dev44+) is a proof-of-concept converter from Common Workflow Language (CWL) to the Broad Institute's Workflow Definition Language (WDL).
- **Core Function**: Translates CWL workflow descriptions to WDL format for execution on Cromwell and other WDL engines.
- **Input/Output**: Input: CWL workflow files (.cwl). Output: WDL workflow files (.wdl).
- **Supported Features**: Basic workflow structures, command line tools, file inputs/outputs.
- **Key Features**: Workflow language conversion, preserves workflow logic, supports basic tool definitions.
- **Installation**: `conda install -c bioconda cwl2wdl`

## Pitfalls

- **Feature Limitations**: Not all CWL features are supported; complex workflows may require manual adjustments.
- **Version Compatibility**: CWL and WDL versions may affect conversion accuracy.
- **Manual Review**: Converted workflows should be reviewed and tested before production use.
- **Error Handling**: Error messages may be cryptic for complex workflows.
- **Documentation**: Limited documentation for advanced usage.

## Examples

### Convert CWL to WDL
**Args:** `cwl2wdl -i workflow.cwl -o workflow.wdl`
**Explanation:** Convert CWL workflow to WDL format.

### Convert with validation
**Args:** `cwl2wdl -i workflow.cwl -o workflow.wdl --validate`
**Explanation:** Convert and validate the resulting WDL file.

### Convert multiple files
**Args:** `cwl2wdl -i tool1.cwl tool2.cwl -o wdl_output/`
**Explanation:** Convert multiple CWL files to WDL format.
