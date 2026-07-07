---
name: regtools
category: variant-calling
description: RegTools integrates DNA-seq and RNA-seq data to interpret mutations in regulatory and splicing contexts.
tags: [regtools, variant-calling, rna-seq, dna-seq]
author: oxo-call-community
source_url: "https://regtools.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: regtools analyzes mutations.
- **Core Function**: Variant interpretation.
- **Algorithm**: Uses integration methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces variant annotations.
- **Use Case**: Variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `regtools --help`
**Explanation:** Shows available options and usage instructions.

### Junction analysis
**Args:** `regtools junctions extract -i rna.bam -o junctions.bed`
**Explanation:** Extracts splice junctions.

### With parameters
**Args:** `regtools junctions extract -i rna.bam -p params.yaml -o junctions.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `regtools -v junctions extract -i rna.bam -o junctions.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `regtools -t 4 junctions extract -i rna.bam -o junctions.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Variant effect
**Args:** `regtools variants effect -i variants.vcf -r reference.fasta -o effects.txt`
**Explanation:** Analyzes variant effects.

### Generate report
**Args:** `regtools junctions extract -i rna.bam -o junctions.bed --report report.html`
**Explanation:** Generates HTML report.