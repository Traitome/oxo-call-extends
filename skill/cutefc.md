---
name: cutefc
category: variant-calling
description: Regenotyping structural variants through an accurate and efficient force-calling method
tags: [cutefc, variant-calling, structural-variants, force-calling, re-genotyping]
author: oxo-call-community
source_url: "https://github.com/Meltpinkg/cuteFC"
---

## Concepts

- **Tool Overview**: cutefc (v1.0.2+) is a tool for re-genotyping structural variants using an accurate and efficient force-calling method.
- **Core Function**: Improves structural variant genotyping accuracy by force-calling known variant positions from alignment data.
- **Input/Output**: Input: BAM alignments, reference genome, VCF with known variants. Output: Re-genotyped VCF with improved accuracy.
- **Algorithm**: Uses read depth and split-read analysis to force-call genotypes at known SV positions.
- **Key Features**: Improved genotype accuracy, efficient processing, supports multiple variant types.
- **Installation**: `conda install -c bioconda cutefc`

## Pitfalls

- **VCF Input**: Requires VCF file with known variants for re-genotyping.
- **BAM Index**: BAM files must be indexed for efficient access.
- **Reference Genome**: Must match the reference used for alignment.
- **Memory Usage**: Large datasets may require significant memory.
- **Output Interpretation**: Results should be validated with orthogonal methods.

## Examples

### Re-genotype SVs from BAM
**Args:** `cutefc -i input.bam -r reference.fasta -v known_svs.vcf -o re_genotyped.vcf`
**Explanation:** Re-genotype known structural variants using aligned reads.

### Force-call specific regions
**Args:** `cutefc -i input.bam -r reference.fasta -v svs.vcf -o results.vcf -b regions.bed`
**Explanation:** Limit re-genotyping to specific genomic regions.

### Generate genotype statistics
**Args:** `cutefc -i input.bam -r reference.fasta -v svs.vcf -o results.vcf --stats`
**Explanation:** Generate statistics on genotype quality and confidence.
