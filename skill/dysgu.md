---
name: dysgu
category: variant-calling
description: "A collection of tools for calling structural variants using short or long reads."
tags: [dysgu, variant-calling, structural-variants, SV, long-reads, short-reads]
author: oxo-call-community
source_url: "https://github.com/kcleal/dysgu/blob/v1.8.7/README.rst"
---

## Concepts

- **Tool Overview**: Dysgu is a tool for calling structural variants (SVs) from both short and long sequencing reads.
- **Core Function**: Detects deletions, insertions, duplications, inversions, and translocations.
- **Input/Output**: Input: BAM alignment files, reference genome. Output: VCF with structural variant calls.
- **Algorithm**: Uses machine learning and read depth analysis for accurate SV detection.
- **Key Features**: Supports multiple sequencing platforms, high accuracy, genotyping, breakpoint refinement.
- **Installation**: `conda install -c bioconda dysgu`

## Pitfalls

- **Alignment Quality**: Requires high-quality alignments for accurate SV calling.
- **Coverage Depth**: Low coverage reduces sensitivity for SV detection.
- **Reference Genome**: Must use the same reference genome as the alignment.
- **Memory Usage**: Large genomes may require significant RAM.
- **Complex Regions**: Highly repetitive regions may produce false positives.

## Examples

### Call SVs from BAM
**Args:** `dysgu run ref.fa sample.bam > sv.vcf`
**Explanation:** Calls structural variants from aligned reads.

### With genotyping
**Args:** `dysgu run ref.fa sample.bam --genotype > sv.vcf`
**Explanation:** Calls SVs with genotype information.

### Filter by quality
**Args:** `dysgu run ref.fa sample.bam --min-qual 30 > sv.vcf`
**Explanation:** Filters variants by minimum quality score.

### Merge multiple samples
**Args:** `dysgu merge sample1.vcf sample2.vcf > merged.vcf`
**Explanation:** Merges SV calls from multiple samples.

### Use specific SV types
**Args:** `dysgu run ref.fa sample.bam --sv-types DEL,INS > sv.vcf`
**Explanation:** Only calls deletions and insertions.