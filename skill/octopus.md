---
name: octopus
category: variant-calling
description: Octopus is a mapping-based variant caller with haplotype-aware variant calling framework.
tags: [octopus, variant-calling, haplotype, snp-calling]
author: oxo-call-community
source_url: "https://github.com/luntergroup/octopus"
---

## Concepts

- **Tool Overview**: Octopus calls variants from aligned sequencing data using haplotype-aware methods.
- **Core Function**: Detects SNPs, indels, and complex variants from BAM files.
- **Algorithm**: Uses Bayesian haplotype estimation for variant calling.
- **Input Format**: Accepts BAM alignment files and FASTA reference sequences.
- **Output**: Produces VCF files with variant calls and genotypes.
- **Use Case**: Variant calling, population genetics, and clinical genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require significant memory.
- **Computational Cost**: Variant calling can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Reference Quality**: Results depend on reference sequence quality.
- **Validation**: Results should be validated with other callers.

## Examples

### Display help
**Args:** `octopus --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `octopus -R reference.fasta -I alignments.bam -O variants.vcf`
**Explanation:** Calls variants from BAM file.

### Multiple samples
**Args:** `octopus -R reference.fasta -I sample1.bam sample2.bam -O variants.vcf`
**Explanation:** Calls variants from multiple samples.

### Targeted sequencing
**Args:** `octopus -R reference.fasta -I alignments.bam -T targets.bed -O variants.vcf`
**Explanation:** Calls variants in specific target regions.

### Output genotype likelihoods
**Args:** `octopus -R reference.fasta -I alignments.bam -O variants.vcf --emit-gl`
**Explanation:** Outputs genotype likelihoods.

### Threads
**Args:** `octopus -R reference.fasta -I alignments.bam -O variants.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `octopus -R reference.fasta -I alignments.bam -O variants.vcf --verbose`
**Explanation:** Runs with verbose output.