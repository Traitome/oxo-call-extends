---
name: plasmidhawk
category: annotation
description: plasmidhawk detects lab-of-origin of plasmids.
tags: [plasmidhawk, annotation, plasmid, pangenome]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/plasmidhawk"
---

## Concepts

- **Tool Overview**: plasmidhawk identifies plasmid origins.
- **Core Function**: Lab-of-origin detection for plasmids.
- **Algorithm**: Uses pangenome analysis methods.
- **Input Format**: Accepts plasmid sequence files.
- **Output**: Produces origin detection results.
- **Use Case**: Plasmid tracking, forensic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on training data quality.
- **Detection Accuracy**: May have identification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plasmidhawk --help`
**Explanation:** Shows available options and usage instructions.

### Detect plasmid origin
**Args:** `plasmidhawk -i plasmid.fasta -o origin_result.txt`
**Explanation:** Detects lab-of-origin of input plasmids.

### With parameters
**Args:** `plasmidhawk -i plasmid.fasta -p params.yaml -o origin_result.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plasmidhawk -v -i plasmid.fasta -o origin_result.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plasmidhawk -t 4 -i plasmid.fasta -o origin_result.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plasmidhawk -i plasmid.fasta -o origin_result.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `plasmidhawk -i plasmid.fasta -o origin_result.txt --report report.html`
**Explanation:** Generates HTML report.