---
name: orthanq
category: expression
description: Orthanq performs uncertainty-aware HLA typing and haplotype quantification.
tags: [orthanq, expression, hla-typing, haplotype]
author: oxo-call-community
source_url: "https://github.com/orthanq/orthanq"
---

## Concepts

- **Tool Overview**: Orthanq quantifies haplotypes with uncertainty estimates.
- **Core Function**: Performs HLA typing and haplotype quantification.
- **Algorithm**: Uses probabilistic modeling for uncertainty estimation.
- **Input Format**: Accepts sequencing reads or aligned BAM files.
- **Output**: Produces haplotype calls with confidence measures.
- **Use Case**: HLA typing, haplotype analysis, and immunogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Data Quality**: Results depend on sequencing quality.
- **Ambiguity**: May report ambiguous haplotypes.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orthanq --help`
**Explanation:** Shows available options and usage instructions.

### Run HLA typing
**Args:** `orthanq -i reads.fastq -o hla_results.txt`
**Explanation:** Performs HLA typing from reads.

### With BAM input
**Args:** `orthanq -i alignments.bam -o hla_results.txt`
**Explanation:** Uses BAM file for typing.

### Uncertainty output
**Args:** `orthanq -i reads.fastq -u -o hla_results.txt`
**Explanation:** Outputs uncertainty estimates.

### Verbose mode
**Args:** `orthanq -i reads.fastq -v -o hla_results.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `orthanq batch -d fastqs/ -o results/`
**Explanation:** Processes multiple samples.

### Confidence threshold
**Args:** `orthanq -i reads.fastq -c 0.9 -o hla_results.txt`
**Explanation:** Sets confidence threshold.