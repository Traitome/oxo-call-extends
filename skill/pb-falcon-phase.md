---
name: pb-falcon-phase
category: variant-calling
description: pb-falcon-phase provides phasing utilities for PacBio sequencing data.
tags: [pb-falcon-phase, variant-calling, phasing]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pb-falcon-phase"
---

## Concepts

- **Tool Overview**: pb-falcon-phase performs haplotype phasing.
- **Core Function**: Phases genetic variants using long reads.
- **Algorithm**: Uses haplotype-aware phasing algorithms.
- **Input Format**: Accepts variant calls and alignments.
- **Output**: Produces phased haplotypes.
- **Use Case**: Variant phasing, population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Coverage**: Requires sufficient sequencing coverage.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `falcon-phase --help`
**Explanation:** Shows available options and usage instructions.

### Run phasing
**Args:** `falcon-phase -v variants.vcf -b alignments.bam -o phased.vcf`
**Explanation:** Phases variants from VCF and BAM files.

### With reference
**Args:** `falcon-phase -v variants.vcf -r reference.fasta -o phased.vcf`
**Explanation:** Uses reference genome for phasing.

### Verbose mode
**Args:** `falcon-phase -v -i input.vcf -o phased.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `falcon-phase -t 8 -v variants.vcf -o phased.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `falcon-phase -v variants.vcf -o phased.hap --haplotype`
**Explanation:** Outputs in haplotype format.

### Generate report
**Args:** `falcon-phase -v variants.vcf -o phased.vcf --report report.html`
**Explanation:** Generates HTML report.