---
name: hmnillumina
category: formatting
description: HmnIllumina is a parser for Illumina sequencing run data, extracting useful information from InterOp folders.
tags: [hmnillumina, illumina, sequencing, parser]
author: oxo-call-community
source_url: "https://github.com/guillaume-gricourt/HmnIllumina"
---

## Concepts

- **Illumina InterOp Parsing**: HmnIllumina parses Illumina InterOp folders containing binary files that record real-time sequencing metrics during run execution.
- **Run Information Extraction**: Extracts key sequencing metrics including cluster density, phasing/pre-phasing, quality scores, and cycle-by-cycle statistics.
- **Multi-platform Support**: Compatible with various Illumina sequencing platforms including NovaSeq, HiSeq, MiSeq, and NextSeq.
- **Quality Control Metrics**: Provides comprehensive quality metrics for assessing sequencing run performance and identifying potential issues.
- **Automated Report Generation**: Generates structured reports summarizing run quality, cluster passing filters, and sequencing yield.
- **Integration Ready**: Outputs data in formats suitable for downstream analysis pipelines and quality monitoring systems.

## Pitfalls

- **InterOp Folder Structure**: Requires proper Illumina InterOp folder structure; corrupted or incomplete folders may cause parsing failures.
- **Version Compatibility**: Different Illumina software versions may produce slightly different InterOp formats; verify compatibility with specific run versions.
- **Large Data Volumes**: High-output sequencing runs generate large InterOp files; ensure sufficient memory for parsing.
- **File Permissions**: Requires read access to the InterOp folder and all contained files.
- **Run Completion**: Parsing incomplete runs may yield incomplete or inaccurate metrics.
- **Platform Specificity**: Some metrics are platform-specific; ensure correct platform configuration for accurate interpretation.

## Examples

### Parse a single Illumina run directory
**Args:** `hmnillumina -i /path/to/run_directory -o run_report.json`
**Explanation:** Parses the InterOp folder from a completed Illumina sequencing run and generates a JSON report with all quality metrics.

### Generate HTML quality report
**Args:** `hmnillumina -i /path/to/run_directory -o report.html --format html`
**Explanation:** Generates a human-readable HTML report with visualizations of key sequencing metrics.

### Extract specific metrics only
**Args:** `hmnillumina -i /path/to/run_directory -o metrics.json --metrics cluster_density quality_score`
**Explanation:** Extracts only cluster density and quality score metrics, reducing output size for targeted analysis.

### Batch processing mode
**Args:** `hmnillumina -i /path/to/runs/ -o batch_results/ -b`
**Explanation:** Processes multiple run directories in batch mode, generating individual reports for each run.

### Validate run completeness
**Args:** `hmnillumina -i /path/to/run_directory --validate`
**Explanation:** Validates the integrity of the InterOp folder and checks for missing or corrupted files before full parsing.

### Extract phasing metrics
**Args:** `hmnillumina -i /path/to/run_directory -o phasing.json --phasing`
**Explanation:** Focuses on extracting phasing and pre-phasing metrics, critical for assessing sequencing cycle quality.