---
name: schema-salad
category: workflow
description: Schema Salad - Schema Annotations for Linked Avro Data for CWL workflows
tags: ["schema-salad", "workflow", "CWL", "schema"]
author: oxo-call-community
source_url: "https://github.com/common-workflow-language/schema_salad"
---

## Concepts

- **Tool Overview**: Schema Salad (v2.7.20180809223002) provides Schema Annotations for Linked Avro Data, used in Common Workflow Language (CWL).
- **Core Function**: Validates and processes workflow schemas and documents.
- **Algorithm**: Uses JSON Schema and linked data principles for schema validation.
- **Input/Output**: Accepts schema definitions and workflow documents, produces validated outputs.
- **CWL Integration**: Integrates with Common Workflow Language for workflow description.
- **Applications**: Workflow validation, schema generation, and data integration.

## Pitfalls

- **Schema Complexity**: Complex schemas may be difficult to debug.
- **Version Compatibility**: Different CWL versions may have different schemas.
- **Validation Errors**: May produce cryptic validation error messages.
- **Documentation**: Limited documentation for complex schema features.
- **Tool Dependencies**: Requires compatible CWL tooling.
- **Learning Curve**: Steep learning curve for schema design.

## Examples

### Validate workflow
**Args:** `schema-salad-tool --validate workflow.cwl`
**Explanation:** Validates CWL workflow file against schema.

### Generate documentation
**Args:** `schema-salad-tool --doc workflow.cwl -o documentation.html`
**Explanation:** Generates HTML documentation from workflow.

### Convert schema
**Args:** `schema-salad-tool --convert schema.yml -o schema.json`
**Explanation:** Converts schema between YAML and JSON formats.

### Resolve references
**Args:** `schema-salad-tool --resolve workflow.cwl -o resolved.cwl`
**Explanation:** Resolves all references in workflow document.

### Verbose output
**Args:** `schema-salad-tool --validate workflow.cwl -v`
**Explanation:** `-v` enables verbose validation output.

### Extract schema
**Args:** `schema-salad-tool --extract-schema workflow.cwl -o schema.json`
**Explanation:** Extracts schema from workflow document.

### Test schema
**Args:** `schema-salad-tool --test schema.yml tests/`
**Explanation:** Runs tests against schema definition.