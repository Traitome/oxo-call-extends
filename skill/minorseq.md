---
name: minorseq
category: variant-calling
description: Minor Variant Calling and Phasing Tools
tags: [minorseq, variant-calling, phasing]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: MinorSeq v1.12.0 calls and phases minor genetic variants.
- **Core Function**: Identifies and phases low-frequency genetic variants.
- **Minor Variant Calling**: Detects variants present at low frequencies.
- **Variant Phasing**: Determines haplotype phase of variants.
- **Input/Output**: Accepts sequencing data; outputs variant calls.
- **PacBio Support**: Optimized for PacBio sequencing data.

## Pitfalls

- **PacBio Specific**: Optimized for PacBio sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Calling accuracy depends on input data quality.
- **Frequency Threshold**: Choice of frequency threshold affects results.

## Examples

### Call minor variants
**Args:** `minorseq -i alignments.bam -o variants.vcf`
**Explanation:** Calls minor variants from BAM file.

### With phasing
**Args:** `minorseq -i alignments.bam -o variants.vcf -p`
**Explanation:** Calls and phases variants.

### Custom frequency threshold
**Args:** `minorseq -i alignments.bam -o variants.vcf -t 0.01`
**Explanation:** Uses 1% frequency threshold.

### Batch processing
**Args:** `minorseq -i bam/ -o vcfs/`
**Explanation:** Processes multiple BAM files.

### Generate statistics
**Args:** `minorseq -i alignments.bam -o variants.vcf -s stats.txt`
**Explanation:** Generates variant calling statistics.