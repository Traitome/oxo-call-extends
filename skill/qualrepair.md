---
name: qualrepair
category: qc
description: QualRepair updates FASTQ quality scores from a subsequence FASTQ file.
tags: [qualrepair, qc, quality-scores, fastq]
author: oxo-call-community
source_url: "https://github.com/clintval/qualrepair"
---

## Concepts

- **Tool Overview**: qualrepair repairs quality scores.
- **Core Function**: Quality score update.
- **Algorithm**: Uses subsequence mapping.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces repaired FASTQ.
- **Use Case**: Data correction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Subsequence Match**: Must be found.
- **File Format**: Must be correct.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qualrepair --help`
**Explanation:** Shows available options and usage instructions.

### Repair quality scores
**Args:** `qualrepair repair -i input.fastq -s subseq.fastq -o repaired.fastq`
**Explanation:** Updates quality scores.

### With parameters
**Args:** `qualrepair repair -i input.fastq -s subseq.fastq -p params.yaml -o repaired.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qualrepair -v repair -i input.fastq -s subseq.fastq -o repaired.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qualrepair -t 4 repair -i input.fastq -s subseq.fastq -o repaired.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With quality cutoff
**Args:** `qualrepair repair -i input.fastq -s subseq.fastq -q 20 -o repaired.fastq`
**Explanation:** Uses quality cutoff.

### Generate report
**Args:** `qualrepair repair -i input.fastq -s subseq.fastq -o repaired.fastq --report report.html`
**Explanation:** Generates HTML report.