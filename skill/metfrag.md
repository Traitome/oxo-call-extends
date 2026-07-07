---
name: metfrag
category: annotation
description: MetFrag is a freely available software for the annotation of high precision tandem mass spectra of metabolites which is a first and critical step for the identification of a molecular structure.
tags: [metfrag, annotation, metabolomics]
author: oxo-call-community
source_url: "http://c-ruttkies.github.io/MetFrag/"
---

## Concepts

- **Tool Overview**: MetFrag v2.4.5 is a software for annotation of high precision tandem mass spectra of metabolites, enabling molecular structure identification.
- **Core Function**: Annotates tandem mass spectra for metabolite identification.
- **In Silico Fragmentation**: Fragments candidate molecules in silico and matches against mass-to-charge values.
- **Score Calculation**: Calculates scores based on fragment peak matches for candidate spectrum assignment.
- **Database Integration**: Supports multiple metabolite databases for candidate generation.
- **Input/Output**: Accepts mass spectra data; outputs annotated metabolite identifications.

## Pitfalls

- **Database Completeness**: Annotation quality depends on database completeness.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal scoring.
- **False Positives**: May produce false positive annotations.
- **Data Quality**: Annotation accuracy depends on input spectrum quality.

## Examples

### Annotate mass spectrum
**Args:** `metfrag -i spectrum.mzML -o annotations.txt`
**Explanation:** Annotates tandem mass spectrum for metabolite identification.

### With custom database
**Args:** `metfrag -i spectrum.mzML -d database.csv -o annotations.txt`
**Explanation:** Uses custom metabolite database for annotation.

### Adjust scoring parameters
**Args:** `metfrag -i spectrum.mzML -o annotations.txt -s 0.8`
**Explanation:** Sets minimum score threshold to 0.8.

### Detailed output
**Args:** `metfrag -i spectrum.mzML -o annotations.txt -v`
**Explanation:** Generates detailed annotation report.

### Batch processing
**Args:** `metfrag -i spectra/ -o annotations/`
**Explanation:** Processes multiple spectra in batch mode.