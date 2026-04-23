---
name: bumbershoot
category: annotation
description: Tool suite for analyzing shotgun proteomic data
tags: [bumbershoot, proteomics, mass-spectrometry, peptide]
author: oxo-call-community
source_url: "https://proteowizard.sourceforge.net"
---

## Concepts

- **Tool Overview**: Bumbershoot is a suite for analyzing shotgun proteomic data.
- **Core Function**: Identifies peptides and proteins from mass spectrometry data.
- **Components**: Peptide identification, protein inference, and quantification tools.
- **Input**: Mass spectrometry files (mzML, mzXML) and protein database.
- **Output**: Peptide-spectrum matches, protein identifications, and quantification.
- **Installation**: Install via bioconda: `conda install -c bioconda bumbershoot`

## Pitfalls

- **Database Required**: Requires protein sequence database for identification.
- **File Format**: Convert raw data to mzML/mzXML before analysis.
- **FDR Control**: Apply false discovery rate filtering to results.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Identify peptides
**Args:** `tide-search spectra.mzML database.fa -o peptides.tsv`
**Explanation:** Searches mass spectra against protein database for peptide identification.

### Percolate results
**Args:** `percolator peptides.tsv -o filtered_peptides.tsv`
**Explanation:** Applies FDR filtering to peptide identifications.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
