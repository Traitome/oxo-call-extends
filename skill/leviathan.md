---
name: leviathan
category: variant-calling
description: Linked-reads based structural variant caller with barcode indexing
tags: [leviathan, variant-calling, structural-variants, linked-reads, barcode]
author: oxo-call-community
source_url: "https://github.com/morispi/LEVIATHAN"
---

## Concepts

- **Linked-reads**: Uses linked-read sequencing data for SV detection
- **Barcode Indexing**: Leverages barcode information for phasing
- **Structural Variants**: Detects large-scale structural variations
- **Phased Analysis**: Enables phased variant calling
- **SV Calling**: Identifies deletions, duplications, inversions, translocations
- **Hi-C Support**: Works with Hi-C and linked-read technologies

## Pitfalls

- **Barcode Quality**: Poor barcode quality affects phasing
- **Read Coverage**: Low coverage affects SV detection sensitivity
- **Complex Regions**: Repeat regions may cause false positives
- **Computational Resources**: Requires significant memory and CPU
- **Library Preparation**: Library quality affects results
- **SV Size**: Very small or very large SVs may be missed

## Examples

### Call SVs
**Args:** `leviathan -b aligned.bam -o sv_calls.vcf`
**Explanation:** Calls structural variants from linked-read BAM.

### Specify barcode file
**Args:** `leviathan -b aligned.bam -c barcodes.txt -o sv_calls.vcf`
**Explanation:** Uses external barcode information.

### Set minimum SV size
**Args:** `leviathan -b aligned.bam -m 500 -o sv_calls.vcf`
**Explanation:** Only reports SVs >= 500bp.

### Phased output
**Args:** `leviathan -b aligned.bam -p -o phased_sv.vcf`
**Explanation:** Outputs phased structural variants.

### Generate statistics
**Args:** `leviathan -b aligned.bam -o sv_calls.vcf --stats`
**Explanation:** Generates SV calling statistics.

### Batch processing
**Args:** `leviathan batch -d bams/ -o results/`
**Explanation:** Processes multiple BAM files.