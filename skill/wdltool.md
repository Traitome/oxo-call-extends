---
name: wdltool
category: bioinformatics
description: WDLTool - WDL workflow tool.
tags: [wdltool, workflow, wdl, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/wdltool"
---

## Concepts

- **Tool Overview**: WDLTool - WDL workflow processing tool.
- **Core Function**: Processes and validates WDL workflows.
- **Input**: WDL file.
- **Output**: Processed workflow.
- **Installation**: Install via Java or conda
- **Use Case**: Workflow development, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for complex workflows.
- **Complexity**: May have steep learning curve.

## Examples

### Validate workflow
**Args:** `wdltool validate workflow.wdl`
**Explanation:** Validate WDL workflow.

### With options
**Args:** `wdltool compile workflow.wdl -o compiled.wdl`
**Explanation:** Compile workflow.
