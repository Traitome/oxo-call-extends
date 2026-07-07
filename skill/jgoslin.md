---
name: jgoslin
category: utility
description: Parser, validator and normalizer for shorthand lipid names based on the Goslin project.
tags: [jgoslin, utility, lipid, parser, metabolomics]
author: oxo-call-community
source_url: "https://github.com/lifs-tools/jgoslin"
---

## Concepts

- **Tool Overview**: jgoslin (v2.2.0) - A parser, validator and normalizer for shorthand lipid names based on the Goslin grammar.
- **Lipid Parsing**: Parses shorthand lipid nomenclature into structured data.
- **Validation**: Validates lipid names against standard nomenclature.
- **Normalization**: Normalizes lipid names to a standard format.
- **Goslin Grammar**: Implements the Goslin lipid nomenclature grammar.
- **Metabolomics Integration**: Integrates with metabolomics analysis workflows.

## Pitfalls

- **Nomenclature Variations**: Different lipid databases use different naming conventions.
- **Ambiguous Names**: Some lipid names can be ambiguous.
- **Version Compatibility**: Grammar rules may change between versions.
- **Unsupported Lipids**: Rare or novel lipids may not be recognized.
- **Input Format**: Requires proper lipid name format.
- **Case Sensitivity**: Lipid names may be case-sensitive.

## Examples

### Parse lipid name
**Args:** `jgoslin parse "PC 18:1(9Z)/16:0"`
**Explanation:** Parses the lipid name and returns structured information.

### Validate lipid name
**Args:** `jgoslin validate "PC 18:1/16:0"`
**Explanation:** Validates if the lipid name follows standard nomenclature.

### Normalize lipid names
**Args:** `jgoslin normalize -i lipids.txt -o normalized.txt`
**Explanation:** Normalizes a list of lipid names to standard format.

### Convert to JSON
**Args:** `jgoslin parse --format json "PE 18:0/20:4"`
**Explanation:** Outputs parsed lipid information in JSON format.

### Batch processing
**Args:** `jgoslin batch -i lipid_list.txt -o results.json`
**Explanation:** Processes multiple lipid names from a file.

### Show grammar version
**Args:** `jgoslin version`
**Explanation:** Displays the current Goslin grammar version.