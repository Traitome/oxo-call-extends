---
name: proact
category: formatting
description: proact detects provirus activity from host sequencing data.
tags: [proact, formatting, provirus, viral-integration]
author: oxo-call-community
source_url: "https://github.com/mujiezhang/ProAct"
---

## Concepts

- **Tool Overview**: proact identifies provirus activity.
- **Core Function**: Provirus detection.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts BAM/FASTQ files.
- **Output**: Produces activity predictions.
- **Use Case**: Viral integration analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Detection Sensitivity**: May have false positives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proact --help`
**Explanation:** Shows available options and usage instructions.

### Detect provirus
**Args:** `proact -i aligned.bam -o provirus_results.txt`
**Explanation:** Detects provirus activity from sequencing data.

### With parameters
**Args:** `proact -i aligned.bam -p params.yaml -o provirus_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proact -v -i aligned.bam -o provirus_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proact -t 4 -i aligned.bam -o provirus_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proact -i aligned.bam -o provirus_results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `proact -i aligned.bam -o provirus_results.txt --report report.html`
**Explanation:** Generates HTML report.