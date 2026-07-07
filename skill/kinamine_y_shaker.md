---
name: kinamine_y_shaker
category: proteomics
description: Kinamine is a tool to export all phospho-peptides that were discovered by a mass spec search program
tags: [kinamine_y_shaker, proteomics, mass-spectrometry, phosphopeptide]
author: oxo-call-community
source_url: "https://github.com/LaurieParkerLab/KinamineY-shaker"
---

## Concepts

- **Phosphopeptide Extraction**: Extracts phosphorylated peptides from mass spectrometry search results
- **Mass Spectrometry Data**: Works with mzML, mzXML, and other standard mass spec formats
- **Proteomics Analysis**: Integrates with major search engines like Mascot and MaxQuant
- **Post-translational Modification**: Focuses on phosphorylation site identification and characterization
- **Peptide Identification**: Filters and exports identified phosphopeptides with confidence scores
- **Data Export**: Generates CSV reports with detailed phosphopeptide information

## Pitfalls

- **Input Format Compatibility**: Requires specific search engine output formats
- **Search Engine Dependencies**: Results may vary based on search engine parameters
- **False Positive Identification**: Stringent filtering recommended to reduce false positives
- **Contamination Issues**: Sample contamination can affect identification accuracy
- **Missing Values**: Incomplete search results may cause processing errors
- **Database Versioning**: Protein database version should match search parameters

## Examples

### Export phosphopeptides from mzML
**Args:** `kinamine_y_shaker -i search_results.mzML -o phosphopeptides.csv`
**Explanation:** Extracts phosphopeptides from mass spectrometry results and exports to CSV.

### Filter by confidence score
**Args:** `kinamine_y_shaker -i results.mzXML -o filtered.csv -c 0.95`
**Explanation:** Filters phosphopeptides with confidence score >= 0.95 before export.

### Generate detailed report
**Args:** `kinamine_y_shaker -i mascot_results.dat -o report.csv --detailed`
**Explanation:** Generates a comprehensive report with additional peptide information.

### Batch processing mode
**Args:** `kinamine_y_shaker --batch -d search_results/ -o output/`
**Explanation:** Processes all result files in a directory and outputs to specified folder.

### Merge multiple results
**Args:** `kinamine_y_shaker --merge file1.dat file2.dat -o combined.csv`
**Explanation:** Combines phosphopeptide results from multiple search runs.

### Validate identifications
**Args:** `kinamine_y_shaker -i results.dat -o validated.csv --validate`
**Explanation:** Validates phosphopeptide identifications against a reference database.