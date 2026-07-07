---
name: get_mnv
category: variant-calling
description: get_mnv - Tool to identify Multi-Nucleotide Variants (MNVs) in genomic sequences.
tags: [get_mnv, variant-calling, MNV, genomic-variants]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/get_mnv"
---

## Concepts
- **MNV Detection**: Identifies multi-nucleotide variants.
- **Variant Calling**: Calls variants from sequencing data.
- **SNP Analysis**: Analyzes single nucleotide polymorphisms.
- **Indel Detection**: Detects insertions and deletions.
- **Genomic Variation**: Analyzes genomic variation.

## Pitfalls
- **Input Quality**: Requires high-quality sequencing data.
- **Mapping Quality**: Depends on read mapping quality.
- **False Positives**: May detect false MNVs.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Validation**: Results should be validated.

## Examples
### Call MNVs
**Args:** `get_mnv -i variants.vcf -o mnvs.vcf`
**Explanation:** Identifies MNVs from VCF file.

### With BAM input
**Args:** `get_mnv -b aligned.bam -r genome.fasta -o mnvs.vcf`
**Explanation:** Calls MNVs directly from BAM file.

### Filter by quality
**Args:** `get_mnv -i variants.vcf -q 30 -o mnvs.vcf`
**Explanation:** Filters MNVs by quality score.

### Batch processing
**Args:** `get_mnv -l vcfs.txt -o ./mnvs/`
**Explanation:** Processes multiple VCF files.

### Generate report
**Args:** `get_mnv -i variants.vcf -r -o report.html`
**Explanation:** Generates MNV detection report.