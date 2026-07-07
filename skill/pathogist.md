---
name: pathogist
category: utility
description: PathOGiST performs calibrated multi-criterion genomic analysis for public health microbiology.
tags: [pathogist, utility, public-health, microbiology]
author: oxo-call-community
source_url: "https://github.com/WGS-TB/PathOGiST"
---

## Concepts

- **Tool Overview**: PathOGiST analyzes genomic data for public health.
- **Core Function**: Performs multi-criterion pathogen analysis.
- **Algorithm**: Uses calibrated scoring methods.
- **Input Format**: Accepts genome sequences and metadata.
- **Output**: Produces analysis reports and classifications.
- **Use Case**: Public health microbiology, outbreak investigation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Calibration**: Results depend on calibration parameters.
- **Database Quality**: Results depend on reference data.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathogist --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pathogist -i genome.fasta -o results/`
**Explanation:** Performs multi-criterion analysis.

### With metadata
**Args:** `pathogist -i genome.fasta -m metadata.txt -o results/`
**Explanation:** Uses metadata for analysis.

### Verbose mode
**Args:** `pathogist -v -i genome.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathogist -t 4 -i genome.fasta -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pathogist -i genome.fasta -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pathogist -i genome.fasta -o results/ -r report.pdf`
**Explanation:** Generates PDF report.