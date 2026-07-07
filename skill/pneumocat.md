---
name: pneumocat
category: utility
description: pneumocat performs pneumococcal capsular typing.
tags: [pneumocat, utility, typing, bacteria]
author: oxo-call-community
source_url: "https://github.com/phe-bioinformatics/pneumocat"
---

## Concepts

- **Tool Overview**: pneumocat types S.pneumoniae capsular serotypes.
- **Core Function**: Capsular type assignment.
- **Algorithm**: Uses sequence matching methods.
- **Input Format**: Accepts Illumina sequencing data.
- **Output**: Produces capsular typing results.
- **Use Case**: Pneumococcal epidemiology, clinical microbiology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Typing Accuracy**: May have classification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pneumocat --help`
**Explanation:** Shows available options and usage instructions.

### Type capsular serotype
**Args:** `pneumocat -i reads.fastq -o typing.txt`
**Explanation:** Assigns capsular type to S.pneumoniae.

### With parameters
**Args:** `pneumocat -i reads.fastq -p params.yaml -o typing.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pneumocat -v -i reads.fastq -o typing.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pneumocat -t 4 -i reads.fastq -o typing.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pneumocat -i reads.fastq -o typing.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pneumocat -i reads.fastq -o typing.txt --report report.html`
**Explanation:** Generates HTML report.