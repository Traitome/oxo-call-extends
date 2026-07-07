---
name: lamps
category: annotation
description: Liverpool Annotation of Metabolites using Mass Spectrometry
tags: [lamps, annotation, metabolomics, mass-spectrometry, metabolite]
author: oxo-call-community
source_url: "https://github.com/MJW1860/LAMPS"
---

## Concepts

- **Metabolite Annotation**: Annotates metabolites from mass spectrometry data
- **MS/MS Support**: Uses tandem mass spectrometry for identification
- **Database Search**: Searches against metabolite databases
- **Fragment Matching**: Matches fragment patterns for identification
- **Confidence Scoring**: Provides confidence scores for annotations
- **Metabolomics**: Designed for metabolomics workflows

## Pitfalls

- **Spectral Quality**: Poor quality spectra give incorrect annotations
- **Database Coverage**: Limited database coverage affects identification
- **Isomers**: Structural isomers may have identical spectra
- **Concentration Effects**: Ion suppression affects detection
- **Fragmentation Energy**: Different energies produce different fragments
- **Adduct Detection**: Multiple adducts complicate interpretation

## Examples

### Annotate metabolites
**Args:** `lamps -i spectrum.mgf -o results.csv`
**Explanation:** Annotates metabolites from MS/MS spectra.

### Specify database
**Args:** `lamps -i spectrum.mgf -d hmdb.csv -o results.csv`
**Explanation:** Uses HMDB metabolite database.

### Set mass tolerance
**Args:** `lamps -i spectrum.mgf -t 0.01 -o results.csv`
**Explanation:** Sets 0.01 Da mass tolerance.

### Filter by score
**Args:** `lamps -i spectrum.mgf -s 0.8 -o results.csv`
**Explanation:** Only keeps annotations with score >= 0.8.

### Export report
**Args:** `lamps -i spectrum.mgf -o results.csv --report`
**Explanation:** Creates detailed annotation report.

### Batch processing
**Args:** `lamps batch -d spectra/ -o results/`
**Explanation:** Processes multiple spectral files.