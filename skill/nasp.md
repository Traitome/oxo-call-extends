---
name: nasp
category: variant-calling
description: NASP is an accurate, rapid method for the identification of SNPs in WGS datasets with flexible input and output formats.
tags: [nasp, variant-calling, snp, wgs, identification]
author: oxo-call-community
source_url: "https://github.com/TGenNorth/nasp"
---

## Concepts

- **Tool Overview**: NASP v1.2.1 is a SNP identification tool for whole genome sequencing datasets with flexible input/output support.
- **Core Function**: Identifies single nucleotide polymorphisms (SNPs) from aligned sequencing data with high accuracy.
- **Algorithm**: Uses reference-based alignment analysis to detect variant positions across multiple samples.
- **Input Format**: Accepts BAM files, FASTQ reads, and FASTA reference sequences.
- **Output**: Produces SNP matrices in various formats including VCF, TSV, and Phylip.
- **Use Case**: Population genetics, phylogenetic analysis, and variant discovery in WGS studies.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions.
- **Alignment Quality**: SNP calling accuracy depends on alignment quality.
- **Reference Requirements**: Requires high-quality reference genome.
- **Memory Usage**: Processing large datasets requires significant memory.
- **Multi-sample Analysis**: Batch processing requires careful configuration.
- **Output Format**: Default output may need conversion for specific downstream tools.

## Examples

### Display help
**Args:** `nasp --help`
**Explanation:** Shows available options and usage instructions.

### Basic SNP calling
**Args:** `nasp -r reference.fasta -i aligned.bam -o snp_matrix.tsv`
**Explanation:** Identifies SNPs from WGS alignment data.

### Multiple samples
**Args:** `nasp -r ref.fasta -i sample1.bam sample2.bam -o multi_sample_snps.tsv`
**Explanation:** Calls SNPs across multiple aligned samples.

### Output VCF format
**Args:** `nasp -r ref.fasta -i aligned.bam --vcf -o variants.vcf`
**Explanation:** Outputs SNPs in VCF format.

### Quality filtering
**Args:** `nasp -r ref.fasta -i aligned.bam -q 30 -o high_quality_snps.tsv`
**Explanation:** Filters SNPs with minimum quality score of Q30.

### Threads
**Args:** `nasp -r ref.fasta -i aligned.bam -t 8 -o snps.tsv`
**Explanation:** Uses 8 threads for parallel processing.