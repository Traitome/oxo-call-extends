---
name: sv2
category: variant-calling
description: Support Vector Structural Variation Genotyper for accurate SV genotyping.
tags: [sv2, structural-variants, genotyping, machine-learning]
author: oxo-call-community
source_url: "https://github.com/dantaki/SV2"
---

## Concepts

- **Tool Overview**: sv2 (v1.4.3.4) is a Support Vector Machine-based SV genotyper.
- **Core Function**: Genotypes structural variants using machine learning.
- **Algorithm**: Uses support vector machines for accurate SV genotyping.
- **Input/Output**: Input: SV VCF, BAM file; Output: Genotyped VCF.
- **Applications**: Structural variant genotyping, population genetics, clinical genomics.
- **Installation**: `conda install -c bioconda sv2` or download from GitHub.

## Pitfalls

- **Training Data**: Requires training for optimal performance.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Genotyping of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect genotyping accuracy.
- **Input Quality**: Poor quality BAM files affect results.
- **Model Compatibility**: Requires compatible model files.

## Examples

### Display help
**Args:** `sv2 --help`
**Explanation:** Shows available options and usage information.

### Basic SV genotyping
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype SVs from VCF and BAM files.

### With trained model
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -m model.pkl -o genotyped.vcf`
**Explanation:** Use pre-trained model for genotyping.

### Verbose mode
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -o genotyped.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -o genotyped.vcf --stats`
**Explanation:** Generate statistics about genotyping.

### Batch processing
**Args:** `sv2 genotype -i sv.vcf -b bams/ -r reference.fasta -o results/`
**Explanation:** Genotype multiple samples together.

### Filter by quality
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -o genotyped.vcf -q 0.9`
**Explanation:** Filter by genotyping quality score.

### Include phasing
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -o genotyped.vcf --phase`
**Explanation:** Include phasing information.

### Generate report
**Args:** `sv2 genotype -i sv.vcf -b sample.bam -r reference.fasta -o genotyped.vcf --report`
**Explanation:** Generate comprehensive HTML report.
