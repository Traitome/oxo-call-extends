---
name: verifybamid
category: bioinformatics
description: VerifyBamID - BAM verification tool.
tags: [verifybamid, bam-processing, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/statgen/verifyBamID"
---

## Concepts

- **Tool Overview**: VerifyBamID - BAM file verification tool.
- **Core Function**: Verifies sample identity and detects contamination.
- **Input**: BAM file.
- **Output**: Verification report.
- **Installation**: Install via conda or source
- **Use Case**: Quality control, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Reference**: Requires reference genome.

## Examples

### Verify BAM
**Args:** `verifyBamID --bam input.bam --vcf ref.vcf --out report`
**Explanation:** Verify BAM file.

### With options
**Args:** `verifyBamID --bam input.bam --vcf ref.vcf --out report --maxThreads 8`
**Explanation:** Use 8 threads.
