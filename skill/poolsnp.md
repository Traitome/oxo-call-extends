---
name: poolsnp
category: epigenomics
description: poolsnp calls SNPs from pooled sequencing data using MPILEUP.
tags: [poolsnp, epigenomics, snp-calling, pooled]
author: oxo-call-community
source_url: "https://github.com/capoony/PoolSNP"
---

## Concepts

- **Tool Overview**: poolsnp identifies SNPs in pooled data.
- **Core Function**: Heuristic SNP calling from pools.
- **Algorithm**: Uses MPILEUP-based methods.
- **Input Format**: Accepts MPILEUP and FASTA files.
- **Output**: Produces VCF SNP calls.
- **Use Case**: Population genetics, pooled sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Calling Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `poolsnp --help`
**Explanation:** Shows available options and usage instructions.

### Call SNPs
**Args:** `poolsnp -i data.mpileup -r reference.fasta -o snps.vcf`
**Explanation:** Calls SNPs from pooled sequencing data.

### With parameters
**Args:** `poolsnp -i data.mpileup -r reference.fasta -p params.yaml -o snps.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `poolsnp -v -i data.mpileup -r reference.fasta -o snps.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `poolsnp -t 4 -i data.mpileup -r reference.fasta -o snps.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `poolsnp -i data.mpileup -r reference.fasta -o snps.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `poolsnp -i data.mpileup -r reference.fasta -o snps.vcf --report report.html`
**Explanation:** Generates HTML report.