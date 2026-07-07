---
name: novasplice
category: population-genomics
description: NovaSplice predicts novel intronic splice sites from VCF variant data.
tags: [novasplice, population-genomics, splice-sites, variant-analysis]
author: oxo-call-community
source_url: "https://github.com/aryakaul/novasplice"
---

## Concepts

- **Tool Overview**: NovaSplice predicts novel intronic splice sites from VCF files.
- **Core Function**: Identifies potential splice-altering variants in intronic regions.
- **Algorithm**: Uses sequence analysis to predict splice site creation/destruction.
- **Input Format**: Accepts VCF files with variant calls.
- **Output**: Produces predicted splice sites and their effects.
- **Use Case**: Variant interpretation, splicing analysis, and functional genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **VCF Quality**: Results depend on variant call quality.
- **Reference Genome**: Requires matching reference genome.
- **False Positives**: May predict non-functional splice sites.
- **Validation**: Predictions should be experimentally validated.
- **Intronic Focus**: Focuses on intronic variants only.

## Examples

### Display help
**Args:** `novasplice --help`
**Explanation:** Shows available options and usage instructions.

### Predict splice sites
**Args:** `novasplice -i variants.vcf -o splice_sites.txt`
**Explanation:** Predicts novel splice sites from VCF.

### With reference
**Args:** `novasplice -i variants.vcf -r reference.fasta -o splice_sites.txt`
**Explanation:** Uses reference genome for analysis.

### Output VCF
**Args:** `novasplice -i variants.vcf -o annotated.vcf --vcf-output`
**Explanation:** Outputs annotated VCF with splice predictions.

### Score threshold
**Args:** `novasplice -i variants.vcf -o splice_sites.txt -s 0.8`
**Explanation:** Sets minimum prediction score threshold.

### Include existing sites
**Args:** `novasplice -i variants.vcf -o splice_sites.txt --include-existing`
**Explanation:** Includes known splice sites in analysis.

### Threads
**Args:** `novasplice -i variants.vcf -t 8 -o splice_sites.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `novasplice -i variants.vcf -v -o splice_sites.txt`
**Explanation:** Runs with verbose output.