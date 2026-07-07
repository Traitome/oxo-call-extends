---
name: cutehap
category: variant-calling
description: Haplotype-Aware Structural Variant Detector
tags: [cutehap, variant-calling, structural-variants, haplotype-aware, SV-detection]
author: oxo-call-community
source_url: "https://github.com/Meltpinkg/cuteHap"
---

## Concepts

- **Tool Overview**: cutehap (v1.0.4+) is a haplotype-aware structural variant detector for identifying SVs from sequencing data.
- **Core Function**: Detects structural variants while considering haplotype phase information for improved accuracy.
- **Input/Output**: Input: BAM alignments, reference genome. Output: SV calls with phased genotypes.
- **Algorithm**: Integrates haplotype information with split-read and read-depth analysis for SV detection.
- **Key Features**: Haplotype-aware calling, supports multiple SV types, improved breakend resolution.
- **Installation**: `conda install -c bioconda cutehap`

## Pitfalls

- **Phasing Information**: Requires phased data for full haplotype-aware analysis.
- **BAM Quality**: High-quality alignments are essential for accurate SV detection.
- **Complex Regions**: May struggle with highly repetitive or complex genomic regions.
- **Memory Usage**: Large genomes may require significant memory.
- **Validation**: SV calls should be validated with orthogonal methods.

## Examples

### Detect SVs with haplotype awareness
**Args:** `cutehap -i input.bam -r reference.fasta -o sv_calls.vcf`
**Explanation:** Detect structural variants while considering haplotype information.

### Use phased BAM
**Args:** `cutehap -i phased.bam -r reference.fasta -o phased_svs.vcf --phased`
**Explanation:** Analyze phased alignment data for improved SV detection.

### Specify minimum SV size
**Args:** `cutehap -i input.bam -r reference.fasta -o svs.vcf --min-size 50`
**Explanation:** Detect only SVs larger than 50 base pairs.
