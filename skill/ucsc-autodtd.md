---
name: ucsc-autodtd
category: utility
description: UCSC autoDtd - Tool for generating DTD files from autoSql schemas.
tags: [ucsc-autodtd, ucsc, dtd-generation, schema, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC autoDtd - A tool for generating DTD (Document Type Definition) files from autoSql schemas.
- **Core Function**: Converts autoSql schema definitions to XML DTD format.
- **Input**: autoSql schema file.
- **Output**: DTD file for XML validation.
- **Installation**: Part of UCSC utilities
- **Use Case**: Schema generation, XML validation, data standardization.

## Pitfalls

- **Schema Format**: Requires proper autoSql schema format.
- **Validation**: Generated DTD requires validation.

## Examples

### Generate DTD
**Args:** `autoDtd schema.as > output.dtd`
**Explanation:** Generate DTD from autoSql schema.

### With output file
**Args:** `autoDtd -o schema.dtd input.as`
**Explanation:** Generate DTD with specified output file.
