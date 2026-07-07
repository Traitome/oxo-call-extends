---
name: rd-analyzer
category: utility
description: RD-Analyzer performs in silico region of difference (RD) analysis of Mycobacterium tuberculosis complex from sequence reads.
tags: [rd-analyzer, utility, tuberculosis, genotyping]
author: oxo-call-community
source_url: "https://github.com/xiaeryu/RD-Analyzer"
---

## Concepts

- **Tool Overview**: rd-analyzer analyzes TB.
- **Core Function**: RD analysis.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts sequence reads.
- **Output**: Produces RD profiles.
- **Use Case**: TB genotyping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Coverage**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rd-analyzer --help`
**Explanation:** Shows available options and usage instructions.

### Analyze RDs
**Args:** `rd-analyzer analyze -i reads.fastq -o rd_profile.txt`
**Explanation:** Analyzes region of difference.

### With parameters
**Args:** `rd-analyzer analyze -i reads.fastq -p params.yaml -o rd_profile.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rd-analyzer -v analyze -i reads.fastq -o rd_profile.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rd-analyzer -t 4 analyze -i reads.fastq -o rd_profile.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `rd-analyzer analyze -i reads.fastq -r reference.fasta -o rd_profile.txt`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `rd-analyzer analyze -i reads.fastq -o rd_profile.txt --report report.html`
**Explanation:** Generates HTML report.