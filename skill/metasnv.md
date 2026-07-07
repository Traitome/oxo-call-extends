---
name: metasnv
category: variant-calling
description: SNV calling software
tags: [metasnv, variant-calling, SNV]
author: oxo-call-community
source_url: "http://metasnv.embl.de"
---

## Concepts

- **Tool Overview**: MetaSNV v2.0.4 is a software tool for calling single nucleotide variants (SNVs) from sequencing data.
- **Core Function**: Identifies single nucleotide variations in genomic sequences.
- **SNV Detection**: Detects point mutations and single base changes in sequencing data.
- **Accuracy**: Designed for high-accuracy variant calling from various sequencing platforms.
- **Input/Output**: Accepts BAM/CRAM files; outputs VCF files with variant calls.
- **Quality Filtering**: Includes quality filtering to reduce false positive calls.

## Pitfalls

- **Coverage Depth**: Requires sufficient coverage depth for accurate SNV calling.
- **Mapping Quality**: Poor mapping quality can affect variant calling accuracy.
- **False Positives**: May produce false positive SNV calls.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Indel Handling**: May have difficulty distinguishing SNVs from small indels.

## Examples

### Call SNVs
**Args:** `metasnv -i alignment.bam -o variants.vcf`
**Explanation:** Calls single nucleotide variants from aligned reads.

### With quality filtering
**Args:** `metasnv -i alignment.bam -o variants.vcf -q 30`
**Explanation:** Applies minimum quality score filter of 30.

### Targeted calling
**Args:** `metasnv -i alignment.bam -o variants.vcf -t targets.bed`
**Explanation:** Limits variant calling to specified genomic regions.

### Output statistics
**Args:** `metasnv -i alignment.bam -o variants.vcf -s stats.txt`
**Explanation:** Generates variant calling statistics.

### Batch processing
**Args:** `metasnv -i bam/ -o vcf/`
**Explanation:** Processes multiple BAM files in batch mode.