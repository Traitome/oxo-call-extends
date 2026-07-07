---
name: pindel
category: variant-calling
description: pindel detects structural variants from next-gen sequence data.
tags: [pindel, variant-calling, structural-variants, sv]
author: oxo-call-community
source_url: "http://gmt.genome.wustl.edu/packages/pindel/index.html"
---

## Concepts

- **Tool Overview**: pindel detects structural variants.
- **Core Function**: Structural variant calling.
- **Algorithm**: Uses split-read mapping methods.
- **Input Format**: Accepts FASTA and BAM files.
- **Output**: Produces SV detection results.
- **Use Case**: Variant calling, structural analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Mapping Quality**: Results depend on mapping quality.
- **SV Detection**: May miss or misidentify variants.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pindel --help`
**Explanation:** Shows available options and usage instructions.

### Detect structural variants
**Args:** `pindel -i input.bam -f reference.fasta -o sv_results.txt`
**Explanation:** Detects structural variants from sequencing data.

### With parameters
**Args:** `pindel -i input.bam -f reference.fasta -p params.yaml -o sv_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pindel -v -i input.bam -f reference.fasta -o sv_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pindel -t 4 -i input.bam -f reference.fasta -o sv_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pindel -i input.bam -f reference.fasta -o sv_results.vcf --vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `pindel -i input.bam -f reference.fasta -o sv_results.txt --report report.html`
**Explanation:** Generates HTML report.