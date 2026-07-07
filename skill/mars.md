---
name: mars
category: alignment
description: Multiple Alignment-based Refinement of SVs (MARS)
tags: [mars, alignment, structural-variants]
author: oxo-call-community
source_url: "https://github.com/maiziex/MARS"
---

## Concepts

- **Tool Overview**: mars v1.2.4 - MARS (Multiple Alignment-based Refinement of SVs) refines structural variant calls using multiple sequence alignments.
- **Core Function**: Improves structural variant calling accuracy by using multiple sequence alignments.
- **Input/Output**: Input: VCF file, reference genome; Output: Refined VCF with improved SV calls.
- **Installation**: `conda install -c bioconda mars`
- **SV Refinement**: Refines structural variant calls using alignment information.
- **Multiple Alignments**: Uses multiple sequence alignments for improved accuracy.

## Pitfalls

- **VCF Quality**: Poor quality SV calls affect refinement.
- **Reference Genome**: Must use appropriate reference genome.
- **Memory Usage**: Large datasets require significant memory.
- **Computational Time**: Complex analyses may take time.
- **False Positives**: May introduce false positive SV calls.
- **Parameter Tuning**: Incorrect parameters affect refinement.

## Examples

### Refine SV calls
**Args:** `mars -i sv_calls.vcf -r ref.fa -o refined.vcf`
**Explanation:** Refines structural variant calls using alignment.

### With BAM file
**Args:** `mars -i sv_calls.vcf -r ref.fa -b aligned.bam -o refined.vcf`
**Explanation:** Uses BAM file for additional alignment information.

### Multiple samples
**Args:** `mars -i sv_calls.vcf -r ref.fa -o refined.vcf --multi-sample`
**Explanation:** Processes multiple samples.

### Verbose mode
**Args:** `mars -i sv_calls.vcf -r ref.fa -o refined.vcf -v`
**Explanation:** Provides detailed logging during analysis.

### Generate report
**Args:** `mars -i sv_calls.vcf -r ref.fa -o refined.vcf --report`
**Explanation:** Generates refinement report.

### Custom parameters
**Args:** `mars -i sv_calls.vcf -r ref.fa -o refined.vcf -p params.json`
**Explanation:** Uses custom parameter file.