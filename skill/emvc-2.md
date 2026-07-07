---
name: emvc-2
category: variant-calling
description: "An efficient SNV variant caller based on the expectation maximization algorithm."
tags: [emvc-2, variant-calling, SNV-calling, EM-algorithm, variant-detection]
author: oxo-call-community
source_url: "https://github.com/guilledufort/EMVC-2"
---

## Concepts

- **Tool Overview**: EMVC-2 is an efficient SNV (Single Nucleotide Variant) caller that uses the expectation-maximization (EM) algorithm for accurate variant detection from sequencing data.
- **Core Function**: Identifies single nucleotide variants from aligned sequencing reads using a probabilistic EM-based approach.
- **Input/Output**: Input: BAM/SAM files (aligned reads), reference FASTA. Output: VCF file with SNV calls and quality scores.
- **Algorithm**: Uses expectation-maximization algorithm to estimate genotype probabilities and call variants with high accuracy.
- **Key Features**: Efficient variant calling, EM-based probability estimation, support for paired-end data, quality filtering, batch processing.
- **Installation**: `conda install -c bioconda emvc-2`

## Pitfalls

- **Reference Compatibility**: Requires matching reference genome version.
- **Alignment Quality**: Poor alignments may lead to false positives.
- **Coverage Depth**: Low coverage regions may have unreliable calls.
- **Parameter Tuning**: EM parameters may need adjustment for specific datasets.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic SNV calling
**Args:** `emvc-2 -i input.bam -r ref.fasta -o variants.vcf`
**Explanation:** Calls SNVs from aligned BAM file.

### With quality filtering
**Args:** `emvc-2 -i input.bam -r ref.fasta -o variants.vcf -q 30`
**Explanation:** Filters variants with quality score below 30.

### Output confidence scores
**Args:** `emvc-2 -i input.bam -r ref.fasta -o variants.vcf -c`
**Explanation:** Outputs confidence scores for each variant call.

### Batch processing
**Args:** `emvc-2 -i samples/ -r ref.fasta -o results/ --batch`
**Explanation:** Processes multiple BAM files in batch mode.

### Specify ploidy
**Args:** `emvc-2 -i input.bam -r ref.fasta -o variants.vcf -p 2`
**Explanation:** Specifies ploidy level (default is diploid).