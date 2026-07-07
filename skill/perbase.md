---
name: perbase
category: formatting
description: perbase calculates per-base metrics on BAM/CRAM files.
tags: [perbase, formatting, bam, cram]
author: oxo-call-community
source_url: "https://github.com/sstadick/perbase"
---

## Concepts

- **Tool Overview**: perbase analyzes BAM/CRAM files.
- **Core Function**: Calculates per-base metrics.
- **Algorithm**: Uses alignment position analysis.
- **Input Format**: Accepts BAM/CRAM alignment files.
- **Output**: Produces per-base metrics.
- **Use Case**: Alignment QC, coverage analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAM files require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Coverage Calculation**: May have coverage gaps.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `perbase --help`
**Explanation:** Shows available options and usage instructions.

### Calculate metrics
**Args:** `perbase -i alignments.bam -o metrics.txt`
**Explanation:** Calculates per-base metrics.

### With reference
**Args:** `perbase -i alignments.bam -r reference.fasta -o metrics.txt`
**Explanation:** Uses reference for metrics calculation.

### Verbose mode
**Args:** `perbase -v -i alignments.bam -o metrics.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `perbase -t 4 -i alignments.bam -o metrics.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `perbase -i alignments.bam -o metrics.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `perbase -i alignments.bam -o metrics.txt --report report.html`
**Explanation:** Generates HTML report.