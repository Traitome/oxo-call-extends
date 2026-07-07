---
name: sccaller
category: variant-calling
description: SCcaller - Accurate identification of single-nucleotide variants in whole-genome-amplified single cells
tags: ["sccaller", "variant-calling", "single-cell", "SNV"]
author: oxo-call-community
source_url: "https://github.com/biosinodx/SCcaller"
---

## Concepts

- **Tool Overview**: SCcaller (v2.0.0) is a tool for accurate identification of single-nucleotide variants in whole-genome-amplified single cells.
- **Core Function**: Calls SNVs from single-cell sequencing data with high accuracy.
- **Algorithm**: Uses statistical models to distinguish true variants from amplification artifacts.
- **Input/Output**: Accepts BAM files and reference genome, produces VCF with SNV calls.
- **Single-Cell Focus**: Specifically designed for whole-genome-amplified single cell data.
- **Applications**: Single-cell variant calling, cancer genomics, and somatic mutation detection.

## Pitfalls

- **Amplification Bias**: WGA artifacts can affect variant calling.
- **Read Depth**: Requires sufficient sequencing depth per cell.
- **Allelic Dropout**: May miss heterozygous variants due to dropout.
- **Reference Genome**: Results depend on reference quality.
- **Computational Resources**: High memory and CPU requirements.
- **False Positives**: May report false variants from amplification errors.

## Examples

### Basic variant calling
**Args:** `sccaller -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** `-i` input BAM; `-r` reference genome; `-o` output VCF.

### With quality filtering
**Args:** `sccaller -i aligned.bam -r reference.fasta -q 20 -o variants.vcf`
**Explanation:** `-q 20` filters variants with quality below 20.

### Targeted regions
**Args:** `sccaller -i aligned.bam -r reference.fasta -t targets.bed -o variants.vcf`
**Explanation:** `-t` BED file with target regions.

### Multiple cells
**Args:** `sccaller -i cell1.bam cell2.bam -r reference.fasta -o variants.vcf`
**Explanation:** Processes multiple single-cell BAM files.

### Verbose logging
**Args:** `sccaller -i aligned.bam -r reference.fasta -v -o variants.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Output statistics
**Args:** `sccaller -i aligned.bam -r reference.fasta -s stats.txt -o variants.vcf`
**Explanation:** `-s` outputs variant calling statistics.

### Minimum coverage
**Args:** `sccaller -i aligned.bam -r reference.fasta -c 5 -o variants.vcf`
**Explanation:** `-c 5` requires minimum 5 reads per variant.