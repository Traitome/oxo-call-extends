---
name: quickmirseq
category: expression
description: QuickmiRseq is a pipeline for fast and accurate quantification of known miRNAs and isomiRs by joint processing multiple samples.
tags: [quickmirseq, expression, mirna, isomir]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/quickmirseq/"
---

## Concepts

- **Tool Overview**: quickmirseq quantifies miRNAs.
- **Core Function**: miRNA expression analysis.
- **Algorithm**: Uses mapping methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces expression counts.
- **Use Case**: miRNA profiling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Database**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quickmirseq --help`
**Explanation:** Shows available options and usage instructions.

### Run quantification
**Args:** `quickmirseq quantify -i reads.fastq -o counts.txt`
**Explanation:** Quantifies miRNA expression.

### With parameters
**Args:** `quickmirseq quantify -i reads.fastq -p params.yaml -o counts.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quickmirseq -v quantify -i reads.fastq -o counts.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quickmirseq -t 4 quantify -i reads.fastq -o counts.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Multiple samples
**Args:** `quickmirseq quantify -i sample1.fastq,sample2.fastq -o counts.txt`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `quickmirseq quantify -i reads.fastq -o counts.txt --report report.html`
**Explanation:** Generates HTML report.