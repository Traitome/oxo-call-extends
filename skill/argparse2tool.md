---
name: argparse2tool
category: utility
description: Convert Python argparse definitions to Galaxy XML and CWL tool descriptions
tags: [argparse2tool, utility, galaxy, cwl, workflow, python]
author: oxo-call-community
source_url: "https://github.com/erasche/argparse2tool"
---

## Concepts

- **Tool Overview**: argparse2tool converts Python argparse argument definitions into Galaxy XML wrappers and Common Workflow Language (CWL) tool descriptions. Version 0.5.2.
- **Core Function**: Automates the creation of workflow tool definitions from existing Python command-line programs.
- **Galaxy Integration**: Generates Galaxy XML format for integration with Galaxy workflow platform.
- **CWL Support**: Outputs CWL tool descriptions for portable, reproducible workflows.
- **Argument Mapping**: Maps argparse parameters (types, choices, defaults) to appropriate tool descriptor formats.
- **Installation**: `conda install -c bioconda argparse2tool` or install via pip from GitHub.

## Pitfalls

- **Argparse Limitations**: Only captures argparse-defined arguments. Custom argument parsing not supported.
- **Type Mapping**: Some Python types may not map cleanly to Galaxy/CWL types.
- **Complex Arguments**: Nested arguments or positional arguments may need manual adjustment.
- **Output Quality**: Generated descriptors may need manual refinement for production use.
- **Version Compatibility**: Generated formats may vary with Galaxy/CWL version updates.

## Examples

### Generate Galaxy XML
**Args:** `argparse2tool --parser myscript.py --format galaxy --output mytool.xml`
**Explanation:** Creates Galaxy XML wrapper from Python argparse definitions.

### Generate CWL tool description
**Args:** `argparse2tool --parser myscript.py --format cwl --output mytool.cwl`
**Explanation:** Creates CWL tool description file for workflow integration.

### Specify input type
**Args:** `argparse2tool --parser myscript.py --format galaxy --output tool.xml --default_type File`
**Explanation:** Sets default input type as File for unspecified arguments.

### Batch conversion
**Args:** `argparse2tool_batch --input_dir parsers/ --format cwl --output_dir cwl_tools/`
**Explanation:** Converts multiple Python scripts to CWL format in batch mode.