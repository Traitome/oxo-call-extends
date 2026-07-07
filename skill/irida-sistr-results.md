---
name: irida-sistr-results
category: utility
description: Exports SISTR (Salmonella In Silico Typing Resource) results from IRIDA into a consolidated report.
tags: [irida-sistr-results, SISTR, Salmonella, serotyping, cgMLST]
author: oxo-call-community
source_url: "https://github.com/phac-nml/irida-sistr-results"
---

## Concepts

- **SISTR Integration**: irida-sistr-results (v0.6.0) integrates with the SISTR pipeline in IRIDA to export Salmonella serotyping results into spreadsheets and reports.
- **Salmonella Serotyping**: The tool extracts serovar predictions, antigen gene detection results, and cgMLST (core genome Multi-Locus Sequence Typing) profiles from IRIDA analyses.
- **Output Formats**: Generates CSV reports containing cgMLST allelic profiles, allele call details in JSON format, and summary statistics for multiple samples.
- **Quality Control**: Results include PASS/FAIL/WARNING status based on genome quality metrics and database matching confidence.
- **Batch Processing**: Supports bulk export of results from multiple SISTR analyses run through IRIDA.
- **Metadata Integration**: Combines typing results with sample metadata for comprehensive reporting.

## Pitfalls

- **IRIDA Version Compatibility**: Requires specific IRIDA versions to access SISTR results API endpoints.
- **Network Connectivity**: Requires stable connection to IRIDA server for data retrieval.
- **Result Availability**: Only exports results for completed SISTR analyses; running or failed analyses cannot be exported.
- **Data Format Changes**: Output structure may vary between different SISTR pipeline versions.
- **Authentication**: Requires valid IRIDA credentials with appropriate project access permissions.
- **Large Datasets**: Exporting results from hundreds of samples may require increased memory allocation.

## Examples

### Export SISTR results to CSV
**Args:** `irida-sistr-results --project "Salmonella Study" --output results.csv`
**Explanation:** Exports SISTR typing results from a specific IRIDA project into a CSV file containing serovar predictions and cgMLST profiles.

### Export with detailed allele information
**Args:** `irida-sistr-results --project "Outbreak Investigation" --output detailed_report.csv --include-alleles`
**Explanation:** Generates a comprehensive report including detailed allele call information for each detected antigen gene.

### Filter by analysis status
**Args:** `irida-sistr-results --project "Surveillance" --status COMPLETED --output completed_results.csv`
**Explanation:** Exports only successfully completed SISTR analyses, excluding failed or running jobs.

### Batch export from multiple projects
**Args:** `irida-sistr-results --projects-file project_list.txt --output combined_report.csv`
**Explanation:** Processes a list of projects specified in a text file and combines all SISTR results into a single report.

### Include Mash distance information
**Args:** `irida-sistr-results --project "Phylogenetics" --output mash_report.csv --include-mash`
**Explanation:** Adds Mash MinHash distance calculations to the exported results for phylogenetic comparison.

### Dry run mode
**Args:** `irida-sistr-results --project "Test Project" --dry-run`
**Explanation:** Shows what would be exported without actually generating any files, useful for verification before export.