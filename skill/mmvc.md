---
name: mmvc
category: variant-calling
description: Call variants based on a Bayesian multinomial mixture model.
tags: [mmvc, variant-calling, bayesian]
author: oxo-call-community
source_url: "https://github.com/veg/mmvc"
---

## Concepts

- **Tool Overview**: mmvc v1.0.2 calls variants using Bayesian multinomial mixture model.
- **Core Function**: Identifies genetic variants using statistical modeling.
- **Bayesian Approach**: Uses Bayesian inference for variant calling.
- **Multinomial Mixture**: Models allele frequencies as mixture distributions.
- **Input/Output**: Accepts aligned reads; outputs variant calls.
- **Variant Detection**: Supports SNV and INDEL calling.

## Pitfalls

- **Computational Resources**: Bayesian inference may require significant resources.
- **Memory Requirements**: Memory usage depends on data complexity.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on alignment quality.
- **Model Assumptions**: Relies on statistical model assumptions.
- **Convergence Issues**: May require careful convergence monitoring.

## Examples

### Call variants
**Args:** `mmvc -i alignments.bam -g genome.fasta -o variants.vcf`
**Explanation:** Calls variants using Bayesian model.

### With prior knowledge
**Args:** `mmvc -i alignments.bam -g genome.fasta -p prior.txt -o variants.vcf`
**Explanation:** Uses custom prior probabilities.

### Verbose output
**Args:** `mmvc -i alignments.bam -g genome.fasta -v -o variants.vcf`
**Explanation:** Shows detailed variant calling process.

### Filter variants
**Args:** `mmvc -i alignments.bam -g genome.fasta -f 0.05 -o variants.vcf`
**Explanation:** Applies quality filtering threshold.

### Batch processing
**Args:** `mmvc -i bam/ -g genome.fasta -o vcfs/`
**Explanation:** Processes multiple BAM files.