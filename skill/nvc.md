---
name: nvc
category: variant-calling
description: NVC (Naive Variant Caller) performs simple variant calling from aligned sequencing data.
tags: [nvc, variant-calling, snp-detection, genomics]
author: oxo-call-community
source_url: "https://github.com/blankenberg/nvc"
---

## Concepts

- **Tool Overview**: NVC is a simple variant caller for detecting SNPs and indels.
- **Core Function**: Calls variants from aligned sequencing reads.
- **Algorithm**: Uses straightforward statistical approaches for variant detection.
- **Input Format**: Accepts BAM alignment files and FASTA reference sequences.
- **Output**: Produces VCF files with variant calls.
- **Use Case**: Variant calling, SNP detection, and genetic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Simplistic Approach**: May miss complex variants.
- **No Quality Scores**: Limited quality filtering options.
- **Memory Usage**: Large datasets require memory.
- **False Positives**: May report false variant calls.
- **Validation**: Results should be validated with other callers.

## Examples

### Display help
**Args:** `nvc --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `nvc -r reference.fasta -b alignments.bam -o variants.vcf`
**Explanation:** Calls variants from BAM file.

### Minimum depth
**Args:** `nvc -r reference.fasta -b alignments.bam -d 10 -o variants.vcf`
**Explanation:** Sets minimum coverage depth to 10.

### Minimum quality
**Args:** `nvc -r reference.fasta -b alignments.bam -q 30 -o variants.vcf`
**Explanation:** Sets minimum quality score to 30.

### Output BED
**Args:** `nvc -r reference.fasta -b alignments.bam -o variants.bed --bed`
**Explanation:** Outputs variants in BED format.

### Threads
**Args:** `nvc -r reference.fasta -b alignments.bam -t 8 -o variants.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nvc -r reference.fasta -b alignments.bam -v -o variants.vcf`
**Explanation:** Runs with verbose output.