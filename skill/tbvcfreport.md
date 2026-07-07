---
name: tbvcfreport
category: visualization
description: TBVcfReport - Generates interactive HTML reports from SnpEff-annotated M. tuberculosis VCF files.
tags: [tbvcfreport, tuberculosis, vcf, html-report, snpeff, combat-tb, visualization]
author: oxo-call-community
source_url: "https://github.com/COMBAT-TB/tbvcfreport"
---

## Concepts

- **Tool Overview**: tbvcfreport (v0.1.7+) - A tool that parses SnpEff-annotated VCF files from M. tuberculosis and generates interactive HTML reports with links to the Combat-TB-Explorer database.
- **Core Function**: Converts raw VCF data into human-readable HTML reports showing variants, annotations, drug resistance associations, and lineage information.
- **Input**: SnpEff-annotated VCF file(s) from M. tuberculosis WGS. Optionally provide TBProfiler JSON report for integrated results.
- **Output**: Interactive HTML report files with variant details, functional annotations, and database links.
- **Installation**: `pip install tbvcfreport` or `conda install -c bioconda tbvcfreport`
- **Key Feature**: Provides links to Combat-TB-NeoDB for extended variant exploration in a Neo4j graph database.

## Pitfalls

- **SnpEff Required**: Input VCF must be annotated by SnpEff - unannotated VCFs will not work.
- **Database Access**: Links to Combat-TB-Explorer require network access or local NeoDB instance.
- **Python Version**: Requires Python 3.6+ (versions 1.0+ require Python 3.10+).
- **Filter Defaults**: Default filtering removes intergenic variants - use `-nf` flag to keep all variants.

## Examples

### Basic report generation
**Args:** `tbvcfreport generate vcf_directory/`
**Explanation:** Scan directory for VCF files and generate HTML reports for each.

### With TBProfiler report
**Args:** `tbvcfreport generate -t tbprofiler.json vcf_directory/`
**Explanation:** Include TBProfiler results in the HTML report for comprehensive drug resistance view.

### Keep all variants
**Args:** `tbvcfreport generate -nf vcf_directory/`
**Explanation:** Use `--no-filter-udi` to include upstream, downstream, and intergenic variants in report.

### Install and check help
**Args:** `pip install tbvcfreport && tbvcfreport --help`
**Explanation:** Install tool and display available commands and options.
