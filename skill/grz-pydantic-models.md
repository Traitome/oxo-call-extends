---
name: grz-pydantic-models
category: bioinformatics
description: grz-pydantic-models provides Pydantic models for validating GRZ metadata schema.
tags: [grz-pydantic-models, validation, Pydantic, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BfArM-MVH/grz-tools"
---

## Concepts

- **Pydantic Models**: grz-pydantic-models defines data models using Pydantic.

- **Schema Validation**: Validates metadata against GRZ schema requirements.

- **Data Parsing**: Parses and validates incoming metadata submissions.

- **Type Safety**: Provides type-safe data structures for metadata.

- **Automatic Validation**: Automatically validates data on instantiation.

- **Documentation**: Generates documentation from model definitions.

## Pitfalls

- **Schema Changes**: Stay updated with changes to GRZ metadata schema.

- **Version Compatibility**: Ensure compatibility with Pydantic version.

- **Required Fields**: Missing required fields will cause validation errors.

- **Data Types**: Ensure data types match expected schema.

- **Nested Models**: Complex nested models require careful handling.

## Examples

### Import models
**Args:** `from grz_pydantic_models import SubmissionMetadata, SampleInfo`
**Explanation:** Imports Pydantic models.

### Validate metadata
**Args:** `metadata = SubmissionMetadata(**data)`
**Explanation:** Validates metadata against schema.

### Parse JSON
**Args:** `metadata = SubmissionMetadata.parse_raw(json_string)`
**Explanation:** Parses and validates JSON data.

### Export to dict
**Args:** `dict_data = metadata.dict()`
**Explanation:** Converts model to dictionary.

### Generate schema
**Args:** `schema = SubmissionMetadata.schema()`
**Explanation:** Generates JSON schema from model.

### Validate partial data
**Args:** `metadata = SubmissionMetadata.partial(**data)`
**Explanation:** Validates partial metadata.

### Custom validation
**Args:** `from grz_pydantic_models import validate_submission`
**Explanation:** Uses custom validation functions.