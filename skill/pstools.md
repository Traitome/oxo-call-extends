---
name: pstools
category: programming
description: pstools is a toolkit for processing fully phased sequences.
tags: [pstools, programming, phased-sequences, genetics]
author: oxo-call-community
source_url: "https://github.com/shilpagarg/pstools"
---

## Concepts

- **Tool Overview**: pstools handles phased sequences.
- **Core Function**: Phased sequence processing.
- **Algorithm**: Uses phasing algorithms.
- **Input Format**: Accepts phased VCF/FASTA files.
- **Output**: Produces phased data.
- **Use Case**: Genomics phasing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Phasing Quality**: Affects accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pstools --help`
**Explanation:** Shows available options and usage instructions.

### Process phased sequences
**Args:** `pstools -i phased.vcf -o phased_output.txt`
**Explanation:** Processes fully phased sequence data.

### With parameters
**Args:** `pstools -i phased.vcf -p params.yaml -o phased_output.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pstools -v -i phased.vcf -o phased_output.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pstools -t 4 -i phased.vcf -o phased_output.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pstools -i phased.vcf -o phased_output.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pstools -i phased.vcf -o phased_output.txt --report report.html`
**Explanation:** Generates HTML report.