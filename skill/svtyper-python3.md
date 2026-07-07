---
name: svtyper-python3
category: variant-calling
description: Python3-compatible Bayesian genotyper for structural variants.
tags: [svtyper-python3, structural-variants, genotyping, bayesian]
author: oxo-call-community
source_url: "https://github.com/hall-lab/svtyper"
---

## Concepts

- **Tool Overview**: svtyper-python3 (v0.7.1) is the Python3 version of svtyper.
- **Core Function**: Determines genotypes of known structural variants using Bayesian methods.
- **Algorithm**: Uses Bayesian statistical modeling for accurate genotyping.
- **Input/Output**: Input: BAM file, SV VCF, reference genome; Output: Genotyped VCF.
- **Applications**: SV genotyping, population genetics, variant validation.
- **Installation**: `conda install -c bioconda svtyper-python3` or download from GitHub.

## Pitfalls

- **Python Version**: Requires Python 3.x environment.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Genotyping large SV sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect accuracy.
- **Input Quality**: Requires high-quality SV calls as input.
- **Alignment Quality**: Requires well-aligned BAM files.

## Examples

### Display help
**Args:** `svtyper-python3 --help`
**Explanation:** Shows available options and usage information.

### Basic SV genotyping
**Args:** `svtyper-python3 -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype SVs using Bayesian model.

### With multiple samples
**Args:** `svtyper-python3 -i samples.txt -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype multiple samples together.

### Verbose mode
**Args:** `svtyper-python3 -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svtyper-python3 -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --stats`
**Explanation:** Generate statistics about genotyping.

### Batch processing
**Args:** `svtyper-python3 -i bams/ -v sv.vcf -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svtyper-python3 -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -q 0.9`
**Explanation:** Filter by confidence score.

### Include phasing
**Args:** `svtyper-python3 -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --phase`
**Explanation:** Include phasing information.

### Generate report
**Args:** `svtyper-python3 -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --report`
**Explanation:** Generate comprehensive HTML report.
