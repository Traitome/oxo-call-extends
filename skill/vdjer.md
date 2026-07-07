---
name: vdjer
category: bioinformatics
description: vdjer - Variant detection tool.
tags: [vdjer, variant-calling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vdjer/"
---

## Concepts

- **Tool Overview**: vdjer - Variant detection in sequencing data.
- **Core Function**: Detects variants from sequencing reads.
- **Input**: BAM/FASTQ files.
- **Output**: VCF file.
- **Installation**: Install via pip or conda
- **Use Case**: Variant calling, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Accuracy**: Results depend on read quality.

## Examples

### Call variants
**Args:** `vdjer -i input.bam -r ref.fasta -o variants.vcf`
**Explanation:** Call variants.

### With options
**Args:** `vdjer -i input.bam -r ref.fasta -o variants.vcf -t 8`
**Explanation:** Use 8 threads.
