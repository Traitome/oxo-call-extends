---
name: kestrel
category: alignment
description: Mapping-free variant caller for short-read Illumina data.
tags: [kestrel, alignment, variant calling, mapping-free, Illumina]
author: oxo-call-community
source_url: "https://github.com/paudano/kestrel"
---

## Concepts

- **Tool Overview**: kestrel (v1.0.3) - Mapping-free variant caller for Illumina reads.
- **Mapping-Free**: Calls variants without read mapping.
- **k-mer Based**: Uses k-mer analysis for variant detection.
- **Speed**: Faster than mapping-based callers.
- **Illumina Support**: Optimized for Illumina short reads.
- **VCF Output**: Generates standard VCF output.

## Pitfalls

- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Memory Usage**: Requires significant memory.
- **False Positives**: Can produce false positive calls.
- **Indel Detection**: Limited indel detection capability.
- **Reference Genome**: Needs reference genome.
- **Read Length**: Performance varies with read length.

## Examples

### Call variants
**Args:** `kestrel -i reads.fastq -r ref.fasta -o variants.vcf`
**Explanation:** Calls variants without mapping.

### Set k-mer size
**Args:** `kestrel -i reads.fastq -r ref.fasta -k 31 -o variants.vcf`
**Explanation:** Uses k-mer size of 31.

### Paired-end mode
**Args:** `kestrel -i reads_1.fastq -j reads_2.fastq -r ref.fasta -o variants.vcf`
**Explanation:** Processes paired-end reads.

### Quality filtering
**Args:** `kestrel -i reads.fastq -r ref.fasta -o variants.vcf -q 30`
**Explanation:** Filters variants by quality >= 30.

### Verbose mode
**Args:** `kestrel -i reads.fastq -r ref.fasta -o variants.vcf -v`
**Explanation:** Shows verbose output during calling.

### Batch processing
**Args:** `kestrel batch -i samples.txt -r ref.fasta -o output/`
**Explanation:** Processes multiple samples in batch.