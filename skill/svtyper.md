---
name: svtyper
category: variant-calling
description: Bayesian genotyper for structural variants using statistical modeling.
tags: [svtyper, structural-variants, genotyping, bayesian]
author: oxo-call-community
source_url: "https://github.com/hall-lab/svtyper"
---

## Concepts

- **Tool Overview**: svtyper (v0.7.1) genotypes structural variants using Bayesian methods.
- **Core Function**: Determines genotypes of known structural variants.
- **Algorithm**: Uses Bayesian statistical modeling for accurate genotyping.
- **Input/Output**: Input: BAM file, SV VCF, reference genome; Output: Genotyped VCF.
- **Applications**: SV genotyping, population genetics, variant validation.
- **Installation**: `conda install -c bioconda svtyper` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Genotyping large SV sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect accuracy.
- **Input Quality**: Requires high-quality SV calls as input.
- **Alignment Quality**: Requires well-aligned BAM files.
- **SV Complexity**: Complex SVs may be difficult to genotype.

## Examples

### Display help
**Args:** `svtyper --help`
**Explanation:** Shows available options and usage information.

### Basic SV genotyping
**Args:** `svtyper -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype SVs using Bayesian model.

### With multiple samples
**Args:** `svtyper -i samples.txt -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype multiple samples together.

### Verbose mode
**Args:** `svtyper -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svtyper -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --stats`
**Explanation:** Generate statistics about genotyping.

### Batch processing
**Args:** `svtyper -i bams/ -v sv.vcf -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svtyper -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -q 0.9`
**Explanation:** Filter by confidence score.

### Include phasing
**Args:** `svtyper -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --phase`
**Explanation:** Include phasing information.

### Generate report
**Args:** `svtyper -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --report`
**Explanation:** Generate comprehensive HTML report.
