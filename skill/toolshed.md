---
name: toolshed
category: utility
description: ToolShed - Tool management and sharing platform for bioinformatics.
tags: [toolshed, tool-management, bioinformatics, sharing, workflow]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/toolshed"
---

## Concepts

- **Tool Overview**: ToolShed - A platform for sharing and managing bioinformatics tools and workflows.
- **Core Function**: Provides a repository for sharing tools, versions, and dependencies for Galaxy and other workflow systems.
- **Input**: Tool wrappers, configuration files, metadata.
- **Output**: Shared tools, version tracking, dependency management.
- **Installation**: Galaxy ToolShed is a web service; tools can be installed via Galaxy interface.
- **Use Case**: Tool sharing, reproducible research, collaborative bioinformatics.

## Pitfalls

- **Dependency Management**: Tool dependencies may conflict with existing installations.
- **Version Compatibility**: Tools may require specific versions of dependencies.

## Examples

### Install tool
**Args:** `galaxy-tool-shed install tool_name --version 1.0.0`
**Explanation:** Install a tool from the ToolShed.

### Search tools
**Args:** `galaxy-tool-shed search --query "variant calling"`
**Explanation:** Search for variant calling tools in the ToolShed.
