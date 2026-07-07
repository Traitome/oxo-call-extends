---
name: metasv
category: variant-calling
description: An accurate and integrative structural-variant caller for next generation sequencing
tags: [metasv, variant-calling, structural-variants]
author: oxo-call-community
source_url: "https://github.com/bioinform/metasv"
---

## Concepts

- **Tool Overview**: MetaSV v0.5.4 is an accurate and integrative structural variant caller for next-generation sequencing data.
- **Core Function**: Detects and characterizes structural variants (SVs) including deletions, duplications, inversions, and translocations.
- **Integrative Calling**: Combines evidence from multiple sources for improved SV detection accuracy.
- **Multi-platform Support**: Works with data from various sequencing platforms including Illumina, PacBio, and Oxford Nanopore.
- **Input/Output**: Accepts BAM files and variant calls; outputs VCF files with structural variant calls.
- **Accuracy**: Designed for high-accuracy structural variant detection.

## Pitfalls

- **Complex Variants**: May struggle with complex structural variants.
- **Coverage Depth**: Requires sufficient coverage depth for accurate SV calling.
- **False Positives**: May produce false positive SV calls.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.

## Examples

### Call structural variants
**Args:** `metasv -i alignment.bam -o sv.vcf`
**Explanation:** Calls structural variants from aligned reads.

### Integrate multiple callers
**Args:** `metasv -i alignment.bam -o sv.vcf --integrate callers.txt`
**Explanation:** Integrates calls from multiple variant callers.

### With quality filtering
**Args:** `metasv -i alignment.bam -o sv.vcf -q 30`
**Explanation:** Applies minimum quality score filter of 30.

### Targeted calling
**Args:** `metasv -i alignment.bam -o sv.vcf -t targets.bed`
**Explanation:** Limits SV calling to specified genomic regions.

### Batch processing
**Args:** `metasv -i bam/ -o vcf/`
**Explanation:** Processes multiple BAM files in batch mode.