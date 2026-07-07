---
name: pepr
category: epigenomics
description: PePr calls peaks from replicated ChIP-Seq data.
tags: [pepr, epigenomics, chip-seq, peak-calling]
author: oxo-call-community
source_url: "https://github.com/shawnzhangyx/PePr/"
---

## Concepts

- **Tool Overview**: PePr calls ChIP-seq peaks.
- **Core Function**: Identifies peaks from replicated data.
- **Algorithm**: Uses peak calling and prioritization.
- **Input Format**: Accepts ChIP-seq alignment files.
- **Output**: Produces peak calls.
- **Use Case**: ChIP-seq analysis, peak calling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Replication Quality**: Requires proper replication.
- **Peak Definition**: Different parameters give different results.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pepr --help`
**Explanation:** Shows available options and usage instructions.

### Call peaks
**Args:** `pepr -c chip1.bam chip2.bam -i input1.bam input2.bam -o peaks.bed`
**Explanation:** Calls peaks from replicated ChIP-seq.

### With parameters
**Args:** `pepr -c chip1.bam chip2.bam -i input1.bam input2.bam -p params.yaml -o peaks.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pepr -v -c chip1.bam chip2.bam -i input1.bam input2.bam -o peaks.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pepr -t 4 -c chip1.bam chip2.bam -i input1.bam input2.bam -o peaks.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pepr -c chip1.bam chip2.bam -i input1.bam input2.bam -o peaks.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `pepr -c chip1.bam chip2.bam -i input1.bam input2.bam -o peaks.bed --report report.html`
**Explanation:** Generates HTML report.