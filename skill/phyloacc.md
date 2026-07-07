---
name: phyloacc
category: utility
description: phyloacc estimates substitution rate shifts in non-coding regions.
tags: [phyloacc, utility, substitution, bayesian]
author: oxo-call-community
source_url: "https://phyloacc.github.io/"
---

## Concepts

- **Tool Overview**: phyloacc estimates rate shifts.
- **Core Function**: Bayesian substitution rate analysis.
- **Algorithm**: Uses Bayesian estimation methods.
- **Input Format**: Accepts non-coding region files.
- **Output**: Produces rate shift analysis results.
- **Use Case**: Substitution analysis, rate estimation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Bayesian Estimation**: May have estimation errors.
- **Runtime**: Estimation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyloacc --help`
**Explanation:** Shows available options and usage instructions.

### Estimate rate shifts
**Args:** `phyloacc -i noncoding_regions.fasta -o rate_shifts.txt`
**Explanation:** Estimates substitution rate shifts.

### With parameters
**Args:** `phyloacc -i noncoding_regions.fasta -p params.yaml -o rate_shifts.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyloacc -v -i noncoding_regions.fasta -o rate_shifts.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyloacc -t 4 -i noncoding_regions.fasta -o rate_shifts.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyloacc -i noncoding_regions.fasta -o rate_shifts.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phyloacc -i noncoding_regions.fasta -o rate_shifts.txt --report report.html`
**Explanation:** Generates HTML report.