---
name: optitype
category: utility
description: OptiType performs precision HLA typing from next-generation sequencing data.
tags: [optitype, utility, hla-typing, immunogenetics]
author: oxo-call-community
source_url: "https://github.com/FRED-2/OptiType"
---

## Concepts

- **Tool Overview**: OptiType determines HLA genotypes from sequencing data.
- **Core Function**: Performs high-resolution HLA typing.
- **Algorithm**: Uses integer linear programming for allele calling.
- **Input Format**: Accepts BAM, FASTQ, or VCF files.
- **Output**: Produces HLA allele calls with confidence scores.
- **Use Case**: Immunogenetics, transplantation, and population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Coverage**: Requires sufficient sequencing coverage.
- **Ambiguity**: May report ambiguous allele calls.
- **Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `optitype --help`
**Explanation:** Shows available options and usage instructions.

### Run HLA typing
**Args:** `optitype -i reads.fastq -o hla_results.txt`
**Explanation:** Performs HLA typing from FASTQ reads.

### With BAM input
**Args:** `optitype -i alignments.bam -o hla_results.txt`
**Explanation:** Uses BAM file for typing.

### High resolution
**Args:** `optitype -i reads.fastq -h -o hla_results.txt`
**Explanation:** Outputs high-resolution alleles.

### Verbose mode
**Args:** `optitype -i reads.fastq -v -o hla_results.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `optitype batch -d fastqs/ -o results/`
**Explanation:** Processes multiple samples.

### Confidence threshold
**Args:** `optitype -i reads.fastq -c 0.9 -o hla_results.txt`
**Explanation:** Sets confidence threshold.