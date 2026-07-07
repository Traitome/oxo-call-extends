---
name: pbhoover
category: qc
description: pbhoover is a variant caller for legacy and low coverage PacBio long-read sequencing data.
tags: [pbhoover, qc, variant-calling, pacbio]
author: oxo-call-community
source_url: "https://gitlab.com/LPCDRP/pbhoover"
---

## Concepts

- **Tool Overview**: pbhoover calls variants from long reads.
- **Core Function**: Detects variants in low coverage data.
- **Algorithm**: Uses error correction and variant detection.
- **Input Format**: Accepts BAM/SAM alignments.
- **Output**: Produces VCF variant calls.
- **Use Case**: Low coverage variant calling, legacy data.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Coverage Requirements**: Designed for low coverage data.
- **Error Rates**: PacBio error rates affect accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbhoover --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `pbhoover -i alignments.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from BAM file.

### With coverage threshold
**Args:** `pbhoover -i alignments.bam -r reference.fasta -o variants.vcf --min-coverage 5`
**Explanation:** Sets minimum coverage threshold.

### Verbose mode
**Args:** `pbhoover -v -i alignments.bam -r reference.fasta -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbhoover -t 4 -i alignments.bam -r reference.fasta -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbhoover -i alignments.bam -r reference.fasta -o variants.gvcf --gvcf`
**Explanation:** Outputs in GVCF format.

### Generate report
**Args:** `pbhoover -i alignments.bam -r reference.fasta -o variants.vcf --report report.html`
**Explanation:** Generates HTML report.