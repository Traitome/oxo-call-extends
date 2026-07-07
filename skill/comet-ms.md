---
name: comet-ms
category: utility
description: Tandem mass spectrometry sequence database search tool
tags: [comet-ms, mass-spectrometry, proteomics, database-search, bioinformatics]
author: oxo-call-community
source_url: "https://uwpr.github.io/Comet/"
---

## Concepts

- **Tool Overview**: Comet is an open-source tandem mass spectrometry (MS/MS) sequence database search tool for identifying peptides and proteins from mass spectrometry data.
- **Core Function**: Searches MS/MS spectra against protein sequence databases to identify peptide-spectrum matches (PSMs).
- **Algorithm**: Uses cross-correlation scoring and probabilistic models to match experimental spectra with theoretical fragment ions.
- **Input**: MGF, MSTransform, or mzXML format MS/MS spectra files, protein sequence database in FASTA format.
- **Output**: Search results in pepXML, protXML, or other standard formats with PSMs and confidence scores.
- **Application**: Proteomics identification, post-translational modification analysis, and protein characterization.
- **Installation**: Install via bioconda: `conda install -c bioconda comet-ms`

## Pitfalls

- **Database Size**: Large databases increase search time and false discovery rate.
- **Modification Specification**: Must correctly specify variable and fixed modifications.
- **Mass Tolerance**: Incorrect tolerance settings reduce identification accuracy.
- **Decoy Database**: Required for false discovery rate estimation.
- **Parameter File**: Requires properly configured parameter file for optimal results.

## Examples

### Search MS/MS spectra
**Args:** `comet-ms -P params.txt -D database.fasta spectra.mgf`
**Explanation:** Searches spectra against protein database using parameter file.

### With custom parameters
**Args:** `comet-ms -P params.txt -s 1 -D database.fasta spectra.mgf`
**Explanation:** Runs search with specific enzyme digest settings.

### Generate pepXML output
**Args:** `comet-ms -P params.txt -N 1 -D database.fasta spectra.mgf`
**Explanation:** Generates pepXML format output for downstream analysis.

### Display help
**Args:** `comet-ms --help`
**Explanation:** Shows all available options and usage information.