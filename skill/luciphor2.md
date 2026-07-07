---
name: luciphor2
category: utility
description: Luciphor2 performs PTM-site localization on MS/MS data
tags: [luciphor2, utility, PTM, proteomics]
author: oxo-call-community
source_url: "http://luciphor2.sourceforge.net/"
---

## Concepts

- **Tool Overview**: luciphor2 v2020_04_03 is a tool for post-translational modification (PTM) site localization from MS/MS data.
- **Core Function**: Identifies and localizes PTM sites on peptides using tandem mass spectrometry data.
- **PTM Types**: Supports various PTMs including phosphorylation, acetylation, methylation, and glycosylation.
- **Input/Output**: Input: MS/MS spectra in mzML or mzXML format; Output: Localized PTM sites with confidence scores.
- **Installation**: `conda install -c bioconda luciphor2`
- **Key Features**: High accuracy PTM localization, supports multiple search engines, provides confidence metrics.

## Pitfalls

- **Spectra Quality**: Requires high-quality MS/MS spectra for accurate localization.
- **Database Dependencies**: Depends on protein database for peptide identification.
- **Search Engine Compatibility**: May require specific search engine output formats.
- **Computation Time**: Processing large datasets can be time-consuming.
- **False Positives**: May produce false positive PTM localizations requiring manual validation.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Run PTM localization
**Args:** `luciphor2 -i spectra.mzML -d database.fasta -o results.txt`
**Explanation:** Performs PTM site localization on MS/MS spectra.

### Phosphorylation only
**Args:** `luciphor2 -i spectra.mzML -d database.fasta -m phosphorylation -o results.txt`
**Explanation:** Focuses on phosphorylation site localization.

### Threads
**Args:** `luciphor2 -i spectra.mzML -d database.fasta -t 8 -o results.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum confidence
**Args:** `luciphor2 -i spectra.mzML -d database.fasta -c 0.95 -o results.txt`
**Explanation:** Sets minimum confidence threshold to 95%.

### Output format
**Args:** `luciphor2 -i spectra.mzML -d database.fasta -f csv -o results.csv`
**Explanation:** Outputs results in CSV format.

### Help documentation
**Args:** `luciphor2 --help`
**Explanation:** Displays all available options and parameters.