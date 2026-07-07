---
name: ngless
category: metagenomics
description: NGLess is a domain-specific language for metagenomics data processing.
tags: [ngless, metagenomics, bioinformatics, dsl]
author: oxo-call-community
source_url: "https://ngless.embl.de"
---

## Concepts

- **Tool Overview**: NGLess is a specialized language for metagenomics analysis.
- **Core Function**: Processes raw sequencing data for metagenomics studies.
- **Algorithm**: Implements optimized pipelines for quality control and analysis.
- **Input Format**: Accepts FASTQ files and NGLess script files.
- **Output**: Produces processed reads and analysis results.
- **Use Case**: Metagenomics analysis, microbiome research, and environmental sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Script Syntax**: Requires learning NGLess DSL.
- **Memory Usage**: Large datasets require memory.
- **Reference Databases**: Requires downloading reference databases.
- **Computational Cost**: Analysis can be computationally intensive.
- **Error Messages**: May require debugging script issues.

## Examples

### Display help
**Args:** `ngless --help`
**Explanation:** Shows available options and usage instructions.

### Run script
**Args:** `ngless script.ngl`
**Explanation:** Executes NGLess script.

### Run with verbose
**Args:** `ngless -v script.ngl`
**Explanation:** Runs script with verbose output.

### Print AST
**Args:** `ngless --print-ast script.ngl`
**Explanation:** Prints abstract syntax tree.

### Version
**Args:** `ngless --version`
**Explanation:** Shows NGLess version.

### Help on function
**Args:** `ngless --help-function read`
**Explanation:** Shows help for specific function.

### Install reference
**Args:** `ngless --install-reference humann3`
**Explanation:** Installs reference database.