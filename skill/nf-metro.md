---
name: nf-metro
category: workflow
description: nf-metro provides Metromap-style workflow components for Nextflow pipelines.
tags: [nf-metro, workflow, nextflow, pipeline]
author: oxo-call-community
source_url: "https://github.com/pinin4fjords/nf-metro"
---

## Concepts

- **Tool Overview**: nf-metro offers reusable workflow components for Nextflow pipelines.
- **Core Function**: Provides modular components for common pipeline patterns.
- **Algorithm**: Implements workflow patterns as Nextflow modules.
- **Input Format**: Accepts Nextflow pipeline configurations.
- **Output**: Produces pipeline components and workflows.
- **Use Case**: Pipeline development, workflow composition, and code reuse.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Nextflow Version**: Requires compatible Nextflow version.
- **Module Compatibility**: Components may need adaptation.
- **Documentation**: Limited documentation available.
- **Complexity**: May add complexity to simple pipelines.
- **Maintenance**: Dependencies require regular updates.

## Examples

### Display help
**Args:** `nf-metro --help`
**Explanation:** Shows available options and usage instructions.

### List modules
**Args:** `nf-metro list`
**Explanation:** Lists available workflow modules.

### Generate pipeline
**Args:** `nf-metro generate --template rna-seq --output pipeline/`
**Explanation:** Generates RNA-seq pipeline template.

### Add module
**Args:** `nf-metro add --module fastqc --to pipeline/`
**Explanation:** Adds FastQC module to pipeline.

### Update modules
**Args:** `nf-metro update --pipeline pipeline/`
**Explanation:** Updates modules in existing pipeline.

### Validate pipeline
**Args:** `nf-metro validate --pipeline pipeline/`
**Explanation:** Validates pipeline structure.

### Export template
**Args:** `nf-metro export --template my-template --output templates/`
**Explanation:** Exports custom template.