---
name: ngs-chew
category: qc
description: NGS-Chew performs quality control and sanity checking of germline NGS data.
tags: [ngs-chew, qc, germline, quality-control]
author: oxo-call-community
source_url: "https://github.com/bihealth/ngs-chew"
---

## Concepts

- **Tool Overview**: NGS-Chew provides comprehensive QC for germline sequencing data.
- **Core Function**: Performs quality checks and generates reports.
- **Algorithm**: Analyzes sequencing metrics and variant calls.
- **Input Format**: Accepts BAM, VCF, and sequencing metrics files.
- **Output**: Produces QC reports and metrics summaries.
- **Use Case**: Quality control, data validation, and pipeline validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Requirements**: Requires specific input files.
- **Memory Usage**: Large datasets require memory.
- **Configuration**: Requires proper configuration.
- **Report Interpretation**: Reports may require domain knowledge.
- **Dependency Management**: Requires proper environment setup.

## Examples

### Display help
**Args:** `ngs-chew --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `ngs-chew --input config.yaml --output report/`
**Explanation:** Runs QC using configuration file.

### BAM QC
**Args:** `ngs-chew bam --input alignment.bam --output bam_qc/`
**Explanation:** Performs BAM-specific QC.

### VCF QC
**Args:** `ngs-chew vcf --input variants.vcf --output vcf_qc/`
**Explanation:** Performs VCF-specific QC.

### Multi-sample
**Args:** `ngs-chew multi --input samples.csv --output reports/`
**Explanation:** Processes multiple samples.

### Summary report
**Args:** `ngs-chew summary --input qc_results/ --output summary.html`
**Explanation:** Generates summary HTML report.

### Verbose mode
**Args:** `ngs-chew --input config.yaml --output report/ -v`
**Explanation:** Runs with verbose output.