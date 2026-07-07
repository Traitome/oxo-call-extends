---
name: irida-staramr-results
category: utility
description: Batch downloads StarAMR antimicrobial resistance analysis results from IRIDA into spreadsheets.
tags: [irida-staramr-results, StarAMR, antimicrobial resistance, AMR, ResFinder]
author: oxo-call-community
source_url: "https://github.com/phac-nml/irida-staramr-results"
---

## Concepts

- **StarAMR Integration**: irida-staramr-results (v0.3.1) exports antimicrobial resistance (AMR) gene detection results from IRIDA's StarAMR pipeline into structured reports.
- **Resistance Gene Detection**: Extracts findings from ResFinder and PointFinder databases, identifying acquired resistance genes and chromosomal mutations.
- **Multi-database Support**: Integrates results from multiple AMR databases including ResFinder, PointFinder, PlasmidFinder, and MLST.
- **Spreadsheet Generation**: Produces Excel/CSV reports with gene names, resistance phenotypes, sequence identities, and database matches.
- **Batch Processing**: Enables bulk export of AMR results from multiple samples and analyses.
- **Plasmid Identification**: Includes plasmid replicon typing results alongside resistance gene detection.

## Pitfalls

- **Database Versioning**: AMR detection relies on database versions used in the original StarAMR analysis.
- **Threshold Sensitivity**: Results may vary based on identity and coverage thresholds used during analysis.
- **False Positives**: Partial gene matches may produce false positive calls requiring manual review.
- **IRIDA API Rate Limits**: Large batch exports may trigger API rate limiting.
- **Result Interpretation**: Requires expertise to interpret complex AMR profiles and phenotype predictions.
- **Incomplete Databases**: Some rare resistance determinants may not be captured by current databases.

## Examples

### Basic AMR results export
**Args:** `irida-staramr-results --project "AMR Surveillance" --output amr_results.csv`
**Explanation:** Exports StarAMR results from the specified project into a CSV file with resistance gene information.

### Include plasmid information
**Args:** `irida-staramr-results --project "Plasmid Study" --output plasmid_report.csv --include-plasmids`
**Explanation:** Generates a report that includes plasmid replicon typing results along with resistance genes.

### Export with MLST data
**Args:** `irida-staramr-results --project "Epidemiology" --output mlst_amr.csv --include-mlst`
**Explanation:** Combines AMR detection results with multi-locus sequence typing (MLST) information.

### Filter by resistance phenotype
**Args:** `irida-staramr-results --project "Drug Resistance" --phenotype "cephalosporin" --output cephalosporin_resistance.csv`
**Explanation:** Filters and exports only results showing resistance to specific antimicrobial classes.

### Batch export from analysis IDs
**Args:** `irida-staramr-results --analysis-ids analysis_ids.txt --output batch_results.csv`
**Explanation:** Processes a list of specific analysis IDs and exports their AMR results.

### Generate summary statistics
**Args:** `irida-staramr-results --project "Screening" --output summary.csv --summary-only`
**Explanation:** Creates a condensed summary report with aggregate statistics rather than detailed gene-level data.