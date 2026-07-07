---
name: msmetaenhancer
category: annotation
description: Python tool for adding annotations like SMILES, InChI, CAS to MSP files.
tags: [msmetaenhancer, annotation, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/RECETOX/MSMetaEnhancer"
---

## Concepts

- **Tool Overview**: MSMetaEnhancer v0.5.0 adds annotations to MSP files.
- **Core Function**: Enriches mass spectrometry data with additional annotations.
- **Chemical Annotations**: Adds SMILES, InChI, and CAS numbers.
- **Database Integration**: Queries various chemical databases.
- **MSP Format**: Works with Mass Spectra of Products format.
- **Input/Output**: Accepts MSP files; outputs annotated MSP files.

## Pitfalls

- **Network Dependence**: Requires internet for database queries.
- **Database Availability**: Depends on external database availability.
- **Rate Limiting**: May be subject to API rate limits.
- **Memory Requirements**: Memory usage depends on file size.
- **Annotation Coverage**: Not all compounds may have annotations.
- **Computational Resources**: Large files may require significant resources.

## Examples

### Add annotations to MSP file
**Args:** `msmetaenhancer -i spectra.msp -o annotated.msp`
**Explanation:** Adds chemical annotations to MSP file.

### With specific databases
**Args:** `msmetaenhancer -i spectra.msp -d pubchem chebi -o annotated.msp`
**Explanation:** Queries specific databases for annotations.

### Async processing
**Args:** `msmetaenhancer -i spectra.msp -a -o annotated.msp`
**Explanation:** Uses asynchronous processing for faster annotation.

### Generate report
**Args:** `msmetaenhancer -i spectra.msp -r report.txt -o annotated.msp`
**Explanation:** Generates annotation coverage report.

### Batch processing
**Args:** `msmetaenhancer -i msp/ -o results/`
**Explanation:** Processes multiple MSP files.