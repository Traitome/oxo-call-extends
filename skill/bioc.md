---
name: bioc
category: utility
description: Processing BioC, Brat, and PubTator formats with Python
tags: [bioc, text-mining, nlp, annotation]
author: oxo-call-community
source_url: "https://github.com/bionlplab/bioc"
---

## Concepts
- **Tool Overview**: bioc is a Python library for processing BioC, Brat, and PubTator formats, which are used for biomedical text annotation and natural language processing.
- **BioC Format**: XML-based format for biomedical text annotations (entities, relations, events).
- **Supported Formats**: BioC XML, Brat standoff, PubTator format.
- **Applications**: Biomedical NLP, text mining, literature annotation, named entity recognition.

## Pitfalls
- **Format Differences**: Each format has different annotation capabilities and limitations.
- **Encoding**: Ensure proper text encoding when processing biomedical literature.

## Examples
### Parse BioC file
**Args:** `bioc parse input.xml --output parsed.json`
**Explanation:** Parses a BioC XML file to JSON format.

### Convert Brat to BioC
**Args:** `bioc convert brat_to_bioc --input brat_dir/ --output output.xml`
**Explanation:** Converts Brat annotations to BioC format.
