---
name: verifybamid2
category: bioinformatics
description: VerifyBamID2 - BAM verification tool.
tags: [verifybamid2, bam-processing, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Griffan/VerifyBamID2"
---

## Concepts

- **Tool Overview**: VerifyBamID2 - BAM file verification tool.
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
**Args:** `verifybamid2 --bam input.bam --vcf ref.vcf --out report`
**Explanation:** Verify BAM file.

### With options
**Args:** `verifybamid2 --bam input.bam --vcf ref.vcf --out report --threads 8`
**Explanation:** Use 8 threads.
