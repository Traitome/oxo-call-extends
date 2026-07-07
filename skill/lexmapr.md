---
name: lexmapr
category: ontology
description: Lexicon and rule-based tool for translating biomedical descriptions to ontology terms
tags: [lexmapr, ontology, semantic-web, biomedical, terminology]
author: oxo-call-community
source_url: "https://github.com/LexMapr/lexmapr"
---

## Concepts

- **Ontology Mapping**: Maps text descriptions to ontology terms
- **Lexicon-based**: Uses lexicon for term matching
- **Rule-based**: Applies rules for semantic translation
- **Biomedical Focus**: Designed for biomedical specimen descriptions
- **Semantic Web**: Integrates with semantic web technologies
- **Terminology Standardization**: Standardizes biomedical terminology

## Pitfalls

- **Ontology Coverage**: Limited ontology coverage may miss terms
- **Ambiguity**: Ambiguous terms may map incorrectly
- **Synonyms**: Missing synonyms affect matching
- **Term Variation**: Different term formats may fail
- **Context Sensitivity**: Terms may have different meanings in context
- **Update Frequency**: Ontologies need regular updates

## Examples

### Map terms
**Args:** `lexmapr map -i descriptions.txt -o results.tsv`
**Explanation:** Maps text descriptions to ontology terms.

### Specify ontology
**Args:** `lexmapr map -i descriptions.txt -o results.tsv -o ontology.owl`
**Explanation:** Uses specific ontology for mapping.

### Batch processing
**Args:** `lexmapr batch -d descriptions/ -o results/`
**Explanation:** Processes multiple description files.

### Generate report
**Args:** `lexmapr map -i descriptions.txt -o results.tsv --report`
**Explanation:** Creates detailed mapping report.

### Verbose output
**Args:** `lexmapr map -i descriptions.txt -o results.tsv --verbose`
**Explanation:** Shows detailed mapping information.

### Validate mappings
**Args:** `lexmapr validate -i results.tsv`
**Explanation:** Validates mapped ontology terms.