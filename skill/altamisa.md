---
name: altamisa
category: programming
description: Alternative Python API for accessing ISA-Tab files
tags: [altamisa, ISA-Tab, Python, bioinformatics, metadata, experiment-data]
author: oxo-call-community
source_url: "https://github.com/bihealth/altamisa"
---

## Concepts

- **Tool Overview**: AltamISA is a Python 3 library for representing the ISA-tools data model and reading/writing ISA-Tab file format, designed as an alternative to the official isa-api.
- **Core Function**: Provides immutable data structures (named tuples) for ISA records, implements a directed acyclic graph (DAG) for material and process nodes, and includes strictly validating parsers.
- **Input/Output**: Reads ISA-Tab investigation files (i_investigation.txt) and associated study/assay files; outputs validated ISA data structures and ISA-Tab files.
- **Installation**: Available via PyPI (`pip install altamisa`) or Bioconda (`conda install -c bioconda altamisa`).
- **Features**: Full ISA-Tab format support, strict validation, type annotations, >90% test coverage, and extensions like semicolon-separated list values.

## Pitfalls

- **Validation Strictness**: Strict parsing may reject files that other tools accept; ensure ISA-Tab files follow official specifications.
- **ISA-JSON Support**: Currently does not support ISA-JSON format; use official isa-api if JSON is required.
- **Python Version**: Requires Python 3.8+; older versions are not supported.
- **File Structure**: ISA-Tab requires specific file naming conventions (i_investigation.txt, s_*.txt, a_*.txt); incorrect naming causes errors.
- **Ontology Terms**: Multiple values in Characteristics/ParameterValue fields require matching TermSource REF and Term Accession Number fields.

## Examples

### Read and validate investigation file
**Args:** Python API usage
```python
from altamisa.isatab import InvestigationReader, InvestigationValidator
with open("i_investigation.txt", "rt") as f:
    investigation = InvestigationReader.from_stream(f).read()
InvestigationValidator(investigation).validate()
```
**Explanation:** Reads an ISA-Tab investigation file and validates its structure and content against ISA specifications.

### Iterate through studies and assays
**Args:** Python API usage
```python
for study in investigation.studies:
    print(f"Study: {study.study_title}")
    for assay in study.assays:
        print(f"  Assay: {assay.assay_name}")
```
**Explanation:** Iterates through the hierarchical structure of studies and assays in an investigation.

### Access materials and processes
**Args:** Python API usage
```python
for study in investigation.studies:
    for material in study.materials:
        print(f"Material: {material.name}, Type: {material.type}")
```
**Explanation:** Accesses material nodes in the ISA-Tab graph structure.

### Convert to Graphviz dot format
**Args:** Python API usage with graphviz extension
```python
from altamisa.graphviz import to_dot
dot_output = to_dot(investigation)
with open("output.dot", "wt") as f:
    f.write(dot_output)
```
**Explanation:** Converts the ISA investigation graph to Graphviz DOT format for visualization.

### Write ISA-Tab files
**Args:** Python API usage
```python
from altamisa.isatab import InvestigationWriter
with open("output/i_investigation.txt", "wt") as f:
    InvestigationWriter.to_stream(investigation, f)
```
**Explanation:** Writes a validated investigation object back to ISA-Tab file format.