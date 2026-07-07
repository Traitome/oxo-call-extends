---
name: phenix
category: variant-calling
description: phenix provides SNP calling pipeline for public health analysis.
tags: [phenix, variant-calling, snp, pipeline]
author: oxo-call-community
source_url: "https://github.com/phe-bioinformatics/PHEnix"
---

## Concepts

- **Tool Overview**: phenix calls SNPs for public health.
- **Core Function**: SNP calling pipeline.
- **Algorithm**: Uses variant calling methods.
- **Input Format**: Accepts sequencing data files.
- **Output**: Produces SNP variant calls.
- **Use Case**: SNP calling, public health analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Genome**: Requires proper reference genome.
- **SNP Calling**: May miss low-frequency variants.
- **Runtime**: Calling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phenix --help`
**Explanation:** Shows available options and usage instructions.

### Call SNPs
**Args:** `phenix -i reads.fastq -r ref.fasta -o snps.vcf`
**Explanation:** Calls SNPs from sequencing data.

### With config
**Args:** `phenix -i reads.fastq -r ref.fasta -c config.yaml -o snps.vcf`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `phenix -v -i reads.fastq -r ref.fasta -o snps.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phenix -t 4 -i reads.fastq -r ref.fasta -o snps.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phenix -i reads.fastq -r ref.fasta -o snps.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phenix -i reads.fastq -r ref.fasta -o snps.vcf --report report.html`
**Explanation:** Generates HTML report.