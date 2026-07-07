---
name: sneep
category: variant-analysis
description: SNEEP - Identify regulatory non-coding SNPs (rSNPs) from sequencing data
tags: [sneep, variant-analysis, regulatory-snps, non-coding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/SchulzLab/SNEEP"
---

## Concepts

- **Tool Overview**: sneep (v1.1) - A tool for identifying regulatory non-coding SNPs
- **Core Function**: Detects regulatory SNPs in non-coding regions
- **Input/Output**: Accepts BAM/VCF files; outputs annotated rSNPs
- **Algorithm**: Analyzes non-coding regions for regulatory potential
- **Installation**: `conda install -c bioconda sneep`
- **Key Features**: rSNP detection, regulatory annotation, non-coding analysis

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM files
- **Reference Genome**: Must use compatible reference genome
- **Annotation Files**: Requires regulatory annotation files
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `sneep --help`
**Explanation:** Shows available options and usage information.

### Basic rSNP detection
**Args:** `sneep -i variants.vcf -r reference.fasta -o rsnp_results.txt`
**Explanation:** Detect regulatory SNPs from VCF file.

### With BAM input
**Args:** `sneep -i aligned.bam -r reference.fasta -o rsnp_results.txt`
**Explanation:** Detect rSNPs directly from BAM file.

### With annotation
**Args:** `sneep -i variants.vcf -r reference.fasta -a annotations.gff -o rsnp_results.txt`
**Explanation:** Use regulatory annotations for analysis.

### With regulatory database
**Args:** `sneep -i variants.vcf -r reference.fasta -db regulatory_db.bed -o rsnp_results.txt`
**Explanation:** Use custom regulatory database.

### Filter by score
**Args:** `sneep -i variants.vcf -r reference.fasta -o rsnp_results.txt --min-score 0.8`
**Explanation:** Filter results by minimum regulatory score.

### Generate report
**Args:** `sneep -i variants.vcf -r reference.fasta -o rsnp_results.txt --report`
**Explanation:** Generate comprehensive analysis report.

### Export to VCF
**Args:** `sneep -i variants.vcf -r reference.fasta -o rsnp_results.vcf --vcf`
**Explanation:** Output results in VCF format.