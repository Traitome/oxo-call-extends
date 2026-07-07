---
name: nf-docs
category: programming
description: nf-docs generates API documentation for Nextflow pipelines using the Nextflow Language Server.
tags: [nf-docs, programming, nextflow, documentation]
author: oxo-call-community
source_url: "https://github.com/ewels/nf-docs"
---

## Concepts

- **Tool Overview**: nf-docs automates documentation generation for Nextflow pipelines.
- **Core Function**: Extracts and formats API documentation from pipeline code.
- **Algorithm**: Queries Nextflow Language Server to parse pipeline metadata.
- **Input Format**: Accepts Nextflow pipeline files and configurations.
- **Output**: Produces HTML or Markdown documentation.
- **Use Case**: Pipeline documentation, API reference generation, and developer documentation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Language Server**: Requires Nextflow Language Server installation.
- **Pipeline Structure**: Works best with well-structured pipelines.
- **Documentation Quality**: Depends on code annotations.
- **Output Format**: Limited output format options.
- **Complex Pipelines**: May struggle with highly complex pipelines.

## Examples

### Display help
**Args:** `nf-docs --help`
**Explanation:** Shows available options and usage instructions.

### Generate documentation
**Args:** `nf-docs generate --input main.nf --output docs/`
**Explanation:** Generates documentation for pipeline.

### Serve documentation
**Args:** `nf-docs serve --input main.nf`
**Explanation:** Serves documentation locally for preview.

### Markdown output
**Args:** `nf-docs generate --input main.nf --format markdown --output docs.md`
**Explanation:** Outputs documentation in Markdown format.

### HTML output
**Args:** `nf-docs generate --input main.nf --format html --output docs.html`
**Explanation:** Outputs documentation in HTML format.

### Watch mode
**Args:** `nf-docs watch --input main.nf --output docs/`
**Explanation:** Watches for changes and auto-updates documentation.

### Specify config
**Args:** `nf-docs generate --input main.nf --config nextflow.config --output docs/`
**Explanation:** Uses custom configuration file.