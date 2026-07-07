---
name: jms-metabolite-services
category: utility
description: Conversion and search of metabolic models and metabolomics data.
tags: [jms-metabolite-services, utility, metabolomics, conversion, annotation]
author: oxo-call-community
source_url: "https://github.com/shuzhao-li/JMS"
---

## Concepts

- **Tool Overview**: jms-metabolite-services (v0.5.8) - A service for conversion and search of metabolic models and metabolomics data.
- **Metabolite Conversion**: Converts metabolite identifiers between different databases.
- **Model Integration**: Integrates metabolic models with experimental data.
- **Annotation**: Annotates metabolomics data with metabolite information.
- **Database Search**: Searches metabolite databases for matching compounds.
- **Cross-referencing**: Cross-references metabolite identifiers across databases.

## Pitfalls

- **Database Coverage**: Not all metabolites may be covered in all databases.
- **Identifier Ambiguity**: Some identifiers may map to multiple metabolites.
- **Version Differences**: Database versions can affect mappings.
- **Network Dependencies**: Requires network access for database queries.
- **Data Format**: Requires specific input data formats.
- **Ambiguous Names**: Common names may refer to multiple compounds.

## Examples

### Convert metabolite identifiers
**Args:** `jms convert --input metabolites.txt --from chebi --to hmdb`
**Explanation:** Converts metabolite identifiers from ChEBI to HMDB format.

### Search metabolite database
**Args:** `jms search --name "glucose"`
**Explanation:** Searches for metabolite information by name.

### Annotate metabolomics data
**Args:** `jms annotate --input peaks.csv --output annotated.csv`
**Explanation:** Annotates metabolomics peaks with metabolite information.

### Map metabolites to pathways
**Args:** `jms pathway --input metabolites.txt --output pathways.json`
**Explanation:** Maps metabolites to their associated pathways.

### Batch conversion
**Args:** `jms batch --input ids.txt --output mapped.txt --map kegg-to-reactome`
**Explanation:** Batch converts identifiers between databases.

### Show available databases
**Args:** `jms databases`
**Explanation:** Lists available metabolite databases.