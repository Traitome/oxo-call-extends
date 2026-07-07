---
name: easypqp
category: proteomics
description: "EasyPQP: Simple library generation for OpenSWATH"
tags: [easypqp, proteomics, OpenSWATH, mass-spectrometry, peptide-library]
author: oxo-call-community
source_url: "https://github.com/grosenberger/easypqp"
---

## Concepts

- **Tool Overview**: EasyPQP is a Python package for simplified peptide query parameter library generation for OpenSWATH mass spectrometry analysis.
- **Core Function**: Generates spectral libraries from database search results for targeted proteomics analysis.
- **Input/Output**: Input: pepXML files from MSFragger or other search engines. Output: Library files for OpenSWATH.
- **Algorithm**: Processes peptide identification results, validates statistics, and calibrates retention times.
- **Key Features**: Fast library generation, supports PyProphet/PeptideProphet validation, non-linear RT alignment, run-specific libraries.
- **Installation**: `pip install easypqp` or `conda install -c bioconda easypqp`

## Pitfalls

- **Python Version**: Requires Python 3.6+.
- **Dependency Management**: Best installed in a virtual environment.
- **Input Format**: Requires pepXML format from supported search engines.
- **Retention Time Calibration**: Needs internal or external standards for RT calibration.
- **Memory Usage**: Large datasets require significant RAM.

## Examples

### Basic library generation
**Args:** `easypqp library --input search.pep.xml --output library.pqp`
**Explanation:** Generates a PQP library from pepXML search results.

### Convert format
**Args:** `easypqp convert --input search.pep.xml --output library.tsv`
**Explanation:** Converts pepXML to tabular format.

### With retention time calibration
**Args:** `easypqp library --input search.pep.xml --output library.pqp --rt-calibration std.pep.xml`
**Explanation:** Uses external standard for retention time calibration.

### With PyProphet validation
**Args:** `easypqp library --input search.pep.xml --output library.pqp --validation pyprophet`
**Explanation:** Uses PyProphet for statistical validation.

### Generate run-specific libraries
**Args:** `easypqp library --input search.pep.xml --output library.pqp --run-specific`
**Explanation:** Generates run-specific libraries for non-linear RT alignment.