---
name: rad_haplotyper
category: variant-calling
description: RAD_Haplotyper builds SNP haplotypes from RAD (Restriction site Associated DNA) sequencing data.
tags: [rad_haplotyper, variant-calling, rad-seq, haplotypes]
author: oxo-call-community
source_url: "https://github.com/chollenbeck/rad_haplotyper"
---

## Concepts

- **Tool Overview**: rad_haplotyper builds haplotypes.
- **Core Function**: Haplotype construction.
- **Algorithm**: Uses RAD-seq data.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces haplotype files.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Depth**: Must be sufficient.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rad_haplotyper --help`
**Explanation:** Shows available options and usage instructions.

### Build haplotypes
**Args:** `rad_haplotyper build -i reads.fastq -o haplotypes.vcf`
**Explanation:** Constructs SNP haplotypes.

### With parameters
**Args:** `rad_haplotyper build -i reads.fastq -p params.yaml -o haplotypes.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rad_haplotyper -v build -i reads.fastq -o haplotypes.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rad_haplotyper -t 4 build -i reads.fastq -o haplotypes.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `rad_haplotyper build -i reads.fastq -r reference.fasta -o haplotypes.vcf`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `rad_haplotyper build -i reads.fastq -o haplotypes.vcf --report report.html`
**Explanation:** Generates HTML report.