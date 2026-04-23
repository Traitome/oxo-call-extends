---
name: mutserve
category: variant-calling
description: Mutserve2 is a variant caller for the mitochondrial genome to detect homoplasmic and heteroplasmic sites in sequence data.
tags: [mutserve, variant-calling, mitochondrial, heteroplasmy, homoplasmy]
author: oxo-call-community
source_url: "https://github.com/seppinho/mutserve"
---

## Concepts

- **Tool Overview**: Mutserve2 v2.0.3 - variant caller for the mitochondrial genome detecting homoplasmic and heteroplasmic sites.
- **Core Function**: Calls mitochondrial DNA variants, distinguishing between homoplasmic and heteroplasmic sites.
- **Input/Output**: Takes BAM files aligned to mitochondrial reference (e.g., rCRS); outputs VCF with variant calls.
- **Installation**: `conda install -c bioconda mutserve`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure BAM files are aligned to the correct mitochondrial reference (rCRS recommended).

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Variant calling
**Args:** `call --reference rCRS.fasta --output output.vcf.gz --threads 4 *.bam`
**Explanation:** Calls mitochondrial variants from BAM files.

### Variant annotation
**Args:** `annotate --input variantfile.txt --annotation rCRS_annotation.txt --output AnnotatedVariants.txt`
**Explanation:** Annotates mitochondrial variants using reference annotation.
